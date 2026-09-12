# Day 1 — Teaching Run-of-Show (9:00–12:00)

**Instructor use only.** Not served by GitHub Pages. `.instructor/agenda.md` has the section
table and the measured times behind it; this is how to run it.

**Two cycles of short lecture → long self-paced work block**, the same shape as Day 2.
**40 min lecture · 140 min work block = 180.** No whole-room breaks — tables break when
they reach a natural stopping point.

Before anything else: **`prereq-triage.md`**. You have five minutes at 9:00 to find who
will be stuck, and the order you check matters.

---

## The shape of the day

| Clock | Block | min | Mode |
|-------|-------|-----|------|
| 9:00 | **Lecture 1** — the two-day map, the Yens, and why version control | 20 | talk |
| 9:20 | **Work block 1** — Part 1, ending in the Part 1 Checkpoint | 70 | self-paced, circulate |
| 10:30 | **Lecture 2** — Python on the Yens, then Stanford's AI services and data privacy | 20 | talk + demo + discussion |
| 10:50 | **Work block 2** — Part 2, ending in the extraction → capstone arc | 70 | self-paced, circulate |

Per-section budgets inside each block are in `.instructor/agenda.md`. **Protected:** Claude
Code (25) in block 1 and the extraction-to-capstone arc (35) in block 2.

## How to run it

- **The lecture is the only part you drive.** Inside the work block you circulate rather
  than lead — participants sit at small tables and help each other.
- **Bonus sections are the buffer.** Point fast finishers at them rather than slowing the room.
- **The pre-work is doing real work.** Day 1 opens at SSH, not at `ls`. If several people
  clearly skipped it, do **not** re-teach the CLI — that costs the whole room the hour the
  pre-work bought. Pair them up and keep moving.

## Section notes, from what actually happened last time

| Section | What the clock showed | What to do |
|---|---|---|
| **Connecting to the Yens** (15) | Ran 25 in the four-day course (14 + 11 across two pages) | Most of that was first-time-login friction, and **this year it is genuinely first login** — there is no pre-work check to absorb it. Budget 15 but expect 20–25, and take it out of the JupyterHub tour. Get Duo enrolment sorted before anything else |
| **Git & GitHub** (13) | Ran **20**, and "Actions failed for some" | Both causes are gone: the Actions/Pages clicks were removed from the fork steps, and token creation is now pre-work. It is `gh auth login` → paste → branch → commit → push. If it runs long, the token is why — check who's missing one at 9:00, not 9:20 |
| **Claude Code** (25) | Ran ~30 and then **spilled ~60 min into Day 2** | **Protected.** Concepts are now a pre-read, so this is 25 min of pure keyboard: `ml claude-code`, sign in, `/cost`, `Shift+Tab` through the modes, one real task on `aws_links.csv`, install `github-for-research`. Skip the sf311 practice unless you're ahead |
| **Running Python** (14) | Ran **25–35**, flagged too slow | JupyterHub is a **tour**: open it, show a cell running on Yens hardware, move on. The `$PATH` demo is the actual content. Cut the notebook-editing bit first |
| **Python environments** (18) | Ran 20, "could be streamlined" | **Demo** the Potion Brawl rebuild rather than having 20 people pip-install a heavy tree. They still see reproducibility land; you save 8 minutes and a dozen support questions |
| **Stanford's AI services** (14) | Ran only **10** | You have time here — this is where the privacy discussion now lives. The data-risk table is the one thing everyone must leave with |
| **API keys** (13) | Ran **20** | Pre-stage the shared `.env` somewhere they can `cp` it, rather than typing a key. Keep "a committed key is a leaked key" |
| **Extraction → capstone** (35) | Extraction ran 25 **and didn't finish**; capstones ran 60+ whenever run | **Protected, and one continuous arc.** Walk `diff scripts/extract_form_3_step2_logged.py scripts/extract_form_3_one_file.py` on screen — the diff *is* the Pydantic lesson. Then introduce the Genre Tribunal: ten movies, Haiku classification, Sonnet judging, and a Python review rule. Participants build the script and finish outside class if needed |

## If you are behind at 11:10

In order:

1. Trim the extraction walkthrough to the `diff` plus one live call, and let the capstone's
   two-model movie exercise carry the rest.
2. Review one movie disagreement aloud instead of extending the capstone discussion.
3. Let the capstone run out of the room — participants carry on with it in their own time.

**Do not** cut the Pydantic validation step — it is the payoff of the whole arc. (Day 2 no
longer depends on it: it profiles the `extract_form_3_batch.py` committed in the repo, so an
unfinished capstone does not block anyone tomorrow.)

## Close the day by saying this out loud

Finishing the capstone is worth their time, but it is **not** a gate on Day 2 — Day 2
profiles the batch script that ships in the repo. Say that explicitly. The four-day cohort
opened every morning with an hour of catch-up precisely because Day N+1 depended on Day N's
homework; that dependency is now cut, so don't reintroduce it by implying it.
