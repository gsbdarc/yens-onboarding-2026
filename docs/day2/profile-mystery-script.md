---
layout: default
title: "1. Profile the Mystery Script"
parent: "Part 1 — Measure & Submit"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 1
permalink: /day2/profile-mystery-script/
---

# Profile the Mystery Script

{: .note }
> Everything here runs from your clone with the environment active:
> `cd ~/yens-onboarding-2026 && source .venv/bin/activate`

---

You are going to run a script you have never seen before and figure out what resources it uses — without reading the code. This is called **profiling**: measuring a script's time, CPU, and RAM usage as it runs. The technique: one terminal runs the script, a second terminal on the **same node** watches it live.

<svg viewBox="0 0 700 132" role="img" aria-labelledby="twoterm-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:700px;height:auto;margin:1.5rem auto" font-family="'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="twoterm-title">Profiling uses two terminals on the same Yen node: Terminal 1 runs the script, Terminal 2 watches its CPU and RAM live.</title>
  <rect x="16" y="8" width="668" height="116" rx="16" fill="#f7f9fc" stroke="#bcd4f2" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="40" y="34" font-size="12.5" font-weight="700" letter-spacing="0.4" fill="#6b7280">🖥️  ONE YEN NODE · BOTH TERMINALS ON IT</text>
  <rect x="40" y="46" width="300" height="70" rx="12" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="60" y="76" font-size="17" font-weight="700" fill="#2c3e50">Terminal 1 · the worker</text>
  <text x="60" y="100" font-size="15" fill="#6a7280">runs the script</text>
  <rect x="360" y="46" width="300" height="70" rx="12" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="380" y="76" font-size="17" font-weight="700" fill="#2c3e50">Terminal 2 · the observer</text>
  <text x="380" y="100" font-size="15" fill="#6a7280">watches CPU + RAM live</text>
</svg>

*Two terminals on the **same** Yen node: one runs the script, the other watches it live.*

{: .important }
> **Mandatory.** **Task:** Run `mystery_script.py` and measure its resource usage in real time using two terminals — both on the **same Yen node**.

**Step 1 — Note which Yen you are on.**

In your current terminal, run:

```bash
hostname
```

You will see something like `yen2`. Remember this — your second terminal must connect to the exact same node.

**Step 2 — Open a second terminal on the same node.**

In the new terminal, SSH directly to that node by name (not the load-balanced `yen.stanford.edu`, which could land you on a different machine):

```bash
ssh SUNetID@yen2.stanford.edu   # replace yen2 with whatever hostname showed above
```

{: .note }
> 💡 **Skip the second login.** A fresh `ssh` means another password + Duo prompt. To avoid re-authenticating, open a terminal through JupyterHub instead: browse to that node's hub (e.g. `https://yen2.stanford.edu/jupyter/`), then **New → Terminal**. You're already authenticated there, and it drops you onto that exact node — ideal for the second monitoring terminal.

**Step 3 — Start `watch userload` in Terminal 2 *first*, before running anything.**

Terminal 2:
```bash
watch userload
```

- `userload` shows how many **cores** you're using and what **% of the node's memory** you're holding — your total footprint across all your processes on this node. It looks like `SUNetID  |  0.34 Cores  |  0.00% Mem  on yen2`
- `watch` re-runs it every 2 seconds, so the numbers refresh live
- Jupyter processes are tracked separately and are not included

**What are we seeing?** Right now — before you run anything — this is your **baseline**: **Cores** near 0 and **% Mem** near 0. That's what an idle account looks like. Keep this terminal visible; you'll watch these numbers move once the script starts. (See the [current per-user limits](https://rcpedia.stanford.edu/_policies/user_limits/) for how much CPU and RAM any one user can use on an interactive Yen.)

**Step 4 — Now run the script in Terminal 1 and watch Terminal 2 change.**

Terminal 1:
```bash
time python scripts/mystery_script.py
```

{: .note }
> **What's the `time` in front?** `time` is a wrapper — it runs whatever command follows (`python scripts/mystery_script.py`) exactly as normal, then, once it finishes, prints how long it took. It doesn't change what your script does; it just measures it. That's where the `real` / `user` / `sys` lines below come from.

As it runs, watch Terminal 2: **your Cores number climbs and % Mem grows** — that's the script's footprint stacking on top of your baseline. If Cores climbs above 1, the script is using more than one core at once. When it finishes, the numbers fall back toward baseline, and `time` prints three lines:

```
real    0m31.234s
user    2m0.682s
sys     0m2.212s
```

- **real** — wall-clock time: how long you actually waited
- **user** — CPU time your code consumed across all cores; if `user` > `real`, the script used multiple cores in parallel
- **sys** — CPU time spent on OS-level work (file I/O, memory allocation)

**Step 5 — Run the script again, this time watching it in `htop`.**

First, in **Terminal 2**, stop `watch userload` by pressing **`Ctrl+C`**. Then start `htop`, filtered to just your own processes:

```bash
htop -u SUNetID
```

The `-u` flag limits `htop` to your processes, so the hundreds of other users' processes on the node don't drown yours out.

**Each row in `htop` is one process.** The columns that matter:

- **`CPU%`** — how hard that process is pushing. `100%` = one full core busy, `200%` = two cores, and so on — a single process reading over `100%` is spread across multiple cores.
- **`RES`** — the real RAM the process is actually using. Shown in **KB** by default, so `9000` ≈ **9 MB**; bigger values get an `M` or `G` suffix (like `111M`).
- **`MEM%`** — that same `RES` as a share of the **whole node's** RAM. On a 1 TB node a few MB rounds to **0.0%** — which is why `userload` can read `0% Mem` even though the process really is using memory.
- **`VIRT`** — ignore it. That's memory the process *reserved*, not what it's actually using.

Now, in **Terminal 1**, run the script again and watch your rows in `htop` light up:

```bash
time python scripts/mystery_script.py
```

As the script runs, watch new `python` rows appear — that's it spawning work. Count them to answer "how many processes did it run?"

**Compare with your neighbor:**
- How long did it take, and how much RAM did it peak at?
- How many CPU cores did it use?
- How many processes did it run?
- Is it therefore **serial** (one core) or **parallel** (multiple)?


{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help


<details markdown="1">
<summary>✅ Check your answer</summary>

You saw about **4 `python` processes** in `htop` and roughly **4 Cores** in `userload` — no accident. Open `scripts/mystery_script.py` and you'll find `num_cores = 4`: the script deliberately starts 4 worker processes, one per core, which is exactly what made it a **parallel, multi-core** program. The amount of parallelism is a **choice in the code** — change that number and the processes and cores you'd see change with it.

</details>
---

---

<details markdown="1">
<summary>⭐ Bonus — if you finished early</summary>

**Bonus — Vectorized vs. Non-Vectorized**

One quick way to speed up scientific Python is **vectorization** — doing the math on a whole array in one operation instead of looping element-by-element in Python. The array operation runs in fast, pre-compiled code, so it's often 10–100× faster. We ship a script that computes the same sum of squares both ways — profile it and see the difference.

Terminal 1 — run it:
```bash
source .venv/bin/activate
time python scripts/vectorize_demo.py
```

Terminal 2 — watch the load while it runs:
```bash
watch userload
```

Both versions produce the identical result; the script prints how much faster the vectorized one was (often 10× or more). Notice the slow Python loop pins a core the whole time, while the NumPy version finishes almost before you can look at Terminal 2.


**Bonus — Change the number of cores**

Open `scripts/mystery_script.py` and change `num_cores = 4` to a different number — try **1**, or **8**. Then **profile it again** with the same two-terminal setup: run `time python scripts/mystery_script.py` in Terminal 1, and watch it in Terminal 2 with `watch userload` (or `htop -u SUNetID`).

Document what changes and discuss with your neighbor:

- How many `python` processes appear in `htop` now?
- How many **Cores** in `userload`?
- Did the `real` (wall-clock) time go up or down?
- Does the resource usage match the number you set?

</details>
