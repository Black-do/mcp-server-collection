# 🤖 MCP Server Collection

![Version](https://img.shields.io/badge/Version-1.1.0-blue.svg)

个人开发的 MCP（Model Context Protocol）服务器集合，用于 Trae、Cursor 等 AI 编辑器，覆盖文件、HTTP、Git、数据库、记忆等全场景。

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)
![Version](https://img.shields.io/badge/Version-1.1.0-blue.svg)

---

## 📋 目录

- [功能特性](#功能特性)
- [快速开始](#快速开始)
- [项目结构](#项目结构)
- [安装指南](#安装指南)
- [配置说明](#配置说明)
- [使用示例](#使用示例)
- [各 MCP 文档](#各-mcp-文档)
- [常见问题](#常见问题)
- [贡献指南](#贡献指南)
- [License](#license)

---

## ✨ 功能特性

### MCP 服务器列表

| MCP | 功能 | 状态 | 来源 |
| :--- | :--- | :--- | :--- |
| **📁 Filesystem** | 读写本地文件 | ✅ 稳定 | 🔌 官方 npm 包 |
| **🌐 HTTP Client** | HTTP 请求测试，支持本地和网络 API | ✅ 稳定 | 💻 自研 |
| **🔀 Git Client** | Git 状态、历史、分支查询（支持多项目） | ✅ 稳定 | 💻 自研 |
| **🗄️ Database Client** | 多数据库支持（PostgreSQL + MySQL） | ✅ 稳定 | 💻 自研 |
| **🧠 Memory Client** | 长期记忆存储，记住个人偏好 | ✅ 稳定 | 💻 自研 |

> 💡 **说明：** 🔌 表示使用官方/第三方包，💻 表示本项目自研

### 核心优势

- ✅ **完全免费** - 无订阅费，无 API 费用
- ✅ **国内可用** - 自研模块无需特殊网络，全部本地运行
- ✅ **配置灵活** - 每个 MCP 独立配置，互不影响
- ✅ **安全可控** - 代码开源，数据本地存储
- ✅ **易于扩展** - 模块化设计，可快速添加新 MCP

---

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/Black-do/mcp-server-collection.git
cd mcp-server-collection
```

### 2. 安装依赖

```bash
# 自研 MCP 依赖
pip install -r http-client/requirements.txt
pip install -r git-client/requirements.txt
pip install -r db-client/requirements.txt
pip install -r memory-client/requirements.txt
```

### 3. 配置各 MCP

```bash
# 1. 复制配置模板
cp mcp.json.example mcp.json
cp git-client/config.json.example git-client/config.json
cp db-client/db_config.example.json db-client/db_config.json

# 2. 编辑配置文件，替换占位符为你的实际路径
# 3. ⚠️ 不要将含个人路径的配置文件提交到 Git
```

### 4. 配置 Trae/Cursor

1. 打开编辑器设置
2. 找到 MCP 配置文件（`MCP: Open Config File`）
3. 复制 `mcp.json` 内容
4. 保存并重启编辑器

### 5. 验证

查看底部状态栏，所有 MCP 图标应为绿色 🟢

---

## 📁 项目结构

```
mcp-server-collection/
├── README.md                    # 本文件
├── LICENSE                      # MIT 开源协议
├── .gitignore                   # Git 忽略配置
├── mcp.json.example             # MCP 配置模板
├── CHANGELOG.md                 # 更新日志
├── docs/
│   ├── installation.md          # 详细安装文档
│   └── usage.md                 # 使用指南
│
├── http-client/                 # 🌐 HTTP 客户端 MCP（自研）
│   ├── README.md
│   ├── http_mcp.py
│   ├── requirements.txt
│   └── config.json
│
├── git-client/                  # 🔀 Git 客户端 MCP（自研）
│   ├── README.md
│   ├── git_mcp.py
│   ├── requirements.txt
│   ├── config.json
│   └── config.json.example
│
├── db-client/                   # 🗄️ 数据库客户端 MCP（自研）
│   ├── README.md
│   ├── db_mcp.py
│   ├── requirements.txt
│   ├── db_config.json
│   └── db_config.example.json
│
└── memory-client/               # 🧠 记忆 MCP（自研）
    ├── README.md
    ├── memory_mcp.py
    ├── requirements.txt
    └── memory.db
```

---

## 📥 安装指南

### 前置条件

| 软件 | 版本要求 | 下载链接 |
| :--- | :--- | :--- |
| **Python** | 3.8+ | https://www.python.org/downloads/ |
| **Node.js** | 16+ | https://nodejs.org/ |
| **Git** | 2.0+ | https://git-scm.com/ |
| **Trae/Cursor** | 最新版 | https://trae.ai/ 或 https://cursor.sh/ |

### 验证环境

```bash
python --version  # 应 >= 3.8
node --version    # 应 >= 16
git --version     # 应 >= 2.0
```

### 配置国内镜像（推荐）

```bash
# npm 淘宝镜像
npm config set registry https://registry.npmmirror.com

# pip 清华镜像
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 完整安装步骤

详见 [docs/installation.md](docs/installation.md)

---

## ⚙️ 配置说明

### 1. MCP 配置文件

**不要直接提交 `mcp.json`**（包含个人路径），请使用模板：

```bash
# 复制模板
cp mcp.json.example mcp.json

# 编辑 mcp.json，修改所有路径为你的实际路径
```

### 2. 路径配置格式

| 系统 | 格式 | 示例 |
| :--- | :--- | :--- |
| **Windows** | 正斜杠 | `D:/Workspace/MCPServer/http-client/http_mcp.py` |
| **Windows** | 双反斜杠 | `D:\\Workspace\\MCPServer\\http-client\\http_mcp.py` |
| **Mac/Linux** | 正斜杠 | `/Users/username/MCPServer/http-client/http_mcp.py` |

> ⚠️ **不要使用单反斜杠** `D:\Workspace\...`，在 JSON 中会被转义

### 3. mcp.json.example 模板

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "<YOUR_PROJECT_PATH>"],
      "disabled": false
    },
    "http-client": {
      "command": "python",
      "args": ["<YOUR_PATH>/http-client/http_mcp.py"],
      "disabled": false
    },
    "git-client": {
      "command": "python",
      "args": ["<YOUR_PATH>/git-client/git_mcp.py"],
      "disabled": false
    },
    "db-client": {
      "command": "python",
      "args": ["<YOUR_PATH>/db-client/db_mcp.py"],
      "disabled": false
    },
    "memory-client": {
      "command": "python",
      "args": ["<YOUR_PATH>/memory-client/memory_mcp.py"],
      "disabled": false
    }
  }
}
```

### 4. 各 MCP 配置

| MCP | 配置文件 | 说明 |
| :--- | :--- | :--- |
| **Filesystem** | `mcp.json` | 官方 npm 包，配置项目路径 |
| **http-client** | `http-client/config.json` | 可选，配置超时等参数 |
| **git-client** | `git-client/config.json` | **必填**，配置 Git 项目路径（支持多项目） |
| **db-client** | `db-client/db_config.json` | **必填**，配置数据库连接（从 example 复制） |
| **memory-client** | 无需配置 | 自动创建 memory.db |

---

## 🔌 外部依赖说明

以下 MCP 服务器使用官方或第三方包，需要单独配置：

### Filesystem MCP（官方 npm 包）

**功能：** 读取和写入本地文件，让 AI 能够理解项目代码结构。

**来源：** [Model Context Protocol 官方仓库](https://github.com/modelcontextprotocol/servers)

**安装方式：** 通过 npx 按需运行，无需预先安装

**配置步骤：**

1. 编辑项目根目录 `mcp.json`

2. 添加以下配置：
   ```json
   {
     "mcpServers": {
       "filesystem": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-filesystem", "<YOUR_PROJECT_PATH>"],
         "disabled": false
       }
     }
   }
   ```

3. 替换 `<YOUR_PROJECT_PATH>` 为你的项目路径：
   - Windows: `D:/Workspace/your-project`
   - Mac/Linux: `/Users/username/your-project`

4. 保存并重启 Trae/Cursor

**使用示例：**
```
# 读取文件
用户：读取 README.md 的内容

# 列出目录
用户：列出当前目录的文件

# 写入文件
用户：在 docs 目录下创建一个新的 API 文档
```

**安全说明：**
- ⚠️ 文件读写权限受限，只能访问配置的路径及其子目录
- ⚠️ 不要将 `mcp.json` 提交到 Git（包含个人路径）
- ✅ 官方维护，定期更新

**相关链接：**
- GitHub: https://github.com/modelcontextprotocol/servers
- npm: https://www.npmjs.com/package/@modelcontextprotocol/server-filesystem

---

## 💡 使用示例

### HTTP Client

```
# 测试网络 API
用 http-client 访问 https://httpbin.org/get

# 测试本地接口
用 test_local_api 测试 /api/users 接口，POST 方法

# 查看请求历史
查看最近的请求历史
```

### Git Client

```
# 查看状态
查看当前 Git 状态

# 多项目支持
查看 api 项目的 Git 状态
列出所有可访问的 Git 项目

# 生成 commit message
帮我生成 commit message
```

### Database Client

```
# 列出数据库
列出所有配置的数据库

# 查看表结构
查看 users 表的结构，用 dev_db 数据库

# 执行查询
查询最近 10 个用户
```

### Memory Client

```
# 保存记忆
记住我喜欢用 pytest 写测试

# 读取记忆
我偏好什么测试框架？

# 列出记忆
列出所有记忆
```

### Filesystem（官方）

```
# 读取文件
读取 README.md 的内容

# 列出目录
列出当前目录的文件

# 搜索文件
搜索所有 *.py 文件
```

---

## 📚 各 MCP 文档

| MCP | 文档链接 | 说明 |
| :--- | :--- | :--- |
| **HTTP Client** | [http-client/README.md](http-client/README.md) | HTTP 请求测试工具（自研） |
| **Git Client** | [git-client/README.md](git-client/README.md) | Git 版本控制工具（自研，支持多项目） |
| **Database Client** | [db-client/README.md](db-client/README.md) | 多数据库查询工具（自研） |
| **Memory Client** | [memory-client/README.md](memory-client/README.md) | 长期记忆存储工具（自研） |
| **Filesystem** | [官方仓库](https://github.com/modelcontextprotocol/servers) | 文件系统工具（官方 npm 包） |
| **安装指南** | [docs/installation.md](docs/installation.md) | 详细安装步骤 |

---

## ❓ 常见问题

### Q: MCP 状态显示红色

**A:** 检查路径是否正确，手动运行脚本测试：
```bash
python http-client/http_mcp.py
```

### Q: 数据库连接失败

**A:** 确保 `db_config.json` 已创建，数据库服务已启动。

### Q: Git 命令无法执行

**A:** 安装 Git 并添加到系统 PATH。

### Q: Filesystem MCP 无法使用

**A:** 确保 Node.js 已安装，配置正确的项目路径。

### Q: 中文乱码

**A:** 确保文件保存为 UTF-8 编码，Git 配置：
```bash
git config --global core.quotepath false
```

更多问题详见 [docs/installation.md](docs/installation.md#常见问题)

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 开发流程

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 代码规范

- 遵循 PEP 8 代码风格
- 添加必要的类型注解
- 编写清晰的文档字符串
- 确保代码有适当注释

### 添加新 MCP

1. 创建新文件夹 `xxx-client/`
2. 复制其他 MCP 的结构模板
3. 更新根目录 README 和文档
4. 提交 PR

---

## 📄 License

本项目采用 [MIT License](LICENSE) 开源协议。

自研模块（HTTP/Git/Database/Memory Client）由本项目作者开发。
Filesystem MCP 使用官方 npm 包，遵循其原有许可证。

---

## 📞 联系方式

- 📧 Email: locc233outlook.com
- 💬 Issues: [GitHub Issues](https://github.com/Black-do/mcp-server-collection/issues)

---

## 🙏 致谢

- [Model Context Protocol](https://modelcontextprotocol.io/) - MCP 协议
- [Trae](https://trae.ai/) - AI 编辑器
- [Cursor](https://cursor.sh/) - AI 编辑器
- [Filesystem MCP](https://github.com/modelcontextprotocol/servers) - 官方文件服务器

---

## 📝 更新日志

详见 [CHANGELOG.md](CHANGELOG.md)

### v1.1.0 (2026-04-03)
- ✨ Git Client 新增多项目支持
- ✨ 新增 `list_projects` 和 `get_current_branch` 工具
- 📝 更新文档，突出多项目功能

### v1.0.0 (2026-04-02)
- 🎉 初始版本发布
- ✨ HTTP/Git/Database/Memory Client 自研 MCP
- 🔌 集成官方 Filesystem MCP

---

**如果这个项目对你有帮助，请给个 ⭐ Star！** 🎉