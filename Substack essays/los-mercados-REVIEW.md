# Review: "Los mercados que nos negamos a tener"

Date: 2026-10-29. Review of Edgar's first draft (1,879 words, 72 paragraphs). **Applied 2026-10-29:** the essay file now holds the revised version (1,700 words, 26 paragraphs, 6 headers, 10 footnotes). The original draft is in git history (commit 058e20c). Items A–L and the fact fixes below were all applied; the OECD reference now supports the Korea figure.

## The style guide applied

The repo has no standalone style-guide file. The review uses the three sources that function as one:

1. `edgar_profile.md`, "Voice and Tone" section.
2. `Substack bot/content_generator.py`, the `_VOICE` block (casual but rigorous; ground every point in a concrete example or finding; never a think-piece opener; never "as an economist" framing; no slogans; let the example persuade).
3. The published posts on edgarcastrom.substack.com (read 2026-10-29), above all the Spanish essay "¿Quién puede detener a quién?" (22 May 2026), which is the closest published comparator in language, length and register: personal anchor at the top that returns at the bottom; real cases rather than hypotheticals; a thesis-stating subtitle; short paragraphs used sparingly; a crisp closing line with personal stake ("En diez días, mi país vota.").

Plus the working maxims in SESSION_NOTES: verify references twice, highlight epistemic risks, make assumptions explicit.

One correction to the bot-era rules: the `_VOICE` block says "no politicians by name", but the published essays name Petro, Cepeda, López Obrador, Uribe and Orbán freely when the argument is institutional. The operative rule in the essays is "no partisan framing", not "no names". This draft needs no names, so nothing changes here, but the review does not hold the draft to the bot rule.

## Calibration against the published Spanish essay

Measured on body text, excluding headers and references.

| Metric | "¿Quién puede detener a quién?" (published) | This draft |
|---|---|---|
| Words | 2,832 | 1,879 |
| Paragraphs | 49 | 72 |
| Words per paragraph | ~58 | ~26 |
| One-sentence paragraphs (≤90 chars) | 7 | 13 |
| "puede / pueden / podría / podrían" | 8 | 22 |
| Section headers | 4 | 8 |
| Opens with a personal scene | yes | no (section 2) |
| Closes on personal stake | yes | no |
| Citations | Substack footnotes (18) + inline links (15) | references list, URLs in parentheses |

The draft is a third shorter but has half again as many paragraphs, twice the one-liners, and nearly three times the hedging. Everything in Priority 2 below follows from that table. The published essay proves the author's Spanish voice can sustain 60-word paragraphs; the draft should be allowed to as well.

The short October post ("Empezar antes no es lo mismo que empezar bien", 311 words, a LinkedIn repost) does open with "Imaginemos a dos estudiantes". The hypothetical device is part of the voice for a 300-word note. At 1,900 words it is not what the long-form pieces do, so recommendation D stands.

## Verdict

The piece is in the right language (Spanish, Latin American topic), the right length, respectful, non-partisan, names no politicians, and acknowledges the objections honestly. Those boxes are ticked.

What it lacks, measured against the two reference essays, is a spine and an anchor. The title promises an essay about repugnant markets. The reader gets ten paragraphs of demography before Roth appears, a hypothetical couple instead of a real case, and a closing third that reads like the future-research section of a paper. The author's voice, which carries the reference essays, appears once ("Soy un pésimo agricultor") and never comes back.

## Priority 1: structure

**A. Cut the on-ramp in half.** Section 1 is 10 paragraphs and ~430 words before the actual subject. The reference essays reach their thesis in 4 to 5 paragraphs. Keep: Latin America at 1,8, Korea at 0,72, the "subsidies disappoint because children cost time and autonomy, not just money" observation, and the WHO/UNFPA unmet-demand point. Cut: the opening paragraph on "lo que significa vivir bien" (a generic think-piece opener, exactly what `_VOICE` forbids), and the "biología vs. aspiraciones" paragraph can be one sentence.

**B. State the thesis in the subtitle.** The reference subtitles are one bold sentence that says what the essay argues. "Sobre las cosas que más valoramos y las oportunidades que dejamos pasar" says what the essay is about, not what it claims. Candidates:

- *Prohibir un intercambio que nos incomoda también tiene un costo. Casi nunca lo pagan quienes lo prohíben.*
- *Por qué la pregunta no es solo qué intercambios nos repugnan, sino qué pasa cuando los impedimos.*

**C. Fix the demographic argument or drop it.** The essay sets up low fertility as a collective problem, then says surrogacy "está lejos de constituir una solución general al problema demográfico." If the aggregate effect is admittedly negligible, the demographic frame oversells. Two honest options:

- Reframe the hook around *unmet desired fertility* (the WHO and UNFPA numbers), which is about individuals facing a restriction, and drop the pensions/activity-economica paragraph. This is the stronger essay.
- Or keep the collective frame and own the implication: if births have positive externalities, the consistent position is to *subsidize* surrogacy, not merely permit it. The essay currently stops short of that and the reader will notice.

**D. Replace the hypothetical with a real case.** "Imaginemos una pareja..." is the one place the essay violates "ground every point in a concrete example." Options already within reach of the draft:

- Mexico, where the author lives: the Suprema Corte ruled in June 2021 that gestational surrogacy, paid or unpaid, is constitutionally protected, yet only Tabasco (since 1997) and Sinaloa (since 2013) regulate it and several states prohibit it. A couple in Monterrey and a couple in Villahermosa face different laws for the same act. That is the essay's argument in one country.
- Colombia: Corte Constitucional T-968/2009 recognised the practice; Congress has never legislated it.

**E. Merge "Lo que todavía no sabemos" into the ending.** Five consecutive hedged paragraphs ("No sabemos", "tampoco sabemos", "No tenemos buenas estimaciones", "necesitamos más investigación") deflate the essay just before the close. Keep two of the questions as a single paragraph. The honesty is right; the dose is not.

**F. Give the ending an anchor.** Both reference essays return to the opening scene. This one ends on abstraction ("deberíamos comprender mejor lo que estamos dejando de ganar"). Proposed close, returning to the farmer:

> Sigo siendo un pésimo agricultor. Nadie me prohíbe comprar mis alimentos a quien sabe producirlos. A las personas de las que habla este ensayo sí les prohibimos algo parecido, con razones que entiendo y con costos que casi nunca medimos. Antes de decidir qué mercados no queremos tener, deberíamos saber cuánto cuesta no tenerlos.

## Priority 2: voice and rhythm

**G. One-line paragraphs.** The draft has 13 (excluding subtitle and rule); the reference essay of similar length has 3. At that frequency the device stops landing. Delete these outright, they add nothing the previous sentence did not say:

- "No son preocupaciones menores."
- "Y esas consecuencias pueden ser enormes."
- "Regresemos al problema de la reproducción." (make it the first clause of the next paragraph)
- "Pero también hay algo que merece nuestra atención."
- "Es precisamente ahí donde necesitamos más investigación."
- "Distinguir entre ambas situaciones no es sencillo."

Keep "En este caso, hablamos potencialmente de vidas." and "Esta es, en esencia, la posibilidad que ofrece la gestación subrogada." Those earn their line.

**H. Rhetorical questions.** Three sections end on one. Keep one (the "¿Estamos seguros de que esa es la mejor forma de protegerlas?" is the best). Convert the other two to statements.

**I. Hedging density.** "puede/pueden/podría/podrían" appears 22 times and "necesariamente" 3 times in 1,900 words. The reference essays hedge at the level of the claim, not the sentence. Pass through and keep the hedge only where the claim is genuinely uncertain (the Becker-Elías estimate, the LATAM welfare gains). Sentences like "Pero pagar por un servicio no significa necesariamente que aquello que valoramos se reduzca a su precio" are stronger as "Pagar por un servicio no reduce a su precio lo que valoramos."

**J. The comparative-advantage mini-lecture.** Paragraphs 3 to 5 of section 2 ("Parece una observación trivial, pero hay algo extraordinario detrás...") are textbook. The farmer joke does the work alone; cut to the joke plus one sentence and go straight to "Pero hay situaciones en las que esta posibilidad desaparece."

**K. Repeated title.** The last section header repeats the essay title. Fine as a device, but then the section mostly restates earlier paragraphs. If F is adopted, the section can be cut to three paragraphs.

**L. Acronyms.** Expand on first use for a Spanish-speaking general reader: CEPAL (fine, well known), UNFPA ("el Fondo de Población de las Naciones Unidas (UNFPA)"), CDC ("los Centros para el Control y la Prevención de Enfermedades de Estados Unidos (CDC)").

## Priority 3: facts and references (verified 2026-10-29)

| Claim in draft | Status | Action |
|---|---|---|
| CEPAL, 1,8 hijos por mujer en 2024 | Confirmed (Observatorio Demográfico 2025, press release 29 Oct 2025). Below replacement since 2015. | Keep. Optionally add "por debajo del reemplazo desde 2015". |
| Corea del Sur, 0,72 en 2023 | Confirmed. | Keep. |
| OMS, una de cada seis personas | Confirmed (lifetime prevalence 17,5 %, April 2023). | Keep. |
| UNFPA 2025, "cerca de una quinta parte" | Confirmed: ~18 % of reproductive-age adults in a 14-country, ~14,000-person YouGov poll. | Add scope: "en 14 países". |
| Elías, Lacetera y Macis 2015: 52 % → **71 %** | **Wrong number.** The NBER/AER abstract reports 52 % → **72 %**. | Fix to 72 %. Consider also citing their full paper, Elías, Lacetera & Macis (2019), "Paying for Kidneys? A Randomized Survey and Choice Experiment", *AER* 109(8): the 2015 piece is a 5-page Papers & Proceedings note. Worth a clause: Julio Elías is Argentine (UCEMA), a LATAM link the audience will like. |
| Becker y Elías 2007: ~12 % cost increase | Confirmed in secondary sources (UCEMA summary). The estimate is for **kidneys in the US**, not "órganos" in general. | Write "trasplantes de riñón en Estados Unidos". Roth and Becker-Elías appeared in the same JEP symposium (21(3), 2007); a nice detail if wanted. |
| CDC: ~3.500 ciclos en 2013 → **9.700 en 2022** | **Not confirmed.** CDC embryo-transfer cycles with a gestational carrier: 3,432 (2013); 3,202 (2012) → 8,862 (2021), peak 9,195 (2019). SART clinic totals: 3,530 (2013) → 9,225 (2022). No source found for 9,700. | Use "de unos 3.400 en 2013 a unos 8.900 en 2021, según los CDC" or switch to SART and cite SART. Do not attribute 9,700 to the CDC. |
| LATAM regulation sentence | Broadly right. Mexico: Tabasco and Sinaloa regulate; some states prohibit; SCJN 2021 ruling. Uruguay: Ley 19.167 (2013), altruistic, relatives only, medical indication. Brazil: CFM resolution, altruistic, relatives. Colombia, Argentina: no statute, courts fill the gap. | Keep, but see D above: Mexico deserves a concrete sentence. |
| OCDE (2024) *Society at a Glance 2024* | Listed in references, **never cited in the text**. | Cite it (it carries OECD fertility at ~1,5) or remove it. |

## Priority 4: Substack mechanics

- URLs in parentheses after titles will not render as links when pasted into Substack. The published May essay settled this: it uses native Substack footnotes plus inline links on names and institutions, and has no references list. Do the same here: link "Alvin Roth", "Elías, Lacetera y Macis", "Becker y Elías", "CEPAL", "OMS", "UNFPA" and "CDC" inline, move the bibliographic detail into Substack footnotes, and delete the "Referencias" block.
- Reference list is in no order (OCDE, Roth, UNFPA, OMS, CDC). Alphabetise, and give CDC a year.
- Use the thin space or non-breaking space before "%" consistently ("52 %" is RAE style and is used throughout; good).

## What not to change

- The Roth section is the best-written part of the draft. The usury example, the "quienes más sienten esas consecuencias no siempre son quienes defienden las prohibiciones" line, and the medical/teacher/caregiver payment analogy all land.
- The honest acknowledgment of exploitation risk is in keeping with "acknowledge market failures honestly". Keep it; just do not repeat it four times.
- Spanish is the right call per the language rule.
