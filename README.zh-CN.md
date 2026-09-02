# 未来博物馆策展人

> **3026 年会把它认成什么？**

[English README](README.md)

Future Museum Curator 是一个开源 Codex Skill：把日常物品的照片或描述，变成来自未来的虚构博物馆藏品。Codex 负责策展概念、文案，以及在用户已有图像能力可用时完成场景转化；零依赖本地脚本负责稳定生成 1080×1440 分享卡。

![示例：3026 年如何误读一只会议室纸杯](examples/cards/meeting-room-paper-cup.png)

## 示例画廊

六件物品、三种口吻、两种语言。每个示例都包含[展签数据](examples/)、生成的[博物馆场景](examples/scenes/)、可编辑 SVG 和最终 PNG 分享卡；图像来源记录见 [examples/SOURCES.md](examples/SOURCES.md)。

<table>
  <tr>
    <td width="50%"><img src="examples/cards/meeting-room-paper-cup.png" alt="会议室纸杯未来博物馆卡"><br><strong>一次性共识容器</strong> · 中文 · deadpan<br><a href="examples/meeting-room-paper-cup.json">数据</a> · <a href="examples/scenes/meeting-room-paper-cup.jpg">场景</a> · <a href="examples/meeting-room-paper-cup.svg">SVG</a></td>
    <td width="50%"><img src="examples/cards/tangled-charging-cable.png" alt="打结充电线未来博物馆卡"><br><strong>Portable Energy Umbilical</strong> · English · deadpan<br><a href="examples/tangled-charging-cable.json">数据</a> · <a href="examples/scenes/tangled-charging-cable.jpg">场景</a> · <a href="examples/tangled-charging-cable.svg">SVG</a></td>
  </tr>
  <tr>
    <td><img src="examples/cards/forgotten-folding-umbrella.png" alt="遗忘折叠伞未来博物馆卡"><br><strong>Rain Negotiation Device</strong> · English · absurd<br><a href="examples/forgotten-folding-umbrella.json">数据</a> · <a href="examples/scenes/forgotten-folding-umbrella.jpg">场景</a> · <a href="examples/forgotten-folding-umbrella.svg">SVG</a></td>
    <td><img src="examples/cards/worn-wired-earbuds.png" alt="旧有线耳机未来博物馆卡"><br><strong>私人声音脐带</strong> · 中文 · tender<br><a href="examples/worn-wired-earbuds.json">数据</a> · <a href="examples/scenes/worn-wired-earbuds.jpg">场景</a> · <a href="examples/worn-wired-earbuds.svg">SVG</a></td>
  </tr>
  <tr>
    <td><img src="examples/cards/faded-brass-key.png" alt="褪色黄铜钥匙未来博物馆卡"><br><strong>Permission to Return</strong> · English · tender<br><a href="examples/faded-brass-key.json">数据</a> · <a href="examples/scenes/faded-brass-key.jpg">场景</a> · <a href="examples/faded-brass-key.svg">SVG</a></td>
    <td><img src="examples/cards/used-pencil-stub.png" alt="铅笔头未来博物馆卡"><br><strong>可消耗思想探针</strong> · 中文 · absurd<br><a href="examples/used-pencil-stub.json">数据</a> · <a href="examples/scenes/used-pencil-stub.jpg">场景</a> · <a href="examples/used-pencil-stub.svg">SVG</a></td>
  </tr>
</table>

## 为什么有人会想试

钩子只有一句：给未来一件普通物品，看看它会误解成什么。

- 打结充电线变成“便携能源脐带”；
- 被遗忘的雨伞变成“降水协商装置”；
- 会议室纸杯变成古代会议仪式的证据。

好结果不是随机科幻，而是从一个真实的当代习惯出发，再让未来策展人一本正经地误读半步。

它也不是只玩一次的滤镜：可以每次从书桌、背包、厨房或家庭旧物里选一件，用同一句问题和同一套卡片持续做成系列。物品和人的习惯不断变化，分享格式保持可识别。

## 为什么做成 Codex Skill

创作流程运行在用户自己的 Codex 环境中：

- 项目不维护集中式推理服务；
- 不共享 API Key；
- 不要求账号、统计或上传接口；
- 仓库维护者不承担按图片计费的推理成本。

如果用户环境已有图像生成或编辑能力，Skill 会用它把真实物品放进未来展柜。没有图像能力时，也会继续产出展签、可复用生图提示和纯排版分享卡。

默认画面把物品当作“千年后的考古幸存物”：主体仍可识别，但允许符合材质的褪色、磨损、修复痕迹，并采用有纵深的偏侧馆藏镜头。如果希望原物保持今天的状态，可明确要求 `original-condition preservation`（原物完好保存）。

## 安装

可以让 Codex 安装：

```text
$skill-installer install https://github.com/xxwzkdwz/future-museum-curator
```

本地开发：

```bash
git clone https://github.com/xxwzkdwz/future-museum-curator.git
cd future-museum-curator
mkdir -p "$HOME/.agents/skills"
ln -s "$(pwd)/skills/future-museum-curator" "$HOME/.agents/skills/future-museum-curator"
```

## 试一试

附上一张照片或描述一件物品，然后输入：

```text
$future-museum-curator 3026 年会把这根打结充电线认成什么？
```

也可以补充：

- `语气冷静严肃，不要堆笑话。`
- `温柔一点，不要搞笑。`
- `保留每一道划痕，只替换背景。`
- `原物完好保存，不要添加未来损伤。`
- `给我三个策展人注释版本。`
- `生成竖版分享卡。`

每张渲染卡都会明确标注“AI辅助虚构内容”，不声称真实来源、鉴定、估值或历史真实性。

## 工作方式

```text
物品照片或描述
      ↓
一个只属于它的当代习惯
      ↓
未来策展人的虚构解释
      ↓
可选：使用用户自己的 Codex 图像能力
      ↓
本地确定性 SVG 排版
      ↓
自包含 1080×1440 分享卡
```

这个拆分是项目的核心：AI 负责场景转化和策展创意，本地脚本负责稳定排版、披露与导出。

## 直接渲染分享卡

```bash
python3 skills/future-museum-curator/scripts/render_exhibit_card.py \
  examples/meeting-room-paper-cup.json \
  --output examples/meeting-room-paper-cup.svg
```

渲染器只使用 Python 标准库，支持 UTF-8 中文和英文，并可把本地 PNG、JPEG、GIF、WebP 或 SVG 嵌入自包含分享卡。

## 开发与校验

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_release.py
python3 /path/to/skill-creator/scripts/quick_validate.py skills/future-museum-curator
python3 /path/to/plugin-creator/scripts/validate_plugin.py .
```

前两项只需要 Python 3.11+，可在任意干净 CI 环境运行；后两项使用 Codex 自带校验器。

## 隐私和边界

- 使用照片前检查人脸、地址、工牌、账号信息等可识别内容；
- 不添加没有依据的品牌标志，不暗示真实博物馆完成鉴定；
- 日期、馆藏编号、机构与解释全部属于虚构；
- 示例和生成卡不得包含雇主机密、专有材料或客户内容。

## 许可证与作者

MIT © 2026 [WANG ZHEN](https://github.com/xxwzkdwz)
