# 更新日志

## [1.1.0] - 2026-04-03

### Added
- Git Client 多项目支持，可配置和切换多个 Git 仓库
- Git Client `list_projects` 工具，列出所有可访问项目
- Git Client `get_current_branch` 工具，查看当前分支
- 根目录 README 添加外部依赖说明（Filesystem MCP）

### Changed
- Git Client 所有工具函数支持 `project_name` 参数
- 更新 README 文档，区分官方包和自研模块
- 更新 git-client/README.md，突出多项目功能
- 更新配置模板支持多项目格式

### Fixed
- 修复作者名称显示问题
- 修复路径配置安全问题

### Security
- 敏感配置文件已加入 .gitignore
- 配置模板使用占位符替代实际路径

---

## [1.0.0] - 2026-04-02
...