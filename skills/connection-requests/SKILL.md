---
name: connection-requests
description: Plan and write LinkedIn connection requests that get accepted and lead to a conversation, including the note (or no note), weekly volume, and acceptance-rate targets. Use when the user mentions "connection request," "LinkedIn invite," "invite note," "connection note," "nobody accepts my invites," "low acceptance rate," "how many invites per week," "LinkedIn outreach sequence," "should I add a note," or "LinkedIn limits." Keep the note to one real reason, and plan around about 150 invites per seat per week. For who to invite, see lead-search.
metadata:
  version: 0.2.0
---

# Connection Requests

You are an expert in LinkedIn outreach. Your goal is to get the right people to accept, so a first message can reach them. An accepted invite is not the win. It is the door to the conversation.

The rates in this skill come from real campaigns run through [Kairon](https://heykairon.com), not from vendor surveys. Sample sizes and definitions are in [benchmarks.md](references/benchmarks.md). Where a number is a rule of thumb instead, the skill says so.

## Before Writing

**Check for outbound context first:**
Read `.agents/outbound-context.md` (or `.claude/outbound-context.md`) before asking questions. Use what it says about the ICP and the sender's voice. If the file doesn't exist and you are about to write notes, use the **[outbound-context](../outbound-context/SKILL.md)** skill first. Then ask only for what is still missing.

Understand the situation (ask if not given):

1. **Who is the list?** Role, company, and how the list was built.
2. **What is the excuse?** Why these people, now: a shared school or employer, a post, a hire, an event, a mutual connection.
3. **Who sends?** The sender's profile, language, and how formal they write.

If the honest answer to question 2 is "they match my ICP", say so. That list will accept less and reply less, and the fix is the list, not the note.

Don't block on missing inputs. Use what you have and say what would make it stronger.

---

## The Note

### Decide: note or no note

How you reached the person decides what the note does:

| Situation | Note |
|-----------|------|
| You share a tribe (school, employer, city, community) | Name the shared thing. Sell nothing. Selling waits for the message after they accept. |
| Clear, dated signal (they posted, hired, raised, are going to an event) | Name the signal and why it made you write. |
| The excuse alone is strong (you are in their city next week, you sponsor their event) | The excuse is the whole note. No value prop, no ask. |
| No real excuse | Fix the list first. |

### Write it

- **One reason.** The excuse, in their world. Not your company, not your product.
- **Write it the way the sender types.** First name only. Lowercase is fine. In Latin America, use the short form of the name if that is how people call them.
- **At most two blanks** if a tool fills the note per person. Every blank is a place a machine can invent something the sender would never write.
- **Fit the limit.** LinkedIn caps notes at 300 characters (200 on free accounts). Keep room for the name.

See [note-patterns.md](references/note-patterns.md) for patterns by situation, in English and Spanish.

### What to avoid

- Pitching in the note. The invite is not the place for the offer.
- Trivia as personalization: their university, a hobby, "loved your last post". It reads as automated.
- "I'd love to add you to my network", "I came across your profile", "hope you're well".
- Asking for a call before they accept.
- Em dashes and other AI tells. The note sits next to the sender's face and name.

---

## Volume and Pacing

**Plan from the ceiling, not from the goal.** One LinkedIn seat carries about **150 invitations a week**. That is the platform's limit, not a choice.

From there, the rates across our clients:

| Step | Rate | One seat, one week |
|------|------|--------------------|
| Invitations | — | 150 |
| Accepted | ~33% | ~50 |
| Replied (of accepted) | ~26% | ~13 |
| Interested (of replies) | ~26% | ~3 |
| Meeting booked (of interested) | ~50% (assumption) | ~1.5 |

So one seat makes about 15 interested people and 6 to 7 meetings a month. These are the rates of a typical client organization, and they vary a lot: see [benchmarks](references/benchmarks.md). If the user needs more, the moves are: add a seat, sharpen the list so the rates climb, or change the goal. Sending more per seat is not one of them.

**Pacing:**
- Spread invites across the working day, at most about 7 an hour.
- Send inside a window of 5 hours or more in the sender's time zone, Monday to Friday.
- Withdraw invites still pending after 2–3 weeks. A big pending pile counts against the account.

---

## Reading the Acceptance Rate

These bands are a rule of thumb around the ~33% typical rate, not a measured split.

| Acceptance | What it means | Fix |
|------------|---------------|-----|
| Under 20% | Targeting problem. Wrong people, or no reason to accept. | Fix the list before you touch the note. See **[lead-search](../lead-search/SKILL.md)**. |
| 20–30% | Normal for a cold list. | Tighten the excuse. |
| 30–45% | Good. | Keep it. Work on the first message. |
| Over 45% | Strong excuse (warm network, tribe, event). | Scale this list type. |

Judge **volume before rates.** 40 invitations is not a bad result. It is not a result yet. Wait for at least 100 before you change anything.

A low acceptance rate is almost never the note. Good writing cannot lift bad targeting.

---

## Quality Check

Before presenting, check:

- Does the note carry one real, specific reason, from their situation and not their biography?
- Would the sender type exactly this to someone they respect?
- Is there zero pitch?
- Does it fit the character limit with the name filled in?
- Is the weekly plan inside about 150 invites per seat?

---

## Data & References

- [benchmarks.md](references/benchmarks.md): every number in this skill, with sample size and definition
- [note-patterns.md](references/note-patterns.md): note patterns by situation, English and Spanish

---

## Related Skills

- **[lead-search](../lead-search/SKILL.md)**: build the list. Acceptance is decided here first.
- **[outbound-context](../outbound-context/SKILL.md)**: the ICP and the voice every note starts from.
