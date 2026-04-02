# 🧠 Memory Client MCP

长期记忆存储工具，让 AI 助手能够记住你的个人偏好、项目规范、常用配置等信息。

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

---

## ✨ 功能特性

- ✅ 保存记忆（键值对）
- ✅ 查询记忆
- ✅ 列出所有记忆
- ✅ 删除单个记忆
- ✅ 清空所有记忆
- ✅ SQLite 本地存储
- ✅ 自动创建数据库
- ✅ 时间戳记录

---

## 📁 目录结构

```
memory-client/
├── README.md          # 本文件
├── memory_mcp.py      # 主代码
├── requirements.txt   # Python 依赖
└── memory.db          # SQLite 数据库（不提交 Git）
```

---

## 🚀 快速开始

### 1. 安装依赖

```bash
cd memory-client
pip install -r requirements.txt
```

### 2. 配置 Trae/Cursor

在项目根目录 `mcp.json` 中添加：

```json
{
  "mcpServers": {
    "memory-client": {
      "command": "python",
      "args": ["<YOUR_PATH>/memory-client/memory_mcp.py"],
      "disabled": false
    }
  }
}
```

### 3. 重启编辑器

完全关闭后重新打开，查看底部状态栏 MCP 图标。

> ✅ **无需额外配置**，数据库会自动创建。

---

## 🛠️ 可用工具

| 工具 | 说明 | 参数 |
| :--- | :--- | :--- |
| `save_memory` | 保存记忆 | key, value |
| `get_memory` | 获取记忆 | key |
| `list_memories` | 列出所有记忆 | 无 |
| `delete_memory` | 删除记忆 | key |
| `clear_all_memories` | 清空所有记忆 | 无 |

---

## 💡 使用示例

### 保存记忆

```
用户：记住我喜欢用 pytest 写单元测试
```

**预期输出：**
```
✅ 已保存：test_framework = pytest
```

### 读取记忆

```
用户：我偏好什么测试框架？
```

**预期输出：**
```
pytest
```

### 列出所有记忆

```
用户：列出所有记忆
```

**预期输出：**
```
• test_framework: pytest (2026-04-02)
• project_stack: FastAPI + PostgreSQL (2026-04-02)
• deploy_command: docker-compose up -d (2026-04-02)
```

### 保存更多记忆

```
用户：记住当前项目使用 FastAPI + SQLAlchemy 2.0
用户：记住我的部署命令是 docker-compose up -d
```

### 删除记忆

```
用户：删除 test_framework 记忆
```

**预期输出：**
```
✅ 已删除：test_framework
```

### 清空所有记忆

```
用户：清空所有记忆
```

**预期输出：**
```
✅ 已清空所有记忆
```

---

## 🎯 实际应用场景

### 场景 1：编码偏好

```
用户：记住我喜欢用 pytest 写测试
用户：帮我写一个用户登录的测试用例
```

AI 会自动使用 pytest 框架生成代码。

### 场景 2：项目规范

```
用户：记住当前项目使用 FastAPI + PostgreSQL
用户：创建一个用户模型
```

AI 会自动使用 FastAPI + SQLAlchemy 2.0 生成代码。

### 场景 3：团队规范

```
用户：记住我们团队的 commit 规范是 feat/fix/docs
用户：帮我生成 commit message
```

AI 会根据团队规范生成 commit message。

### 场景 4：常用命令

```
用户：记住我的部署命令是 docker-compose up -d --build
用户：怎么部署项目？
```

AI 会返回你配置的部署命令。

---

## ⚙️ 配置说明

### 无需配置

Memory MCP 无需额外配置文件，数据库会自动创建在：

```
memory-client/memory.db
```

### 手动查看数据库（可选）

```bash
# 使用 SQLite 命令行
sqlite3 memory-client/memory.db

# 查询所有记忆
SELECT * FROM memories;

# 退出
.exit
```

---

## 🔐 安全说明

| 事项 | 说明 |
| :--- | :--- |
| **敏感信息** | 不要存储密码、API Key 等敏感信息 |
| **本地存储** | 数据存储在本地 SQLite 数据库 |
| **不提交 Git** | `memory.db` 已加入 .gitignore |
| **隐私保护** | 数据仅本地可见，不会上传云端 |

---

## ❓ 常见问题

### Q: 提示 "ModuleNotFoundError: No module named 'sqlite3'"

**A:** sqlite3 是 Python 标准库，无需安装。如果报错，请重装完整版 Python。

### Q: memory.db 无法创建

**A:** 检查文件夹权限，或以管理员身份运行编辑器。

### Q: 中文乱码

**A:** 确保文件保存为 UTF-8 编码。

### Q: MCP 状态红色

**A:** 检查 `mcp.json` 中的路径是否正确，手动运行测试：
```bash
python memory_mcp.py
```

---

## 📄 依赖说明

**requirements.txt**
```txt
mcp>=0.1.0
```

> SQLite 是 Python 标准库，无需额外安装。

---

## 📊 与 .cursorrules 对比

| 特性 | Memory MCP | .cursorrules |
| :--- | :--- | :--- |
| 存储位置 | SQLite 数据库 | 文本文件 |
| 作用范围 | 全局（所有项目） | 局部（单个项目） |
| 更新方式 | 对话中动态更新 | 手动编辑文件 |
| 查询方式 | AI 主动读取 | 每次对话自动注入 |
| 适合场景 | 个人偏好、跨项目规范 | 项目特定规范 |

**建议：** 项目规范用 `.cursorrules`，个人偏好用 Memory MCP。

---

## 📝 更新日志

| 版本 | 日期 | 更新内容 |
| :--- | :--- | :--- |
| 1.0.0 | 2026-04-02 | 初始版本 |

---

## 📞 反馈

- 📚 主项目：[README](../README.md)
- 📚 安装指南：[docs/installation.md](../docs/installation.md)
- 💬 Issues: [GitHub Issues](https://github.com/Black-do/mcp-server-collection/issues)