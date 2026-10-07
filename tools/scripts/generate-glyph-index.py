#!/usr/bin/env python3
"""
Generate spec/glyph-index.md from spec/glyph-table.tsv and spec/phoneme-readings.tsv.

Usage:  python3 tools/scripts/generate-glyph-index.py
Output: spec/glyph-index.md  (do not edit by hand)

Bit order: cell n carries 2**n; cell 0 is top-left, row-major (see spec/grid.md).
"""

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SPEC = ROOT / "spec"
INVARIANTS = {0, 16, 170, 186, 325, 341, 495, 511}


def pattern(value: int) -> str:
    """Three rows, top first; cell n is bit n."""
    rows = []
    for r in range(3):
        rows.append("".join("█" if value >> (r * 3 + c) & 1 else "░" for c in range(3)))
    return "`" + "`<br>`".join(rows) + "`"


def msb(value: int) -> str:
    return format(value, "09b")


def clean_name(name: str) -> str:
    name = name.replace("“", "").replace("”", "")
    return re.sub(r"⚠.*$", "", name).strip()


def main() -> None:
    table = list(csv.DictReader(open(SPEC / "glyph-table.tsv", encoding="utf-8"), delimiter="\t"))
    readings = list(csv.DictReader(open(SPEC / "phoneme-readings.tsv", encoding="utf-8"), delimiter="\t"))

    non_phoneme = [r for r in table if r["meaning"] != "Phoneme"]
    agree = [r["phoneme"] for r in readings if r["agree"] == "yes"]

    out = []
    w = out.append
    w("# Glyph Index")
    w("")
    w("> **Generated** by `tools/scripts/generate-glyph-index.py` from [`glyph-table.tsv`](glyph-table.tsv) and "
      "[`phoneme-readings.tsv`](phoneme-readings.tsv). Edit the TSVs, not this file.")
    w("")
    w("Every glyph value with a claim on it. Unlisted values are unassigned. Patterns use the bit order in "
      "[grid.md](grid.md#bit-order): cell *n* = 2ⁿ, cell 0 top-left. Binary is written MSB first.")
    w("")
    w("**Confidence:** `confirmed` — stated in Banks' text · `decided` — marainkit decision or geometry · "
      "`community` — prior art (zakalwe2040) · `open` — competing readings, unresolved.")
    w("")
    w("---")
    w("")
    w("## Structural, numeral and community glyphs")
    w("")
    w("| # | Name | Glyph | Binary | Meaning | Source | Confidence |")
    w("|--:|------|-------|--------|---------|--------|------------|")
    for r in sorted(non_phoneme, key=lambda r: int(r["id"])):
        v = int(r["id"])
        src = r["proposed_by"]
        if v in INVARIANTS:
            conf, meaning = "decided", r["meaning"] + " · invariant"
        elif src == "zakalwe2040":
            conf, meaning = "community", r["meaning"]
        elif v == 1:
            conf, meaning = "confirmed", r["meaning"] + " (Banks fig. 1)"
        else:
            conf, meaning = "decided", r["meaning"]
        w(f"| {v} | {clean_name(r['name'])} | {pattern(v)} | `{msb(v)}` | {meaning} | {src} | `{conf}` |")
    w("")
    w("Emoting glyphs (*paa*, *bay*, *gang*…) are zakalwe2040's, recorded so collisions are visible. "
      "zakalwe2040's *yan* (disgust) sits on #325, a reserved invariant, and is not adopted.")
    w("")
    w("---")
    w("")
    w("## Phonemes — two competing readings")
    w("")
    w("Banks published his 32-letter alphabet only as a low-resolution figure "
      "([`../sources/assets/marain-example-banks.png`](../sources/assets/marain-example-banks.png)). "
      "Only **/w/ = #121** is stated in his text. Two readings of the figure exist in this project:")
    w("")
    w("- **Font reading**: values extracted from the MarainBanks TrueType font (Tom Cully, 2006), "
      "which was built from Banks' alphabet. This is what `glyph-table.tsv` and the "
      "[web table](https://marainkit.github.io/marain/) use.")
    w("- **Image reading**: values read by eye from the figure (March 2026), with /ng/ and /th/ moved off invariant glyphs.")
    w("")
    w(f"They agree on **{len(agree)} of {len(readings)}** phonemes ({', '.join('/' + p + '/' for p in agree)}). "
      "Neither is adopted. Resolving them is an open decision in [decisions.md](decisions.md). Order is Banks' "
      "alphabet order.")
    w("")
    w("| Phoneme | IPA | Font # | Font glyph | Image # | Image glyph | Agree |")
    w("|---------|-----|-------:|------------|--------:|-------------|:-----:|")
    for r in readings:
        f, i = int(r["font_reading"]), int(r["image_reading"])
        mark = "✓" if r["agree"] == "yes" else ""
        conf_p = " (confirmed)" if r["phoneme"] == "w" else ""
        w(f"| /{r['phoneme']}/{conf_p} | {r['ipa']} | {f} | {pattern(f)} | {i} | {pattern(i)} | {mark} |")
    w("")
    w("Collisions to note:")
    w("")
    w("- Font reading /t/ = **#317**, which [grid.md](grid.md#reserved-pending-the-base-question) holds open as zakalwe2040's decimal 8.")
    w("- Font reading /l/ = #187 is one cell away from Cross (#186). That's a legibility risk under the "
      "distinction rules in [rendering.md](rendering.md).")
    w("- Neither reading places a phoneme on an invariant.")
    w("")
    (SPEC / "glyph-index.md").write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {SPEC / 'glyph-index.md'}")


if __name__ == "__main__":
    main()
