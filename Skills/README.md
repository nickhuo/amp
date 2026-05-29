# Skills — distilled meta-skills

Reusable, shareable skills distilled from real work. Each skill is one subdirectory
holding a `SKILL.md` (and any supporting files).

## What belongs here

A skill earns a place here when a workflow or tool-usage pattern has **recurred** enough
that capturing it pays off — turning a one-off into something repeatable and shareable.

## How skills land here

- **Manually:** author with the `skill-creator` skill.
- **Via triage:** the `clippings-triage` skill can detect a clipping that captures a
  reusable pattern and **propose** distilling it into a skill here (propose-only — it
  scaffolds only after you confirm).

## Layout

```
Skills/
└── <skill-name>/
    └── SKILL.md   # frontmatter: name, description (trigger phrases)
```

> Live global skills are symlinked at `../Harness/global → ~/.claude/skills`. This folder
> is for the curated, vault-owned meta-skills I choose to keep and share.
