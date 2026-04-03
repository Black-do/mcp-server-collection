# 更新日志

所有重要的项目变更将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

---

## [未发布]

### Added
- Git Client 多项目支持，可配置和切换多个 Git 仓库
- Git Client `list_projects` 工具，列出所有可访问项目
- Git Client `get_current_branch` 工具，查看当前分支
- 配置模板 `config.json.example` 支持多项目格式

### Changed
- Git Client 所有工具函数支持 `project_name` 参数
- 更新 README 文档，添加多项目配置说明
- 更新 git-client/README.md，突出多项目功能

### Deprecated
- 无

### Removed
- 无

### Fixed
- 无

### Security
- 无

---

## [1.0.0] - 2026-04-02

### Added
- HTTP Client MCP
- Git Client MCP
- Database Client MCP
- Memory Client MCP
- Filesystem MCP 集成
- 完整文档和配置模板