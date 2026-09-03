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

**Lectures are concepts and graphics. Anything with a keyboard — or any syntax — stays in
the work block.**

Every slide answers one question: *what is this, and why do we do it.* No commands, no flags,
no script anatomy. The website carries the how, and students read it during the block while we
circulate.

Two things follow from that.

**First, the material is already written.** These chunks of Day 2 are pure concept sitting
*inside* the work blocks today, competing with hands-on time:

| Concept prose currently in a work block | Goes to |
|---|---|
| `compute-environments.md` — the whole page bar two widget bonuses | Lecture 1 |
| `slurm-scheduler.md:13–91` — ~80 lines of concept before the first command | Lecture 1 |
| `profiling.md:170–174` — the Profiling / Serial / Parallel definitions box | Lecture 1 |
| `slurm-with-claude.md:20–24` — the three-step skill pattern | Lecture 1 |
| `parallelization.md:16–120` — independence and "embarrassingly parallel" | Lecture 2 |
| `job-arrays.md:43–110` — fan-out, and arrays as *one* way to parallelize | Lecture 2 |
| `why-local-llms.md:98–142` — the local vs. Gateway vs. third-party framework | Lecture 2 |

Moving these to the front of the room recovers roughly **20 minutes of hands-on time**.

**Second, use the diagrams — the repo has 34 of them, four animated.** Of the 13 slides
below, **9 use an SVG that already exists**, 2 are simple tables, and only 2 need a new
graphic drawn. Every reference below was checked against the file.

Nothing is deleted from the website. The slides are the spine; the pages are the reference.

---

## Lecture 1 (9:00–9:20) — "Where your code runs, and who decides"

**Seven concept slides, ~3 min each.** Order follows the natural narrative: what the machine
is → how you measure it → who allocates it → what happens when it breaks.

Two merges keep this inside 20 minutes: *profiling — what it means* and *why we do this* are
one slide plus its payoff (2 and 3), and *interactive vs Slurm* and *what is Slurm* are a
single arc (4).

| # | Concept — *what is it, why do we do it* | Min | Graphic |
|---|---|---|---|
| 1 | **What is the cluster?** 17 nodes, one shared file system, and you are a guest on shared hardware | 3 | `day1/connect-to-the-yens.md:52` — SSH → interactive tier → scheduled tier. Storage tiers at `:156`; `server-hardware-cpu-ram.png` for scale |
| 2 | **What is profiling?** Measuring what your code actually consumes — time, cores, RAM — instead of guessing | 3 | `compute-environments.md:75` — disk → RAM → CPU, **animated** |
| 3 | **Why do we profile?** You have to declare what you need. Ask too little and the job dies; ask too much and you wait longer and waste shared capacity. Measuring is the only way to know | 3 | **Draw this one** — 3 panels: *too little → job dies* · *too much → wait + waste* · *measured → right-sized*. Trivial to draw, and this is the hinge slide |
| 4 | **Interactive Yens vs. Slurm — why use one over the other?** Shared-now vs. dedicated-later. And what Slurm *is*: an orchestrator you declare your needs to, which decides when and where | 3 | `slurm-scheduler.md:55` — submit from a shared Yen → scheduler → dedicated compute node, **animated** |
| 5 | **What are partition limits, and why do they exist?** Different queues, different caps. Caps are a fairness mechanism, not bureaucracy | 2 | Small table: *partition · what it's for · has a time cap · has a per-user cap.* **Concept only — no numbers** |
| 6 | **What is debugging a failed job, and why does it matter?** A job that vanished is not a job that worked. The cluster writes down what went wrong — your job is to go read it | 3 | `slurm-scheduler.md:124` — the job lifecycle, PD → R → done → **logs**. The logs box at the end is the whole slide |
| 7 | **What is a skill, and why capture one?** You just worked out the conventions the hard way. Write them down once and Claude follows them next time | 2 | `slurm-with-claude.md:44` — global `~/.claude/` vs. project `.claude/` |

**Close with the preview** — one line, no slide: *by 10:30 you will have submitted a job, read
its logs, and fixed a broken one.* Self-paced work needs a stated finish line.

### Notes for delivery

- **Slide 3 is the hinge of the morning.** It is what makes profiling feel necessary rather
  than academic, and every `#SBATCH` number in block 1 traces back to believing it.
  `slurm-scheduler.md:88–89` is this slide already written as one sentence.
- **Slide 5 needs no real numbers**, which is the point of keeping it conceptual — the docs
  defer to RCpedia for actual caps, and those drift. Teach that caps exist and where to look
  them up.
- **Say out loud, not on a slide:** login node vs. compute node (one sentence at slide 4 — it
  causes more downstream confusion than anything else on Day 2); how to edit a file on the
  Yens; and that `SUNetID`/`JOBID` in the docs are placeholders, not literal text.
- **If you overrun**, compress slide 1 — cluster hardware is the most familiar material in the
  room. Protect 3 and 6.

---

## Lecture 2 (10:30–10:50) — "Scaling out"

**Six concept slides.** The GPU half is two slides rather than one: "what type of LLM work"
is a genuinely separate idea from "what hardware exists", and it happens to be the
best-documented content in the repo.

| # | Concept — *what is it, why do we do it* | Min | Graphic |
|---|---|---|---|
| 1 | **What is parallelization, and when does it help?** Only when the pieces are **independent**. It never makes one task faster — it makes many finish sooner | 4 | `parallelization.md:23` (one burner) → `:63` (four burners), **animated**. The grilled-cheese analogy is the best conceptual graphic in the repo |
| 2 | **What shapes does parallelism come in?** One job many cores · many jobs one core · both | 3 | Four existing diagrams: `parallelization.md:169` · `:209` · `:255` · `:303` |
| 3 | **What is a Slurm array?** One script, submitted once, run as many independent tasks — **one way to parallelize, not the only one** | 3 | `job-arrays.md:80` — one array script fans out into many tasks |
| 4 | **Why estimate before you run?** Committing to a number first is what turns a run into a measurement | 2 | No existing graphic — reuse the Day 2 map, or skip the visual |
| 5 | **What are GPUs for, and what do we have?** Arithmetic-heavy parallel work — and **VRAM is the ceiling**: it decides which models you can load *at all* | 4 | The three-tier table at `running-llms-on-the-yens.md:150–154` — A30 24 GB · A40 48 GB · H200 141 GB |
| 6 | **Where does LLM work belong?** Local weights vs. the Stanford Gateway vs. a third-party API | 4 | `why-local-llms.md:27` (calling an API sends your data away) → `:63` (running it yourself keeps it local), **both animated** |

**Close with the preview:** *100 filings, then check yourself against `sacct`.*

### Notes for delivery

- **Slide 3's framing is already in the docs** at `job-arrays.md:12` — "there are a few ways
  to run work in parallel on a cluster; for embarrassingly parallel jobs like ours, a standard
  tool is a Slurm job array." Keep that hedge; arrays are not the only answer.
- **Name the off-by-one on slide 3, and do not solve it.** Tasks count from 1, Python lists
  from 0. Warning makes it recognisable when it bites in the block; defusing it removes the
  lesson.
- **Slide 6 needs almost no authoring** — `why-local-llms.md:129–134` is a ready-made
  three-way table (where your data goes · cost · which models · best for), with the rule of
  thumb at `:142`: *restricted data → local, no exceptions.* Its sharpest point is at
  `:109–113`: the frontier proprietary models cannot run on the Yens at all, so the real
  choice is never "any model, local or cloud" — it is a proprietary model in the cloud, or an
  open-weight model you run yourself. Pair it with the counterweights at `:121` (the API still
  wins on capability) so it does not read as a sales pitch.
- **If you overrun**, merge slides 1 and 2.

### ⚠ Two limits on the GPU slides

**1. "What models fit in 24 / 48 / 141 GB" does not exist in the repo.** The tier table says
only "small models, embeddings" / "mid-size models" / "large models" — no model names, no
parameter counts. The one VRAM-to-model claim anywhere is an instructor script comment
(`llama3.2:1b` ≈ 1.3 GB quantised, fits an A30).

If you want a concrete "what fits" slide, you are authoring it, and the honest version has to
say **weights are not the whole story: context length consumes VRAM too.** The dry-run notes
flag exactly this — the 262144-token default context was derived on a 141 GiB H200, and a
24 GiB A30 defaults far lower. SEC filings are long, so this is the trap most likely to bite
someone later. The safer slide keeps to the concept: *VRAM is the ceiling, here are the three
tiers*, and promises no specific model.

**2. No performance claim is supportable.** `.instructor/ollama/dry-run-2026-08-02.md:59–63`
states it plainly: *"No GPU-vs-CPU timing. The runtime contrast the demo rests on is
unmeasured."* The repo holds exactly one tokens-per-second figure — 13 tok/s — and it is
**CPU-only**, from a before/after bug fix, not a GPU comparison. There are zero GPU figures.
So no "N× faster", no tok/s, no latency numbers. `query_server.py` exists to measure this; the
measurement has never been run.

Three smaller traps if a command does reach a slide: node names and per-node counts
(`yen-gpu1` 4×A30, `yen-gpu2/3` 4×A40, `yen-gpu4` 2×H200 = 14) are **instructor-only** and
student pages have just the tier table and "14 in total" — and 14 is a snapshot to re-check
with `sinfo -p gpu`; `curl --json` does **not** work on the Yens (curl 7.81.0, the flag landed
in 7.82.0); and the one verified chat request used `llama3.2:3b` while every student-facing
default is `llama3.2:1b`.

### Two things to be deliberate about

**Skills (L1 #7) and GPUs (L2 #5–6) are Bonus-only exercises** — about 9 of the 40 lecture
minutes go to material most students will not practise today. That is coherent: skills-as-demo
was the original Day 2 treatment, and GPUs are explicitly a preview. But frame both the same
way out loud: *"you won't do this today — here's what it's for and where it lives."*

**Slide 4 exists to protect the capstone.** The capstone is a Main exercise whose whole
discipline is *write your estimate down before you submit*; without two minutes of concept
here, that instruction arrives cold on the page 40 minutes later. It is the cheapest insurance
on the day — and the first thing to cut if you want the GPU time back.

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
