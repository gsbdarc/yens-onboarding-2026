---
layout: default
title: "6. Debug a Failed Job"
parent: "Part 1 — Profile & Submit a Job"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 6
permalink: /day2/debug-a-failed-job/
---

# Debug a Failed Job

{: .note }
> Everything here runs from your clone with the environment active:
> `cd ~/yens-onboarding-2026 && source .venv/bin/activate`

---

{: .important }
> **Mandatory.** **Task:** Submit a deliberately broken job, read the error log it leaves behind, and fix it with Claude as your reviewer. Reading a failed job's `.err` is the first debugging skill you will actually need on the cluster.


Your repo ships several Slurm scripts that are **deliberately broken**. Fix `slurm/fix_me.slurm` here; the others are waiting for you in the [Bonus](#bonus) section. **Work with Claude**: point Claude Code at the job's error log and ask it to explain what went wrong and propose a fix. **Read its explanation, and if the fix makes sense, approve it** and let Claude apply it — you're the reviewer, so don't accept a change you don't understand.

{: .note }
> 💡 **Let it fail before you fix it.** A `logs/fix_me_*.err` file has to exist for you to read, and a bonus exercise later reuses it — so submit it and let it fail rather than reading the script and spotting the bug by eye.


Submit the first one:

```bash
sbatch --reservation=class_day2 slurm/fix_me.slurm
```

Watch it move through the queue — `PD` (pending), then `R` (running), then gone once it finishes:

```bash
squeue --me
```

Once it's no longer in the queue, check how it ended:

```bash
sacct -u SUNetID --format=JobID,JobName,State,Elapsed --starttime=today
```

When it shows `FAILED`, read the error log to find out *why*:

```bash
cat logs/fix_me_*.err
```

**Put Claude Code in plan mode first** (press `Shift`+`Tab` to switch) so it lays out *what* it would change and *why* instead of editing right away. Then point it at the error log — a simple prompt is enough:

> Help me troubleshoot `logs/fix_me_*.err`

**Read the plan it comes back with.** If the fix makes sense, approve it and let Claude apply it — you're the reviewer.

You'll also want a completion email, so ask Claude to add the notification lines to this script:

> Add `#SBATCH --mail-type=ALL` and `#SBATCH --mail-user=SUNetID@stanford.edu` to `slurm/fix_me.slurm`.

Then resubmit — **keep debugging and resubmitting until the Slurm email says the job succeeded** (exit status `0`).

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

---

---

<details markdown="1">
<summary>⭐ Bonus — if you finished early</summary>

**Bonus — Debug `fix_me_2.slurm`**

Same drill, a different setup mistake. Submit it, watch it fail, and read its error log:

```bash
sbatch --reservation=class_day2 slurm/fix_me_2.slurm
squeue --me
cat logs/fix_me_2_*.err
```

Troubleshoot with Claude in plan mode (`> Help me troubleshoot logs/fix_me_2_*.err`), approve the fix if it makes sense, have Claude add the email lines to `slurm/fix_me_2.slurm` too, and resubmit until the Slurm email says it succeeded.


**Bonus — Debug `fix_me_3.slurm`**

One more, hiding yet another setup mistake. Same process:

```bash
sbatch --reservation=class_day2 slurm/fix_me_3.slurm
squeue --me
cat logs/fix_me_3_*.err
```

Troubleshoot with Claude in plan mode, approve the fix, have Claude add the email lines to `slurm/fix_me_3.slurm`, and resubmit until it completes.


**Bonus — Debug `extract_form_3_one_file_broken.slurm`**

The trickiest one: it hides *two* bugs — one in the Slurm script and one in the Python it runs (`scripts/extract_form_3_one_file_broken.py`). Submit it, read the error log, and work through **both** with Claude the same way (plan mode → read the plan → approve → add the email lines → resubmit) until it completes.

</details>
