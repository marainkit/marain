# The Packet

> **Status:** `[project decision]`. The 16-bit structure is marainkit's; nothing like it is in Banks. The slate inside it is canonical. Rail and herald meanings are deliberately unassigned.

A 9-bit slate doesn't fit in an 8-bit byte. If you store glyphs in byte-aligned systems (files, network protocols, `uint16` arrays), the smallest container is **2 bytes = 16 bits**, which leaves 7 spare bits. The packet gives those 7 bits a fixed shape so they can later carry context that travels *with* the glyph.

The byte alignment is the choice. Once you make it, 16 bits and 7 spare follow. (Essays 03 and 04 describe this two different ways; this sentence is the reconciliation.)

---

## Layout

```
H  [R₁][R₂][R₃]        ← herald + upper rail
   [ 0][ 1][ 2]         ┐
   [ 3][ 4][ 5]         ├  slate — cells as in grid.md (cell n = 2ⁿ)
   [ 6][ 7][ 8]         ┘
   [R₄][R₅][R₆]        ← lower rail
```

| Field | Bits | As a `uint16` |
|-------|-----:|---------------|
| herald | 1 | bit 15 |
| upper rail R₁R₂R₃ | 3 | bits 14–12 (R₁ = bit 14) |
| slate | 9 | bits 11–3 (slate bit *n* = packet bit *n* + 3) |
| lower rail R₄R₅R₆ | 3 | bits 2–0 (R₄ = bit 2) |

```
packet = (herald << 15) | (upper << 12) | (slate << 3) | lower
```

On the wire it's big-endian, most significant bit first: herald, upper rail, slate (bit 8 down to bit 0), lower rail. The `uint16` mapping formalises the worked examples the project has used all along. Confirming it is listed in [decisions.md](decisions.md).

### Examples (rails and herald empty)

| Glyph | Slate (MSB first) | Packet | Hex | Decimal |
|-------|-------------------|--------|-----|--------:|
| #341 Checkerboard | `101010101` | `0 000 101010101 000` | `0x0AA8` | 2728 |
| #121 /w/ | `001111001` | `0 000 001111001 000` | `0x03C8` | 968 |

### Terms

[slate](glossary.md#slate) (9) · [rails](glossary.md#rails) (6) · [herald](glossary.md#herald) (1) · [lattice](glossary.md#lattice) = rails + slate (15) · [packet](glossary.md#packet) = herald + lattice (16).

---

## Rails and herald: unassigned on purpose

The rails and herald carry **no meaning in M1**. Don't assign them until the language layer has enough real vocabulary to choose with content in hand. Locking one now risks spending the bit you'll later need for something else.

Candidate models:

| Model | Herald | Rails |
|-------|--------|-------|
| **Linguistic** (after zakalwe2040) | word/phrase boundary | upper = vowel diacritics, lower = secondary vowels / tone |
| **Contextual** | — | vary by document type: syntax class in code, stress/tone in text, urgency/certainty on alert surfaces |
| **Mixed** | universal frame marker | context-assigned |

Together the 7 bits give 128 context states. Things that could ride there: status/urgency, surface type, certainty or scope, vowel/tone diacritics, an error-detection bit.

### Relation to zakalwe2040's 4×5 lattice

Tonal Marain wraps the 3×3 slate in upper and lower diacritic rows (4 wide) and a right-hand tonal column. marainkit's lattice keeps the rails, drops the tonal column, and uses the saved bit as the herald, which gives byte alignment. The 4×5 geometry stays the reference design for any future M2 (see [decisions.md](decisions.md)).

### Fonts and rails

- An M1 font may render the slate only. It must still accept a full packet and ignore the non-slate bits.
- Rails, when rendered, are visually subordinate to the slate. They're diacritics.
- A font declares in its metadata whether it renders rails.

---

## Density — what the numbers actually say

| Encoding | Bits per symbol | Symbol carries |
|----------|----------------:|----------------|
| ASCII | 7 (stored as 8) | one Latin character |
| Marain slate | 9 | one glyph |
| Marain packet | 16 | one glyph + 7 context bits |

Banks' alphabet has **one glyph per phoneme** (32 letters). At roughly one glyph per letter, a packet costs 16 bits per letter against ASCII's 8. **As stored, Marain is about twice the size of ASCII**, in exchange for 7 bits of per-glyph context ASCII has no room for.

An earlier argument put the figure at ~6.4 bits per letter. That assumed glyphs encode phoneme *clusters* of about 2.5 letters ("str"). Nothing in Banks or this spec defines cluster glyphs. That remains a possible Column B design `[speculative]` and shouldn't be cited as a property of Marain.

---

## Open questions

- Herald role: start-of-word, start-of-phrase, frame marker, or protocol bit?
- Are rail meanings fixed per tier (M1, M2…) or per context type?
- How does Banks' buffer bit (transmission) relate to the herald (storage)? Both are "one extra bit per glyph".
- A future right-hand tonal rail (6×3 + 1), following zakalwe2040 more closely?
