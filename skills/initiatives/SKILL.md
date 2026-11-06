---
name: initiatives
description: Create, track and review the user's go-to-market initiatives in .agents/initiatives.md. An initiative is a bet with an end date (one ICP, one offer and one source of leads, changing one thing such as region, industry, size, buyer, offer or source) and what it should bring by then, worked back from real rates. Use when the user says "I want to test," "let's try selling to," "new initiative," "what should we try next," "set a goal," "weekly review," "checkpoint," "how is the push going," "did it work," "what have we tried," or starts outreach toward a goal with a date. Propose the goal with its arithmetic, judge volume before rates, compare against the user's own numbers, end every review with a next move that has an owner, and never propose again what already failed without saying what is different. For who the user is (value proposition, ICPs, voice), see outbound-context.
metadata:
  version: 0.2.2
---

# Initiatives

An initiative is a bet: this ICP will want this offer, and by this date we will know. Written down, it does three things most teams never do. It puts a date on the bet. It says in advance what success looks like. And it keeps a record of what was already tried.

## Before Starting

Read `.agents/icp.md`. Every initiative goes after one of its ICPs. If the initiative goes after people no ICP describes, use **[icp](../icp/SKILL.md)** to add one first, with the status the user gives it. Read `.agents/outbound-context.md` for the offer and the voice. If it doesn't exist, use **[outbound-context](../outbound-context/SKILL.md)** first.

Then read `.agents/initiatives.md`, if it exists. Look for two things:
- **An open initiative with the same bet.** Update it. Don't start a second one.
- **An ended initiative that tried something close.** Never propose it again without saying what is different this time. Check the ICP's status too: a discarded ICP comes with its reason.

Ask for one thing per turn. Draft from what you hold, then ask.

---

## What an Initiative Is

**One ICP, one offer, one source.** The ICP is who you sell to. The offer is the reason to say yes. The source is where the people on the list come from, and what gives you a reason to write to them. Change one thing from what already works: the region, the industry, the company size, the buyer, the offer or the source. Change two at once and the result cannot tell you which one mattered.

**The offer is the reason to say yes.** "I'm in your city next week, coffee?" A report on their industry. A seat at an event. A session on a set date. What makes sense to test depends on the business, so propose, and let the user pick. In our campaigns, a specific session on a specific date drew 17–22% interested replies. A report with no date drew 7–9% ([benchmarks](../connection-requests/references/benchmarks.md)).

### Start with the closest source

The same ICP answers very differently depending on the source, closest first:

1. **Warm network.** They know the sender.
2. **Tribes.** They share something with the sender: a school, a past employer, a country.
3. **Signals.** Something just happened to them: a hire, a new branch, a post about the problem.
4. **Competitors' audience.** They already know they have the problem.
5. **Cold.** Only the ICP filters. The hardest source.

Propose the closest source that still has people in it. Move to the next one when it runs dry, and keep the earlier ones going. Never default to cold. If you don't know whether the sender has a network or a tribe in that market, that is your one question: the source changes every rate in the arithmetic. How to build each list is in **[lead-search](../lead-search/SKILL.md)**.

---

## Work the Expectation Backwards

**Propose the goal. Don't ask for it.** Draft it in the unit the user needs (calls, customers, sign-ups for an event, not always replies), with the arithmetic, and ask them to confirm or move it.

Work back from the goal to invitations. Use the user's own rates if they have sent before. If not, use our measured rates and **say they are an assumption**: about 33% of invitations accepted, 26% of accepted reply, 26% of replies interested, about half of interested book a meeting (an assumption, not a measurement), and about 150 invitations per LinkedIn seat per week ([benchmarks](../connection-requests/references/benchmarks.md)).

> 5 meetings by December 15. If half the interested book (an assumption), that is 10 interested replies. At 26% of replies interested, about 38 replies. At 26% of accepted replying, about 150 accepted. At 33% accepted, about 450 invitations. One seat sends about 150 a week, so one seat needs three weeks.

**If it does not fit before the date, say so.** Then name the choice: move the goal, add a sender, or pick a warmer audience. Never write a round number because it sounds like a goal.

---

## The File

```markdown
# Initiatives

## [Short name, e.g. "Distributors, Chile"]
- **Status:** active | ended
- **The bet:** [ICP from icp.md] + [the offer] + [the source]. [Why we think it could work, and why now.]
- **What changes:** [the one thing that differs from what already works]
- **Until:** YYYY-MM-DD
- **What we expect:** [About 450 invitations by the date. At our rates, about 38 replies, 10 interested and 5 meetings. The rates are an assumption until the first review.]
- **Campaigns:** [one line each, what it does]

### Reviews
- **YYYY-MM-DD, at risk.** What happened: [numbers, with the denominators]. What it means: [...]. Last time we said: [...], [done or not]. Next: [the move], owner [name].

### Result
[Only once it ends. Worked, didn't work, or can't tell. The numbers, and what we learned in one line.]
```

Show the full draft. Save only after a clear yes. Ended initiatives stay in the file: they are the record.

---

## The Weekly Review

Ask for the numbers since the last review, per campaign: invitations, accepted, messages, replies, interested, and the goal unit. Read them from a tool if one has them. Never judge before you have the numbers.

1. **Volume before rates.** Below about 20 invitations, 10 messages or 5 replies, that rate means nothing yet. Say "not enough to judge", and don't colour it. A real case: 43 invitations, 30% accepted against an average of 35%. That gap is two people. The initiative has a volume problem, not a performance problem, and the next move is to send more, not to rewrite the copy.
2. **Compare against the user's own numbers,** then against "What we expect". Never against an industry average nobody measured.
3. **Say whether the last move was done.** Read the last review's next move. "Last time we said to narrow the list to Córdoba; the campaign still runs the old list." If the same move is undone three reviews running, that is the finding.
4. **Name the next move, with an owner.** Lead with the change that matters most, specific enough to start without a follow-up question. More moves are fine, each with a name on it. Never end on a menu with nobody's name.
5. **Give it a health.** On track: the numbers support it, at enough volume to believe them. At risk: something has to change, including "we have not sent enough to know". Off track: it is not working as stated. Say what would have to be true to recover, or say it should end.

Add each review under the last one. Never rewrite an old review: a change of mind is a new review, and the record is only worth reading because it shows what was believed at the time.

---

## Ending an Initiative

At the end date, or earlier if the user calls it, write the **Result**: worked, didn't work, or can't tell. "Can't tell" is the honest result when too little was sent. It does not mean the ICP failed.

Then ask the user what it means for the ICP. Whether it is validated or discarded is their call. Record their answer and reason in the ICP's status in `.agents/icp.md` (see **[icp](../icp/SKILL.md)**).

---

## Related Skills

- **[icp](../icp/SKILL.md)**: the ICPs every initiative goes after, and where each ICP's status lives.
- **[outbound-context](../outbound-context/SKILL.md)**: the value proposition and the voice.
- **[lead-search](../lead-search/SKILL.md)**: build the list for the initiative's ICP.
- **[connection-requests](../connection-requests/SKILL.md)**: the invitations, and the measured rates the expectation uses.
- **[linkedin-posts](../linkedin-posts/SKILL.md)**: content that serves the active initiatives.
