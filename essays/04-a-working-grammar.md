![[point-glyph-dual-meaning.png]]
Glyph #16 — Point, which Banks uses as both the decimal point and the phoneme /ng/. The same value in two registers. The tension is a theme of this essay.

# A Working Grammar
### What you can actually build, and where the spec runs out

_Fourth in a series. The first essay — [*Engineered Defaults*](https://jlesser.substack.com/p/engineered-defaults) — was about whether languages can be engineered to make particular kinds of thinking cognitively cheap. The second — [*Substrate vs Content*](https://jlesser.substack.com/p/substrate-vs-content) — was about whether designed languages can actually spread. The third — [*Transmission First*](https://jlesser.substack.com/p/transmission-first) — was about the inversion at the heart of Marain's writing system: signal as canonical, glyph as rendering. This one is what it says on the tin: a spec sheet with the seams showing, and the answer to "what is actually solid enough to build with."_

---

## 1. Three kinds of "true"

Every essay in this series has made a claim about Marain. The first claimed its geometry encodes a thesis; the second claimed its substrate is the part that could survive; the third claimed its transmission-first inversion makes survival conceivable. Each of those is an argument about intent, about historical pattern, about design philosophy. They are claims of different kinds, and they are not all equally *settled*.

This essay is a different kind of document. It is not an argument. It is a tour of the spec — the parts that are solid enough that you could hand them to someone and say "build from this," and the parts where you would have to stop and make a choice first.

The organizing principle comes from a note I buried in the third essay: there are three tiers of authority in any claim about Marain, and the whole reconstruction sits on them like a three-legged stool. The legs are different lengths, and it helps to know which is which.

**Canon** — Banks fixed it. The 3×3 slate, 512 states, glyph #1 for the number 1, #121 for the phoneme /w/, base-8 numerals, the rotation-invariance constraint, the 32-phoneme alphabet figure, the single gender-neutral pronoun. This is a small list, and every item on it is precious because there is so little of it. A Few Notes on Marain runs about 800 words. The canon fits in a human short-term memory buffer.

**Consequence** — the geometry forces it; nobody chose it. 512 states follows from 9 binary cells. The 8 invariant glyphs follow from asking "which 3×3 patterns are identical under every rotation and mirror reflection?" Base-8 follows from the grid in a subtler way I'll get to. These are not authorial decisions. They are arithmetic and geometry doing their work. They are also the most stable part of the reconstruction, because they are not negotiable.

**Decision** — the project chose it. The 16-bit packet is a choice. The phoneme corrections where Banks' low-resolution image reads landed on reserved invariant glyphs — those are choices. The layout convention, the rail semantics (or their current absence), the bit-order convention, the glyphs for punctuation and operators Banks didn't enumerate — all choices. They are not arbitrary, and they are documented with rationale, but they are not the same kind of thing as the canon or the consequence.

The payoff line, and the one I want to land before going further: "solid enough to build with" does not mean "canonical." Some of the most buildable parts of Marain are pure geometry Banks never mentioned. Some of the canonical parts are still a fight among reconstructions. The tier that matters for a given question depends on the question.

This essay sorts the whole spec into those three buckets, section by section. What follows is what falls out.

## 2. The slate, settled

The 9-bit slate is the stable centre of the entire project. 512 states. It is not a preference. It is not an interpretation. It is arithmetic — 2⁹ = 512 — and arithmetic does not have a scholarly disagreement.

[Essay 1](https://jlesser.substack.com/p/engineered-defaults) worked through what falls out of that arithmetic unprompted — the eight invariant glyphs, their semantic pairs, the fact that the geometry designs a small hazard vocabulary without anyone intending to. I won't re-argue that here. What matters for this essay is the policy status: closed. The 8 invariant values (#0, #16, #170, #186, #325, #341, #495, #511) are permanently reserved. No phoneme, numeral, operator, or vocabulary assignment may use them. Any future assignment that collides with an invariant is a conflict requiring explicit resolution — not a negotiation about whether the invariant is reserved.

This was decided 2026-04-03. It is the least controversial decision in the project, because no one made it. The geometry did.

The 8 invariants divide into two vocabularies — four warning glyphs (Diamond, Cross, Corners, Checkerboard) and four structural delimiters (Empty/Point/Frame/Full) — but that's a project naming choice layered on top of the geometry. The geometry gives you the eight patterns and their symmetry properties. What you call them, and what semantic load you assign them, is downstream.

The slate is done. Everything else is a negotiation with the slate's consequences.

## 3. Numbers, decided

Base-8 numeration is the cleanest example of consequence over canon, so it earns a section to itself.

Banks stated that numerals are in base-8. That makes it canon. But the grid *also* forces base-8, for a reason that has nothing to do with Banks' preferences and everything to do with count-the-dots readability — the property that makes a Marain numeral self-explaining by visual inspection.

The argument works like this. In a 3×3 binary grid, the most natural visual encoding for a digit is the number of filled cells: digit 0 has zero cells filled, digit 1 has one cell, and so on up to digit 8 which would have all nine cells filled. But position nine filled is #511 — the Full invariant, which is also the status-escalation maximum and the critical-structural glyph. There is no self-explaining "digit 9." The geometry refuses to let you have base-10 even if you wanted it, because any numeral legible by count-the-dots would collide with itself at 9. The highest digit you can represent unambiguously by counting filled cells is 8, which in this system means digits 0 through 7. Base-8.

The three-legged stool lines up here: canon (Banks said base-8), consequence (the grid cannot encode base-10 by count-the-dots), and decision (marainkit chose to follow both, with the specific sequential-fill mapping and Mandarin-derived digit names from the zakalwe2040 reconstruction). The canal was already cut. The project just dug where the water wanted to go.

Honesty beat: base-8 is a hard sell. No human community counts in octal. The first question any reader asks is "why not base-10?" and the answer is not "because we like octal" — it is "because the grid makes base-10 illegible at the count-the-dots level, and any numeral system that can't be read by counting dots is wasting the grid's main perceptual affordance." The decision is the right one. It is not the friendly one.

## 4. The alphabet, mostly settled

The phoneme assignment was the most contested decision in the project, and it is now closed — closed 2026-04-03, same date as the invariant reservation. The resolution is what the roadmap calls *Banks corrected*.

Here is the problem the decision had to solve. Banks published a glyph table with 32 phonemes. Only one value is confirmed in prose — #121 for /w/. The remaining 31 are approximate visual reads from a low-resolution image, and the image has been argued over for decades. Several of the image-reads land on values that marainkit had already reserved as invariant glyphs. Banks' /ng/ landed on #16 (Point, the decimal point, the singularity glyph). Banks' /th/ landed on #186 (Cross, the alert/stop glyph). Banks' /oh/ landed on #170 (Diamond, the warning/hazard glyph).

Three options presented themselves. Accept the collisions and let dual meaning sort itself out by register. Reassign Banks' phonemes to different values. Or adopt a different phoneme assignment entirely — zakalwe2040's abjad, for instance, which is designed around place of articulation and homoiconicity but is both non-canonical and deeply incompatible with Banks at several points (most critically /wa/ = #511, which is the Full invariant).

The decision was a hybrid. All 32 Banks phonemes are adopted. The two invariant collisions where the image read was clearly wrong (/ng/ on Point, /th/ on Cross) are corrected: /ng/ moves from #16 to #286, /th/ from #186 to #447. The /oh/ on Diamond is provisionally accepted as a dual-meaning case — warning/hazard in the display register, vowel in the linguistic register — and remains an open question. Three hybrid anchors where Banks, zakalwe2040, and marainkit independently agree are treated as bedrock: #121 = /w/, #484 = /m/, #187 = /l/. Convergence across independent reconstructions is the closest thing to evidence a project like this gets, and it is worth naming that as a method point rather than pretending it is canon.

The full assignment is captured in the glyph table at [marainkit.github.io/marain](https://marainkit.github.io/marain). The alphabet layer is not finished — there are still open items (the remaining invariant collisions, the buffer bit as a long-vowel marker, the digit-to-value mapping for base-8) — but the phoneme strategy is decided, and the decisions are recorded with rationale. "Mostly settled" is the honest status. It will do.

## 5. The packet pays for itself

This section and the next two deliver threads the third essay explicitly deferred. Here is the first: the density argument.

The packet anatomy, restated briefly. Marain's base encoding unit is 16 bits — two standard bytes. The structure is 1 herald bit + 3 upper rail bits + 9 slate bits + 3 lower rail bits.

```
H  [R₁][R₂][R₃]        ← herald + upper rail
   [ 0][ 1][ 2]         ┐
   [ 3][ 4][ 5]         ├  slate (3×3 — glyph index 0–511)
   [ 6][ 7][ 8]         ┘
   [R₄][R₅][R₆]        ← lower rail
```

The slate is 9 bits. 9 bits do not fit in a single 8-bit byte. The next available power-of-two boundary that holds them is 16 bits — two bytes. That is not a design choice. It is an arithmetic consequence of aligning a 9-bit value to standard computer storage. The 7 bits left over (the rails and herald) are not a wishlist. They are what you get when you put a 9-bit object in a 16-bit container.

The naive read of this — 16 bits per symbol versus ASCII's 8 — makes Marain look like a luxury encoding. The fair comparison is different, because Marain's Column B glyphs encode phoneme clusters: roughly two to three Latin characters' worth of phonology per symbol. A single Marain glyph representing the cluster "str" is doing the same lexical work as three ASCII characters. At a conservative 2.5 letters per glyph, the 16-bit packet works out to about 6.4 bits per letter. ASCII's 8 bits per character is the baseline; the packet comes in under it, while reserving 7 bits of embedded context that ASCII has no room for at all.

The honest qualifier: the reserved bits only "pay" once they carry something. Right now they are headroom, not payload. The density comparison is real — Marain on the wire is genuinely more compact than ASCII when you account for the phoneme-cluster encoding. The context channels are a promise. Density is a current property. The rails are a future one. Neither claim depends on the other, and I want to keep them separate so the reader can evaluate each on its own terms.

## 6. What rides the rails

The straight answer to the question the third essay deferred: nothing yet, on purpose.

The six rail bits (three above the slate, three below) plus the herald bit make 128 possible context states. None are currently assigned. This is not a stall. It is a design discipline the project committed to explicitly: no rail or herald bit gets assigned until the linguistic layer has enough real vocabulary to make the choice with content in hand. Premature assignment locks the wrong semantics. A rail bit assigned to "vowel length" because it seemed plausible at the time turns out to be exactly the bit you needed for "certainty modifier" once the grammar is more developed, and now you have a compatibility problem.

The candidates are well-documented in the project's [channels.md](https://github.com/marainkit/marain/blob/main/encoding/docs/channels.md). There are three families of approach.

The **linguistic** model, following zakalwe2040's Tonal Marain: upper rail carries vowel diacritics, lower rail carries secondary vowels, herald marks word or phrase boundaries. This maps cleanly onto existing prior art and would give the language layer a native way to encode tonal and vowel-length distinctions without expanding the slate.

The **contextual** model: rail semantics vary by document type. A code document assigns rails to syntax class (noun, verb, modifier). A narrative text assigns them to stress or tone. An alert surface assigns them to urgency and certainty. The rails describe the glyph's relationship to its context rather than its linguistic properties.

The **mixed** model: herald as a universal frame marker (present in every packet, role fixed), rails as context-assigned (role varies by register). This is architecturally the most flexible and operationally the most complex.

The governing principle, stated as a rule rather than indecision: **no rail or herald bit gets assigned until the language layer has enough vocabulary to make the choice with real content.** Until then, the packet is 9 bits of payload in a 16-bit container with 7 bits of purposefully empty space. This is the responsible way to keep options open — and I want to say that explicitly so it does not read as hand-waving. An empty slot is not a missing feature. It is capacity reserved against an unknown future requirement, which is exactly the right posture for a layer whose semantics depend on a development track that has barely started.

The herald — that single bit at the front of every packet — is the most conspicuously empty slot in the whole system. Role undecided. Frame marker, protocol header, word-boundary signal, or something nobody has thought of yet. One bit, honestly empty. It stays that way until there is a reason not to.

## 7. How you write a word

Once you can encode a single glyph, the next question is how glyphs relate to each other on a page. This is the layout layer, and it is the part of the spec where the most interesting design work is happening and the least is settled.

There are three approaches on the table, and they are not competing — they are nested. Each is a valid answer at a different level of the system.

**Approach 1: Linear.** Left to right, top to bottom, words separated by Empty glyphs (#0). This is the current convention, inherited from UTF-8 and the habits of the English-speaking internet. It works. It is also, as the project's [layout.md](https://github.com/marainkit/marain/blob/main/encoding/docs/layout.md) puts it, "un-Culture-like." A civilisation with no gravitational anchor and a rotation-invariant script should not default to an arrangement that privileges one reading direction.

**Approach 2: Macro 3×3.** A 3×3 block of Marain glyphs arranged into a larger square — nine glyphs in a grid, each cell of the macro-grid containing one 3×3 glyph. The macro grid is readable from any edge, maps the script's own geometry up one scale, and turns a sequence of glyphs into a visually bounded unit that the reader processes as a whole before decomposing.

This is the **Hangul syllable-block move**, and it is the strongest design idea in the layout layer. Korean Hangul composes two to four phonetic letters (jamo) into square syllable blocks — a reader recognizes the block as a unit before decomposing it into its constituent parts. It has been the dominant writing system of a major civilisation for six centuries. A macro 3×3 group of Marain glyphs would function identically: the group is a "word" or morpheme unit, with tighter intra-group spacing and looser inter-group spacing creating the same density rhythm. The script becomes self-similar at two scales — nine bits in a 3×3 grid, nine glyphs in a 3×3 grid, the same geometry composing upward. That is exactly the kind of "more out than you put in" property Essay 1 prized about the invariant glyphs, showing up at the layout layer instead of the encoding layer.

**Approach 3: Radial/fractal.** A centre-emitting arrangement with no start or end — how a Mind would write, when the constraints of sequential human reading do not apply. This is architecturally correct in the sense that it is the most natural output for a consciousness that processes information in parallel across arbitrarily many dimensions. It is also completely impractical for current tooling, human readers, and any display surface that is not a holographic interface inside a General Systems Vehicle. Deferred indefinitely.

The project's recommendation is Approach 2 as the default, with Approach 1 as the fallback for narrow displays and machine interchange. Approach 3 is a research note, not a design target.

Directionality within any of these layouts: Marain's rotation-invariance means there is no gravitational up. The M1 convention is a *recommended* default direction (left-to-right, top-to-bottom), not a mandatory one. Is a linear layout culturally chauvinist? Partly — but defensibly so. Two forward-facing eyes and a brain hemisphere that strongly prefers sequential processing are mammal traits, not Western ones. Banks wrote the Culture novels in linear English prose for human readers; M1 being book-like at the human-reading layer is the same pragmatic concession. The script is not required to be linear. The default is allowed to be.

## 8. The bit nobody pinned down

The orientation question. Which corner of the 3×3 grid holds bit 0? Read top-left as the high bit — the most significant, the one that contributes the largest value to the index — and glyph #121 (Banks' /w/, the double-u bar-on-the-left) comes out as index 316. It only reads as 121 if top-left is the *low* bit instead, the least significant, with the index value climbing from there.

Banks never fixed this. He gave us the glyph shapes, he gave us the index values for two of them, and he did not specify which corner maps to which bit position. The community has been arguing about it for as long as there has been a community to argue.

marainkit's call: follow Banks' drawing convention — the bar-on-the-left rendering of #121 — and document the low-bit-at-top-left as a deliberate convention. Of the two community fonts that render Banks' glyphs, only *marain-banks* is internally consistent; *marain-regular* draws #121 mirror-flipped. The project follows *marain-banks*.

The wider point, and the one that earns this section a place in the essay: this is the smallest possible design decision — one convention, one bit's reading order — and it is load-bearing for the deep-time claim in Essay 3. The rendering rule has to stay derivable from the bits. A reader in the far future who recovers a Marain document and the codebook needs to know which way the bits scan. If the convention is not documented — if it is just an inherited habit that every practitioner "just knows" — the system has a single point of failure at the tiniest possible scale. A spec is only as buildable as its least-documented convention. This is that convention for Marain.

## 9. The backlog, shown honestly

The three-tier sorting has been running through all eight preceding sections. Here is the version pulled into one place: the open decisions, collected not as a to-do list but as the honest shape of a reconstruction.

**Rail + herald semantics.** Open, blocked on the language layer maturing. 128 context states, all unassigned, by design. The governing rule is stated above and I will not restate it.

**/wa/ vs #511 conflict.** Zakalwe2040 assigns the all-filled glyph (#511, Full, maximum/critical) to the bilabial approximant /wa/. Banks gives /w/ = #121. marainkit's lean: keep #121. The Full invariant should stay structural. This is not yet formally decided.

**/oh/ on Diamond (#170) and /th/ on Cross (#186).** Banks' low-res image reads put two phonemes on invariant glyphs. /oh/ = Diamond is provisionally accepted as dual-meaning by register. /th/ = Cross has been corrected to #447. The /oh/ decision is open for revision if the language layer produces a collision.

**Base-8 digit value assignment.** 8 digit values need to be assigned. #0 as zero is universally accepted (Empty glyph, *nuul*). The remaining seven have no published values from any source. The sequential-fill rule is the leading candidate — digit 1 = one filled cell, digit 2 = two filled cells, up to digit 7 — but this needs to be formally adopted.

**Cell shape default: square vs. dot.** The font spec defines four rendering variants (square, rounded, dot, pixel). The default gates the font build pipeline. Square has the highest geometric fidelity. Dot is more visually distinctive and carries Braille resonance. No decision yet.

**Centre-cell salience hypothesis.** The proposal that the centre cell (position 4) has lowest perceptual salience, meaning glyphs differing only in their centre cell should not be adjacent in the vocabulary. This is testable — brief-exposure identification trials at 14px rendering — but has not been tested.

**Column B vocabulary selection.** Deferred. Depends on phoneme authority, tone encoding, register semantics, centre-cell salience validation, and vocabulary provenance. All of those are upstream of this decision, and none of them are settled enough to build on.

**Full 512-state semantic assignment.** The geometry and the invariants are settled. The complete table of which value maps to which phoneme, numeral, operator, punctuation mark, chemical element, and physical constant is not. This is not a gap. It is the working edge of the project. The backlog *is* the project: a small bedrock of canon, a ring of forced consequences, and a frontier of decisions where the work of reconstruction is visibly being done.

Every item on this list has a corresponding entry in the project's [roadmap.md](https://github.com/marainkit/marain/blob/main/encoding/docs/roadmap.md), with options and current leans recorded. None of them is hidden. None is presented as more settled than it is.

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
- Iain M. Banks, ["A Few Notes on Marain"](../notes/source/a-few-notes-on-marain.md). The original technical essay. ~800 words.

**Prior essays in this series**
- [Engineered Defaults](01-engineered-defaults.md) — the design thesis, the geometry, the Sapir-Whorf evidence.
- [Substrate vs Content](02-substrate-vs-content.md) — Esperanto, Hangul, and what helps designed languages propagate.
- [Transmission First](03-transmission-first.md) — signal-primary encoding, the W, Braille, deep-time survival.

**Project documentation**
- [`encoding/docs/roadmap.md`](../encoding/docs/roadmap.md) — full decision backlog with status indicators, options, and current leans.
- [`encoding/docs/glyph-decisions.md`](../encoding/docs/glyph-decisions.md) — phoneme comparison tables, numeral assignments, operator decisions.
- [`encoding/docs/channels.md`](../encoding/docs/channels.md) — the 16-bit packet structure: herald, rails, slate, lattice. Rail semantic candidates.
- [`encoding/docs/layout.md`](../encoding/docs/layout.md) — the three layout approaches (linear, macro 3×3, radial/fractal) and the directionality analysis.
- [`encoding/docs/invariant-glyphs.md`](../encoding/docs/invariant-glyphs.md) — the 8 rotation/mirror-invariant glyphs, policy status: closed.
- [`direction/encoding-density-and-packets.md`](../direction/encoding-density-and-packets.md) — the density argument worked out in more technical detail.
- [`language/phonemes/alphabet.md`](../language/phonemes/alphabet.md) — 32-phoneme inventory with IPA and Marain lexical order.
- [`notes/evidence-labels.md`](../notes/evidence-labels.md) — the four-label convention (canonical/inference/project decision/speculative) used in internal documentation.
- [marainkit.github.io/marain](https://marainkit.github.io/marain) — current state of the glyph table.

**Prior art**
- zakalwe2040, [Tonal Marain](https://github.com/zakalwe2040/marain). The most developed community reconstruction; introduced the 4×5 lattice, the abjad organized by place of articulation, and much of the bracket/operator notation adopted by marainkit.
- Marain Tools, [marain-tools.netlify.app](https://marain-tools.netlify.app/). Community vocabulary and alphabet browser.
- Lee and Ramsey, *Hunminjeongeum* — the standard English source on Hangul's design, cited here for the syllable-block composition precedent in §7.
