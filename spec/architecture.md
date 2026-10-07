# Architecture

How the pieces of marainkit fit together: a four-layer model, two composition modes, and one glyph traced from pattern to packet.

---

## Transmission first `[inference]`

Banks designed the grid "so that the language could be rendered into binary code as informationally economically as possible", and he describes a buffer bit for data transmission `[canonical]`. The novels show Marain sent over tight-beam links and broadcast as "standard nonary Marain" `[canonical]`.

This project takes the next step, which is its own reading: **the binary value is the primary form, and the visible glyph is one rendering of it.** A 9-bit number can be drawn, carved, woven, embossed or sent as light pulses. Every one of those is a rendering of the same value. Banks doesn't put it this way, so the claim is labelled `[inference]`.

What follows from that reading:

- the glyph value, not any font, is the unit the spec standardises
- renderers (fonts, the GCU Grey Area tool, PNGs) are interchangeable
- anything that travels *with* a glyph, such as tone or context, can be carried in bits beside it rather than in a separate channel (see [packet.md](packet.md))

---

## Four layers `[project decision]`

```
┌─────────────────────────────────────────────────────┐
│  LAYER 4 — TRANSMISSION                             │
│  Bitstream · framing · error detection · tiers      │  out of scope
├─────────────────────────────────────────────────────┤
│  LAYER 3 — ENCODING                                 │
│  9-bit slate · 16-bit packet · bit order            │  grid.md, packet.md
├─────────────────────────────────────────────────────┤
│  LAYER 2 — LANGUAGE                                 │
│  Phonemes · vocabulary · grammar · tone (open)      │  ../language/
├─────────────────────────────────────────────────────┤
│  LAYER 1 — RENDERING                                │
│  Fonts · layout · display context                   │  rendering.md, layout.md, display.md
└─────────────────────────────────────────────────────┘
```

Layer 3 is the hinge. Language content is encoded into glyph values, and renderers turn glyph values into something visible.

Tone is shown in Layer 2 because a tonal system is one option for the language (zakalwe2040 proposes five tones). Banks specifies no tones. If tone is adopted, it would be carried in Layer 3 bits, most likely the rails.

---

## Column A and Column B

| | Column A | Column B |
|---|----------|----------|
| Input | Any binary, e.g. UTF-8 bytes | Marain phonemes (± tone) |
| Glyph use | All 512 values; the value *is* the glyph | A curated subset with linguistic meaning |
| Layers touched | 3 → 1 | 2 → 3 → 1 |
| Status | Working: [`marainkit/grey-area`](https://github.com/marainkit/grey-area) renders UTF-8 → binary → SVG grids | Research track, blocked on the phoneme table, tone and vocabulary (see [decisions.md](decisions.md)) |

The gap nobody has filled is a tool where you compose in Marain phonemes *and* see the exact bits produced, which bridges Layer 2 and Layer 3. That's the long-term aim.

The Klingon precedent suggests Column B input should look like a romanisation picker that outputs glyphs, not a glyph-grid picker (see [`../research/klingon.md`](../research/klingon.md)).

---

## One glyph, four representations

Every glyph has four forms that convert into each other deterministically. Here is /w/, #121, the one phoneme value Banks states outright.

**1. Pattern.** The cell numbering is defined in [grid.md](grid.md#bit-order) (cell 0 is top-left):

```
cells        /w/ = #121
0 1 2        █ ░ ░
3 4 5        █ █ █
6 7 8        █ ░ ░
```

**2. Value.** The filled cells are 0, 3, 4, 5, 6, so the value is 2⁰ + 2³ + 2⁴ + 2⁵ + 2⁶ = 1 + 8 + 16 + 32 + 64 = **121**.

| Notation | String |
|----------|--------|
| Binary, MSB first (repo convention) | `001111001` |
| Cell order 0→8 (Banks' notation) | `100111100` |

**3. Meaning.** Looked up in [glyph-table.tsv](glyph-table.tsv): phoneme /w/, the first letter of the alphabet, `[canonical]`.

**4. Packet.** With empty rails and herald (layout in [packet.md](packet.md)):

```
H  upper   slate        lower
0  000     001111001    000      = 0000 0011 1100 1000 = 0x03C8 = 968
```

The rendered icon is `docs/assets/glyphs/121.png`. Fonts, PNGs and SVGs all derive from the value. None of them is the glyph.
