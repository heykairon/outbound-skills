---
name: lead-search
description: Find and build a B2B lead list worth sending to, on LinkedIn and the open web, then check it against the ICP before filling it. Starts from an active initiative, then measures the market, because a small market needs a different strategy. Use when the user mentions "find leads," "build a list," "lead list," "prospect list," "who should I target," "find decision makers at," "find companies that," "my search returns the wrong people," "too many results," "zero results," or "target accounts." Count the market in the unit that matters, let the count pick the strategy, judge every result against the ICP (in or out, with the criterion that decided it), and give every fact its source. For a large market, see large-market. For a market of a few hundred companies, see small-market. For how to write a Sales Navigator search, see sales-navigator.
metadata:
  version: 0.6.0
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
- **A large market.** Enough people to replace the ones who don't answer. You don't need the whole list. Run different searches and test them: see **[large-market](../large-market/SKILL.md)**.
- **Both.** If only the biggest accounts look like a small market, work those with **[small-market](../small-market/SKILL.md)** and the rest with **[large-market](../large-market/SKILL.md)**.

---

## Judge Every Result Against the ICP

Whatever the source, read each result yourself before it goes on a list. Check it against the ICP in `.agents/icp.md`: title, company, location. Each one is **in or out**, and say which criterion or disqualifier decided it. Open the doubtful ones. Never let a result in because the search returned it.

Every column holds a fact a stranger could check, with its source: "Hiring 3 backend engineers in Madrid, per their careers page, March 2026". Not "yes" or "hot". A fact you could not verify stays empty.

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
- **[large-market](../large-market/SKILL.md)**: sources, probing and splitting, when the market is large.
- **[small-market](../small-market/SKILL.md)**: when the whole market is a few hundred companies.
- **[sales-navigator](../sales-navigator/SKILL.md)**: how to write the search.
- **[outbound-context](../outbound-context/SKILL.md)**: the voice, and where the other files are.
