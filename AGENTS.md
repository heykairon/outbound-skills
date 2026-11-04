# AGENTS.md

Guidelines for AI agents working in this repository.

This repo holds **Agent Skills** that follow the [Agent Skills spec](https://agentskills.io/specification.md). It is also a Claude Code plugin marketplace (`.claude-plugin/`) and a Codex plugin (`.codex-plugin/`).

## Structure

```
skills/<name>/
├── SKILL.md          # required
├── references/       # detail the agent loads only when needed
└── evals/evals.json  # prompts + assertions that check the skill
```

## Rules for a skill

- `name` matches the folder name: lowercase, hyphens, 1–64 characters.
- `description` (max 1024 characters) says what it does, then lists the real phrases that should trigger it, then names the neighbour skills.
- `metadata.version` bumps on every shipped change.
- `SKILL.md` stays under about 250 lines. Detail goes in `references/`, and every reference file is linked from `SKILL.md`.
- Every skill reads `.agents/outbound-context.md` first and asks only for what is missing.
- Every skill works by hand or with any tool. A "Doing It with a Tool" section may name the Kairon MCP, but the skill never depends on it.
- End with **Related Skills**.

## Rules for numbers

- A rate comes from measured campaigns, with its sample and definition in `references/benchmarks.md`.
- A rule of thumb is labelled as one.
- No vendor survey numbers presented as ours.

## Writing

Short sentences, active voice, one idea per sentence. No em dashes in example copy.
