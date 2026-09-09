---
layout: default
title: "2. Profile the Batch Script"
parent: "Part 1 — Profile & Submit a Job"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 2
permalink: /day2/profile-batch-script/
---

# Profile the Batch Script

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put one up as soon as either is true — an instructor will come to you.

<svg viewBox="0 0 720 164" role="img" aria-labelledby="daymap-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:720px;height:auto;margin:1.5rem auto" font-family="'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="daymap-title">Day 2 arc — you are on step 1, profile.</title>
  <defs>
    <marker id="daymap-ah" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c2cad4"/></marker>
  </defs>
  <text x="70" y="46" text-anchor="middle" font-size="17" font-weight="700" fill="#8C1515">profile</text>
  <text x="210" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">document</text>
  <text x="350" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">submit</text>
  <text x="490" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">read logs</text>
  <text x="630" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">scale (Part 2)</text>
  <line x1="92" y1="80" x2="608" y2="80" stroke="#c2cad4" stroke-width="3"/>
  <path d="M490,101 L490,124 Q490,130 484,130 L356,130 Q350,130 350,124 L350,103" fill="none" stroke="#c2cad4" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#daymap-ah)"/>
  <text x="420" y="150" text-anchor="middle" font-size="15" font-weight="400" fill="#6a7280">debug</text>
  <circle cx="70" cy="80" r="20" fill="#fff" stroke="#8C1515" stroke-width="3"/><text x="70" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8C1515">1</text>
  <circle cx="210" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="210" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">2</text>
  <circle cx="350" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="350" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">3</text>
  <circle cx="490" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="490" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">4</text>
  <circle cx="630" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="630" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">5</text>
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
> **Task:** Profile the real batch script on 10 filings using the same two-terminal technique.

Now apply the same technique to a **real workload**. `scripts/extract_form_3_batch.py` — committed in the repo, so everyone has it — runs the same Form 3 extraction you did on Day 1 with `extract_form_3_one_file.py`, but loops over many filings instead of one. Process **10 filings** and profile it. (If you finished the Day 1 capstone and have your own batch script, profile that one instead — the numbers are what matter, not whose script produced them.)

First, open the script so you know what you're profiling — `cat scripts/extract_form_3_batch.py` (or open it in JupyterHub).

<details markdown="1">
<summary>💡 Hint — what the script does</summary>

It loops over the filings in `data/aws_links.csv`, calls the API for each, and writes one JSON per filing to `results/`.

</details>

The script is set to process **10 filings** (see `NUM_FILINGS` near the top — kept small so a stray run doesn't fire hundreds of paid API calls).

**First run — watch the load.** Terminal 2 (start this first):
```bash
watch userload
```

Terminal 1 — run it and note the `real`, `user`, and `sys` times when it finishes:
```bash
time python scripts/extract_form_3_batch.py
```

**Second run — watch the processes.** Switch Terminal 2 to `htop`, then run the script once more so you can see the processes live:

Terminal 2:
```bash
htop -u SUNetID
```

Terminal 1:
```bash
time python scripts/extract_form_3_batch.py
```

Watch Terminal 2 as the 10 filings process one after another.

{: .note }
> **No need to clear `results/` first.** The script overwrites each file as it goes — there
> is no check for work already done, so the second run repeats all ten API calls whether or
> not the output is already sitting there.
>
> Worth noticing, because it is a real cost: a rerun after a partial failure pays for
> everything again. You fix exactly this in
> [Make Your Tasks Rerun-Safe]({{ '/day2/rerun-safe-tasks/' | relative_url }}).

{: .note }
> **Reminder — `real` / `user` / `sys`:**
> - **`real`** — wall-clock time: how long you actually waited
> - **`user`** — CPU time your code used across all cores (if `user` > `real`, it ran on multiple cores in parallel)
> - **`sys`** — CPU time spent on OS-level work (file I/O, memory allocation)

Let's open these and discuss as a class before revealing the answer:

<details markdown="1">
<summary>❓ Question 1</summary>

What did we observe in `userload` while the 10 filings ran — what happened to **Cores** and **% Mem**?

</details>

<details markdown="1">
<summary>❓ Question 2</summary>

Why do the **Cores** stay near 0, even with 10 filings running?

</details>

<details markdown="1">
<summary>❓ Question 3</summary>

Why does **% Mem** stay near 0?

</details>

<details markdown="1">
<summary>❓ Question 4</summary>

Is this script **serial** or **parallel**?

</details>

<details markdown="1">
<summary>✅ Check your answer</summary>

- **Cores and % Mem barely moved.** The job spends almost all its time **waiting on the Anthropic API** to answer, not computing — so it barely touches the CPU. That makes it an **I/O-bound** job (waiting on the network), unlike the mystery script, which was **CPU-bound** (doing math).
- **`% Mem` reading 0 is two things at once.** The script really does hold little memory, because it handles one filing at a time rather than loading all ten. But even a few hundred MB would still print `0%`, because that column is a share of the node's whole ~1 TB. Trust `RES` in `htop` for the actual number — `% Mem` cannot resolve anything a single job is likely to use.
- **`real` is large, `user` is small.** `real` (wall-clock) is big because you waited on the API; `user` (actual CPU time) is tiny because the CPU had little to do. That gap — `real` ≫ `user` — is the fingerprint of a job that mostly waits.

A typical run: `real 0m22.5s`, `user 0m1.9s`, `sys 0m0.5s` — about 2 seconds of real work, ~20 seconds spent waiting. In `htop` you'll see just **one `python` process**, and **under 1 Core** in `userload`.

Two more things worth knowing:

- **Per-filing times vary** — each takes however long the API takes, so 10 filings isn't exactly 10× one.
- **Why the script sets `OPENBLAS_NUM_THREADS=1`.** Libraries like NumPy and pandas try to speed up math by grabbing *every* core on the machine — 256 on Yen2, for example. But the Yens enforce [per-user limits](https://rcpedia.stanford.edu/_policies/user_limits/) on how much CPU one person can use, so grabbing all 256 doesn't help — it just crowds a pile of threads onto the cores you're actually allowed, which can make the job *slower*. Setting it to `1` keeps the job to what it needs. The habit: on a shared node, don't let a library grab the whole machine — keep its thread count within your limits.

</details>

---

<details markdown="1">
<summary>⭐ Bonus — if you finished early</summary>

**Bonus — Run it twice**

Run the 10 filings twice in a row:

```bash
time python scripts/extract_form_3_batch.py
time python scripts/extract_form_3_batch.py
```

Compare the two `real` times — **was the second run different? If so, how, and why?**

<details markdown="1">
<summary>✅ Check your answer</summary>

Probably not by much — and **which run is faster will vary**. Nothing about the work changed: the script sends the same 10 filings, one at a time, and waits for each answer. Almost all of that `real` time is the API thinking, which is **latency you don't control** and which drifts run to run with load on the other end.

That is the useful lesson, and it bites in the capstone. **A single timing is weak evidence.** If you size a job off one measurement you are partly sizing off noise, so run it twice before you trust a number — and when you request `--time` in a Slurm script, leave headroom above your best measurement rather than pinning it to the fastest run you saw.

{: .note }
> **What about prompt caching?** It's real, and it's worth knowing about — an API can cache a chunk of a prompt it has already processed and skip re-reading it. But it doesn't help here, for two reasons. On Anthropic it is **opt-in**: you mark the reusable chunk with `cache_control`, and this script doesn't. And even if it did, there's nothing to reuse — the bulk of every request is a **different filing**, and the one part that does repeat (the system prompt) is far too short to be cacheable. Caching pays off when many requests share a **large** prefix, which is not the shape of this job. See [Anthropic's prompt caching docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).

</details>
</details>
