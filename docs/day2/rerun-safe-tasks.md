---
layout: default
title: "3. Make Your Tasks Rerun-Safe"
parent: "Part 2 — Scale & Ship"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 3
permalink: /day2/rerun-safe-tasks/
---

# Make Your Tasks Rerun-Safe

{: .note }
> Everything here runs from your clone with the environment active:
> `cd ~/yens-onboarding-2026 && source .venv/bin/activate`

---

{: .important }
> **Mandatory.** **Task:** Make each array task skip work it has already done, then resubmit
> the same array and watch it finish in seconds.

A handful of your 100 will come back empty sooner or later — a node reboots, a task hits
its time limit, the API times out. Rerunning the whole array to catch them wastes compute
and, with a paid API, money.

Add the existence check to your script, then resubmit the array you just ran.

<details markdown="1">
<summary>💡 Hint — one way to do it</summary>

```python
# already done? skip — makes the array safe to resubmit after a partial failure
if output_path.exists():
    print(f"{output_path} already exists — skipping")
    sys.exit(0)
```

</details>

Nothing has been deleted, so every task should find its output and exit at once — the whole array finishing in seconds rather than minutes is the sign it worked.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

---
