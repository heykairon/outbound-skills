---
name: icp
description: Define, test and update the ideal customer profiles in .agents/icp.md, the one file every outbound skill reads to know who to go after. Built on Alex Hormozi's $100M Offers (pick a starving crowd, then commit to a niche) and his first-avatar method (find what the best customers have in common). Use when the user says "define my ICP," "who should I sell to," "ideal customer," "target market," "which niche," "is this a good market," "our best customers," "update my ICP," "this segment doesn't work," "where do I find them," or "drop this ICP." Start from the best customers, not from a wish. Test the market for pain, money, ease of finding and growth, narrow until someone is left out, list where to find them (its sources, closest first, from people who already know the user to a lookalike search), never invent a customer or a fact, and let the user set each ICP's status. For testing an ICP with outreach, see initiatives.
metadata:
  version: 0.4.0
---

# ICP

Who you sell to decides more than what you say. Hormozi ranks it first, in *$100M Offers*: the market, then the offer, then how well you sell. A great market forgives a weak offer. A bad one sinks a great offer, however well it is sold.

This skill owns `.agents/icp.md`: what an ICP is made of, and the rules for each one. Other skills read the file. They never define an ICP themselves.

## Before Starting

**Requires [outbound-context](../outbound-context/SKILL.md).** Read that skill's Before Starting first, and read the files it names. If the file that skill owns does not exist yet, do that skill first. This skill does not repeat any of it.

Read `.agents/icp.md` if it exists, and update only what changed.

Draft from what you hold, then ask, one thing per turn. **Never invent a customer, a number or a buyer.** An invented ICP reads plausible and sends every later list after the wrong people. Leave the gap open instead.

---

## 1. Start From the Best Customers

The ICP is already inside the customer list. Ask for it, or read the CRM export the user has.

**Pick the best ones, by three measures:** they paid the most, they stayed the longest, and the user liked working with them (fast result, little effort). Keep the top fifth, or the best 2 to 5 when there are few. Ignore the rest for this job.

For each best customer, find out:
- **The company:** industry, size, where it sells, and the state it was in when it bought (for example: a signed lease, at least one employee, already selling online).
- **The person who bought:** their role, and what they are measured on.
- **Why they bought:** the main reason, the goal behind it: what they want to reach, and why they need help to reach it. Then, apart, what happened just before (the trigger): an event with a date, never the pain itself. They switched systems, opened a branch, hired, raised a round. "Slow collections" is the pain. "They moved to a new ERP in March" is the trigger.

**Then find the fewest criteria they all share.** Usually 3 to 5. A long list of traits describes customers. A short one filters strangers.

**A place is a criterion only when the user truly cannot serve people elsewhere:** a licence, the language the product works in, where they can deliver. When the place is only about closeness (a shared language, a shared culture, the sender's country), it is not a criterion. It goes in the sources, as a tribe.

The trigger is not why they buy. It is a signal: it goes in the ICP's sources (see "Sources" below), and **[lead-search](../lead-search/SKILL.md)** looks for it.

**No customers yet?** Start from the offer and 2 to 5 companies the user wants as customers. Say plainly that this ICP is a guess.

---

## 2. Test the Market

Four tests, from *$100M Offers*. Run each one, with the evidence behind it, and tell the user what you found. They decide whether to go after this market. They are not a field in the file.

- **Pain.** They need it, they don't just want it. If you describe their problem in one sentence, they would say "that's me".
- **Money.** They can pay the price, and the person you talk to can decide or get the budget. Unemployed people have the pain of a bad resume and no money for a coach.
- **Easy to find.** You can build a list of them: a search filter, an association, a group, an event. Run the search and say the real count. Never guess it.
- **Growing.** There will be more of them next year. A shrinking market defeats everything else, even when it passes the other three tests.

If one test clearly fails, narrow the ICP or move to another market before you go on.

---

## 3. Narrow Until Someone Is Left Out

A narrow ICP lets every message speak to exactly one kind of person, and the same product is worth far more to them. Write **disqualifiers**: who is a clear no, even when the user could help them.

If the ICP leaves nobody out, it is not an ICP yet. As a rule of thumb from the book, a business under about USD 10 million a year almost always does better narrower. Widen later, from proof.

---

## 4. Sources, Closest First

A source is where the people on a list come from, and the reason the sender writes to them. The same ICP answers very differently depending on the source, so each ICP lists its own sources, closest first. There are six:

| # | Source | Who |
|---|--------|-----|
| 1 | **They already know you** | People the user already talked to, where it stopped halfway: ex-customers, conversations that went quiet, demos that went nowhere, contacts in their CRM. The easiest list, because the context is already there and unused. |
| 2 | **Network and tribes** | 1st-degree connections who fit the ICP, the sender's close circles, and people who share something with the sender: a university, a school, a past employer, a community, a country. Take them from the sender's identity. |
| 3 | **They come to you** | People who reacted to the sender's posts, visited the profile, sent an invitation, follow them or subscribe to their newsletter. |
| 4 | **Warm intros** | Someone the sender knows introduces them: a customer who refers, an investor, a friend. |
| 5 | **Signals** | Something happened, with a date, or there is a public trace: hiring the role, a funding round, a new job, a post about the problem, going to an event, following or reacting to a competitor, being on a public list (an exhibitor list, a directory, a registry). |
| 6 | **Lookalike** | A search for the ICP's roles at companies like the best customers. The coldest source: nobody there knows the sender. |

In the file, list the ones that apply to this ICP, in this order, with real names: which network, which tribe, which signal, which competitor. A source with no real name behind it is not one yet. Two ICPs usually have different sources: a recruiting buyer leaves different signals than a sales buyer.

Every list starts at source 1: first check whether there is a list the user can work today. Move to the next source only when the closer one runs dry. Never start with the lookalike.

---

## 5. Commit, Then Judge

Pick one ICP and stay with it. Switching between two good markets restarts the learning each time, and makes both look bad.

Judge it only on volume. As a rule of thumb, under about 50 conversations a quiet market proves nothing. Testing an ICP with outreach is an initiative, with an end date and what it should bring: see **[initiatives](../initiatives/SKILL.md)**.

---

## The File

```markdown
# ICPs

_Last updated: YYYY-MM-DD_

## [Short name, e.g. "Wholesale distributors, Argentina"]
- **Status:** [validating | validated | discarded], since YYYY-MM-DD, because [the user's reason]
- **Companies:** [the 3 to 5 shared criteria: industry, size, the state they are in, and a place only when it truly limits who you can serve]
- **People:** [roles that feel the pain and can decide]
- **Disqualifiers:** [who is a clear no]
- **Best customers:** [real names, and what made each one the best]
- **Why they buy:** [the main reason: the goal they want to reach, and why they need help to reach it]
- **Business approach:** [how the user sells to them, for example: start with a small account, show the value, then grow]
- **Sources** (closest first): [the ones that apply, each with real names]
```

One block per ICP. Most companies have one or two. A real one, filled in: [Kairon's ICPs](references/example.md).

### The user sets the status

**Validating**, **validated** or **discarded**. What counts as validated is the user's call, not yours: write the status and the reason they give. If they have not said, leave the status open. Don't infer it from the customers.

A discarded ICP stays in the file with its reason, so nobody tries it again without reading why. Other skills skip it.

### Save, then read it back

Show the full draft. Save only after a clear yes. Then say in one or two lines who the user sells to, and who is a clear no.

---

## Related Skills

- **[outbound-context](../outbound-context/SKILL.md)**: the voice, and the first step for a new user.
- **[value-prop](../value-prop/SKILL.md)**: what each ICP is promised.
- **[initiatives](../initiatives/SKILL.md)**: test an ICP with outreach, and change its status when the test ends.
- **[lead-search](../lead-search/SKILL.md)**: turn the ICP and its trigger into a list.
