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
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put one up as soon as either is true — an instructor will come to you.

<svg viewBox="0 0 720 164" role="img" aria-labelledby="daymap-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:720px;height:auto;margin:1.5rem auto" font-family="'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="daymap-title">Day 2 arc — you are on step 3, submit.</title>
  <defs>
    <marker id="daymap-ah" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c2cad4"/></marker>
  </defs>
  <text x="70" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">profile</text>
  <text x="210" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">document</text>
  <text x="350" y="46" text-anchor="middle" font-size="17" font-weight="700" fill="#8C1515">submit</text>
  <text x="490" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">read logs</text>
  <text x="640" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">scale (Part 2)</text>
  <line x1="92" y1="80" x2="468" y2="80" stroke="#c2cad4" stroke-width="3"/>
  <line x1="512" y1="80" x2="618" y2="80" stroke="#c2cad4" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#daymap-ah)"/>
  <path d="M490,101 L490,124 Q490,130 484,130 L356,130 Q350,130 350,124 L350,103" fill="none" stroke="#c2cad4" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#daymap-ah)"/>
  <text x="420" y="150" text-anchor="middle" font-size="15" font-weight="400" fill="#6a7280">debug</text>
  <circle cx="70" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="70" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">1</text>
  <circle cx="210" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="210" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">2</text>
  <circle cx="350" cy="80" r="20" fill="#fff" stroke="#8C1515" stroke-width="3"/><text x="350" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8C1515">3</text>
  <circle cx="490" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="490" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">4</text>
  <circle cx="640" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="640" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">5</text>
</svg>

{: .note }
> Everything here runs from your clone with the environment active:
> `cd ~/yens-onboarding-2026 && source .venv/bin/activate`

---

Before you add a job to the queue, look at the queue.

{: .important }
> **Task:** Look at the live Slurm queue to see what jobs are waiting or running right now.

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
