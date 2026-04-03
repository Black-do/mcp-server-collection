# MCP Server 安装指南

个人开发的 MCP 服务器集合，用于 Trae/Cursor 等 AI 编辑器，覆盖文件、HTTP、Git、数据库、记忆等全场景。

---

## 📋 目录

1. [前置条件](#前置条件)
2. [项目结构](#项目结构)
3. [快速开始](#快速开始)
4. [各 MCP 安装步骤](#各-mcp-安装步骤)
5. [配置说明](#配置说明)
6. [验证测试](#验证测试)
7. [常见问题](#常见问题)

---

## 前置条件

### 必需软件

| 软件 | 版本要求 | 下载链接 |
| :--- | :--- | :--- |
| **Python** | 3.8+ | https://www.python.org/downloads/ |
| **Node.js** | 16+ | https://nodejs.org/ |
| **Git** | 2.0+ | https://git-scm.com/ |
| **Trae/Cursor** | 最新版 | https://trae.ai/ 或 https://cursor.sh/ |

### 验证安装

```powershell
# 验证 Python
python --version  # 应 >= 3.8

# 验证 Node.js
node --version  # 应 >= 16

# 验证 npm
npm --version

# 验证 Git
git --version