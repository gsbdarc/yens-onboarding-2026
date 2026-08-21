---
layout: default
title: "Connecting to the Yens"
parent: "Day 1 — Foundations & AI"
nav_order: 1
permalink: /day1/connect-to-the-yens/
---

# Connecting to the Yens

SSH lets you connect from your laptop to a remote computer and run commands there
as if you were sitting at it. In this section you will log in to the Yens for the
first time, then learn how storage is organized: where your files live, how much
space you have, and what software is available.

{: .note }
> This section assumes you did the Canvas pre-work — a working terminal, and the
> `whoami` check that confirmed your Yens account is live. If your login does not
> work, put up a red sticky now rather than reading ahead.

---

## Why Use a Server at All?

Your laptop is fine for writing code and running small tests. But research computing regularly runs into limits that a laptop cannot handle:

| Situation | What happens on a laptop | What happens on the Yens |
|-----------|--------------------------|--------------------------|
| Dataset is 80 GB | Out of memory, script crashes | Loads fine — 250 GB–3 TB RAM per node |
| Analysis takes 12 hours | Laptop sleeps, WiFi drops, run dies | Job keeps running — always on, always connected |
| Need to run 100 jobs in parallel | One at a time, ties up your machine | Submit all 100 at once via the scheduler |
| Data is restricted (IRB, NDA) | Must stay on Stanford systems | Yens are Stanford-managed infrastructure |
| Collaborating with your PI | "Can you send me the data?" | PI already has access to `/yen/projects/` |

The Yens are available to all researchers at GSB — faculty, PhD students, post-docs, and research staff alike. Today we learn how to use them effectively.

{: .note }
> *"My regression on the full sample took 14 hours. My laptop died at hour 6. I lost everything. Two days later I reran it on the Yens and went to sleep. It finished while I was gone."* — Ben

---

## What Is a Remote Server?

Your laptop is powerful but limited: one machine, one location, and it has to be open and plugged in for work to run. A **remote server** is a computer you connect to over the network — it's always on, more powerful than your laptop, and your work keeps running after you close the lid.

**What are the Yens?**

The Yens are a 17-node shared research computing cluster: 5 interactive nodes you SSH into directly, and 12 nodes accessible only through the SLURM scheduler (Day 2). All 17 nodes share the same file system — a file you write on yen1 is instantly visible on every other node.

<svg viewBox="0 0 700 516" role="img" aria-labelledby="ssh-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:700px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="ssh-title">Your laptop connects over SSH to the remote Yens cluster. You land on a shared interactive Yen for light work; the powerful SLURM compute nodes are reached later, on Day 2, through a scheduler. Every node shares the same storage.</title>
  <defs>
    <marker id="ssh-ah" markerWidth="10" markerHeight="10" refX="7" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#e67e22"/></marker>
  </defs>

  <!-- Laptop -->
  <rect x="210" y="12" width="280" height="62" rx="12" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="232" y="40" font-size="15" font-weight="700" fill="#2c3e50">💻  Your laptop</text>
  <text x="232" y="59" font-size="12.5" fill="#6a7280">where you type your commands</text>

  <!-- SSH arrow -->
  <line x1="350" y1="76" x2="350" y2="115" stroke="#e67e22" stroke-width="2.5" marker-end="url(#ssh-ah)"/>
  <text x="366" y="93" font-size="13" font-weight="700" fill="#b3611a">connect with SSH</text>
  <text x="366" y="109" font-size="11.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">ssh SUNetID@yen.stanford.edu</text>

  <!-- Cluster band -->
  <rect x="16" y="118" width="668" height="384" rx="16" fill="#f7f9fc" stroke="#bcd4f2" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="38" y="142" font-size="12" font-weight="700" letter-spacing="0.6" fill="#8a94a6">☁️  THE YENS CLUSTER · REMOTE, ALWAYS ON</text>

  <!-- Interactive Yens -->
  <rect x="40" y="156" width="620" height="106" rx="12" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="60" y="184" font-size="15" font-weight="700" fill="#2c3e50">Interactive Yens — where you land today</text>
  <rect x="60" y="200" width="104" height="26" rx="6" fill="#f3f4f7" stroke="#d5d8e2" stroke-width="1"/>
  <text x="112" y="217" text-anchor="middle" font-size="12" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">yen1</text>
  <rect x="176" y="200" width="104" height="26" rx="6" fill="#f3f4f7" stroke="#d5d8e2" stroke-width="1"/>
  <text x="228" y="217" text-anchor="middle" font-size="12" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">yen2</text>
  <rect x="292" y="200" width="104" height="26" rx="6" fill="#f3f4f7" stroke="#d5d8e2" stroke-width="1"/>
  <text x="344" y="217" text-anchor="middle" font-size="12" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">yen3</text>
  <rect x="408" y="200" width="104" height="26" rx="6" fill="#f3f4f7" stroke="#d5d8e2" stroke-width="1"/>
  <text x="460" y="217" text-anchor="middle" font-size="12" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">yen4</text>
  <rect x="524" y="200" width="104" height="26" rx="6" fill="#f3f4f7" stroke="#d5d8e2" stroke-width="1"/>
  <text x="576" y="217" text-anchor="middle" font-size="12" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">yen5</text>
  <text x="60" y="250" font-size="12.5" fill="#6a7280">Shared compute for light work — per-user CPU &amp; RAM limits enforced</text>

  <!-- Scheduler arrow -->
  <line x1="350" y1="262" x2="350" y2="299" stroke="#e67e22" stroke-width="2.5" marker-end="url(#ssh-ah)"/>
  <text x="366" y="286" font-size="13" font-weight="700" fill="#b3611a">via the SLURM scheduler — Day 2</text>

  <!-- SLURM compute nodes -->
  <rect x="40" y="302" width="620" height="72" rx="12" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="60" y="330" font-size="15" font-weight="700" fill="#2c3e50">SLURM compute nodes — reached on Day 2</text>
  <text x="60" y="356" font-size="11.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">8 CPU + 4 GPU nodes (12 total) · only via sbatch / srun</text>

  <!-- Shared storage -->
  <rect x="40" y="390" width="620" height="100" rx="12" fill="#f3f4f7" stroke="#d5d8e2" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="60" y="414" font-size="12" font-weight="700" letter-spacing="0.6" fill="#8a94a6">SHARED STORAGE · EVERY NODE SEES THE SAME FILES</text>
  <text x="60" y="438" font-size="11.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">/home/users/SUNetID/<tspan font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" fill="#6a7280">   personal · backed up · limited</tspan></text>
  <text x="60" y="460" font-size="11.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">/yen/projects/<tspan font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" fill="#6a7280">   project files &amp; results · backed up · large</tspan></text>
  <text x="60" y="482" font-size="11.5" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">/scratch/users/SUNetID/<tspan font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" fill="#6a7280">   large &amp; fast · NOT backed up</tspan></text>
</svg>

*Your laptop and the Yens are two separate computers; **SSH** is the connection between them. When you log in you land on one of the shared **interactive Yens** (yen1–yen5) — fine for light work. The powerful **SLURM compute nodes** come later, on Day 2, reached through a scheduler rather than directly. Whichever node you're on, you see the same shared files.*

`ssh` opens an encrypted tunnel: you type locally, commands execute remotely, output streams back to your screen. The interactive Yens are shared — per-user CPU and RAM limits are enforced automatically. See the [current limits](https://rcpedia.stanford.edu/_policies/user_limits/) for details. For heavier jobs, the SLURM scheduler (Day 2) gives you dedicated compute nodes.

**What's inside a Yen server:**

![Server hardware diagram showing CPU, cores, and RAM — Yen1 has 256 cores]({{ "/assets/images/server-hardware-cpu-ram.png" | relative_url }})

The **CPU** is the processor chip. **Cores** are the individual workers inside it — each core runs instructions independently, which is what makes parallel work possible. **RAM** holds the data the CPU is actively using. The Yen servers vary in size — see the [current specs on RCPedia](https://rcpedia.stanford.edu/_getting_started/yen-servers/#overview-of-the-yen-computing-infrastructure) for details.

---

## Exercise 1 — Log In

Log in to the Yens for the first time and get your bearings.

{: .important }
> **Task:** Connect to the Yens cluster over SSH, identify which interactive Yen you landed on, and read the login banner.

**Connect:**
```bash
ssh SUNetID@yen.stanford.edu
```

Replace `SUNetID` with your Stanford username. When prompted for your password, type your Stanford password (nothing will appear — that's normal). You will be prompted for Duo two-factor authentication.

**Identify your node:**
```bash
hostname      # e.g. yen1, yen2, yen3, yen4, or yen5
whoami        # confirm you are logged in as yourself
```

{: .note }
> The Yens (yen1–yen5) are shared interactive compute servers. You land on whichever one the load balancer picks. They're powerful, but shared — read the login banner when you connect, it describes current usage policies.

**Read the banner, then look around:**
```bash
ls ~                              # your home directory on the Yens
pwd                               # /home/users/SUNetID
ls /scratch/users/                # personal scratch — you will create your own folder here later
ls /yen/projects/                 # shared project storage
```

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

---

## Where Your Files Live

<svg viewBox="0 0 660 200" role="img" aria-labelledby="fs-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:660px;height:auto;margin:1.5rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="fs-title">The Yens have three main places to keep files. Your home directory is small and backed up. Project storage is shared with your team and backed up. Scratch is huge and fast but NOT backed up, so files there can be deleted — copy out anything you want to keep.</title>
  <text x="14" y="26" font-size="12.5" font-weight="700" letter-spacing="0.4" fill="#8a94a6">📁  WHERE YOUR FILES LIVE ON THE YENS</text>

  <!-- Home: backed up -->
  <rect x="14" y="40" width="200" height="150" rx="14" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="30" y="74" font-size="14.5" font-weight="700" fill="#2c3e50">🏠  Your home</text>
  <text x="30" y="98" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">/home/users/SUNetID/</text>
  <rect x="28" y="112" width="172" height="28" rx="8" fill="#e3f2e6" stroke="#b7ddba" stroke-width="1.5"/>
  <text x="114" y="131" text-anchor="middle" font-size="12" font-weight="700" fill="#2e7d46">✓  backed up</text>
  <text x="30" y="162" font-size="11" fill="#6a7280">personal workspace</text>
  <text x="30" y="180" font-size="11" fill="#6a7280">small quota</text>

  <!-- Projects: backed up -->
  <rect x="230" y="40" width="200" height="150" rx="14" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="246" y="74" font-size="14.5" font-weight="700" fill="#2c3e50">👥  Project storage</text>
  <text x="246" y="98" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">/yen/projects/</text>
  <rect x="244" y="112" width="172" height="28" rx="8" fill="#e3f2e6" stroke="#b7ddba" stroke-width="1.5"/>
  <text x="330" y="131" text-anchor="middle" font-size="12" font-weight="700" fill="#2e7d46">✓  backed up</text>
  <text x="246" y="162" font-size="11" fill="#6a7280">shared with your team</text>
  <text x="246" y="180" font-size="11" fill="#6a7280">space is limited</text>

  <!-- Scratch: NOT backed up -->
  <rect x="446" y="40" width="200" height="150" rx="14" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="462" y="74" font-size="14.5" font-weight="700" fill="#2c3e50">⚡  Scratch space</text>
  <text x="462" y="98" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" fill="#5b6472">/scratch/users/SUNetID/</text>
  <rect x="460" y="112" width="172" height="28" rx="8" fill="#fdeceb" stroke="#f0c3bd" stroke-width="1.5"/>
  <text x="546" y="131" text-anchor="middle" font-size="12" font-weight="700" fill="#c0392b">✕  NOT backed up</text>
  <text x="462" y="162" font-size="11" fill="#6a7280">huge &amp; fast</text>
  <text x="462" y="180" font-size="11" fill="#6a7280">copy out what you keep</text>
</svg>

Rule of thumb: the project itself — scripts, data, and outputs — lives in **projects**; your personal files live in **home** (both are backed up); **scratch** is for big temporary files you don't need to keep.

{: .note }
> **How to organize your work on the Yens:**
> - **A project — its scripts, data, and outputs → `/yen/projects/faculty/your_project/`.** This is the shared, backed-up home for the project itself; keep raw data and outputs in **separate subfolders** (e.g. `data/` and `output/`) so they never get mixed up. Access is controlled by the project's **workgroup**: everyone in it can read and write, which is how you, your PI, and collaborators share the same files. You may belong to **several** project workgroups at once, each with its own folder under `/yen/projects/faculty/` (or `/yen/projects/students/`). See [Workgroups](https://rcpedia.stanford.edu/_policies/workgroups/) on RCpedia for who gets access and how it's managed.
> - **Personal files → your home, `/home/users/SUNetID/`.** Things that are yours, not any one project's: authentication tokens, R or shell preferences, quick one-off experiments. Backed up, and only you can see it.
> - **Large, temporary things → `/scratch/users/SUNetID/`.** Fast and roomy, but **not backed up** and periodically cleared. Use it for things you don't need to keep or that won't fit in your quota — a big public dataset you're exploring, or an LLM you're testing out. Copy anything worth keeping back to `/yen/projects/`.

**Local disk: `/tmp`**

Those three locations — home, projects, and scratch — are all on the **shared file system**: every node sees the same files. Each node *also* has its own **local disk** that is **not** shared with other nodes, and `/tmp` lives there — it's where programs often write temporary files while they run.

Two things to know about `/tmp`: it's **private to that node** (a file at `/tmp` on `yen1` isn't visible on `yen2`), and it's **temporary and not backed up** (cleared automatically). Keep anything you care about — data, results — on the shared file system.

---

## Exercise 2 — Storage and Software

{: .important }
> **Task:** Check your disk quota, then find and load a Python module.

**Check your quota:**
```bash
gsbquota                             # shows home and scratch usage for your account
gsbquota /yen/projects/faculty/your_project  # append a path to check usage for a project folder
```

**Browse storage in a visual file manager:**
```bash
gsbbrowser                # opens an interactive file size browser in the terminal

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

---

## Optional Practice

**Skip the repeated logins with SSH multiplexing**

Every time you `ssh` to the Yens you re-enter your password and approve Duo again — tedious once you're opening several sessions. **SSH multiplexing** keeps one authenticated connection open and reuses it for every later session to the same host, so you authenticate just **once**.

Set it up on your **laptop** (not the Yens) by adding this to `~/.ssh/config` — create the file if it doesn't exist:

```
Host yen yen? yen??
  HostName %h.stanford.edu

Host yen yen.stanford.edu yen? yen?? yen?.stanford.edu yen??.stanford.edu
  ControlMaster auto
  ControlPersist yes
  GSSAPIDelegateCredentials yes

Host *
  ControlPath ~/.ssh/%r@%h:%p
```

Then try it:

1. Open your first connection as usual — `ssh SUNetID@yen.stanford.edu` — and authenticate with your password and Duo. This becomes the shared "master" connection.
2. Leave it open, and in a **second** terminal run `ssh SUNetID@yen.stanford.edu` again. It connects **instantly** — no password, no Duo — because it's reusing the first connection.

Full write-up: [SSH Setup for the Yen Servers](https://rcpedia.stanford.edu/blog/2026/03/17/ssh-setup-for-the-yen-servers/) on RCpedia.
