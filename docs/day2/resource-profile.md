---
layout: default
title: "3. Write Down What You Measured"
parent: "Part 1 — Measure & Submit"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 3
permalink: /day2/resource-profile/
---

# Write Down What You Measured

{: .note }
> Everything here runs from your clone with the environment active:
> `cd ~/yens-onboarding-2026 && source .venv/bin/activate`

---

{: .important }
> **Mandatory.** **Task:** Write down the resources you measured for the 10-filing run in your README.

Now that you've profiled **10 filings**, write down what you measured. Open the `README.md` in your repo and add a **Resource Profile** section:

```markdown
## Resource Profile

### extract_form_3_batch.py — 10 filings

- Yen node used:
- Wall-clock time (real):
- CPU cores used:
- RAM used (RES from htop, or % Mem from userload):
- Serial or parallel:
```

{: .tip }
> If your RAM here is tiny — just a few MB (`RES`), showing as 0% Mem in `userload` — you can't ask for 0, so a good tip is to write down a small round number like `1G`.

Fill in the actual numbers from your `time`, `userload`, and `htop` output.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

---
