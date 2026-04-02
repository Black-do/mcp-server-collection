# 🌐 HTTP Client MCP

HTTP 请求测试工具，支持本地和网络 API 调试，让 AI 助手能够直接发送 HTTP 请求。

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

---

## ✨ 功能特性

- ✅ 支持所有 HTTP 方法（GET/POST/PUT/DELETE/PATCH）
- ✅ 自定义 Headers 和 Body
- ✅ URL 查询参数支持
- ✅ 本地 API 快速测试
- ✅ 请求历史记录
- ✅ JSON 响应自动美化
- ✅ 超时控制
- ✅ 详细错误提示

---

## 📁 目录结构

```
http-client/
├── README.md          # 本文件
├── http_mcp.py        # 主代码
├── requirements.txt   # Python 依赖
└── config.json        # 配置文件（可选）
```

---

## 🚀 快速开始

### 1. 安装依赖

```bash
cd http-client
pip install -r requirements.txt
```

### 2. 配置（可选）

编辑 `config.json` 设置默认参数：

```json
{
  "default_timeout": 30,
  "max_response_length": 5000,
  "allowed_methods": ["GET", "POST", "PUT", "DELETE", "PATCH"]
}
```

### 3. 配置 Trae/Cursor

在项目根目录 `mcp.json` 中添加：

```json
{
  "mcpServers": {
    "http-client": {
      "command": "python",
      "args": ["<YOUR_PATH>/http-client/http_mcp.py"],
      "disabled": false
    }
  }
}
```

> ⚠️ **替换 `<YOUR_PATH>`** 为你的实际路径，如 `D:/Workspace/MCPServer`

### 4. 重启编辑器

完全关闭后重新打开，查看底部状态栏 MCP 图标。

---

## 🛠️ 可用工具

| 工具 | 说明 | 参数 |
| :--- | :--- | :--- |
| `http_request` | 完整 HTTP 请求 | method, url, headers, body, params, timeout |
| `get_url` | 快速 GET 请求 | url, params, timeout |
| `post_json` | 快速 POST JSON | url, body, headers, timeout |
| `test_local_api` | 本地接口测试 | path, method, port, body |
| `check_url_status` | URL 状态检查 | url, timeout |
| `get_history` | 查看请求历史 | 无 |

---

## 💡 使用示例

### 测试网络 API

```
用户：用 http-client 访问 https://httpbin.org/get
```

**预期输出：**
```
Status: 200
Headers: {...}
Body: {"args": {}, "headers": {...}, ...}
```

### 发送 POST 请求

```
用户：用 http-client 发送 POST 到 https://httpbin.org/post
     body: {"name": "test", "age": 25}
```

### 测试本地接口

```
用户：用 test_local_api 测试 /api/users 接口，POST 方法
     body: {"name": "test"}
```

### 带查询参数的 GET

```
用户：用 get_url 访问 https://httpbin.org/get
     params: {"page": 1, "size": 10}
```

### 查看请求历史

```
用户：查看最近的请求历史
```

**预期输出：**
```
最近的请求历史：
1. [10:30:15] GET https://httpbin.org/get → 200
2. [10:31:20] POST https://httpbin.org/post → 201
3. [10:32:45] GET http://127.0.0.1:8000/api/users → 200
```

### 检查服务状态

```
用户：检查 http://127.0.0.1:8000 是否可用
```

---

## ⚙️ 配置说明

### config.json（可选）

| 配置项 | 类型 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- |
| `default_timeout` | int | 30 | 默认超时时间（秒） |
| `max_response_length` | int | 5000 | 响应体最大长度 |
| `allowed_methods` | array | 全部 | 允许的 HTTP 方法 |

### mcp.json 配置

```json
{
  "mcpServers": {
    "http-client": {
      "command": "python",
      "args": ["<YOUR_PATH>/http-client/http_mcp.py"],
      "disabled": false
    }
  }
}
```

> ⚠️ **路径格式：** 
> - Windows: `D:/MCPServer/http-client/http_mcp.py` 或 `D:\\...`
> - Mac/Linux: `/Users/username/MCPServer/http-client/http_mcp.py`

---

## 🔐 安全提醒

| 事项 | 说明 |
| :--- | :--- |
| **敏感信息** | 不要在请求中硬编码密码、API Key |
| **生产环境** | 不要连接生产数据库或 API |
| **响应长度** | 已限制 5000 字符，防止 token 爆炸 |
| **超时控制** | 默认 30 秒，防止请求卡死 |
| **配置文件** | `config.json` 不含敏感信息，可提交 Git |

---

## ❓ 常见问题

### Q: 提示 "ModuleNotFoundError: No module named 'httpx'"

**A:** 安装依赖：
```bash
pip install -r requirements.txt
```

### Q: 请求超时

**A:** 增加 timeout 参数或检查网络连接。

### Q: JSON 解析失败

**A:** 确保 headers/body 是合法的 JSON 格式字符串。

### Q: MCP 状态红色

**A:** 检查 `mcp.json` 中的路径是否正确，手动运行测试：
```bash
python http_mcp.py
```

---

## 📄 依赖说明

**requirements.txt**
```txt
mcp>=0.1.0
httpx>=0.25.0
```

| 依赖 | 用途 |
| :--- | :--- |
| `mcp` | MCP 协议支持 |
| `httpx` | HTTP 客户端（支持异步） |

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