# Canvas Modules — Yens Onboarding 2026

**Instructor use only.** Specification for the Canvas side of the course. None of this
exists yet; it is new authoring, not a port — the four-day course had no quizzes and no
pre-assignments.

Canvas carries **all** progress tracking. The course site has no quest log, no
checkboxes, and no leaderboard.

---

## 1 — Pre-work module (due the day before Day 1)

This module is load-bearing. It buys roughly 50 minutes of Day 1, which is what makes a
two-day version fit at all. Publish it at least a week ahead.

### Items

1. **Page: Welcome & what to expect** — the two-day shape, what to bring, the sticky-note protocol.
2. **Assignment (completion): Set up your accounts.**
   - [Claude for Education](https://uit.stanford.edu/service/claude)
   - [GitHub](https://github.com/signup)
   - Yens access — see [Access the Yens](https://rcpedia.stanford.edu/_getting_started/how_access_yens/)
3. **Assignment (completion): Install a terminal.** macOS → built-in Terminal. Windows → [Git Bash](https://git-scm.com/downloads).
4. **Assignment (graded, 1 pt): Confirm your Yens login.** ⭐ *The most important item in the module.*
   > SSH to the Yens and run `whoami` and `pwd`. Paste both commands and their output.
   Chase anyone who has not submitted this **48 hours before Day 1**. A login that fails
   on the morning of Day 1 costs that person most of Day 1, and it cannot be fixed in the
   room.
5. **Reading: [Command Line Basics](https://gsbdarc.github.io/yens-onboarding-2026/reference/command-line-basics/)** — do the exercises, don't just read.
6. **Reading: [Bulk File Operations](https://gsbdarc.github.io/yens-onboarding-2026/reference/bulk-file-operations/)** — generates its own dataset locally; nothing to download.
7. **Quiz: Command line basics** (8 questions, unlimited attempts, must score 8/8).

### Quiz question bank

1. You are in `/home/users/jdoe/projects`. What does `cd ../data` put you in? *(`/home/users/jdoe/data`)*
2. Which is an absolute path? *(`/scratch/users/jdoe/out.csv`)*
3. `ls *_2021_*` — which of these filenames does it match? *(the one with `_2021_` anywhere in it)*
4. What does `ls | wc -l` do? *(counts the files, by counting the lines `ls` prints)*
5. What is the difference between `>` and `>>`? *(overwrite vs. append)*
6. `ls */*.txt | cut -d'_' -f2 | sort | uniq -c` — what does this produce? *(a count of files per value of the second underscore-separated field)*
7. Why must you `sort` before `uniq -c`? *(`uniq` only collapses **adjacent** identical lines)*
8. In the pre-work dataset you found XOM's 2021 Form 4 files missing. Which command surfaced it? *(the `cut … | sort | uniq -c | sort -n` count, showing 8 where every other pair had 12)*

---

## 2 — Day 1 exit quiz (due that evening, 4 questions)

1. Why use a virtual environment instead of the system Python? What breaks without one?
2. `.env` and `.gitignore` — what does each protect against, and why do you need both?
3. You have a dataset under NDA. Which Stanford AI service may you use, and which may you not? *(Playground/Gateway are cleared for Low and Moderate risk; High Risk needs Carina/Nero. Cite the data-risk table.)*
4. Pydantic validated the model's reply and it passed. Name one kind of error that still gets through. *(A plausible but factually wrong value — validation checks shape and type, not truth.)*

---

## 3 — Day 2 exit quiz (due that evening, 4 questions)

1. Match each `#SBATCH` directive to what it controls: `--time`, `--mem`, `--cpus-per-task`, `--array`.
2. `squeue` shows your job as `PD`. What does that mean, and name two reasons for it.
3. You have 500 independent filings to process. Why is a job array better than a `for` loop in one job? Give two distinct reasons. *(Wall-clock: they run at once. Fault isolation: one failure costs one filing.)*
4. You profiled a 10-filing run at 4 min and 1.2 GB peak RAM. What `--time` and `--mem` would you request for 100 filings, and why is your answer not simply 10×? *(Time scales with the work; RAM largely does not, since one filing is in memory at a time. Add headroom to both.)*

---

## 4 — Optional extension assignments

Ungraded or extra credit. Each is self-contained and needs nothing from the other.

| Assignment | Page | Est. |
|---|---|---|
| LLM-as-a-judge | [/reference/llm-as-a-judge/](https://gsbdarc.github.io/yens-onboarding-2026/reference/llm-as-a-judge/) | ~1 hr |
| All 992 filings through an array, against the 512-task cap | [/reference/parallelization/](https://gsbdarc.github.io/yens-onboarding-2026/reference/parallelization/) + the Day 2 arrays section | ~1 hr |
| Local LLMs on the Yens GPUs | [/reference/why-local-llms/](https://gsbdarc.github.io/yens-onboarding-2026/reference/why-local-llms/), then [/reference/running-llms-on-the-yens/](https://gsbdarc.github.io/yens-onboarding-2026/reference/running-llms-on-the-yens/) | ~1.5 hr |
| Handling LLM failure modes | [/reference/llm-failure-modes/](https://gsbdarc.github.io/yens-onboarding-2026/reference/llm-failure-modes/) | ~45 min |

{: .note }
The local-LLM assignment needs the shared Ollama server running. See
`.instructor/ollama/` — and note the dry-run's caveats before you promise anything about
GPU-vs-CPU timings.

---

## Verifying the pre-work check works

Before you publish, submit a deliberately-broken `whoami` answer (wrong username, or
output from a laptop rather than a Yen) against the rubric and confirm you would catch
it. The whole point of that item is catching a broken account early; a check nobody
grades carefully is worse than no check.
