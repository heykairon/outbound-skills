---
name: value-prop
description: Write and sharpen the value proposition in .agents/value-prop.md, the one file every outbound skill reads for what the user promises and why a buyer would believe it. Built on Alex Hormozi's value equation from $100M Offers (raise the dream outcome and the likelihood of getting it, cut the time and the effort it takes). Use when the user says "value proposition," "value prop," "what do we promise," "positioning," "why us," "our pitch," "before and after," "nobody gets what we do," "our message sounds generic," or "what problems do our customers have." Write one per ICP, in the customer's words. Work the before and after, list every problem with its solution, push on proof, time and effort rather than on a bigger promise, and never invent proof. For who it is for, see icp.
metadata:
  version: 0.2.0
---

# Value Proposition

Hormozi's value equation, from *$100M Offers*:

```
        Dream outcome × Perceived likelihood of getting it
Value = ──────────────────────────────────────────────────
             Time it takes × Effort and sacrifice
```

A value proposition says all four in the buyer's words, with proof. This skill owns `.agents/value-prop.md`: what a value proposition is made of, and its rules. Other skills read the file. They never define a value proposition themselves.

## Before Starting

**Requires [icp](../icp/SKILL.md).** Read that skill's Before Starting first, and read the files it names. If the file that skill owns does not exist yet, do that skill first. This skill does not repeat any of it.

A value proposition is written for one ICP: two ICPs get two. Read `.agents/value-prop.md` if it exists, and update only what changed.

Draft from what the user already has: the website, a deck, case studies, notes from sales calls, the customers' own replies. Then ask, one thing per turn. **Never invent proof.** Not a customer, a number or a result, not even as an example. An invented proof reads plausible and ends up in every message. Leave the gap open instead.

---

## 1. Before and After

- **Before:** the customer's situation today, in their own words, and what it costs them: money, hours, a person's salary, a risk. Take the words from calls, replies and reviews. Never from the website.
- **After:** the dream outcome. The destination, not the vehicle: "collect 18 days sooner", not "collections software". The strongest version says how others will see them: their boss, their team, their peers. Hormozi's point is that the outcome people value most is the one that raises their status.

**Test:** a customer who reads the before says "that's me". If it reads like a brochure, it is not their words yet.

---

## 2. The Four Drivers

| Driver | The buyer asks | What to write |
|--------|----------------|---------------|
| **Dream outcome** (raise it) | What will I get? | The after, above |
| **Likelihood** (raise it) | How do I know it will work for me? | Proof: real customers with real numbers, how many, a guarantee if there is one |
| **Time** (cut it) | How long until I see something? | The first concrete win, and when it arrives. They buy the end result, and stay for the first win |
| **Effort** (cut it) | What do I have to do? | What they no longer have to do. Done for them beats done by them |

**Work the bottom, not the top.** Anyone can promise a bigger outcome, so a bigger promise sets nobody apart. When two vendors promise the same outcome, it cancels out, and proof, time and effort decide. Make those three concrete, because the buyer judges what they believe, not the real number: "live in two days, we do the setup" beats "fast onboarding".

**Name the weakest driver**, and what would fix it. Usually it is proof, or the time to a first result.

---

## 3. Problems and Solutions

**List every step** the customer has to go through to reach the outcome, in order: before, during and after using the product.

**For each step, list what stops them**, in their words, under the four drivers:
- **Outcome:** it won't be worth it.
- **Likelihood:** it won't work for me, I won't stick with it, something will get in the way.
- **Effort:** it's too hard, too confusing, I'll be bad at it.
- **Time:** it takes too long, I don't have the time.

Aim for many problems: a dozen at least. Each one is a reason a buyer says no.

**Then turn each problem into a solution.** Write "how to" and reverse the problem: "it's too hard to chase late payers" becomes "how to get paid without calling anyone". Each solution names what the user does or provides. A problem with no solution yet stays on the list, marked open. Never paper over it.

The problems become the hooks for posts and first messages. The solutions become the offer.

---

## 4. Why Us

The mechanism: how the product produces the result in a way others don't. A mechanism, never an adjective. "We reconcile every payment with your ERP every night" is a mechanism. "Powerful and easy" is not.

---

## The File

```markdown
# Value Proposition

_Last updated: YYYY-MM-DD_

## For [ICP name, as in icp.md]
- **The line:** We help [who] get [dream outcome] in [time to the first result] without [effort], [proof].
- **Before:** [their situation, in their words, and what it costs them]
- **After:** [the dream outcome, and how others see them]
- **Proof:** [real customers and real numbers]
- **Time to first result:** [the first concrete win, and when]
- **Effort we remove:** [what they no longer have to do]
- **Why us:** [the mechanism]
- **Weakest driver:** [which one, and what would fix it]

### Problems and solutions
| Step | Problem, in their words | Driver | Solution |
|------|-------------------------|--------|----------|
```

Show the full draft. Save only after a clear yes. Then read back the line.

---

## Related Skills

- **[icp](../icp/SKILL.md)**: who each value proposition is for.
- **[outbound-context](../outbound-context/SKILL.md)**: the voice, and the first step for a new user.
- **[linkedin-posts](../linkedin-posts/SKILL.md)**: the problems are the hooks.
- **[initiatives](../initiatives/SKILL.md)**: the offer each test makes, built from the solutions.
- **[lead-magnet](../lead-magnet/SKILL.md)**: one problem, solved for free, that leads to the paid offer.
