---
layout: default
title: "GPUs"
parent: "Part 2 — Scale & Ship"
grand_parent: "Day 2 — The Cluster"
nav_order: 3
permalink: /day2/gpus/
---

# GPUs

{: .note }
> ⭐ **This whole page is bonus.** Do it once the capstone is done — and check whether
> anyone at your table is stuck first.

---

Every job you have submitted today asked for CPU cores and RAM. The Yens also have
**GPUs**, and asking for one is two extra `#SBATCH` lines. The interesting part is not the
syntax — it's working out whether your job wanted one in the first place.

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

The `nvidia-smi` output tells you the model and its VRAM. Look it up in the table on
[How to Run LLMs on the Yens]({{ '/reference/running-llms-on-the-yens/' | relative_url }}):

| GPU | VRAM |
|---|---|
| A30 | 24 GB |
| A40 | 48 GB |
| H200 | 141 GB |

**VRAM is the binding constraint on a GPU**, in the same way RAM was the binding constraint
when you profiled on a Yen. A model that does not fit in VRAM does not run at all — it
doesn't run slowly.

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
> No — and not by a little. A GPU accelerates *arithmetic*. Your job does almost none: it
> makes an HTTP request, waits, parses the reply, writes a file. The GPU would sit idle at
> 0% utilisation for the entire run while you held it out of the queue, and the job would
> take exactly as long as it did on a CPU core.
>
> This is the same distinction you drew when profiling — **I/O-bound vs. CPU-bound** — and
> it is the reason to profile before requesting. Asking for hardware you don't need makes
> your job wait longer in the queue *and* blocks someone whose job actually needs it.
>
> </details>

GPUs earn their keep when the work really is arithmetic-heavy and parallel: training or
fine-tuning a model, large matrix operations, and — the case most relevant to today —
**running an LLM's weights yourself** instead of calling someone else's API.

---

## Where to Go From Here

| Page | What it covers |
|---|---|
| [Why Run LLMs on the Yens?]({{ '/reference/why-local-llms/' | relative_url }}) | Local weights vs. the Gateway vs. a third party |
| [Running LLMs on the Yens]({{ '/reference/running-llms-on-the-yens/' | relative_url }}) | Serving a model on cluster hardware; GPU tiers and how to ask for one |

---

## What You Learned

- **Asking for a GPU** is `--partition=gpu` plus `--gres=gpu:1` — and forgetting `--gres`
  fails quietly rather than loudly.
- **VRAM is the binding constraint**, the way RAM was on a CPU node.
- **GPUs are scarce and contended**, so a specific request queues longer than a general one.
- **An I/O-bound job gains nothing from a GPU.** Profiling first is what tells you which
  kind of job you have.
