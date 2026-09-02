# Release checklist

Use this checklist before creating a public GitHub release.

## Identity and ownership

- [ ] Author name is `WANG ZHEN` in `LICENSE` and `.codex-plugin/plugin.json`.
- [ ] GitHub account is `xxwzkdwz` and the canonical repository URL is `https://github.com/xxwzkdwz/future-museum-curator`.
- [ ] The repository owner has confirmed that every file may be released under MIT.
- [ ] Examples contain no employer-confidential, proprietary, client, or personal information.
- [ ] `output/` remains ignored; Owner trial uploads and derivatives are absent from the staged diff.

## Product truth

- [ ] README does not imply that this repository hosts image inference or pays users' generation costs.
- [ ] Example cards visibly disclose `AI-ASSISTED FICTION · AI辅助虚构内容`.
- [ ] No generated label claims real provenance, authentication, valuation, or museum affiliation.
- [ ] Install commands use the actual public repository URL.

## Verification

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_release.py
python3 /path/to/skill-creator/scripts/quick_validate.py skills/future-museum-curator
python3 /path/to/plugin-creator/scripts/validate_plugin.py .
```

- [ ] All generated SVG examples match their JSON inputs.
- [ ] All six public examples include portable JSON, an AI-generated scene with recorded provenance, editable SVG, and a 1080×1440 PNG card.
- [ ] Example cards render correctly in GitHub's file preview and a local browser.
- [ ] A clean Codex conversation can invoke `$future-museum-curator` from the installed skill.
- [ ] The repository description uses the hook: `What will 3026 think this was?`

## Publication

- [ ] Create the repository under the confirmed account.
- [ ] Push only after reviewing the staged diff and commit identity.
- [ ] Add topics such as `codex`, `agent-skill`, `creative-coding`, `image-generation`, and `svg`.
- [ ] Do not add analytics, hosted inference, payments, or user uploads without a separate design and privacy review.
