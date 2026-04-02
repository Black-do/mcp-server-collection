#!/usr/bin/env python3
from mcp.server.fastmcp import FastMCP
import json
import os
from datetime import datetime

mcp = FastMCP("DatabaseClient")

# 配置文件路径
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "db_config.json")

def _load_config() -> dict:
    """加载数据库配置"""
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"配置文件不存在：{CONFIG_PATH}")
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _get_connection(db_name: str = None) -> dict:
    """获取数据库连接配置"""
    config = _load_config()
    if db_name is None:
        db_name = config.get("default", list(config["connections"].keys())[0])
    if db_name not in config["connections"]:
        raise ValueError(f"数据库 '{db_name}' 未配置，可用：{list(config['connections'].keys())}")
    return config["connections"][db_name]

@mcp.tool()
def list_databases() -> str:
    """列出所有配置的数据库"""
    try:
        config = _load_config()
        lines = [f"默认数据库：{config.get('default', '无')}"]
        lines.append("\n可用数据库：")
        for name, conn in config["connections"].items():
            default_mark = " (默认)" if name == config.get("default") else ""
            lines.append(f"  - {name}: {conn.get('name', '')} [{conn['type']}]@{conn['host']}:{conn['port']}{default_mark}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def get_tables(db_name: str = None) -> str:
    """获取所有表名"""
    try:
        conn_config = _get_connection(db_name)
        db_type = conn_config["type"]
        
        if db_type == "postgresql":
            import asyncpg
            conn = await asyncpg.connect(
                host=conn_config["host"],
                port=conn_config["port"],
                database=conn_config["database"],
                user=conn_config["user"],
                password=conn_config["password"]
            )
            tables = await conn.fetch("""
                SELECT table_name FROM information_schema.tables 
                WHERE table_schema = 'public'
            """)
            await conn.close()
            return f"数据库 [{db_name or conn_config['database']}] 的表:\n" + "\n".join([t["table_name"] for t in tables])
        
        elif db_type == "mysql":
            import aiomysql
            conn = await aiomysql.connect(
                host=conn_config["host"],
                port=conn_config["port"],
                db=conn_config["database"],
                user=conn_config["user"],
                password=conn_config["password"]
            )
            async with conn.cursor() as cursor:
                await cursor.execute("SHOW TABLES")
                tables = await cursor.fetchall()
            conn.close()
            return f"数据库 [{db_name or conn_config['database']}] 的表:\n" + "\n".join([t[0] for t in tables])
        
        else:
            return f"Error: 不支持的数据库类型 {db_type}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def get_table_schema(table_name: str, db_name: str = None) -> str:
    """获取表结构"""
    try:
        conn_config = _get_connection(db_name)
        db_type = conn_config["type"]
        
        if db_type == "postgresql":
            import asyncpg
            conn = await asyncpg.connect(
                host=conn_config["host"],
                port=conn_config["port"],
                database=conn_config["database"],
                user=conn_config["user"],
                password=conn_config["password"]
            )
            columns = await conn.fetch("""
                SELECT column_name, data_type, is_nullable, column_default
                FROM information_schema.columns 
                WHERE table_name = $1 AND table_schema = 'public'
                ORDER BY ordinal_position
            """, table_name)
            await conn.close()
            
            result = [f"表 {table_name} 结构 ({db_name or conn_config['database']}):"]
            for col in columns:
                nullable = "NULL" if col["is_nullable"] == "YES" else "NOT NULL"
                default = f" DEFAULT {col['column_default']}" if col["column_default"] else ""
                result.append(f"  {col['column_name']}: {col['data_type']} {nullable}{default}")
            return "\n".join(result)
        
        elif db_type == "mysql":
            import aiomysql
            conn = await aiomysql.connect(
                host=conn_config["host"],
                port=conn_config["port"],
                db=conn_config["database"],
                user=conn_config["user"],
                password=conn_config["password"]
            )
            async with conn.cursor() as cursor:
                await cursor.execute(f"DESCRIBE {table_name}")
                columns = await cursor.fetchall()
            conn.close()
            
            result = [f"表 {table_name} 结构 ({db_name or conn_config['database']}):"]
            for col in columns:
                result.append(f"  {col[0]}: {col[1]} {col[2]} {col[3]}")
            return "\n".join(result)
        
        else:
            return f"Error: 不支持的数据库类型 {db_type}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def execute_query(sql: str, db_name: str = None) -> str:
    """执行 SQL 查询（只读 SELECT）"""
    # 安全检查：只允许 SELECT 语句
    sql_upper = sql.strip().upper()
    if not sql_upper.startswith("SELECT") and not sql_upper.startswith("WITH"):
        return "Error: 为安全起见，只允许执行 SELECT 查询语句"
    
    try:
        conn_config = _get_connection(db_name)
        db_type = conn_config["type"]
        
        if db_type == "postgresql":
            import asyncpg
            conn = await asyncpg.connect(
                host=conn_config["host"],
                port=conn_config["port"],
                database=conn_config["database"],
                user=conn_config["user"],
                password=conn_config["password"]
            )
            rows = await conn.fetch(sql)
            await conn.close()
            
            if not rows:
                return "无结果"
            # 限制返回行数
            result = [f"查询结果 ({len(rows)} 行，显示前 50 行):"]
            for i, row in enumerate(rows[:50], 1):
                result.append(f"{i}. {dict(row)}")
            return "\n".join(result)
        
        elif db_type == "mysql":
            import aiomysql
            conn = await aiomysql.connect(
                host=conn_config["host"],
                port=conn_config["port"],
                db=conn_config["database"],
                user=conn_config["user"],
                password=conn_config["password"]
            )
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(sql)
                rows = await cursor.fetchall()
            conn.close()
            
            if not rows:
                return "无结果"
            result = [f"查询结果 ({len(rows)} 行，显示前 50 行):"]
            for i, row in enumerate(rows[:50], 1):
                result.append(f"{i}. {row}")
            return "\n".join(result)
        
        else:
            return f"Error: 不支持的数据库类型 {db_type}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def test_connection(db_name: str = None) -> str:
    """测试数据库连接"""
    try:
        conn_config = _get_connection(db_name)
        db_type = conn_config["type"]
        
        if db_type == "postgresql":
            import asyncpg
            conn = await asyncpg.connect(
                host=conn_config["host"],
                port=conn_config["port"],
                database=conn_config["database"],
                user=conn_config["user"],
                password=conn_config["password"]
            )
            version = await conn.fetchval("SELECT version()")
            await conn.close()
            return f"✅ 连接成功\n数据库：{conn_config['database']}\n版本：{version[:50]}"
        
        elif db_type == "mysql":
            import aiomysql
            conn = await aiomysql.connect(
                host=conn_config["host"],
                port=conn_config["port"],
                db=conn_config["database"],
                user=conn_config["user"],
                password=conn_config["password"]
            )
            async with conn.cursor() as cursor:
                await cursor.execute("SELECT VERSION()")
                version = await cursor.fetchone()
            conn.close()
            return f"✅ 连接成功\n数据库：{conn_config['database']}\n版本：{version[0]}"
        
        else:
            return f"Error: 不支持的数据库类型 {db_type}"
    except Exception as e:
        return f"❌ 连接失败\n数据库：{db_name or conn_config['database']}\n错误：{str(e)}"

if __name__ == "__main__":
    print("DatabaseClient MCP Server 已启动...")
    print(f"配置文件：{CONFIG_PATH}")
    mcp.run()