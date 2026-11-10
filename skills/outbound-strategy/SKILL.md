---
name: outbound-strategy
description: Give strategic advice on outbound before any list or message. Whether outbound suits the business at all, why it works now, what to chase at the user's stage, when to hand outreach to an SDR or an agency, and what to use AI for. Use when the user says "should I do outbound," "is outbound dead," "does cold outreach still work," "should I stop outbound," "should I hire an SDR," "should I hire an agency," "can someone else do my outreach," "what should I focus on," "we're early, what do we chase," "can AI do my outreach," "can I automate all my messages," or "should I just send more." Test the two preconditions (market size and deal value), treat early outbound as discovery until a motion repeats, keep outreach with the founder until then, automate the boring parts and keep the judgment, and answer first. For a goal with a date, see initiatives. For a campaign that stopped working, see funnel-diagnosis.
metadata:
  version: 0.1.0
---

# Outbound Strategy

Most outbound advice starts with the list or the message. This skill answers the question before those: should this business do outbound, what should it chase right now, who should do it, and what can a machine do for them. The answers below are Luciano's opinions from running outbound for Kairon's clients, and they say "I think" where they are opinions. The numbers come from [benchmarks](../initiatives/references/benchmarks.md).

## Before Starting

**Requires [outbound-context](../outbound-context/SKILL.md).** Read that skill's Before Starting first, and read the files it names. If the file that skill owns does not exist yet, do that skill first. This skill does not repeat any of it.

Read `.agents/icp.md` and `.agents/initiatives.md` if they exist. They say how big the market is, how the customers arrived, and how much outbound the user has really run. Judge from those facts, not from how the user describes the company.

**Answer first.** Say the recommendation in one or two sentences, then the reasons, then the next step. Ask for one missing fact at a time, and only when the answer depends on it.

---

## 1. Does Outbound Suit This Business?

Outbound is a bet with two preconditions. Check both before any other advice.

- **Market size.** If only a few hundred companies could ever buy, outbound as a numbers game is the wrong main motion. The list runs out fast, and a rough message burns accounts that never come back. Go deep instead: see **[small-market](../small-market/SKILL.md)**.
- **Deal value.** Each customer must be worth a human conversation. With tiny contracts, the work to research, reach and close one customer never pays back. Recommend a product-led or marketing-led motion instead. A higher contract value makes every part of outbound easier.

If the market is large enough, the problem sharp and expensive, and the deal worth a conversation, I think outbound is likely the highest-leverage move the user has. If one test fails, say so plainly now. If you lack the deal value or the market count, ask for it before you advise.

---

## 2. Is Outbound Dead?

I think now is the best time to do outbound. LinkedIn is full of AI slop, in posts and in messages. Nobody is trying hard, so being different is cheap.

The outbound that is dead deserved to die: spam, sent with no work to reach the right person with the right message. A message that shows the sender did the research, written for this person and no one else, still gets answered. In our clients' campaigns, the median organization gets 33% of invitations accepted, 26% of those reply, and 26% of the replies are interested. That is about 2 interested people per 100 invitations ([benchmarks](../initiatives/references/benchmarks.md)).

The old choice is gone too. Research by hand meant few messages. Skipping research meant spam. The research no longer has to be done by hand, so quality and volume can both go up.

The ceiling is the number of people with a real reason to write to them, not the platform's limits. When those run out, look for new signals and new markets. Never fill the gap with weaker messages.

**When the user says "it doesn't work for us",** ask for their numbers and run **[funnel-diagnosis](../funnel-diagnosis/SKILL.md)** before you agree. A product pitch to a cold list is a fixable offer, not proof the channel is dead: see **[message-copies](../message-copies/SKILL.md)**.

---

## 3. What to Chase at Each Stage

**The stage that matters is how long the user has done outbound, not how big the company is.** A company with many customers is still early if they all came warm. Someone referred already trusts you. A stranger does not. Selling to the stranger is a different job.

**Early in outbound, treat it as discovery.** I see outbound at this stage as a learning tool that sometimes brings revenue on the side. Every reply and every silence says who has the problem and how they think about it. Every objection is a bug report on the positioning. When someone lights up at one sentence, they hand you the messaging.

Founders who treat it as a vending machine (effort in, meetings out) count meetings, quit after two quiet weeks, and learn nothing.

**The first job is a motion the user can repeat.** Three customers won through charm and warm intros are revenue without a motion: nobody can say which message worked, which objection was real, or which company fit. The mark I would aim for, as a rule of thumb: 30 to 50 qualified prospects through the process, and 10 to 20 of them converted. Short of that, more volume will not help. There is more to learn first.

**Once the motion repeats, the priority flips to revenue.** Even then, the user does not need a flood. As a rule of thumb, the first fifty customers come from a couple dozen sharp messages a day, kept up for months. When they need more reach, add a channel before adding volume.

Each bet with a date and a goal goes in **[initiatives](../initiatives/SKILL.md)**.

---

## 4. When to Delegate Outreach

**Until the motion repeats, the founder does the outreach.** They build the list, write the messages and read every reply. This holds for an agency and for a first SDR.

- **The learning is the point.** When someone else runs early outbound, the founder gets a report instead of the conversation. The messaging ends up aimed at what the agency says, not at what the market said.
- **Look at what the agency is paid for.** The usual deal pays for meetings that happen, with no fit requirement. So the user gets meetings, and fit is nobody's job. One case I know: USD 2,500 a month for two months of LinkedIn outreach, and one good meeting from it.
- **"I don't have time to sell" is a finding,** not a reason to delegate. The operation has bottlenecks big enough to keep the founder out of the market. Fix those first.

**Delegate once the motion is proved:** targeting and messaging the user knows work, with scale as the only job left. Before that, they pay someone else to run the experiment they needed to watch.

---

## 5. What to Use AI For

**AI is leverage on craft. Used for volume, it is what ruined the channel.** A thousand near-identical messages land in the most crowded, most filtered category there is.

- **Automate the boring parts.** Research (reading a site, the news, the job posts, scanning many accounts for signals), sending, enriching, verifying, logging and scheduling. A system does all of it better than a person.
- **Keep the judgment.** Who to go after and why, what a signal means for this company, what a reply really says. That part wins deals, and it stays with the user.
- **Go deeper on fewer people, not shallower on more.** A name and a scraped detail in a template is personal in form and generic in substance. Buyers and spam filters spot it at once. How to leave a model only the blanks it can fill: **[message-copies](../message-copies/SKILL.md)**.
- **Full autonomy fits simple conversations.** Sending someone the link to an event needs no judgment. The more a conversation carries, the more it needs a person.

The platform caps volume anyway: about 150 invitations per LinkedIn seat per week ([benchmarks](../initiatives/references/benchmarks.md)).

---

## Related Skills

- **[small-market](../small-market/SKILL.md)**: when the market is a few hundred companies.
- **[initiatives](../initiatives/SKILL.md)**: turn a strategy into a bet with a date and a goal.
- **[funnel-diagnosis](../funnel-diagnosis/SKILL.md)**: when the user says outbound does not work, find the stage that broke.
- **[message-copies](../message-copies/SKILL.md)**: the offer and the message, and what a model may fill.
- **[icp](../icp/SKILL.md)**: who the motion goes after.
