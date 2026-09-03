# 命名研究与选择记录

调研日期：2026-09-03。目标是让展示品牌、仓库名和用户调用的 Skill 名保持一致，同时兼顾记忆度、搜索辨识度与传播性。

## 可核验样本

公开生态样本显示，强势 Skill 名通常是短词或直接的动词/对象组合，而不是带供应商后缀的长名称：

- [skills.sh 排行榜](https://skills.sh/) 当日可见 `find-skills`（约 320 万安装）、`grill-me`（约 100 万）、`frontend-design`（约 84.6 万）、`tdd`（约 82.3 万）、`agent-browser`（约 77.4 万）、`web-design-guidelines`（约 60.1 万）。安装数会变化，此处仅为当日快照。
- [anthropics/skills](https://github.com/anthropics/skills) 的目录名包括 `algorithmic-art`、`canvas-design`、`doc-coauthoring`、`frontend-design`、`mcp-builder`；GitHub API 当日显示约 173,203 stars。
- [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) 使用 `composition-patterns`、`react-best-practices`、`web-design-guidelines` 等功能导向名称；当日约 30,746 stars。
- [vercel-labs/skills](https://github.com/vercel-labs/skills) 提供跨 Agent 安装工具；当日约 30,235 stars。
- [github/awesome-copilot](https://github.com/github/awesome-copilot) 中可见 `acquire-codebase-knowledge`、`anti-ui-slop`、`appinsights-instrumentation` 等可预判输出的名称；当日约 38,555 stars。

归纳出的破圈特征：短、易读、能想象输出、供应商中立、自然英语、搜索歧义低、适合 hashtag 与视觉品牌。应避免长串 `xxx-agent-skill`、Codex 专属词、过度抽象或只描述实现方式的名字。

## 候选评分

满分 5；“搜索竞争”分数越高代表同名污染越低。评分是产品判断，不是商标法律意见。

| 候选 | 记忆度 | 功能清晰 | 国际传播 | 搜索竞争 | 扩展空间 | 合计 | 反证摘要 |
|---|---:|---:|---:|---:|---:|---:|---|
| **Artifact 3026** | 5 | 4 | 5 | 5 | 5 | **24** | GitHub 精确检索无同名仓库；数字形成故事钩子，也可扩展为系列、画廊或年度版本 |
| Museum of Now | 4 | 4 | 4 | 3 | 5 | 20 | 已有 `Museum Now` 项目，且“museum of …”机构命名较拥挤；概念好但搜索边界较弱 |
| Ordinary Relics | 4 | 4 | 4 | 4 | 4 | 20 | GitHub 精确检索污染低，但 `relics` 容易偏向宗教、收藏或游戏语境 |
| Relicmaker | 4 | 3 | 4 | 5 | 4 | 20 | GitHub 精确检索无明显同名；动作感强，但不直接传达未来博物馆与 3026 钩子 |
| Tomorrow's Archive | 4 | 4 | 4 | 4 | 4 | 20 | 语义自然、扩展性好，但更像文档归档工具，物品视觉输出不够直观 |
| Future Relic | 5 | 5 | 4 | 1 | 4 | 19 | 与 Daniel Arsham 的 *Future Relic* 同类艺术系列高度重叠，且存在相关美国商标申请与多个商业使用；本项目也做“日常物品的未来考古”，混淆风险过高 |
| Aftertime | 4 | 2 | 4 | 2 | 5 | 17 | 已有 App、开源项目、音乐等同名使用；过于抽象，无法预判输出 |

## 决策

采用：

- **展示品牌：Artifact 3026 / 3026号藏品**
- **Skill 标识和目录：`artifact-3026`**
- **仓库名与 URL：`artifact-3026-skill` / `https://github.com/xxwzkdwz/artifact-3026-skill`**

理由：`Artifact 3026` 在不借用现有知名艺术系列名称的前提下，保留了“未来把当下错认成文物”的故事。它短、自然、可形成 `#Artifact3026`，又能让输出物（artifact）和时间钩子（3026）立即可见。`artifact-3026` 满足开放 Agent Skills 的小写连字符规则。

展示品牌继续保持简洁的 `Artifact 3026`，仓库名使用 `artifact-3026-skill`，让 GitHub 搜索结果和外部分享在脱离上下文时也能立即表明它是一个 Skill。内部 Skill 标识仍为 `artifact-3026`，避免安装后的调用名称变长。旧仓库地址由 GitHub 自动重定向，仅用于兼容已经分享出去的链接，不再作为首页内容强调。

## 风险边界

- GitHub 与公开网页检索不能替代完整商标清查；未来若商业化，应在目标法域按软件、出版、艺术与数字商品相关类别做专业检索。
- `Artifact` 是通用词，品牌辨识主要来自 `3026` 的组合；发布视觉应始终保留数字。
- `Future Relic` 因与现有艺术系列的主题和表达都高度接近，已从品牌候选中淘汰，也不应作为对外主标签。
