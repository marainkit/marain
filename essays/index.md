# Essays

Long-form pieces on Marain — the constructed language designed for Iain M. Banks' Culture novels — and what its design choices reveal about language, cognition, and the substrates we transmit meaning across.

These are working drafts. They are written for a general intellectually-curious audience and are intended for cross-posting on Substack and [r/Marain](https://www.reddit.com/r/Marain/). The repository is the source of truth; the published versions will follow.

## Series

1. **[Engineered Defaults](01-engineered-defaults.md)** — Banks' design theory, the geometry of the 3×3 grid, and the Sapir-Whorf evidence behind making egalitarianism cognitively cheap.
2. **[Substrate vs Content](02-substrate-vs-content.md)** — what Esperanto and Hangul tell us about whether designed languages survive at all, and what kind of design choices help.
3. **[Transmission First](03-transmission-first.md)** — the inversion at the heart of Marain's writing system: signal as primary, glyph as rendering, and what that means for substrate independence over very long timescales.
4. **[A Working Grammar](04-a-working-grammar.md)** — the parts of the spec solid enough to actually build with, and the parts where this project has had to make decisions Banks left open.

## Conventions

Each essay is self-contained. Cross-references between essays are kept minimal — readers should be able to enter at any piece without having read the others.

Citations follow standard academic form where empirical evidence is being claimed (the Sapir-Whorf experimental literature, the Esperanto and Hangul historical record). Where the project is making a design decision Banks did not specify, the essay says so explicitly rather than presenting the choice as canonical.

The four-label evidence convention used in the spec and research docs (see [`CONTRIBUTING.md`](../CONTRIBUTING.md)) (`[canonical]` · `[inference]` · `[project decision]` · `[speculative]`) is not used inline in the essay prose — it makes the writing brittle. The same discipline is enforced through phrasing: *Banks states*, *the project takes the position that*, *one plausible reading is*, and so on.

## Corrections

Essays 01–03 are published on Substack, so their text here matches the published versions. These points are corrected in the spec, and in essay 04, which was revised before publication:

- **Rotation (01, 02).** Banks requires that no primary letter can be *mistaken for another* when rotated or mirrored. That's not the same as glyphs reading identically in any orientation: rotated letters are different phonemes. Only the eight invariant glyphs read the same from any side. See [`spec/grid.md`](../spec/grid.md).
- **Banks' stated purpose (01).** *A Few Notes on Marain* says Marain was designed to be culturally inclusive and technically comprehensive. The "values as cognitive default" framing comes from the novels (*The Player of Games*: "language-as-moral-weapon"), not from the essay.
- **How much Banks specified (02).** Banks gave the 3×3 binary system, a 32-letter alphabet figure and (in the novels) the single pronoun. He didn't specify a vocabulary, a morphology or a "9-bit packet". The packet is marainkit's, and tightbeam transmission is novel colour.
- **Bit order (03).** Banks *did* pin bit 0: his Figure 1 draws glyph #1 as the top-left cell, and his /w/ = 121 fixes row-by-row reading. See [`spec/grid.md`](../spec/grid.md#bit-order).
- **Density (03).** The 6.4 bits-per-letter figure assumes glyphs that encode phoneme clusters, which nothing in Banks or the spec defines. With one glyph per phoneme, a 16-bit packet costs about twice ASCII's storage per letter. See [`spec/packet.md`](../spec/packet.md#density--what-the-numbers-actually-say).
- **Invariant glyphs (03).** Banks never mentions the invariants or gives them meanings. They're a mathematical consequence of the grid, and their roles are a project decision.
- **Textiles (03).** The damask-weaving "canonical Banks reference" isn't found in the essay or the extracted novel passages. Treat it as unsourced until a passage turns up.
- **Fonts (03, footnote).** The font in the site's "Banks" column is Tom Cully's MarainBanks (2006). Check whether the "Banks" panel in the five-W figure is TTFTCUTS' *Marain* or Cully's font.
