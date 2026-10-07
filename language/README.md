# language/

The linguistic layer (Layer 2 in [`../spec/architecture.md`](../spec/architecture.md)): phonemes, vocabulary, example sentences.

> **Status:** early. The data here is community-derived ([Marain Tools](https://marain-tools.netlify.app/)) and **not yet reconciled** with Banks' glyph values or marainkit's encoding. Grammar, tone and the phoneme → glyph mapping are open.

---

## What canon gives us

- A **32-letter alphabet**, shown in Banks' figure. /w/ is the first letter `[canonical]`.
- Rotated letters stand for related sounds, and the system aims to reproduce any language a humanoid can speak `[canonical]`.
- **One gender-neutral personal pronoun** (*The Player of Games*) `[canonical]`.
- No published grammar, tones or vocabulary.

This project works only at **M1**, standard nonary Marain.

## Contents

| File | What it is |
|------|------------|
| [alphabet.md](alphabet.md) · [alphabet.tsv](alphabet.tsv) | The 32 letters with IPA, letter names and Marain Tools' sort order (`w` first) |
| [vocabulary.md](vocabulary.md) · [vocabulary.tsv](vocabulary.tsv) | 430-word community vocabulary |
| [sentences.md](sentences.md) | Three example sentences with glosses |
| [raw/](raw/) | The original Marain Tools JavaScript source files |

Phoneme → glyph values are in [`../spec/glyph-index.md`](../spec/glyph-index.md). There are two competing readings.

---

## Priorities

1. **Settle the phoneme → glyph values** (blocked: see [`../spec/decisions.md`](../spec/decisions.md))
2. Grammar: word order, cases, pronouns
3. Tone, if any: whether, how many, and how it's encoded (most likely in the rails)

**Column B** (composing in phonemes with live bit output) is a research track, not active backlog. It depends on all three priorities above, plus register semantics and vocabulary provenance.

## Guard against your own defaults

Esperanto is the warning case. It aimed at neutrality but scores about 75% feature overlap with European languages against a 54% world average, because Zamenhof drew on the languages he knew. A designed language reproduces its designer's languages unless it actively resists them. So phoneme, grammar and vocabulary work here needs a **documented** counterweight: non-Indo-European phonemic features, word orders other than SVO, roots that aren't transparently European.

The community's lean toward Sanskrit and Chinese sources reflects that instinct and Banks' anti-Eurocentrism. Make it an explicit requirement rather than a matter of taste. See [`../research/esperanto-and-hangul.md`](../research/esperanto-and-hangul.md) and [`../research/sanskrit.md`](../research/sanskrit.md).
