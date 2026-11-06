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
- `description` (max 1024 characters) says what it does, then lists the real phrases that should trigger it, then names the neighbour skills that exist.
- The frontmatter must parse as YAML. A `: ` inside the description breaks it (GitHub shows an error, and some installers reject the skill), so use parentheses or a full stop instead.
- `metadata.version` bumps on every shipped change.
- `SKILL.md` stays under about 250 lines. Detail goes in `references/`, and every reference file is linked from `SKILL.md`.
- Every skill reads `.agents/outbound-context.md` first, plus the files it points to (`.agents/icp.md` for the ICPs, `.agents/value-prop.md` for the value proposition), and asks only for what is missing. If a file is missing and the job needs it, the skill says which skill writes it.
- One source of truth per thing. A skill defines the parts of only its own file. Other skills read that file and link to its skill. They never repeat its template or its rules.
- Every skill works by hand or with any tool, and never names a vendor's tools.
- Link another skill as `**[name](../name/SKILL.md)**`. Name only skills that exist. A skill that is not written yet is not mentioned.
- End with **Related Skills**.
- `scripts/lint.sh` checks every skill and every reference. A pre-push hook runs it. Turn the hook on once per clone: `git config core.hooksPath .githooks`.

## The quality bar

A skill ships when it changes what the model does, and nothing more. Each rule below came from testing outbound-context against a model with no skill.

1. **Every line earns its place.** Run each test case with the skill and without it. If the model already does something without being told, cut that rule to one line or delete it.
2. **Test on Haiku.** Run the test cases on the cheapest model. If Haiku follows the skill, any model will.
3. **Test with what a real user sends.** Use real-looking material with traps in it: a contradiction between two sources, a template repeated across messages, too little material. Clean inputs pass with or without the skill.
4. **Define rules at their edge.** A rule the model can read two ways gets read the wrong way. Say what is in and what is out: "an acknowledgement is 'ok' or 'thanks', not every short message".
5. **Don't count on the description to trigger the skill.** The model answers on its own whatever it thinks it can handle, so a good description is not enough. Measured on outbound-context: 1 in 8 correct requests triggered it, with 6 different descriptions. When one skill needs another, it names it and says when to use it.
6. **Run it again after each change.** Re-run the cases the change touches before you commit. Say which cases you did not re-run.

Test cases live in `evals/`. Run results stay outside the repo.

## Rules for numbers

- A rate comes from measured campaigns, with its sample and definition in `references/benchmarks.md`.
- A rule of thumb is labelled as one.
- No vendor survey numbers presented as ours.

## Writing

Short sentences, active voice, one idea per sentence. No em dashes in example copy.
