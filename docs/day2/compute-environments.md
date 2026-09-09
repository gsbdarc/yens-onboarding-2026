---
layout: default
title: "★ Size Your Own Machine"
parent: "Part 1 — Profile & Submit a Job"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 3
permalink: /day2/compute-environments/
---

# Size Your Own Machine

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put one up as soon as either is true — an instructor will come to you.

{: .note }
> ⭐ **This whole page is bonus.** Do it once you have reached the
> [Part 1 Checkpoint]({{ '/day2/part1-checkpoint/' | relative_url }}) — and check whether
> anyone at your table is stuck first.

Put your own machine's numbers against a Yen node's, and price the same work in the
cloud. The written comparison is in
[Compute Environments]({{ '/reference/compute-environments/' | relative_url }}).

---

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
