# 06_Amp — How I extend myself through tools

This is the public **amplification layer** of the brain: how I use tools, agents, and
repeatable methods to amplify my work and intelligence. It's where my "meta" lives —
the skills, prompts, templates, and methodology I iterate on and share outward.

> Merged from the former `06_Methodology/` — there is now a single layer, not two.

## Structure

```
06_Amp/
├── Skills/        # Distilled, shareable meta-skills (one subdir each + SKILL.md)
├── Prompt/        # System prompts / operating instructions
│   ├── instructions
│   └── Global Instruction for AI Assistance.md
├── Templates/     # Note templates (Daily, Project, Research)
├── Reference/     # Guides, how-tos, style docs
└── Harness/
    └── global  →  ~/.claude/skills   # symlink to the global skill collection
```

## What lives here

- **Skills/** — meta-skills/meta-tools distilled from real work, written to be reusable
  and shareable. New skills land here (the `skill` action in `clippings-triage` proposes
  drafts into this folder). Each skill is its own subdirectory with a `SKILL.md`.
- **Prompt/** — operating instructions and system prompts that shape how agents work in
  this vault.
- **Templates/** — consistent note scaffolds; referenced by `claude_config.json`
  (`template_folder`) and the `init`/`upgrade` flows.
- **Reference/** — documentation, style guides, learning resources.
- **Harness/global** — symlink to `~/.claude/skills`, the live global skill collection.

## Conventions

- This folder is the orchestration/methodology layer — content (Projects/Areas/Resources)
  lives elsewhere and is orchestrated, not stored here.
- `06_Amp` is its own git repo; commit changes from inside it.
- Outward-facing by design: keep it clean enough to share.
