---
layout: default
title: "4. Capstone"
parent: "Part 2 — Submit a Job Array"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 4
permalink: /day2/capstone/
---

# Capstone — Estimate, Submit, Compare

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put one up as soon as either is true — an instructor will come to you.

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

---

{: .important }
> **Task:** Estimate what a 100-filing run will cost in CPU, RAM, and time —
> **write the estimate down first** — then run it and check yourself against `sacct`.

All morning you have profiled and run **10 filings**. Scale to **100** — and commit to what
it will need *before* you run it.

### 1. Estimate the resources for 100 filings — and write it down first

You're running the same loop, just over 100 files instead of 10. Think about what **CPU**, **RAM**, and **time** it will take. Open `scripts/extract_form_3_batch.py` (or have Claude read it) and reason it out:

> Look at `scripts/extract_form_3_batch.py` and my Profiling README (the 10-filing numbers) and help me estimate the CPU, RAM, and wall-clock time this needs for 100 filings.

**Before you submit anything**, write in your `README.md`: which resources you think will **scale** with the number of filings processed and which will stay about flat — and **why** — along with your CPU, RAM, and wall-clock **estimate for 100**. Committing to a number *before* you run it is the whole point.

### 2. Write a Slurm script for the batch

You already built `slurm/extract_form_3_batch.slurm` for **10 filings**. Two changes:

1. In `scripts/extract_form_3_batch.py`, set `NUM_FILINGS = 100`.
2. In the `.slurm`, re-tune `--time`, `--mem` and `--cpus-per-task` to **your estimates for
   100**, and keep the email-notification lines so you get the completion summary.

{: .warning }
> **Confirm the edit took before you submit.** The filing count lives inside the Python
> script, not on the `sbatch` command line — so if the edit does not save, the job still
> succeeds and still emails you, having processed ten filings while holding a request
> sized for a hundred. Your "actuals" then describe the wrong run, and the honest
> conclusion is that you over-estimated by 10×.
>
> ```bash
> grep NUM_FILINGS scripts/extract_form_3_batch.py
> ```
>
> It should say `100`. Clear out the old results too, so what lands in `results/` is from
> this run only: `rm -f results/*.json`.

### 3. Submit and confirm it ran

{: .note }
> **Today only:** keep the class reservation flag — `--reservation=class_day2` — on your `sbatch` so the job runs on the reserved nodes. Drop it for your own work after today.

```bash
sbatch --reservation=class_day2 \
  slurm/extract_form_3_batch.slurm
squeue --me
```

Wait for the completion email. From it — and from
`sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS` — note **how long it took** and **how
much CPU and RAM it actually used** against what you requested.

Check you measured what you think you measured:

```bash
ls results/*.json | wc -l        # should be 100, not 10
```

### 4. Compare actual vs. your estimate

Back in `README.md`, next to the estimate you wrote in step 1, add the **actual** numbers from the email and `sacct`, and note whether you **over- or under-estimated** each resource — and by how much. That comparison is the payoff; next time you'll estimate better.

### 5. Commit and push from the Yens

Ask Claude Code to handle it:

> Add and commit `slurm/extract_form_3_batch.slurm` and my README changes with a message like "Day 2 Capstone: 100-filing batch", then push to my fork.

---

---

<details markdown="1">
<summary>⭐ Bonus — try a GPU</summary>

Asking for a GPU is two extra `#SBATCH` lines. The interesting part is not the syntax —
it's working out whether your job wanted one.

{: .important }
> **Task:** Submit a two-minute job that asks Slurm for one GPU, read back which GPU you
> landed on, and then decide whether today's extraction pipeline would run any faster on it.

---

### 1. Look at the GPU partition

You already read the queue for the `normal` partition. Do the same for `gpu`:

```bash
sinfo -p gpu
sinfo -p normal
```

There are far fewer GPU nodes than CPU nodes, and the QoS limits differ too:

```bash
sacctmgr show qos gpu
sacctmgr show qos normal
```

{: .note }
> **Your job will probably queue, and that is the lesson.** GPUs are the scarcest resource
> on the cluster — there are 14 in total, against hundreds of CPU cores per node. Today's
> class reservation covers the `normal` partition, **not** the GPU nodes, so this job waits
> in line with everyone else's. Keep it short.

---

### 2. Read the job script

`slurm/gpu_check.slurm` is already in your repo. Open it — it is the shortest Slurm script
you have seen today, and two directives are new:

```bash
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
```

`--gres` is "generic resource". `gpu:1` asks for one GPU on the node you land on. Miss it
out and you get a slot on a GPU node with **no GPU allocated to you** — the job runs,
`nvidia-smi` finds nothing, and the failure is quiet. That is the mistake worth knowing
about.

Notice what is *not* in the script: `--reservation=class_day2`. Every other `sbatch` today
carried it; this one must not.

---

### 3. Submit it and read what you got

```bash
mkdir -p logs
sbatch slurm/gpu_check.slurm
squeue --me
```

Once it clears the queue:

```bash
cat logs/gpu_check_*.out
```

The `nvidia-smi` output tells you which model you landed on and how much VRAM it has. The
per-tier numbers are in
[Running LLMs on the Yens]({{ '/reference/running-llms-on-the-yens/' | relative_url }}).

Note what your own output says, because **VRAM is the binding constraint on a GPU** the way
RAM was on a Yen node: a model that does not fit does not run slowly, it does not run.

To ask for a specific model, add `--constraint="GPU_MODEL:A40"`. Be aware that the more
specific you are, the longer you wait.

---

### 4. The actual question: did your job want a GPU?

Now check what it cost you:

```bash
sacct -j JOBID --format=JobID,State,Elapsed,ReqTRES
```

Then think back to your profiling numbers from this morning. You measured
`extract_form_3_batch.py` and found `real` far larger than `user` — the script spent almost
all its wall-clock time **waiting on the network** for the API to answer, not computing.

{: .important }
> **So: would a GPU have made your extraction job faster?**
>
> <details markdown="1">
> <summary>Think about it, then check</summary>
>
> No — and not by a little. Your `real` ≫ `user` measurement from this morning says the job
> waits on the network rather than computing, and a GPU only accelerates computing. It
> would sit at 0% utilisation for the whole run while you held it out of a queue somebody
> else needs.
>
> </details>

---

### Where to Go From Here

| Page | What it covers |
|---|---|
| [Why Run LLMs on the Yens?]({{ '/reference/why-local-llms/' | relative_url }}) | Local weights vs. the Gateway vs. a third party |
| [Running LLMs on the Yens]({{ '/reference/running-llms-on-the-yens/' | relative_url }}) | Serving a model on cluster hardware; GPU tiers and how to ask for one |

</details>
