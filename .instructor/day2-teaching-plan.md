# Day 2 — Teaching Run-of-Show (9:00–12:00)

**Instructor use only.** Not served by GitHub Pages. `.instructor/agenda.md` has the section
table and the measured times behind it.

**152 min teaching · 20 min breaks · 8 min slack.** Blocks are 60 / 50 / 50.

---

## Before you start

- `scontrol show reservation class_day2` — confirm it is live. Every `sbatch` and `srun` in
  today's pages carries `--reservation=class_day2`, **including job arrays and the capstone**.
- Have a **known-good branch** ready to hand anyone who didn't finish the between-days
  assignment. Without a working `extract_form_3_batch.py` they cannot do the 9:20 profiling
  section, and that is the whole first block.

## The shape of the day

| Clock | Section | min | Mode |
|-------|---------|-----|------|
| 9:00 | Recap + artifact check | 5 | talk |
| 9:05 | Compute environments | 15 | demo |
| 9:20 | Profiling | 25 | hands-on |
| 9:45 | The Slurm scheduler | 10 | live queue |
| 10:00 | ☕ Break | 10 | |
| 10:10 | Writing & submitting a Slurm job | 35 | **hands-on, protected** |
| 10:45 | Slurm with Claude | 12 | demo |
| 11:00 | ☕ Break | 10 | |
| 11:10 | Job arrays | 22 | hands-on |
| 11:32 | Day 2 capstone | 23 | hands-on |
| 11:55 | Where to go next + Q&A | 5 | talk |

## Section notes, from what actually happened last time

| Section | What the clock showed | What to do |
|---|---|---|
| **Recap** (5) | The four-day course spent **60–65 min** here, every single day | Keep it to the checklist: venv, `.env`, working batch script. Hand out the known-good branch and move on. Resist reopening Day 1 |
| **Compute environments** (15) | Ran **27**, of which the demo was 15 | Run the demo, skip the rest. The two calculators and the disk→RAM→CPU animation carry it; the lecture prose around them has been cut from the page |
| **Profiling** (25) | Ran **27** | About right. Two terminals side by side on the projector, big font. This is the section people remember |
| **The Slurm scheduler** (10) | Ran **10** | Accurate. Read the *live* queue — a busy queue teaches `PD` better than any slide. Note that `squeue` filters with its own flags (`--me`, `-p`, `-o`), not pipes |
| **Writing & submitting a Slurm job** (35) | Ran **25** — but that was *without* any debugging | **The most important 35 minutes of the two days, and protected.** Write the directives by hand. Two gotchas bite everyone: `logs/` must exist before submit (Slurm resolves `--output` at submit time), and a fresh shell on the compute node has no venv. Then do **one** `fix_me*.slurm` live — reading a failed job's `.err` is the skill they need first |
| **Slurm with Claude** (12) | Ran **15**, and the second skill was never reached | Demo-led now, and the project/plotting skill is optional practice on the page. Show the global `yen-slurm` skill being distilled and invoked once. Drop to 8 if you're behind |
| **Job arrays** (22) | **No clean measurement** — the four-day course crammed all its Day 4 material into one 60-min block | The least reliable number on the schedule. **Time it deliberately this year.** 4 min of concepts, then hands on keyboard. Let them hit the off-by-one between `--array=1-10` and a zero-indexed CSV |
| **Capstone** (23) | Ran **60** when actually reached, and was skipped entirely the first time | Make them **write the estimate down before submitting**. The `sacct` comparison is the whole lesson and there is nothing to compare against without a recorded guess. It continues as homework |

## If you are behind at 11:10

Cut Slurm-with-Claude to 8 (or skip it — it is the most self-contained section on the day),
and compress the Job Arrays concept half to the single "100 filings, 4 workers" example.

**Protect the capstone's estimate step.** It is the one thing on Day 2 that changes how
people size their own jobs afterwards.

## Q&A

The four-day cohort spent a **full hour** on Q&A on its final morning. Five minutes here is
thin, deliberately: two mornings accumulate less confusion, and circulating during the
capstone absorbs a lot of it. If the room is full of questions, **shorten the capstone,
not the breaks** — the capstone continues as homework, the questions don't.

## Known gotchas

- `curl` on the Yens is 7.81.0, so `--json` does not exist. Use `-H` and `-d`.
- Slurm resolves `--output`/`--error` relative to the submit directory **at submit time**,
  so `logs/` must pre-exist. `slurm/hello.slurm` notes this in its header.
- `MaxArraySize` is 512 (`scontrol show config`) against 992 filings in
  `data/aws_links.csv` — that mismatch is the point of the optional full-scale assignment.
