# Release checklist

Use this checklist before creating a public release of Artifact 3026.

## Identity and ownership

- [ ] Author name is `WANG ZHEN` in `LICENSE` and the canonical Skill metadata.
- [ ] The canonical repository is `https://github.com/xxwzkdwz/artifact-3026`.
- [ ] Display brand is `Artifact 3026 / 3026号藏品`; Skill name and parent directory are both `artifact-3026`.
- [ ] The repository contains exactly one `SKILL.md`, under `.agents/skills/artifact-3026/`.
- [ ] Examples contain no confidential, proprietary, client, or personal information.
- [ ] `output/` remains ignored; owner trial uploads and derivatives are absent from the staged diff.

## Product truth

- [ ] English is the root README, Chinese remains available at `README.zh-CN.md`, and both provide a working language switcher.
- [ ] README says “for AI assistants that support the open Agent Skills standard” and does not claim universal one-click installation.
- [ ] Both READMEs expose the `npx skills add` command near the top and link to community Discussions.
- [ ] Platform-specific behavior is sourced in `COMPATIBILITY.md` and separated from local runtime testing.
- [ ] Canonical Skill instructions use host-neutral terms and contain no platform-specific wrapper.
- [ ] Public JPG scenes, finished SVG cards, and PNG share cards contain no AI-generation, AI-assistance, virtual-generation, or equivalent badge/watermark.
- [ ] README and `examples/SOURCES.md` still describe the AI-assisted workflow and preserve scene provenance.
- [ ] No label claims real provenance, authentication, valuation, or museum affiliation.

## Verification

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_release.py
skills-ref validate .agents/skills/artifact-3026
```

- [ ] The 12 renderer and Skill contract tests pass.
- [ ] Repository validation passes copy, symlink, portable ZIP, metadata, structure, terminology, gallery, and hygiene checks.
- [ ] `skills-ref` passes when the reference validator is available; otherwise record it as unavailable rather than substituting an invented command.
- [ ] All six public examples include portable JSON, recorded scene provenance, editable SVG, and a 1080×1440 PNG.
- [ ] `.github/assets/social-preview.jpg` is 1280×640, below 1 MB, and uploaded as the repository social preview.
- [ ] Installer dry runs point OpenAI/Codex, Cursor, GitHub Copilot, and project-level Kimi Code CLI to `.agents/skills`; Claude to `.claude/skills`; Qwen Code to `.qwen/skills`; and user-level Kimi Code CLI to `.config/agents/skills`.

## Publication

- [ ] Review the staged diff and commit identity before pushing.
- [ ] Keep the public repository name aligned with the Artifact 3026 brand and installation instructions.
- [ ] Do not add analytics, hosted inference, payments, or user uploads without a separate design and privacy review.
