# Day 2 — Lecture Topics & the Main/Bonus Split

**Instructor use only.** Not served by GitHub Pages.

Two decisions live here: **what goes on the slides**, and **which exercises every single
person has to clear**. `.instructor/day2-teaching-plan.md` has the run-of-show and the
timings; `.instructor/agenda.md` has the measured history behind them.

The room is all new PhD students, but the skill spread is the widest of anything we teach:
some have never opened a terminal, some have written parallel code for years. Every decision
below is made against that spread.

---

## The principle behind the split

**Prose and discussion go on a slide. Anything with a keyboard stays in the work block.**

Six chunks of Day 2 are currently pure reading sitting *inside* the work blocks, competing
with hands-on time. They are already-written lecture material — nothing new to author:

| Where it is now | Belongs in |
|---|---|
| `compute-environments.md` — the whole page bar two widget bonuses | Lecture 1 |
| `profiling.md:68–87` — Questions 1–3, deliberately unanswerable before the technique | Lecture 1 |
| `slurm-scheduler.md:13–91` — ~80 lines of concept before the first command | Lecture 1 |
| `job-arrays.md:16–110` — the two `hello` demos, the fan-out diagram, the off-by-one warning | Lecture 2 |
| `job-arrays.md:276–285` — "Why a Job Array Beats a Loop" | Lecture 2 |
| `capstone.md:21` — the I/O-bound framing that sets up the estimate | Lecture 2 |

Moving these to the front of the room recovers roughly **20 minutes of hands-on time**.

The website keeps all of it in depth — students re-read the pages during the block. Nothing
is deleted from the site; the slides are the spine, the pages are the reference.

---

## Lecture 1 (9:00–9:20) — "Where your code runs, and who decides"

Six slides, ~3 minutes each. One idea per slide.

| # | Slide | Why it earns a slide | Reuse |
|---|---|---|---|
| 1 | **Three things every script needs: cores, RAM, time** | The vocabulary for the whole morning. Nothing after this lands without it | `compute-environments.md:39` onward + the disk→RAM→CPU animation |
| 2 | **Why not just run it right here?** Five shared interactive Yens, per-user caps, a 256-core node you don't own | Makes the scheduler a *fairness* mechanism rather than bureaucracy | `slurm-scheduler.md:13–56` |
| 3 | **Measure, don't guess.** *Do you know what your script uses right now? How would you find out?* | The best hook on the day. Already written as three questions nobody in the room can answer yet — ask them, let it be awkward, don't answer | `profiling.md:68–87` |
| 4 | **`real` vs `user`** — and what a gap between them tells you | The idea that makes profiling more than button-pushing. Sets up I/O-bound vs CPU-bound without naming it yet | `profiling.md:155–174` |
| 5 | **The queue** — submit → `PD` → `R` → logs. **Show the live queue** | A busy queue teaches `PD` better than any diagram. If the queue is empty, say so and use the diagram | job-lifecycle SVG at `slurm-scheduler.md:123` |
| 6 | **Anatomy of `#SBATCH`** — the money slide | They will refer back to this for the next 70 minutes. **Put one valid `--time` and one valid `--mem` value on it** — the docs never show an example, and it is the most common first error | annotated SVG at `slurm-job.md:148` |

**Close with the preview:** *by 10:30 you will have submitted a job, read its logs, and
fixed a broken one.* Self-paced work needs a stated finish line, and lectures usually skip it.

**Say out loud, don't put on a slide**

- The **login node vs. compute node** distinction, at slide 2. One sentence. It causes more
  downstream confusion than anything else on Day 2.
- **How to edit a file on the Yens.** The first two places students must edit a file
  (`profiling.md:323` and `:371`) name no editor at all; the JupyterHub recipe doesn't appear
  until `slurm-job.md:62`. Say it once at the start of the block: JupyterHub file browser, or
  `nano` if they know it.
- **`SUNetID` and `JOBID` are placeholders, not literal text.** The docs make this point
  beautifully for `JOBID` once and never for `SUNetID`, which appears literally in about
  fourteen commands.

**If Lecture 1 overruns**, compress slide 1 — it's the most familiar material in the room.
Protect slides 4 and 6; block 1 depends on both.

---

## Lecture 2 (10:30–10:50) — "Scaling out"

Seven slides. Slide 5 is a deliberate trap, not an oversight.

| # | Slide | Why it earns a slide | Reuse |
|---|---|---|---|
| 1 | **Your loop is a choice, not a law** — 100 filings one at a time, or 100 at once | Frames the block as a decision they own | `job-arrays.md:43–47` |
| 2 | **What qualifies: independence.** The embarrassingly-parallel test | The one concept that transfers to their own research | `reference/parallelization.md`, condensed hard |
| 3 | **Three shapes** — one job/many cores · many jobs/one core · both | The 2×2. Enough to place any workload they meet later | `reference/parallelization.md` summary table |
| 4 | **The array.** One script, `--array`, and `$SLURM_ARRAY_TASK_ID` is the *only* difference between tasks | Show `hello.slurm` and `hello_array.slurm` side by side — **they differ by one line.** That single diff is the whole mechanism | `job-arrays.md:20–72`, fan-out SVG |
| 5 | **The off-by-one.** Tasks count from 1, Python lists from 0. **Name it, do not solve it** | Warn them so it's recognisable when it bites. Defusing it removes the lesson — the failure is silent, which is exactly what makes it worth meeting once | `job-arrays.md:109–110` |
| 6 | **Why an array beats a loop** — failure isolation, one job ID, waves | Pure prose today, sitting in the work block | `job-arrays.md:276–285` |
| 7 | **estimate → request → run → check** — and why the guess gets written down **first** | The transferable discipline, and the capstone's entire point | `capstone.md:21–31` |

**Close with the preview:** *100 filings, then check yourself against `sacct`.*

**Say out loud, don't put on a slide**

- **`slurm/hello_array.slurm` is already in their repo.** It is a complete, correct array
  template — `--array=1-4`, `%A_%a` log naming, and the `mkdir -p logs` reminder in its
  header. The page pastes its *contents* into a demo block and never names the path, so
  nobody knows the file exists. Telling them to `cp` it is the single cheapest thing that
  makes block 2 reachable for the whole room.
- **`MaxRSS` is in kilobytes and shows up on the `.batch` row.** The capstone turns entirely
  on comparing it against the estimate, and the docs never explain the column.
- **`mkdir -p logs` before submitting an array.** `logs/` is gitignored, so it doesn't exist
  after a clone, and Slurm resolves `--output` at submit time. Without it, all 100 tasks fail
  and leave no log to explain why.

**If Lecture 2 overruns**, merge slides 2 and 3. Protect slides 5 and 7.

---

## Main vs Bonus

**Main** = every person leaves able to do it. **Bonus** = depth, or for whoever finishes early.

The standing instruction stays: **if you finish the Main exercises, check whether anyone at
your table is stuck before starting Bonus material.**

### Work block 1 (9:20–10:30)

| Exercise | Call |
|---|---|
| Profile the mystery script (two terminals) | **Main** — the most-remembered exercise of the day; teaches serial vs. parallel by observation |
| Profile the batch script | **Main** — where I/O-bound lands, and it produces the numbers everything downstream needs |
| Write the Resource Profile into the README | **Main** — the handoff. **Protect this above everything else in block 1**; the `#SBATCH` values come from here |
| Peek at the Queue | **Main** — two minutes, and it makes the lecture's queue concrete |
| Write & submit a Slurm job | **Main** — the core skill of the morning |
| Debug a failed job (`fix_me.slurm`) | **Main — the most important one.** Reading a failed job's `.err` is the first thing they will actually need |
| "Run Your Script" warm-up | **→ Lecture 1.** Its value is the three unanswerable questions, which are a hook, not a keyboard task. The `python` invocation folds into the next exercise |
| Watch a job on its node · interactive `srun` · `fix_me_2`/`_3` · broken one-file · chain two jobs · `dev` partition · vectorization · core count · prompt caching · `longsqueue` · `scontrol` · compare partitions | **Bonus** — all fine where they are |

### Work block 2 (10:50–11:50)

| Exercise | Call |
|---|---|
| Get an array running, **starting from `slurm/hello_array.slurm`** | **Main** — everyone should see fan-out work with their own eyes |
| Avoiding wasteful computation (idempotent tasks) | **Main** — four lines, and rerun-safety is the habit that saves them real money later |
| Capstone — estimate first, submit, compare against `sacct` | **Main** — the transferable discipline of the whole course |
| Write both array files from scratch | **→ Bonus** — see the flag below |
| Merge results to CSV · Slurm with Claude · GPUs · all 992 filings | **Bonus** |

### The one call worth arguing about

Splitting the array exercise into **run one** (Main) and **build one from scratch** (Bonus)
is the biggest judgement in this document, and it is a real trade. A student who only does
the Main version has *adapted a template* rather than reasoned from a blank page, and that
is genuinely less.

The reason to accept it: authoring two files from scratch does not fit the block for roughly
half the room. An experienced programmer finishes in under ten minutes; someone new to the
command line is still assembling files at forty-five. And a novice who runs out of time
gets **neither** the authoring practice **nor** a working array — they leave with nothing
from the one section that the whole "scaling" half of the day exists to deliver.

This way everyone gets the array running, and the authoring is right there for anyone who
wants it. The learning objective was never "can you type a Slurm script from memory" — it
is the off-by-one, the fan-out, and reading a failed task's log. All three survive.

### For the experienced — a ranked list, not the whole pile

Most of Day 2 is genuinely trivial for someone with real HPC experience. Don't send them
into the bonus pile at random; these are the only items with new content in them:

1. **Slurm with Claude** — skill scoping, global vs. project, description-as-trigger. The
   highest expert-value material on the day by a distance.
2. **The array from scratch.**
3. **GPUs** — mainly for the think-first question, which works at any level.
4. `$HOMEyens` variable-boundary bug (in the broken one-file bonus); `OPENBLAS_NUM_THREADS`
   on a shared node.

And the honest first answer stays: **go help your table.** Explaining a thing you just
learned is the fastest way to find out whether you actually learned it, and in a room this
uneven it's worth more than another exercise.

---

## The mastery floor — 8 things everyone leaves able to do

This is the test of whether the split above is right. Every item must be reachable using
**Main exercises only** — and as assigned, each one is.

| # | They can… | From |
|---|---|---|
| 1 | Measure a script's wall-clock, cores, and RAM instead of guessing | profiling |
| 2 | Tell an I/O-bound job from a CPU-bound one, from `real` vs `user` | profiling |
| 3 | Write those numbers somewhere the next step can use them | profiling README |
| 4 | Read the queue and tell `R` from `PD` | peek at the queue |
| 5 | Turn measured numbers into `#SBATCH` directives and submit | write & submit |
| 6 | Find and read a job's `.out` and `.err` | write & submit |
| 7 | **Diagnose a failed job from its `.err`** ← the one that matters most | debug a failed job |
| 8 | Explain what an array buys, and compare actual vs. requested with `sacct` | array + capstone |

If you have to cut on the day, cut *toward* this list. Items 3 and 7 are the two that
nothing else on Day 2 substitutes for.

---

## Not yet done

Deliberately deferred — this document is an agenda decision, not a content pass.

- **The website still labels sections Mandatory/Bonus by time, not by this split.**
  `docs/day2/index.md` and the section pages need relabelling to match.
- **A set of real defects found while surveying the exercises** is recorded in the planning
  notes and has not been touched: the `NUM_FILINGS` trap that invalidates the capstone's own
  conclusion, the unexplained `MaxRSS`/`ReqTRES` columns, a `% Mem` claim in `profiling.md`
  that the same page contradicts, the missing `mkdir -p logs` on the arrays page, the three
  array hints that don't assemble into a working script, and a `longsqueue` bonus that can
  truncate a student's `~/.bash_profile`.
- **These timings have never been observed in this format.** Record what actually happens and
  correct this file and the teaching plan afterwards.
