---
layout: default
title: "4. Peek at the Queue"
parent: "Part 1 — Profile & Submit a Job"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 4
permalink: /day2/peek-at-the-queue/
---

# Peek at the Queue

{: .note }
> Everything here runs from your clone with the environment active:
> `cd ~/yens-onboarding-2026 && source .venv/bin/activate`

---

Before you add a job to the queue, look at the queue.

{: .important }
> **Mandatory.** **Task:** Look at the live Slurm queue to see what jobs are waiting or running right now.

```bash
squeue
```

Look at the columns:
- **JOBID** — unique ID for each job
- **PARTITION** — which partition (queue) the job was submitted to — each partition has different node types, time limits, and resource caps; see the [current partitions and their limits](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits)
- **ST** — status: `R` = running, `PD` = pending (waiting in queue for resources)
- **TIME** — how long the job has been running
- **NODELIST** — which compute node it landed on

There is also a shorthand to filter to just your jobs:

```bash
squeue --me
```

You can also filter by partition — for example, to see only GPU jobs:

```bash
squeue -p gpu
```

Every `PD` job is waiting for a node with the resources it requested. When Slurm finds a matching node — it runs.

---


---

---

<details markdown="1">
<summary>⭐ Bonus — if you finished early</summary>

**Bonus — Add a `longsqueue` alias**

The default `squeue` output is sparse. Pass a custom format to see what each job actually
requested — CPU cores, memory, and time limit:

```bash
squeue -o "%.18i %.9P %.8j %.8u %.8T %.10M %.10l %.4C %.7m %.15R"
```

The columns are: job ID, partition, job name, user, state, time elapsed, time limit, CPU
cores requested, memory requested, and reason/node.

To keep it, append an alias. The quoted heredoc (`<<'EOF'`) means nothing inside needs
escaping — paste the whole block at once:

```bash
cat >> ~/.bash_profile <<'EOF'
alias longsqueue='squeue -o "%.18i %.9P %.8j %.8u %.8T %.10M %.10l %.4C %.7m %.15R"'
EOF
source ~/.bash_profile
```

Now run `longsqueue`. If the alias comes back "not found", check the tail of the file with
`tail -3 ~/.bash_profile` before appending again.


**Bonus — Inspect any job with `scontrol`**

Pick any job from `squeue` and look up its full details:

```bash
scontrol show job JOBID
```

Find **NumCPUs** (cores requested), **mem=** (RAM requested) and **TimeLimit**. This works
on any job — yours or someone else's — as long as it is still queued or running.


**Bonus — Compare partitions**

Run `sinfo -p gpu` and `sinfo -p normal` to compare node counts and time limits. `sinfo`
does not show the per-user resource **caps** — those come from each partition's QoS, so
check `sacctmgr show qos gpu` against `sacctmgr show qos normal` (or the
[current partitions and their limits](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits)).
When would you request one over the other?


---

---

## Before You Move On

Head to the [Part 1 Checkpoint]({{ '/day2/part1-checkpoint/' | relative_url }}) — six
checks, about five minutes. Everything in Part 2 assumes they pass, so run it while there
is still someone circulating who can help with whatever is broken.

</details>
