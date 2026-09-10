# Day 2 — Teaching Run-of-Show (9:00–12:00)

**Instructor use only.** Not served by GitHub Pages. `.instructor/agenda.md` has the
measured times behind this schedule.

**Two cycles of short lecture → long self-paced work block.** Participants sit at small
tables and help each other; we circulate. **No whole-room breaks** — tables break when they
reach a natural stopping point.

**40 min lecture · 130 min hands-on · 10 min wrap = 180.**

---

## Before you start

- `scontrol show reservation class_day2` — confirm it is live. Every `sbatch` and `srun` in
  today's pages carries `--reservation=class_day2`, **including job arrays and the
  capstone**. The **one exception is the GPU bonus**, which must *not* carry it.
- `sinfo -p gpu` — confirm the GPU partition has idle nodes. If it is fully drained or
  down, say so when you introduce the bonus, or the page dead-ends. 14 GPUs cluster-wide
  (yen-gpu1 4×A30, yen-gpu2/3 4×A40, yen-gpu4 2×H200), so expect queueing if a whole table
  submits at once. `slurm/gpu_check.slurm` is capped at 2 minutes for this reason.
- **No artifact check this year.** Day 2 profiles `scripts/extract_form_3_batch.py` as
  committed in the repo, so nobody is blocked by unfinished Day 1 work. You still need
  venv + `.env` + a clone — ask about those three by name and pair anyone missing one.

## The shape of the day

| Clock | Block | min | Mode |
|-------|-------|-----|------|
| 9:00  | **Lecture 1** — where your code runs, and who decides | 20 | talk |
| 9:20  | **Work block 1** — profile it, then hand it to Slurm | 70 | self-paced |
| 10:30 | **Lecture 2** — scaling out | 20 | talk |
| 10:50 | **Work block 2** — scale it, then size it | 60 | self-paced |
| 11:50 | Wrap + Q&A | 10 | talk |

### Lecture 1 (9:00–9:20)

| min | What |
|---|---|
| 6 | **Compute environments** — CPU cores, RAM, storage; the disk→RAM→CPU path; laptop vs. Yens vs. cloud. **Talk it through — no live demo.** The two calculator widgets stay on the page as bonus, so don't drive them from the front |
| 14 | **Why a scheduler exists** — the live queue on the projector (`squeue`, `sinfo`, `R` vs. `PD`, partitions), then the **anatomy of an `#SBATCH` header** line by line, so nobody starts Block 1 from zero |

Big font, projector, and *read the live queue* — a busy queue teaches `PD` better than any
slide. Note that `squeue` filters with its own flags (`--me`, `-p`, `-o`), not pipes.

### Work block 1 (9:20–10:30, 70 min)

**Mandatory, in order** — each one's output is the next one's input:

1. **Profiling** — all four exercises, ending with the **Resource Profile written into the
   README**. That README is where the `#SBATCH` numbers come from, so don't let anyone skip
   the writing-it-down step.
2. **Slurm scheduler** — Peek at the Queue.
3. **Slurm job** — write the directives by hand, `sbatch`, `squeue`, `scancel`, email
   notifications, read `.out`/`.err`.
4. **Debug a Failed Job** — `slurm/fix_me.slurm`. **Promoted to mandatory this year.**
   Reading a failed job's `.err` is the skill they need first, and it used to be the one
   thing you did live. Its `<details>` wrapper is removed so the steps are visible.

**Two gotchas bite everyone.** Watch for both while circulating: `logs/` must exist before
submit (Slurm resolves `--output` at submit time), and a fresh shell on the compute node
has no venv.

### Lecture 2 (10:30–10:50)

| min | What |
|---|---|
| 8 | **Parallelization** — embarrassingly parallel work; the three shapes (one job/many cores, many jobs/one core, both); waves when filings outnumber cores. Condensed from `docs/reference/parallelization.md`; the four runnable demos are in `.instructor/parallelization_demos/` if you want to show one |
| 7 | **Array mechanics** — `--array`, `%A`/`%a`, `SLURM_ARRAY_TASK_ID`. **Tasks count from 0 throughout**, matching the deck's `0 to 511` — a task ID indexes a list directly, so there is no off-by-one to plant. Do say the cap out loud: `MaxArraySize` caps the *index* at 511 on **every** submission, which is why the 992 bonus cannot just continue at a higher index |
| 5 | **estimate → request → run → check** — and why the capstone estimate gets written down *before* submitting. Protect this; it is the one thing that changes how people size their own jobs afterwards |

### Work block 2 (10:50–11:50, 60 min)

**Mandatory:**

1. **Hello World Array** — `slurm/hello_array.slurm`, fan-out, `%A`/`%a`.
2. **Scale the Loop to an Array** — the block's real exercise. They get a brief, not a
   walkthrough: turn Part 1's loop into a 100-task array, write both files themselves, run
   it, read `sacct`. On-page hints are nudges only; working code is in
   `.instructor/loop-to-array.key.md`. **Do not hand out the key** — the conclusion they
   have to reach on their own is that one task = one filing. If someone has kept the loop
   and added `--array`, ask what task 7 is doing that task 8 is not.
3. **Rerun-safe tasks** — the existence check, then resubmit and watch it finish in seconds.
4. **Scale** — all ~992 filings, the `MaxArraySize` wall, then document and push.

**This no longer has slack.** The old list measured ~45 min against the 60, but Scale is now
the full 992 run rather than a bonus, which is what that ~15 min used to absorb. If the room
is behind, the thing to cut is Scale's *submission*: have them work out the batching and size
it, and stop short of running it. Steps 1–3 are what the checkpoint depends on.

**Bonus, in rough order of value:** the remaining `fix_me` puzzles → Slurm with Claude →
**GPUs & Local LLMs** → merge-to-CSV → Reference pages.

**The GPUs & Local LLMs page (`/day2/gpus/`) needs setup.** It absorbed both Reference pages
on local LLMs plus the old GPU bonus, and its second exercise is **one Ollama server per
table**: one person `srun`s a GPU, starts the server from `gsbdarc/ollama_helper`, reads the
host/port out of `/scratch/users/$USER/ollama/`, and gives the URL to their table. Before
class:

- Confirm the reservation admits `--partition=gpu`, and that the reserved node has **enough
  GPUs for one per table**. Fewer means tables share, or serve on CPU — `llama3.2:1b` does
  answer on CPU, slowly, and `.instructor/ollama/start_ollama_server.sh` warns and continues.
- Warm one server yourself with that script as a fallback, so a table that cannot get a GPU
  still has something to query. It prints the URL to put on the board.
- The first `apptainer pull` is slow. If several tables pull at once it is slower; consider
  pulling `ollama.sif` into a shared location beforehand.

---

## Section notes, from what actually happened last time

| Section | What the clock showed | What to do |
|---|---|---|
| **Recap** | The four-day course spent **60–65 min** here, every single day | Gone. There is no recap block — ask about venv/`.env`/clone by name and start Lecture 1. Resist reopening Day 1 |
| **Compute environments** | Ran **27**, of which the demo was 15 | Now 6 min of talk. The demo is cut; the widgets are bonus on the page |
| **Profiling** | Ran **27** | The best-remembered section. Two terminals side by side, big font, while you circulate |
| **The Slurm scheduler** | Ran **10** | Split: concepts in Lecture 1, `squeue`/`sinfo` hands-on in Block 1 |
| **Writing & submitting a Slurm job** | Ran **25** — *without* any debugging | Still the most important stretch of the two days. Writing the directives by hand is the point; don't let anyone paste a finished script |
| **Slurm with Claude** | Ran **15**, and the second skill was never reached | **Now entirely bonus.** Demo-led delivery has no slot in this format. Self-paced framing is on the page |
| **Job arrays** | **No clean measurement** — the four-day course crammed all its Day 4 material into one block | Still the least reliable number here. **Time it deliberately.** |
| **Capstone** | Ran **60** when actually reached, and was skipped entirely the first time | Make them **write the estimate down before submitting**. The `sacct` comparison is the whole lesson and there is nothing to compare against without a recorded guess |

## If you are behind at 10:50

The mandatory list in Block 2 is short precisely so you don't have to cut it. If a table is
still finishing Block 1 work, let them — the array exercise is more valuable than the
capstone only if they already have a job that runs. **Protect the capstone's estimate
step** over everything else in the block.

## When a table finishes early

Point them at their neighbours first, then the bonus list. The standing instruction is on
every page and on the Day 2 landing page; say it out loud once at 9:20 anyway.

## Q&A

Ten minutes at the end, plus whatever you absorb while circulating — which in this format
should be most of it. The four-day cohort spent a **full hour** on Q&A on its final
morning; if the room is still full of questions at 11:50, run over into the capstone's
slack rather than cutting the wrap-up.

## Known gotchas

- `curl` on the Yens is 7.81.0, so `--json` does not exist. Use `-H` and `-d`.
- Slurm resolves `--output`/`--error` relative to the submit directory **at submit time**,
  so `logs/` must pre-exist. The site teaches this at `submit-a-slurm-job.md:112`.
- `MaxArraySize` is 512 (`scontrol show config`) against 992 filings in
  `data/aws_links.csv` — that mismatch is the point of Scale.

## This schedule has never been timed

The 70/60 split is **derived** from instructor-led measurements of the old section list, not
observed in this format. Self-paced pace at a table is genuinely unknown — it could run
faster (no waiting for the slowest person) or slower (no instructor pulling the room
forward). **Note the real times as you go and correct this file afterwards.**
