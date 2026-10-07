# Prior-Art Comparison: zakalwe2040's Tonal Marain

> **Status:** reference. Lines up the most developed community reconstruction, [zakalwe2040/marain](https://github.com/zakalwe2040/marain) ("Z" below), against Banks and marainkit, so that adoptions and conflicts are visible. Decisions taken from this comparison live in [decisions.md](decisions.md). Z's values were extracted programmatically from the SVGs in that repo (`abjad.svg`, `numerals.svg`, `emojis.svg`, operator sheets).

Z is non-canonical and not endorsed by the Banks estate. It adds a 24-consonant abjad, five tones (named after Mandarin's), vowel diacritics, 22 emoting glyphs, decimal numerals and operator notation. It is written right to left on a **4×5 lattice**: upper and lower diacritic rows, a right-hand tonal column, and the 3×3 slate in the centre.

---

## Phonemes

Banks' values come in two readings (see [glyph-index.md](glyph-index.md)). The Z abjad is organised by place of articulation, and a bare consonant takes a default vowel *a*.

| Phoneme | Banks, font reading | Banks, image reading | Z | Note |
|---------|-------:|--------:|--:|------|
| w / *wa* | **121** | **121** | 511 | Z uses the Full invariant. Banks' only text-confirmed value. |
| m / *ma* | 484 | 457 | 457 | Z = image reading |
| l / *la* | 187 | 484 | 484 | Z = image reading |
| p / *pa* | 489 | 459 | 79 | |
| b / *ba* | 500 | 432 | 295 | font *b* = Z *ka* |
| f / *fa* | 319 | 56 | 173 | font *h* = Z *fa* |
| v / *va* | 367 | 367 | 362 | Banks *v* = Z *sa* |
| th / *tha* | 447 | 447 | 133 | |
| — / *dtha* | — | — | 319 | = font *f* |
| tch / *cha* | 87 | 60 | 127 | Z *cha* = marainkit digit 7 |
| ch | 174 | 174 | — | Banks only |
| — / *dja* | — | — | 465 | |
| t / *ta* | 317 | 168 | 307 | font *ih* = Z *ta* |
| n / *na* | 251 | 295 | 493 | |
| s / *sa* | 342 | 214 | 367 | |
| d / *da* | 403 | 480 | 87 | = font *tch* |
| z / *za* | 189 | 384 | 469 | Z *za* = Banks *ll* |
| r / *ra* | 509 | 292 | 189 | = font *z* |
| sh / *sha* | 347 | 57 | 383 | |
| y / *ya* | 247 | 184 | 468 | |
| g / *ga* | 242 | 120 | 502 | |
| k / *ka* | 444 | 312 | 500 | = font *b* |
| ng / *nga* | 286 | 286 | 509 | = font *r* |
| ah / *aa* | 143 | 456 | 322 | |
| h / *ha* | 173 | 493 | 487 | |

Banks-only vowels and letters: *uh, ih, oh, ay, ee, eh, je, oo, ll*.

**What this shows.** Z and Banks are independent designs on the same grid. Against the image reading they share two values (*ma*, *la*). Against the font reading they share none. The sharpest conflict is *wa* = #511: it overrides the one phoneme value Banks states in prose, and it occupies the Full invariant.

### Z's short-vowel diacritics

| Mark | Position | Vowel |
|------|----------|-------|
| *up* | bar above | *a* /æ/ |
| *out* | dot above start | *u* /ʊ/ |
| *down* | bar below | *i* /ɪ/ |
| *stop* | dot above end | none |

---

## Numerals

| Digit | marainkit (base 8) | Z (base 10) | Conflict |
|------:|-------------------:|------------:|----------|
| 0 | 0 | 341 | Z uses the Checkerboard invariant |
| 1 | 1 | 471 | |
| 2 | 3 | 466 | |
| 3 | 7 | **121** | Z's digit 3 = Banks' /w/ |
| 4 | 15 | 243 | |
| 5 | 31 | 95 | |
| 6 | 63 | 373 | #63 is also Z's `=` |
| 7 | 127 | 125 | #127 is also Z's *cha* |
| 8 | — | 317 | held open in marainkit |
| 9 | — | 381 | held open in marainkit |

marainkit follows Banks' base 8. Z's numerals aren't adopted, though their Mandarin digit *names* are.

---

## Operators and punctuation

| Symbol | Z name | # | marainkit status |
|--------|--------|--:|------------------|
| `+` | — | 170 | 🟡 Diamond invariant. Iconic (rotated plus), still open. |
| `×` | — | 495 | 🟡 Frame invariant. Lean: reassign. |
| `−` | — | 300 | not yet considered |
| `÷` | — | 364 | not yet considered |
| `mod` | — | 301 | not yet considered |
| `&` | *wa* | 284 | 🟢 adopted |
| `\|` | *ow* | 113 | 🟢 adopted |
| `!` | *ma* | 343 | 🟢 adopted |
| `=` | *heeya* | 63 | 🟢 adopted. Note #63 is also marainkit digit 6. |
| `:=` | *kun* | 191 | 🟢 adopted |
| copula | *iz* | 186 | 🟡 Cross invariant. Lean: reassign. |
| `?` | *mahu* | 342 | ⚠ = font reading /s/ |
| `.` | period | 16 | 🟢 = Point invariant (allowed) |
| `,` | comma | 128 | not yet considered |
| `;` | semicolon | 144 | not yet considered |
| `> <` `] [` `) (` `} {` | brackets | 81/276 · 211/406 · 251/446 · 479/503 | 🟢 adopted. Pairs are mirror images. |

⚠ Two adopted values overlap marainkit numerals (`=` #63 = digit 6) or the font reading (`?` #342 = /s/). Recorded here so the next pass over [decisions.md](decisions.md) resolves them.

---

## Emoting glyphs

Z's 22 non-verbal glyphs, in four groups. Values are in [glyph-index.md](glyph-index.md). None is adopted. They're recorded so collisions are visible.

- **Logical:** *shacha* 🖖 greeting/peace · *samara* 🤨 logic understood
- **Positive:** *hub* 💛 love · *zing* ✨ positivity · *yam* 🙏 hope · *wun* 💕 warmth · *shaa* 🤣 laughter · *mar* 😂 joy · *hoo* 😊 happiness · *lang* 🥰 romance · *gang* 😘 affection · *shii* 😉 synchronicity · *shai* 👍 agreement · *zang* 😲 surprise · *shuu* 😍 infatuation
- **Necessary:** *ging* 🥺 sympathy · *bay* 😢 sadness
- **Negative:** *buz* 😭 overwhelmed · *yan* 🤢 disgust (#325, the Corners invariant) · *fin* 😡 anger · *pil* 🥱 fatigue · *paa* 😨 fear

---

## Other community work

- **Reddit conlang** (u/comradelenin456, u/ratioprosperous; r/TheCulture, r/Marain): a synthetic grammar on Banks' alphabet with free word order, no tenses, six cases, fourth-person pronouns and a genderless third person. No glyph extensions. Popular for tattoos.
- **[Marain Tools](https://marain-tools.netlify.app/)** (author unknown): romanised Marain ↔ glyphs ↔ 9-bit binary, plus the dictionary and alphabet used in [`../language/`](../language/). Its example *ra'yuh prenva zawen* is glossed "I am flying aboard a spaceship" ([`../language/sentences.md`](../language/sentences.md)).
- **[tomdionysus/marain-font](https://github.com/tomdionysus/marain-font)**: Tom Cully's TrueType font of Banks' alphabet (2006). The source of the "font reading".
