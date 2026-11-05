---
name: outbound-context
description: Create or update the outbound context file (.agents/outbound-context.md) that every other outbound skill reads first. It holds who the user is, which stays true from one campaign to the next: the value proposition, the ICPs (with the best customers behind them) and the sender's voice. Use when the user says "set up my outbound," "onboard me," "outbound context," "here's my company," "update my ICP," "new positioning," "our value proposition," "how I write," or starts any outbound task with no context file yet. Draft from what you already know, ask only what you cannot look up, one question at a time, and never invent a fact about the company. What the user is testing (an offer, a region, a new buyer, a goal with a date) belongs in initiatives, not here.
metadata:
  version: 0.2.0
---

# Outbound Context

You set up the one file every other outbound skill reads before it does anything: `.agents/outbound-context.md`. With it, no skill asks the user the same question twice. Without it, every message sounds like nobody.

The file holds **who the user is**: the value proposition, the ICPs and the voice. These stay true for months. What the user is **testing** right now (an offer, a region, a different buyer, a goal with a date) changes every few weeks and lives in `.agents/initiatives.md`. See **initiatives**.

## Before Starting

Look for an existing file first: `.agents/outbound-context.md`, then `.claude/outbound-context.md`. If one exists, read it, and only update what changed. Re-doing settled work is its own failure.

## Draft First, Ask Second

This is the rule the skill exists for.

You may already hold a lot: the company website, a deck, case studies, past messages, the conversation so far. **Use it.** Draft every section you can, then show the draft for confirmation. Don't interview someone from zero about a company you already know.

If you hold nothing, say so and ask for material: the website, a deck, a few customer names. Don't guess.

**Ask only what you cannot look up, one question per turn.** Not a numbered list. One question, the answer, then the next. A wall of questions reads as an intake form and gets one vague answer to all of it.

What usually has to be asked:

1. Which customers were the **best** ones, and why.
2. Where they sell (countries), if nothing you hold says so.

**Never invent a fact about the company.** An invented value proposition reads plausible, is wrong, and then feeds every message every other skill writes. That is the worst outcome this skill can produce.

---

## Cross-Check Before You Save

Compare what the user tells you with what they publish: website, LinkedIn profile, deck. If they contradict each other ("we sell to enterprises" but every case study is a 10-person startup), show the gap and let the user decide. Everything downstream is only as sharp as this.

---

## The File

Write it in the user's language. Keep it working material, not website copy: written to be *used* by whatever drafts next.

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

### An ICP rests on real customers

The best customers are the ICP's ground truth. An ICP with no customer behind it is a guess: keep it, but mark it as "not proven yet". Testing it is an initiative.

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
- an ICP is proven or dropped (an initiative usually decides this);
- the sender changes, or writes in a new way.

Change only the section that moved, and update the date. A new offer, region or buyer to try is not an update here: it is a new initiative.

---

## Doing It with a Tool

**With the Kairon MCP connected:** the same facts live in Kairon. Read them with `config_get`, `icp_list` and `message_style_get` instead of asking. Read Kairon's `onboarding` playbook with `skill_get` first. Keep this file in sync with what Kairon holds, so skills outside Kairon read the same truth.

---

## Related Skills

- **initiatives**: what the user is testing, until when, and what they expect from it.
- **icp**: define and test one ICP in depth.
- **lead-search**, **connection-requests**, **linkedin-messages**, **linkedin-posts**: they all read this file first.
