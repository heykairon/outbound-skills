---
name: content-strategy
description: Decide what the user posts on LinkedIn, how often, and how to tell if it works, and keep it in .agents/content-strategy.md, the one file the post skill reads for what to write about. Use when the user says "content strategy," "what should I post," "content ideas," "I don't know what to post," "content calendar," "posting strategy," "how often should I post," "personal branding," "thought leadership," "my posts get no reach," "lots of impressions but no leads," "should I start a newsletter," or "how do I get leads from content." Pick one subject where the ICP's pain meets what the user sells, rotate four pillars (tactical, aspirational, personal, insight), each with its own map of what to post, post once a week, measure leads per post rather than impressions, work the people who react, and add a newsletter once posting is steady. For writing each post, see linkedin-posts.
metadata:
  version: 0.3.0
  section: content
---

# Content Strategy

Content is the one lead source with no ceiling. LinkedIn limits invitations and messages per day, lists run out, markets have a size. A post doesn't. And someone who read a post and then wrote to the user arrives with intent: they already know what the user does.

This skill owns `.agents/content-strategy.md`: the subject, the pillars and their topics, the cadence, and what brought leads. The post skill reads it. It never decides the subject itself.

## Before Starting

**Requires [value-prop](../value-prop/SKILL.md).** Read that skill's Before Starting first, and read the files it names. If the file that skill owns does not exist yet, do that skill first. This skill does not repeat any of it.

Read `.agents/content-strategy.md` if it exists, and update only what changed. Read the user's last posts too, if they have any: what they already wrote about, and what brought leads. Check the author of each one. A repost, or a post by someone else that shows up in the feed, is not the user's.

Draft from what you hold, then ask, one thing per turn.

---

## 1. One Subject

**Pick one subject and stay on it.** LinkedIn reads months of activity to decide who the user is and who should see them. AI today, recruiting tomorrow, manufacturing next week: they become hard to place, and the reach goes to someone easier to categorise.

The subject is the overlap of **what the ICP cares about** and **what the user sells**. Take it from the problems in `.agents/value-prop.md`: the problems are what the ICP cares about, the solutions are what the user sells.

**Test:** would the ICP read a post on this subject, and think "this person can solve my problem"? A subject the ICP doesn't care about brings the wrong audience. A subject unrelated to what the user sells brings an audience that never buys.

---

## 2. Four Pillars

Inside the one subject, rotate four angles:

| Pillar | Proves | Example |
|--------|--------|---------|
| **Tactical** | The user knows what they're talking about | A framework, a step-by-step, a tip the reader can use today |
| **Aspirational** | The approach works | A real customer's result, or the user's own, with how it happened |
| **Personal** | The user is a person, not a company | A hard moment and how they got through it, the team's culture. Always a concrete story, with a photo or a video |
| **Insight** | The user is at the front of the field | Their real opinion on news, where the field is going |

The personal pillar is the one people skip, and often the one that does best.

Each pillar gets its own map, built a different way:

- **Tactical: a map of concepts.** Split the user's work into its parts, in order (for outbound: decide the strategy, find the leads, reach them until there is a call, post). Under each part, list the concepts the user can teach: "How to define your ICP", "How to write good follow-ups". A concept can be told in many ways. A post is one angle on one concept, so never list post titles here.
- **Aspirational: one story per concept.** For each tactical concept, write the story that proves it: someone (the user, a customer, or a well-known company) who had that problem, and how they got past it. "Someone who wrote to anyone, and how they started to filter." Fill in the real case when there is one.
- **Personal: the themes the user already posts about.** Personal posts come spontaneously, so don't plan the stories. Read the user's own posts, name the two or three themes they come back to, and keep the ones that drew the most. Under each theme, cite the posts already published, with their reactions.
- **Insight: the user's opinion themes.** The same way: two or three themes from their own posts, with a stance. Posts that go against the current draw the most comments.

When the user says "I don't know what to post", propose from the maps. Don't ask them to pick a topic from nothing.

Never invent the material behind a story. If a concept has no real case yet, say what to collect: "Your next customer result goes here."

---

## 3. Cadence

**Once a week is enough** to see traction. Each pillar comes around about once a month. Steady beats a lot: four posts in one week and then silence for a month teaches LinkedIn nothing.

---

## 4. Measure Leads, Not Likes

Impressions and likes give you nothing to act on. After each post, count:

- **Saves and sends to a colleague.** The strongest signs the post landed.
- **Profile visits and new connections** that came from the post.
- **Whether the ICP engaged.** Ten decision-makers who save it beat a hundred unrelated likes.
- **Leads.** Conversations that started from the post.

**What moves reach**, as LinkedIn is widely understood to work (nobody outside it has measured this): attention. How long people stop to read the post, and whether they save it. Reach follows each reader's interests, not only the user's network, so a post can reach the ICP with no connection to the user. And a post earns its reach over days, not in the first hour, so don't judge it the same day.

A post with many impressions and no leads reached the wrong people, or said nothing the ICP needed. Check who engaged before you call it a success.

**Let leads per post decide what to write more of.** Write each post's result in the file, next to its topic.

---

## 5. Work the People Who React

Everyone who commented, reacted or visited the profile came to the user. Open a conversation with the ones who fit the ICP. Ask for their view on the post, not for a meeting: the conversation starts warmer than any cold message, and the answer says what to write next.

---

## 6. The Newsletter

Once the user posts every week, give readers a place to subscribe, such as LinkedIn's own newsletter. Not before: a newsletter with no weekly posts behind it has nobody to grow from.

Put real learnings in it, and take time writing them. Subscribers are an asset that grows, and a weak issue is how you lose them. A link to the newsletter is not an offer in a cold message: it asks the reader to work, and gives them nothing for it.

---

## The File

```markdown
# Content Strategy

_Last updated: YYYY-MM-DD_

## Subject
[The one subject: where the ICP's problem meets what the user sells]
- **For:** [ICP name, as in icp.md]
- **Cadence:** [once a week, on which day]

## Pillars
### Tactical
1. [part of the work]
   - [a concept the user can teach]
### Aspirational
A story (the user's own, a customer's, or a well-known company's) of someone who...
1. [part of the work]
   - [had the problem a tactical concept solves, and how they got past it]
### Personal
1. [a theme the user already posts about]. Already posted: [post (reactions)]
### Insight
1. [an opinion theme, with a stance]. Already posted: [post (reactions)]

## What worked
| Date | Topic | Pillar | Saves | ICP who engaged | Leads |
|------|-------|--------|-------|-----------------|-------|

## Newsletter
[none yet | name, cadence, subscribers]
```

A real one, filled in: [Kairon's content strategy](references/example.md).

Show the full draft. Save only after a clear yes. Then say in one line the subject, and the first topic to post.

---

## Related Skills

- **[linkedin-posts](../linkedin-posts/SKILL.md)**: how to write each post.
- **[value-prop](../value-prop/SKILL.md)**: the problems and solutions the subject comes from.
- **[linkedin-profile](../linkedin-profile/SKILL.md)**: what readers see when they click the user's name.
