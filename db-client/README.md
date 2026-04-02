# 🗄️ Database Client MCP

多数据库查询工具，支持 PostgreSQL 和 MySQL，让 AI 助手能够直接查询数据库结构和数据。

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

---

## ✨ 功能特性

- ✅ 多数据库支持（PostgreSQL + MySQL）
- ✅ 配置文件与代码分离
- ✅ 查看表名列表
- ✅ 查看表结构
- ✅ 执行 SQL 查询（只读）
- ✅ 测试数据库连接
- ✅ 安全限制（仅 SELECT）
- ✅ 响应长度限制

---

## 📁 目录结构

```
db-client/
├── README.md                # 本文件
├── db_mcp.py                # 主代码
├── requirements.txt         # Python 依赖
├── db_config.json           # ⚠️ 数据库配置（不提交 Git）
└── db_config.example.json   # ✅ 配置模板（可提交）
```

---

## 🚀 快速开始

### 1. 安装依赖

```bash
cd db-client
pip install -r requirements.txt
```

### 2. 创建配置文件

```bash
cp db_config.example.json db_config.json
```

### 3. 编辑配置

编辑 `db_config.json`，**替换占位符为你的实际数据库信息**：

```json
{
  "default": "dev_db",
  "connections": {
    "dev_db": {
      "name": "开发数据库",
      "type": "postgresql",
      "host": "localhost",
      "port": 5432,
      "database": "<YOUR_DATABASE_NAME>",
      "user": "<YOUR_DATABASE_USER>",
      "password": "<YOUR_DATABASE_PASSWORD>"
    },
    "test_db": {
      "name": "测试数据库",
      "type": "postgresql",
      "host": "localhost",
      "port": 5432,
      "database": "<YOUR_TEST_DATABASE_NAME>",
      "user": "<YOUR_TEST_DATABASE_USER>",
      "password": "<YOUR_TEST_DATABASE_PASSWORD>"
    }
  }
}
```

> ⚠️ **安全提醒：** `db_config.json` 包含数据库密码，**绝对不要提交到 Git**！

### 4. 配置 Trae/Cursor

在项目根目录 `mcp.json` 中添加：

```json
{
  "mcpServers": {
    "db-client": {
      "command": "python",
      "args": ["<YOUR_PATH>/db-client/db_mcp.py"],
      "disabled": false
    }
  }
}
```

### 5. 重启编辑器

完全关闭后重新打开，查看底部状态栏 MCP 图标。

---

## 🛠️ 可用工具

| 工具 | 说明 | 参数 |
| :--- | :--- | :--- |
| `list_databases` | 列出所有配置的数据库 | 无 |
| `get_tables` | 获取表名列表 | db_name |
| `get_table_schema` | 查看表结构 | table_name, db_name |
| `execute_query` | 执行 SQL 查询（只读） | sql, db_name |
| `test_connection` | 测试数据库连接 | db_name |

---

## 💡 使用示例

### 列出所有数据库

```
用户：列出所有配置的数据库
```

**预期输出：**
```
默认数据库：dev_db

可用数据库：
  - dev_db: 开发数据库 [postgresql]@localhost:5432 (默认)
  - test_db: 测试数据库 [postgresql]@localhost:5432
```

### 查看表名列表

```
用户：获取 dev_db 数据库的所有表名
```

### 查看表结构

```
用户：查看 users 表的结构，用 dev_db 数据库
```

**预期输出：**
```
表 users 结构 (dev_db):
  id: integer NOT NULL DEFAULT nextval('users_id_seq'::regclass)
  username: character varying(50) NOT NULL
  email: character varying(100) NOT NULL
  created_at: timestamp without time zone NOT NULL
```

### 执行 SQL 查询

```
用户：查询最近 10 个用户
     sql: SELECT * FROM users ORDER BY created_at DESC LIMIT 10
```

### 测试连接

```
用户：测试 dev_db 数据库连接
```

**预期输出：**
```
✅ 连接成功
数据库：myapp_dev
版本：PostgreSQL 15.2
```

### 切换数据库

```
用户：查看 orders 表的结构，用 test_db 数据库
```

---

## ⚙️ 配置说明

### db_config.json

| 配置项 | 类型 | 说明 |
| :--- | :--- | :--- |
| `default` | string | 默认数据库名称 |
| `connections` | object | 数据库连接配置 |

### 连接配置

| 字段 | 类型 | 说明 |
| :--- | :--- | :--- |
| `name` | string | 数据库描述名称 |
| `type` | string | 数据库类型（postgresql/mysql） |
| `host` | string | 数据库主机 |
| `port` | int | 数据库端口 |
| `database` | string | 数据库名 |
| `user` | string | 用户名 |
| `password` | string | 密码 |

### PostgreSQL 配置示例

```json
{
  "type": "postgresql",
  "host": "localhost",
  "port": 5432,
  "database": "<YOUR_DATABASE_NAME>",
  "user": "<YOUR_DATABASE_USER>",
  "password": "<YOUR_DATABASE_PASSWORD>"
}
```

### MySQL 配置示例

```json
{
  "type": "mysql",
  "host": "localhost",
  "port": 3306,
  "database": "<YOUR_DATABASE_NAME>",
  "user": "<YOUR_DATABASE_USER>",
  "password": "<YOUR_DATABASE_PASSWORD>"
}
```

---

## 🔐 安全说明

| 事项 | 说明 |
| :--- | :--- |
| **只读权限** | 数据库账号建议只给 SELECT 权限 |
| **禁止写操作** | 代码层面拦截 INSERT/UPDATE/DELETE |
| **不连生产库** | 仅限本地开发库或只读从库 |
| **配置不提交** | `db_config.json` 已加入 .gitignore |
| **响应限制** | 最多返回 50 行，防止数据泄露 |

---

## ❓ 常见问题

### Q: 提示 "ModuleNotFoundError: No module named 'asyncpg'"

**A:** 安装依赖：
```bash
pip install -r requirements.txt
```

### Q: 数据库连接失败

**A:** 检查：
1. 数据库服务是否启动
2. `db_config.json` 是否已创建
3. 用户名密码是否正确
4. 防火墙是否允许连接

### Q: 只允许 SELECT 查询

**A:** 出于安全考虑，仅允许 SELECT 和 WITH 语句。

### Q: MCP 状态红色

**A:** 检查 `db_config.json` 是否已创建，路径是否正确。

---

## 📄 依赖说明

**requirements.txt**
```txt
mcp>=0.1.0
asyncpg>=0.29.0    # PostgreSQL
aiomysql>=0.2.0    # MySQL
```

| 依赖 | 用途 |
| :--- | :--- |
| `mcp` | MCP 协议支持 |
| `asyncpg` | PostgreSQL 异步驱动 |
| `aiomysql` | MySQL 异步驱动 |

---

## 📝 更新日志

| 版本 | 日期 | 更新内容 |
| :--- | :--- | :--- |
| 1.0.0 | 2026-04-02 | 初始版本，支持 PostgreSQL + MySQL |

---

## 📞 反馈

- 📚 主项目：[README](../README.md)
- 📚 安装指南：[docs/installation.md](../docs/installation.md)
- 💬 Issues: [GitHub Issues](https://github.com/<YOUR_USERNAME>/mcp-server-collection/issues)