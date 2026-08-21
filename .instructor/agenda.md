# Instructor Planning Agenda

**Instructor use only.** Not served by GitHub Pages.

Condensed from the four-day
[GSB Research Computing & AI Skills](https://github.com/gsbdarc/gsb-research-computing-ai-skills)
course. Both mornings run **9:00–12:00 with two 10-minute breaks**.

The section times below are **calibrated against a real four-day cohort** rather than
estimated — see [Where these numbers come from](#where-these-numbers-come-from) at the
bottom, and please correct them again after this course runs.

---

## Day 1 — Foundations & AI

| Clock | Section | min |
|-------|---------|-----|
| 9:00  | **Welcome + pre-work triage** — the two-day map; find who is missing a prereq and seat a helper with them (see `.instructor/prereq-triage.md`) | 5 |
| 9:05  | **Connecting to the Yens** — log in, storage layout, quotas, `module load` | 15 |
| 9:20  | **Git & GitHub** — fork (2 clicks), clone, `gh auth login` with the token they made in pre-work, branch, commit, push | 13 |
| 9:33  | **Working with Claude Code** — hands-on only: sign in, `/cost`, `Shift+Tab` through modes, one real task, install `github-for-research` | 25 |
| 9:58  | *slack* | 2 |
| 10:00 | ☕ **Break** | 10 |
| 10:10 | **Running Python on the Yens** — `$PATH`, `module load python`, script vs. notebook. JupyterHub is a **tour**, not a lab | 14 |
| 10:24 | **Python environments** — venv, pip, `requirements.txt`; the Potion Brawl rebuild as a **demo** | 18 |
| 10:42 | **Stanford's AI services + data privacy** — Playground vs. Gateway, data-risk levels, cost; the agents/privacy discussion folded in here | 14 |
| 10:56 | *slack* | 4 |
| 11:00 | ☕ **Break** | 10 |
| 11:10 | **Managing API keys** — `.env`, `python-dotenv`, `.gitignore`, init the client | 13 |
| 11:23 | **Extraction → Day 1 capstone** *(one continuous arc)* — first call → one filing → Pydantic; then straight into 10 filings, README, commit via Claude Code | 35 |
| 11:58 | *slack* | 2 |

**152 min teaching · 20 min breaks · 8 min slack = 180.**

**Protected:** Claude Code (25) and the extraction-to-capstone arc (35). These are the two
things the four-day cohort never got enough of.

**Squeeze first if behind:** the JupyterHub tour inside Running Python; then demo the
Potion Brawl rebuild instead of having everyone run it. Do **not** cut the Pydantic
validation step — Day 2's profiling section needs a working `extract_form_3_batch.py`.

**Why extraction and the capstone are one block.** Run separately in the four-day course
they *both* overran — extraction ran 25 min and didn't finish, and the capstone consumed
the next morning's first hour. As a single arc the guided build flows straight into
scaling it, with no context switch. It **continues as Canvas homework**, which is what
happened anyway.

## Day 2 — The Cluster

| Clock | Section | min |
|-------|---------|-----|
| 9:00  | **Recap + artifact check** — confirm venv, `.env`, and a working `extract_form_3_batch.py`. Profiling needs all three | 5 |
| 9:05  | **Compute environments** — demo-led: the two calculators and the disk→RAM→CPU animation | 15 |
| 9:20  | **Profiling** — two-terminal `time` / `watch userload` / `htop` on `mystery_script.py`, then the real batch script | 25 |
| 9:45  | **The Slurm scheduler** — `squeue` / `sinfo`, `R` vs. `PD`, partitions, on the **live** queue | 10 |
| 9:55  | *slack* | 5 |
| 10:00 | ☕ **Break** | 10 |
| 10:10 | **Writing & submitting a Slurm job** — write it by hand; `sbatch` / `squeue` / `scancel`; read `.out`/`.err`; **one `fix_me`** | 35 |
| 10:45 | **Slurm with Claude** — demo-led: distil the global `yen-slurm` skill, invoke it once | 12 |
| 10:57 | *slack* | 3 |
| 11:00 | ☕ **Break** | 10 |
| 11:10 | **Job arrays** — 4 min of concepts, then `--array`, `SLURM_ARRAY_TASK_ID`, rerun safety | 22 |
| 11:32 | **Day 2 capstone** — write the estimate **first**, submit, compare against `sacct` | 23 |
| 11:55 | **Where to go next + Q&A** | 5 |

**152 min teaching · 20 min breaks · 8 min slack = 180.**

**Protected:** Writing & Submitting a Slurm Job (35). It is the single most important
block of the two days — writing the directives by hand, the `logs/` and fresh-shell
gotchas, and reading a failed job's `.err`.

**Squeeze first if behind:** Slurm with Claude is already demo-led and can drop to 8; then
the concepts half of Job Arrays.

{: .warning }
> **Q&A is under-budgeted and we know it.** The four-day cohort spent a **full hour** on
> Q&A on its last morning. Two mornings accumulate less confusion, and circulating during
> the capstone absorbs a lot of it — but if the room is full of questions, **shorten the
> capstone, not the breaks.** The capstone continues as homework; the questions won't.

{: .important }
> **Slurm reservation.** Day 2 runs against a dedicated reservation, `class_day2`. Every
> `sbatch` and `srun` in the Day 2 pages carries `--reservation=class_day2`, **including
> the job-arrays section and the capstone**. Book it beforehand and confirm the name
> matches, or every command in the docs is wrong.

---

## Where These Numbers Come From

A real four-day cohort was timed section by section. Two findings reshaped this agenda.

### 1. The four-day course delivered ~395 min of new content, not 640

Roughly **three of its twelve hours went to finishing the previous day's material**:

| | Spent on the prior day |
|---|---|
| Day 2, 9:00–10:00 | finishing Claude Code + the Day 1 challenge |
| Day 3, 9:00–10:05 | the Day 2 challenge + demo |
| Day 4, 9:00–10:00 | the Day 3 capstone |

Plus a 60-minute Q&A on the final morning. So this two-day version cuts about **19% of
delivered content, not 50%** — there is only one day boundary to lose an hour to, and
that hour is now a deliberate Canvas assignment instead of an overrun.

### 2. Measured section times, and what we did about them

| Section | Observed in the 4-day run | Here | Why |
|---|---|---|---|
| Command line + bulk file operations | **60 min**, flagged too long | → pre-work | This *was* the slow first hour |
| Connecting to a cluster + file system | 14 + 11 = 25 | 15 | Most of that 25 was first-time login friction; the pre-work `whoami` check removes it |
| Git & GitHub | **20**, and the Actions step failed for several people | 13 | Actions/Pages clicks removed entirely; PAT creation moved to pre-work |
| Claude Code | ~30, then **spilled ~60 min into Day 2** | 25 hands-on | ~180 lines of concept became a pre-read |
| Running Python on the Yens | **25–35**, flagged too slow | 14 | JupyterHub demoted to a tour |
| Python environments | 20, "could be streamlined" | 18 | Potion Brawl rebuild is a demo |
| Stanford AI services | **10** | 14 | *Given time back*, with the privacy discussion folded in |
| Managing API keys | **20** | 13 | `.env` copy pre-staged |
| Extraction | **25 and did not finish** | merged into 35 | See above |
| Compute environments | **27** (the demo alone was 15) | 15 | Demo-led; remaining lecture cut |
| Profiling | **27** | 25 | Roughly right as-is |
| Exploring cluster usage data | **skipped live** | → Reference | Confirmed cut |
| The Slurm scheduler | **10** | 10 | *Given time back* |
| Writing & submitting a Slurm job | **25**, without the debug exercises | 35 | Adds one `fix_me` |
| Slurm with Claude | **15**, second skill never reached | 12 | Second skill is now optional practice |
| Documenting your pipeline | **never reached, twice** | → Reference | Confirmed cut |
| Capstones | **60–65** whenever actually run | 23–35 + homework | Started in class, finished on Canvas |
| `scp` | 10 min spent | → Reference | Nothing in class depends on it |

**Least reliable number on this page:** job arrays at 22 min. The four-day run crammed all
of its Day 4 material into a single 60-minute block, so there is no clean measurement of
the arrays section on its own. Time it deliberately this year.

---

## What Was Cut, and Where It Went

| Original material | Now |
|---|---|
| CLI basics; wildcards, pipes, `grep` | **Canvas pre-work** + [Reference](https://gsbdarc.github.io/yens-onboarding-2026/reference/), with a quiz |
| Accounts, installs, repo fork | **Canvas pre-work**, incl. a `whoami`-on-a-Yen completion check |
| **GitHub PAT creation** | **Canvas pre-work** — it was the measured Git bottleneck |
| **Claude Code concepts** | **Canvas pre-read**, on the Day 1 page; class is hands-on only |
| Day 1 Challenge (grimoire / public IP) | **Dropped.** Removed the grimoire generation and `/scratch/shared` staging entirely |
| `scp` file transfer | [Reference](https://gsbdarc.github.io/yens-onboarding-2026/reference/transferring-files/) |
| Exploring cluster usage data | [Reference](https://gsbdarc.github.io/yens-onboarding-2026/reference/cluster-usage-data/) |
| Documenting your pipeline | Folded into the Day 2 capstone |
| Parallelization concepts (399 lines) | ~4 min at the head of Job Arrays; full page in Reference |
| LLM-as-a-judge ("Genre Tribunal") | **Optional Canvas assignment** |
| **GPUs & local LLMs** | **The one topic cut from class.** 5-min closing pointer + three Reference pages + optional Canvas module |
| Two of four capstones | Merged: one per day, each continuing as homework |
| Grimoire, boss gates, `cast`, leaderboard, quest log | **Deleted** — progress tracking is Canvas's job now |

The GPU/local-LLM cut is the deliberate one. It is the least actionable topic for someone
in their first week, everything else is a prerequisite *to* it rather than the reverse, and
it leans on the most fragile instructor infrastructure — the previous cohort's dry-run
recorded that CPU inference was never exercised and the GPU-vs-CPU timing the demo rests
on was never measured.

---

## Canvas

Built separately; see `.instructor/canvas-modules.md` for the full spec, and
[Before You Arrive](https://gsbdarc.github.io/yens-onboarding-2026/prework/) for the student-facing checklist and
the prereq dependency map.

- **Pre-work module** (before Day 1) — accounts, terminal, **GitHub PAT**, the two CLI reading pages, the **Claude Code concepts pre-read**, a 10-question quiz, and the `whoami` completion check
- **Between-days assignment** — finish the Day 1 capstone. Required, not optional: Day 2's profiling section needs a working `extract_form_3_batch.py`
- **Day 1 and Day 2 exit quizzes**
- **Optional extensions** — LLM-as-a-judge; all 992 filings through an array; local LLMs on the Yens GPUs
