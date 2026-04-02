#!/usr/bin/env python3
from mcp.server.fastmcp import FastMCP
import sqlite3
import os
from datetime import datetime

mcp = FastMCP("MemoryClient")

# 数据库路径（当前文件夹）
DB_PATH = os.path.join(os.path.dirname(__file__), "memory.db")

def _init_db():
    """初始化数据库"""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE,
            value TEXT,
            created_at TEXT,
            updated_at TEXT
        )
    """)
    conn.commit()
    conn.close()

@mcp.tool()
def save_memory(key: str, value: str) -> str:
    """保存记忆"""
    _init_db()
    conn = sqlite3.connect(DB_PATH)
    try:
        now = datetime.now().isoformat()
        conn.execute("""
            INSERT OR REPLACE INTO memories (key, value, created_at, updated_at)
            VALUES (?, ?, ?, ?)
        """, (key, value, now, now))
        conn.commit()
        return f"✅ 已保存：{key} = {value}"
    except Exception as e:
        return f"❌ Error: {str(e)}"
    finally:
        conn.close()

@mcp.tool()
def get_memory(key: str) -> str:
    """获取记忆"""
    _init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute("SELECT value FROM memories WHERE key = ?", (key,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    return "⚠️ 未找到该记忆"

@mcp.tool()
def list_memories() -> str:
    """列出所有记忆"""
    _init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute("SELECT key, value, updated_at FROM memories ORDER BY updated_at DESC")
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        return "📭 暂无记忆"
    return "\n".join([f"• {r[0]}: {r[1]} ({r[2][:10]})" for r in rows])

@mcp.tool()
def delete_memory(key: str) -> str:
    """删除记忆"""
    _init_db()
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute("DELETE FROM memories WHERE key = ?", (key,))
        conn.commit()
        if conn.total_changes > 0:
            return f"✅ 已删除：{key}"
        return f"⚠️ 未找到：{key}"
    except Exception as e:
        return f"❌ Error: {str(e)}"
    finally:
        conn.close()

@mcp.tool()
def clear_all_memories() -> str:
    """清空所有记忆"""
    _init_db()
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute("DELETE FROM memories")
        conn.commit()
        return "✅ 已清空所有记忆"
    except Exception as e:
        return f"❌ Error: {str(e)}"
    finally:
        conn.close()

if __name__ == "__main__":
    _init_db()
    print("MemoryClient MCP Server 已启动...")
    print(f"数据库：{DB_PATH}")
    mcp.run()