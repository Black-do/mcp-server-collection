#!/usr/bin/env python3
from mcp.server.fastmcp import FastMCP
import subprocess
import json
import os
from typing import Optional

mcp = FastMCP("GitClient")

# 配置文件路径
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

def _load_config() -> dict:
    """加载配置文件"""
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"配置文件不存在：{CONFIG_PATH}")
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _get_project_path(project_name: Optional[str] = None) -> str:
    """
    获取项目路径
    
    Args:
        project_name: 项目标识符（如 "main", "api"），None 则使用默认
    """
    config = _load_config()
    
    # 如果指定了项目名，从 projects 中查找
    if project_name:
        projects = config.get("projects", {})
        if project_name not in projects:
            available = list(projects.keys())
            raise ValueError(f"项目 '{project_name}' 未配置，可用项目：{available}")
        return projects[project_name]["path"]
    
    # 否则使用默认路径（向后兼容）
    default_path = config.get("default_project_path", "")
    if not default_path:
        # 如果也没配置默认，尝试使用第一个项目
        projects = config.get("projects", {})
        if projects:
            first_key = list(projects.keys())[0]
            return projects[first_key]["path"]
        raise ValueError("未配置任何项目路径，请检查 config.json")
    
    return default_path

def _run_git(args: list, project_name: Optional[str] = None) -> str:
    """执行 git 命令"""
    try:
        project_path = _get_project_path(project_name)
        
        # 验证路径
        if not os.path.exists(project_path):
            return f"Error: 项目路径不存在：{project_path}"
        if not os.path.exists(os.path.join(project_path, ".git")):
            return f"Error: '{project_path}' 不是 Git 仓库"
        
        # 执行命令
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
        return "Error: Git 命令超时（30 秒）"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def list_projects() -> str:
    """列出所有可访问的项目"""
    try:
        config = _load_config()
        lines = ["📁 可访问的 Git 项目："]
        
        # 默认项目
        default = config.get("default_project_path", "")
        if default:
            lines.append(f"  • (default) {default}")
        
        # 配置的项目
        projects = config.get("projects", {})
        for key, info in projects.items():
            mark = " (default)" if info["path"] == default else ""
            name = info.get("name", key)
            desc = info.get("description", "")
            lines.append(f"  • {key}: {name}{mark}")
            if desc:
                lines.append(f"      └─ {desc}")
        
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_status(project_name: Optional[str] = None) -> str:
    """查看 Git 状态"""
    return _run_git(["status", "--short"], project_name)

@mcp.tool()
def get_log(limit: int = 10, project_name: Optional[str] = None) -> str:
    """查看提交历史"""
    config = _load_config()
    max_entries = config.get("max_log_entries", 20)
    limit = min(limit, max_entries)
    return _run_git(["log", f"-{limit}", "--oneline"], project_name)

@mcp.tool()
def get_diff(file: Optional[str] = None, project_name: Optional[str] = None) -> str:
    """查看未提交的改动"""
    args = ["diff"]
    if file:
        args.append(file)
    return _run_git(args, project_name)

@mcp.tool()
def get_branches(project_name: Optional[str] = None) -> str:
    """查看分支列表"""
    return _run_git(["branch", "-a"], project_name)

@mcp.tool()
def generate_commit_message(project_name: Optional[str] = None) -> str:
    """根据改动生成 commit message 建议"""
    status = _run_git(["status", "--short"], project_name)
    diff = _run_git(["diff", "--stat"], project_name)
    
    project_info = ""
    if project_name:
        config = _load_config()
        projects = config.get("projects", {})
        if project_name in projects:
            project_info = f"[{projects[project_name].get('name', project_name)}] "
    
    return f"""{project_info}当前改动:
{status}
文件变更:
{diff}
建议 commit message:
- feat: 添加新功能
- fix: 修复 bug
- refactor: 重构代码
- docs: 更新文档
- test: 添加测试"""

@mcp.tool()
def get_current_branch(project_name: Optional[str] = None) -> str:
    """查看当前分支"""
    result = _run_git(["branch", "--show-current"], project_name)
    return result.strip() if result and not result.startswith("Error") else result

if __name__ == "__main__":
    print("GitClient MCP Server 已启动...")
    print(f"配置文件：{CONFIG_PATH}")
    try:
        config = _load_config()
        projects = config.get("projects", {})
        print(f"配置了 {len(projects)} 个项目: {list(projects.keys())}")
    except Exception as e:
        print(f"警告：无法加载配置 - {e}")
    mcp.run()