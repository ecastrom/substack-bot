# SESSION_NOTES.md — Substack essays

**Last update:** 2026-05-15 (full structural rewrite around the separation-of-powers thesis)

## Project state

- **Active work:** drafting and reviewing Substack essays.
- **Substack-bot codebase:** ABANDONED.
- **Drafts location:** `Substack essays/`
- **Two essays exist:**
  - `my-favorite-coworker-complains-a-lot.md` — published; reference voice.
  - `who-can-stop-whom.md` — current essay. Full rewrite 2026-05-15.
- **Cross-conversation memory:** `~/.claude/projects/C--Users-L03574200-Documents-GitHub-substack-bot/memory/`

---

## Current essay: "Who can stop whom?"

- **Title:** Who can stop whom?
- **Subtitle:** *Why the stupidest moment to weaken separation of powers is when you like the president.* *(updated to make the topic explicit and align with the central thesis)*
- **Filename:** `who-can-stop-whom.md`
- **Length:** approximately 2,900 words.
- **Status:** Full structural rewrite delivered 2026-05-15. Awaiting Edgar's review and fact-verification.

---

## Structure of the rewrite (the spine)

The central thesis is now load-bearing throughout: **separation of powers is the architecture that makes power fight power; it is the loser's protection against a winning majority, and the worst time to weaken it is precisely when you like the people in power.**

Sections in order:

1. **Open — Peruvian lunch (personal anchor).** Establishes the cast and the February 2026 impeachment-as-theater story. Closes with the framing question: *who can stop whom?*
2. **The loser's power.** Scalia on rights-on-paper; the most-important-democratic-institution-is-the-loser's-power thesis; the five "Congress / Courts / Central banks / Local governments / Opposition" beats; explicit introduction of Scalia's *"love the gridlock"* as a load-bearing image.
3. **Today's shortcut, tomorrow's environment.** Generational frame (Edgar at 36, Great Moderation, Colombia without hyperinflation); Levitsky-Ziblatt attribution for the 21st-century-democracies-die-slowly thesis; the four "if firms / judges / legislators / citizens learn..." beats; closes with *"the stupidest moment to weaken constraints is when you like the president."*
4. **Mexico — when no one can be stopped.** Edgar's regression-to-the-mean historical sweep (71 yrs PRI, revolution, Porfiriato, unstable republic, two wars, two failed monarchies); the old PRI logic; Morena as resurrected PRI in redistributive costume.
5. **American exceptionalism, shattered.** Acknowledges American institutional strengths, then the concrete post-Jan-2025 deterioration list (pardons, IEEPA tariffs, Fed pressure, DOJ, judges). Constitutional opportunism. *Separation of letterhead.*
6. **Peru, again — the case for dysfunction.** The original hostage-taking / demolition-crew framing, then Edgar's reframe: maybe Peru's gridlock is doing useful selective work after all. Scalia's *love the gridlock* paid off. Bridge to Mexico via the "too much power vs. too little stability" couplet.
7. **Colombia — more complicated than it looks.** Edgar's clientelism / *gobernabilidad* / Robinson paragraph; the BanRep / 1991-constitution paragraph; Petro's reaction; Cepeda + the constituent assembly with El País and La Silla Vacía sources.
8. **Hope, but not cheap hope.** Hungary April 2026 as counterexample; *losing possible* as the key phrase.
9. **The architecture that makes power fight power.** Closes with the love-separation-of-powers-in-the-moments-it-frustrates-you move, the warning against confusing victory with ownership, Scalia's uncomfortable point, the return to the Peruvian lunch, and the final closer: *"Rights on paper are easy. The hard part is keeping someone strong enough to say no, and honest about when to say it."*

---

## Material from prior drafts that was kept verbatim (or near-verbatim)

- The Peruvian-lunch opener
- The five-things-must-still-matter list (loser's power)
- The four if-X-learn beats (firms, judges, legislators, citizens)
- "Today's shortcut becomes tomorrow's institutional environment."
- "Everyone learns where power lives. Everyone adapts."
- "The stupidest moment to weaken constraints is when you like the president."
- The Mexico section's PRI body paragraphs and the "burying neoliberalism / resurrecting the PRI" closer
- "Constitutional opportunism." / "Separation of letterhead."
- The Peru-too-much-power-vs.-too-little-stability paragraph
- The Hungary paragraph
- "Losing possible. That is the key phrase."
- The closing return to the lunch + "Rights on paper are easy. The hard part is keeping someone strong enough to say no..."

## Material from prior drafts that was cut or compressed

- The mid-essay standalone "In Peru, no one can govern" paragraph (the new Peru-thesis paragraph at the opening, plus the integrated Peru-again reframe, do its work better)
- The mid-essay standalone "Who can stop whom?" body line — the question is now framed in the opener and answered through the rest of the essay
- The "balanced harmony" addendum to the Scalia paragraph (textbook-sounding; the meaning is carried by *love the gridlock* and the architecture closer)
- The mid-paragraph aside about Petro splitting (typographical artifact)

## Material that I added

- The thesis sentence in the opener: *"the most important question in a democracy is not who wins? but who can stop whom?"* — to make the central question explicit and connect title to body.
- The "frustration is the point" beat in §2 — to set up *love the gridlock* before Peru's reframe pays it off.
- A few transitional sentences between sections to keep the spine visible.

---

## Things flagged for Edgar (decisions / verifications pending)

1. **Subtitle.** I changed it to *"Why the stupidest moment to weaken separation of powers is when you like the president."* The change makes the topic explicit and ties to the title's question. If you prefer your original *"Why the stupidest moment to weaken constraints is when you like the president,"* revert — both work.

2. **Facts to verify before publication (Maxim 5):**
   - Levitsky-Ziblatt attribution as written. (*How Democracies Die*, 2018, Crown — verified accurate)
   - Mexican history sweep (compressed; defensible but worth a sanity check).
   - U.S. events paragraph — each item is publicly reported (Jan 6 pardons Jan 2025, IEEPA tariffs early 2025, Powell/Fed pressure 2025, DOJ political prosecutions, judicial attacks). Read it once against current news.
   - Robinson clientelism cite — `[^robinson-note]` is a placeholder; needs a specific work or interview.
   - Hungary opposition win April 2026.
   - Peru elections April 12-13 2026.

3. **Mexico previous-entry link.** The `[my previous entry](#)` is a placeholder — fill once you have the prior post URL.

4. **Footnote rendering on Substack.** Pandoc `[^name]` footnotes will not render natively in Substack paste. Two options: (a) inline the citations as `([El País](URL))` and remove the `## Sources` block, or (b) keep `## Sources` and re-create the footnotes using Substack's footnote tool in the GUI after pasting. Decision needed before publication.

5. **The Peru-reframe tension.** The section now holds two readings in productive tension: "Peru is dysfunctional" + "but the dysfunction might be doing useful selective work." This is by design — per `essay_voice_notes.md` this is one of your signature moves (contrarian-economist reframe). Read it once and decide whether the two readings strengthen or undercut each other in your voice.

6. **Length.** ~2,900 words. Longer than the reference essay (~1,800) but tighter than the previous version of this one (~3,400). The four country cases plus the generational frame justify the length — but if you want a tightening pass to bring it closer to 2,400, I can do that.

---

## Working Maxims (NON-NEGOTIABLE — copied from global CLAUDE.md)

1. Do not touch raw source data. Worked products are NOT raw data; no backup copies.
2. Do not force results.
3. Academic honesty is a categorical imperative.
4. Highlight epistemic risks.
5. Verify all references twice.
6. Make assumptions explicit.
7. Protect user data wisely — proportionate.
8. Respect user edits. Read before overwrite. No `.bak`/`-old`/`_backup`.
9. Read before overwrite; do not hoard versions.
10. Test after writing.
