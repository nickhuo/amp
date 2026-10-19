#!/usr/bin/env python3
"""Print (previous request -> agent reply -> user's next message) turns from Claude Code and Codex transcripts since a date.

Usage: uv run extract_pairs.py --since YYYY-MM-DD [--agent-chars 1200] [--max-chars 1200]
Prints every turn with an id, including each session's opening message. It does not decide which pairs are corrections; classify.md does.
Skips tool output, injected instructions, and wrapper tags.
"""
import argparse
import datetime as dt
import json
import re
from pathlib import Path

HOME = Path.home()
SOURCES = {
    "claude": HOME / ".claude/projects",
    "codex": HOME / ".codex/sessions",
}
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
INJECTED = (
    "<", "# AGENTS.md instructions", "Caveat:", "[Raft", "New message received:",
    "This session is being continued", "[Request interrupted",
)
REQUEST = "## My request:"

def clean(text):
    text = REMINDER.sub("", text).strip()
    # Codex wraps attachments and annotations around the actual request.
    if REQUEST in text:
        text = text.split(REQUEST, 1)[1].strip()
    return "" if not text or text.startswith(INJECTED) else text


def claude_turns(path):
    """Yield (timestamp, cwd, role, text); tool calls and results are dropped."""
    cwd = None
    for line in path.open(encoding="utf-8", errors="replace"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        cwd = d.get("cwd") or cwd
        role = d.get("type")
        if role not in ("user", "assistant") or d.get("isMeta") or d.get("isSidechain"):
            continue
        content = d.get("message", {}).get("content")
        if isinstance(content, list):
            content = "\n".join(b.get("text", "") for b in content if b.get("type") == "text")
        if not isinstance(content, str):
            continue
        text = clean(content) if role == "user" else content.strip()
        if text:
            yield d.get("timestamp", ""), cwd, role, text


def codex_turns(path):
    cwd = None
    for line in path.open(encoding="utf-8", errors="replace"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        p = d.get("payload") if isinstance(d.get("payload"), dict) else {}
        if d.get("type") == "session_meta":
            cwd = p.get("cwd")
        role = p.get("role")
        if d.get("type") != "response_item" or role not in ("user", "assistant"):
            continue
        kind = "input_text" if role == "user" else "output_text"
        content = "\n".join(c.get("text", "") for c in p.get("content") or [] if c.get("type") == kind)
        text = clean(content) if role == "user" else content.strip()
        if text:
            yield d.get("timestamp", ""), cwd, role, text


def pairs(turns):
    """Yield (ts, cwd, previous user message, agent text since it, next user message)."""
    agent, before = [], ""
    for ts, cwd, role, text in turns:
        if role == "assistant":
            agent.append(text)
            continue
        yield ts, cwd, before, "\n".join(agent), text
        agent, before = [], text


def clip(text, n):
    """Keep the start and end: what a reply opens with and what it ends asking are both context."""
    if len(text) <= n:
        return text
    return text[: n // 3] + " …[cut]… " + text[-(n - n // 3):]


def indent(text):
    return text.replace("\n", "\n  ")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since", required=True, type=dt.date.fromisoformat)
    parser.add_argument("--agent-chars", type=int, default=1200, help="keep the start and end of the agent reply, N chars total")
    parser.add_argument("--max-chars", type=int, default=1200)
    args = parser.parse_args()
    cutoff = dt.datetime.combine(args.since, dt.time()).timestamp()
    readers = {"claude": claude_turns, "codex": codex_turns}

    n = 0
    sessions = []
    for tool, root in SOURCES.items():
        if root.exists():
            sessions += [(f.stat().st_mtime, tool, f) for f in root.rglob("*.jsonl") if f.stat().st_mtime >= cutoff]
    for _, tool, path in sorted(sessions):
        found = [
            p for p in pairs(readers[tool](path))
            if p[0][:10] >= args.since.isoformat()
        ]
        if not found:
            continue
        # Session info rides on every item, so splitting on "### p" never leaves a header inside a turn.
        for ts, cwd, before, agent, user in found:
            n += 1
            # A session's opening message (or a second message sent before any reply) has no agent text.
            # Keep it: it is the user's own request, and classify.md reads an empty reply as "not a correction".
            before = before or "(none: session start)"
            agent = agent or "(none: no agent reply yet)"
            print(f"### p{n}\n<!-- {tool} {ts[:10]} {cwd} {path} -->\n- before: {indent(clip(before, 300))}\n  agent: {indent(clip(agent, args.agent_chars))}"
                  f"\n  user: {indent(clip(user, args.max_chars))}\n")


if __name__ == "__main__":
    main()
