---
layout: default
title: "Compute Environments"
parent: "Day 2 — The Cluster"
nav_order: 1
permalink: /day2/compute-environments/
---

# Compute Environments

---

## Your Research Project in Computing Terms

Every research computing project has three questions:

<div style="display:flex; gap:1rem; margin:1.5rem 0;">
  <div style="flex:1; border:2px solid #4a90d9; border-radius:8px; padding:1rem;">
    <div style="font-size:2rem; text-align:center;">🎯</div>
    <div style="font-weight:700; font-size:1.1rem; text-align:center; margin:0.5rem 0;">What?</div>
    <div style="font-size:0.9rem;">Your research <strong>task</strong> — defined by your PI. For this course: extract names and CIKs from SEC Form 3 filings.</div>
  </div>
  <div style="flex:1; border:2px solid #27ae60; border-radius:8px; padding:1rem;">
    <div style="font-size:2rem; text-align:center;">🐍</div>
    <div style="font-weight:700; font-size:1.1rem; text-align:center; margin:0.5rem 0;">How?</div>
    <div style="font-size:0.9rem;">Your Python <strong>script</strong> — a sequence of steps that produces your output: extracted names, CIKs, a CSV.</div>
  </div>
  <div style="flex:1; border:2px solid #e67e22; border-radius:8px; padding:1rem;">
    <div style="font-size:2rem; text-align:center;">🖥️</div>
    <div style="font-weight:700; font-size:1.1rem; text-align:center; margin:0.5rem 0;">Where?</div>
    <div style="font-size:0.9rem;">Your compute environment — laptop, the Yens, or the cloud. Each has different <strong>resources</strong> (CPU cores, RAM, and storage).</div>
  </div>
</div>

The rest of this page answers the **Where** question — understanding the resources behind each environment: **CPU cores**, **RAM**, and **storage**.

---

## Three Places Your Code Can Run

Yesterday you wrote a Python script and ran it on the Yens interactively. But what is
actually inside the machine running your code?

Every machine you will run research code on — your laptop, a Yen, a cloud instance — is
built from the same few physical parts. The photo below shows a Yen server opened up.
What changes between environments is how much of each part you get, and who else is
competing for it.

![Server hardware diagram showing CPU, cores, and RAM]({{ site.baseurl }}/assets/images/server-hardware-cpu-ram.png)

| Component | What it is |
|-----------|-----------|
| **CPU** | The processor chip — executes your code |
| **CPU core** | An individual worker inside the CPU; each runs independently, which is what makes parallel work possible |
| **RAM** | Fast memory the CPU reads from and writes to while working — limited in size |
| **Storage (disk / file system)** | Where your files live when nothing is running — large, but slow to reach |
| **I/O (input/output)** | Moving data from disk into RAM and writing results back — almost always the slowest step |
| **Script** | The sequence of steps the CPU follows to produce your output |

---

### What Happens When You Run a Script

When you run `python scripts/extract_form_3_one_file.py`, four things happen in order:

1. **Load from disk** — Python reads your script and data files from storage.
2. **Into RAM** — the data lands in memory, where the CPU can reach it quickly.
3. **CPU does the work** — cores execute the steps in your script against what's in RAM.
4. **Save to disk** — results are written back to storage so they survive the run.

Watch the first leg. Getting data from disk into RAM is the slow one; once it's close to
the processor, the rest is quick:

<svg viewBox="0 2 600 220" role="img" aria-labelledby="hwflow-title hwflow-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:820px;height:auto;margin:0.75rem auto" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="hwflow-title">How your data moves: disk to RAM to CPU</title>
  <desc id="hwflow-desc">A packet of data loops from Storage to RAM to the CPU and back to Storage. Reading from disk into RAM is slow, and writing results back to disk is slow too; the CPU reaches data in RAM quickly.</desc>
  <defs><marker id="bk-hw" markerWidth="9" markerHeight="9" refX="6.5" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#c0392b"/></marker></defs>
  <text x="12" y="20" font-size="14" font-weight="700" letter-spacing="0.4" fill="#6b7280">🖥  HOW YOUR DATA MOVES: DISK → RAM → CPU</text>
  <line x1="80" y1="56" x2="520" y2="56" stroke="#cdd4e6" stroke-width="2" stroke-dasharray="4 5"/>
  <text x="190" y="46" text-anchor="middle" font-size="13" font-weight="700" fill="#c0392b">read — slow (~milliseconds)</text>
  <text x="410" y="46" text-anchor="middle" font-size="13" font-weight="700" fill="#3f4f74">fast (~nanoseconds)</text>
  <rect x="20" y="84" width="120" height="60" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="80" y="111" text-anchor="middle" font-size="16" font-weight="700" fill="#2c3e50">Storage</text>
  <text x="80" y="130" text-anchor="middle" font-size="12" fill="#6a7280">disk — large, slow</text>
  <rect x="240" y="84" width="120" height="60" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="300" y="111" text-anchor="middle" font-size="16" font-weight="700" fill="#2c3e50">RAM</text>
  <text x="300" y="130" text-anchor="middle" font-size="12" fill="#6a7280">fast, limited</text>
  <rect x="460" y="84" width="120" height="60" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="520" y="106" text-anchor="middle" font-size="16" font-weight="700" fill="#2c3e50">CPU</text>
  <rect x="487" y="116" width="12" height="12" rx="2" fill="#cdd4e6"/><rect x="503" y="116" width="12" height="12" rx="2" fill="#cdd4e6"/><rect x="519" y="116" width="12" height="12" rx="2" fill="#cdd4e6"/><rect x="535" y="116" width="12" height="12" rx="2" fill="#cdd4e6"/>
  <text x="520" y="140" text-anchor="middle" font-size="12" fill="#6a7280">cores do the work</text>
  <line x1="520" y1="174" x2="90" y2="174" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="4 4" marker-end="url(#bk-hw)"/>
  <text x="305" y="168" text-anchor="middle" font-size="13" font-weight="700" fill="#c0392b">write back — slow (~milliseconds)</text>
  <g>
    <circle cx="80" cy="56" r="8" fill="#0072B2"><animate attributeName="r" values="8;10;8" dur="1s" repeatCount="indefinite"/></circle>
    <animateTransform attributeName="transform" type="translate" values="0,0; 0,0; 220,0; 220,0; 440,0; 440,0; 440,118; 0,118; 0,0" keyTimes="0; 0.04; 0.38; 0.44; 0.52; 0.58; 0.63; 0.96; 1" dur="8s" repeatCount="indefinite" calcMode="linear"/>
  </g>
  <text x="300" y="212" text-anchor="middle" font-size="13.5" fill="#6a7280">Data crawls from disk into RAM (the slow step); the CPU reads it fast from RAM.</text>
</svg>

{: .warning }
> **Reading from disk is slow — by a factor of about a million.** Your CPU reaches data
> in RAM in nanoseconds; a disk read takes milliseconds. If your dataset does not fit in
> RAM all at once, your script keeps going back to disk mid-computation, and *that* is
> what makes a job crawl. This is why knowing how much RAM your script needs matters —
> on the cluster, and on your laptop too.

---

### Your Laptop

Yours alone, and small: a handful of cores, RAM measured in single-digit gigabytes, and
a disk that is bigger than RAM but far slower to reach. Nothing competes with you, and
nothing helps you either — when you close the lid, the work stops.

### The Yens — Shared

A Yen node has far more of everything: `yen1` has **256 cores and roughly 1 TB of RAM**.
But you share it. Cores, RAM, and the file system are all contended, and **they are not
infinite**. Per-user limits are enforced so that one person cannot claim a whole node —
see the [current limits](https://rcpedia.stanford.edu/_policies/user_limits/) — but when
the cluster is busy, you feel it.

{: .note }
> **Shared file system.** A file you write on `yen1` is instantly visible on every other
> node, because they all read and write the same VAST storage (~1 PB). That is what makes
> collaboration easy — and it also means everyone is hitting the same storage at once.

A **node** is one physical server, with its own CPU and RAM, independent of the others.
That distinction matters later today: a job asking for more cores than any single node has
will never start, however much the cluster has in total.

### The Cloud — Rented

AWS, GCP, and Azure rent you a machine that is **yours alone** and effectively
unlimited: need 1,000 cores for an hour, rent them; need a petabyte, rent it. No
queueing behind other researchers.

{: .warning }
> **You pay for everything you rent, for as long as you rent it** — not for what you
> use. Leaving a large instance running overnight by accident costs real money, and the
> bill arrives whether the machine did anything or not. Shut down what you are not using.

For most GSB research, the Yens are the right answer: no per-hour cost, data stays on
Stanford-managed infrastructure, and your PI already has access to the same project
storage. The cloud earns its keep when you need something the Yens do not have, or need
it faster than the queue will give it to you.

---

## Discussion

{: .important }
> **Follow along.** We'll talk through the tradeoffs together — laptop vs. Yens vs. cloud.

<details markdown="1">
<summary>❓ Questions to discuss</summary>

- What are the tradeoffs between your laptop, the Yens, and the cloud?
- What happens when many researchers all run jobs at once on the shared Yens?

</details>


---

## Bonus
{: .note }
> **Done with the mandatory exercises?** First, check whether anyone at your table is stuck — explaining it is how it sticks. Then pick anything below.

**Bonus — Know your own machine**

**Work with Claude** to figure out how to check your own laptop's CPU core count and RAM — tell it what operating system you're on and have it walk you through finding each one. Then enter your specs below to see just how much bigger one Yen node is (**yen1 has 256 cores and 1 TB of RAM**).

{: .warning }
> Start Claude **on your laptop**, not on the Yens — otherwise it'll report the Yen node's specs (256 cores, 1 TB), not your own machine's.

<details markdown="1">
<summary>💡 Hint — what to ask Claude</summary>

You don't need a fancy prompt. For example:

> Would you help me find the RAM and number of cores on my laptop?

</details>

<style>
.yen-widget { border: 1px solid #ddd; border-radius: 6px; padding: 1rem 1.25rem; margin: 1rem 0; }
.yen-widget label { display: block; margin: 0.35rem 0; }
.yen-widget input { width: 6rem; margin-left: 0.4rem; }
.yen-widget button { margin-top: 0.6rem; padding: 0.35rem 0.9rem; cursor: pointer; border-radius: 4px; border: 1px solid #ccc; background: #f0f0f0; }
#yw-out, #cw-out { margin-top: 0.75rem; line-height: 1.5; }
</style>

<div class="yen-widget">
  <label>Your laptop's CPU cores: <input id="yw-cores" type="number" min="1" step="1" value="8"></label>
  <label>Your laptop's RAM (GB): <input id="yw-ram" type="number" min="1" step="1" value="16"></label>
  <button id="yw-go">Compare</button>
  <p id="yw-out"></p>
</div>

<script>
(function () {
  var YEN_CORES = 256, YEN_RAM = 1024; // one Yen node (yen1): 256 logical cores, ~1 TB RAM
  function compare() {
    var c = parseFloat(document.getElementById('yw-cores').value);
    var r = parseFloat(document.getElementById('yw-ram').value);
    var out = document.getElementById('yw-out');
    if (!(c > 0) || !(r > 0)) { out.textContent = 'Enter your laptop’s cores and RAM above.'; return; }
    var coreX = YEN_CORES / c, ramX = YEN_RAM / r;
    var fit = Math.floor(Math.min(coreX, ramX));
    out.innerHTML =
      'A Yen node has <strong>' + coreX.toFixed(0) + '×</strong> your cores (' + YEN_CORES + ' vs ' + c + ')'
      + ' and <strong>' + ramX.toFixed(0) + '×</strong> your RAM (' + YEN_RAM + ' GB vs ' + r + ' GB).<br>'
      + 'About <strong>' + fit + '</strong> of your laptop' + (fit === 1 ? '' : 's') + ' would fit inside one Yen node.';
  }
  document.getElementById('yw-go').addEventListener('click', compare);
  compare();
})();
</script>


**Bonus — Price a cloud instance**

**Work with Claude** to find on-demand pricing for a cloud VM comparable to a Yen node — 256 cores and 1 TB of RAM, for example on AWS. Then use the calculator below — enter the VM's specs and the price per hour you found — to estimate what your Day 1 extraction job would cost to run there for an hour. Grant budgets aren't infinite; this is a real judgment call you'll make in your own research.

<details markdown="1">
<summary>💡 Hint — what to ask Claude</summary>

You don't need a fancy prompt. For example:

> Do you have on-demand VM pricing for a cloud VM (say AWS) with 256 cores and 1 TB of RAM?

</details>

<div class="yen-widget">
  <label>VM CPU cores: <input id="cw-cores" type="number" min="1" step="1" value="256"></label>
  <label>VM RAM (GB): <input id="cw-ram" type="number" min="1" step="1" value="1024"></label>
  <label>Price per hour ($): <input id="cw-rate" type="number" min="0" step="0.01" value="3.00"></label>
  <label>Hours you'd run it: <input id="cw-hours" type="number" min="0" step="0.5" value="1"></label>
  <button id="cw-go">Estimate cost</button>
  <p id="cw-out"></p>
</div>

<script>
(function () {
  function estimate() {
    var cores = parseFloat(document.getElementById('cw-cores').value);
    var ram = parseFloat(document.getElementById('cw-ram').value);
    var rate = parseFloat(document.getElementById('cw-rate').value);
    var hours = parseFloat(document.getElementById('cw-hours').value);
    var out = document.getElementById('cw-out');
    if (!(rate >= 0) || !(hours >= 0)) { out.textContent = 'Enter a price per hour and how many hours.'; return; }
    var total = rate * hours;
    out.innerHTML =
      'A VM with <strong>' + (cores > 0 ? cores : '?') + '</strong> cores and <strong>'
      + (ram > 0 ? ram : '?') + ' GB</strong> at <strong>$' + rate.toFixed(2) + '/hr</strong>'
      + ' would cost <strong>$' + total.toFixed(2) + '</strong> to run for '
      + hours + ' hour' + (hours === 1 ? '' : 's') + '.';
  }
  document.getElementById('cw-go').addEventListener('click', estimate);
  estimate();
})();
</script>


