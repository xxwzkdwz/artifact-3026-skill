# 3026号藏品（Artifact 3026）

> **3026 年会把它认成什么？**

[English](README.md) · 简体中文

[![skills.sh 安装量](https://skills.sh/b/xxwzkdwz/artifact-3026)](https://skills.sh/xxwzkdwz/artifact-3026)
[![License: MIT](https://img.shields.io/badge/License-MIT-b28a50.svg)](LICENSE)

Artifact 3026 是一个面向**支持开放 Agent Skills 标准的 AI 助手**的开源 Skill。它把日常物品的照片或描述变成一件来自未来的虚构博物馆藏品：宿主 Agent 负责策展文案和可选的图像创作，零依赖本地脚本负责稳定生成 1080×1440 分享卡。

<p align="center">
  <img src="examples/cards/meeting-room-paper-cup.png" width="400" alt="示例：3026 年如何误读一只会议室纸杯">
</p>

## 一行安装

```bash
npx skills add https://github.com/xxwzkdwz/artifact-3026 --skill artifact-3026
```

然后附上一张照片，问它：“3026 年会把它认成什么？” 安装器会识别支持的 Agent，并让你选择安装位置。分平台安装和普通聊天产品的使用方法仍在下方[安装](#安装)部分。

## 看看 3026 年如何理解今天

下面是六件来自日常生活的“未来藏品”，有中文也有英文，口吻从一本正经到温柔、荒诞。点击图片可查看可编辑 SVG；每件藏品还保留了 [JSON 数据](examples/)、[生成场景](examples/scenes/)和 [1080×1440 PNG](examples/cards/)，图像来源见 [examples/SOURCES.md](examples/SOURCES.md)。

<table>
  <tr>
    <td width="50%" align="center"><a href="examples/meeting-room-paper-cup.svg"><img src="examples/cards/meeting-room-paper-cup.png" width="180" alt="一次性共识容器"></a><br><strong>一次性共识容器</strong><br><sub>中文 · deadpan</sub></td>
    <td width="50%" align="center"><a href="examples/tangled-charging-cable.svg"><img src="examples/cards/tangled-charging-cable.png" width="180" alt="Portable Energy Umbilical"></a><br><strong>Portable Energy Umbilical</strong><br><sub>English · deadpan</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="examples/forgotten-folding-umbrella.svg"><img src="examples/cards/forgotten-folding-umbrella.png" width="180" alt="Rain Negotiation Device"></a><br><strong>Rain Negotiation Device</strong><br><sub>English · absurd</sub></td>
    <td align="center"><a href="examples/worn-wired-earbuds.svg"><img src="examples/cards/worn-wired-earbuds.png" width="180" alt="私人声音脐带"></a><br><strong>私人声音脐带</strong><br><sub>中文 · tender</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="examples/faded-brass-key.svg"><img src="examples/cards/faded-brass-key.png" width="180" alt="Permission to Return"></a><br><strong>Permission to Return</strong><br><sub>English · tender</sub></td>
    <td align="center"><a href="examples/used-pencil-stub.svg"><img src="examples/cards/used-pencil-stub.png" width="180" alt="可消耗思想探针"></a><br><strong>可消耗思想探针</strong><br><sub>中文 · absurd</sub></td>
  </tr>
</table>

## 生成以后，可以这样玩

- **朋友圈 / 小红书打卡**：每天拍一件身边的小东西，连续发布“3026 年的人会把它认成什么”，慢慢攒出一座属于自己的未来博物馆。
- **抖音 / 视频号反差短片**：先展示真实物品，再切到未来展品卡，配上一本正经的展签旁白；也可以让评论区决定下一件入馆藏品。
- **和朋友一起玩**：互相发一张物品照片，先猜未来人会怎么误解，再揭晓生成结果。情侣、同事、宿舍和家庭旧物都可以做成系列。
- **做一场私人展览**：把一个人的钥匙、耳机、旧票根和书桌物件收成一组，作为生日纪念、旅行回忆或年度生活档案分享出去。

发布时可以带上 **#3026号藏品** 或 **#Artifact3026**，附上仓库链接，也欢迎发到 [GitHub Discussions](https://github.com/xxwzkdwz/artifact-3026/discussions)。取得作者同意后，优秀作品可能进入后续社区展厅。

## 在哪些 AI 里可以用

Artifact 3026 的玩法不绑定某一家模型。区别只在于：有些 Agent 能直接加载 Skill，有些聊天产品需要上传文件或复制提示词。

| 平台 | 怎么用 |
|---|---|
| OpenAI / Codex、Cursor、GitHub Copilot | 直接读取仓库里的 `.agents/skills/artifact-3026/`，也可以安装到用户目录 |
| Claude / Claude Code | 运行安装脚本，放到 Claude 官方识别的 `.claude/skills/` |
| Qwen Code（通义千问） | 运行 `--platform qwen`，放到 `.qwen/skills/` |
| Kimi Code CLI | 项目内可直接读取 `.agents/skills/`；用户级可运行 `--platform kimi` |
| 豆包模型 / 火山引擎 AgentKit | 运行打包脚本，把生成的 ZIP 作为自定义 Skill 上传到 AgentKit |
| 智谱 GLM / GLM Coding Plan | 模型本身不负责安装；在支持 Agent Skills 的编码工具中按该工具的目录加载 |

豆包 App、智谱清言、通义千问 App/Web、Kimi、DeepSeek 等普通聊天产品，也可以读取物品照片并完成创作，但目前不能统一当作“原生安装 Skill”：上传 `SKILL.md` 或便携 ZIP，再附上下面的普通聊天版提示词即可。图片生成和本地分享卡脚本能否执行，取决于具体产品。

> 请阅读我上传的 Artifact 3026 Skill。把这张物品照片想象成 3026 年博物馆的藏品，保留主体辨识度，生成未来考古展陈图，并给出藏品名、原用途、未来误读、策展人注释和馆藏编号。如果不能运行仓库脚本，先直接输出文案和图片。

仓库始终只维护一个权威 `SKILL.md`。以上路径均按官方资料核验，来源、版本边界与本地实测状态见 [COMPATIBILITY.md](COMPATIBILITY.md)。

## 安装

上面的一行安装是最省事的方式。如果希望检查源码或参与开发，可以克隆仓库；支持项目级 `.agents/skills/` 的宿主能直接读取权威目录：

```bash
git clone https://github.com/xxwzkdwz/artifact-3026.git
cd artifact-3026
```

复制到支持开放 `.agents` 约定的用户目录（Codex、Cursor、GitHub Copilot）：

```bash
python3 scripts/install_skill.py --platform agents --scope user --mode copy
```

适配 Claude / Claude Code 的用户目录：

```bash
python3 scripts/install_skill.py --platform claude --scope user --mode copy
```

适配 Qwen Code 或 Kimi Code CLI：

```bash
python3 scripts/install_skill.py --platform qwen --scope user --mode copy
python3 scripts/install_skill.py --platform kimi --scope user --mode copy
```

开发时可把 `--mode copy` 改为 `--mode symlink`。脚本若发现目标已存在会停止，不会覆盖现有 Skill；先用 `--dry-run` 可只查看目标路径。

火山引擎 AgentKit 和没有自动 Skill 加载器的普通聊天产品，可先生成便携包；前者按平台流程上传自定义 Skill，后者手动附加 ZIP，或直接附加 `SKILL.md` 与其资源：

```bash
python3 scripts/package_skill.py
```

AgentKit 使用官方的自定义 Skill 上传流程；普通聊天产品则属于**手动兼容**，能否读取附件和执行本地脚本取决于具体产品，不能宣传为一键安装。

## 使用

附上一张照片或描述一件物品，然后要求宿主 Agent 使用 `artifact-3026`：

```text
使用 artifact-3026：3026 年会把这根打结充电线认成什么？请生成竖版分享卡。
```

可补充：

- `语气冷静严肃，不要堆笑话。`
- `温柔一点，不要搞笑。`
- `保留每一道划痕，只替换背景。`
- `原物完好保存，不要添加未来损伤。`
- `给我三个策展人注释版本。`

项目页面与 [examples/SOURCES.md](examples/SOURCES.md) 会客观说明 AI 辅助流程和图像来源；成品卡画面不嵌入 AI 生成标识。所有解释仍属于创意虚构，不声称真实来源、鉴定、估值或历史真实性。项目不托管推理服务，不要求共享 API Key、账号、统计或上传接口。

## 直接渲染与校验

```bash
python3 .agents/skills/artifact-3026/scripts/render_exhibit_card.py \
  examples/meeting-room-paper-cup.json \
  --output examples/meeting-room-paper-cup.svg

python3 -m unittest discover -s tests -v
python3 scripts/validate_release.py
skills-ref validate .agents/skills/artifact-3026
```

最后一条需要本地已安装官方参考校验器；未安装时，前两项仍会验证目录、元数据、单一 `SKILL.md`、平台中立用语、示例一致性和渲染器行为。

## 仓库结构

- `.agents/skills/artifact-3026/`：唯一权威 Skill、引用资料与零依赖渲染器
- `examples/`：双语示例、场景、SVG 与 PNG 画廊
- `scripts/install_skill.py`：复制/软链接安装适配器
- `scripts/package_skill.py`：普通聊天产品的手动 ZIP 交付
- `scripts/validate_release.py` 与 `tests/`：兼容性、结构与行为验证
- [CONTRIBUTING.md](CONTRIBUTING.md)：社区展品投稿与代码贡献说明

## 隐私与边界

- 使用照片前检查人脸、地址、工牌、账号信息等可识别内容；
- 不添加没有依据的品牌标志，不暗示真实博物馆完成鉴定；
- 日期、馆藏编号、机构与解释全部属于虚构；
- 示例和生成卡不得包含雇主机密、专有材料或客户内容。

## 许可证与作者

MIT © 2026 [WANG ZHEN](https://github.com/xxwzkdwz)
