# 🔀 Git Client MCP

Git 版本控制工具，让 AI 助手能够读取 Git 状态、历史、分支等信息，辅助代码管理。

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

---

## ✨ 功能特性

- ✅ 查看 Git 状态
- ✅ 查看提交历史
- ✅ 查看未提交改动
- ✅ 查看分支列表
- ✅ 生成 commit message 建议
- ✅ 多项目支持
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

```json
{
  "default_project_path": "<YOUR_GIT_PROJECT_PATH>",
  "max_log_entries": 20,
  "timeout_seconds": 30,
  "allowed_commands": ["status", "log", "diff", "branch", "show"],
  "exclude_patterns": ["*.log", "*.tmp", "node_modules/", "__pycache__/"]
}
```

> ⚠️ **必填：** `default_project_path` 必须指向包含 `.git` 文件夹的目录
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

| 工具 | 说明 | 参数 |
| :--- | :--- | :--- |
| `get_status` | 查看 Git 状态 | project_name（可选） |
| `get_log` | 查看提交历史 | limit, project_name |
| `get_diff` | 查看未提交改动 | file, project_name |
| `get_branches` | 查看分支列表 | project_name |
| `generate_commit_message` | 生成 commit 建议 | project_name |
| `list_projects` | 列出所有配置的项目 | 无 |

---

## 💡 使用示例

### 查看 Git 状态

```
用户：查看当前 Git 状态
```

**预期输出：**
```
M src/app.py
?? src/new_feature.py
```

### 查看提交历史

```
用户：显示最近 10 次提交
```

**预期输出：**
```
a1b2c3d 修复登录 bug
e4f5g6h 添加用户 API
i7j8k9l 重构数据库模块
...
```

### 查看文件改动

```
用户：查看 app.py 的改动
```

### 生成 commit message

```
用户：帮我生成 commit message
```

**预期输出：**
```
当前改动:
M src/app.py
?? src/new_feature.py

文件变更:
 src/app.py | 15 +++++++++++++++
 src/new_feature.py | 50 ++++++++++++++++++++++++++++++++++++++++++++++++++

建议 commit message:
- feat: 添加新功能
- fix: 修复 bug
- refactor: 重构代码
```

### 多项目支持

```json
{
  "default_project_path": "<YOUR_MAIN_PROJECT_PATH>",
  "projects": {
    "main": "<YOUR_MAIN_PROJECT_PATH>",
    "api": "<YOUR_API_PROJECT_PATH>",
    "web": "<YOUR_WEB_PROJECT_PATH>"
  }
}
```

```
用户：列出所有配置的项目
用户：查看 api 项目的 Git 状态
```

---

## ⚙️ 配置说明

### config.json（必填）

| 配置项 | 类型 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- |
| `default_project_path` | string | - | 默认 Git 项目路径（必填） |
| `max_log_entries` | int | 20 | git log 最大显示条数 |
| `timeout_seconds` | int | 30 | Git 命令超时时间 |
| `allowed_commands` | array | 见下 | 允许的 Git 命令白名单 |
| `exclude_patterns` | array | 见下 | 忽略的文件模式 |

### 完整配置示例

```json
{
  "default_project_path": "<YOUR_GIT_PROJECT_PATH>",
  "max_log_entries": 20,
  "timeout_seconds": 30,
  "allowed_commands": ["status", "log", "diff", "branch", "show"],
  "exclude_patterns": ["*.log", "*.tmp", "node_modules/", "__pycache__/"]
}
```

---

## 🔐 安全说明

| 事项 | 说明 |
| :--- | :--- |
| **只读操作** | 仅允许 status/log/diff/branch/show |
| **禁止修改** | 不允许 commit/push/reset/rebase |
| **超时保护** | 30 秒超时，防止卡死 |
| **路径验证** | 确保指向有效的 Git 仓库 |
| **配置文件** | `config.json` 含个人路径，**不要提交 Git** |

---

## ❓ 常见问题

### Q: 提示 "git 不是内部或外部命令"

**A:** 安装 Git 并添加到系统 PATH：
- Windows: https://git-scm.com/download/win
- 安装后重启终端/编辑器

### Q: 提示 "不是 Git 仓库"

**A:** 确保 `default_project_path` 指向包含 `.git` 文件夹的目录。

### Q: 中文乱码

**A:** 配置 Git：
```bash
git config --global core.quotepath false
git config --global gui.encoding utf-8
```

### Q: MCP 状态红色

**A:** 检查 `config.json` 是否已创建，路径是否正确。

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
| 1.0.0 | 2026-04-02 | 初始版本 |

---

## 📞 反馈

- 📚 主项目：[README](../README.md)
- 📚 安装指南：[docs/installation.md](../docs/installation.md)
- 💬 Issues: [GitHub Issues](https://github.com/Black-do/mcp-server-collection/issues)