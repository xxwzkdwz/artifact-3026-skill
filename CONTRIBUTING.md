# Contributing to Artifact 3026

Artifact 3026 welcomes new artifacts, language improvements, compatibility reports, and focused fixes. Keep every contribution aligned with the project's fictional museum premise and privacy boundaries.

## Share a community artifact

The lightest way to participate is to post your result in [GitHub Discussions](https://github.com/xxwzkdwz/artifact-3026/discussions). Please include:

- the finished exhibit card;
- a short description of the original object;
- the host agent or chat product you used;
- the tone you requested (`deadpan`, `tender`, or `absurd`);
- confirmation that you own or have permission to share the source and result.

Use **#Artifact3026** or **#3026号藏品** when sharing publicly. Avoid faces, addresses, workplace badges, account details, confidential materials, unsupported brand marks, or claims of real museum authentication.

## Add a repository example

Open a pull request only when the example is safe to redistribute. A complete example includes:

- portable JSON under `examples/`;
- the generated museum scene under `examples/scenes/`;
- an editable SVG and a 1080×1440 PNG card;
- an entry in `examples/SOURCES.md` recording provenance and permission.

Run the checks before submitting:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_release.py
```

## Improve the Skill

The repository intentionally keeps one canonical instruction file at `.agents/skills/artifact-3026/SKILL.md`. Platform adapters must copy or link that directory rather than introducing another `SKILL.md`. Keep canonical instructions vendor-neutral and document platform-specific behavior in `COMPATIBILITY.md`.

Small, reviewable pull requests are preferred. Explain the user-visible problem, the proposed change, and how you verified it.

## 中文说明

欢迎在 GitHub Discussions 分享你的“3026号藏品”，也欢迎提交语言修订、兼容性报告和小范围代码改进。请确认图片和物品由你拥有或已获授权，避免上传人脸、地址、工牌、账号信息、雇主材料或其他敏感内容。仓库示例需要同时提供 JSON、场景图、SVG、1080×1440 PNG，并在 `examples/SOURCES.md` 记录来源。
