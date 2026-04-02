#!/usr/bin/env python3
from mcp.server.fastmcp import FastMCP
import httpx
import json
from datetime import datetime
from typing import Optional

mcp = FastMCP("HTTPClient")

# 请求历史记录（内存存储，重启清空）
request_history = []
MAX_HISTORY = 20  # 最多保留 20 条

def _save_history(method: str, url: str, status: int):
    """保存请求历史"""
    request_history.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "method": method,
        "url": url,
        "status": status
    })
    if len(request_history) > MAX_HISTORY:
        request_history.pop(0)

def _format_response(resp: httpx.Response) -> str:
    """智能格式化响应内容"""
    content_type = resp.headers.get("content-type", "").lower()
    body = resp.text[:5000]  # 限制长度
    
    # 尝试美化 JSON
    if "application/json" in content_type:
        try:
            body = json.dumps(resp.json(), indent=2, ensure_ascii=False)[:5000]
        except:
            pass
    
    return f"""Status: {resp.status_code}
Headers: {json.dumps(dict(resp.headers), indent=2, ensure_ascii=False)}
Body:
{body}"""

@mcp.tool()
async def http_request(
    method: str,
    url: str,
    headers: str = "{}",
    body: str = "{}",
    params: str = "{}",
    timeout: int = 30
) -> str:
    """
    发送 HTTP 请求（完整版）
    
    Args:
        method: HTTP 方法 (GET/POST/PUT/DELETE/PATCH)
        url: 请求 URL
        headers: JSON 格式的请求头
        body: JSON 格式的请求体（POST/PUT/PATCH 时使用）
        params: JSON 格式的查询参数（URL 参数）
        timeout: 超时时间（秒）
    
    Returns:
        响应状态码、头和内容
    """
    try:
        headers_dict = json.loads(headers) if headers else {}
        body_dict = json.loads(body) if body else None
        params_dict = json.loads(params) if params else {}
        
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.request(
                method=method.upper(),
                url=url,
                headers=headers_dict,
                params=params_dict,
                json=body_dict if method.upper() in ["POST", "PUT", "PATCH"] else None
            )
            
            _save_history(method.upper(), url, resp.status_code)
            return _format_response(resp)
            
    except httpx.TimeoutException:
        return f"Error: Request timeout ({timeout}s)"
    except httpx.ConnectError as e:
        return f"Error: Connection failed - {str(e)}"
    except json.JSONDecodeError as e:
        return f"Error: Invalid JSON format - {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def get_url(url: str, params: str = "{}", timeout: int = 30) -> str:
    """快速 GET 请求"""
    return await http_request("GET", url, "{}", "{}", params, timeout)

@mcp.tool()
async def post_json(url: str, body: str, headers: str = "{}", timeout: int = 30) -> str:
    """快速 POST JSON 请求"""
    return await http_request("POST", url, headers, body, "{}", timeout)

@mcp.tool()
async def get_history() -> str:
    """查看最近的请求历史"""
    if not request_history:
        return "暂无请求历史"
    
    lines = ["最近的请求历史："]
    for i, req in enumerate(request_history[-10:], 1):
        lines.append(f"{i}. [{req['time']}] {req['method']} {req['url']} → {req['status']}")
    return "\n".join(lines)

@mcp.tool()
async def test_local_api(
    path: str,
    method: str = "GET",
    port: int = 8000,
    body: str = "{}"
) -> str:
    """
    快速测试本地 API（简化本地测试）
    
    Args:
        path: API 路径（如 /api/users）
        method: HTTP 方法
        port: 本地服务端口（默认 8000）
        body: JSON 格式的请求体
    """
    url = f"http://127.0.0.1:{port}{path}"
    return await http_request(method, url, "{}", body, "{}", 10)

@mcp.tool()
async def check_url_status(url: str, timeout: int = 10) -> str:
    """
    快速检查 URL 状态（只返回状态码）
    
    Args:
        url: 要检查的 URL
        timeout: 超时时间
    """
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.head(url, follow_redirects=True)
            return f"URL: {url}\nStatus: {resp.status_code}\nServer: {resp.headers.get('server', 'Unknown')}"
    except Exception as e:
        return f"URL: {url}\nError: {str(e)}"

if __name__ == "__main__":
    print("HTTPClient MCP Server 已启动...")
    print("可用工具：http_request, get_url, post_json, get_history, test_local_api, check_url_status")
    mcp.run()