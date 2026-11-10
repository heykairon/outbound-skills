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
npx skills add heykairon/outbound-skills --skill lead-search
```

**Claude Code plugin:**

```
/plugin marketplace add heykairon/outbound-skills
/plugin install outbound-skills@outbound-skills
```

**By hand:** copy `skills/<name>/` into `.agents/skills/` (or `.claude/skills/`) in your project.

## Start here

After you install, run `/outbound-context` (or ask your agent to "use the outbound-context skill"). It sets up your outbound context: a `.agents/` folder with one file per thing.

```
.agents/
├── identity.md     who sends: identity, background, close circles, network
├── voice.md        how you write, from your real messages
├── icp.md          who you sell to
└── value-prop.md   what you promise
```

Every other skill reads them, so none of them asks you the same thing twice. If you skip it, the first skill that needs it will start it for you.

## How the skills fit together

```
                         outbound-context
     (identity and voice, next to icp and value-prop — read first)
                                 │
   ┌───────────────┬─────────────┴───────────────┬───────────────┐
   ▼               ▼                             ▼               ▼
Strategy         Leads                       Profile &        Outreach
                                              content
initiatives      lead-search                 linkedin-        message-
icp              small-market                 profile          copies
lead-magnet      large-market                content-         funnel-
value-prop       sales-navigator              strategy         diagnosis
                                             linkedin-posts
```

## Skills

| Skill | Status | What it does |
|-------|--------|--------------|
| [outbound-context](skills/outbound-context/) | ✅ | Your voice, and the start of every setup: every skill reads it |
| [value-prop](skills/value-prop/) | ✅ | Your value proposition, built on the value equation: before and after, proof, time, effort, problems and solutions |
| [initiatives](skills/initiatives/) | ✅ | What you are testing: an ICP plus an offer, an end date, what you expect, and what already failed |
| [icp](skills/icp/) | ✅ | Find your ICP in your best customers and test the market it sits in |
| [lead-magnet](skills/lead-magnet/) | ✅ | Something free, made for each person, that leads to what you sell |
| [lead-search](skills/lead-search/) | ✅ | Measure your market, then build lists worth sending to |
| [small-market](skills/small-market/) | ✅ | A market of a few hundred companies, worked account by account |
| [large-market](skills/large-market/) | ✅ | A large market: closest source first, probe small, then fill |
| [sales-navigator](skills/sales-navigator/) | ✅ | Turn your ICP into searches that find only those people |
| [linkedin-profile](skills/linkedin-profile/) | ✅ | Photo, banner, headline and about, aimed at one market |
| [content-strategy](skills/content-strategy/) | ✅ | One subject, four pillars, once a week, and leads per post |
| [linkedin-posts](skills/linkedin-posts/) | ✅ | Hooks, real material, and posts nobody mistakes for AI |
| [message-copies](skills/message-copies/) | ✅ | The offer first, then the connection note, the first message and the follow-ups |
| [funnel-diagnosis](skills/funnel-diagnosis/) | ✅ | Find which stage broke: volume first, then rates |

## Contributing

Found a better way, or have data that disagrees with ours? Open an issue or a PR. See [AGENTS.md](AGENTS.md) for the skill format.

## License

MIT
