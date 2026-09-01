---
layout: default
title: "Your Data on the Yens"
parent: "Day 1 — Foundations & AI"
nav_order: 2
permalink: /day1/your-data/
---

# Your Data on the Yens

You are logged in. Before you put anything on this machine, learn where it goes — because
the three places you can put it behave very differently, and only one of the differences
is recoverable when you get it wrong.

The short version: **two of the three are backed up, and the fast one is not.**

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

## Know Before You Fill It

Quotas on the Yens are enforced, and a job that hits one does not politely pause — it
fails partway through, often after hours of work, sometimes leaving a half-written file
that looks complete. Two commands keep you ahead of that.

**How much space am I using?**

```bash
gsbquota                             # shows home and scratch usage for your account
gsbquota /yen/projects/faculty/your_project  # append a path to check usage for a project folder
```

Run it with no arguments for your own home and scratch. Give it a path to ask about a
project folder instead — quotas there belong to the project, not to you, so a collaborator
filling it up is your problem too.

**What is actually taking up the space?**

`gsbquota` tells you that you are at 94%. It does not tell you which forgotten folder of
intermediate files got you there. `gsbbrowser` does:

```bash
gsbbrowser                # opens an interactive file size browser in the terminal
# navigate with arrow keys, q to quit
```

It opens a browser in the terminal, biggest directories first, and you walk down into them
with the arrow keys. Nine times out of ten the answer is one directory of output from a run
you have forgotten about.

{: .tip }
> **Check before a big run, not after it fails.** `gsbquota` takes one second, and it is
> the cheapest possible way to find out that tomorrow's cluster job has nowhere to write
> its results.

---

## Exercise

{: .important }
> **Task:** Find out where you are, how much room you have, and what is using it.

```bash
gsbquota                     # how full are home and scratch?
ls /yen/projects/            # which project spaces exist?
ls ~                         # what's in your home directory already?
gsbbrowser                   # what's actually taking up the space? (q to quit)
```

Three questions worth being able to answer before you move on:

1. **Which of your three locations has the most room?** It will not be home.
2. **If your laptop died tonight, which of your files on the Yens would survive?** Everything
   in home and projects. Nothing in scratch.
3. **Where should the SEC filings you process later today end up?** In your cloned repo, in
   home — they are small, and they are part of a project under version control.

{: .warning }
> **"Not backed up" means what it says.** Scratch is periodically cleared, and deleted files
> there are gone — there is no snapshot, no trash, and nothing DARC can restore for you. It
> is the right place for a 200 GB download you can fetch again. It is the wrong place for
> the only copy of anything.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put a sticky note on your laptop lid so instructors can see where you are.

---

## Getting Data In and Out

Knowing where data goes is half of it; putting it there is the other half. You will need
this before the morning is out, and it is one of the six items on the
[Part 1 Checkpoint]({{ '/day1/part1-checkpoint/' | relative_url }}):

- **From your laptop** — `scp`, covered in [Transferring Files]({{ '/reference/transferring-files/' | relative_url }}). Run it *from the laptop*, in its own terminal, not from inside your SSH session.
- **From GitHub** — `git clone`, which is how the course repo gets here in [Git & GitHub]({{ '/day1/git-and-github/' | relative_url }}).
- **Moving a lot of files at once** — [Bulk File Operations]({{ '/reference/bulk-file-operations/' | relative_url }}).

{: .aside }
> **Why the Yens have a small home and a huge scratch.** Backed-up storage costs several
> times what unbacked storage does, because every byte is kept more than once. Rather than
> charge everyone for the most expensive tier, the cluster gives you a little of the safe
> kind and a lot of the fast kind, and leaves the sorting to you. Most research computing
> systems you meet later — Sherlock, Oak, an AWS account — split storage the same way and
> for the same reason.
