---
layout: default
title: "Instructor Agenda"
nav_order: 5
permalink: /agenda/
---

# Instructor Planning Agenda

Condensed from the four-day
[GSB Research Computing & AI Skills](https://github.com/gsbdarc/gsb-research-computing-ai-skills)
course. Both mornings run **9:00–12:00 with two 10-minute breaks → ~160 min of
teaching per day, 320 min total**, against roughly 640 min in the original. Canvas
carries the pre-work and the quizzes.

Drive the numbered sections live on screen. **Optional practice is the buffer** —
point fast finishers at it so nobody idles and you don't have to slow the room.

---

## Day 1 — Foundations & AI

| Clock | Section | ~min |
|-------|---------|------|
| 9:00  | **Welcome** — who DARC is, what the Yens are, the two-day map, sticky protocol | 10 |
| 9:10  | **Connecting to the Yens** — log in; storage layout, quotas, `module load`, interactive vs. scheduled nodes | 20 |
| 9:30  | **Git & GitHub for Research** — fork (2 clicks now, not 5), clone, `gh auth`, branch, commit, push | 15 |
| 9:45  | **Working with Claude Code** — models & budgeting, permission modes, context, data governance; first real task | 15 |
| 10:00 | ☕ **Break** | 10 |
| 10:10 | **Running Python on the Yens** — `$PATH`, `module load python`, interpreter vs. notebook vs. script, JupyterHub | 15 |
| 10:25 | **Python Environments** — venv, pip, `requirements.txt`; rebuild Potion Brawl to prove reproducibility | 20 |
| 10:45 | **Stanford's AI Services** — Playground vs. API Gateway, data-risk levels, metering & cost | 15 |
| 11:00 | ☕ **Break** | 10 |
| 11:10 | **Managing API Keys** — `.env`, `python-dotenv`, `.gitignore`, init the client | 10 |
| 11:20 | **Extracting Data with an LLM** — first call → real filing → Pydantic validation → notebook to logged script | 25 |
| 11:45 | **Capstone + AI Agents & Data Privacy** — 10 filings, README, commit; closing discussion | 15 |
| 12:00 | **End** | |

Blocks around the breaks are ≈ **60 / 50 / 50**.

**Protected blocks:** Extracting Data with an LLM (25) and Python Environments (20).
Those two are where the day either lands or doesn't.

**Squeeze first if you're behind:** the JupyterHub tour inside Running Python, and the
Potion Brawl rebuild (demo it rather than having everyone run it).

---

## Day 2 — The Cluster

| Clock | Section | ~min |
|-------|---------|------|
| 9:00  | **Day 1 recap + Q&A** — confirm venv, `.env`, and a working extraction script | 5 |
| 9:05  | **Compute Environments** — laptop vs. Yens vs. cloud; CPU / RAM / storage; the two calculators | 15 |
| 9:20  | **Profiling Resource Usage** — two-terminal live profiling of `mystery_script.py`, then the real batch script | 25 |
| 9:45  | **The Slurm Scheduler** — why it exists; `squeue` / `sinfo`, `R` vs. `PD`, partitions | 15 |
| 10:00 | ☕ **Break** | 10 |
| 10:10 | **Writing & Submitting a Slurm Job** — write it line by line; `sbatch` / `squeue` / `scancel`; read logs; one `fix_me` | 35 |
| 10:45 | **Writing a Slurm Job with Claude** — distil a global `yen-slurm` skill from the job just run, then invoke it | 15 |
| 11:00 | ☕ **Break** | 10 |
| 11:10 | **Slurm Job Arrays** — 5 min parallelization concepts, then `--array`, `SLURM_ARRAY_TASK_ID`, rerun safety | 25 |
| 11:35 | **Capstone** — estimate *first*, submit, compare actual vs. estimate with `sacct`, finish the README | 20 |
| 11:55 | **Where to Go Next** — GPUs & local LLMs (pointer), Slack, DARC, RCpedia | 5 |
| 12:00 | **End** | |

Blocks around the breaks are ≈ **60 / 50 / 50**.

**Protected blocks:** Writing & Submitting a Slurm Job (35). It is the single most
important 35 minutes of the two days — writing the directives by hand, the fresh-shell
and `logs/` gotchas, and reading a failed job's `.err`.

**Squeeze first if you're behind:** the Claude-skill section (demo it, don't have
everyone author one) and the concepts front-half of Job Arrays.

{: .important }
> **Slurm reservation.** Day 2 runs against a dedicated reservation, `class_day2`.
> Every `sbatch` and `srun` in the Day 2 pages carries `--reservation=class_day2`,
> **including the job-arrays section and the capstone**. Book it before the course and
> confirm the name matches, or every command in the docs is wrong.

---

## What Was Cut, and Where It Went

| Original material | Now |
|---|---|
| CLI basics; wildcards, pipes, `grep` | **Canvas pre-work** + [Reference]({{ '/reference/' | relative_url }}), with a quiz |
| Accounts, installs, repo fork | **Canvas pre-work**, incl. a `whoami`-on-a-Yen completion check |
| Day 1 Challenge (grimoire / public IP) | **Dropped.** Removed the grimoire generation and `/scratch/shared` staging entirely |
| `scp` file transfer | [Reference]({{ '/reference/transferring-files/' | relative_url }}) — the shared file system makes it low-priority |
| Exploring cluster usage data | [Reference]({{ '/reference/cluster-usage-data/' | relative_url }}) |
| Documenting your pipeline | Folded into the Day 2 capstone |
| Parallelization concepts (399 lines) | Compressed to ~5 min at the head of Job Arrays; full page in Reference |
| LLM-as-a-judge ("Genre Tribunal") | **Optional Canvas assignment** |
| **GPUs & local LLMs** | **The one topic cut from class.** 5-min closing pointer + three Reference pages + optional Canvas module |
| Two of four capstones | Merged: one per day |
| Grimoire, boss gates, `cast`, leaderboard, quest log | **Deleted** — progress tracking is Canvas's job now |

The GPU/local-LLM cut is the deliberate one. It is the least actionable topic for
someone in their first week, everything else is a prerequisite *to* it rather than the
reverse, and it leans on the most fragile instructor infrastructure — the previous
cohort's dry-run recorded that CPU inference was never exercised and the GPU-vs-CPU
timing the demo rests on was never measured.

---

## Canvas

Built separately; see `.instructor/canvas-modules.md` in this repo for the full spec.

- **Pre-work module** (before Day 1) — accounts, terminal, the two CLI reading pages, an 8-question quiz, and the `whoami` completion check
- **Day 1 exit quiz** — venvs, `.env` vs. `.gitignore`, data-risk levels, what Pydantic buys you
- **Day 2 exit quiz** — `#SBATCH` directives, `squeue` states, arrays vs. loops, sizing `--mem` and `--time`
- **Optional assignments** — LLM-as-a-judge; all 992 filings through an array; local LLMs on the Yens GPUs
