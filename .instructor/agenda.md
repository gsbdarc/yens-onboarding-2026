# Instructor Planning Agenda

**Instructor use only.** Not served by GitHub Pages.

Condensed from the four-day
[GSB Research Computing & AI Skills](https://github.com/gsbdarc/gsb-research-computing-ai-skills)
course. Both mornings run **9:00–12:00**. Day 1 keeps two 10-minute breaks; **Day 2 has
none** — it runs as two self-paced blocks and tables break when they reach a stopping
point.

The section times below are **calibrated against a real four-day cohort** rather than
estimated — see [Where these numbers come from](#where-these-numbers-come-from) at the
bottom, and please correct them again after this course runs.

---

## Day 1 — Foundations & AI

| Clock | Section | min |
|-------|---------|-----|
| 9:00  | **Welcome + prereq triage** — the two-day map; find who is missing an account and seat a helper with them (see `.instructor/prereq-triage.md`) | 5 |
| 9:05  | **Connecting to the Yens** — log in, storage layout, quotas, `module load` | 15 |
| 9:20  | **Git & GitHub** — fork (2 clicks), clone, **make the PAT as a whole-room step**, `gh auth login`, branch, commit, push | 13 |
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
validation step — it is the payoff of the arc. (Day 2 profiles the `extract_form_3_batch.py`
committed in the repo, so it no longer depends on this finishing.)

**Why extraction and the capstone are one block.** Run separately in the four-day course
they *both* overran — extraction ran 25 min and didn't finish, and the capstone consumed
the next morning's first hour. As a single arc the guided build flows straight into
scaling it, with no context switch. Participants **carry on with it in their own time** —
which is what happened anyway. Day 2 no longer depends on it finishing.

## Day 2 — The Cluster

**Restructured this year.** Two cycles of short lecture → long self-paced work block, with
participants at small tables helping each other. No whole-room breaks. Full run-of-show in
`.instructor/day2-teaching-plan.md`.

| Clock | Block | min |
|-------|-------|-----|
| 9:00  | **Lecture 1** — compute environments (6, talk only, no demo); then why a scheduler exists, the live queue, and `#SBATCH` anatomy (14) | 20 |
| 9:20  | **Work block 1** — profiling (all four exercises, ending with the README numbers) → peek at the queue → write & submit a Slurm job → debug `fix_me.slurm` | 70 |
| 10:30 | **Lecture 2** — parallelization and the three shapes (8); array mechanics and the off-by-one (7); estimate → request → run → check (5) | 20 |
| 10:50 | **Work block 2** — the 100-filing array + idempotent tasks → the capstone | 60 |
| 11:50 | **Wrap + Q&A** | 10 |

**40 min lecture · 130 min hands-on · 10 min wrap = 180.**

**Mandatory vs. bonus.** Every Day 2 section is marked on the page. Mandatory: profiling,
the queue, writing/submitting a job, debugging a failed job, job arrays, the capstone.
Bonus: the remaining `fix_me` puzzles, Slurm with Claude, GPUs, merge-to-CSV, chained jobs,
interactive `srun`, and the widget/vectorization extras.

**Protected:** the profiling README (it is the input to every `#SBATCH` number that follows)
and the capstone's write-the-estimate-down step.

**Three deliberate changes from last year's shape:**

- **The recap block is gone.** Day 2 profiles the `extract_form_3_batch.py` committed in the
  repo, so an unfinished Day 1 capstone blocks nobody. Ask about venv / `.env` / clone by
  name and start.
- **`fix_me.slurm` is promoted to mandatory.** Reading a failed job's `.err` is the first
  debugging skill anyone needs, and it used to be an optional practice that the instructor
  did live. Self-paced now, so it has to be required.
- **Slurm with Claude is entirely bonus.** Demo-led delivery has no slot in this format. It
  is the most self-contained section on the day and was already first on the cut list — but
  this is a real reduction in guaranteed coverage, not a free win.

{: .warning }
> **This schedule has never been timed.** The 70/60 split is derived from instructor-led
> measurements of the old section list, not observed in this format. Self-paced pace at a
> table could run faster (nobody waits for the slowest person) or slower (nobody is pulling
> the room forward). **Record the real times and correct these files afterwards.**

{: .important }
> **Slurm reservation.** Day 2 runs against a dedicated reservation, `class_day2`. Every
> `sbatch` and `srun` in the Day 2 pages carries `--reservation=class_day2`, **including the
> job-arrays section and the capstone**. Book it beforehand and confirm the name matches, or
> every command in the docs is wrong.
>
> **One exception:** the GPU bonus (`slurm/gpu_check.slurm`) must **not** carry it — the
> reservation covers the `normal` partition, not the GPU nodes. Check `sinfo -p gpu` has
> idle capacity before class, or that bonus dead-ends.

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
delivered content, not 50%** — there is only one day boundary to lose an hour to, and that
hour is now closed off entirely: Day 2 starts from code that ships in the repo rather than
from the previous day's homework, so there is nothing to spend the hour finishing.

### 2. Measured section times, and what we did about them

| Section | Observed in the 4-day run | Here | Why |
|---|---|---|---|
| Command line + bulk file operations | **60 min**, flagged too long | → pre-work | This *was* the slow first hour |
| Connecting to a cluster + file system | 14 + 11 = 25 | 15 | Most of that 25 was first-time login friction. **The pre-work login check that was supposed to absorb it is gone**, so 15 is now optimistic — this is the first place Day 1 will run over |
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
| Capstones | **60–65** whenever actually run | 23–35 in class | Started in class; participants carry on in their own time |
| `scp` | 10 min spent | → Reference | Nothing in class depends on it |

**Least reliable number on this page:** job arrays at 22 min. The four-day run crammed all
of its Day 4 material into a single 60-minute block, so there is no clean measurement of
the arrays section on its own. Time it deliberately this year.

---

## What Was Cut, and Where It Went

| Original material | Now |
|---|---|
| CLI basics; wildcards, pipes, `grep` | **Optional** [Reference](https://gsbdarc.github.io/yens-onboarding-2026/reference/) reading. Nothing in class depends on it |
| Accounts | **Pre-work** — GitHub + Claude via Stanford, and nothing else. No completion check; chase Yens access by name instead |
| **GitHub PAT creation** | **Back in class** at 9:20, as a whole-room step. It was the measured Git bottleneck, so this costs real time — see `prereq-triage.md` |
| **Claude Code concepts** | **Pre-read**, on the Day 1 page itself; class is hands-on only. Optional now that there is no quiz behind it |
| Day 1 Challenge (grimoire / public IP) | **Dropped.** Removed the grimoire generation and `/scratch/shared` staging entirely |
| `scp` file transfer | [Reference](https://gsbdarc.github.io/yens-onboarding-2026/reference/transferring-files/) |
| Exploring cluster usage data | [Reference](https://gsbdarc.github.io/yens-onboarding-2026/reference/cluster-usage-data/) |
| Documenting your pipeline | Folded into the Day 2 capstone |
| Parallelization concepts (399 lines) | ~4 min at the head of Job Arrays; full page in Reference |
| LLM-as-a-judge ("Genre Tribunal") | **Optional**, self-serve in [Reference](https://gsbdarc.github.io/yens-onboarding-2026/reference/llm-as-a-judge/) |
| **GPUs** | **No longer cut** — now a Day 2 bonus exercise (`docs/day2/gpus.md`, `slurm/gpu_check.slurm`): request one GPU, read `nvidia-smi`, then work out that an I/O-bound job gains nothing from it. **Local LLMs stay cut** — see below |
| Two of four capstones | Merged: one per day, each continuing as homework |
| Grimoire, boss gates, `cast`, leaderboard, quest log | **Deleted.** Nothing tracks progress this cohort; green/red stickies and circulating do the job |

**On GPUs, and what is still cut.** The *local-LLM demo* remains cut, and for the original
reason: it leans on the most fragile instructor infrastructure, and the previous cohort's
dry-run recorded that CPU inference was never exercised and the GPU-vs-CPU timing the demo
rests on **was never measured**. The new GPU bonus deliberately does not depend on any of
that — it submits a 2-minute `nvidia-smi` job and asks one question the participants can
already answer from their own profiling numbers (*would a GPU speed up an I/O-bound job?
No*). If someone wants the local-LLM material, it stays in Reference and in
`.instructor/ollama/`.

---

## No LMS This Cohort

There is no LMS this cohort, so **nothing is collected and nothing is graded**. What
that changes:

- **Pre-work is two accounts** — GitHub, and Claude via Stanford. See
  [Before You Arrive](https://gsbdarc.github.io/yens-onboarding-2026/prework/). No terminal
  install, no login check, no PAT, no reading, no quiz.
- **No completion check on Yens access.** That check was the highest-value pre-work item and
  it is gone, so chase it **by name** a week out — see `.instructor/setup.md`.
- **The GitHub PAT is back in class time.** It was the measured Git bottleneck. Run it as a
  whole-room step at 9:20; see `.instructor/prereq-triage.md`.
- **No between-days assignment.** Day 2 profiles the `extract_form_3_batch.py` committed in
  the repo, so an unfinished Day 1 capstone does not block anyone. Say so out loud at the end
  of Day 1 — and don't imply otherwise.
- **No exit quizzes.**
- **Extensions are self-serve** in [Reference](https://gsbdarc.github.io/yens-onboarding-2026/reference/):
  LLM-as-a-judge, all 992 filings through an array, local LLMs on the Yens GPUs.
- **Progress tracking is green/red stickies and circulating.** In the Day 2 format that is
  the *only* signal you get, so watch the room rather than the clock.
