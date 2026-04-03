# MCP Server Collection 安装指南

详细的安装和配置说明，帮助你快速部署 MCP 服务器集合。

---

## 📋 目录

1. [前置条件](#前置条件)
2. [项目结构](#项目结构)
3. [快速开始](#快速开始)
4. [详细安装步骤](#详细安装步骤)
5. [各 MCP 配置](#各-mcp-配置)
6. [验证测试](#验证测试)
7. [常见问题](#常见问题)
8. [国内用户优化](#国内用户优化)

---

## 前置条件

### 必需软件

| 软件 | 版本要求 | 下载链接 | 验证命令 |
| :--- | :--- | :--- | :--- |
| **Python** | 3.8+ | https://www.python.org/downloads/ | `python --version` |
| **Node.js** | 16+ | https://nodejs.org/ | `node --version` |
| **npm** | 8+ | 随 Node.js 安装 | `npm --version` |
| **Git** | 2.0+ | https://git-scm.com/ | `git --version` |
| **Trae/Cursor** | 最新版 | https://trae.ai/ 或 https://cursor.sh/ | - |

### 验证安装

```bash
# Windows PowerShell
python --version
node --version
npm --version
git --version

# Mac/Linux
python3 --version
node --version
npm --version
git --version
```

### 最低配置要求

| 配置 | 要求 |
| :--- | :--- |
| 操作系统 | Windows 10+ / macOS 10.15+ / Linux |
| 内存 | 4GB+ |
| 磁盘空间 | 500MB+ |
| 网络 | 可访问 GitHub 和 npm/pypi |

---

## 项目结构

```
mcp-server-collection/
├── README.md                    # 项目说明
├── LICENSE                      # MIT 开源协议
├── .gitignore                   # Git 忽略配置
├── mcp.json.example             # MCP 配置模板
├── CHANGELOG.md                 # 更新日志
├── docs/
│   ├── installation.md          # 本文件
│   └── usage.md                 # 使用指南
│
├── http-client/                 # 🌐 HTTP 客户端（自研）
│   ├── README.md
│   ├── http_mcp.py
│   ├── requirements.txt
│   └── config.json
│
├── git-client/                  # 🔀 Git 客户端（自研）
│   ├── README.md
│   ├── git_mcp.py
│   ├── requirements.txt
│   ├── config.json
│   └── config.json.example
│
├── db-client/                   # 🗄️ 数据库客户端（自研）
│   ├── README.md
│   ├── db_mcp.py
│   ├── requirements.txt
│   ├── db_config.json
│   └── db_config.example.json
│
└── memory-client/               # 🧠 记忆客户端（自研）
    ├── README.md
    ├── memory_mcp.py
    ├── requirements.txt
    └── memory.db
```

### 模块说明

| 模块 | 类型 | 说明 |
| :--- | :--- | :--- |
| **http-client** | 自研 | HTTP 请求测试工具 |
| **git-client** | 自研 | Git 版本控制工具（支持多项目） |
| **db-client** | 自研 | 多数据库查询工具 |
| **memory-client** | 自研 | 长期记忆存储工具 |
| **filesystem** | 官方 | 文件系统工具（npm 包） |

---

## 快速开始

### 5 分钟快速安装

```bash
# 1. 克隆项目
git clone https://github.com/Black-do/mcp-server-collection.git
cd mcp-server-collection

# 2. 安装 Python 依赖
pip install -r http-client/requirements.txt
pip install -r git-client/requirements.txt
pip install -r db-client/requirements.txt
pip install -r memory-client/requirements.txt

# 3. 复制配置模板
cp mcp.json.example mcp.json
cp git-client/config.json.example git-client/config.json
cp db-client/db_config.example.json db-client/db_config.json

# 4. 编辑配置文件，替换占位符为实际路径

# 5. 配置 Trae/Cursor 的 MCP 设置

# 6. 重启编辑器，验证 MCP 状态
```

---

## 详细安装步骤

### 步骤 1：克隆项目

```bash
# 选择安装目录
cd D:/Workspace  # Windows
# 或
cd ~/Workspace   # Mac/Linux

# 克隆项目
git clone https://github.com/Black-do/mcp-server-collection.git

# 进入项目目录
cd mcp-server-collection
```

### 步骤 2：安装 Python 依赖

```bash
# 方式 1：分别安装（推荐）
pip install -r http-client/requirements.txt
pip install -r git-client/requirements.txt
pip install -r db-client/requirements.txt
pip install -r memory-client/requirements.txt

# 方式 2：一次性安装所有
find . -name "requirements.txt" -exec pip install -r {} \;  # Mac/Linux
# 或 Windows PowerShell
Get-ChildItem -Recurse -Filter "requirements.txt" | ForEach-Object { pip install -r $_.FullName }
```

### 步骤 3：配置国内镜像（推荐国内用户）

```bash
# pip 清华镜像
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# npm 淘宝镜像
npm config set registry https://registry.npmmirror.com

# 验证配置
pip config get global.index-url
npm config get registry
```

### 步骤 4：复制配置模板

```bash
# 根目录配置
cp mcp.json.example mcp.json

# Git Client 配置
cp git-client/config.json.example git-client/config.json

# Database Client 配置
cp db-client/db_config.example.json db-client/db_config.json

# 验证文件已创建
ls -la mcp.json git-client/config.json db-client/db_config.json
```

### 步骤 5：编辑配置文件

#### 编辑 `mcp.json`

```bash
# 用文本编辑器打开
notepad mcp.json  # Windows
# 或
code mcp.json     # VS Code
```

**修改内容：**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "D:/Workspace/your-project"],
      "disabled": false
    },
    "http-client": {
      "command": "python",
      "args": ["D:/Workspace/MCPServer/http-client/http_mcp.py"],
      "disabled": false
    },
    "git-client": {
      "command": "python",
      "args": ["D:/Workspace/MCPServer/git-client/git_mcp.py"],
      "disabled": false
    },
    "db-client": {
      "command": "python",
      "args": ["D:/Workspace/MCPServer/db-client/db_mcp.py"],
      "disabled": false
    },
    "memory-client": {
      "command": "python",
      "args": ["D:/Workspace/MCPServer/memory-client/memory_mcp.py"],
      "disabled": false
    }
  }
}
```

> ⚠️ **替换所有 `<YOUR_PATH>` 为你的实际路径**

#### 编辑 `git-client/config.json`

```json
{
  "default_project_path": "D:/Workspace/your-main-project",
  "projects": {
    "main": {
      "path": "D:/Workspace/your-main-project",
      "name": "主项目",
      "description": "MCP 服务器集合"
    },
    "api": {
      "path": "D:/Workspace/your-api-project",
      "name": "API 项目",
      "description": "FastAPI 后端服务"
    }
  },
  "max_log_entries": 20,
  "timeout_seconds": 30
}
```

#### 编辑 `db-client/db_config.json`

```json
{
  "default": "dev_db",
  "connections": {
    "dev_db": {
      "name": "开发数据库",
      "type": "postgresql",
      "host": "localhost",
      "port": 5432,
      "database": "your_database",
      "user": "your_user",
      "password": "your_password"
    }
  }
}
```

> ⚠️ **安全提醒：** `db_config.json` 包含密码，不要提交到 Git！

### 步骤 6：配置 Trae/Cursor

#### Trae 配置

1. 打开 Trae
2. 命令面板：`Ctrl + Shift + P` (Windows) 或 `Cmd + Shift + P` (Mac)
3. 输入 `MCP: Open Config File` 并回车
4. 复制 `mcp.json` 全部内容
5. 粘贴到 Trae 的 MCP 配置文件中
6. 保存 (`Ctrl + S` / `Cmd + S`)
7. 完全关闭 Trae 后重新打开

#### Cursor 配置

1. 打开 Cursor
2. 设置 → Features → MCP
3. 点击 "Add New MCP Server"
4. 复制 `mcp.json` 配置
5. 保存并重启 Cursor

### 步骤 7：验证安装

```bash
# 1. 测试各 MCP 脚本能否启动
python http-client/http_mcp.py &
python git-client/git_mcp.py &
python db-client/db_mcp.py &
python memory-client/memory_mcp.py &

# 2. 查看 Trae/Cursor 底部状态栏
# 所有 MCP 图标应为绿色 🟢

# 3. 在聊天窗口测试
# 见下方"验证测试"章节
```

---

## 各 MCP 配置

### 📁 Filesystem MCP（官方）

| 配置项 | 说明 |
| :--- | :--- |
| **来源** | 官方 npm 包 |
| **安装** | 无需安装，npx 按需运行 |
| **配置** | 在 `mcp.json` 中配置项目路径 |
| **依赖** | Node.js 16+ |

**配置示例：**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "D:/Workspace/your-project"],
      "disabled": false
    }
  }
}
```

---

### 🌐 HTTP Client MCP（自研）

| 配置项 | 说明 |
| :--- | :--- |
| **来源** | 本项目自研 |
| **安装** | `pip install -r http-client/requirements.txt` |
| **配置** | `http-client/config.json`（可选） |
| **依赖** | Python 3.8+, mcp, httpx |

**配置示例：**
```json
{
  "default_timeout": 30,
  "max_response_length": 5000,
  "allowed_methods": ["GET", "POST", "PUT", "DELETE", "PATCH"]
}
```

---

### 🔀 Git Client MCP（自研）

| 配置项 | 说明 |
| :--- | :--- |
| **来源** | 本项目自研 |
| **安装** | `pip install -r git-client/requirements.txt` |
| **配置** | `git-client/config.json`（必填） |
| **依赖** | Python 3.8+, mcp, Git |

**配置示例（多项目）：**
```json
{
  "default_project_path": "D:/Workspace/main",
  "projects": {
    "main": {
      "path": "D:/Workspace/main",
      "name": "主项目"
    },
    "api": {
      "path": "D:/Workspace/api",
      "name": "API 项目"
    }
  },
  "max_log_entries": 20,
  "timeout_seconds": 30
}
```

---

### 🗄️ Database Client MCP（自研）

| 配置项 | 说明 |
| :--- | :--- |
| **来源** | 本项目自研 |
| **安装** | `pip install -r db-client/requirements.txt` |
| **配置** | `db-client/db_config.json`（必填） |
| **依赖** | Python 3.8+, mcp, asyncpg/aiomysql |

**配置示例：**
```json
{
  "default": "dev_db",
  "connections": {
    "dev_db": {
      "type": "postgresql",
      "host": "localhost",
      "port": 5432,
      "database": "your_db",
      "user": "your_user",
      "password": "your_password"
    }
  }
}
```

**安装数据库驱动：**
```bash
# PostgreSQL
pip install asyncpg

# MySQL
pip install aiomysql
```

---

### 🧠 Memory Client MCP（自研）

| 配置项 | 说明 |
| :--- | :--- |
| **来源** | 本项目自研 |
| **安装** | `pip install -r memory-client/requirements.txt` |
| **配置** | 无需配置，自动创建数据库 |
| **依赖** | Python 3.8+, mcp |

---

## 验证测试

### 测试清单

| MCP | 测试指令 | 预期结果 |
| :--- | :--- | :--- |
| **Filesystem** | `读取 README.md 的内容` | 返回文件内容 |
| **HTTP Client** | `用 http-client 访问 https://httpbin.org/get` | 返回 200 状态码 |
| **Git Client** | `列出所有可访问的 Git 项目` | 显示配置的项目列表 |
| **Git Client** | `查看当前 Git 状态` | 显示 Git 状态 |
| **Database** | `列出所有配置的数据库` | 显示数据库列表 |
| **Memory** | `记住我喜欢用 pytest 写测试` | 返回保存成功 |
| **Memory** | `列出所有记忆` | 显示已保存的记忆 |

### 批量测试脚本

```bash
#!/bin/bash
# test_all_mcp.sh

echo "🧪 开始测试所有 MCP..."

# 测试 HTTP Client
echo "测试 HTTP Client..."
python http-client/http_mcp.py &
sleep 2

# 测试 Git Client
echo "测试 Git Client..."
python git-client/git_mcp.py &
sleep 2

# 测试 Database Client
echo "测试 Database Client..."
python db-client/db_mcp.py &
sleep 2

# 测试 Memory Client
echo "测试 Memory Client..."
python memory-client/memory_mcp.py &
sleep 2

echo "✅ 所有 MCP 启动测试完成！"
```

---

## 常见问题

### Q: MCP 状态显示红色

**A:** 检查以下步骤：
```bash
# 1. 检查路径是否正确
cat mcp.json | python -m json.tool

# 2. 手动测试脚本
python http-client/http_mcp.py

# 3. 查看 Trae MCP 日志
# 命令面板 → MCP: Show Server Logs
```

### Q: 提示 "python 不是内部或外部命令"

**A:** 
```bash
# Windows: 重新安装 Python，勾选 "Add Python to PATH"
# 或在 mcp.json 中使用完整路径
{
  "command": "C:/Python311/python.exe",
  "args": [".../http_mcp.py"]
}
```

### Q: npm 包下载失败

**A:** 配置国内镜像：
```bash
npm config set registry https://registry.npmmirror.com
npm config get registry  # 验证
```

### Q: pip 安装依赖失败

**A:** 配置国内镜像：
```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt
```

### Q: Git Client 提示"不是 Git 仓库"

**A:** 确保配置的路径包含 `.git` 文件夹：
```bash
# 验证
Test-Path "D:/Workspace/your-project/.git"  # Windows
ls -la /path/to/your-project/.git           # Mac/Linux
```

### Q: Database Client 连接失败

**A:** 检查：
```bash
# 1. 数据库服务是否启动
# 2. db_config.json 是否已创建
# 3. 用户名密码是否正确
# 4. 防火墙是否允许连接
# 5. 测试连接：
python -c "import asyncpg; print('OK')"
```

### Q: 中文乱码

**A:** 
```bash
# Git 配置
git config --global core.quotepath false
git config --global gui.encoding utf-8

# 确保文件保存为 UTF-8 编码
```

### Q: 敏感文件被提交到 Git

**A:** 
```bash
# 1. 从 Git 缓存中移除
git rm --cached mcp.json
git rm --cached git-client/config.json
git rm --cached db-client/db_config.json

# 2. 更新 .gitignore
echo "mcp.json" >> .gitignore
echo "git-client/config.json" >> .gitignore
echo "db-client/db_config.json" >> .gitignore

# 3. 提交更改
git add .gitignore
git commit -m "Fix: Remove sensitive files"
```

---

## 国内用户优化

### 网络加速配置

```bash
# pip 镜像
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# npm 镜像
npm config set registry https://registry.npmmirror.com

# Git 加速（可选）
git config --global url."https://github.com/".insteadOf git@github.com:
```

### 预下载依赖（可选）

```bash
# 下载所有 Python 依赖到本地
pip download -r http-client/requirements.txt -d ./wheels
pip download -r git-client/requirements.txt -d ./wheels
pip download -r db-client/requirements.txt -d ./wheels
pip download -r memory-client/requirements.txt -d ./wheels

# 离线安装
pip install --no-index --find-links=./wheels -r http-client/requirements.txt
```

### 常见问题（国内）

| 问题 | 解决 |
| :--- | :--- |
| GitHub 访问慢 | 使用镜像站或代理 |
| npm 下载慢 | 配置淘宝镜像 |
| pip 下载慢 | 配置清华/中科大镜像 |
| npm 包找不到 | 检查镜像同步状态 |

---

## 📞 获取帮助

- 📚 主文档：[README.md](../README.md)
- 💬 Issues: [GitHub Issues](https://github.com/black-do/mcp-server-collection/issues)
- 📧 Email: locc233@outlook.com