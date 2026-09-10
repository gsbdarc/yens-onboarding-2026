---
layout: default
title: "4. Scale"
parent: "Part 2 — Submit a Job Array"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 4
permalink: /day2/scale/
---

# Scale

{: .note }
> 🔴 **Red sticky** = I need help. Put it up the moment you are stuck — an instructor will
> come to you.
>
> 🟢 **Green sticky** = I have passed the checkpoint. Feel free to go back to the bonus
> exercises if you still have time, or help your table.

<svg viewBox="0 0 720 164" role="img" aria-labelledby="daymap-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:720px;height:auto;margin:1.5rem auto" font-family="'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="daymap-title">Day 2 arc — you are on step 5, scale (Part 2).</title>
  <defs>
    <marker id="daymap-ah" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c2cad4"/></marker>
  </defs>
  <text x="70" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">profile</text>
  <text x="210" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">document</text>
  <text x="350" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">submit</text>
  <text x="490" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">read logs</text>
  <text x="630" y="46" text-anchor="middle" font-size="17" font-weight="700" fill="#8C1515">scale (Part 2)</text>
  <line x1="92" y1="80" x2="608" y2="80" stroke="#c2cad4" stroke-width="3"/>
  <path d="M490,101 L490,124 Q490,130 484,130 L356,130 Q350,130 350,124 L350,103" fill="none" stroke="#c2cad4" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#daymap-ah)"/>
  <text x="420" y="150" text-anchor="middle" font-size="15" font-weight="400" fill="#6a7280">debug</text>
  <circle cx="70" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="70" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">1</text>
  <circle cx="210" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="210" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">2</text>
  <circle cx="350" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="350" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">3</text>
  <circle cx="490" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="490" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">4</text>
  <circle cx="630" cy="80" r="20" fill="#fff" stroke="#8C1515" stroke-width="3"/><text x="630" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8C1515">5</text>
</svg>

{: .note }
> Everything on this page runs from your clone, with the environment active:
>
> ```bash
> cd ~/yens-onboarding-2026
> source .venv/bin/activate
> ```

{: .important }
> **Task:** Run **all ~992 filings** through an array — now that your tasks are safe to
> rerun — then write down what the full run cost and push it.

`data/aws_links.csv` lists **992** filings. You have run 100 of them. Scaling to all of them
looks like one number in one directive — except that it is not, and finding out why is the
exercise.

You are doing this now, rather than earlier, because of
[3. Make Your Tasks Rerun-Safe]({{ '/day2/rerun-safe-tasks/' | relative_url }}). At 992
tasks something will fail — a node reboots, the API times out — and rerun-safety is what
turns that from "start again" into "resubmit and it picks up what is missing."

### 1. Try the obvious thing, and read the error

```bash
sbatch --reservation=class --array=0-991 slurm/extract_array.slurm
```

Slurm refuses. `MaxArraySize` on the `normal` partition is **512**, and what it caps is the
task *index*, not the count — so the highest index you may use is **511**, and an array
holds at most 512 tasks. Check the ceiling yourself:

```bash
scontrol show config | grep MaxArraySize
```

The catch is that the cap applies to *every* submission, so you cannot just pick up where
the first array stopped — there is no second window of higher indices to move into.
Reaching filing 991 means submitting an index at or below 511 and mapping it upward.

### 2. Pick a way round it

Two options, and they are different tradeoffs:

- **Give each task more than one filing.** The cleaner of the two, because nothing needs
  offsetting. Keep the array small — `--array=0-99` — and have each task handle ten
  filings, `filings[task_id * 10 : task_id * 10 + 10]`. Fewer, longer tasks and less
  scheduler overhead; the per-task `--time` now has to cover ten API calls, not one. 992
  is not a multiple of ten, so the last task gets two — the slice handles that on its own.

  ```bash
  sbatch --reservation=class --array=0-99 slurm/extract_array.slurm
  ```
- **Submit two arrays.** Both have to start at 0, so the second one has to be *told* which
  slice is its own:

  ```bash
  sbatch --reservation=class --array=0-511 slurm/extract_array.slurm

  sbatch --reservation=class --array=0-479 \
         --export=ALL,OFFSET=512 slurm/extract_array.slurm
  ```

  and the `.slurm` adds it on before handing over. `ALL` keeps the rest of your
  environment, and the `:-0` default leaves the first submission working unchanged:

  ```bash
  python scripts/extract_array.py $(( SLURM_ARRAY_TASK_ID + ${OFFSET:-0} ))
  ```

### 3. Size it — and work out what it costs

Whichever route you picked, the per-task numbers change: ten filings per task means ten API
calls inside one `--time`, not one. Re-size the directives before you submit — and this time
you are not guessing, because
[2. Scale the Loop to an Array]({{ '/day2/loop-to-array/' | relative_url }}) left you real
`sacct` numbers for one filing to build on.

{: .warning }
> **992 API calls is real money, and the whole room is submitting at once.** Work the cost
> out from your 100-filing run before you submit, and **check the number with an instructor**.
> This is the one job today where getting the arithmetic wrong is expensive rather than
> merely slow.

### 4. Run it

Make sure `logs/` exists, then submit with whichever command matches the route you picked
in step 2 — one `sbatch` for ten-filings-per-task, two for the offset route:

```bash
mkdir -p logs
watch squeue --me
```

When it drains, count what landed:

```bash
ls results/*.json | wc -l        # aiming for 992
```

Short of 992? That is what rerun-safety is for — resubmit the same array. Finished tasks
find their output and exit immediately, so only the gaps are redone.

### 5. Document it, and push

In `README.md`, next to your 100-filing numbers, record what the full run actually took:
per-task time and memory from `sacct`, total wall-clock, how many tasks you split it into,
and which of the two routes you chose and why.

```bash
sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS
```

Then commit it. Ask Claude Code to handle it:

```
> Add and commit my array scripts and README changes with a message like "Day 2: all 992 filings through an array", then push to my fork.
```
