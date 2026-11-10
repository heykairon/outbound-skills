---
name: large-market
description: Build lead lists in a large market (more people than you could ever write to, so the ones who don't answer are replaced by new ones). Use when the user says "which source should I use," "start with a cold search," "load all the results," "fill the list," "the search is full of the wrong companies," "should I change the ICP," "how many leads do I need," "split the list," "who do I contact at each company," "job posts as leads," or "exhibitor list." work the ICP's sources in order, closest first, and never default to cold, search from the side a filter can see (people or companies), reach one or two people per company, probe 20 to 40 results before filling, fix the search when the misses are companies nobody wanted, and split a cold list by segment. For counting the market and judging each result, see lead-search.
metadata:
  version: 0.3.2
  section: lists
---

# Large Market

In a large market you never run out of people. When someone doesn't answer, someone new takes their place. So you don't build the whole market. You run different searches, test each one small, and keep the ones that work.

## Before Starting

**Requires [lead-search](../lead-search/SKILL.md).** Read that skill's Before Starting first, and read the files it names. If the file that skill owns does not exist yet, do that skill first. This skill does not repeat any of it.

This method is for a market lead-search counted as large. A market of a few hundred companies is worked account by account instead: see **[small-market](../small-market/SKILL.md)**.

---

## 1. Work the ICP's Sources in Order

Each ICP in `.agents/icp.md` lists its sources, closest first: the people who already know the user, their network and tribes, the people who come to them, warm intros, signals, and a lookalike search last. What each one is, is in **[icp](../icp/SKILL.md)**. If the ICP lists no sources yet, add them there first.

Start at the closest source that still has people in it. **Never default to the lookalike, even when the user asks for a cold search.** If a closer source exists in this market (the sender's network, a tribe, people who reacted to them), name it, and propose it before the cold search. If you don't know, ask that first: the answer changes every rate. Run the cold search first only if the user still wants it.

Max out a source before starting the next. No source closes behind you: if you remember a tribe while working signals, work it in parallel. A competitor's audience mixes their employees and vendors in with buyers: filter it hard.

---

## 2. People or Companies First

Search from the side where the fit is easiest to filter:

- **People first** when the role is the fit, and a title filter finds it: CHROs in LATAM, founders in Buenos Aires. Search the role directly, and judge each person's company after.
- **Companies first** when the fit is in the company and no title filter can see it: an industry, a size, a tech they use, a signal like a funding round. Build the company list, then find the people inside it.

**Reach one or two people per company, not ten.** Many messages into one company in a short time look like spam to filters, and colleagues who compare near-identical messages write you off. Pick the one or two whose job your problem affects and who can act on it.

---

## 3. Probe Small, Then Fill

**Never fill a list from a search you have not read.** The loop, every time:

1. **Run the search small:** 20 to 40 results. Don't save them yet.
2. **Judge every result** against the ICP, the way lead-search says: in or out, and the criterion that decided it.
3. **Count the fit.** "14 of 30 fit. The misses are recruiters and agencies."
4. **Name the fix** for the misses: an exclusion, a tighter title, a different source.
5. **Run small again** with the fix.
6. **Fill the list** only after the sample is clean and the user says yes.

If two or three rounds don't produce a clean sample, say the search is wrong. Never lower the bar to make the numbers look better.

### Which side is wrong

A low fit rate has two causes with opposite repairs:

- **The search is too wide.** The misses are companies the user never wanted (consultancies, resellers, media that share your keywords). The ICP is doing its job. **Fix the search** (see **[sales-navigator](../sales-navigator/SKILL.md)**).
- **The ICP is too tight.** The misses are companies the user *did* want, rejected on a fact nobody publishes. **Fix the ICP** (see **[icp](../icp/SKILL.md)**).

Read the misses before changing anything. Ask: would the user have wanted this company at all?

---

## 4. A Lookalike List: Split It

With no closer source left, search the ICP's roles at companies like the best customers, and nothing cleverer. Then **split the list** by country, industry or role, so you learn which segment responds. Because the list is a guess, the message carries an offer worth a yes to anyone in the segment, not a question about their pain: a question about their problem costs interest. See **[message-copies](../message-copies/SKILL.md)** for the offers that drew the most.

Real ones that work: [three of our clients' lookalike lists](references/example.md).

---

## 5. Beyond LinkedIn: The Open Web

Some of the best lists are not on LinkedIn:

- **Job posts.** The richest source. A company hiring its first RevOps lead just decided ops is a problem. The post names the team, the stack, the manager and often the pain. Many boards have public APIs (Ashby: `api.ashbyhq.com/posting-api/job-board/{slug}`; Greenhouse: `api.greenhouse.io/v1/boards/{slug}/jobs`).
- **Directories and registries.** Association members, licence registries, chamber of commerce lists, partner and "powered by" pages.
- **Marketplaces and app stores.** Who is listed as an integration, partner or certified implementer.
- **Events.** Speaker lists, exhibitor lists, sponsors. An exhibitor list is a qualified buyer list someone else paid to build.
- **Public technical traces.** GitHub issues, changelogs, forum threads where practitioners describe the problem in their own words.
- **Local press and funding news.** A raise, a new market, a new plant.

---

## 6. How Big

It depends on how sure you are of the market:

- **Validating a market** (the ICP is still being tested): about 200 to 300 people are enough to see if it works.
- **Sure of the market:** as big as you can. The limit is what the senders can send: one LinkedIn seat sends about 150 invitations a week.

---

## Related Skills

- **[lead-search](../lead-search/SKILL.md)**: count the market, judge each result, and the output table.
- **[sales-navigator](../sales-navigator/SKILL.md)**: how to write the search.
- **[initiatives](../initiatives/SKILL.md)**: the bet each list serves, and its source.
- **[small-market](../small-market/SKILL.md)**: when the market is a few hundred companies.
