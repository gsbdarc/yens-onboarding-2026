---
layout: default
title: "★ GPUs"
parent: "Part 2 — Submit a Job Array"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 3
permalink: /day2/gpus/
---

# GPUs

{: .note }
> ⭐ **This whole page is bonus.** Do it once you have reached the
> [Part 2 Checkpoint]({{ '/day2/part2-checkpoint/' | relative_url }}) — and check whether
> anyone at your table is stuck first.

---

Asking for a GPU is two extra `#SBATCH` lines. The interesting part is not the syntax —
it's working out whether your job wanted one.

{: .important }
> **Task:** Submit a two-minute job that asks Slurm for one GPU, read back which GPU you
> landed on, and then decide whether today's extraction pipeline would run any faster on it.

---

## 1. Look at the GPU partition

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

## 2. Read the job script

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

## 3. Submit it and read what you got

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

## 4. The actual question: did your job want a GPU?

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

## Where to Go From Here

| Page | What it covers |
|---|---|
| [Why Run LLMs on the Yens?]({{ '/reference/why-local-llms/' | relative_url }}) | Local weights vs. the Gateway vs. a third party |
| [Running LLMs on the Yens]({{ '/reference/running-llms-on-the-yens/' | relative_url }}) | Serving a model on cluster hardware; GPU tiers and how to ask for one |
