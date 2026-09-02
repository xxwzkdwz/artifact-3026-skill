# 兼容性证据与验证边界

核验日期：2026-09-03。本文只记录官方文档能够支持的结论，并把“官方原生支持”“本地结构/脚本验证”“尚未运行真实客户端”分开。

## 开放标准基线

- [Agent Skills Specification](https://agentskills.io/specification)：Skill 是包含 `SKILL.md` 的目录，可附带 `scripts/`、`references/`、`assets/`；`name` 必须与父目录匹配。官方参考命令为 `skills-ref validate <path>`。
- [How to add skills support to your agent](https://agentskills.io/client-implementation/adding-skills-support)：`.agents/skills/` 是建议的通用项目目录。
- 本仓库只有一个 `SKILL.md`：`.agents/skills/artifact-3026/SKILL.md`。Claude 适配与 ZIP 交付均从这个目录复制或链接，不提交第二份指令。

## 平台矩阵

| 平台 | 官方证据 | 官方原生位置 | 本仓库验证状态 | 结论 |
|---|---|---|---|---|
| OpenAI / Codex | [Build skills](https://developers.openai.com/codex/skills) 明确称其基于开放 Agent Skills 标准，并说明 Codex 扫描项目到仓库根目录的 `.agents/skills`、用户级 `~/.agents/skills`，支持软链接 | `.agents/skills/`、`~/.agents/skills/` | 权威目录、复制和软链接模式均由自动测试验证；当前工作在 Codex 桌面环境中完成，但未另行创建新会话检查 Skill 选择器 UI | **官方原生 + 本地结构/脚本验证** |
| Cursor | [Cursor Agent Skills](https://prod.cursor.com/docs/skills) 明确称其为开放标准，并列出项目/用户 `.agents/skills` | `.agents/skills/`、`~/.agents/skills/` | 权威目录和安装脚本已验证；本机没有可用于验收的 Cursor CLI 会话 | **官方原生，客户端运行未验证** |
| GitHub Copilot | [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) 将 Agent Skills 定义为开放标准，列出 `.agents/skills` 与 `~/.agents/skills`；[Adding agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) 说明支持的 Copilot 体验 | `.agents/skills/`、`~/.agents/skills/` | `gh 2.98.0` 的 `gh skill` 已从本地权威目录成功发现并复制全部资源；Copilot Agent 本身未运行 | **官方原生 + GitHub CLI 打包验证；Agent 运行未验证** |
| Claude / Claude Code | [Extend Claude with skills](https://code.claude.com/docs/en/slash-commands) 明确称 Claude Code Skills 遵循开放 Agent Skills 标准，但使用 `.claude/skills`；[Agent Skills in the SDK](https://code.claude.com/docs/en/agent-sdk/skills) 说明自动发现范围 | `.claude/skills/`、`~/.claude/skills/` | 安装器把唯一权威目录复制或链接到官方位置，并在临时目录中验证；本机若无 Claude Code CLI，不宣称运行验证 | **标准兼容，经适配安装；客户端运行待验证** |

## 安装器与普通聊天产品

`scripts/install_skill.py` 只实现两种公开、可审计的文件操作：

- `agents`、`codex`、`cursor`、`copilot` 目标映射到 `.agents/skills/artifact-3026`；
- `claude` 目标映射到 `.claude/skills/artifact-3026`；
- `copy` 复制权威目录，`symlink` 创建到权威目录的链接；
- 若目标已存在且不是同一源目录，立即失败，不覆盖用户文件。

没有自动 Skill 加载器的普通聊天产品，只能使用 `scripts/package_skill.py` 生成 ZIP 后手动附加。该方式要求产品能够读取附件；若还要生成分享卡，则需要本地执行 Python 脚本的能力。因此它只标为**手动兼容**。

## 本机验证快照

- 开放标准参考实现：从 [agentskills/agentskills](https://github.com/agentskills/agentskills/tree/main/skills-ref) 当日 `main` 构建并运行 `skills-ref validate`，结果为 `Valid skill`。
- 通用结构校验：本机 Skill Creator 的 `quick_validate.py` 返回 `Skill is valid!`。
- 行为验证：原有 12 项单元测试全部通过；仓库校验器还在临时目录完成 `.agents` 复制、Claude `.claude` 软链接和 ZIP 内容验证。
- GitHub CLI：`gh 2.98.0` 提供预览版 `gh skill`；使用 `--from-local --allow-hidden-dirs --dir <临时目录>` 已成功发现并复制 `artifact-3026` 及全部资源。
- OpenAI/Codex：本机存在 `codex-cli 0.151.0-alpha.7.2`，且当前任务运行在 Codex 桌面环境；未为了截图另开任务或产生额外运行。
- Claude Code、Cursor 与 GitHub Copilot 独立客户端命令在本机不可用，所以只标记为官方路径兼容，不冒充端到端运行验证。

## 不做的兼容性声明

- 不声称所有 AI 助手都支持 Agent Skills。
- 不声称任何平台都能从 GitHub URL 一键安装。
- 不把 `.codex-plugin/plugin.json` 当作主交付；当前版本不提交该文件。
- 不提交平台专属 `agents/openai.yaml`，以确保权威目录的表述和内容保持供应商中立。以后如需平台 UI 元数据，应放入明确标注的可选适配层，并仍只引用权威 Skill。
