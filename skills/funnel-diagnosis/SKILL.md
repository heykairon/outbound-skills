---
name: funnel-diagnosis
description: Find which stage of an outbound funnel broke (volume, acceptance, replies, interest or meetings), say why from the evidence, and propose one fix. Use when the user says "why isn't this working," "nobody accepts," "nobody answers," "they reply but nobody is interested," "we get interest but no meetings," "what's wrong with my campaign," "diagnose my funnel," "where are we losing people," "my numbers dropped," or "should I change the message or the list." Judge volume before any rate, compare each stage against the user's own numbers and then against measured benchmarks, stop at the first stage that broke because every stage below inherits it, read the replies before blaming the message, check that the interest labels are right, and end with one fix, the number it should move and when to measure again. For tracking an initiative and its weekly review, see initiatives.
metadata:
  version: 0.2.0
  section: strategy
---

# Funnel Diagnosis

An outbound funnel breaks at one stage, and every stage below inherits the break. A campaign that nobody accepts gets no replies, and rewriting the message will not fix it. Most teams change the message first because it is the easiest thing to change. Your goal is to find the first stage that broke, say why with evidence, and propose the one change that should fix it.

## Before Starting

**Requires [initiatives](../initiatives/SKILL.md).** Read that skill's Before Starting first, and read the files it names. If the file that skill owns does not exist yet, do that skill first. This skill does not repeat any of it.

Every diagnosis is of one campaign, or one initiative's campaigns. Get, per campaign and per segment if the list was split:

- **Invitations sent** at least 7 days ago, and how many were **accepted**.
- **People messaged**, how many **replied**, how many replied **with interest**, and how many **meetings** came of it.
- **The replies themselves.** At least the last 20, with the message they answered.

Read them from a tool if one has them. Never diagnose before you have the numbers.

---

## 1. Volume First

A rate on a small sample is noise. Before any rate means something, the stage needs about **20 invitations, 10 messages or 5 replies**. Below that, say "not enough to judge" for that stage, and stop there.

Then check whether volume itself is the problem. One LinkedIn seat sends about 150 invitations a week. A campaign that sent 40 in a month has a volume problem, whatever its rates say, and the fix is to send, not to rewrite.

---

## 2. Find the First Stage That Broke

Go down the funnel in order, and compare each stage first against the user's own past campaigns, then against the median of measured campaigns in **[benchmarks](../initiatives/references/benchmarks.md)**:

| Stage | Rate | Median organization |
|-------|------|---------------------|
| Acceptance | accepted ÷ invitations | 33% |
| Reply | replied ÷ accepted | 26% |
| Interest | interested ÷ replied | 26% |
| Meeting | meetings ÷ interested | not measured, about half assumed |

For people who were already connected, skip acceptance and count replies over people messaged.

**Stop at the first stage clearly below both.** A stage below the median by a few points, on a small sample, is not broken. Say so, and look at the next one.

---

## 3. What Breaks Each Stage

Each stage has its own causes. Name the one the evidence points to, and say what the evidence is.

**Acceptance.** Almost always the list, not the note.
- In measured campaigns, acceptance rose with mutual connections (+15 points with 1–2, +26 with 3–10), with people who posted in the last 30 days (+12) and with people who started their role in the last 3 months (+10). It fell for C-level and founders against individual contributors (−10).
- A note that pitches or asks for a meeting cut acceptance by about 6 points against no note.
- A lookalike list whose first hundred invitations accept under 30% rarely produces interest (a rule of thumb from our lists). Fix the search before filling more.

**Reply and interest.** Usually the offer, then how it is asked. See **[message-copies](../message-copies/SKILL.md)** for the fixes.
- A product pitch drew about 6% interest from people messaged. A partnership, a request for help or an event with a date drew more.
- A link or form in the first message, a closing question about the reader's problem, and "if it's not a good time, no problem" each went with less interest.
- A follow-up that asks for a no brings refusals, not interest.

**Interest to meeting.** Two causes:
- **A soft yes.** An invitation to an event or a free resource draws "send me the link". That is interest in the thing offered, not in a meeting. Count it apart.
- **No urgency.** "Let's talk in December" and "not right now" from people who liked the offer. The list and the message work. What is missing is a reason to meet now: a date, a limited group, a deadline that is true.

---

## 4. Read the Replies Before You Blame the Message

The replies say where the problem is. Sort the no's and the objections:

| What they say | Where the problem is |
|---------------|----------------------|
| "I'm not the right person", "that's another area" | the list: the wrong role or company |
| "Not relevant to us", "we don't do that" | the list: the wrong kind of company |
| "We already have a provider", "we do it in-house" | the offer, against what they already have |
| "I don't get what you sell", "how is this different from the others?" | the framing: the value proposition does not come across (see **[value-prop](../value-prop/SKILL.md)**) |
| "Not right now", "write me next quarter" | urgency |
| "Is this spam?", "how did you get my profile?" | the message |
| No reason | count it, and don't read much into it |

In a reading of 135 no's from our clients' campaigns, "not right now" was the most common, then "wrong person" and "not relevant" together, then "we already have a provider". Complaints about the message were rare ([benchmarks](../initiatives/references/benchmarks.md)).

**Check the labels.** Read ten replies marked interested and ten marked not interested. A label that judges where the person ended up can mark "yes, but I can only work remotely" as an objection, which is right, or miss a "send me the details", which is not. If the labels are wrong, fix the count before you diagnose.

---

## 5. One Fix

End with one change, the stage it fixes, the number it should move, and when to measure again:

- **One change at a time.** Two changes at once and the next measure can't say which one worked.
- **The number it should move,** from the stage's rate today to a target. "Acceptance from 21% to about 33%."
- **When to measure again:** when the stage has the volume of section 1 again, with the change in place.

If the first broken stage is volume, the fix is to send more, and the rates wait.

If no stage broke (every rate holds against the user's past and the median) and the totals are still too small, the fix is more volume or a higher price.

**Give the fix an owner, and record it.** When the campaign belongs to an initiative in `.agents/initiatives.md`, add the diagnosis there as a new review, under the last one, the way **[initiatives](../initiatives/SKILL.md)** writes reviews: the numbers, what they mean, whether the last move was done, and the next move with a named owner. Never rewrite an earlier review.

---

## The Diagnosis

```
| Stage | Your rate (n) | Your past | Median | Verdict |
|-------|---------------|-----------|--------|---------|
| Volume | 
| Acceptance |
| Reply |
| Interest |
| Meeting |

First stage that broke: [stage], because [evidence: numbers and replies].
The fix: [one change]. It should move [rate] from [x] to about [y]. Measure again after [volume or date].
```

A real one: [one of Kairon's initiatives](references/example.md).

---

## Related Skills

- **[initiatives](../initiatives/SKILL.md)**: the bet behind each campaign, and its weekly review.
- **[message-copies](../message-copies/SKILL.md)**: fixing the offer and the message when interest is the broken stage.
- **[lead-search](../lead-search/SKILL.md)**: fixing the list when acceptance or the no's point to it.
- **[sales-navigator](../sales-navigator/SKILL.md)**: fixing the search behind a list.
