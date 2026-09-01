#!/usr/bin/env python3
"""Render the course website's inline SVG diagrams to PNGs and animated GIFs.

The docs pages carry their diagrams as inline <svg>. Those SVGs are
self-contained (inline font-family, no CSS variables, no external classes), so
each can be lifted out and rendered on its own.

Rendering uses headless Chrome, which is the most faithful renderer available
here -- it handles the system font stacks and emoji the diagrams rely on.

Animation is driven explicitly rather than by waiting:

    svg.pauseAnimations(); svg.setCurrentTime(T)

runs synchronously at load, so the screenshot is deterministically the frame at
T no matter how long the render takes. Sweeping T across the loop gives the
frames for a GIF, which Google Slides *does* play in present mode (it cannot
play SVG animation).

    python render_website_graphics.py <repo-root> <out-dir>
"""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SCALE = 2  # 2x for crisp embedding

# name, source file, line at/after which the <svg> starts, gif?, frames, loop seconds
GRAPHICS = [
    ("cluster-shape",    "docs/day1/connect-to-the-yens.md",      51,  False, 0,  0),
    ("data-moves",       "docs/day2/compute-environments.md",     74,  True,  24, 10),
    ("two-terminals",    "docs/day2/profiling.md",                97,  False, 0,  0),
    ("day2-map",         "docs/day2/profiling.md",                11,  False, 0,  0),
    ("size-a-request",   ".instructor/slides/day2-lecture1.html",  358, False, 0,  0),
    ("slurm-submit",     "docs/day2/slurm-scheduler.md",          54,  False, 0,  0),
    ("job-lifecycle",    "docs/day2/slurm-scheduler.md",          123, True,  24, 10),
    ("kitchen-one",      "docs/reference/parallelization.md",     22,  True,  20, 14),
    ("kitchen-four",     "docs/reference/parallelization.md",     62,  True,  20, 14),
    ("shape-1job1core",  "docs/reference/parallelization.md",     168, True,  20, 12),
    ("shape-1jobNcore",  "docs/reference/parallelization.md",     208, True,  20, 12),
    ("shape-Njob1core",  "docs/reference/parallelization.md",     254, True,  20, 14),
    ("shape-NjobNcore",  "docs/reference/parallelization.md",     302, True,  20, 14),
    ("array-fanout",     "docs/day2/job-arrays.md",               79,  False, 0,  0),
]

WRAP = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;padding:0;background:transparent}}
svg{{display:block;width:{w}px !important;height:{h}px !important;max-width:none !important}}
</style></head><body>
{svg}
<script>
const s = document.querySelector('svg');
if (s && s.pauseAnimations) {{ s.pauseAnimations(); s.setCurrentTime({t}); }}
</script></body></html>"""


def extract_svg(root: Path, relpath: str, line: int) -> str:
    txt = (root / relpath).read_text(encoding="utf-8")
    lines = txt.split("\n")
    # byte offset a couple of lines before the reported line, then take the next <svg>
    start = sum(len(l) + 1 for l in lines[: max(0, line - 3)])
    m = re.search(r"<svg\b.*?</svg>", txt[start:], re.S)
    if not m:
        raise SystemExit(f"no <svg> found in {relpath} at/after line {line}")
    return m.group(0)


def normalise_root(svg: str) -> str:
    """Drop the root <svg>'s own style/width/height so the wrapper sets the size."""
    m = re.match(r"<svg\b[^>]*>", svg)
    tag = m.group(0)
    clean = re.sub(r'\s(?:style|width|height)="[^"]*"', "", tag)
    return clean + svg[m.end():]


def trim(path: Path, pad: int = 6) -> None:
    """Crop to the drawn content; several SVGs leave large empty margins."""
    im = Image.open(path).convert("RGBA")
    box = im.getchannel("A").getbbox()
    if not box:
        return
    l, t, r, b = box
    l, t = max(0, l - pad), max(0, t - pad)
    r, b = min(im.width, r + pad), min(im.height, b + pad)
    im.crop((l, t, r, b)).save(path)


def viewbox_size(svg: str):
    m = re.search(r'viewBox="([\d.\-\s]+)"', svg)
    if not m:
        raise SystemExit("svg has no viewBox")
    _, _, w, h = [float(x) for x in m.group(1).split()]
    return w, h


def shoot(svg: str, w: float, h: float, t: float, out: Path, tmp: Path) -> Path:
    """Screenshot the SVG at animation time t."""
    pw, ph = int(round(w * SCALE)), int(round(h * SCALE))
    wrap = tmp / "wrap.html"
    wrap.write_text(WRAP.format(svg=svg, w=pw, h=ph, t=t), encoding="utf-8")
    subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
         "--default-background-color=00000000",
         f"--window-size={pw},{ph}", f"--screenshot={out}",
         f"file://{wrap}"],
        check=True, capture_output=True, timeout=120,
    )
    return out


def is_blank(path: Path) -> bool:
    """A silent Chrome failure yields a uniform image, which a size check passes."""
    im = Image.open(path).convert("RGBA")
    extrema = im.getextrema()
    # every channel flat => nothing was drawn
    return all(lo == hi for lo, hi in extrema)


def main(root: Path, outdir: Path):
    outdir.mkdir(parents=True, exist_ok=True)
    tmp = outdir / "_tmp"
    tmp.mkdir(exist_ok=True)
    report = []

    for name, relpath, line, animated, nframes, loop in GRAPHICS:
        svg = extract_svg(root, relpath, line)
        w, h = viewbox_size(svg)
        svg = normalise_root(svg)

        if not animated:
            # mid-loop-ish time in case there is any motion at all
            out = outdir / f"{name}.png"
            shoot(svg, w, h, 0.0, out, tmp)
            blank = is_blank(out)
            if not blank:
                trim(out)
            report.append(dict(name=name, kind="png", file=out.name, w=w, h=h,
                               bytes=out.stat().st_size, blank=blank, frames=1))
            print(f"  {'BLANK!' if blank else 'ok    '} {name}.png  {w:.0f}x{h:.0f}  "
                  f"{out.stat().st_size//1024} KB")
            continue

        frames = []
        for i in range(nframes):
            t = loop * i / nframes
            f = shoot(svg, w, h, t, tmp / f"{name}-{i:03d}.png", tmp)
            frames.append(Image.open(f).convert("RGBA"))
        # crop every frame to the union box so the GIF does not jitter
        boxes = [fr.getchannel("A").getbbox() for fr in frames if fr.getchannel("A").getbbox()]
        if boxes:
            l = max(0, min(b[0] for b in boxes) - 6); t0 = max(0, min(b[1] for b in boxes) - 6)
            r = min(frames[0].width, max(b[2] for b in boxes) + 6)
            b2 = min(frames[0].height, max(b[3] for b in boxes) + 6)
            frames = [fr.crop((l, t0, r, b2)) for fr in frames]

        # flatten onto white: GIF has 1-bit alpha and halos badly otherwise
        flat = []
        for fr in frames:
            bg = Image.new("RGBA", fr.size, (255, 255, 255, 255))
            bg.alpha_composite(fr)
            flat.append(bg.convert("P", palette=Image.ADAPTIVE, colors=128))

        out = outdir / f"{name}.gif"
        flat[0].save(out, save_all=True, append_images=flat[1:],
                     duration=int(loop * 1000 / nframes), loop=0, optimize=True)

        # did the frames actually differ?
        a, b = frames[0].tobytes(), frames[len(frames) // 2].tobytes()
        moved = a != b
        blank = is_blank(tmp / f"{name}-000.png")
        report.append(dict(name=name, kind="gif", file=out.name, w=w, h=h,
                           bytes=out.stat().st_size, blank=blank, frames=len(flat),
                           moved=moved))
        print(f"  {'BLANK!' if blank else 'STATIC!' if not moved else 'ok    '} "
              f"{name}.gif  {w:.0f}x{h:.0f}  {len(flat)} frames  "
              f"{out.stat().st_size//1024} KB")

    shutil.rmtree(tmp, ignore_errors=True)
    (outdir / "manifest.json").write_text(json.dumps(report, indent=2))

    bad = [r for r in report if r["blank"] or (r["kind"] == "gif" and not r.get("moved"))]
    print(f"\n{len(report)} graphics, {len(bad)} problem(s)")
    for r in bad:
        print(f"  PROBLEM: {r['name']} blank={r['blank']} moved={r.get('moved')}")
    return 1 if bad else 0


if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    out = Path(sys.argv[2] if len(sys.argv) > 2 else "graphics")
    sys.exit(main(root, out))
