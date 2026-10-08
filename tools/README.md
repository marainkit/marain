# tools/

Scripts and build tooling. Everything here *consumes* the data in [`../spec/`](../spec/) and [`../language/`](../language/). None of it defines anything.

Run scripts from the repo root.

## Scripts — `scripts/`

| Script | What it does | Output |
|--------|--------------|--------|
| [generate-glyph-index.py](scripts/generate-glyph-index.py) | Builds the glyph index from `spec/glyph-table.tsv` + `spec/phoneme-readings.tsv` | `spec/glyph-index.md` |
| [generate-glyph-table.py](scripts/generate-glyph-table.py) | Builds the interactive web glyph table | `docs/index.html` |
| [generate-glyph-pngs.py](scripts/generate-glyph-pngs.py) | 64 px PNG of every glyph in the table (needs ImageMagick) | `docs/assets/glyphs/NNN.png` |
| [dict-to-tsv.py](scripts/dict-to-tsv.py) | Converts the Marain Tools JS sources to TSV | `language/vocabulary.tsv`, `language/alphabet.tsv` |
| [split-epub.py](scripts/split-epub.py) | Splits a Culture omnibus EPUB into per-book EPUBs | `books/` (gitignored) |
| [rag-extract.py](scripts/rag-extract.py) | Extracts Marain passages, ship names and vocabulary per novel | `sources/novel-extractions/` (gitignored, never commit) |

After editing `spec/glyph-table.tsv`, run the first three.

> ⚠ `docs/index.html` has hand edits that the generator doesn't reproduce (e.g. the *Future Assigned Key* column and multi-value keys like `space / 0 / ?`). Port those into `generate-glyph-table.py` before regenerating, or they'll be lost.

```bash
python3 tools/scripts/generate-glyph-index.py
python3 tools/scripts/generate-glyph-table.py
python3 tools/scripts/generate-glyph-pngs.py      # optional size arg, e.g. 128
```

All renderers use the bit order in [`../spec/grid.md`](../spec/grid.md#bit-order): cell *n* = 2ⁿ, cell 0 top-left. The PNGs are committed so markdown can embed them: `![#121](../docs/assets/glyphs/121.png)` (adjust the `../` to your directory depth).

## Font build — `font/`

[`build.py`](font/build.py) renders glyphs to SVG from the rendering tokens in [`../spec/rendering.md`](../spec/rendering.md) §6.2, and writes [`preview.html`](font/preview.html). Other previews: `preview-squares.html`, `font-comparison.html` (glyph-by-glyph comparison of the reference fonts), `test-bianc.html`.

```bash
python3 -m venv tools/font/.venv && source tools/font/.venv/bin/activate
pip install fonttools ufoLib2
python3 tools/font/build.py
```

Planned pipeline toward installable fonts: cell patterns → `build.py` → UFO (ufoLib2) → TTF/OTF (fonttools), mapped to the Private Use Area from U+E000, monospaced at 1000 units/em with roughly 200-unit cells.

Third-party reference fonts go in `tools/font/examples/`, which is gitignored. Tom Cully's Marain font (© all rights reserved; identical glyphs to the local `MarainBanks` copy) isn't distributed. `docs/index.html` loads it from [tomdionysus/marain-font](https://github.com/tomdionysus/marain-font).

## Claude Code skill — `skill/`

[`skill/marain/SKILL.md`](skill/marain/SKILL.md) gives Claude linguistic and encoding rigour for Marain work. To install it (symlinked, so edits apply immediately):

```bash
./tools/skill/install.sh          # all skills
./tools/skill/install.sh marain   # one skill
```

Then invoke it with `/marain`. The skill is split into portable sections (domain knowledge, scientific standards) and a project-orientation section to replace if you lift it into another project.
