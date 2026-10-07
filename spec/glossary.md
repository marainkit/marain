# Glossary

The project's terms. Use them consistently, and link to the term the first time it appears in a document. "Canonical" in this file means *this project's established term*. Where a term comes from Banks, that's noted.

---

## The grid and the glyph

### 3×3 grid
Geometry only: nine cells in three rows and three columns.

### binary cell
One grid cell. It has exactly two states: filled (1) or empty (0). Marain cells are binary. They are not ternary and not base-9.

### slate
The 3×3 binary glyph: the stable 9-bit core unit. Every glyph is defined only by its slate state (index 0–511).

### glyph
One slate state, meaning one filled/empty pattern. There are 512 (#0–#511). "Slate" stresses the encoding unit; "glyph" stresses the visible symbol.

### bit order
Cell *n* carries the bit worth 2ⁿ. Cell 0 is top-left, and cells run left→right, top→bottom. Defined in [grid.md](grid.md#bit-order).

### invariant glyph
One of the 8 glyphs that look identical under every rotation and mirror reflection: #0, #16, #170, #186, #325, #341, #495, #511. See [grid.md](grid.md#the-8-invariant-glyphs).

### nonary Marain
Banks' name for standard Marain, the 3×3 grid (*Excession*: "Based on nine… the three-by-three dot grid"). "Nonary" refers to the **nine cells**, not to nine states per cell. Also called **M1**. *Excession* also mentions an "M32-level" transmission. Higher tiers are out of scope here.

### buffer bit
Banks' extra bit after each 9-bit symbol in data transmission `[canonical]`. Its meaning is unassigned (see [decisions.md](decisions.md)).

### base-8 numerals
Numbers in Marain are octal: digits 0–7 `[canonical]`. marainkit's digit glyphs are in [grid.md](grid.md#numerals).

---

## The packet

### rails
The two 3×1 rows above and below the slate: 6 bits, 3 upper and 3 lower. Context channels whose meanings are unassigned in M1. Replaces "upper/lower channel".

### herald
The single leading bit of the packet. Role undecided. Replaces "preceding bit".

### lattice
The 5×3 visual block of rails + slate (15 bits). The *geometric* view: a font renders a lattice.

### packet
The full 16-bit unit: herald + lattice, 2 bytes. The *encoded* view: a transmitter sends a packet. Replaces "16-bit word" and "semantic packet". Defined in [packet.md](packet.md).

Lattice and packet are kept as separate terms because a font may draw only the lattice while a protocol defines the whole packet.

---

## Modes and scales

### Column A
Arbitrary binary (e.g. UTF-8 bytes) shown as glyphs. Every 9-bit value is its own glyph; there's no vocabulary.

### Column B
Composing in Marain phonemes, possibly with tone. Uses a curated subset of glyphs. A research track, not yet buildable.

### status scale 0–8
The display layer's nine-level state scale: 0–2 normal · 3–5 attention · 6–7 warning · 8 critical. It's a display-layer convention and **not** a property of glyph values. See [display.md](display.md#status-scale).

---

## Terms to avoid

| Avoid | Use instead | Why |
|-------|-------------|-----|
| ternary / three-state cells | binary cells | Cells have two states. |
| base-9 encoding, base-9 grid, base-9 scale | 9-bit slate; status scale 0–8 | 9 binary cells give 2⁹ = 512 states, not 9. |
| "nonary" for a cell | — | Nonary describes the grid's nine cells. |
| preceding bit | herald | |
| upper/lower channel | upper/lower rail | |
| 16-bit word, semantic packet | packet | |
| "readable in any orientation" (for Marain in general) | "non-confusable under rotation" | Only the 8 invariants are orientation-free; rotated letters are other phonemes `[canonical]`. |

### Three different nines

1. **9 cells**: the grid. This is where "nonary" comes from.
2. **9 bits**: the encoding, 512 states.
3. **9 status levels (0–8)**: a display convention, unrelated to the other two.
