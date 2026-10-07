# marainkit specification

The normative layer of the repo. Each topic is defined in one file. Everything else links here.

| Doc | Defines | Status |
|-----|---------|--------|
| [glossary.md](glossary.md) | Terms: slate, rails, herald, lattice, packet, nonary, Column A/B | Stable |
| [architecture.md](architecture.md) | The four-layer model, Column A / Column B, one glyph traced from pattern to packet | Stable |
| [grid.md](grid.md) | The 3×3 binary grid, bit order, the 8 invariant glyphs, base-8 numerals | Stable |
| [glyph-index.md](glyph-index.md) | Every assigned glyph value, including both competing phoneme readings | Phonemes open |
| [glyph-table.tsv](glyph-table.tsv) · [phoneme-readings.tsv](phoneme-readings.tsv) | The data behind the index and the [web table](https://marainkit.github.io/marain/) | Data |
| [prior-art-comparison.md](prior-art-comparison.md) | marainkit vs zakalwe2040's Tonal Marain: abjad, numerals, operators, emoting glyphs | Reference |
| [packet.md](packet.md) | The 16-bit packet (herald + rails + slate) and its density | Structure decided, rails open |
| [layout.md](layout.md) | Linear vs macro 3×3 vs radial layout, directionality | Lean: macro 3×3 |
| [rendering.md](rendering.md) | Requirements for any Marain font/renderer | Draft 0.1 |
| [display.md](display.md) | Context model `(type, viewing, status)`, design tokens, status scale 0–8 | Light theme built |
| [decisions.md](decisions.md) | Decision log, open backlog, MVP, implementation stack | Living |
| [validation.md](validation.md) | Testable claims and proposed experiments | Planned |

---

## Design principles

These are the commitments the rest of the spec is judged against. They are `[project decision]`s.

**Foundation**

- **Glyph value is the stable unit.** A glyph is a 9-bit number. Fonts, media and layouts are renderings of it. The value never changes because a rendering changed.
- **Lock the foundation, let the surface move.** Stabilise the smallest core: the grid and bit order, the invariant reservation, the packet structure, the status scale. Explicitly *don't* lock fonts, themes, vocabulary or rendering details. Esperanto froze its *Fundamento* in 1905 and has struggled to evolve since; Hangul kept its featural core and let everything else drift. See [`../research/esperanto-and-hangul.md`](../research/esperanto-and-hangul.md).
- **Canon first, labelled.** Banks-canonical, inferred and project-decided claims are kept visibly separate (see [`../CONTRIBUTING.md`](../CONTRIBUTING.md)).
- **Open space over over-specification.** Where canon is silent and there's no real content to decide with yet, record an open question rather than invent an answer. The unassigned rails are the model case.

**Longevity**

- **100-year horizon.** Prefer open, published, stable formats over convenient current tooling.
- **Substrate independence.** Nothing should need a particular platform, power grid or institution to stay legible. Ideally a human eye is enough.
- **Respect for resources.** No server where a file will do. Plain TSV is canonical; everything else is generated from it.

**Rendering and display**

- **Legibility first. Distinction over harmony.** Every glyph must be distinguishable from every other at the minimum supported size. Aesthetics come second.
- **Token-driven only.** No hard-coded visual values anywhere.
- **Context is explicit.** Rendering adapts to a declared `(type, viewing, status)`, never to guesswork.
- **States scale, don't shout.** Warning and critical are clear without being loud.
- **Working iconicity, not decorative.** A glyph's shape should carry something a reader can use, the way Hangul letters encode articulation.

**Adoption**

- **Additive, not replacement.** Marain should compose with Latin text, JSON and CSS in any proportion, the way Hangul mixed with Hanja. Don't ask anyone to give up what they already use.
- **Politics named.** "Substrate independence" and "no platform dependency" are opinions about platforms and power. Say so rather than pretending to be neutral.
