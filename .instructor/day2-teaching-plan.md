# Day 2 — Teaching Run-of-Show (9:00–12:00)

**Instructor use only.** Not served by GitHub Pages. See `docs/agenda.md` for the
section table.

3 hours including two 10-minute breaks → ~160 min of teaching. Blocks around the breaks
are ≈ **60 / 50 / 50**.

## Before you start

Confirm the reservation is live — `scontrol show reservation class_day2` — and that the
recap items on `docs/day2/index.md` are actually in place for everyone: the venv, the
`.env`, and a working `extract_form_3_batch.py`. Anyone missing those cannot do the
profiling section, which everything after it depends on. Fix it in the recap slot.

## How to run it

| Section | Watch out for |
|---|---|
| Day 1 recap (5) | Keep it to the checklist. Resist reopening Day 1 discussions. |
| Compute Environments (15) | The two calculators carry it. Skip the long kitchen analogy — it was cut for time and the images are gone. |
| Profiling (25) | Two terminals side by side on the projector, big font. This is the section people remember. |
| The Slurm Scheduler (15) | Read the *live* queue, not a screenshot. A busy queue teaches `PD` better than any slide. |
| Writing & Submitting a Slurm Job (35) | **The most important 35 minutes of the two days.** Write the directives by hand. The two gotchas that bite everyone: `logs/` must exist before submit (Slurm resolves `--output` at submit time), and a fresh shell on the compute node has no venv. Do at least one `fix_me*.slurm` live — reading a failed job's `.err` is the skill they will need first. |
| Slurm with Claude (15) | Trimmed to the *global* `yen-slurm` skill only; the project plotting-skill half was cut. If short, demo rather than have everyone author one. |
| Job Arrays (25) | 5 min of concepts, then hands on keyboard. The off-by-one between `--array=1-10` and a zero-indexed CSV is the classic error — let them hit it. |
| Capstone (20) | Make them **write the estimate down before submitting**. The comparison against `sacct` is the entire lesson; without a recorded estimate there is nothing to compare. |
| Where to Go Next (5) | Slack, DARC email, RCpedia, and point at the Reference section for GPUs and local LLMs. |

## If you are running behind at 11:10

Demo the Claude-skill section instead of running it, and compress Job Arrays' concept
half to the single "100 sandwiches, 4 cooks" example. **Protect the capstone's estimate
step** — it is the one thing on Day 2 that changes how people size their own jobs
afterwards.

## Known gotchas

- `curl` on the Yens is 7.81.0, so `--json` does not exist. Use `-H` and `-d`.
- Slurm resolves `--output`/`--error` relative to the submit directory **at submit
  time**, so `logs/` must pre-exist. `slurm/hello.slurm` notes this in its header.
- `MaxArraySize` is 512 (`scontrol show config`), against 992 filings in
  `data/aws_links.csv` — that mismatch is the point of the optional full-scale
  assignment.
