# Outbound Skills for AI Agents

Skills that teach your AI agent to do B2B outbound the way it actually works: find the right people, give them a real reason to talk, and write like a person. LinkedIn first, with email and WhatsApp joining.

Every rate in these skills comes from campaigns we ran, not from vendor surveys. Each skill shows its numbers, with sample sizes, in `references/benchmarks.md`.

Works with Claude Code, OpenAI Codex, Cursor, and any agent that supports the [Agent Skills spec](https://agentskills.io).

Built by [Kairon](https://heykairon.com). The skills work with any tool, or by hand. Connect the [Kairon MCP](https://heykairon.com/mcp) and your agent can run them for you.

## Install

**Any agent** (Claude Code, Codex, Cursor, and more):

```bash
npx skills add heykairon/outbound-skills
```

One skill only:

```bash
npx skills add heykairon/outbound-skills --skill connection-requests
```

**Claude Code plugin:**

```
/plugin marketplace add heykairon/outbound-skills
/plugin install outbound-skills@outbound-skills
```

**By hand:** copy `skills/<name>/` into `.agents/skills/` (or `.claude/skills/`) in your project.

## Start here

After you install, run `/outbound-context` (or ask your agent to "use the outbound-context skill"). It writes one file with your value proposition and how you write, and starts your ICPs. Every other skill reads it, so none of them asks you the same thing twice. If you skip it, the first skill that needs it will start it for you.

## How the skills fit together

```
                         outbound-context
        (value prop and voice; ICPs in icp — every skill reads it first)
                                 │
   ┌──────────────┬──────────────┼───────────────┬────────────────┐
   ▼              ▼              ▼               ▼                ▼
Strategy        Leads        Profile &        Outreach          Measure
                              content
initiatives    lead-search   linkedin-       connection-       funnel-
icp            signal-leads   profile         requests          diagnosis
offer-and-     warm-network  linkedin-posts  linkedin-messages
 lead-magnet                 linkedin-       follow-ups
                              comments
```

## Skills

| Skill | Status | What it does |
|-------|--------|--------------|
| [connection-requests](skills/connection-requests/) | ✅ | The note, weekly volume, reading the acceptance rate |
| [outbound-context](skills/outbound-context/) | ✅ | Writes the file with your value proposition and voice that every skill reads |
| [initiatives](skills/initiatives/) | ✅ | What you are testing: an ICP plus an offer, an end date, what you expect, and what already failed |
| [icp](skills/icp/) | ✅ | Find your ICP in your best customers and test the market it sits in |
| offer-and-lead-magnet | soon | An offer strangers say yes to |
| [lead-search](skills/lead-search/) | ✅ | Sales Navigator filters and lists worth sending to |
| signal-leads | soon | Leads with a dated reason to write: posts, hires, competitors |
| warm-network | soon | Your 1st-degree network, your tribes, warm intros |
| linkedin-profile | soon | Photo, banner, headline, about |
| [linkedin-posts](skills/linkedin-posts/) | ✅ | Pillars, hooks, posts nobody mistakes for AI |
| linkedin-comments | soon | Comments that sound like you and warm up the invite |
| linkedin-messages | soon | The first message, in five parts |
| follow-ups | soon | How many, and how to write them |
| funnel-diagnosis | soon | Find which stage broke: volume first, then rates |

## Contributing

Found a better way, or have data that disagrees with ours? Open an issue or a PR. See [AGENTS.md](AGENTS.md) for the skill format.

## License

MIT
