# Decisions

The single record of what's been decided, what's open, and what's deliberately deferred. When an item changes status, edit it here. Don't keep a second copy elsewhere.

| Status | Meaning |
|--------|---------|
| 🟢 Decided | Closed; rationale in the log |
| 🟡 Open | Needs a decision; lean noted where there is one |
| 🔴 Blocking | Blocks a build target |
| 🔵 Deferred | Consciously parked |

---

## Decision log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-03-31 | **#16 = decimal point / period** | zakalwe2040 uses #16 as the period. It's the Point invariant's own meaning. (Earlier notes credited Banks with this; his essay assigns no value to #16.) |
| 2026-03-31 | **Numerals: sequential fill** #0, #1, #3, #7, #15, #31, #63, #127; Mandarin names *líng*…*qī* | Count-the-dots readable. Digit 1 matches Banks' Figure 1. See [grid.md](grid.md#numerals). |
| 2026-03-31 | ***nuul*** names the null/silence concept of #0 | Distinct from the digit name *líng*. |
| 2026-04-03 | **Number base: 8** | Banks says base 8. It also avoids zakalwe2040's digit 3 = #121 colliding with /w/. |
| 2026-04-03 | **Invariant reservation policy closed** | The 8 invariants are reserved for structural/warning roles. Wording clarified 2026-10 to allow #0 = zero and #16 = decimal point, which were already decided. See [grid.md](grid.md#reservation-policy-project-decision--closed-2026-04-03). |
| 2026-04-03 | **Phoneme strategy: follow Banks' alphabet** (all 32), never on an invariant | Banks' figure is the only canonical alphabet. ⚠ The values are reopened below: two readings exist. |
| 2026-04-03 | **Brackets adopted** from zakalwe2040: `>` 81 · `<` 276 · `]` 211 · `[` 406 · `)` 251 · `(` 446 · `}` 479 · `{` 503 | No conflicts. Open/close pairs are mirror images. |
| 2026-04-03 | **Logic and equality adopted**: `&` 284 · `\|` 113 · `!` 343 · `=` 63 · `:=` 191 | No conflicts. Copula *iz* excluded (see below). |
| 2026-04 | **Implementation stack**: data as TSV/JSON; reference implementation in Python; web in vanilla HTML/JS; graphics in SVG | 100-year horizon. See [below](#implementation-stack). |
| 2026-10 | **Bit order documented as canonical**: cell n = 2ⁿ, cell 0 top-left, row-major | Fixed by Banks' Figure 1 plus /w/ = 121 drawn bar-left. Not a free choice. See [grid.md](grid.md#bit-order). |
| 2026-10 | **Phoneme values: both readings kept, labelled** | The font reading and image reading agree on only 9 of 32. See [glyph-index.md](glyph-index.md). |

---

## Open

### Language and glyph values

**🔴 Phoneme values: font reading vs image reading**
Two readings of Banks' alphabet figure disagree on 23 of 32 phonemes. The font reading (from the MarainBanks TTF) drives the web table today. Options: (a) adopt the font reading, (b) adopt the image reading, (c) produce a third reading at higher resolution and adopt whichever two agree. Points to weigh: the font reading puts /t/ on #317, which is reserved for zakalwe2040's decimal 8, and /l/ on #187, one cell from Cross. **Blocks Column B.**

**🟡 Copula *iz* = #186 (Cross)**
zakalwe2040's copula sits on a warning invariant with no iconic reason. *Lean:* assign *iz* a non-invariant value.

**🟡 `+` = #170 (Diamond)**
A diamond is a rotated plus, which is a genuinely good iconic argument, but it puts arithmetic on a hazard glyph. *Lean:* undecided. Either separate the values, or allow dual meaning by context.

**🟡 `×` = #495 (Frame)**, zakalwe2040's multiplication on an invariant. *Lean:* reassign.

**🟡 Buffer bit as long-vowel flag**
Banks' 10th transmission bit is unassigned. As a long-vowel flag it costs no index space and parallels zakalwe2040's diacritic rows. *Lean:* yes.

**🟡 Base-8 vs universal numerals** (issue #31)
No human community counts in octal. #255, #317 and #381 are held open in case a base-10 layer is ever added.

**🟡 Dictionary details**
The architecture is decided (below). Still open: Wikidata Q-IDs vs OMW synsets (or both), the TSV schema, the offline snapshot strategy, and the TSV → SQLite build.

### Encoding

**🟡 Packet as `uint16`**
Formalise the layout in [packet.md](packet.md#layout) (herald = bit 15 … lower rail = bits 2–0). The worked examples already assume it.

**🟡 Herald and rail semantics**
Deliberately unassigned until the language layer can inform them. See [packet.md](packet.md#rails-and-herald-unassigned-on-purpose).

### Rendering and display

**🟡 Default cell shape: square or dot.** Square is highest fidelity; dot is more distinctive and braille-like. This gates the build pipeline ([rendering.md](rendering.md#7-style-variants)).

**🟡 Centre-cell salience.** Is the centre cell least salient? If so, glyphs that differ only there shouldn't be neighbours in the vocabulary. Testable ([validation.md](validation.md)).

**🟡 Invariants → status scale.** Two incompatible orderings are on file ([grid.md](grid.md#still-open)).

**🟡 Dark mode, HUD context, attention state, syntax-colour tokens.** See [display.md](display.md#roadmap).

### Research questions

- Make Sanskrit the formal structural template (as Mutsun was for Klingon), or keep the multi-source approach?
- Compound grammar for "forced legibility" (social structures as decomposable compounds): which compound types, what order, and how tone registers interact ([`../research/sanskrit.md`](../research/sanskrit.md) Cat. 9).
- Bit cost of three tonal registers (analytical / empathic / critical).
- A proof-of-life translation target.
- A periodic research digest, along the lines of the Klingon Language Institute's journal *HolQeD*.

---

## Deferred

**🔵 Column B vocabulary.** Depends on the phoneme values, tone encoding, register semantics, centre-cell salience and vocabulary provenance. Selection constraints once those settle: no two glyphs from the same rotation/reflection class, minimum Hamming distance 2, high-salience glyphs, no invariants ([rendering.md](rendering.md#53-tier-3-active-vocabulary-column-b)).

**🔵 M2: the 4×5 lattice.** zakalwe2040's geometry is a superset of M1 and would be the reference design. Its phoneme values wouldn't necessarily carry over.

**🔵 Radial / fractal layout.** "How a Mind would write". Not practical for human readers ([layout.md](layout.md)).

**🔵 Encryption tiers.** M1 only. *Excession* mentions M32; nothing else is sourced.

---

## MVP

Narrow goal: show that the glyph system **works, renders correctly, and is legible** before widening scope.

| # | Deliverable | Status |
|---|-------------|--------|
| 1 | Settled terminology ([glossary.md](glossary.md)) | ✅ (the "base-9" sweep is finished in this restructure) |
| 2 | Invariant reservation policy closed | ✅ 2026-04-03 |
| 3 | Glyph index with an explicit confidence on every entry | ✅ structure. Phoneme values are open (see above). |
| 4 | One reference renderer ([`marainkit/grey-area`](https://github.com/marainkit/grey-area)): all assigned glyphs, square + dot variants, ≥ 11 px, a README stating what layer it covers | Partly: verify variants, write README |
| 5 | One macro 3×3 layout experiment | Not started |
| 6 | At least 3 of the [validation](validation.md) tests run, with documented results | Not started |

**Done when** a reader with no prior context can tell from the repo what works, what's tested and what's left.

**Out of scope for the MVP:** Column B, rail/herald meanings, radial layout, the dictionary, M2, formal studies.

---

## Implementation stack

| Layer | Format / language | Why |
|-------|-------------------|-----|
| Data | TSV, JSON, plain UTF-8 | Readable with no software. TSV is canonical. |
| Reference implementation | Python | Ubiquitous and open |
| Web | Vanilla HTML + JS | Runs anywhere with no build step |
| Graphics | SVG | Open, stable spec |

Define data first. Code consumes it. Strong later candidates: **C** (the most substrate-independent renderer possible) and **Lua** (embeddable). Excluded: Swift/Kotlin (platform-locked), TypeScript (adds a compile step), Rust (heavy toolchain for a 100-year horizon), Electron/React Native (framework churn).

## Dictionary architecture

The dictionary maps **Marain → concept ID**, not Marain → English. Translations into any language are derived on demand from an external concept graph.

```
Marain word  →  concept ID (Wikidata Q-ID and/or OMW synset)  →  translation in any language
```

| Format | Role |
|--------|------|
| TSV | Canonical source, one entry per line, diffable |
| SQLite | Generated local index, single file, no server |
| JSON Lines | Interchange |
| RDF N-Triples | Linked-data export |

Server-dependent stores (Postgres, MongoDB, Neo4j) fail the substrate test.
