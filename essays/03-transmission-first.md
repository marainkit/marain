![[00-header-W-eb-garamond-light.png]]
The capital letter W, set in EB Garamond — Georg Duffner and Octavio Pardo's free, open-source revival (SIL Open Font License) of Claude Garamond's sixteenth-century types.
# Transmission First
### Signal as the canonical form, glyph as a rendering choice

_Third in a series. The first essay - [*Engineered Defaults*](https://jlesser.substack.com/p/engineered-defaults) - was about whether languages can be engineered to make particular kinds of thinking cognitively cheap. The second - [*Substrate vs Content*](https://jlesser.substack.com/p/substrate-vs-content) - was about whether designed languages can actually spread far enough to do that work. This one is about the part of Marain that's specifically unusual: the writing system, and the design choice that put the binary signal at the canonical layer and the visible glyph at the rendering layer._

---

## The National Association of W Lovers

W is the first letter Iain M. Banks specified in the Marain alphabet. I can't help thinking Banks would be drawn to a letter that wears its own compositional history on its face: it is visibly two glyphs welded into one. It's a letter that refuses to hide its construction - that's exactly the design value Marain encodes elsewhere. Decompose the concept, show the mechanism, don't let the unit pretend it's primitive. A language consciously designed by the Minds to be inclusive and non-native to everyone equally — a deliberate constructed common tongue — choosing the most conspicuously constructed, borrowed, assembled letter as its anchor has a self-aware wit to it.

W is a late arrival. The Old English scribes of the seventh century didn't have a Latin letter for the **/w/** sound, so they wrote two u's next to each other - "uu," literal double-u, which is also where the modern name of the letter comes from. The Anglo-Saxons preferred the runic letter wynn (ƿ) for a couple of centuries, but on the continent the Carolingian scribes kept using uu, and after the Norman Conquest the ligatured form drifted back across the channel and took over. By 1300, ƿ was out and W was in. The shape kept moving - uu (English: double-u), vv (French: double vé), W, variously joined or unjoined depending on the era - until 15th-century printers more or less locked in the angular version we use now.

Modern fonts still disagree about the interior angles. Pick up two different sans-serifs and lay their W's next to each other and you'll see two different shapes. The encoding doesn't care. ASCII assigned the letter W the value 87 (binary `1010111` - a 7-bit code, padded into an 8-bit byte as `01010111`) in 1963, after roughly three thousand years of glyph design had already settled the question of what a W was. The encoding is downstream of the visible mark. The visible mark itself is canonical. Whatever any given font is doing with the diagonals, the underlying claim "this is a W" is something the typographer inherited from the scribes who inherited it from earlier scribes, all the way back. Glyph first. Encoding second.

That's how every writing system in current daily use works. Including the one this page is rendered in.

Before getting to Marain, I'm going to have to take a small detour through another place this pattern shows up. Louis Braille invented his writing system in 1824, when he was fifteen, and he wasn't trying to encode the Latin alphabet. He was designing a tactile system for blind readers, and what he started from was the cell - a 2x3 grid of dot positions, six dots total, sixty-four possible states. The dots are the canonical thing. The letter assignments are downstream. Braille looked at his 64 cells and parceled them out to letters of the French alphabet, and later other languages, and later mathematical operators and punctuation and music notation. The cell came first. The correspondence to written language came second.

Braille has since survived four substrate transitions - embossed paper, mechanical Braille typewriters, refreshable Braille displays, Unicode code points (`U+2800` through `U+28FF`, for the curious) - and the dot pattern has carried across each one. Each substrate transition required somebody to write a new render function. The canonical dots didn't move.

The Marain letter for **/w/** is glyph 121 - the bits `001111001`. Banks draws it bar-on-the-left, on a 3x3 grid:

```
* . .
* * *
* . .
```

Those asterisks and dots are themselves a rendering - the ASCII one, the crudest there is, the version any keyboard can type. A real Marain font draws the same nine bits as connected strokes, and the result looks nothing like these boxes; I'll line a few up later. Boxes or strokes, it's the same glyph.

Read that grid the obvious way - top-left cell as the high bit, down to bottom-right - and you get `100111100`, which is 316, not 121. It only comes out 121 if the top-left cell is the *low* bit instead, the least significant, with the value climbing from there. Which corner holds bit 0 is a convention Banks never pinned down; I come back to it later.[^orient]

The Braille letter W is dots 2, 4, 5, and 6[^braile]. Drawn out:

```
. *
* *
. *
```

Put the Braille W next to the Marain **/w/** and the coincidence is there; mirror images. Marain's **/w/** runs its bar down the left column; Braille's runs down the right. Reflect either one across a vertical axis and they land on the same skeleton: vertical bar, crossed middle row, gaps top and bottom.[^consistent] Two designers, a fictional starship civilization and a fifteen-year-old in 1824 Paris, reaching independently for mirror images of the same cellular W. It's possible that this is the reason **/w/** is the first letter of the Marain alphabet; it's a deep cut for the linguists, I suppose. The other possibility is that I've been looking at these glyphs too long.

I bring this up partly because the visual coincidence is hard to resist, but also because Braille is the version of this that's already in the world. A binary-first cellular-grid writing system, in active daily use, running its inversion experiment for two centuries. Hold onto that two-century run - it's a small-scale rehearsal for the property I actually care about, the one that only shows up on a much longer clock. The substrate-independence I'm about to attribute to Marain isn't an exotic property somebody made up for a science fiction novel. It's a property a fifteen-year-old in Paris built into a tactile alphabet before [Babbage](https://www.sciencemuseum.org.uk/objects-and-stories/charles-babbages-difference-engines-and-science-museum) finished the difference engine. Marain isn't a one-of-one. It's the second example we have of a script where the signal came first.

So, Marain inverts the natural-script order.

The 3x3 binary grid is the canonical unit. The visible glyph is one particular way of rendering it - a font's interpretation, or a sequence of bits transmitted as light pulses over a tightbeam laser, or a pattern of dots in a textile (the canonical Banks reference, where [damask](https://en.wikipedia.org/wiki/Damask) weavers' patterns can carry Marain text without the weaver needing to know they're carrying anything). The bits don't change. The renderings can.

It's worth considering how strange this is for a moment, because we don't have many examples of it. Almost every script you're familiar with came up the other way. Cyrillic, Hangul, Devanagari, Arabic, Chinese characters, Modern Hebrew, every Latin-derivative alphabet from Vietnamese to Esperanto - all glyph-primary and substrate-derivative. Braille and Marain are the two examples I can find where the canonical artifact is the bit pattern and the visible-or-tactile rendering is downstream.

Two designed scripts: one for the blind, one for a fictional space civilization. That's the company we're keeping.

## The 5 W's

The Marain glyph for **/w/** has been drawn into a number of free fonts that I can find on the internet. They all generally reflect the original version Banks drew in "A Few Notes on Marain".

![[5-Ws-7.jpg]]


All five are the same glyph[^fonts]. The ASCII boxes - the asterisks-and-dots I drew the glyph in up top - are obviously the crudest rendering of the lot, but none of them is more correct than any other. They are all reading from the same 9-bit value. They disagree about how to draw it. The drawing isn't what the glyph is.

For comparison, here's the Marain **/w/** next to the Braille W:

![[02-marain-w-vs-braille-w-2.png]]

Different cellular grid - 2x3 versus 3x3 - but the same **/w/** phoneme being rendered, and the two are mirror images of each other. Marain's bar sits on the left, Braille's on the right; reflect one across a vertical axis and, setting aside Marain's third column (it has no counterpart in the 2-wide Braille cell), they coincide. That leftover column is doing the indexing work, the bits that distinguish glyph 121 from its neighbors in the 512-state space. Strip it off, mirror what's left, and you're looking at a Braille W.

This is the move Unicode doesn't make - and it's worth being precise, because Unicode and Marain are built the same way at the top. Both put an abstract unit at the canonical layer and leave the visible mark to a renderer; Unicode's own first rule is "characters, not glyphs." So the difference isn't that Unicode puts the glyph first. It's what the abstract unit *is*. A Unicode code point is an opaque index - `U+0057` is a pointer to a letter whose shape was inherited from existing scripts and lives in a font, drawn by someone who already knew what a W looked like. You can't derive the glyph from the number; you look it up. A Marain 9-bit value isn't a pointer to a glyph, it *is* the glyph: the bits say which cells are filled, and the geometry does the rest, with no font and no inherited hand required. Emoji make the gap obvious - Apple, Google, and Microsoft all ship different pictures for the same code point precisely because the code point doesn't specify the picture. Marain's values do. That's the contrast: not abstract versus visible, but a label that indexes an inherited shape versus a value that generates the shape from a rule.[^generative]

## The packet, decided (by marainkit, mostly)

A quick note of honesty before I get ahead of myself, because it matters for everything downstream.

Three different things get called "Marain" in this section, and they don't all carry the same authority. The 3x3 binary slate, and the handful of glyph values Banks fixed in his essay (#1 for "one," #121 for **/w/**), are canon - Banks's own. The 512-state space and the eight rotation-invariants are mathematical consequences of the grid; nobody decided them, they just exist. Everything from here up - the 16-bit packet, the byte-alignment choice, the rails, the herald, and whatever any of them eventually carry - is marainkit's, uh, mine: a project layer on top of Banks, and in several places not yet decided at all. I'll flag which is which as we go. The thesis of this essay rides on the first tier. The rest is design.

The slate - the 3x3 grid - is 9 bits, because that's what 3x3 binary means. Three rows by three columns is nine cells. Each cell can be filled or empty. There are 512 possible states. None of that is a choice; it's a consequence of starting from a 3x3 grid.

The packet that wraps the slate is 16 bits. That part IS a choice - and it's marainkit's, not Banks's.

A 9-bit value is one bit too many to fit in a single byte. Modern computing infrastructure runs on bytes, on multiples of eight - the file you're reading this in is bytes, the network protocol that delivered it to your screen is bytes, the CPU register that's holding the next character is some multiple of bytes wide. A 9-bit value doesn't fit. The next available power-of-two boundary is 16 bits, which is two bytes. The project chose to ride that boundary because that's how Marain text gets to travel through software written for systems that assume byte alignment. Without it, every implementation of Marain would have to deal with the off-by-one awkwardness of packing 9-bit values into 8-bit byte streams. The interop cost is real, and the choice was to eat it at the wire-format level rather than push it onto every downstream implementation.

So the canonical signal is 9 bits. The wire format is 16. The difference - the 7 leftover bits - is where the project's design choices live, and where most of them are still open.

The 7 extra bits are structured as six rail bits and one herald bit. The full packet:

![[03-packet-anatomy 4.jpg]]

The herald is a single bit whose function the project hasn't decided yet. The rails are six bits of context - 64 possible states - meant to ride with the symbol rather than getting declared somewhere else in the document. What rides on the rails is still rattling around in my head (there's a design document called [channels.md](https://github.com/marainkit/marain/blob/main/encoding/docs/channels.md) that has the running thread, and as of now it carries no assigned meaning), but the candidates are things like: what kind of surface is this glyph rendering on (a document page, a status display, an alert on a ship's HUD), how urgent is the content, how certain is the speaker, what register is the language in. ASCII does not carry any of this. ASCII can't. There's no room.

Now for the part that should flip the reader's intuition, because the naive read here is that 16 bits per symbol is double ASCII's 8 and therefore wasteful. The math says otherwise.

Marain glyphs in the phoneme-cluster vocabulary - the part of the 512-state space Banks reserved for actual language sounds - encode about two to three Latin characters' worth of phonology per symbol. A single Marain glyph that represents the cluster "str" is doing roughly the same lexical work as three ASCII characters. At a conservative 2.5 letters per glyph, the 16-bit packet works out to about 6.4 bits per letter. The fair comparison is stored size against stored size, and there the two encodings rhyme: ASCII rounds a 7-bit character code up to an 8-bit byte; Marain rounds a 9-bit glyph up to a 2-byte packet. Both pay the same byte-alignment tax. Measured as bytes on the wire, Marain's 6.4 bits per letter still comes in under ASCII's 8 - and it does so while reserving 7 bits per glyph that ASCII has no room for at all. Whether those reserved bits turn into real payload depends on rail and herald assignments the project hasn't made yet; for now the honest claim is that Marain is denser as stored, with headroom ASCII can't match - not that the context channels are already earning their keep.

This is going to get more developed in the next essay. The phoneme-cluster economics, what specifically the rails carry, how the herald question gets settled - those want their own space. The takeaway here is that the wire-format choice that looks wasteful at the symbol level is already competitive once you count the phonology, and carries room the encoding it's measured against can't. The 16-bit packet is reserved headroom - payload once the project spends it.

## And I'm supposed to care about this because...

Density is one reason to put the signal first, but it isn't the interesting one. The interesting reason shows up when you run the clock forward - not years but centuries, out past the point where everyone who could read the script is dead.

That's the bet the inversion is really making: that a script whose canonical artifact is a bit-geometry, not an inherited glyph, can be picked back up by someone with no one left to teach them. Whether that bet holds depends on a problem every script eventually runs into - so start there, with how ordinary scripts survive, and how they die.

The natural-script answer to deep time is unbroken human transmission. Scripts survive across centuries because each generation teaches the next how to read the marks on the page, and each substrate transition (papyrus to parchment to paper to movable type to digital fonts) is a re-rendering by somebody who knows what the marks are supposed to look like. The transmission chain is human. When the chain holds, the script survives. When the chain breaks, the script is boned.

Hangul made it 600 years and survived three substrate transitions (brush-and-ink, movable type, digital encoding) because every transition had Korean speakers who knew Hangul and could re-author the script in the new medium without losing the underlying phonological logic. Each transition was a deliberate design pass by people who understood what they were preserving. The script survived because the chain didn't break.

![[rosetta-stone.jpg]]
*Hieroglyphs on the Rosetta Stone*, engraved by James Basire for the Society of Antiquaries of London, 1810. Public domain, via [New York Public Library](https://nypl.getarchive.net/media/hieroglyphs-on-the-rosetta-stone-f1ec34).

Egyptian hieroglyphs are the counterexample. The last fluent reader of hieroglyphs died sometime in the fourth century, after Coptic Christianity had displaced the older religious context the script depended on. The script became, in functional terms, a corpus of inscriptions on tombs and temples that nobody alive could read. From the death of the last reader to [Champollion](https://en.wikipedia.org/wiki/Jean-Fran%C3%A7ois_Champollion) publishing his decipherment in 1822 is right around fourteen hundred years. The script and artifacts existed that whole time. What didn't exist was the human transmission chain, and the recovery had to wait until someone happened to find a stone with the same text in three scripts, one of which (ancient Greek) was still legible to nineteenth-century scholars.

A small canon of deliberate deep-time messaging projects has tried to design around this problem. The Long Now Foundation's [Rosetta Disk](https://rosettaproject.org/), the Voyager [Golden Record](https://goldenrecord.org/#universum), the [WIPP nuclear-waste markers](https://wipp.info/) in the New Mexico desert, the original Rosetta Stone itself. I don't have a horse in any of those fights and this essay isn't trying to plant a flag in that conversation; it's just useful to namecheck them so the reader knows the territory exists, and to note that almost every deliberate deep-time messaging project still operates on the natural-script assumption. They preserve glyphs and embed parallel texts in known scripts so future readers have an anchor. They rely, in one form or another, on the survival of a script we can already read.

Concretely, the bet is this: if the canonical artifact is bits in a particular geometry, the substrate-transition problem reduces. You're trying to preserve a finite enumerable list of states instead of trying to preserve the visual style of a particular rendering. The geometry is reconstructable from the bits, and the bits are reconstructable from any document where the geometry is visible.

That's the claim, anyway. The question is whether the claim survives contact with the actual preservation problem.

## The codebook problem

Glyph-primary scripts need glyphs and a survivor language. Marain needs the codebook - the table that maps each 9-bit value to a meaning. If a future reader recovers a Marain document and doesn't have the table, they have a 512-state enumeration with no semantic content. So which is the easier thing to preserve?

Let's start with what a recovered artifact gives you for free. Picture a far-future reader holding a single Marain document. From the artifact alone they can see that the marks are made of 3x3 binary cells, and they can count and confirm that there are 512 possible states. The packet structure - slate plus rails plus herald, 16 bits in a specific visual banding - is also visible just by sitting there. None of that requires anyone to have told them anything. A reader who recovers any single Marain document recovers the geometry and the packet structure for free, whether or not they have the codebook.

A glyph corpus does not work this way. If you find a single inscription in a forgotten alphabet, what you have is one writing sample. The alphabet's full inventory isn't given to you - some letters might not appear at all - and the visual conventions are only as recoverable as the inscription's fidelity. The script depends on a tradition of visual judgment that the inscription can hint at but can't reconstitute. A finite cellular grid is more recoverable than a glyph corpus, in this specific sense. Not infinitely more, but measurably so.

![[05-checkerboard-glyph.png]]

What the artifact still won't give you is what any given state means. The bit-pattern for the checkerboard glyph might mean "noise" or "interference" or "maximum-intensity warning," but nothing in the pattern itself says so. That's the codebook problem proper, and on its own it's the same problem the Egyptian hieroglyphs presented to nineteenth-century philologists: a finite enumerable system with no Rosetta Stone in evidence and no surviving fluent reader.

The encoding's response is structural. Of the 512 states, exactly eight are invariant under rotation and reflection - they look the same no matter how you turn the page. ([Essay 1](https://jlesser.substack.com/i/195789730/the-geometry-that-designs-itself) walked through which ones and why.) These eight are geometrically distinguished, in the sense that a future reader sorting the state space by structural property would surface them without being told to. And the encoding is designed so that the same eight glyphs are also semantically extreme - void, full, saturation, noise, the maximum-intensity warning states. The structural distinction and the semantic distinction are deliberately coupled. A reader who notices the first is one inference away from the second.

That coupling is key. It's an anchor of eight known points in a 512-point space. What it doesn't get you is anything resembling fluency. Champollion had Greek and two decades to crack the hieroglyphs, and he started further along than a Marain decoder would. The claim isn't that Marain decodes itself. The claim is that the design gives a sufficiently motivated future reader the foothold they need to start, where a glyph-primary script with arbitrary form-to-meaning mappings gives them nothing.

This is a different strategy than the one used by the historical Rosetta Stone. The Stone was a parallel text - the same content in three scripts, one of which, luckily, was still readable in the 1790s - and it gave Champollion a known anchor to align the unknown ones against. The Marain inversion tries to put the anchor inside the encoding itself, by making the structural extremes of the state space line up with the semantic extremes of the content. We're building the Greek into the geometry, not the next stone over.

More honesty.

First, the inversion does not survive total artifact loss. If every Marain document is destroyed, the script is gone regardless of how cleverly it was structured - the argument is about recovery from partial loss, not from zero. A bunker with one surviving Marain document does better than a bunker with one surviving Egyptian inscription; a bunker with zero surviving anything does the same in both cases, which is to say *nada*. Second, the structural-to-semantic mapping is partly Banks and partly project decision. Banks specified that the invariant glyphs exist and gave them certain semantic loads; the marainkit project has been formalizing the connection, making the geometric-to-semantic relationship a designed property rather than letting it read as decorative. Both are still being settled. The current glyph table lives at [marainkit.github.io/marain](https://marainkit.github.io/marain/) for anyone who wants to see how the sausage gets made.

## What it would actually take

What would have to be true for the inversion to actually buy the deep-time property I've been claiming for it. Well, three things, roughly.

The codebook has to be published and stable - not just exist as a working file in somebody's GitHub repo, but published in a form that's enumerable, inspectable, and recoverable. marainkit is partial on this: the geometry, the packet structure, and the invariant glyphs are settled; the full 512-state semantic assignment isn't.

The rendering rule has to stay derivable from the bits. The 3x3 geometry already does this work - a reader who knows the system is 3x3 binary can reconstruct the rendering directly, no font required. The project's job is to keep it that way as the design evolves. (This is the bit-order question from earlier: whether Banks intended the least-significant bit to read top-left or bottom-right needs to be documented as a deliberate convention rather than left as an inherited accident - because it's a pain in the butt.)

And the eight invariant glyphs have to be designed - and documented as having been designed - so that geometric distinction tracks semantic extremity. If a future reader sorts the state space by symmetry and finds the symmetry-distinguished glyphs sitting in the semantically extreme positions, the anchor argument works. If the relationship reads as decorative, it doesn't.

There's a fourth thing, more poetic than load-bearing, but it's aspirational and keeps me up at night. The spec itself could be encoded in Marain - the codebook, written in Marain, kept as part of any sufficiently large Marain document. A reader who recovers the document also recovers the means to interpret it. A Rosetta Stone that's also the language it's written in. I haven't worked out whether it's achievable; the spec has technical content - numerical state values, geometric descriptions - that a phonological language might not be the right tool for, so it may be more aspirational than practical. But it's the kind of property a script designed transmission-first could in principle have, and a glyph-primary script can't.

## Outside the fictional frame

I'm not going to pretend any of this is going to happen.

The marainkit project is a reconstruction of a language that both never was and hasn't been invented yet. There's no Culture. There are no Minds enforcing anything. There's no civilizational mandate for Marain to spread. The whole substrate-content discussion from the [last essay](https://jlesser.substack.com/p/substrate-vs-content) applies - this is an Esperanto-shaped project, not a Hangul-shaped one. Whether the inversion produces deep-time-survivable artifacts is testable only in principle. We will never have the controlled experiment.

Which is fine.

The project isn't trying to produce a deep-time artifact for some future civilization to decipher. It's trying to specify a script that COULD have the property, under the constraints Banks set up in the books. The reason to think about deep time is that it's the design horizon Banks was implicitly designing against. A civilization that has run for thousands of years and survives across substrate changes and lightspeed-delay communication needs a writing system that can travel. The inversion is one way to give it one. Working out the implications of that choice tells you something about what the script is and what it isn't.

There's a related way of saying this. The structural property - that a script can be designed so its own geometry partially encodes its decoding instructions - survives whether or not anyone uses it for transmission. It's a way of building. Like other ways of building. The property is still there in the design, and the design is still interesting, regardless of whether anyone is ever going to recover a Marain document from a bunker in five thousand years.

## Coming up

The next essay — [*A Working Grammar*](04-a-working-grammar.md) — is about the parts of the spec that are solid enough to actually build with. The geometry, the packet structure, the invariant glyphs, the phoneme-cluster vocabulary. And the parts where the project has had to make decisions Banks left open. It also picks up the density argument from earlier here, the phoneme-cluster economics that make the 16-bit packet pay for itself, and what specifically the rails are carrying.

That's the spec essay. After that, we'll see.

_This essay was developed with AI-assisted research, outlining, and editing support._

---

[^orient]: Which corner holds bit 0 - top-left or bottom-right - isn't fixed in Banks's source. It's the same rendering-rule convention I come back to in "What it would actually take"; the glyphs here follow marain-banks.

[^braile] In a standard 6-dot braille cell, the dots are numbered with 1, 2, and 3 down the left column and 4, 5, and 6 down the right.

[^consistent]: Of the two fonts that render Banks's glyphs, only marain-banks is internally consistent — it lays every glyph down under one bit-to-cell rule. marain-regular isn't, and draws this one mirror-flipped. I'm following Banks.

[^fonts] Font marked ‘Banks’ is [Marain](https://fontstruct.com/fontstructions/show/1446008/marain-5) by TTFTCUTS. [Marain Serif](https://fontstruct.com/fontstructions/show/1562513/marain-serif-1) by comradelenin456. [Marain Dots](https://fontstruct.com/fontstructions/show/1445997/marain-dots) also by TTFTCUTS. The other two are mine.

[^generative]: Two caveats, since a careful reader will raise them. Marain is "generative" only once one convention is fixed - which corner is bit 0, which way the bits run; that's the orientation question above. And Unicode isn't uniformly non-generative: Hangul syllable blocks are composed algorithmically from jamo, and there's structure in the code-point ranges. So the contrast is design intent and degree - generative throughout versus indexical almost everywhere - not an absolute.

## Sources and further reading

- Iain M. Banks, ["A Few Notes on Marain"](../notes/source/a-few-notes-on-marain.md). The original technical essay.
- The history of W: the [OED entry](https://www.oed.com/dictionary/w_n) for the lexicographic story. Michelle P. Brown, *A Guide to Western Historical Scripts from Antiquity to 1600* (British Library, 1990) for the paleographic side, with plates from actual Insular and Carolingian manuscripts. The Pat O'Conner / Stewart Kellerman ["Why the 'w' is called a 'double u'"](https://grammarphobia.com/blog/2023/02/double-u-2.html) post for a free and well-sourced summary.
- Louis Braille's original publication: *Procédé pour écrire les paroles, la musique et le plain-chant au moyen de points* (1829). The Unicode Braille block `U+2800`-`U+28FF` for the digital substrate.
- On Hangul, the standard English source is the Lee and Ramsey edition of *Hunminjeongeum*. On Egyptian decipherment, Andrew Robinson's *Cracking the Egyptian Code: The Revolutionary Life of Jean-François Champollion* (Oxford, 2012) is the readable single-volume biography.
- Raposo, Joe (music), and Jerry Juhl (lyrics). "The National Association of 'W' Lovers." Performed by Bert (Frank Oz). *Sesame Street*, Episode 0366, 1971. Released on *The Muppet Alphabet Album* (Columbia Records, CC 25503, 1971), track 23. Recording sessions: September 20-24, 1971 (per *Jim Henson's Red Book*). Publishing rights: Instructional Children's Music, Inc. ©1973. [YouTube](https://www.youtube.com/watch?v=XJcdpKYIFKs).

**Project documentation**
- [`encoding/`](https://github.com/marainkit/marain/tree/main/encoding) - the canonical spec for the slate, packet, rails, and herald.
- [`encoding/docs/invariant-glyphs.md`](https://github.com/marainkit/marain/blob/main/encoding/docs/invariant-glyphs.md) - the eight rotation/mirror-invariant glyphs and their reserved semantic loads.
- [`direction/encoding-density-and-packets.md`](https://github.com/marainkit/marain/blob/main/direction/encoding-density-and-packets.md) - the density argument worked out in more technical detail.
- [marainkit.github.io/marain](https://marainkit.github.io/marain/) - current state of the glyph table - I gotta figure out the bit order question because it's really doing my head in.
