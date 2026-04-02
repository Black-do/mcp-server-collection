#!/usr/bin/env python3
from mcp.server.fastmcp import FastMCP
import subprocess
import json
import os

mcp = FastMCP("GitClient")

# ✅ 推荐：从配置文件读取路径
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

def _load_config() -> dict:
    """加载配置文件"""
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"配置文件不存在：{CONFIG_PATH}")
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _get_project_path(project_name: str = None) -> str:
    """获取项目路径"""
    config = _load_config()
    
    # 如果指定了项目名称，从 projects 中查找
    if project_name and "projects" in config:
        if project_name not in config["projects"]:
            raise ValueError(f"项目 '{project_name}' 未配置，可用：{list(config['projects'].keys())}")
        return config["projects"][project_name]
    
    # 否则使用默认路径
    return config.get("default_project_path", "")

def _run_git(args: list, project_name: str = None) -> str:
    """执行 git 命令"""
    try:
        project_path = _get_project_path(project_name)
        if not project_path:
            return "Error: 未配置项目路径，请检查 config.json"
        if not os.path.exists(os.path.join(project_path, ".git")):
            return f"Error: '{project_path}' 不是 Git 仓库"
        
        result = subprocess.run(
            ["git"] + args,
            cwd=project_path,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode != 0:
            return f"Error: {result.stderr}"
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Error: Git 命令超时"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_status(project_name: str = None) -> str:
    """查看 Git 状态"""
    return _run_git(["status", "--short"], project_name)

@mcp.tool()
def get_log(limit: int = 10, project_name: str = None) -> str:
    """查看最近的提交历史"""
    config = _load_config()
    max_entries = config.get("max_log_entries", 20)
    limit = min(limit, max_entries)  # 不超过配置上限
    return _run_git(["log", f"-{limit}", "--oneline"], project_name)

@mcp.tool()
def get_diff(file: str = None, project_name: str = None) -> str:
    """查看未提交的改动"""
    args = ["diff"]
    if file:
        args.append(file)
    return _run_git(args, project_name)

@mcp.tool()
def get_branches(project_name: str = None) -> str:
    """查看分支列表"""
    return _run_git(["branch", "-a"], project_name)

@mcp.tool()
def generate_commit_message(project_name: str = None) -> str:
    """根据改动生成 commit message 建议"""
    status = _run_git(["status", "--short"], project_name)
    diff = _run_git(["diff", "--stat"], project_name)
    return f"当前改动:\n{status}\n\n文件变更:\n{diff}\n\n建议 commit message:\n- feat: 添加新功能\n- fix: 修复 bug\n- refactor: 重构代码"

@mcp.tool()
def list_projects() -> str:
    """列出所有配置的项目"""
    try:
        config = _load_config()
        lines = [f"默认项目：{config.get('default_project_path', '无')}"]
        if "projects" in config:
            lines.append("\n配置的项目:")
            for name, path in config["projects"].items():
                default_mark = " (默认)" if path == config.get("default_project_path") else ""
                lines.append(f"  - {name}: {path}{default_mark}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("GitClient MCP Server 已启动...")
    print(f"配置文件：{CONFIG_PATH}")
    try:
        config = _load_config()
        print(f"默认项目：{config.get('default_project_path', '未配置')}")
    except Exception as e:
        print(f"警告：无法加载配置 - {e}")
    mcp.run()