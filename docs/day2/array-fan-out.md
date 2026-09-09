---
layout: default
title: "1. Watch an Array Fan Out"
parent: "Part 2 — Scale & Ship"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 1
permalink: /day2/array-fan-out/
---

# Watch an Array Fan Out

{: .note }
> Everything here runs from your clone with the environment active:
> `cd ~/yens-onboarding-2026 && source .venv/bin/activate`

---

{: .important }
> **Mandatory.** **Task:** Submit `slurm/hello_array.slurm` unchanged, and confirm you got
> four tasks and four separate logs out of one submission.

The repo ships two scripts that differ by exactly one line. Read them both:

```bash
cd ~/yens-onboarding-2026
diff slurm/hello.slurm slurm/hello_array.slurm
```

The array version adds `#SBATCH --array=1-4` and changes its log paths from `%j` to
`%A_%a`. That is the whole difference between one job and four.

Submit it:

```bash
mkdir -p logs
sbatch --reservation=class_day2 slurm/hello_array.slurm
squeue --me
```

You get **one** job ID back, but `squeue` shows four rows — `12345678_1` through
`12345678_4`. When they finish:

```bash
cat logs/hello_*_*.out
```

Four files, four different task numbers. One submission, four independent tasks, four
logs that never collided.


<svg viewBox="0 0 618 270" role="img" aria-labelledby="array-title array-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:616px;height:auto;margin:1.5rem auto" font-family="'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="array-title">One array script fans out into many tasks</title>
  <desc id="array-desc">A single submission script with the directive array equals 1 to N fans out into N independent tasks, numbered 1, 2, 3 and so on up to N. What each task does is determined by your code together with its array task ID.</desc>
  <!-- fan-out connectors (drawn first, behind boxes) -->
  <line x1="188" y1="129" x2="330" y2="37"  stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="188" y1="129" x2="330" y2="89"  stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="188" y1="129" x2="330" y2="141" stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="188" y1="129" x2="330" y2="221" stroke="#cbd3e0" stroke-width="1.5"/>
  <rect x="24" y="103" width="164" height="52" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="106" y="124" font-size="12.5" font-weight="700" fill="#2c3e50" text-anchor="middle">Slurm script</text>
  <text x="106" y="142" font-size="10.5" fill="#6a7280" text-anchor="middle" font-family="'Source Code Pro', ui-monospace, SFMono-Regular, Menlo, monospace">--array=1–N</text>
  <rect x="330" y="15" width="264" height="44" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="462" y="31" font-size="12" fill="#2c3e50" text-anchor="middle">task 1</text>
  <text x="462" y="46" font-size="8" fill="#6a7280" text-anchor="middle">determined by your code <tspan font-weight="700">and</tspan> SLURM_ARRAY_TASK_ID</text>
  <rect x="330" y="67" width="264" height="44" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="462" y="83" font-size="12" fill="#2c3e50" text-anchor="middle">task 2</text>
  <text x="462" y="98" font-size="8" fill="#6a7280" text-anchor="middle">determined by your code <tspan font-weight="700">and</tspan> SLURM_ARRAY_TASK_ID</text>
  <rect x="330" y="119" width="264" height="44" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="462" y="135" font-size="12" fill="#2c3e50" text-anchor="middle">task 3</text>
  <text x="462" y="150" font-size="8" fill="#6a7280" text-anchor="middle">determined by your code <tspan font-weight="700">and</tspan> SLURM_ARRAY_TASK_ID</text>
  <text x="462" y="188" font-size="16" fill="#6b7280" text-anchor="middle">⋮</text>
  <rect x="330" y="199" width="264" height="44" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="462" y="215" font-size="12" fill="#2c3e50" text-anchor="middle">task N</text>
  <text x="462" y="230" font-size="8" fill="#6a7280" text-anchor="middle">determined by your code <tspan font-weight="700">and</tspan> SLURM_ARRAY_TASK_ID</text>
  <!-- caption -->
  <text x="309" y="263" font-size="12.5" fill="#6a7280" text-anchor="middle">One submission becomes N independent tasks, each with its own task ID.</text>
</svg>

The task number is what makes this general. Every task runs the identical script, and `SLURM_ARRAY_TASK_ID` is the only thing that differs between them — so wherever the work needs to vary, you derive it from that number: which file to read, which row of a list to process, which parameter value to try.

{: .warning }
> **Counting from 1.** `--array=1-N` numbers the tasks 1, 2, … N. Slurm doesn't insist on that: numbering from 0 instead, so the tasks run 0 through N − 1, is equally valid. But starting at 1 is the convention used here, and it matters as soon as the task ID indexes something. In some languages a list of N items, `items`, is indexed 0 through N − 1, so a 1-based task ID has to be shifted — `items[task_id - 1]` rather than `items[task_id]`. Get it wrong and nothing complains up front: the first item is silently skipped, and the last task runs off the end of the list.
---
