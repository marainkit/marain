# The Grid

The 3×3 binary grid, how its cells map to bits, the 8 glyphs that survive every rotation and reflection, and the numerals.

---

## The slate `[canonical]`

Each Marain symbol is a 3×3 grid of binary cells, which Banks calls a "nine-digit binary number". 2⁹ = **512 glyphs**, #0 (all empty) to #511 (all filled). Banks' Figures 2 and 3 show those two extremes.

## Bit order

```
cell numbers           bit weights
┌───┬───┬───┐         ┌─────┬─────┬─────┐
│ 0 │ 1 │ 2 │         │   1 │   2 │   4 │
├───┼───┼───┤         ├─────┼─────┼─────┤
│ 3 │ 4 │ 5 │         │   8 │  16 │  32 │
├───┼───┼───┤         ├─────┼─────┼─────┤
│ 6 │ 7 │ 8 │         │  64 │ 128 │ 256 │
└───┴───┴───┘         └─────┴─────┴─────┘
```

**Glyph value = sum of the weights of the filled cells.** Cell *n* carries 2ⁿ.

Where this comes from:

- **Bit 0 is top-left** `[canonical]`. Banks' Figure 1 draws the number 1 (glyph #1) as the top-left cell alone ([`../sources/assets/marain-a-few-notes-figures-1-3.png`](../sources/assets/marain-a-few-notes-figures-1-3.png)).
- **Cells run row by row** `[inference]`. Banks gives /w/ = 121 and draws it as a bar down the left column crossed by the middle row. Row-major order gives exactly that shape (`█░░/███/█░░`). Column-major order would give a T-shape instead. Banks' own binary for /w/, `100111100`, is just the cells read 0→8.

So bit order isn't a free project choice. It's fixed by Banks' figures, and every renderer in this repo follows it.

> **History.** An early renderer drew grids rotated 180° (bit 0 bottom-right). It was fixed by mapping cell → 8 − cell. One walkthrough doc also numbered cells MSB-first. Both are superseded by this section.

### Writing binary

The repo writes binary **most-significant bit first**, as ordinary numbers: `121 = 001111001`. When a string is in *cell order* (cell 0 first, as Banks writes it: `100111100`), it's labelled that way. Grid drawings always put the top row first.

---

## The 8 invariant glyphs

### Geometry `[inference]`

Under the eight symmetries of the square (4 rotations × reflection), exactly **8 of the 512 states map to themselves**. Nobody chose them. They're the only grids that look the same whichever way you hold the page. Banks never mentions them.

| # | Name | Pattern | Complement |
|--:|------|---------|-----------|
| 0 | Empty | `░░░` `░░░` `░░░` | Full #511 |
| 16 | Point | `░░░` `░█░` `░░░` | Frame #495 |
| 170 | Diamond | `░█░` `█░█` `░█░` | Checkerboard #341 |
| 186 | Cross | `░█░` `███` `░█░` | Corners #325 |
| 325 | Corners | `█░█` `░░░` `█░█` | Cross #186 |
| 341 | Checkerboard | `█░█` `░█░` `█░█` | Diamond #170 |
| 495 | Frame | `███` `█░█` `███` | Point #16 |
| 511 | Full | `███` `███` `███` | Empty #0 |

Each glyph's pair is its **bitwise complement** (value XOR 511): nothing ↔ everything, one cell ↔ one gap, cardinal ↔ diagonal, sparse ↔ dense alternation.

### Reservation policy `[project decision]` — closed 2026-04-03

The 8 invariant values are reserved for **structural and warning roles**. No phoneme, operator or vocabulary item may take them. Two assignments are part of the invariants' own structural meaning and are explicitly allowed:

- **#0 = digit zero / null / word space**
- **#16 = decimal point / period**

Any other collision is a conflict to resolve, not a reason to reopen the policy. (This wording supersedes the earlier "no numeral may use these values", which contradicted the project's own zero digit.)

### Roles `[project decision]`

| Group | Glyph | Meaning |
|-------|-------|---------|
| Structural | Empty #0 | silence · null · word space · zero |
| | Point #16 | singularity · reference · decimal point |
| | Frame #495 | enclosure · bracket · container |
| | Full #511 | full stop · header · maximum |
| Warning | Diamond #170 | danger · hazard |
| | Cross #186 | alert · stop |
| | Corners #325 | boundary · perimeter · limit |
| | Checkerboard #341 | noise · interference · maximum intensity |

Why this matters: invariant glyphs stand out from ordinary text the way hazard signs do, and they read correctly from any side. That's a safety vocabulary that comes from geometry rather than convention. Whether they really pop out at reading size is untested. See [validation.md](validation.md) claim 1.

### Still open

- **Mapping to the status scale.** No accepted ordering yet. Proposals so far disagree:

  | Glyph | Proposal A (earlier docs) | Proposal B ([sapir-whorf §4.4](../research/sapir-whorf.md)) |
  |-------|---------------------------|--------------------|
  | Empty | 0 | — |
  | Point | 1–2 | — |
  | Frame | 3–4 | — |
  | Corners | 5 | critical |
  | Diamond | 5–6 | attention |
  | Cross | 6–7 | warn |
  | Checkerboard | 7 | system failure |
  | Full | 8 | — |

- **Radical vocabulary.** An invariant before a Column B word could mark its semantic domain, the way Chinese radicals (氵 = water-related) do. See [`../research/cjk-mixed-scripts.md`](../research/cjk-mixed-scripts.md) §3.4.
- **Names.** Sanskrit candidates (*śūnya*, *bindu*, *kṣetra*, *pūrṇa*, …) are in [`../research/sanskrit.md`](../research/sanskrit.md). Note that they assign "boundary" to Cross where the table above gives it to Corners.
- Whether Column A output should highlight invariants.

---

## Numerals

### Base 8 `[canonical]`

Banks: numbers are written "in base 8". Each glyph is one octal digit, and multi-digit numbers read most-significant digit first.

### Sequential fill `[project decision]` — 2026-03-31

Digit *n* is the glyph with the first *n* cells filled, in cell order. Count the dots to read the digit.

| Digit | Name | # | Pattern |
|------:|------|--:|---------|
| 0 | *líng* | 0 | `░░░` `░░░` `░░░` |
| 1 | *yī* | 1 | `█░░` `░░░` `░░░` |
| 2 | *èr* | 3 | `██░` `░░░` `░░░` |
| 3 | *sān* | 7 | `███` `░░░` `░░░` |
| 4 | *sì* | 15 | `███` `█░░` `░░░` |
| 5 | *wǔ* | 31 | `███` `██░` `░░░` |
| 6 | *liù* | 63 | `███` `███` `░░░` |
| 7 | *qī* | 127 | `███` `███` `█░░` |

Names are Mandarin, adopted from zakalwe2040. Digit 1 matches Banks' Figure 1, and digit 0 is the Empty invariant (allowed above).

**On the "geometry forces base-8" argument:** it doesn't. Count-the-dots works for 0–8 filled cells, which is nine digits. Only a tenth digit would need all nine cells, and that's #511 (Full). So the geometry rules out count-the-dots *base-10*, not base-9. Base-8 rests on Banks and on the grid's three 3-bit rows (2³ = 8), not on dot-counting.

### Reserved pending the base question

| # | Pattern | Why held |
|--:|---------|----------|
| 255 | `███` `███` `██░` | The natural sequential-fill "8" |
| 317 | `█░█` `███` `░░█` | zakalwe2040's decimal 8 ⚠ also /t/ in the font reading (see [glyph-index.md](glyph-index.md)) |
| 381 | `█░█` `███` `█░█` | zakalwe2040's decimal 9 |

---

## Beyond nine bits `[canonical]`

Banks: a 10-bit byte gives 1,024 symbols, a 12-bit byte (4,096) is the most common extended form, and a 4×4 grid gives 65,536. Larger grids carry pictograms, alien symbols and diagrams, up to photographs in principle. Data transmission adds a buffer bit after each byte. marainkit works only at 9 bits (M1). Extended forms are out of scope.
