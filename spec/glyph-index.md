# Glyph Index

> **Generated** by `tools/scripts/generate-glyph-index.py` from [`glyph-table.tsv`](glyph-table.tsv) and [`phoneme-readings.tsv`](phoneme-readings.tsv). Edit the TSVs, not this file.

Every glyph value with a claim on it. Unlisted values are unassigned. Patterns use the bit order in [grid.md](grid.md#bit-order): cell *n* = 2ⁿ, cell 0 top-left. Binary is written MSB first.

**Confidence:** `confirmed` — stated in Banks' text · `decided` — marainkit decision or geometry · `community` — prior art (zakalwe2040) · `open` — competing readings, unresolved.

---

## Structural, numeral and community glyphs

| # | Name | Glyph | Binary | Meaning | Source | Confidence |
|--:|------|-------|--------|---------|--------|------------|
| 0 | Empty · *líng* · *nuul* | `░░░`<br>`░░░`<br>`░░░` | `000000000` | Silence · null · word space · zero · invariant | marainkit | `decided` |
| 1 | *yī* | `█░░`<br>`░░░`<br>`░░░` | `000000001` | Octal digit 1 (Banks fig. 1) | Banks (implied) | `confirmed` |
| 3 | *èr* | `██░`<br>`░░░`<br>`░░░` | `000000011` | Octal digit 2 | marainkit | `decided` |
| 5 | *paa* | `█░█`<br>`░░░`<br>`░░░` | `000000101` | Fear 😨 | zakalwe2040 | `community` |
| 7 | *sān* | `███`<br>`░░░`<br>`░░░` | `000000111` | Octal digit 3 | marainkit | `decided` |
| 13 | *bay* | `█░█`<br>`█░░`<br>`░░░` | `000001101` | Sadness 😢 | zakalwe2040 | `community` |
| 15 | *sì* | `███`<br>`█░░`<br>`░░░` | `000001111` | Octal digit 4 | marainkit | `decided` |
| 16 | Point | `░░░`<br>`░█░`<br>`░░░` | `000010000` | Singularity · decimal point · invariant | marainkit | `decided` |
| 21 | *gang* | `█░█`<br>`░█░`<br>`░░░` | `000010101` | Affection 😘 | zakalwe2040 | `community` |
| 31 | *wǔ* | `███`<br>`██░`<br>`░░░` | `000011111` | Octal digit 5 | marainkit | `decided` |
| 45 | *buz* | `█░█`<br>`█░█`<br>`░░░` | `000101101` | Overwhelmed 😭 | zakalwe2040 | `community` |
| 62 | *pil* | `░██`<br>`███`<br>`░░░` | `000111110` | Fatigue 🥱 | zakalwe2040 | `community` |
| 63 | *liù* | `███`<br>`███`<br>`░░░` | `000111111` | Octal digit 6 | marainkit | `decided` |
| 85 | *shaa* | `█░█`<br>`░█░`<br>`█░░` | `001010101` | Laughter 🤣 | zakalwe2040 | `community` |
| 127 | *qī* | `███`<br>`███`<br>`█░░` | `001111111` | Octal digit 7 | marainkit | `decided` |
| 149 | *ging* | `█░█`<br>`░█░`<br>`░█░` | `010010101` | Sympathy 🥺 | zakalwe2040 | `community` |
| 170 | Diamond | `░█░`<br>`█░█`<br>`░█░` | `010101010` | Danger · hazard · invariant | marainkit | `decided` |
| 175 | *hub* | `███`<br>`█░█`<br>`░█░` | `010101111` | Love 💛 | zakalwe2040 | `community` |
| 181 | *shacha* | `█░█`<br>`░██`<br>`░█░` | `010110101` | Greetings · peace · hello · bye 🖖 | zakalwe2040 | `community` |
| 186 | Cross | `░█░`<br>`███`<br>`░█░` | `010111010` | Alert · stop · invariant | marainkit | `decided` |
| 220 | *wun* | `░░█`<br>`██░`<br>`██░` | `011011100` | Warmth 💕 | zakalwe2040 | `community` |
| 221 | *zang* | `█░█`<br>`██░`<br>`██░` | `011011101` | Surprise 😲 | zakalwe2040 | `community` |
| 253 | *shuu* | `█░█`<br>`███`<br>`██░` | `011111101` | Infatuation 😍 | zakalwe2040 | `community` |
| 266 | *samara* | `░█░`<br>`█░░`<br>`░░█` | `100001010` | Fascination · logic understood 🤨 | zakalwe2040 | `community` |
| 277 | *mar* | `█░█`<br>`░█░`<br>`░░█` | `100010101` | Joy 😂 | zakalwe2040 | `community` |
| 309 | *hoo* | `█░█`<br>`░██`<br>`░░█` | `100110101` | Happiness 😊 | zakalwe2040 | `community` |
| 325 | Corners | `█░█`<br>`░░░`<br>`█░█` | `101000101` | Boundary · perimeter · limit · invariant | marainkit | `decided` |
| 334 | *fin* | `░██`<br>`█░░`<br>`█░█` | `101001110` | Anger 😡 | zakalwe2040 | `community` |
| 338 | *yam* | `░█░`<br>`░█░`<br>`█░█` | `101010010` | Hope 🙏 | zakalwe2040 | `community` |
| 341 | Checkerboard | `█░█`<br>`░█░`<br>`█░█` | `101010101` | Noise · interference · maximum intensity · invariant | marainkit | `decided` |
| 365 | *shii* | `█░█`<br>`█░█`<br>`█░█` | `101101101` | Synchronicity 😉 | zakalwe2040 | `community` |
| 405 | *shai* | `█░█`<br>`░█░`<br>`░██` | `110010101` | Agreement 👍 | zakalwe2040 | `community` |
| 437 | *zing* | `█░█`<br>`░██`<br>`░██` | `110110101` | Positivity ✨ | zakalwe2040 | `community` |
| 495 | Frame | `███`<br>`█░█`<br>`███` | `111101111` | Enclosure · bracket · container · invariant | marainkit | `decided` |
| 501 | *lang* | `█░█`<br>`░██`<br>`███` | `111110101` | Romance 🥰 | zakalwe2040 | `community` |
| 511 | Full | `███`<br>`███`<br>`███` | `111111111` | Full stop · header · maximum · critical · invariant | marainkit | `decided` |

Emoting glyphs (*paa*, *bay*, *gang*…) are zakalwe2040's, recorded so collisions are visible. zakalwe2040's *yan* (disgust) sits on #325, a reserved invariant, and is not adopted.

---

## Phonemes — two competing readings

Banks published his 32-letter alphabet only as a low-resolution figure ([`../sources/assets/marain-example-banks.png`](../sources/assets/marain-example-banks.png)). Only **/w/ = #121** is stated in his text. Two readings of the figure exist in this project:

- **Font reading**: values extracted from the MarainBanks TrueType font (Tom Cully, 2006), which was built from Banks' alphabet. This is what `glyph-table.tsv` and the [web table](https://marainkit.github.io/marain/) use.
- **Image reading**: values read by eye from the figure (March 2026), with /ng/ and /th/ moved off invariant glyphs.

They agree on **9 of 32** phonemes (/w/, /oh/, /ch/, /v/, /ll/, /ng/, /je/, /oo/, /th/). Neither is adopted. Resolving them is an open decision in [decisions.md](decisions.md). Order is Banks' alphabet order.

| Phoneme | IPA | Font # | Font glyph | Image # | Image glyph | Agree |
|---------|-----|-------:|------------|--------:|-------------|:-----:|
| /w/ (confirmed) | w | 121 | `█░░`<br>`███`<br>`█░░` | 121 | `█░░`<br>`███`<br>`█░░` | ✓ |
| /uh/ | ʌ | 305 | `█░░`<br>`░██`<br>`░░█` | 273 | `█░░`<br>`░█░`<br>`░░█` |  |
| /m/ | m | 484 | `░░█`<br>`░░█`<br>`███` | 457 | `█░░`<br>`█░░`<br>`███` |  |
| /h/ | h | 173 | `█░█`<br>`█░█`<br>`░█░` | 493 | `█░█`<br>`█░█`<br>`███` |  |
| /d/ | d | 403 | `██░`<br>`░█░`<br>`░██` | 480 | `░░░`<br>`░░█`<br>`███` |  |
| /ah/ | a | 143 | `███`<br>`█░░`<br>`░█░` | 456 | `░░░`<br>`█░░`<br>`███` |  |
| /p/ | p | 489 | `█░░`<br>`█░█`<br>`███` | 459 | `██░`<br>`█░░`<br>`███` |  |
| /s/ | s | 342 | `░██`<br>`░█░`<br>`█░█` | 214 | `░██`<br>`░█░`<br>`██░` |  |
| /t/ | t | 317 | `█░█`<br>`███`<br>`░░█` | 168 | `░░░`<br>`█░█`<br>`░█░` |  |
| /ih/ | ɪ | 307 | `██░`<br>`░██`<br>`░░█` | 84 | `░░█`<br>`░█░`<br>`█░░` |  |
| /l/ | l | 187 | `██░`<br>`███`<br>`░█░` | 484 | `░░█`<br>`░░█`<br>`███` |  |
| /tch/ | t͡x | 87 | `███`<br>`░█░`<br>`█░░` | 60 | `░░█`<br>`███`<br>`░░░` |  |
| /k/ | k | 444 | `░░█`<br>`███`<br>`░██` | 312 | `░░░`<br>`███`<br>`░░█` |  |
| /oh/ | o | 118 | `░██`<br>`░██`<br>`█░░` | 118 | `░██`<br>`░██`<br>`█░░` | ✓ |
| /b/ | b | 500 | `░░█`<br>`░██`<br>`███` | 432 | `░░░`<br>`░██`<br>`░██` |  |
| /ch/ | x | 174 | `░██`<br>`█░█`<br>`░█░` | 174 | `░██`<br>`█░█`<br>`░█░` | ✓ |
| /f/ | f | 319 | `███`<br>`███`<br>`░░█` | 56 | `░░░`<br>`███`<br>`░░░` |  |
| /ay/ | aɪ | 490 | `░█░`<br>`█░█`<br>`███` | 2 | `░█░`<br>`░░░`<br>`░░░` |  |
| /v/ | v | 367 | `███`<br>`█░█`<br>`█░█` | 367 | `███`<br>`█░█`<br>`█░█` | ✓ |
| /ll/ | ɬ | 469 | `█░█`<br>`░█░`<br>`███` | 469 | `█░█`<br>`░█░`<br>`███` | ✓ |
| /n/ | n | 251 | `██░`<br>`███`<br>`██░` | 295 | `███`<br>`░░█`<br>`░░█` |  |
| /ee/ | i | 477 | `█░█`<br>`██░`<br>`███` | 50 | `░█░`<br>`░██`<br>`░░░` |  |
| /g/ | g | 242 | `░█░`<br>`░██`<br>`██░` | 120 | `░░░`<br>`███`<br>`█░░` |  |
| /ng/ | ŋ | 286 | `░██`<br>`██░`<br>`░░█` | 286 | `░██`<br>`██░`<br>`░░█` | ✓ |
| /z/ | z | 189 | `█░█`<br>`███`<br>`░█░` | 384 | `░░░`<br>`░░░`<br>`░██` |  |
| /eh/ | ɛ | 483 | `██░`<br>`░░█`<br>`███` | 32 | `░░░`<br>`░░█`<br>`░░░` |  |
| /je/ | jɛ | 431 | `███`<br>`█░█`<br>`░██` | 431 | `███`<br>`█░█`<br>`░██` | ✓ |
| /sh/ | ʃ | 347 | `██░`<br>`██░`<br>`█░█` | 57 | `█░░`<br>`███`<br>`░░░` |  |
| /y/ | j | 247 | `███`<br>`░██`<br>`██░` | 184 | `░░░`<br>`███`<br>`░█░` |  |
| /oo/ | u | 371 | `██░`<br>`░██`<br>`█░█` | 371 | `██░`<br>`░██`<br>`█░█` | ✓ |
| /r/ | r | 509 | `█░█`<br>`███`<br>`███` | 292 | `░░█`<br>`░░█`<br>`░░█` |  |
| /th/ | θ | 447 | `███`<br>`███`<br>`░██` | 447 | `███`<br>`███`<br>`░██` | ✓ |

Collisions to note:

- Font reading /t/ = **#317**, which [grid.md](grid.md#reserved-pending-the-base-question) holds open as zakalwe2040's decimal 8.
- Font reading /l/ = #187 is one cell away from Cross (#186). That's a legibility risk under the distinction rules in [rendering.md](rendering.md).
- Neither reading places a phoneme on an invariant.
