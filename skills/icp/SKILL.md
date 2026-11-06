---
name: icp
description: Define, test and update the ideal customer profiles in .agents/icp.md, the one file every outbound skill reads to know who to go after. Built on Alex Hormozi's $100M Offers (pick a starving crowd, then commit to a niche) and his first-avatar method (find what the best customers have in common). Use when the user says "define my ICP," "who should I sell to," "ideal customer," "target market," "which niche," "is this a good market," "our best customers," "update my ICP," "this segment doesn't work," or "drop this ICP." Start from the best customers, not from a wish. Test the market for pain, money, ease of finding and growth, narrow until someone is left out, never invent a customer or a fact, and let the user set each ICP's status. For testing an ICP with outreach, see initiatives.
metadata:
  version: 0.1.0
---

# ICP

Who you sell to decides more than what you say. Hormozi ranks it first, in *$100M Offers*: the market, then the offer, then how well you sell. A great market forgives a weak offer. A bad one sinks a great offer, however well it is sold.

This skill owns `.agents/icp.md`: what an ICP is made of, and the rules for each one. Other skills read the file. They never define an ICP themselves.

## Before Starting

Read `.agents/icp.md` if it exists, and update only what changed. Read `.agents/outbound-context.md` for the value proposition. If neither exists and the user is starting from zero, use **[outbound-context](../outbound-context/SKILL.md)** first.

Draft from what you hold, then ask, one thing per turn. **Never invent a customer, a number or a buyer.** An invented ICP reads plausible and sends every later list after the wrong people. Leave the gap open instead.

---

## 1. Start From the Best Customers

The ICP is already inside the customer list. Ask for it, or read the CRM export the user has.

**Pick the best ones, by three measures:** they paid the most, they stayed the longest, and the user liked working with them (fast result, little effort). Keep the top fifth, or the best 2 to 5 when there are few. Ignore the rest for this job.

For each best customer, find out:
- **The company:** industry, size, where it sells, and the state it was in when it bought (for example: a signed lease, at least one employee, already selling online).
- **The person who bought:** their role, and what they are measured on.
- **Why they bought:** what happened just before (the trigger), the main reason, and where they first heard of the user. The trigger is an event with a date, never the pain itself: they switched systems, opened a branch, hired, got referred, saw a post. "Slow collections" is the pain. "They moved to a new ERP in March" is the trigger.

**Then find the fewest criteria they all share.** Usually 3 to 5. A long list of traits describes customers. A short one filters strangers.

The trigger becomes the signal **[lead-search](../lead-search/SKILL.md)** looks for. Where they first heard of the user becomes the source **[initiatives](../initiatives/SKILL.md)** works.

**No customers yet?** Start from the offer and 2 to 5 companies the user wants as customers. Say plainly that this ICP is a guess.

---

## 2. Test the Market

Four tests, from *$100M Offers*. Write one line per test, with the evidence behind it.

- **Pain.** They need it, they don't just want it. If you describe their problem in one sentence, they would say "that's me".
- **Money.** They can pay the price, and the person you talk to can decide or get the budget. Unemployed people have the pain of a bad resume and no money for a coach.
- **Easy to find.** You can build a list of them: a search filter, an association, a group, an event. Run the search and write the real count. Never guess it.
- **Growing.** There will be more of them next year. A shrinking market defeats everything else, even when it passes the other three tests.

If one test clearly fails, narrow the ICP or move to another market before you go on.

---

## 3. Narrow Until Someone Is Left Out

A narrow ICP lets every message speak to exactly one kind of person, and the same product is worth far more to them. Write **disqualifiers**: who is a clear no, even when the user could help them.

If the ICP leaves nobody out, it is not an ICP yet. As a rule of thumb from the book, a business under about USD 10 million a year almost always does better narrower. Widen later, from proof.

---

## 4. Commit, Then Judge

Pick one ICP and stay with it. Switching between two good markets restarts the learning each time, and makes both look bad.

Judge it only on volume. As a rule of thumb, under about 50 conversations a quiet market proves nothing. Testing an ICP with outreach is an initiative, with an end date and what it should bring: see **[initiatives](../initiatives/SKILL.md)**.

---

## The File

```markdown
# ICPs

_Last updated: YYYY-MM-DD_

## [Short name, e.g. "Wholesale distributors, Argentina"]
- **Status:** [validating | validated | discarded], since YYYY-MM-DD, because [the user's reason]
- **Companies:** [the 3 to 5 shared criteria: industry, size, where, the state they are in]
- **People:** [roles that feel the pain and can decide]
- **Disqualifiers:** [who is a clear no]
- **Best customers:** [real names, and what made each one the best]
- **Why they buy:** [the trigger, the main reason, where they first heard of us]
- **Market:** [pain, money, easy to find (with the real count), growing: one line each]
```

One block per ICP. Most companies have one or two.

### The user sets the status

**Validating**, **validated** or **discarded**. What counts as validated is the user's call, not yours: write the status and the reason they give. If they have not said, leave the status open. Don't infer it from the customers.

A discarded ICP stays in the file with its reason, so nobody tries it again without reading why. Other skills skip it.

### Save, then read it back

Show the full draft. Save only after a clear yes. Then say in one or two lines who the user sells to, and who is a clear no.

---

## Related Skills

- **[outbound-context](../outbound-context/SKILL.md)**: the value proposition and the voice, and the first step for a new user.
- **[initiatives](../initiatives/SKILL.md)**: test an ICP with outreach, and change its status when the test ends.
- **[lead-search](../lead-search/SKILL.md)**: turn the ICP and its trigger into a list.
