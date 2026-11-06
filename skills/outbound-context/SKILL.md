---
name: outbound-context
description: Create or update the outbound context file (.agents/outbound-context.md) that every other outbound skill reads first. It holds the sender's voice, which stays true from one campaign to the next, and points to the ICPs and the value proposition, which live in their own files. Use when the user says "set up my outbound," "onboard me," "outbound context," "here's my company," "how I write," or starts any outbound task with no context file yet. Draft from what you already know, ask only what you cannot look up, one question at a time, and never invent a fact about the company. Who the user sells to belongs in icp, and what they promise belongs in value-prop. What the user is testing (an offer, a region, a new buyer, a goal with a date) belongs in initiatives.
metadata:
  version: 0.6.0
---

# Outbound Context

You set up the one file every other outbound skill reads before it does anything: `.agents/outbound-context.md`. With it, no skill asks the user the same question twice. Without it, every message sounds like nobody.

The file holds **the voice**, and points to the rest. **Who the user sells to** lives in `.agents/icp.md`, defined by **[icp](../icp/SKILL.md)**. **What they promise** lives in `.agents/value-prop.md`, defined by **[value-prop](../value-prop/SKILL.md)**. For a new user, set up all three in that order: the ICP, the value proposition, the voice. Use each skill for its own part. What the user is **testing** right now (an offer, a region, a different buyer, a goal with a date) changes every few weeks and lives in `.agents/initiatives.md`. See **[initiatives](../initiatives/SKILL.md)**.

## Before Starting

Look for an existing file first: `.agents/outbound-context.md`, then `.claude/outbound-context.md`. If one exists, read it, and only update what changed. Re-doing settled work is its own failure.

## Draft First, Ask Second

Draft every section you can from what you hold (website, deck, case studies, past messages), then show it. If you hold nothing, ask for material: the website, a deck, a few customer names.

**Never invent a fact about the company.** Not a buyer, a result, a signal or a differentiator, not even marked as an assumption. An invented value proposition reads plausible, is wrong, and then feeds every message every other skill writes. Leave the gap open instead.

Where sources contradict each other (the site says small companies, the featured case is a 3,000-person chain), show the gap and let the user decide.

Ask only what you cannot look up, and ask for one thing per turn, never two joined by "and". A question inside the draft counts too: mark that gap as open instead.

---

## The File

Keep it working material, not website copy: written to be *used* by whatever drafts next.

```markdown
# Outbound Context

_Last updated: YYYY-MM-DD_

## ICPs
See `.agents/icp.md`.

## Value proposition
See `.agents/value-prop.md`.

## Voice
- **Language and formality:** [e.g. Spanish, informal, first names, lowercase ok]
- **How they open, how long they write:**
- **Real examples:** [5–10 messages the sender actually wrote]
- **What worked:** [the difference between their messages that got a conversation and the ones that didn't]
- **Never say:** [words or claims they hate]
```

### The voice section needs real evidence

Read messages the sender actually wrote: their LinkedIn inbox, sent emails. Count only what **they** wrote. Leave out:
- **Acknowledgements:** a message that only says it got yours ("ok", "thanks", "genial", "dale"). A short message with its own content still counts: "no rush, I'll write again in March after you close the books" shows how they write.
- **Templates:** any text that repeats almost word for word across conversations.

**Enough means at least 10 of their own messages, across at least 5 conversations.** With less, don't write a voice section. Two or three messages copy their tics, not how they write. Leave it as "not enough samples yet" and let the writing skills ask.

**Then learn from what worked.** Compare the messages that kept the conversation going with the ones that didn't, and write the difference as a rule under "What worked". If you only have the sender's side, say the rule is inferred from how each thread continued.

---

## Save, Then Read It Back

Show the full draft. Let the user correct it. Only after a clear yes, write the file. Then read back what you wrote and say it in one or two lines: how the sender writes.

If the user skips a section, leave it marked as open in the file and say in one sentence what it costs. For example: "No voice samples yet. Every message will sound generic until we have ten of yours."

---

## Keeping It Fresh

Update the file when:
- the sender changes, or writes in a new way.

Change only the section that moved, and update the date. A new offer, region or buyer to try is not an update here: it is a new initiative.

---

## Related Skills

- **[icp](../icp/SKILL.md)**: who the user sells to, in `.agents/icp.md`.
- **[value-prop](../value-prop/SKILL.md)**: what the user promises, in `.agents/value-prop.md`.
- **[initiatives](../initiatives/SKILL.md)**: what the user is testing, until when, and what they expect from it.
- **[lead-search](../lead-search/SKILL.md)**, **[linkedin-posts](../linkedin-posts/SKILL.md)**: they all read this file first.
