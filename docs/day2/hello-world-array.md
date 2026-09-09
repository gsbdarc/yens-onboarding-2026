---
layout: default
title: "1. Hello World Array"
parent: "Part 2 — Submit a Job Array"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 1
permalink: /day2/hello-world-array/
---

# Hello World Array

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
> **Task:** Submit `slurm/hello_array.slurm` unchanged, and confirm you got
> four tasks and four separate logs out of one submission.

The repo ships two scripts that do the same trivial thing — one as a single job, one as an
array. Read them both:

```bash
cat slurm/hello.slurm
cat slurm/hello_array.slurm
```

You can spot the difference by eye, but let `diff` isolate it:

```bash
diff slurm/hello.slurm slurm/hello_array.slurm
```

```text
2c2
< #SBATCH --job-name=hello
---
> #SBATCH --job-name=hello-array
4,5c4,5
< #SBATCH --output=logs/hello_%j.out
< #SBATCH --error=logs/hello_%j.err
---
> #SBATCH --output=logs/hello_%A_%a.out
> #SBATCH --error=logs/hello_%A_%a.err
8a9
> #SBATCH --array=0-3
12c13
< echo "Hello, world!"
---
> echo "Hello, world! My task number is $SLURM_ARRAY_TASK_ID"
```

One directive is genuinely new — `--array=0-3` — and that is what turns one job into four.
The job name and the log paths change because of it.

{: .note }
> **`%j`, `%A` and `%a`.** Slurm substitutes these when it writes the log file. `%j` is the
> job ID, which is all a single job needs. An array needs two numbers: **`%A` is the
> array's job ID**, the same for all four tasks, and **`%a` is that task's own index**. So
> `hello_%A_%a.out` lands as `hello_12345678_0.out`, `hello_12345678_1.out` and so on —
> four separate files, rather than four tasks overwriting one.

Submit it:

```bash
mkdir -p logs
sbatch --reservation=class slurm/hello_array.slurm
squeue --me
```

You get **one** job ID back, but `squeue` shows four rows — `12345678_0` through
`12345678_3`. When they finish:

```bash
cat logs/hello_*_*.out
```

Four files, four different task numbers. One submission, four independent tasks, four
logs that never collided.

<svg viewBox="0 0 618 270" role="img" aria-labelledby="array-title array-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:616px;height:auto;margin:1.5rem auto" font-family="'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="array-title">One array script fans out into many tasks</title>
  <desc id="array-desc">A single submission script with the directive array equals 0 to N minus 1 fans out into N independent tasks, numbered 0, 1, 2 and so on up to N minus 1. What each task does is determined by your code together with its array task ID.</desc>
  <!-- fan-out connectors (drawn first, behind boxes) -->
  <line x1="188" y1="129" x2="330" y2="37"  stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="188" y1="129" x2="330" y2="89"  stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="188" y1="129" x2="330" y2="141" stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="188" y1="129" x2="330" y2="221" stroke="#cbd3e0" stroke-width="1.5"/>
  <rect x="24" y="103" width="164" height="52" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="106" y="124" font-size="12.5" font-weight="700" fill="#2c3e50" text-anchor="middle">Slurm script</text>
  <text x="106" y="142" font-size="10.5" fill="#6a7280" text-anchor="middle" font-family="'Source Code Pro', ui-monospace, SFMono-Regular, Menlo, monospace">--array=0–(N−1)</text>
  <rect x="330" y="15" width="264" height="44" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="462" y="31" font-size="12" fill="#2c3e50" text-anchor="middle">task 0</text>
  <text x="462" y="46" font-size="8" fill="#6a7280" text-anchor="middle">determined by your code <tspan font-weight="700">and</tspan> SLURM_ARRAY_TASK_ID</text>
  <rect x="330" y="67" width="264" height="44" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="462" y="83" font-size="12" fill="#2c3e50" text-anchor="middle">task 1</text>
  <text x="462" y="98" font-size="8" fill="#6a7280" text-anchor="middle">determined by your code <tspan font-weight="700">and</tspan> SLURM_ARRAY_TASK_ID</text>
  <rect x="330" y="119" width="264" height="44" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="462" y="135" font-size="12" fill="#2c3e50" text-anchor="middle">task 2</text>
  <text x="462" y="150" font-size="8" fill="#6a7280" text-anchor="middle">determined by your code <tspan font-weight="700">and</tspan> SLURM_ARRAY_TASK_ID</text>
  <text x="462" y="188" font-size="16" fill="#6b7280" text-anchor="middle">⋮</text>
  <rect x="330" y="199" width="264" height="44" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="462" y="215" font-size="12" fill="#2c3e50" text-anchor="middle">task N−1</text>
  <text x="462" y="230" font-size="8" fill="#6a7280" text-anchor="middle">determined by your code <tspan font-weight="700">and</tspan> SLURM_ARRAY_TASK_ID</text>
  <!-- caption -->
  <text x="309" y="263" font-size="12.5" fill="#6a7280" text-anchor="middle">One submission becomes N independent tasks, each with its own task ID.</text>
</svg>

The task number is what makes this general. Every task runs the identical script, and `SLURM_ARRAY_TASK_ID` is the only thing that differs between them — so wherever the work needs to vary, you derive it from that number: which file to read, which row of a list to process, which parameter value to try.
