# Sales Navigator

How to turn "who I want" into filters that find those people and nobody else.

## How filters combine

- Several values in the **same** filter are OR: industry "Financial Services" + "Banking" = either.
- **Different** filters are AND: industry AND location AND seniority.
- Every filter you add narrows. Add one intent at a time, and read the results each time.

## Titles

- **Use the current job title filter for any title.** It matches only the current title, not the whole profile. Keywords match everything on the profile, including jobs from ten years ago.
- **A title filter matches a set of words, not a phrase.** "Gerente de Recursos Humanos" also matches "Gerente de Planificación – Gcia. Corporativa de Recursos Humanos". Expect neighbours, and exclude the ones you don't want.
- **It matches across all current jobs.** If a result's shown title doesn't match, open the profile: they probably hold a second current job that does.
- **"Founder", "CEO" and "Owner" on a company list catch side projects.** Someone at the company who founded anything anywhere comes back. To find who runs the company, search "General Manager", "Managing Director", "Country Manager".
- **Past titles** ("used to be a CFO") go in the past job title filter.

## Leaders of a function

For "the people who lead X" (heads of growth, payment managers, whoever owns billing):

- Combine the **seniority** filter (Director, VP, CXO, Manager as needed) with **function words** in the title: "payments" OR "billing" OR "collections".
- Also add the matching C-title on its own: Marketing → CMO, Finance → CFO, Tech → CTO, HR → CHRO, Ops → COO, Product → CPO.
- In Spanish or Portuguese markets, add the local words too: "gerente", "jefe", "pagos", "cobranzas".

Exceptions: for founders or C-suite only, list those titles alone. For a specific non-leadership role ("data engineer"), list the title alone.

## Exclusions

Reach for an exclusion before another positive filter:

- **Title exclusions:** recruiter, talent, agency, assistant, intern, student.
- **Seniority exclusions:** entry level, training, unpaid.
- **Industry exclusions:** "Staffing and Recruiting" when the search fills with recruiters.
- **Company exclusions:** your competitors, your current customers.

Add obvious exclusions in the first search. Add the rest as soon as a wrong type keeps showing up.

## Locations

- **Regions don't resolve.** "LATAM", "Europe", "APAC" fail. Add one location per country. LATAM → Argentina, Brazil, Mexico, Colombia, Chile, Peru, Ecuador, Uruguay, Costa Rica, Panama.
- **Check what a place resolved to.** A name LinkedIn doesn't know often resolves to a place in another country. "CABA" resolves to Cabanatuan, Philippines.
- **Buenos Aires city has no LinkedIn location.** "Buenos Aires" is the province. Use full postal codes (`C1425ECB`, not `1425`), several across the city, with no radius.
- **Headquarters only.** The company location filter is the headquarters. For "companies with an office in Bogotá", search people located in Bogotá in functions every office has (HR, Admin), and keep their employers.

## Companies

- **"Startup" is not a filter.** Use headcount: 1–10, 11–50, 51–200.
- **Industry uses LinkedIn's own names:** "Financial Services", "Banking", "Software Development". A business model ("fintech", "SaaS", "marketplace") is a keyword.
- **A company with no LinkedIn page** can still be searched by the name people write as their employer. Don't add the country to the name ("Decathlon", not "Decathlon Argentina"). Pair it with a location and check each result.

## Keywords

Last resort: only for tools, skills or tech the user named ("Workday", "Kubernetes"), or a business model.

Keywords are a boolean query:
- Bare words are AND-ed: `fintech payments neobank` needs all three in one profile, and returns almost nothing.
- For alternatives: quote each term, uppercase OR, and wrap the group in parentheses: `("fintech" OR "payments" OR "neobank")`. Without the parentheses, an OR of 4+ terms is mis-read and returns about zero.
- Combine groups with AND / NOT.

## Reading the result count

- **Zero results:** drop the narrowest filter, widen a range, or add synonyms.
- **Too many, or a recurring wrong type:** add an exclusion.
- **Suspiciously large for a narrow ask:** probably nobody matched, and Sales Navigator dropped a filter and answered a wider question. Read the results before you trust the count.

## Pace

Run one search at a time on one account. Many searches at once on the same account look like abuse to LinkedIn and get it throttled.

## Worked examples

**Payment managers in LATAM**
```
Seniority: Manager, Director, VP
Current title: "pagos" OR "payments" OR "medios de pago" OR "billing" OR "cobranzas"
Location: Mexico, Brazil, Colombia, Argentina
```

**Marketing leaders in the US**
```
Current title: CMO, Chief Marketing Officer
  + Seniority: Director, VP with title words "marketing" OR "growth" OR "demand generation"
Location: United States
```

**CEOs and founders in Argentina**
```
Current title: CEO, Chief Executive Officer, Founder, Fundador, Fundadora, Co-founder
Location: Argentina
```

**Fintech companies in LATAM, 50–200 people** (company search)
```
Industry: Financial Services, Banking
Location: Mexico, Brazil, Colombia
Headcount: 51–200
Keywords: fintech
```
