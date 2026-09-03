# 3026号藏品（Artifact 3026）

> **3026 年会把它认成什么？**

[English](README.md) · 简体中文

[![skills.sh 安装量](https://skills.sh/b/xxwzkdwz/artifact-3026)](https://skills.sh/xxwzkdwz/artifact-3026)
[![License: MIT](https://img.shields.io/badge/License-MIT-b28a50.svg)](LICENSE)

把一件日常物品的照片变成 3026 年博物馆里的虚构藏品：未来考古展陈图、一本正经的展签、馆藏编号，以及可直接分享的 1080×1440 竖版卡片。

Artifact 3026 是一个面向**支持开放 Agent Skills 标准的 AI 助手**的开源 Skill。你正在使用的助手负责创作，仓库提供策展流程和零依赖卡片渲染器；不需要项目方托管服务、共享 API Key、账号、统计或上传接口。

<p align="center">
  <img src="examples/cards/meeting-room-paper-cup.png" width="400" alt="示例：3026 年如何误读一只会议室纸杯">
</p>

## 安装

```bash
npx skills add https://github.com/xxwzkdwz/artifact-3026 --skill artifact-3026
```

安装器会识别支持的 Agent，并让你选择安装位置。完成后附上一张照片，直接问：

```text
使用 artifact-3026：3026 年会把它认成什么？请生成竖版分享卡。
```

<details>
<summary><strong>手动安装与本地开发</strong></summary>

先克隆仓库：

```bash
git clone https://github.com/xxwzkdwz/artifact-3026.git
cd artifact-3026
```

把唯一权威 Skill 安装到不同平台的用户目录：

```bash
# Codex、Cursor、GitHub Copilot
python3 scripts/install_skill.py --platform agents --scope user --mode copy

# Claude / Claude Code
python3 scripts/install_skill.py --platform claude --scope user --mode copy

# Qwen Code
python3 scripts/install_skill.py --platform qwen --scope user --mode copy

# Kimi Code CLI
python3 scripts/install_skill.py --platform kimi --scope user --mode copy
```

开发时可使用 `--mode symlink`，或加上 `--dry-run` 预览目标位置。脚本若发现不同来源的目标已经存在，会停止操作，不会静默覆盖。

如果要给火山引擎 AgentKit 或普通聊天产品手动上传，可生成便携 ZIP：

```bash
python3 scripts/package_skill.py
```

</details>

## 它会生成什么

一次创作可以得到：

- 一张保留原物辨识度的未来博物馆展陈图；
- 藏品名、原用途、未来误读、策展人注释和馆藏编号；
- 可编辑 SVG，以及适合发布的竖版 PNG 分享卡。

你可以指定一本正经、温柔、荒诞或克制的语气，也可以要求保留划痕、磨损，或者保持原物完好、不添加未来损伤。

## 看看 3026 年如何理解今天

下面是六件来自日常生活的“未来藏品”。点击卡片可查看可编辑 SVG；每件藏品还保留了 [JSON 数据](examples/)、[生成场景](examples/scenes/)和 [1080×1440 PNG](examples/cards/)，图像来源见 [examples/SOURCES.md](examples/SOURCES.md)。

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

- **朋友圈 / 小红书打卡**：每天拍一件身边的小东西，连续发布“3026 年会把它认成什么”，慢慢攒出自己的未来博物馆。
- **抖音 / 视频号反差短片**：先展示真实物品，再切到未来展品卡，配上一本正经的展签旁白；也可以让评论区决定下一件入馆藏品。
- **和朋友一起玩**：互相发物品照片，先猜未来人会怎么误解，再揭晓生成结果。
- **做一场私人展览**：把钥匙、耳机、旧票根和书桌物件收成一组，做成生日纪念、旅行回忆或年度生活档案。

发布时可以带上 **#3026号藏品** 或 **#Artifact3026**，附上仓库链接，也欢迎发到 [GitHub Discussions](https://github.com/xxwzkdwz/artifact-3026/discussions)。取得作者同意后，优秀作品可能进入后续社区展厅。

## 在你的 AI 里使用

Artifact 3026 不绑定某一家模型；安装能力取决于承载模型的产品：

| 使用方式 | 平台示例 | 怎么用 |
|---|---|---|
| 开放 Agent Skills 宿主 | Codex、Cursor、GitHub Copilot | 使用上方命令安装，或直接读取 `.agents/skills/artifact-3026/` |
| 兼容 Skill 的宿主 | Claude / Claude Code、Qwen Code、Kimi Code CLI | 能被安装器识别时使用上方命令，否则展开手动安装部分 |
| 自定义 Skill 平台 | 火山引擎 AgentKit | 生成便携 ZIP，按平台流程上传为自定义 Skill |
| 普通聊天产品 | 豆包、智谱清言、通义千问 App/Web、Kimi、DeepSeek | 上传 `SKILL.md` 或便携 ZIP，再使用下方提示词 |

<details>
<summary><strong>没有 Skill 安装器时使用的提示词</strong></summary>

```text
请阅读我上传的 Artifact 3026 Skill。把这张物品照片想象成 3026 年博物馆的藏品，保留主体辨识度，生成未来考古展陈图，并给出藏品名、原用途、未来误读、策展人注释和馆藏编号。如果不能运行仓库渲染器，直接输出文案和图片。
```

</details>

仓库始终只维护一个权威 `SKILL.md`。官方来源、支持边界与本地实测状态见 [COMPATIBILITY.md](COMPATIBILITY.md)。

## 它如何工作

1. 宿主 Agent 观察物品的可见细节，把真实观察与虚构解释分开；
2. 按指定语气写出未来人对这件物品的误读；
3. 如果具备图像生成能力，创作博物馆展陈图，同时保留物品辨识度；
4. 本地渲染器把结构化藏品数据排成统一的 SVG 或 PNG 分享卡。

成品卡不嵌入 AI 生成标识；项目页面与 [examples/SOURCES.md](examples/SOURCES.md) 仍会说明 AI 辅助流程和图像来源。

## 参与完善

欢迎提交新藏品、翻译、渲染器改进和兼容性实测，具体见 [CONTRIBUTING.md](CONTRIBUTING.md)。

<details>
<summary><strong>运行渲染器和发布校验</strong></summary>

```bash
python3 .agents/skills/artifact-3026/scripts/render_exhibit_card.py \
  examples/meeting-room-paper-cup.json \
  --output examples/meeting-room-paper-cup.svg

python3 -m unittest discover -s tests -v
python3 scripts/validate_release.py
skills-ref validate .agents/skills/artifact-3026
```

最后一条需要安装 Agent Skills 参考校验器。仓库测试会覆盖权威目录、元数据、渲染行为、画廊一致性、兼容适配器和便携 ZIP。

</details>

## 创作边界

- 日期、机构、馆藏编号和解释全部属于虚构，不代表真实鉴定、来源、估值或博物馆背书；
- 使用照片前检查人脸、地址、工牌、账号信息等可识别内容；
- 不添加没有依据的品牌标志，不使用雇主机密、专有材料或客户内容。

## 许可证

MIT © 2026 [WANG ZHEN](https://github.com/xxwzkdwz)
