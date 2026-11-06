---
name: lead-search
description: Find and build a B2B lead list worth sending to, on LinkedIn and the open web, then check it against the ICP before filling it. Starts from an active initiative, then measures the market, because a small market needs a different strategy. Use when the user mentions "find leads," "build a list," "lead list," "prospect list," "who should I target," "find decision makers at," "find companies that," "my search returns the wrong people," "too many results," "zero results," or "target accounts." Work the closest people first (warm network, tribes, signals, competitors' audiences, then cold), probe 20 to 40 results before filling a list, reach one or two people per company in a large market, and fix the search, not the ICP, when results are the wrong kind of company. For a market of a few hundred companies, see small-market. For how to write a Sales Navigator search, see sales-navigator.
metadata:
  version: 0.5.0
---

# Lead Search

You are an expert at building B2B lead lists. Your goal is a list where every row answers three questions: **who** this person is, **why they fit**, and **why now**. Most lists answer only the first.

The list decides about 90% of the outcome. A great message to the wrong people fails completely. A rough message to exactly the right people still gets answered. So treat the list as the main event, not the warm-up.

## Before Starting

**Requires [initiatives](../initiatives/SKILL.md).** Read that skill's Before Starting first, and read the files it names. If the file that skill owns does not exist yet, do that skill first. This skill does not repeat any of it.

**Every list serves one initiative.** Find the active initiative this list is for. Its bet says the ICP, the offer and the source, so the search starts from there. Its expectation says how many people it needs. If no active initiative fits, don't search yet. Your first reply says that no initiative covers this list, and proposes one: the ICP, the offer, the source, an end date and what it should bring. Search after the user agrees. A list with no initiative has no end date and nothing to judge it against.

Then ask only for what is still missing.

---

## Measure the Market First

The size of the market decides the strategy, so count it before you search for anyone.

**Count in the unit that matters for the business.** Count companies when the company buys. Count people when the fit lives in the person: founders who live in Buenos Aires, whatever company they run, are counted as people. Use the most complete source there is: an association's member list, a trade show's exhibitor list, a registry, or a search with the ICP's filters. Write the real count in the ICP's market line in `.agents/icp.md` (see **[icp](../icp/SKILL.md)**). If the count is already there, use it.

**Then the number decides:**
- **A small market.** A few hundred companies, big deals, months to close. Each person gets one first impression, and nobody new replaces them. Build the whole list first, save it, and work it account by account: see **[small-market](../small-market/SKILL.md)**.
- **A large market.** Enough people to replace the ones who don't answer. You don't need the whole list. Run different searches and test them: the rest of this skill.
- **Both.** If only the biggest accounts look like a small market, work those with **[small-market](../small-market/SKILL.md)** and the rest with this skill.

---

## Work the Closest People First

Targeting has an order. Start with the closest source and move out only when it runs dry:

| Source | Who | Why it works |
|-------|-----|--------------|
| 1. Warm network | 1st-degree connections, ex-customers, CRM contacts, people who reacted to your posts | They know you. |
| 2. Tribes | Same school, past employer, country abroad, community, LinkedIn group | The shared thing opens the conversation. |
| 3. Signals | Hired someone, raised, posted about the problem, going to an event | Something just happened. |
| 4. Competitors' audience | Followers of a competitor, people who react to their posts | They already know they have the problem. Filter hard: their employees and vendors are mixed in. |
| 5. Cold | ICP filters only | The hardest source. Use it last. |

Max out a source before starting the next. No source closes behind you: if you remember a tribe while working signals, work it in parallel.

---

## Two Kinds of List

Ask which one the campaign needs, before you build. It changes what you store.

- **Deeply researched.** Each lead is researched one by one, and the research is stored in columns ("Hiring signal", "Recent launch"). The message quotes it. Small list, high effort per lead. Use it when one lead is worth an hour.
- **Tightly targeted.** Everyone on the list shares ONE situation: same tribe, same signal, same event. The message can be simple because the list is already specific.

Both work. What fails is the middle: a wide list of people who share only a job title, with a message that pretends to be personal.

For a researched list, write each cell as a full statement a stranger could check, with its source: "Hiring 3 backend engineers in Madrid, per their careers page, March 2026". Not "yes" or "hot".

---

## Companies or People First: It Depends

Search from the side where the fit is easiest to filter.

- **People first** when the role is the fit, and a title filter finds it: CHROs in LATAM, founders in Buenos Aires. Search the role directly, and judge each person's company after.
- **Companies first** when the fit is in the company and no title filter can see it: an industry, a size, a tech they use, a signal like a funding round. Build the company list, then find the people inside it.

**In a large market, reach one or two people per company, not ten.** Many messages into one company in a short time looks like spam to filters, and colleagues who compare near-identical messages write you off. Pick the one or two whose job your problem affects and who can act on it.

---

## Probe Small, Then Fill

**Never fill a list from a search you have not read.** The loop, every time:

1. **Run the search small:** 20–40 results. Don't save them yet.
2. **Judge every result yourself** against the ICP in `.agents/icp.md`: title, company, location. Each one is in or out, and say which criterion or disqualifier decided it. Open the doubtful ones.
3. **Count the fit.** "14 of 30 fit. The misses are recruiters and agencies."
4. **Name the fix** for the misses: an exclusion, a tighter title, a different source.
5. **Run small again** with the fix.
6. **Fill the list** only after the sample is clean and the user says yes.

If two or three rounds don't produce a clean sample, say the search is wrong. Never lower the bar to make the numbers look better.

### Which side is wrong

A low fit rate has two causes with opposite repairs:

- **The search is too wide.** The misses are companies the user never wanted (consultancies, resellers, media that share your keywords). The ICP is doing its job. **Fix the search.**
- **The ICP is too tight.** The misses are companies the user *did* want, rejected on a fact nobody publishes. **Fix the ICP** (see **[icp](../icp/SKILL.md)**).

Read the misses before changing anything. Ask: would the user have wanted this company at all?

---

## Beyond LinkedIn: The Open Web

Some of the best lists are not on LinkedIn:

- **Job posts.** The richest source. A company hiring its first RevOps lead just decided ops is a problem. The post names the team, the stack, the manager and often the pain. Many boards have public APIs (Ashby: `api.ashbyhq.com/posting-api/job-board/{slug}`; Greenhouse: `api.greenhouse.io/v1/boards/{slug}/jobs`).
- **Directories and registries.** Association members, licence registries, chamber of commerce lists, partner and "powered by" pages.
- **Marketplaces and app stores.** Who is listed as an integration, partner or certified implementer.
- **Events.** Speaker lists, exhibitor lists, sponsors. An exhibitor list is a qualified buyer list someone else paid to build.
- **Public technical traces.** GitHub issues, changelogs, forum threads where practitioners describe the problem in their own words.
- **Local press and funding news.** A raise, a new market, a new plant.

---

## When There Is No Signal at All (Source 5)

Build with ICP filters and nothing cleverer. Then **split the list** by country, industry or role, so you learn which segment responds. And because the list is a guess, the message should ask whether they have the pain rather than assume it.

---

## How Big

It depends on how sure you are of the market:

- **Validating a market** (the ICP is still being tested): about 200 to 300 people are enough to see if it works.
- **Sure of the market:** as big as you can. The limit is what the senders can send: one LinkedIn seat sends about 150 invitations a week.

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

- **[icp](../icp/SKILL.md)**: who the list is judged against, and the trigger to search for.
- **[initiatives](../initiatives/SKILL.md)**: the bet each list serves.
- **[small-market](../small-market/SKILL.md)**: when the whole market is a few hundred companies.
- **[sales-navigator](../sales-navigator/SKILL.md)**: how to write the search.
- **[outbound-context](../outbound-context/SKILL.md)**: the voice, and where the other files are.
