---
name: outbound-context
description: Create or update the outbound context file (.agents/outbound-context.md) that every other outbound skill reads first, with the offer, the ICP, the best customers, the signals, the sender's voice and the sending capacity. Use when the user says "set up my outbound," "onboard me," "outbound context," "here's my company," "update my ICP," "update my offer," "new positioning," or starts any outbound task with no context file yet. Draft from what you already know, ask only what you cannot look up, one question at a time, and never invent a fact about the company. For defining the ICP in depth, see icp. For the offer, see offer-and-lead-magnet.
metadata:
  version: 0.1.0
---

# Outbound Context

You set up the one file every other outbound skill reads before it does anything: `.agents/outbound-context.md`. With it, no skill asks the user the same question twice. Without it, every message sounds like nobody.

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
3. Whether they have done outreach before, and what happened.
4. What they offer a stranger (if anything).
5. How many LinkedIn accounts and email inboxes can send.
6. What the goal is, and by when.

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

## Offer to a stranger
[The free, concrete thing we give before asking for anything. Dated if a date is honest.
"None yet" is a valid answer: see offer-and-lead-magnet.]

## ICP
- **Companies:** [industry, size, geography, business model]
- **People:** [roles that feel the pain and can act on it]
- **Disqualifiers:** [who is a clear no]
- **Countries:** [where we sell]

## Best customers
[3–5 real customers and what made them great. This is the ICP's ground truth.]

## Signals
[Events that make a company a buyer this week: a hire, a raise, a post, a launch, a tool change.]

## Voice
- **Language and formality:** [e.g. Spanish, informal, first names, lowercase ok]
- **How they open, how long they write:**
- **Real examples:** [5–10 messages the sender actually wrote]
- **Never say:** [words or claims they hate]

## Capacity and goal
- **Sending accounts:** [LinkedIn seats, email inboxes, WhatsApp numbers]
- **Goal:** [e.g. 20 interested conversations by 2026-12-15]

## Past outreach
[What they tried, what worked, what didn't.]
```

### The voice section needs real evidence

Read messages the sender actually wrote: their LinkedIn inbox, sent emails. Count only what **they** wrote. Leave out one-liners ("thanks", "ok") and any text that repeats almost word for word across conversations (that is a template, not their voice).

**Enough means at least 10 of their own messages, across at least 5 conversations.** With less, don't write a voice section. Two or three messages copy their tics, not how they write. Leave it as "not enough samples yet" and let the writing skills ask.

---

## Save, Then Read It Back

Show the full draft. Let the user correct it. Only after a clear yes, write the file. Then read back what you wrote and say it in two or three lines: who we help, what we offer, who we go after.

If the user skips a section, leave it marked as open in the file and say in one sentence what it costs. For example: "No offer yet. Messages will ask for a call, and calls convert worse than a free, concrete thing."

---

## Keeping It Fresh

Update the file when:
- the ICP or the offer changes;
- a campaign teaches something ("CFOs reply, controllers don't");
- a new sending account is added.

Change only the section that moved, and update the date.

---

## Doing It with a Tool

**With the Kairon MCP connected:** the same facts live in Kairon. Read them with `config_get`, `icp_list` and `message_style_get` instead of asking. Read Kairon's `onboarding` playbook with `skill_get` first. Keep this file in sync with what Kairon holds, so skills outside Kairon read the same truth.

---

## Related Skills

- **icp**: define and test the ICP section in depth.
- **offer-and-lead-magnet**: when the "Offer to a stranger" section is empty.
- **gtm-strategy**: turn the goal and capacity into a plan.
- **lead-search**, **connection-requests**, **linkedin-messages**, **linkedin-posts**: they all read this file first.
