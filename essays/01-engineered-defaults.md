# Engineered Defaults
### Banks, the Culture, and the mathematics of a designed language

![Marain Font by TTFTCUTS](../notes/assets/marain-TTFTCUTS-font.png)

*Marain glyphs rendered in TTFTCUTS' font. © TTFTCUTS — [Marain font](https://fontstruct.com/fontstructions/show/1446008/marain-5)*

---

Iain M. Banks did something almost no science fiction writer attempts. He didn't just give his civilisation an alien language — he wrote a short technical essay specifying how it worked, and he was explicit about *why* its designers built it the way they did.

The civilisation is the Culture: post-scarcity, anarchist, governed by superintelligent AIs called Minds, spread across a galaxy. The language is Marain. According to Banks, the Minds engineered it at the very beginning of the Culture's existence with a stated purpose — to be culturally inclusive, technically comprehensive, and to make the civilisation's egalitarian values not a rule but a *cognitive default*. The way a language with a single gender-neutral pronoun makes gender-neutral framing free, Marain was meant to make non-hierarchy and non-dominance the path of least resistance.

This is unusual. Most invented languages in fiction are decorative — a few words sprinkled to suggest depth, sometimes a coherent grammar if the author cares enough. Marain is a thesis. Banks claimed, in effect, that a civilisation's language can shape what its inhabitants find easy to think, and that the Culture's Minds had used this property deliberately.

Whether that thesis holds depends on two things. It depends on what Banks himself specified — what is canonical and what is left for readers to fill in. And it depends on what the actual science says about language and cognition. This essay is about both.

## A few notes on Marain

Banks' technical essay — *"A Few Notes on Marain"* — is short. It runs maybe 800 words. He specifies the writing system with mathematical precision and then says comparatively little about the language above it.

Each Marain symbol is a 3×3 binary grid. Nine cells, each filled or empty. There are 2⁹ = 512 possible states, indexed 0 through 511. This is both the visual form (a glyph you can draw) and the transmitted form (a 9-bit number you can send as bits over a tightbeam laser). The same symbol carved in stone, fired across interstellar space, woven into fabric, or drawn on skin is the same number underneath.

![Banks' figures 1–3 from "A Few Notes on Marain"](../notes/assets/marain-a-few-notes-figures-1-3.png)

*Figures 1–3 from Banks' essay. Figure 1 is glyph #1 — the number 1, a single cell at the top-left. Figures 2 and 3 are #0 and #511 — the empty grid and the full grid, the lowest and highest representable values. © Iain M. Banks*

Banks gives us two anchor points and almost nothing else. The number 1 is glyph #1 — a single cell, top-left corner. The phoneme /w/ — the first letter of the Marain alphabet — is glyph #121, which in nine-bit binary is `001111001`. The remaining ~480 states he leaves to "numbers (in base 8), punctuation, and the more common units of measurement, physical and mathematical symbols and constants, chemical elements and so on." He shows a figure of the alphabet but the reproduction is small enough that the community has been arguing for decades about exactly which glyph maps to which phoneme.

He also tells us — and this matters — that the principal alphabetical symbols were chosen so each remained distinguishable from the others under all rotations and mirror reflections. The same script could be read from any side, in any orientation. Rotated versions of glyphs were mostly used for related phonemes, and the whole system was designed with enough flexibility to "accurately, and relatively simply, [...] reproduce any language capable of being spoken by a humanoid."

That is almost the entire technical specification. The math of the grid; two confirmed values; the rotation-invariance constraint; a list of categories the unspecified glyphs cover. The puzzle for everyone who has tried to reconstruct Marain since is what falls out of those constraints, and what doesn't.

## The geometry that designs itself

The 3×3 binary grid has a property Banks probably didn't need to calculate but that drops out of the geometry automatically. Of the 512 possible states, exactly 8 are *fully invariant* under every rotation and every mirror reflection. Whatever angle you read them from, whatever side, they look identical.

These 8 glyphs form four semantic pairs, and once you see them next to each other the structure is hard to unsee.

| Glyph        | Index | Inverse glyph | Index |
|--------------|------:|---------------|------:|
| Empty        |     0 | Full          |   511 |
| Point        |    16 | Frame         |   495 |
| Diamond      |   170 | Checkerboard  |   341 |
| Cross        |   186 | Corners       |   325 |

Each pair is a logical complement: nothing and everything, a single cell and a single gap, sparse alternation and dense alternation, cardinal axis and diagonal axis. The semantics are written into the geometry. They are not Banks' invention; they fall out of asking *which 3×3 patterns are symmetric under all rigid transformations of the square?* The answer is exactly these eight.

This matters for two reasons. The first is practical: invariant glyphs look visually distinct from ordinary text at a glance — the same property that lets a hazard symbol stand out from descriptive signage. A vocabulary of warnings, structural markers, or boundaries that works regardless of orientation or rendering medium is not something you have to *design*. The geometry has already designed it; you just have to notice.

The second reason is more interesting. It is the first hint that Marain has properties the source text doesn't claim and probably didn't intend. Banks gave us a constraint — symbols must remain distinguishable under rotation — and the math of that constraint, applied to a 3×3 binary grid, produces a small, structured, semantically coherent vocabulary as a *consequence*. The script is not just an arbitrary set of shapes that happen to be rotation-friendly. It is a system that, when you push on it, gives you back more than you put in.

That is what a well-designed substrate does.

## Language as a design system

Banks' actual claim — that a language can be engineered to shape how its speakers think — is not, in its weak form, a fictional one. It has a name and a research literature behind it.

The technical name is *linguistic relativity*, often called the Sapir-Whorf hypothesis after the two linguists most associated with it. It comes in two versions, and they have very different evidentiary bases.

The strong version is *linguistic determinism*: language *determines* thought. You literally cannot think what your language cannot express. Almost no linguist holds this view today. People can perceive and reason about things they have no words for; they just do it more slowly and less reliably.

The weak version is what's left after the strong version was falsified in the lab, and it is robust. It says language *influences* thought — the categories your language provides make some distinctions easier to perceive, remember, and act on, and they make others harder. This sounds modest until you look at the experimental evidence.

**Colour.** Russian has obligatory lexical categories for light blue (*goluboy*) and dark blue (*siniy*). They are not optional descriptors; they are the basic-level terms, the way English speakers have "red" and "pink" as separate categories rather than "light red" and "red." In a 2007 study by Winawer and colleagues, Russian speakers discriminated cross-category blues (one *goluboy*, one *siniy*) significantly faster than within-category blues. English speakers, who have one word for both, showed no such asymmetry. The language did not determine what either group could see. It determined which boundaries were cognitively cheap to cross.

**Space.** Some languages use absolute spatial frames — cardinal directions like north and south — instead of body-relative frames like left and right. Speakers of these languages maintain accurate cardinal orientation even in windowless rooms, a feat most English speakers cannot perform without a compass. The linguistic habit builds a persistent mental compass that runs in the background.

**Time.** Mandarin speakers more readily conceptualise time on a vertical axis (earlier = up) than English speakers do. Speakers of Kuuk Thaayorre, an Australian Aboriginal language with absolute spatial reference, lay out time sequences according to cardinal direction rather than body-relative left-to-right. The linguistic frame for time organises how people *physically arrange* temporal information when asked to.

**Grammatical gender.** When Spanish and German speakers describe objects whose grammatical genders differ between the two languages — a bridge is feminine in German, masculine in Spanish — they produce systematically gendered descriptions. The German bridge is "elegant" and "slender"; the Spanish bridge is "strong" and "sturdy." The grammar leaks into conceptual framing even when speakers know perfectly well that the gender assignment is arbitrary.

The consistent finding across all these domains is the same: language doesn't create perceptual *capacity*. It creates perceptual *defaults*. It sets what is fast, cheap, automatic, and socially coordinated, versus what requires deliberate effort.

This is precisely what a design system does.

## Engineered defaults, not engineered constraints

Here is the move that makes Banks' fictional Minds look like they had read the experimental literature.

The naïve way to design a language for egalitarian values would be to *prohibit* hierarchical framing — to make it ungrammatical. This is the strong-version mistake: it tries to determine what speakers can think, and it doesn't work. Speakers always invent workarounds. Banned words become charged words. Forbidden grammar becomes coded grammar. The prohibition itself becomes a marker of the very thing it was supposed to suppress.

The weak-version move is different. You don't ban hierarchical thinking; you stop making it the *path of least resistance*. You build a pronoun system that doesn't sort people by gender by default — speakers can still notice gender, but they have to spend effort to encode it. You build a script with no privileged reading direction — readers can still impose a top-to-bottom hierarchy, but they have to do it consciously. You build a grammar where dominance relationships have no structural shortcut — speakers can still describe dominance, but they have to be explicit about it.

The default shifts. The structure of what is cheap and automatic changes. What people end up doing with the language, on average, when they aren't paying attention, drifts in the direction the designer chose.

This is the deepest alignment between Banks' fiction and the linguistic relativity evidence: **engineered defaults, not engineered constraints.** You don't make people think the way you want. You make the way you want easier to think than the alternative, and you let the cognitive economics do the rest.

It is also why Marain's design choices, taken seriously, are not decorative. The single gender-neutral third-person pronoun, the orientation-invariant glyphs, the engineered phoneme set, the binary-encoded grid — these are claims about what a civilisation's representational defaults would look like if you were trying to make egalitarian thinking the path of least resistance. They are the writing-system equivalent of removing the obligatory "blue is blue" merge in English and replacing it with the obligatory *goluboy/siniy* split. They reshape what is cognitively cheap.

It is worth being explicit about what quiet work the Culture's Minds are doing alongside the language. Marain does not operate in a neutral social substrate. It exists within a civilisation defined by post-scarcity economics, near-perfect conflict mediation, and superintelligent agents that continuously suppress dominance hierarchies and remove material incentives for inequality. Any cognitive bias introduced by the language is therefore inseparable from this broader institutional context. This does not weaken Banks' design hypothesis, but it constrains what the hypothesis actually claims. Marain does not produce egalitarianism on its own. It amplifies and stabilizes a set of values that are already being enforced and reinforced elsewhere. The language is not the foundation of the Culture's social order; it is part of its load-bearing surface.

Whether they would actually produce the claimed civilisational effect is, of course, untested. We have not run the experiment of giving a billion humans a deliberately re-engineered language for several generations and measuring what happens. The Culture novels are a thought experiment about exactly that. The Sapir-Whorf literature gives us the supporting evidence that the thought experiment is at least pointed in a plausible direction.

## The puzzle Banks left

Banks gave us the foundation. He did not give us most of the building.

We have the mathematical structure of the writing system: 3×3 grid, 512 states, indexed 0 to 511. We have two confirmed glyph values: #1 for the number 1, #121 for the phoneme /w/. We have the rotation-invariance constraint and its mathematical consequences. We have a stated design intent — egalitarianism, comprehensiveness, transmission efficiency. We have categorical buckets for the unspecified glyphs (numerals, punctuation, units, constants, elements).

We do not have the full phoneme-to-glyph assignments. We do not have the complete numeral, punctuation, unit, and constant tables. We do not have the grammar. We do not have the tonal system, if there is one. We do not have a specification for how glyphs are arranged spatially when you actually write a sentence or a paragraph — whether they sit on a baseline like Latin, stack like Hangul syllables, tile like Mayan, or do something else Banks didn't describe.

The community has been working on these gaps for decades. The most developed reconstruction — *zakalwe2040*'s tonal Marain — adds a 24-character consonant inventory, five emotional tones, and a 4×5 lattice extending the core 3×3 slate. There are several other partial reconstructions, and they are largely incompatible with each other and only partially consistent with Banks' original.

This is the actual scholarly problem: reconstructing a language from a small number of canonical anchor points and a set of design constraints. It is the same kind of problem as reconstructing a lost grammar from inscriptions — except that the source text is not lost, it just isn't long enough.

## Where this goes next

[*marainkit*](https://github.com/marainkit/marain) is the working name for the project this essay belongs to. Its scope is modest. It studies the published source, reconciles what can be reconciled across the existing reconstructions, and builds working implementations where the spec is solid enough to build on. Where the spec is silent and a choice has to be made, the project says so rather than pretending Banks specified it.

The work is split into three branches.

**Language** is the linguistic layer — phonemes, grammar, tonal encoding, vocabulary. There is a 430-word community vocabulary seeded from prior tools, a working phoneme inventory, and example sentences with glosses. The full grammar and tonal system remain open.

**Encoding** is the glyph layer — all 512 symbols, packet structure for transmission, the mathematics of the grid. This is the layer where the most is settled and where the community has done the most consistent work.

**Display** is the rendering layer — how Marain should look in actual use, across documents, alerts, low-light conditions, high-stakes contexts. This is the layer where most of the engineering thinking happens.

The next essays in this series will follow threads this one has started.

*Substrate vs Content* will look at what Esperanto and Hangul — the two most-studied designed languages in modern history — tell us about whether designed languages survive at all, and what kinds of design choices help.

*Transmission First* will work through the inversion at the heart of Marain's writing system: that the binary signal is primary and the visible glyph is one particular rendering of it, and what that means for substrate independence over very long timescales.

*A Working Grammar* will describe the parts of the system that are solid enough to actually build with — packet structure, status escalation, context model — and the parts where the project has had to make decisions Banks left open.

Banks' design hypothesis — that a language can be engineered to make egalitarian values cognitively cheap — is interesting because the empirical research underneath it is real. The Culture is fiction. The mechanism the Culture's Minds are described as using is not.

That is enough to take the design seriously.

---

## Sources and further reading

**Primary source**
- Iain M. Banks, ["A Few Notes on Marain"](../notes/source/a-few-notes-on-marain.md). The original technical essay. ~800 words.

**Sapir-Whorf empirical literature**
- Winawer, J., Witthoft, N., Frank, M. C., Wu, L., Wade, A. R., & Boroditsky, L. (2007). Russian blues reveal effects of language on color discrimination. *PNAS*, 104(19), 7780–7785.
- Levinson, S. C. (2003). *Space in Language and Cognition*. Cambridge University Press.
- Boroditsky, L. (2001). Does language shape thought? Mandarin and English speakers' conceptions of time. *Cognitive Psychology*, 43(1), 1–22.
- Boroditsky, L., Schmidt, L. A., & Phillips, W. (2003). Sex, syntax, and semantics. In D. Gentner & S. Goldin-Meadow (Eds.), *Language in Mind*.

**Project documentation**
- [`encoding/docs/invariant-glyphs.md`](../encoding/docs/invariant-glyphs.md) — full derivation of the 8 invariant glyphs and their semantic pairs.
- [`notes/sapir-whorf.md`](../notes/sapir-whorf.md) — extended treatment of how the Sapir-Whorf evidence informs the project's design decisions.
- [`notes/rationale.md`](../notes/rationale.md) — the project's broader philosophical position, including which claims are speculative and which are settled.
