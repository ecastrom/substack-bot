# SESSION_NOTES.md — Substack essays

**Last update:** 2026-05-07 (session paused mid-revision; user resuming from home)

## Project state

- **Active work:** drafting and reviewing Substack essays.
- **Substack-bot codebase:** ABANDONED. Do not propose work on it.
- **Drafts location:** `Substack essays/`
- **Two essays exist:**
  - `my-favorite-coworker-complains-a-lot.md` — published; user happy with it. This is the reference voice.
  - `who-can-stop-whom.md` — current draft, retitled "The Loser's Power" (filename unchanged).
- **Cross-conversation memory** (style/preferences) lives at `~/.claude/projects/C--Users-L03574200-Documents-GitHub-substack-bot/memory/` — see `essay_voice_notes.md` and `project_substack_essays.md` there.

---

## Current essay: "The Loser's Power"

- **Title:** The Loser's Power
- **Subtitle:** *Why the stupidest moment to weaken constraints is when you like the president.*
- **Filename:** still `who-can-stop-whom.md` (rename to `the-losers-power.md` not yet decided)
- **Word count:** ~2,600
- **Status:** mid-revision. One polish edit applied this session (boss/colleague clarification on line 5). **Six edits queued but NOT applied.**

### Decisions made this session

- Personal anchor: Peruvian-lunch opener, paralleling the lunch-table move from the complaining essay; anchored further with biographical detail (Cesar Martinelli as PhD advisor; boss/RA Peruvian).
- Personal anchor is *not* a permanent requirement — see `essay_voice_notes.md` for alternative imprint moves (contrarian-economist reframe, named-concept move, structural surprise, etc.).
- Title chosen: "The Loser's Power" with "stupidest moment" subtitle, fusing two ideas the user wanted to combine.
- Transition accepted: *"In Peru, no one can govern. In most of the region, no one can be stopped."*
- Economists section needs full rewrite for three reasons:
  1. Should matter to everyone, not only economists.
  2. Latin American economists lean right by local standards — the "we suddenly turn romantic" framing was US-centric.
  3. Economists are MORE aware of institutional fragility than most other social scientists, not less. The current framing condescends to a profession that actually knows the argument well.

---

## Pending edits (NOT yet applied — apply on resume)

### Edit A — Line 11, Colombia paragraph: grammar polish

**Issues:** "in 24%" (should be "by"); "a a new" typo; "expanding the expenditure by taking expensive debt" (awkward English); whole sentence runs on with embedded clauses that lose the verb.

**Replace:**
> I wanted to write the essay then. Instead, I went back to a field experiment I am working on, because papers have a way of disciplining your moral urgency. What brought the idea back was Colombia: an incoming presidential election, an incumbent president, Gustavo Petro, who is enjoying a spree of popularity after increasing the minimum wage in 24% and expanding the expenditure by taking expensive debt, is openly promoting a a new Constitution via an assembly (Asamblea Constituyente), and a chosen successor, Ivan Cepeda, who may speak more softly but has not clearly broken with the project.

**With:**
> I wanted to write the essay then. Instead, I went back to a field experiment I am working on, because papers have a way of disciplining your moral urgency. What brought the idea back was Colombia. The incumbent president, Gustavo Petro, is riding a wave of popularity after raising the minimum wage by 24% and expanding spending through expensive debt, and is openly promoting a new constitution through a constituent assembly (Asamblea Constituyente). His chosen successor, Ivan Cepeda, may speak more softly but has not clearly broken with the project. A presidential election is approaching.

### Edit B — Line 17, video URL: integrate as inline link

**Issue:** Standalone line `Worth watching video https://x.com/i/status/2025152903921475665` is a placeholder note, breaks reading flow.

**Best guess:** the video shows Scalia making the rights-on-paper argument. **CONFIRM before applying.** If correct, integrate as an inline link on the Scalia sentence:

**Replace** the Scalia opening sentence and the standalone URL line with:
> Antonin Scalia [once made a point](https://x.com/i/status/2025152903921475665) that has aged disturbingly well. Americans, he said, often think their freedoms come from the Bill of Rights. ...

(Remove the standalone "Worth watching video..." line entirely.)

### Edit C — Line 27, Colombian aside: own paragraph + clarify "the president"

**Replace:**
> People say they love democracy. Many only love winning elections. The real test is whether they love the institutions that sometimes make their side lose. And this will be especially important for my fellow Colombians who like the president.

**With (split into two paragraphs):**
> People say they love democracy. Many only love winning elections. The real test is whether they love the institutions that sometimes make their side lose.
>
> This will matter especially for my fellow Colombians who like the current president.

### Edit D — Lines 29–41, economists section: full replacement (THE BIG ONE)

**Section title change:** `## What economists should already know` → `## Today's shortcut, tomorrow's environment`

**Replace the entire section body with:**

```markdown
## Today's shortcut, tomorrow's environment

This is the part that should make everyone uncomfortable, not only economists.

Economists actually know the argument well: time inconsistency, credibility, dynamic effects, the difference between today's policy and tomorrow's equilibrium. In Latin America it is not even academic. It is biographical. We grew up watching capital flight, hyperinflation, populist blowups, and the slow rebuilding of credibility that someone in our family already paid for. If anything, economists tend to be more aware of institutional fragility than most other social scientists.

The trouble is that knowing better is not the same as doing better. When the leader we like is in power, constraints start to look like obstacles. If the reform is good, why let courts delay it? If the people voted for change, why should a central bank, a judge, or an opposition governor stand in the way? The temptation does not respect ideology or geography. Latin American economists, who lean right by local standards, feel it when a market reformer arrives. Heterodox economists feel it when a redistributive coalition takes office. American economists, who lean Democratic these days, feel it when their team wins. Everyone, eventually, finds a leader good enough that the rules look optional.

But politics is not a one-shot game. Today's institutional shortcut becomes tomorrow's institutional environment.

If firms learn that investment depends on political loyalty, they stop competing on productivity and start competing on access. If judges learn that promotion depends on pleasing the ruling movement, legal reasoning becomes career management. If legislators learn that their future depends on obedience to the president, Congress becomes expensive decoration. If citizens learn that losing an election means losing protection, politics becomes existential.

Everyone learns where power lives. Everyone adapts. That is how a country changes equilibrium - not always with a coup, often with applause, public consultations, and the slow conversion of independent institutions into offices of the ruling movement.

The stupidest moment to weaken constraints is when you like the president. That is also when people most want to do it. Separation of powers is not built for moments when everyone is calm and the president is modest. It is built for the moment when a popular leader says: the people are with me, therefore the institutions should move out of the way.
```

### Edit E — Line 105, El País paragraph polish

**Replace:**
> Ivan Cepeda, the candidate of continuity inside Petro's political world, has tried to present a softer version: national agreement, dialogue, political reform. The ambiguity is doing a lot of work. El Pais described it well: Cepeda has tried to distance himself only halfway from the constituent assembly that Petro keeps agitating. The final agreement with the Greens mentioned the idea only lightly, without Cepeda explicitly closing the door to it, while people collected signatures for the constituent assembly around his campaign event.[^colombia-elpais]

**With:**
> Ivan Cepeda, the candidate of continuity inside Petro's political world, has tried to present a softer version: national agreement, dialogue, political reform. The ambiguity is doing a lot of work. El Pais put it well: Cepeda has only half-distanced himself from the constituent assembly Petro keeps pushing. The final agreement with the Greens (Alianza Verde) mentioned the idea only in passing, without Cepeda explicitly closing the door to it, while volunteers collected signatures for the constituent assembly at his campaign events.[^colombia-elpais]

### Edit F — Line 107, La Silla Vacía paragraph polish

**Replace:**
> Around him, the current government is already pushing constitutional change. La Silla Vacia has described Petro's constituent project as a way to keep doing politics beyond 2026, and has emphasized the political function of the proposal: mobilization, pressure, and the attempt to move the center of gravity from Congress and the courts to a more direct appeal to "the people."[^colombia-silla] The successor can say "dialogue" while the president's office builds the machine.

**With:**
> Meanwhile the current government is already pushing constitutional change. La Silla Vacia has described Petro's constituent project as a way to keep doing politics beyond 2026, stressing its political function: mobilization, pressure, and the attempt to shift the center of gravity from Congress and the courts to a more direct appeal to "the people."[^colombia-silla] The successor can say "dialogue" while the president's office builds the machine.

---

## Open items for next session

- Apply edits A–F above (or have Claude apply them after you confirm).
- Decide filename: keep `who-can-stop-whom.md` or rename to `the-losers-power.md`.
- **Verify factual claims before publication (Maxim 5):**
  - Hungary opposition won in April 2026? (line 121)
  - Peru general elections held April 12 and 13, 2026? (line 87)
  - Cesar Martinelli correctly identified as PhD advisor and Peruvian? (line 5)
- Confirm the video URL on line 17 is Scalia making the rights-on-paper argument (so the inline-link placement reads correctly). If it's a different clip, move the link to wherever it belongs.

---

## Working Maxims (NON-NEGOTIABLE — copied from global CLAUDE.md)

1. Do not touch raw source data. Worked products (essays, scripts, papers) are NOT raw data and do not need backup copies.
2. Do not force results. Push back respectfully if asked.
3. Academic honesty is a categorical imperative.
4. Highlight epistemic risks.
5. Verify all references twice. BibTeX + DOI for citations; flag UNVERIFIED rather than guess.
6. Make assumptions explicit; ask before proceeding on uncertain ground.
7. Protect user data wisely — proportionate, not paranoid.
8. Respect user edits. Read before overwrite. No `.bak`, no `-old`, no `_backup`.
9. Read before overwrite, but do not hoard versions.
10. Test after writing.
