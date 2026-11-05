---
name: connection-requests
description: Plan and write LinkedIn connection requests that get accepted and lead to a conversation, including the warm-up touches before the invite, the note (or no note), weekly volume, and acceptance-rate targets. Use when the user mentions "connection request," "LinkedIn invite," "invite note," "connection note," "nobody accepts my invites," "low acceptance rate," "how many invites per week," "warm up before inviting," "profile visit before invite," "LinkedIn outreach sequence," "should I add a note," or "LinkedIn limits." Warm up first (visit and like or comment), invite about an hour later, keep the note to one real reason, and plan around about 150 invites per seat per week. For who to invite, see lead-search.
metadata:
  version: 0.1.1
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

## The Sequence: Warm Up, Then Invite

A cold invite comes from a stranger. A warm one comes from a name they saw an hour ago.

**Default sequence:**

```
Visit profile  →  Like (or comment on) their last post  →  wait 1 hour  →  Invite with note
                                                                    →  wait up to 7 days for accept
                                                                    →  first message
```

- **Wait 1 hour, not 1 day.** The visit and the like show up in their notifications. The invite must arrive while that is still fresh. A day later they forgot it, and the warm-up bought nothing.
- **A comment beats a like** when the person posts. It is the only warm-up touch they actually read. It must say something real about the post, never "Great post!".
- **No recent post?** Visit only, then invite.
- **Opening with a bare invite is the exception.** If you drop the warm-up, say why.

In our campaigns, sequences that visited the profile before inviting reached an interested reply from **19.6%** of the people who got a message, against **12.2%** for cold invites.

---

## The Note

### Decide: note or no note

How you reached the person decides what the note does:

| Situation | Note |
|-----------|------|
| You share a tribe (school, employer, city, community) | Name the shared thing. Sell nothing. Selling waits for the message after they accept. |
| Clear, dated signal (they posted, hired, raised, are going to an event) | Name the signal and why it made you write. |
| The excuse alone is strong (you are in their city next week, you sponsor their event) | The excuse is the whole note. No value prop, no ask. |
| No real excuse | No note, or fix the list first. A generic note is worse than none. |

### Write it

- **One reason.** The excuse, in their world. Not your company, not your product.
- **40–55 words** did best in our sends. Shorter notes often carry no reason to accept.
- **End on one question** when you ask anything. Notes ending on a question reached an interested reply **5.5%** of the time, against **3.9%** without.
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
| Accepted | ~30% | ~45 |
| Replied (of accepted) | ~18% | ~8 |
| Interested (of replies) | ~50% | ~4 |

So one seat makes about 16 interested people a month. If the user needs more, the moves are: add a seat, sharpen the list so the rates climb, or change the goal. Sending more per seat is not one of them.

**Pacing:**
- Spread invites across the working day, at most about 7 an hour.
- Send inside a window of 5 hours or more in the sender's time zone, Monday to Friday.
- Withdraw invites still pending after 2–3 weeks. A big pending pile counts against the account.

---

## Reading the Acceptance Rate

These bands are a rule of thumb around the ~30% average, not a measured split.

| Acceptance | What it means | Fix |
|------------|---------------|-----|
| Under 20% | Targeting problem. Wrong people, or no reason to accept. | Fix the list before you touch the note. See **[lead-search](../lead-search/SKILL.md)**. |
| 20–30% | Normal for a cold list. | Add the warm-up, tighten the excuse. |
| 30–45% | Good. | Keep it. Work on the first message. |
| Over 45% | Strong excuse (warm network, tribe, event). | Scale this list type. |

Judge **volume before rates.** 40 invitations is not a bad result. It is not a result yet. Wait for at least 100 before you change anything.

A low acceptance rate is almost never the note. Good writing cannot lift bad targeting.

---

## Quality Check

Before presenting, check:

- Is there a warm-up before the invite, and is the gap 1 hour?
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
