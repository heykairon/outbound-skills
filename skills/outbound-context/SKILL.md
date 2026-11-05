---
name: outbound-context
description: Create or update the outbound context file (.agents/outbound-context.md) that every other outbound skill reads first. It holds who the user is, which stays true from one campaign to the next (the value proposition, the ICPs with the best customers behind them, and the sender's voice). Use when the user says "set up my outbound," "onboard me," "outbound context," "here's my company," "update my ICP," "new positioning," "our value proposition," "how I write," or starts any outbound task with no context file yet. Draft from what you already know, ask only what you cannot look up, one question at a time, and never invent a fact about the company. What the user is testing (an offer, a region, a new buyer, a goal with a date) belongs in initiatives, not here.
metadata:
  version: 0.3.2
---

# Outbound Context

You set up the one file every other outbound skill reads before it does anything: `.agents/outbound-context.md`. With it, no skill asks the user the same question twice. Without it, every message sounds like nobody.

The file holds **who the user is**: the value proposition, the ICPs and the voice. These stay true for months. What the user is **testing** right now (an offer, a region, a different buyer, a goal with a date) changes every few weeks and lives in `.agents/initiatives.md`. See **[initiatives](../initiatives/SKILL.md)**.

## Before Starting

Look for an existing file first: `.agents/outbound-context.md`, then `.claude/outbound-context.md`. If one exists, read it, and only update what changed. Re-doing settled work is its own failure.

## Draft First, Ask Second

Draft every section you can from what you hold (website, deck, case studies, past messages), then show it. If you hold nothing, ask for material: the website, a deck, a few customer names.

**Never invent a fact about the company.** Not a buyer, a result, a signal or a differentiator, not even marked as an assumption. An invented value proposition reads plausible, is wrong, and then feeds every message every other skill writes. Leave the gap open instead.

Where sources contradict each other (the site says small companies, the featured case is a 3,000-person chain), show the gap and let the user decide.

Ask only what you cannot look up, and ask for one thing per turn, never two joined by "and". A question inside the draft counts too: mark that gap as open instead. What usually has to be asked: which customers were the **best** ones and why, and where they sell if nothing says so.

---

## The File

Keep it working material, not website copy: written to be *used* by whatever drafts next.

```markdown
# Outbound Context

_Last updated: YYYY-MM-DD_

## Value proposition
- **Who we help:** [narrow enough that someone is excluded]
- **The problem, in their words:** [and what it costs them]
- **Before → after:** [what changes, with the proof we would cite]
- **Why us, not the next vendor:** [the mechanism, not adjectives]

## ICPs
One block per ICP. Most companies have one or two.

### [Short name, e.g. "Mid-size logistics, Mexico"]
- **Status:** [validating | validated | discarded], since YYYY-MM-DD, because [the user's reason]
- **Companies:** [industry, size, geography, business model]
- **People:** [roles that feel the pain and can act on it]
- **Disqualifiers:** [who is a clear no]
- **Best customers:** [2–5 real customers of this ICP and what made them great]

## Voice
- **Language and formality:** [e.g. Spanish, informal, first names, lowercase ok]
- **How they open, how long they write:**
- **Real examples:** [5–10 messages the sender actually wrote]
- **What worked:** [the difference between their messages that got a conversation and the ones that didn't]
- **Never say:** [words or claims they hate]
```

### Each ICP has a status, and the user sets it

**Validating**, **validated** or **discarded**. What counts as validated is the user's call, not yours: write the status and the reason they give. If they have not said, leave the status open. Don't infer it from the customers.

A discarded ICP stays in the file with its reason, so nobody tries it again without reading why. Other skills skip it.

### The voice section needs real evidence

Read messages the sender actually wrote: their LinkedIn inbox, sent emails. Count only what **they** wrote. Leave out:
- **Acknowledgements:** a message that only says it got yours ("ok", "thanks", "genial", "dale"). A short message with its own content still counts: "no rush, I'll write again in March after you close the books" shows how they write.
- **Templates:** any text that repeats almost word for word across conversations.

**Enough means at least 10 of their own messages, across at least 5 conversations.** With less, don't write a voice section. Two or three messages copy their tics, not how they write. Leave it as "not enough samples yet" and let the writing skills ask.

**Then learn from what worked.** Compare the messages that kept the conversation going with the ones that didn't, and write the difference as a rule under "What worked". If you only have the sender's side, say the rule is inferred from how each thread continued.

---

## Save, Then Read It Back

Show the full draft. Let the user correct it. Only after a clear yes, write the file. Then read back what you wrote and say it in two or three lines: who we help, why us, who we go after.

If the user skips a section, leave it marked as open in the file and say in one sentence what it costs. For example: "No voice samples yet. Every message will sound generic until we have ten of yours."

---

## Keeping It Fresh

Update the file when:
- the positioning changes;
- the user changes an ICP's status (often when an initiative ends);
- the sender changes, or writes in a new way.

Change only the section that moved, and update the date. A new offer, region or buyer to try is not an update here: it is a new initiative.

---

## Related Skills

- **[initiatives](../initiatives/SKILL.md)**: what the user is testing, until when, and what they expect from it.
- **[lead-search](../lead-search/SKILL.md)**, **[connection-requests](../connection-requests/SKILL.md)**, **[linkedin-posts](../linkedin-posts/SKILL.md)**: they all read this file first.
