---
name: sales-navigator
description: Turn an ICP into LinkedIn Sales Navigator searches that find those people and nobody else, and read the results before trusting them. Use when the user mentions "Sales Navigator," "Sales Nav," "Sales Nav filters," "LinkedIn search," "boolean search," "my search returns the wrong people," "too many results," "zero results," "recruiters keep showing up," "search by postal code," "search my connections," or "find people who follow a profile." Test the search on the user's own customers first, put each filter on the side where the fit lives (the person or the company), search titles as people write them, combine seniority with function words for leaders, exclude before you add, check what every filter resolved to, and treat a suspiciously large count as nobody matching. Run one search at a time. For which source to search and how to judge the results, see lead-search.
metadata:
  version: 0.3.1
---

# Sales Navigator

Your goal is a search that returns the people in `.agents/icp.md` and nobody else. Sales Navigator rarely says when it misunderstood you. It drops a filter, guesses a place, or matches a word somewhere you did not mean. So every search is a guess until you read what came back.

## Before Starting

**Requires [lead-search](../lead-search/SKILL.md).** Read that skill's Before Starting first, and read the files it names. If the file that skill owns does not exist yet, do that skill first. This skill does not repeat any of it.

Which source to search, and how to judge each result against the ICP, is in lead-search. This skill is only how to write the search.

---

## 1. From the ICP to Filters

**Put each filter on the side where the fit lives.** Some criteria are about the company (industry, headcount, headquarters). Some are about the person (role, where they live, where they worked). Put each one on its own side. Example: "founders in Buenos Aires" is about the person. Their companies often list a headquarters in the US or Spain. A company filter on Argentina loses them. A person filter on the city finds them.

**Search titles the way people write them.** Not the way the ICP names the role. In Buenos Aires, most founders write "Founder" and "CEO" in English. A search for "Fundador" or "Gerente General" finds a small part of them. When unsure, open ten profiles of the people you want, and copy their words.

**Test the search on the user's customers.** Before you look at strangers, check that the search finds the best customers in `.agents/icp.md`. If one of them is missing, one filter is wrong: find which one, and fix it. A search that loses your own customers loses strangers like them too.

---

## 2. How Filters Combine

- Several values in the **same** filter are OR: industry "Financial Services" + "Banking" = either one.
- **Different** filters are AND: industry AND location AND seniority.
- Every filter you add narrows the search. Add one intent at a time, and read the results each time.

---

## 3. Titles

- **Use the current job title filter for any title.** It matches only the current title. Keywords match the whole profile, so they find people who did the job ten years ago.
- **A title filter matches a set of words, not a phrase.** "Gerente de Recursos Humanos" also matches "Gerente de Planificación – Gcia. Corporativa de Recursos Humanos". Expect neighbours, and exclude the ones you don't want.
- **It matches across all current jobs.** If a result's shown title doesn't match, open the profile. They probably hold a second current job that does.
- **"Founder", "CEO" and "Owner" on a company list catch side projects.** Anyone at the company who founded anything anywhere comes back. To find who runs the company, search "General Manager", "Managing Director" or "Country Manager".
- **Past titles** ("used to be a CFO") go in the past job title filter.

### Leaders of a function

For "the people who lead X" (heads of growth, payment managers, whoever owns billing), this is the default:

- Combine the **seniority** filter (Manager, Director, VP, CXO, as needed) with **function words** in the title: "payments" OR "billing" OR "collections". A hand-written list of titles misses the variants people really use.
- Add the matching C-title on its own: Marketing → CMO, Finance → CFO, Tech → CTO, HR → CHRO, Ops → COO, Product → CPO.
- In Spanish or Portuguese markets, add the local words too: "gerente", "jefe", "pagos", "cobranzas".

Three exceptions. Founders or C-suite only: list those titles alone. A specific role that is not a leader ("data engineer"): list the title alone. A pure level ("all directors"): use seniority alone.

---

## 4. Exclude Before You Add

When a wrong type keeps coming back, exclude it. Don't add another positive filter.

- **Titles:** recruiter, talent, agency, assistant, intern, student.
- **Seniority:** entry level, training, unpaid.
- **Industry:** "Staffing and Recruiting", when recruiters fill the search.
- **Companies:** your competitors, your current customers.

Put the obvious exclusions in the first search. Add the rest as soon as a wrong type shows up twice.

---

## 5. Locations

- **Regions don't work.** "LATAM", "Europe" and "APAC" fail. Add one location per country. LATAM → Argentina, Brazil, Mexico, Colombia, Chile, Peru, Ecuador, Uruguay, Costa Rica, Panama.
- **Buenos Aires city has no LinkedIn location.** "Buenos Aires" is the province, and "CABA" resolves to Cabanatuan, in the Philippines. Use full postal codes (`C1425ECB`, not `1425`), many of them across the city, with no radius. A code that starts with C is the city. B is the province. The location a result shows can differ from the code that matched, so check a few.
- **The company location filter is the headquarters only.** For "companies with an office in Bogotá", search people who live in Bogotá in jobs every office has (HR, admin), and keep their employers.

---

## 6. Companies

- **"Startup" is not a filter.** Use headcount: 1–10, 11–50, 51–200.
- **Industry uses LinkedIn's own names:** "Financial Services", "Banking", "Software Development". A business model ("fintech", "SaaS", "marketplace") is a keyword.
- **A company with no LinkedIn page** can still be found by the name people write as their employer. Don't add the country ("Decathlon", not "Decathlon Argentina"). Pair it with a location, and check each result.

---

## 7. Keywords, Last

Use keywords only for tools, skills or tech the user named ("Workday", "Kubernetes"), or for a business model. Keywords are a boolean query:

- Bare words are AND-ed: `fintech payments neobank` needs all three in one profile, and returns almost nothing.
- For alternatives, quote each term, write OR in capitals, and put the group in parentheses: `("fintech" OR "payments" OR "neobank")`. Without the parentheses, an OR of four or more terms is misread and returns almost zero.
- Combine groups with AND and NOT.

---

## 8. Filters That Use Your Own Network

Some filters depend on whose account runs the search. They find the warm people, so use them before cold filters:

- **Connection degree:** 1st, 2nd or 3rd degree, from the account that searches. Prefer 2nd degree: a 3rd-degree contact accepted 6% of invitations, and each mutual connection adds more ([benchmarks](../initiatives/references/benchmarks.md)).
- **Connections of:** the connections of one person, for example a customer or an investor who can introduce you.
- **Past colleague**, and the same school or past company as the sender.
- **Shared experiences:** groups and experiences in common.

Two more filters raise acceptance: **posted on LinkedIn in the past 30 days** (about 12 points more) and **changed jobs in the past 90 days** (about 10 points more).

These answer for the account that runs the search. Run them from the sender's own account, or they find the network of someone else.

**Classic LinkedIn search, not Sales Navigator,** is the tool for three jobs: searching your 1st degree when you don't have Sales Navigator, listing the followers of a profile, and finding people who are hiring for a role.

---

## 9. Read the Result Before You Trust It

- **Check what every filter resolved to.** A place, a company or an industry can resolve to something you did not mean, and the search still runs.
- **Zero results:** drop the narrowest filter, widen a range, or add synonyms.
- **Too many results, or one wrong type again and again:** add an exclusion.
- **A count too large for a narrow ask** usually means nobody matched. Sales Navigator dropped a filter and answered a wider question. Open the first results before you trust the number.

**One search at a time** on one account. Many searches at once on the same account look like abuse to LinkedIn, and it slows the account down.

---

## Worked Examples

Real ones, with how many people passed the ICP and accepted: [six of our clients' searches](references/example.md).

**Payment managers in LATAM**
```
Seniority: Manager, Director, VP
Current title: "pagos" OR "payments" OR "medios de pago" OR "billing" OR "cobranzas"
Location: Mexico, Brazil, Colombia, Argentina
Exclude titles: recruiter, talent, intern
```

**Marketing leaders in the US**
```
Current title: CMO, Chief Marketing Officer
  + Seniority: Director, VP, with title words "marketing" OR "growth" OR "demand generation"
Location: United States
```

**Founders and CEOs in Argentina** (the fit lives in the person)
```
Current title: Founder, Co-founder, CEO, Chief Executive Officer, Fundador, Fundadora
Person location: Argentina (not the company's headquarters)
```

**Functional analysts in Buenos Aires city**
```
Current title: "analista funcional" OR "functional analyst"
Location: 33 full postal codes across the city (C1425ECB, ...), no radius
```
This found 35 people. The same search on Greater Buenos Aires found 62: the other 27 live outside the city.

**Fintech companies in LATAM, 50–200 people** (company search)
```
Industry: Financial Services, Banking
Location: Mexico, Brazil, Colombia
Headcount: 51–200
Keywords: ("fintech" OR "payments" OR "neobank")
```

---

## Related Skills

- **[lead-search](../lead-search/SKILL.md)**: which source to search, the probe of 20 to 40 results, and how to judge each one.
- **[icp](../icp/SKILL.md)**: who the search is for, and the customers to test it on.
