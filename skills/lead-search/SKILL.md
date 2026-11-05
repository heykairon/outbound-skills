---
name: lead-search
description: Find and build a B2B lead list worth sending to, on LinkedIn Sales Navigator, classic LinkedIn search and the open web (job posts, directories, event exhibitor lists), then check it against the ICP before filling it. Use when the user mentions "find leads," "build a list," "lead list," "prospect list," "Sales Navigator search," "Sales Nav filters," "who should I target," "find decision makers at," "find companies that," "my search returns the wrong people," "too many results," "zero results," or "target accounts." Work the closest people first (warm network, tribes, signals, competitors' audiences, then cold), probe 20 to 40 results before filling a list, reach one or two people per company, and fix the search, not the ICP, when results are the wrong kind of company. For the invitations that follow, see connection-requests.
metadata:
  version: 0.1.2
---

# Lead Search

You are an expert at building B2B lead lists. Your goal is a list where every row answers three questions: **who** this person is, **why they fit**, and **why now**. Most lists answer only the first.

The list decides about 90% of the outcome. A great message to the wrong people fails completely. A rough message to exactly the right people still gets answered. So treat the list as the main event, not the warm-up.

## Before Starting

**Check for outbound context first:**
Read `.agents/outbound-context.md` (or `.claude/outbound-context.md`). The ICP, the countries and the best customers are there. If the file doesn't exist, use the **[outbound-context](../outbound-context/SKILL.md)** skill first: it takes a few minutes and every later search reuses it. Then ask only for what is still missing.

If there is no ICP at all, stop and define one first with **[outbound-context](../outbound-context/SKILL.md)**. Searching without one means judging results against a hunch. Skip any ICP marked discarded. If the user asks for it again, show the reason it was discarded first.

---

## Work the Closest People First

Targeting has an order. Start close and move out only when a stage runs dry:

| Stage | Who | Why it works |
|-------|-----|--------------|
| 1. Warm network | 1st-degree connections, ex-customers, CRM contacts, people who reacted to your posts | They know you. |
| 2. Tribes | Same school, past employer, country abroad, community, LinkedIn group | The shared thing opens the conversation. |
| 3. Signals | Hired someone, raised, posted about the problem, going to an event | Something just happened. |
| 4. Competitors' audience | Followers of a competitor, people who react to their posts | They already know they have the problem. Filter hard: their employees and vendors are mixed in. |
| 5. Cold | ICP filters only | The hardest stage. Use it last. |

Max out a stage before starting the next. No stage closes behind you: if you remember a tribe while working signals, work it in parallel.

---

## Two Kinds of List

Ask which one the campaign needs, before you build. It changes what you store.

- **Deeply researched.** Each lead is researched one by one, and the research is stored in columns ("Hiring signal", "Recent launch"). The message quotes it. Small list, high effort per lead. Use it when one lead is worth an hour.
- **Tightly targeted.** Everyone on the list shares ONE situation: same tribe, same signal, same event. The message can be simple because the list is already specific.

Both work. What fails is the middle: a wide list of people who share only a job title, with a message that pretends to be personal.

For a researched list, write each cell as a full statement a stranger could check, with its source: "Hiring 3 backend engineers in Madrid, per their careers page, March 2026". Not "yes" or "hot".

---

## Companies First, Then People

Unless the list comes from a relationship (warm network, tribe), build the **companies** list first, then find the people inside it.

**Reach one or two people per company, not ten.** Many messages into one company in a short time looks like spam to filters, and colleagues who compare near-identical messages write you off. Pick the one or two whose job your problem affects and who can act on it.

---

## Probe Small, Then Fill

**Never fill a list from a search you have not read.** The loop, every time:

1. **Run the search small:** 20–40 results. Don't save them yet.
2. **Read every result yourself** against the ICP: title, company, location. Open the doubtful ones.
3. **Count the fit.** "14 of 30 fit. The misses are recruiters and agencies."
4. **Name the fix** for the misses: an exclusion, a tighter title, a different source.
5. **Run small again** with the fix.
6. **Fill the list** only after the sample is clean and the user says yes.

If two or three rounds don't produce a clean sample, say the search is wrong. Never lower the bar to make the numbers look better.

### Which side is wrong

A low fit rate has two causes with opposite repairs:

- **The search is too wide.** The misses are companies the user never wanted (consultancies, resellers, media that share your keywords). The ICP is doing its job. **Fix the search.**
- **The ICP is too tight.** The misses are companies the user *did* want, rejected on a fact nobody publishes. **Fix the ICP** (see **[outbound-context](../outbound-context/SKILL.md)**).

Read the misses before changing anything. Ask: would the user have wanted this company at all?

---

## Sales Navigator: The Rules That Matter

Sales Navigator is the default for stages 3 to 5. Full detail and worked examples in [sales-navigator.md](references/sales-navigator.md). The traps that cost the most:

- **Titles go in the job title filter, not keywords.** Keywords match the whole profile, so they find people who did the job ten years ago.
- **For "leaders of X", combine seniority with function words** ("head", "director", "VP", "manager" + "payments" OR "billing"). A hand-written list of titles misses the variants people actually use.
- **Exclude before you add.** A recurring wrong type (recruiters, students, agencies) is fixed with an exclusion, not another positive filter.
- **Same filter, several values = OR. Different filters = AND.** Each filter you add narrows.
- **Regions don't resolve.** "LATAM" or "Europe" fail. Add one location per country.
- **"Startup" is not a filter.** Use headcount (1–10, 11–50, 51–200).
- **Industry uses LinkedIn's names** ("Financial Services", not "fintech"). A business model ("SaaS", "fintech") goes in keywords.
- **Keywords are boolean.** Quote each term, uppercase OR, and wrap the group in parentheses: `("fintech" OR "payments" OR "neobank")`. Bare words are AND-ed and return zero.
- **A combination that matches nobody does not return zero.** Sales Navigator drops a filter and answers a wider question. A suspiciously large result for a narrow ask means "nobody matched". Read the results before trusting the count.

---

## Beyond LinkedIn: The Open Web

Some of the best lists are not on LinkedIn:

- **Job posts.** The richest source. A company hiring its first RevOps lead just decided ops is a problem. The post names the team, the stack, the manager and often the pain. Many boards have public APIs (Ashby: `api.ashbyhq.com/posting-api/job-board/{slug}`; Greenhouse: `api.greenhouse.io/v1/boards/{slug}/jobs`).
- **Directories and registries.** Association members, licence registries, chamber of commerce lists, partner and "powered by" pages.
- **Marketplaces and app stores.** Who is listed as an integration, partner or certified implementer.
- **Events.** Speaker lists, exhibitor lists, sponsors. An exhibitor list is a qualified buyer list someone else paid to build.
- **Public technical traces.** GitHub issues, changelogs, forum threads where practitioners describe the problem in their own words.
- **Local press and funding news.** A raise, a new market, a new plant.

Use public business information only. Don't bypass logins or CAPTCHAs, and don't buy lists with no known source.

---

## When There Is No Signal at All (Stage 5)

Build with ICP filters and nothing cleverer. Then **split the list** by country, industry or role, so you learn which segment responds. And because the list is a guess, the message should ask whether they have the pain rather than assume it.

---

## How Big

Plan from what the senders can send. One LinkedIn seat sends about 150 invitations a week (see **[connection-requests](../connection-requests/SKILL.md)**). Aim for enough people to keep every seat sending for about two working weeks: roughly 250 per seat at 25 a day.

**The floor is about 30.** Below that, the results can't tell luck from a working motion.

---

## Build the First 50 by Hand

For a new market, research the first 50 accounts one by one: their site, job posts, founder's posts, reviews, news. It feels slow. It teaches you which traits actually predict a fit and which signal you were sure about is noise. Automating before you know that is scaling a hunch.

---

## Output

A table, or CSV past about 25 rows:

```
| Name | Title | Company | Why they fit | Why now | Source | Confidence |
```

After the table, always add:
- **Fit rate of the sample**, and what the misses had in common.
- **Top 5** to reach first, one sentence each on why.
- **Open questions** you could not verify.

---

## Related Skills

- **[connection-requests](../connection-requests/SKILL.md)**: what to do with the list on LinkedIn.
- **[outbound-context](../outbound-context/SKILL.md)**: where the ICP and best customers live.
