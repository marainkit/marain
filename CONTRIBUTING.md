# Contributing to marainkit

marainkit mixes four kinds of material: what Banks wrote, what follows from it, what this project decided, and what is still a hypothesis. Most of the work here is keeping those four apart.

---

## Evidence labels

Every claim that isn't obvious from context gets one of four labels. Use these, and only these.

| Label | Meaning | Example |
|-------|---------|---------|
| `[canonical]` | Stated by Banks: *A Few Notes on Marain*, the novels, or his own statements. You can point at the passage. | /w/ is glyph #121. Marain has one gender-neutral personal pronoun. |
| `[inference]` | Follows from canon, logically or mathematically, but Banks didn't say it. | Exactly 8 of the 512 grids are invariant under every rotation and reflection. |
| `[project decision]` | marainkit chose it where canon is silent. Recorded with date and rationale in [`spec/decisions.md`](spec/decisions.md). | The 16-bit packet. Invariants reserved for warning/structural roles. |
| `[speculative]` | A hypothesis worth testing. Not a property the system has. | Macro 3×3 layout improves recall. |

Equivalents you'll meet elsewhere:

| Here | Essays 03–04 | Glyph index "confidence" |
|------|--------------|--------------------------|
| `[canonical]` | canon | `confirmed` |
| `[inference]` | consequence | (geometry) |
| `[project decision]` | decision | `decided` |
| `[speculative]` | — | `provisional` (an unverified reading), `community` (someone else's proposal) |

**How to apply them:** inline in bold before a claim, or in a section heading when the whole section has one status. The essays don't use the brackets. They say "Banks states…", "the project chose…" instead.

### Three common traps

1. **Rotation.** Banks requires that primary letters aren't *confused* when rotated. He does **not** say glyphs read the same in any orientation; rotated forms are different phonemes. Only the 8 invariant glyphs are orientation-free.
2. **Transmission-first.** Banks mentions binary economy and a buffer bit for data transmission. "Glyphs are a debug view of a tightbeam signal" is this project's `[inference]`, not his claim.
3. **"Base-9."** The grid has 9 *binary* cells: 9 bits, 512 states. Nothing in Marain is base-9. Banks' numerals are base-8. See [`spec/glossary.md`](spec/glossary.md).

---

## Tracks

The repo pursues three things. They need different voices.

| Track | What it is | Lives in |
|-------|------------|----------|
| **Reconstruction** | What Banks actually wrote. Scholarly and conservative. | `sources/`, the canonical parts of `spec/` |
| **Specification** | The system marainkit builds on top: packet, glyph policy, rendering, display. Engineering voice, decisions with rationale. | `spec/`, `tools/`, `themes/` |
| **Argument** | Why it matters: cognition, adoption, deep time. Exploratory, every claim hedged. | `research/`, `essays/` |

When these blur, inference starts to look canonical and philosophy starts to look like a requirement.

---

## Where things go

- **One fact, one place.** If a value or decision is defined in `spec/`, other docs link to it rather than restating it.
- **`spec/glyph-table.tsv` is the data.** `spec/glyph-index.md`, `docs/index.html` and the PNGs in `docs/assets/glyphs/` are generated from it (see [`tools/README.md`](tools/README.md)).
- **Decisions** go in the log in [`spec/decisions.md`](spec/decisions.md), with date, decision and rationale. If an open item closes, update its entry. Don't leave a second "open" copy anywhere else.
- **Research notes** go in `research/`. If a note produces a decision, record the decision in `spec/decisions.md` and link back.
- **Scripts** go in `tools/scripts/`. Improve them in place rather than adding variants.
- **Copyrighted text** stays out. Quote Banks briefly, with a citation. Full-text novel extractions are gitignored (`sources/novel-extractions/`).

---

## Notation conventions

- **Glyph numbers** are decimal with `#`: `#121`.
- **Binary strings** are written most-significant-bit first (`121 = 001111001`) unless marked *cell order*. Cell order reads cells 0→8 and is how Banks writes them (`100111100`). See [`spec/grid.md`](spec/grid.md#bit-order).
- **Grid drawings** use `█` (filled) and `░` (empty), top row first.

---

## Working with AI assistants

Context for AI tools lives in plain markdown that anyone can read: this file, [`spec/README.md`](spec/README.md) and [`spec/decisions.md`](spec/decisions.md). If a tool needs a specially named file (`CLAUDE.md` and the like), make it a one-line pointer here rather than a place where content lives. That keeps the project's knowledge independent of any particular tool.

A Claude Code skill for Marain work is in [`tools/skill/`](tools/skill/).
