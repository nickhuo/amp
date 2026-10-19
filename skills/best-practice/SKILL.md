---
name: best-practice
description: Before doing a task in a field with an established craft, find out what the best people in that field do and why, then teach it to the user so their own judgment improves. Searches high-quality sources (practitioners, organizations, papers, talks), names the goal of the practice and the criteria for doing it well, and compares them with the task at hand. Use when the user asks for best practice, the essence of something, the optimal setting, industry standards, or "how the best do it" (最佳实践, 本质, 最优解, 设计规范, 业界怎么做); and use it proactively, without being asked, when about to choose a default, format, metric, or architecture in an established craft such as design, typography, experimentation, statistics, hiring, writing, security, or agent design.
---

# Best practice

A task done to the agent's average taste lands in the middle of the field. This skill finds where the top of the field is, and why it is there, before the work starts. It has two outputs: a better task, and a user who can now judge the next one without asking.

It answers different questions from a research report. A report answers "what is true about X". This skill answers "what is X for, how do the best do it, where do they disagree, and what does that mean for this task".

## When to run

**Passive.** The user asks for best practice, the essence, the optimum, the standard, or how the industry does it, or invokes `/best-practice`. Always run.

**Active.** Run without being asked when all three hold:

1. **The task is in a craft with an established body of practice**: people have written, taught, or published how to do it well. Typography, A/B testing, resume writing, SOP agents, and memory systems qualify. Renaming a variable does not.
2. **You are about to make a choice that shapes the result**: a default value, a format, a metric, a threshold, a structure, an architecture.
3. **Nothing has settled that choice yet**: not the user's instructions, not their standards (see step 1), not an earlier best-practice brief in this project.

Why these three: research costs minutes and tokens, and it pays only where the agent would otherwise fill a consequential gap with its own average taste. When the user has already decided, research only second-guesses them. For a mechanical task there is nothing to learn.

**Scale depth to how hard the choice is to undo.**

- **Easy to undo**, like a spacing value or a label: do a quick pass of 2–3 sources, act on it, and give the user the brief in 3–5 lines.
- **Hard to undo**, like an architecture, a statistical method, or a product's positioning: do a full pass first, then present the brief and wait for the user before building on it.

Why: a wrong default that is cheap to change only costs a revision. A wrong foundation costs everything built on top of it.

When you run it actively, say so in one line first: what you are checking and why it matters here. This is so the user can stop you if they already know the answer.

## 1. Pick sources

Read `<std>/sources.md` first, where `<std>` is the directory the global `CLAUDE.md` / `AGENTS.md` names in a line like `Standards live at <path>`. If there is no such line or no `sources.md`, offer to create it with empty `## Trusted` and `## Proposed` sections, and treat every domain as one with no trusted sources.

- **The domain has trusted sources there** → start with them. The user chose them, and their trust is the in-house knowledge this skill can't download.
- **The domain has none** → find candidates yourself. A source qualifies when it is:
  - a practitioner writing from their own work (blog, talk, book, YouTube), with a track record you can point to;
  - a paper with citations or replication, or a standards body or official documentation;
  - cited by sources that already qualify.

  Skip SEO listicles, vendor content posing as neutral advice, and unattributed AI-written summaries. They repeat the average, and the average is what this skill exists to beat.

Add each new candidate to the `## Proposed` section of `<std>/sources.md`: name, domain, link, why it qualifies, and the task you found it during. **Never edit `## Trusted`.** Promoting a source is the user's call, because trusting a source is itself a judgment. You can widen what they see, but not what they trust.

## 2. Research

Use the `deep-research` skill for breadth when it is available; otherwise search and fetch directly. Read primary sources, not summaries of them. Find:

1. **The goal of the practice.** What it optimizes, and for whom. Example: resume layout optimizes for a recruiter's 10-second skim and for ATS parsing, not for looking designed.
2. **The criteria for doing it well**, each from a named source.
3. **Where the best disagree.** Disagreement among good sources marks a choice that depends on goals. It is the most useful thing to hand the user, because it is exactly what they need to judge.
4. **Common mistakes** that look reasonable but that good sources warn against.

Label every claim as consensus (several independent good sources agree) or one source's view. Never present one expert's preference as the field's standard.

## 3. Teach, then apply

Give the user a brief before or alongside the work, following `<std>/audience-calibration.md` if it exists:

```
Essence: <what the practice is for, one or two sentences>
Doing it best: <3–5 criteria, each with its why and source>
Common mistakes: <1–3>
Against this task: <where the current approach meets or misses the criteria>
Your call: <where good sources disagree, and what each side optimizes for>
```

Explain each criterion's why, not just the rule. Why: a rule handles this task, but the reason lets the user judge the next one without you, and raising their judgment is half the point.

Then apply what you found to the task. Where you follow a source over the user's earlier approach, say so.

## 4. Keep what recurs

If a best practice will apply again (the same craft keeps coming up), propose saving it as `<std>/<domain>.md` in the standards-file shape, with sources and a note that it is external practice. Write it only if the user approves.

If the user disagrees with a best practice, their view wins for this task. The disagreement is a correction, and `correction-to-rule` will pick it up; there is no need to record it here.
