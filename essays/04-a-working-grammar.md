![Glyph #16, Point](../docs/assets/glyphs/016.png)

Glyph #16 — Point. An early reading of Banks' alphabet put the phoneme /ng/ here, on top of what the project uses as the decimal point. The reading turned out to be wrong, and /ng/ moved. One value, two registers, one correction — that tension is a theme of this essay.

# A Working Grammar
### What you can actually build, and where the spec runs out

_Fourth in a series. The first essay — [*Engineered Defaults*](https://jlesser.substack.com/p/engineered-defaults) — was about whether languages can be engineered to make particular kinds of thinking cognitively cheap. The second — [*Substrate vs Content*](https://jlesser.substack.com/p/substrate-vs-content) — was about whether designed languages can actually spread. The third — [*Transmission First*](https://jlesser.substack.com/p/transmission-first) — was about the inversion at the heart of Marain's writing system: signal as canonical, glyph as rendering. This one is what it says on the tin: a spec sheet with the seams showing, and the answer to "what is actually solid enough to build with."_

---

## 1. Three kinds of "true"

Every essay in this series has made a claim about Marain. The first claimed its geometry encodes a thesis; the second claimed its substrate is the part that could survive; the third claimed its transmission-first inversion makes survival conceivable. Each of those is an argument about intent, about historical pattern, about design philosophy. They are claims of different kinds, and they are not all equally *settled*.

This essay is a different kind of document. It is not an argument. It is a tour of the spec — the parts that are solid enough that you could hand them to someone and say "build from this," and the parts where you would have to stop and make a choice first.

The organizing principle comes from a note I buried in the third essay: there are three tiers of authority in any claim about Marain, and the whole reconstruction sits on them like a three-legged stool. The legs are different lengths, and it helps to know which is which.

**Canon** — Banks fixed it. The 3×3 slate, 512 states, glyph #1 for the number 1, #121 for the phoneme /w/, base-8 numerals, the rotation constraint (no primary letter may be mistaken for another when turned or mirrored), the 32-phoneme alphabet figure, the single gender-neutral pronoun. This is a small list, and every item on it is precious because there is so little of it. A Few Notes on Marain runs about 800 words. The canon fits in a human short-term memory buffer.

**Consequence** — the geometry forces it; nobody chose it. 512 states follows from 9 binary cells. The 8 invariant glyphs follow from asking "which 3×3 patterns are identical under every rotation and mirror reflection?" Base-8 also sits comfortably on the grid, in a way I'll get to. These are not authorial decisions. They are arithmetic and geometry doing their work. They are also the most stable part of the reconstruction, because they are not negotiable.

**Decision** — the project chose it. The 16-bit packet is a choice. The phoneme corrections where Banks' low-resolution image reads landed on reserved invariant glyphs — those are choices. The layout convention, the rail semantics (or their current absence), the bit-order convention, the glyphs for punctuation and operators Banks didn't enumerate — all choices. They are not arbitrary, and they are documented with rationale, but they are not the same kind of thing as the canon or the consequence.

The payoff line, and the one I want to land before going further: "solid enough to build with" does not mean "canonical." Some of the most buildable parts of Marain are pure geometry Banks never mentioned. Some of the canonical parts are still a fight among reconstructions. The tier that matters for a given question depends on the question.

This essay sorts the whole spec into those three buckets, section by section. What follows is what falls out.

## 2. The slate, settled

The 9-bit slate is the stable centre of the entire project. 512 states. It is not a preference. It is not an interpretation. It is arithmetic — 2⁹ = 512 — and arithmetic does not have a scholarly disagreement.

[Essay 1](https://jlesser.substack.com/p/engineered-defaults) worked through what falls out of that arithmetic unprompted — the eight invariant glyphs, their semantic pairs, the fact that the geometry designs a small hazard vocabulary without anyone intending to. I won't re-argue that here. What matters for this essay is the policy status: closed. The 8 invariant values (#0, #16, #170, #186, #325, #341, #495, #511) are permanently reserved. No phoneme, operator, or vocabulary assignment may use them; the only exceptions are the invariants' own structural meanings — #0 as zero and #16 as the decimal point. Any future assignment that collides with an invariant is a conflict requiring explicit resolution — not a negotiation about whether the invariant is reserved.

This was decided 2026-04-03. It is the least controversial decision in the project, because the geometry did most of the work — it picked the eight. The project only decided to keep them clear.

The 8 invariants divide into two vocabularies — four warning glyphs (Diamond, Cross, Corners, Checkerboard) and four structural delimiters (Empty/Point/Frame/Full) — but that's a project naming choice layered on top of the geometry. The geometry gives you the eight patterns and their symmetry properties. What you call them, and what semantic load you assign them, is downstream.

The slate is done. Everything else is a negotiation with the slate's consequences.

## 3. Numbers, decided

Base-8 numeration is the cleanest example of consequence over canon, so it earns a section to itself.

Banks stated that numerals are in base-8. That makes it canon. The grid also turns out to be a comfortable home for it — though not quite in the way I first argued.

The obvious visual encoding for a digit is the number of filled cells: digit 0 has none, digit 1 has one, and so on up. That's the count-the-dots property — a numeral you can read by inspection, without knowing any binary. Fill all nine cells and you've landed on #511, the Full invariant, which is already spoken for. So count-the-dots tops out at eight filled cells: nine digits, 0 through 8. The geometry rules out a count-the-dots base-10. It does not, strictly, rule out base-9 — an earlier draft of this argument got that wrong. What tips it to base-8 is Banks, plus the grid's three rows of three bits each, which is exactly the size of an octal digit (2³ = 8).

The three-legged stool still lines up: canon (Banks said base-8), consequence (the grid caps count-the-dots below base-10 and splits naturally into 3-bit rows), and decision (marainkit chose the specific sequential-fill mapping — #0, #1, #3, #7, #15, #31, #63, #127 — with Mandarin digit names from the zakalwe2040 reconstruction). The canal was already cut. The project just dug where the water wanted to go.

Honesty beat: base-8 is a hard sell. No human community counts in octal. The first question any reader asks is "why not base-10?" and the answer is "because Banks said so, and because a base-10 numeral can't be read by counting dots without colliding with the Full glyph." The decision is the right one. It is not the friendly one.

## 4. The alphabet, honestly unsettled

The phoneme assignment looked closed for a while. On 2026-04-03 the roadmap logged a decision called *Banks corrected*: adopt all 32 of Banks' phonemes, and move any that landed on a reserved invariant. It didn't stay closed, and the reason is worth telling.

Banks published his alphabet as a figure: 32 phonemes, each next to its 3×3 glyph. Only one value is confirmed in prose — #121 for /w/. The rest have to be read off a small, low-resolution image, and the community has argued over that image for decades. This project ended up with two readings of it. One is a careful by-eye reading of the figure. The other comes from the MarainBanks TrueType font, which Tom Cully built from Banks' alphabet in 2006, and which drives the project's web glyph table. Line them up and they agree on nine phonemes out of thirty-two: /w/, /oh/, /ch/, /v/, /ll/, /ng/, /je/, /oo/ and /th/. The other twenty-three disagree.

Some things hold across both. Neither reading puts a phoneme on one of the eight invariant glyphs: an early read that had /ng/ on Point (#16) and /th/ on Cross (#186) was simply wrong, and /oh/, once misread onto Diamond (#170), is #118 in both. And /w/ = #121 is bedrock, because Banks wrote it down.

What doesn't hold is the idea that this is decided. The repo now carries both readings side by side, labelled, and the phoneme values are an open item rather than a closed one. Convergence between independent readings is the closest thing to evidence a project like this gets — and on twenty-three letters there isn't any yet. "Honestly unsettled" is the status. It's less satisfying than "mostly settled," and more true.

## 5. What the packet costs

This section and the next two deliver threads the third essay explicitly deferred. Here is the first: the density argument.

The packet anatomy, restated briefly. Marain's base encoding unit is 16 bits — two standard bytes. The structure is 1 herald bit + 3 upper rail bits + 9 slate bits + 3 lower rail bits.

```
H  [R₁][R₂][R₃]        ← herald + upper rail
   [ 0][ 1][ 2]         ┐
   [ 3][ 4][ 5]         ├  slate (3×3 — glyph index 0–511)
   [ 6][ 7][ 8]         ┘
   [R₄][R₅][R₆]        ← lower rail
```

The slate is 9 bits. 9 bits do not fit in a single 8-bit byte. The next available power-of-two boundary that holds them is 16 bits — two bytes. Choosing to align to bytes at all is the design decision; once that's made, 16 bits is arithmetic. The 7 bits left over (the rails and herald) are not a wishlist. They are what you get when you put a 9-bit object in a 16-bit container.

The naive read of this — 16 bits per symbol versus ASCII's 8 — makes Marain look like a luxury encoding, and on the alphabet we actually have, the naive read is right. Banks' alphabet is one glyph per phoneme. One glyph per letter, at 16 bits a packet, is twice ASCII's storage per letter. The previous essay got Marain *under* ASCII by assuming glyphs that encode phoneme clusters — one glyph for "str", two or three letters at a time — which works out to about 6.4 bits per letter. But nothing in Banks or the spec defines cluster glyphs. They're a possible Column B design, not a property of Marain, and I shouldn't have leaned on them.

So the honest version: Marain as stored costs roughly double ASCII, and buys 7 bits of per-glyph context that ASCII has no room for at all. Right now those bits are headroom, not payload. Whether the trade is worth making depends entirely on what the rails end up carrying — which is the next section.

## 6. What rides the rails

The straight answer to the question the third essay deferred: nothing yet, on purpose.

The six rail bits (three above the slate, three below) plus the herald bit make 128 possible context states. None are currently assigned. This is not a stall. It is a design discipline the project committed to explicitly: no rail or herald bit gets assigned until the linguistic layer has enough real vocabulary to make the choice with content in hand. Premature assignment locks the wrong semantics. A rail bit assigned to "vowel length" because it seemed plausible at the time turns out to be exactly the bit you needed for "certainty modifier" once the grammar is more developed, and now you have a compatibility problem.

The candidates are well-documented in the project's [packet.md](https://github.com/marainkit/marain/blob/main/spec/packet.md). There are three families of approach.

The **linguistic** model, following zakalwe2040's Tonal Marain: upper rail carries vowel diacritics, lower rail carries secondary vowels, herald marks word or phrase boundaries. This maps cleanly onto existing prior art and would give the language layer a native way to encode tonal and vowel-length distinctions without expanding the slate.

The **contextual** model: rail semantics vary by document type. A code document assigns rails to syntax class (noun, verb, modifier). A narrative text assigns them to stress or tone. An alert surface assigns them to urgency and certainty. The rails describe the glyph's relationship to its context rather than its linguistic properties.

The **mixed** model: herald as a universal frame marker (present in every packet, role fixed), rails as context-assigned (role varies by register). This is architecturally the most flexible and operationally the most complex.

The governing principle, stated as a rule rather than indecision: **no rail or herald bit gets assigned until the language layer has enough vocabulary to make the choice with real content.** Until then, the packet is 9 bits of payload in a 16-bit container with 7 bits of purposefully empty space. This is the responsible way to keep options open — and I want to say that explicitly so it does not read as hand-waving. An empty slot is not a missing feature. It is capacity reserved against an unknown future requirement, which is exactly the right posture for a layer whose semantics depend on a development track that has barely started.

The herald — that single bit at the front of every packet — is the most conspicuously empty slot in the whole system. Role undecided. Frame marker, protocol header, word-boundary signal, or something nobody has thought of yet. One bit, honestly empty. It stays that way until there is a reason not to.

## 7. How you write a word

Once you can encode a single glyph, the next question is how glyphs relate to each other on a page. This is the layout layer, and it is the part of the spec where the most interesting design work is happening and the least is settled.

There are three approaches on the table, and they are not competing — they are nested. Each is a valid answer at a different level of the system.

**Approach 1: Linear.** Left to right, top to bottom, words separated by Empty glyphs (#0). This is the current convention, inherited from UTF-8 and the habits of the English-speaking internet. It works. It is also, as the project's [layout.md](https://github.com/marainkit/marain/blob/main/encoding/docs/layout.md) puts it, "un-Culture-like." A civilisation with no gravitational anchor and a script built to survive rotation should not default to an arrangement that privileges one reading direction.

**Approach 2: Macro 3×3.** A 3×3 block of Marain glyphs arranged into a larger square — nine glyphs in a grid, each cell of the macro-grid containing one 3×3 glyph. The macro grid is readable from any edge, maps the script's own geometry up one scale, and turns a sequence of glyphs into a visually bounded unit that the reader processes as a whole before decomposing.

This is the **Hangul syllable-block move**, and it is the strongest design idea in the layout layer. Korean Hangul composes two to four phonetic letters (jamo) into square syllable blocks — a reader recognizes the block as a unit before decomposing it into its constituent parts. It has been the dominant writing system of a major civilisation for six centuries. A macro 3×3 group of Marain glyphs would function identically: the group is a "word" or morpheme unit, with tighter intra-group spacing and looser inter-group spacing creating the same density rhythm. The script becomes self-similar at two scales — nine bits in a 3×3 grid, nine glyphs in a 3×3 grid, the same geometry composing upward. That is exactly the kind of "more out than you put in" property Essay 1 prized about the invariant glyphs, showing up at the layout layer instead of the encoding layer.

**Approach 3: Radial/fractal.** A centre-emitting arrangement with no start or end — how a Mind would write, when the constraints of sequential human reading do not apply. This is architecturally correct in the sense that it is the most natural output for a consciousness that processes information in parallel across arbitrarily many dimensions. It is also completely impractical for current tooling, human readers, and any display surface that is not a holographic interface inside a General Systems Vehicle. Deferred indefinitely.

The project's recommendation is Approach 2 as the default, with Approach 1 as the fallback for narrow displays and machine interchange. Approach 3 is a research note, not a design target.

Directionality within any of these layouts: a script built to survive rotation, used in zero-g, has no gravitational up. The M1 convention is a *recommended* default direction (left-to-right, top-to-bottom), not a mandatory one. Is a linear layout culturally chauvinist? Partly — but defensibly so. Two forward-facing eyes and a brain hemisphere that strongly prefers sequential processing are mammal traits, not Western ones. Banks wrote the Culture novels in linear English prose for human readers; M1 being book-like at the human-reading layer is the same pragmatic concession. The script is not required to be linear. The default is allowed to be.

## 8. The bit nobody pinned down

The orientation question. Which corner of the 3×3 grid holds bit 0? Read top-left as the high bit — the most significant, the one that contributes the largest value to the index — and glyph #121 (Banks' /w/, the double-u bar-on-the-left) comes out as index 316. It only reads as 121 if top-left is the *low* bit instead, the least significant, with the index value climbing from there.

It turns out Banks did fix it — I just hadn't looked closely enough at his figures. Figure 1 in *A Few Notes on Marain* is the number 1, glyph #1, and it's drawn as a single dot in the top-left corner. So bit 0 is top-left. Add his /w/ — value 121, drawn bar-on-the-left — and the scan direction falls out too: only row-by-row reading turns the bar-left /w/ into 121. The third essay said Banks never pinned this down. He did; it was sitting in a figure thirty pixels wide.

So marainkit's call is barely a call: low bit top-left, rows read left to right and top to bottom, cell *n* worth 2ⁿ — written down as the convention, with Banks' figures as the citation. Of the two community fonts that render Banks' glyphs, only *marain-banks* follows it consistently; *marain-regular* draws #121 mirror-flipped. The project follows *marain-banks*.

The wider point, and the one that earns this section a place in the essay: this is the smallest possible design decision — one convention, one bit's reading order — and it is load-bearing for the deep-time claim in Essay 3. The rendering rule has to stay derivable from the bits. A reader in the far future who recovers a Marain document and the codebook needs to know which way the bits scan. If the convention is not documented — if it is just an inherited habit that every practitioner "just knows" — the system has a single point of failure at the tiniest possible scale. A spec is only as buildable as its least-documented convention. This is that convention for Marain.

## 9. The backlog, shown honestly

The three-tier sorting has been running through all eight preceding sections. Here is the version pulled into one place: the open decisions, collected not as a to-do list but as the honest shape of a reconstruction.

**Rail + herald semantics.** Open, blocked on the language layer maturing. 128 context states, all unassigned, by design. The governing rule is stated above and I will not restate it.

**/wa/ vs #511 conflict.** Zakalwe2040 assigns the all-filled glyph (#511, Full, maximum/critical) to the bilabial approximant /wa/. Banks gives /w/ = #121. marainkit's lean: keep #121. The Full invariant should stay structural. This is not yet formally decided.

**Which reading of Banks' alphabet.** The two readings of the alphabet figure disagree on 23 of 32 phonemes, and neither has been adopted. Until that's settled, nothing in Column B can be built on solid ground.

**Operators on invariants.** zakalwe2040's `+` sits on Diamond, `×` on Frame, and the copula *iz* on Cross. `+` = Diamond has a genuinely good iconic argument (a diamond is a rotated plus); the other two will probably be reassigned.

**Cell shape default: square vs. dot.** The font spec defines four rendering variants (square, rounded, dot, pixel). The default gates the font build pipeline. Square has the highest geometric fidelity. Dot is more visually distinctive and carries Braille resonance. No decision yet.

**Centre-cell salience hypothesis.** The proposal that the centre cell (position 4) has lowest perceptual salience, meaning glyphs differing only in their centre cell should not be adjacent in the vocabulary. This is testable — brief-exposure identification trials at 14px rendering — but has not been tested.

**Column B vocabulary selection.** Deferred. Depends on phoneme authority, tone encoding, register semantics, centre-cell salience validation, and vocabulary provenance. All of those are upstream of this decision, and none of them are settled enough to build on.

**Full 512-state semantic assignment.** The geometry and the invariants are settled. The complete table of which value maps to which phoneme, numeral, operator, punctuation mark, chemical element, and physical constant is not. This is not a gap. It is the working edge of the project. The backlog *is* the project: a small bedrock of canon, a ring of forced consequences, and a frontier of decisions where the work of reconstruction is visibly being done.

Every item on this list has a corresponding entry in the project's [decisions.md](https://github.com/marainkit/marain/blob/main/spec/decisions.md), with options and current leans recorded. None of them is hidden. None is presented as more settled than it is.

## 10. Outside the fictional frame

Step back. What does "a working grammar" mean for a project with no Mind to enforce it, no civilisation to adopt it, no institutional backing of any kind?

The honest answer is the same one Essay 2 arrived at, restated with the evidence of this essay behind it: the buildable part is the substrate. The slate, the packet, the invariants, the layout rule, the bit-order convention — that is the layer that compounds. It is geometry and arithmetic and a small number of documented decisions. It can be handed to someone. It can be implemented. It can be tested.

The grammar proper — phonology, vocabulary, the tonal system, the thing that makes Marain a language rather than a writing system — stays the fun, low-odds content layer. It has to be chosen, not inherited. Every historically parallel says it is the part that does not propagate without institutional conditions that do not exist here. That is not a reason to stop working on it. It is a reason to be honest about which layer is which.

This essay's title is "A Working Grammar," and I want to be precise about what that means. It does not mean the language is ready to speak. It means the parts that *can* be specified, *can* be built from, and *can* survive independent implementation are separated from the parts that are still open, and the boundary between them is marked. The value of the project is not a finished language. It is a spec sheet with the seams exposed — a reconstruction that says "this is settled, this is geometry, this is a decision we made, and this is where the next hour of work would go."

If that sounds like a modest claim for the fourth and final essay of a series: good. Modesty is the right register for a project that is, at bottom, a person in a room with an 800-word canonical source text and a lot of geometry. The design is interesting. The honest accounting of its limits is what makes the interesting parts credible.

---

One last thing, and it is the aspirational note Essay 3 ended on, restated here because it is the only fitting close for a series about a language that was designed to outlast its designers.

The codebook written in Marain — the spec itself, encoded in the language it specifies, kept as part of any sufficiently large Marain document. A Rosetta Stone that is also the language it sits next to. I have not worked out whether this is achievable; the spec has technical content — numerical state values, geometric descriptions — that a phonological language might not be the right tool for. But it is the kind of property a system designed with its own survival in mind could in principle have. It is what the deep-time claim in Essay 3 points toward. And it is the thing that a *working grammar* — not the one we have, but the one we would need — would eventually need to contain.

The series does not end with a bow. It ends with that pointing forward. That seems right for a project whose subject is a language that was never finished, designed by a civilization that never existed, reconstructed by a community that is still deciding what it is building.

---

_This essay was developed with AI-assisted research, outlining, and editing support._

---

## Sources and further reading

**Primary source**
- Iain M. Banks, ["A Few Notes on Marain"](../sources/a-few-notes-on-marain.md). The original technical essay. ~800 words.

**Prior essays in this series**
- [Engineered Defaults](01-engineered-defaults.md) — the design thesis, the geometry, the Sapir-Whorf evidence.
- [Substrate vs Content](02-substrate-vs-content.md) — Esperanto, Hangul, and what helps designed languages propagate.
- [Transmission First](03-transmission-first.md) — signal-primary encoding, the W, Braille, deep-time survival.

**Project documentation**
- [`spec/decisions.md`](../spec/decisions.md) — decision log and full backlog with status, options, and current leans.
- [`spec/glyph-index.md`](../spec/glyph-index.md) — every assigned value, with both phoneme readings side by side.
- [`spec/prior-art-comparison.md`](../spec/prior-art-comparison.md) — Banks vs zakalwe2040: phonemes, numerals, operators.
- [`spec/packet.md`](../spec/packet.md) — the 16-bit packet: herald, rails, slate, lattice; rail candidates; density.
- [`spec/layout.md`](../spec/layout.md) — the three layout approaches (linear, macro 3×3, radial/fractal) and the directionality analysis.
- [`spec/grid.md`](../spec/grid.md) — bit order, the 8 invariant glyphs (policy: closed), numerals.
- [`language/alphabet.md`](../language/alphabet.md) — 32-phoneme inventory with IPA and Marain lexical order.
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — the four-label convention (canonical/inference/project decision/speculative) used in internal documentation.
- [marainkit.github.io/marain](https://marainkit.github.io/marain) — current state of the glyph table.

**Prior art**
- zakalwe2040, [Tonal Marain](https://github.com/zakalwe2040/marain). The most developed community reconstruction; introduced the 4×5 lattice, the abjad organized by place of articulation, and much of the bracket/operator notation adopted by marainkit.
- Marain Tools, [marain-tools.netlify.app](https://marain-tools.netlify.app/). Community vocabulary and alphabet browser.
- Lee and Ramsey, *Hunminjeongeum* — the standard English source on Hangul's design, cited here for the syllable-block composition precedent in §7.
