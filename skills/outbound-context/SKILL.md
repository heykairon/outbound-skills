---
name: outbound-context
description: Set up the outbound context, the .agents folder every other outbound skill reads first, and write its two sender files. .agents/identity.md says who sends (identity, background, close circles, network). .agents/voice.md says how they write, from real messages. The ICPs and the value proposition sit next to them, each in its own file. Use when the user says "set up my outbound," "onboard me," "outbound context," "here's my company," "who I am," "how I write," or starts any outbound task with no context yet. Draft from what you already know, ask only what you cannot look up, one question at a time, and never invent a fact. Who the user sells to belongs in icp, and what they promise belongs in value-prop. What the user is testing (an offer, a region, a new buyer, a goal with a date) belongs in initiatives.
metadata:
  version: 0.7.0
  section: business-context
---

# Outbound Context

The outbound context is the `.agents/` folder: one file per thing, and every other outbound skill reads it before it does anything. With it, no skill asks the user the same question twice. Without it, every message sounds like nobody.

This skill owns two of its files. **Who sends** lives in `.agents/identity.md`. **How they write** lives in `.agents/voice.md`. **Who the user sells to** lives in `.agents/icp.md`, defined by **[icp](../icp/SKILL.md)**. **What they promise** lives in `.agents/value-prop.md`, defined by **[value-prop](../value-prop/SKILL.md)**. For a new user, set up these in order: the identity, the ICP, the value proposition and the voice. Use each skill for its own part. What the user is **testing** right now (an offer, a region, a different buyer, a goal with a date) changes every few weeks and lives in `.agents/initiatives.md`. See **[initiatives](../initiatives/SKILL.md)**.

## Before Starting

Look for existing files first: `.agents/identity.md` and `.agents/voice.md` (or the same names under `.claude/`). If they exist, read them, and only update what changed. Re-doing settled work is its own failure.

## Draft First, Ask Second

Draft every section you can from what you hold (website, deck, case studies, past messages), then show it. If you hold nothing, ask for material: the website, a deck, a few customer names.

**Never invent a fact about the company.** Not a buyer, a result, a signal or a differentiator, not even marked as an assumption. An invented value proposition reads plausible, is wrong, and then feeds every message every other skill writes. Leave the gap open instead.

Where sources contradict each other (the site says small companies, the featured case is a 3,000-person chain), show the gap and let the user decide.

Ask only what you cannot look up, and ask for one thing per turn, never two joined by "and". A question inside the draft counts too: mark that gap as open instead.

---

## The Files

Keep them working material, not website copy: written to be *used* by whatever drafts next.

```markdown
# Identity

_Last updated: YYYY-MM-DD_

- **Who:** [name, role, company]
- **Identity:** [who they are beyond the job title: nationality, being a founder, anything that helps them relate to the buyer]
- **Background:** [past employers, schools, countries: the tribes they belong to]
- **Close circles:** [the groups where they have many friends, not just contacts: a university, a former team, a community. Warm introductions start here]
- **Network:** [about how many connections, and where most of them are]
```

```markdown
# Voice

_Last updated: YYYY-MM-DD_

- **Language and formality:** [e.g. Spanish, informal, first names, lowercase ok]
- **How they open, how long they write:**
- **Real examples:** [5–10 messages the sender actually wrote]
- **What worked:** [the difference between their messages that got a conversation and the ones that didn't]
- **Never say:** [words or claims they hate]
```

Real ones, filled in: [Luciano's identity](references/example-identity.md) and [Luciano's voice](references/example-voice.md).

### The voice needs real evidence

Read messages the sender actually wrote: their LinkedIn inbox, sent emails. Count only what **they** wrote. Leave out:
- **Acknowledgements:** a message that only says it got yours ("ok", "thanks", "genial", "dale"). A short message with its own content still counts: "no rush, I'll write again in March after you close the books" shows how they write.
- **Templates:** any text that repeats almost word for word across conversations.

**Enough means at least 10 of their own messages, across at least 5 conversations.** With less, don't write the voice. Two or three messages copy their tics, not how they write. Leave it as "not enough samples yet" and let the writing skills ask.

**Then learn from what worked.** Compare the messages that kept the conversation going with the ones that didn't, and write the difference as a rule under "What worked". If you only have the sender's side, say the rule is inferred from how each thread continued.

---

## Save, Then Read It Back

Show the full draft. Let the user correct it. Only after a clear yes, write the files. Then read back what you wrote and say it in one or two lines: how the sender writes.

If the user skips a section, leave it marked as open in the file and say in one sentence what it costs. For example: "No voice samples yet. Every message will sound generic until we have ten of yours."

---

## Keeping It Fresh

Update the files when:
- the sender changes, or writes in a new way.

Change only the section that moved, and update the date. A new offer, region or buyer to try is not an update here: it is a new initiative.

---

## Related Skills

- **[icp](../icp/SKILL.md)**: who the user sells to, in `.agents/icp.md`.
- **[value-prop](../value-prop/SKILL.md)**: what the user promises, in `.agents/value-prop.md`.
- **[initiatives](../initiatives/SKILL.md)**: what the user is testing, until when, and what they expect from it.
- **[lead-search](../lead-search/SKILL.md)**, **[linkedin-posts](../linkedin-posts/SKILL.md)**: they all read this file first.
