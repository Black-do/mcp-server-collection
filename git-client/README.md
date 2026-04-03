# 🔀 Git Client MCP

Git 版本控制工具，让 AI 助手能够读取 Git 状态、历史、分支等信息，辅助代码管理。**支持多项目配置和切换**。

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)
![Version](https://img.shields.io/badge/Version-1.1.0-blue.svg)

---

## ✨ 功能特性

- ✅ 查看 Git 状态
- ✅ 查看提交历史
- ✅ 查看未提交改动
- ✅ 查看分支列表
- ✅ 查看当前分支（新增）
- ✅ 生成 commit message 建议
- ✅ **多项目支持（新增）**
- ✅ 只读操作（安全）
- ✅ 超时保护

---

## 📁 目录结构

```
git-client/
├── README.md              # 本文件
├── git_mcp.py             # 主代码
├── requirements.txt       # Python 依赖
├── config.json            # ⚠️ 配置文件（不提交 Git）
└── config.json.example    # ✅ 配置模板（可提交）
```

---

## 🚀 快速开始

### 1. 安装依赖

```bash
cd git-client
pip install -r requirements.txt
```

### 2. 创建配置文件

```bash
cp config.json.example config.json
```

### 3. 编辑配置

编辑 `config.json`，**替换占位符为你的实际路径**：

#### 模式 1：单项目配置（向后兼容）

```json
{
  "default_project_path": "<YOUR_GIT_PROJECT_PATH>",
  "max_log_entries": 20,
  "timeout_seconds": 30,
  "allowed_commands": ["status", "log", "diff", "branch", "show"],
  "exclude_patterns": ["*.log", "*.tmp", "node_modules/", "__pycache__/"]
}
```

#### 模式 2：多项目配置（推荐）

```json
{
  "default_project_path": "<YOUR_DEFAULT_PROJECT_PATH>",
  "projects": {
    "main": {
      "path": "<YOUR_MAIN_PROJECT_PATH>",
      "name": "主项目",
      "description": "MCP 服务器集合"
    },
    "api": {
      "path": "<YOUR_API_PROJECT_PATH>",
      "name": "API 项目",
      "description": "FastAPI 后端服务"
    },
    "web": {
      "path": "<YOUR_WEB_PROJECT_PATH>",
      "name": "Web 项目",
      "description": "前端页面"
    }
  },
  "max_log_entries": 20,
  "timeout_seconds": 30,
  "allowed_commands": ["status", "log", "diff", "branch", "show"],
  "exclude_patterns": ["*.log", "*.tmp", "node_modules/", "__pycache__/"]
}
```

> ⚠️ **必填：** `default_project_path` 或 `projects` 至少配置一个
> 
> ⚠️ **安全：** `config.json` 包含个人路径，**不要提交到 Git**！

### 4. 配置 Trae/Cursor

在项目根目录 `mcp.json` 中添加：

```json
{
  "mcpServers": {
    "git-client": {
      "command": "python",
      "args": ["<YOUR_PATH>/git-client/git_mcp.py"],
      "disabled": false
    }
  }
}
```

### 5. 验证 Git 安装

```bash
git --version
```

### 6. 重启编辑器

完全关闭后重新打开，查看底部状态栏 MCP 图标。

---

## 🛠️ 可用工具

| 工具 | 说明 | 参数 | 版本 |
| :--- | :--- | :--- | :--- |
| `list_projects` | 列出所有可访问的项目 | 无 | v1.1.0 |
| `get_status` | 查看 Git 状态 | project_name（可选） | v1.0.0 |
| `get_log` | 查看提交历史 | limit, project_name | v1.0.0 |
| `get_diff` | 查看未提交改动 | file, project_name | v1.0.0 |
| `get_branches` | 查看分支列表 | project_name | v1.0.0 |
| `get_current_branch` | 查看当前分支 | project_name | v1.1.0 |
| `generate_commit_message` | 生成 commit 建议 | project_name | v1.0.0 |

---

## 💡 使用示例

### 单项目模式

```
# 查看 Git 状态
用户：查看当前 Git 状态

AI：（使用 default_project_path）
M src/app.py
?? src/new_feature.py
```

### 多项目模式

#### 列出所有项目

```
用户：列出所有可访问的 Git 项目

AI：（调用 list_projects）
📁 可访问的 Git 项目：
  • (default) D:/Workspace/main
  • main: 主项目 (default)
      └─ MCP 服务器集合
  • api: API 项目
      └─ FastAPI 后端服务
  • web: Web 项目
      └─ 前端页面
```

#### 查看指定项目

```
用户：查看 api 项目的 Git 状态

AI：（调用 get_status project_name="api"）
M src/auth/jwt.py
?? src/middleware/rate_limit.py
```

#### 查看提交历史

```
用户：查看 main 项目的最近 10 次提交

AI：（调用 get_log limit=10 project_name="main"）
35851e0 更新 README 文档
e4f5g6h 添加 Memory MCP
i7j8k9l 修复路径问题
...
```

#### 切换项目

```
用户：切换到 web 项目，查看当前分支

AI：（调用 get_current_branch project_name="web"）
main
```

#### 生成 commit message

```
用户：帮我为 api 项目生成 commit message

AI：（调用 generate_commit_message project_name="api"）
[API 项目] 当前改动:
M src/auth/jwt.py
?? src/middleware/rate_limit.py

文件变更:
 src/auth/jwt.py | 25 ++++++++++++++++++++++++-
 src/middleware/rate_limit.py | 45 +++++++++++++++++++++++++++++++++++++++++++++

建议 commit message:
- feat: 添加 JWT 认证和速率限制中间件
- fix: 修复 token 刷新逻辑
- refactor: 重构认证模块结构
```

#### 跨项目对比

```
用户：对比 main 和 api 项目的最新提交

AI：
【main 项目】
（调用 get_log limit=1 project_name="main"）
35851e0 更新 README 文档

【api 项目】
（调用 get_log limit=1 project_name="api"）
a1b2c3d 修复用户认证逻辑
```

#### 查看文件改动

```
用户：查看 api 项目中 src/auth.py 的改动

AI：（调用 get_diff file="src/auth.py" project_name="api"）
diff --git a/src/auth.py b/src/auth.py
+    def verify_token(token: str) -> bool:
+        ...
```

---

## ⚙️ 配置说明

### config.json（必填）

| 配置项 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| `default_project_path` | string | ✅* | - | 默认 Git 项目路径（与 projects 二选一） |
| `projects` | object | ✅* | - | 多项目配置（与 default_project_path 二选一） |
| `projects.*.path` | string | ✅ | - | 项目实际路径 |
| `projects.*.name` | string | ❌ | - | 项目显示名称 |
| `projects.*.description` | string | ❌ | - | 项目描述（帮助 AI 理解） |
| `max_log_entries` | int | ❌ | 20 | git log 最大显示条数 |
| `timeout_seconds` | int | ❌ | 30 | Git 命令超时时间 |
| `allowed_commands` | array | ❌ | 见下 | 允许的 Git 命令白名单 |
| `exclude_patterns` | array | ❌ | 见下 | 忽略的文件模式 |

> *`default_project_path` 和 `projects` 至少配置一个

### 完整配置示例

```json
{
  "default_project_path": "D:/Workspace/main-project",
  "projects": {
    "main": {
      "path": "D:/Workspace/main-project",
      "name": "主项目",
      "description": "MCP 服务器集合"
    },
    "api": {
      "path": "D:/Workspace/api-project",
      "name": "API 项目",
      "description": "FastAPI 后端服务"
    },
    "web": {
      "path": "D:/Workspace/web-project",
      "name": "Web 项目",
      "description": "前端页面"
    },
    "learning": {
      "path": "D:/Workspace/learning/python",
      "name": "学习项目",
      "description": "Python 学习代码"
    }
  },
  "max_log_entries": 20,
  "timeout_seconds": 30,
  "allowed_commands": ["status", "log", "diff", "branch", "show"],
  "exclude_patterns": ["*.log", "*.tmp", "node_modules/", "__pycache__/"]
}
```

### 项目命名建议

| 项目标识符 | 路径示例 | 说明 |
| :--- | :--- | :--- |
| `main` | `D:/Workspace/main` | 主项目/MCP 集合 |
| `api` | `D:/Workspace/my-api` | 后端 API 服务 |
| `web` | `D:/Workspace/my-web` | 前端项目 |
| `mobile` | `D:/Workspace/my-app` | 移动端项目 |
| `lib-xxx` | `D:/Workspace/libs/xxx` | 工具库 |
| `learning-xxx` | `D:/Workspace/learning/xxx` | 学习项目 |

---

## 🔐 安全说明

| 事项 | 说明 |
| :--- | :--- |
| **只读操作** | 仅允许 status/log/diff/branch/show 等只读命令 |
| **禁止修改** | 不允许 commit/push/reset/rebase 等修改操作 |
| **超时保护** | 30 秒超时，防止命令卡死 |
| **路径验证** | 确保指向有效的 Git 仓库（有 .git 文件夹） |
| **配置文件** | `config.json` 含个人路径，**不要提交 Git** |
| **命令白名单** | 可通过 `allowed_commands` 限制可用命令 |

---

## ❓ 常见问题

### Q: 提示 "git 不是内部或外部命令"

**A:** 安装 Git 并添加到系统 PATH：
- Windows: https://git-scm.com/download/win
- 安装后重启终端/编辑器

### Q: 提示 "不是 Git 仓库"

**A:** 确保配置的路径包含 `.git` 文件夹。

### Q: 如何配置多个项目？

**A:** 在 `config.json` 中添加 `projects` 对象：
```json
{
  "projects": {
    "main": { "path": "D:/Workspace/main", "name": "主项目" },
    "api": { "path": "D:/Workspace/api", "name": "API 项目" }
  }
}
```

### Q: 如何切换项目？

**A:** 在对话中指定项目名称：
```
用户：查看 api 项目的 Git 状态
```

### Q: 中文乱码

**A:** 配置 Git：
```bash
git config --global core.quotepath false
git config --global gui.encoding utf-8
```

### Q: MCP 状态红色

**A:** 检查：
1. `config.json` 是否已创建
2. 路径是否正确
3. 手动运行测试：`python git_mcp.py`

### Q: 如何列出所有可访问的项目？

**A:** 使用 `list_projects` 工具：
```
用户：列出所有可访问的 Git 项目
```

---

## 📄 依赖说明

**requirements.txt**
```txt
mcp>=0.1.0
```

> Git 操作使用 Python 内置 `subprocess` 模块，无需额外依赖。

---

## 📝 更新日志

| 版本 | 日期 | 更新内容 |
| :--- | :--- | :--- |
| 1.1.0 | 2026-04-02 | 新增多项目支持、list_projects、get_current_branch 工具 |
| 1.0.0 | 2026-04-01 | 初始版本，支持单项目 Git 操作 |

---

## 📞 反馈

- 📚 主项目：[README](../README.md)
- 📚 安装指南：[docs/installation.md](../docs/installation.md)
- 💬 Issues: [GitHub Issues](https://github.com/Black-do/mcp-server-collection/issues)