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
| Qwen Code（通义千问） | [Qwen Code Skills](https://qwenlm.github.io/qwen-code-docs/zh/users/features/skills/) 明确支持以 `SKILL.md` 为核心的 Agent Skills，并列出项目与用户目录 | `.qwen/skills/`、`~/.qwen/skills/` | 安装器的项目级与用户级路径均由自动测试验证；未运行 Qwen Code 客户端 | **官方原生，经适配安装；客户端运行待验证** |
| Kimi Code CLI | [Kimi Code CLI Skills](https://github.com/MoonshotAI/kimi-cli/blob/main/docs/en/customization/skills.md) 明确支持开放 Agent Skills，并识别通用及多家兼容目录 | 项目 `.agents/skills/`；用户级推荐 `~/.config/agents/skills/`，也识别 `~/.agents/skills/` | 项目内权威目录可直接发现；用户级安装路径由自动测试验证；未运行 Kimi Code CLI | **官方原生 + 本地结构/脚本验证；客户端运行待验证** |
| 豆包模型 / 火山引擎 AgentKit | [AgentKit 自定义 Skills](https://www.volcengine.com/docs/86681/2205064) 说明可上传包含根目录与 `SKILL.md` 的 ZIP 代码包 | 平台上传的自定义 Skill 包，不是豆包 App 的本地目录 | 便携 ZIP 的唯一根 Skill、`SKILL.md` 与资源结构由自动测试验证；未在 AgentKit 控制台实际上传 | **AgentKit 官方支持 ZIP Skill；平台运行待验证** |
| 智谱 GLM / GLM Coding Plan | [Agentic 开发扩展](https://docs.bigmodel.cn/cn/coding-plan/learning-resources/agentic-extension) 介绍 Skills 作为 Coding Agent 扩展能力；GLM 可由兼容编码工具承载 | 取决于所使用的编码 Agent，而不是 GLM 模型本身 | 可使用上表已支持宿主的安装方式；未找到“智谱清言原生安装 `SKILL.md`”的官方依据 | **宿主相关兼容，不宣称智谱聊天产品原生安装** |

## 安装器与普通聊天产品

面向公开分发，README 首选开放生态安装命令：

```bash
npx skills add https://github.com/xxwzkdwz/artifact-3026-skill --skill artifact-3026
```

`skills` CLI 会从 GitHub 发现唯一权威 Skill，并让用户选择支持的 Agent。仓库自带的 `scripts/install_skill.py` 仍用于明确指定平台路径、离线审阅或开发态软链接：

`scripts/install_skill.py` 只实现两种公开、可审计的文件操作：

- `agents`、`codex`、`cursor`、`copilot` 目标映射到 `.agents/skills/artifact-3026`；
- `claude` 目标映射到 `.claude/skills/artifact-3026`；
- `qwen` 目标映射到 `.qwen/skills/artifact-3026`；
- `kimi` 的项目级目标沿用 `.agents/skills/artifact-3026`，用户级目标使用官方推荐的 `~/.config/agents/skills/artifact-3026`；
- `copy` 复制权威目录，`symlink` 创建到权威目录的链接；
- 若目标已存在且不是同一源目录，立即失败，不覆盖用户文件。

豆包 App、智谱清言、通义千问 App/Web、Kimi、DeepSeek 等普通聊天产品，可使用 `scripts/package_skill.py` 生成 ZIP 后手动附加，或复制 README 中的普通聊天版提示词。该方式要求产品能够读取附件；若还要运行仓库的分享卡渲染器，则需要本地执行 Python 脚本的能力。因此它只标为**手动兼容**，不与火山引擎 AgentKit 的自定义 Skill 上传能力混为一谈。

## 本机验证快照

- 开放标准参考实现：从 [agentskills/agentskills](https://github.com/agentskills/agentskills/tree/main/skills-ref) 当日 `main` 构建并运行 `skills-ref validate`，结果为 `Valid skill`。
- 通用结构校验：本机 Skill Creator 的 `quick_validate.py` 返回 `Skill is valid!`。
- 行为验证：原有 12 项单元测试全部通过；仓库校验器还在临时目录完成 `.agents` 复制、Claude `.claude` 软链接、Qwen 与 Kimi 路径以及 ZIP 内容验证。
- GitHub CLI：`gh 2.98.0` 提供预览版 `gh skill`；使用 `--from-local --allow-hidden-dirs --dir <临时目录>` 已成功发现并复制 `artifact-3026` 及全部资源。
- skills.sh：`skills 1.5.23` 已通过公开 GitHub URL 发现唯一 Skill，并在隔离的临时 Codex 项目中完成复制安装；仓库更名后的公开条目为 [artifact-3026-skill](https://skills.sh/xxwzkdwz/artifact-3026-skill/artifact-3026)。
- OpenAI/Codex：本机存在 `codex-cli 0.151.0-alpha.7.2`，且当前任务运行在 Codex 桌面环境；未为了截图另开任务或产生额外运行。
- Claude Code、Cursor、GitHub Copilot、Qwen Code 与 Kimi Code CLI 独立客户端未做端到端运行，所以只按实际证据标记，不冒充完整客户端验证。

## 不做的兼容性声明

- 不声称所有 AI 助手都支持 Agent Skills。
- 不声称任何平台都能从 GitHub URL 一键安装。
- 不把 `.codex-plugin/plugin.json` 当作主交付；当前版本不提交该文件。
- 不提交平台专属 `agents/openai.yaml`，以确保权威目录的表述和内容保持供应商中立。以后如需平台 UI 元数据，应放入明确标注的可选适配层，并仍只引用权威 Skill。
