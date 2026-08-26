# Instructor Setup — Yens Onboarding 2026

Run these before the course. One-time per cohort unless noted.

Much less than the four-day version needed: dropping the Day 1 grimoire challenge
removed the dataset generation, the Google Drive hosting, and the `/scratch/shared`
staging entirely. Dropping the leaderboard removed the fork-roster sync.

---

## Two weeks before

- [ ] **Book the Slurm reservation.** Day 2 needs a reservation named **`class_day2`**,
      covering 9:00–12:00 on Day 2, sized for the cohort.
      **Every `sbatch` and `srun` in the Day 2 pages hardcodes
      `--reservation=class_day2`** — including the job-arrays section and the capstone.
      If the name differs, every command in the docs is wrong. Confirm with:
      ```bash
      scontrol show reservation class_day2
      ```
- [ ] **Email the two pre-work items** — a GitHub account and Claude via Stanford. See
      `docs/prework.md`. Send it at least a week out: Claude approval goes through
      ServiceNow, and Yens access can take days.
- [ ] **Request a shared Stanford AI API Gateway key** for the cohort, or confirm each
      attendee can request their own. See `docs/day1/stanford-ai-services.md`.

## One week before

- [ ] **Chase Yens access by name.** There is no LMS to collect a completion check this
      year, so ask the cohort directly who does *not* yet have an account. This is the
      highest-value thing you do all week — a missing account is unrecoverable inside a
      3-hour morning, and it is the only prereq that is.
- [ ] **Walk both days end to end on the Yens yourself**, against the reservation. See
      *Dry run* below. Do not skip this; the four-day course shipped with a dead link and
      a `.slurm` file the docs told students to edit that did not exist.

## Day-of checklist

- [ ] `scontrol show reservation class_day2` returns an active reservation (Day 2)
- [ ] Course site loads: <https://gsbdarc.github.io/yens-onboarding-2026/>
- [ ] The Gateway key works — make one live API call from a Yen
- [ ] `ml claude-code` and `ml gh-cli` both resolve
- [ ] Sticky notes on every table (green + red)
- [ ] Roster of who has *not* done the pre-work, so you can seat a helper near them

---

## Dry run

Walk the whole thing as a student would, on the Yens, with a clock running. Record what
you find the way `ollama/dry-run-2026-08-02.md` does — including what you did **not**
verify. That file is the model: its honest "not verified" list is why we know the
GPU-vs-CPU timing claim was never measured.

**Day 1:** SSH → fork → clone → `gh auth` → branch/commit/push → `ml claude-code` and a
real task → `module load python` → venv + `requirements.txt` → Potion Brawl rebuild →
`.env` → the three staged extraction scripts → `extract_form_3_batch.py` over 10 filings.

**Day 2:** profile `mystery_script.py` in two terminals → profile the batch script →
`squeue`/`sinfo` → write a `.slurm` by hand → `sbatch --reservation=class_day2` →
read logs → all three `fix_me*.slurm` → author the `yen-slurm` skill → an array job →
`sacct` for actuals → **the GPU bonus** (`sbatch slurm/gpu_check.slurm`, no reservation
flag; confirm `nvidia-smi` output lands in `logs/gpu_check_*.out`).

**Timing.** Time each section against `.instructor/agenda.md`. If a block overruns, move an
exercise to `docs/reference/` — do not shave the breaks. Two 10-minute breaks in a 3-hour
morning is already the minimum on **Day 1**. **Day 2 has no scheduled breaks at all** —
tables break inside the work blocks — so watch for a room that has not moved in an hour and
call one anyway.

---

## Answer keys

Not served by GitHub Pages.

| File | Covers |
|---|---|
| `capstone.key.md` | Day 2 capstone — which resources scale with the filing count, and why |
| `documenting-pipeline.key.md` | A worked README for the extraction pipeline |
| `yen-slurm-skill.key.md` | Reference `SKILL.md` for the global `yen-slurm` skill; project vs. global scope |
| `storage_pantry_key.ipynb` | Worked analysis of the Yens `yenstop` snapshot (Reference page) |

No key exists for the Day 1 capstone — it has no single right answer, and the point is
the README and the failure inspection rather than a target output.

---

## Optional: the local-LLM assignment

Only needed if you want to run the local-LLM material live. See `ollama/`, and read
`ollama/dry-run-2026-08-02.md` first — particularly the "not verified" section and the
note that `ensure_ollama_server.sh` holds the GPU for its full `WALLTIME` whether it is
being queried or not.
