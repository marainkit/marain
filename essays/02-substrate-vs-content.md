# Substrate vs Content
### Esperanto, Hangul, and what survives when you design a language

_Second in a series. The first essay — [Engineered Defaults](https://jlesser.substack.com/p/engineered-defaults) — made the case that languages can be engineered to make particular kinds of thinking cognitively cheap. This one is about whether designed languages can actually spread far enough to do that work in the first place._

![[a-language.png]]

Esperanto and Hangul show up in the same breath when designed languages come up — which is to say: not all that often, but more than you’d guess if you don’t run in the kind of circles where it does. They show up paired because the framing is irresistible: two deliberately constructed linguistic projects, both internally well thought out, both launched into receptive moments. The framing is also a little misleading. They’re separated by four hundred and fifty years and they’re not the same kind of thing at all. But, you know, the pairing keeps happening, so let’s run with it.

Here’s the gap. Hangul is the daily script of two countries, used by something on the order of eighty-two million native speakers, and is still occasionally adopted by communities that don’t currently have a script of their own. Esperanto is a language I learned three sentences of in 1994, dreaming of becoming a linguist, and have not used since. Both designs are still walking around. One of them is a working part of a country’s infrastructure. The other is a hobby in a small handful of cities, with a literature, with congresses, with a real and dedicated community that is not lying about anything, but is also not going to overtake English as anybody’s second language anytime soon.

Same family of ambition. Different fates. The interesting thing is what accounts for the gap, because the answer turns out to be useful for any project trying to design the surface of a language — including, eventually and self-interestedly, the one I’m working on.

For context, the project in question is _[marainkit](https://github.com/marainkit/marain)_ — a reconstruction effort around the constructed language Iain M. Banks designed for his Culture novels. The substrate-vs-content question keeps surfacing in that work, and the Esperanto-Hangul contrast turns out to be the cleanest analogy I’ve found for what I’m trying to figure out. So the essay is doing two things at once: a historical pass on a pair of designed-language projects, and a sideways setup for what the pass implies for the reconstruction. Anyway.

![File:Unua libro pl.png](https://substackcdn.com/image/fetch/$s_!uO5j!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F151e1c55-4b5c-4189-bb83-16aca1a56d9e_500x716.png "File:Unua libro pl.png")

_Image: Unua Libro, L. L. Zamenhof, 1887. Source: Österreichische Nationalbibliothek, via_ _**[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Unua_Libro_por_Rusoj.jpg)**. Public domain._

## **The peace pamphlet, 1887**

Ludwik Zamenhof was a Polish ophthalmologist who grew up in Białystok, which at the time was a melting pot where four ethnicities had it out with each other in the streets on the regular. Zamenhof blamed language. He thought if everyone had a shared neutral second language — not English, not French, not German, none of the ones whose use already implied a power relationship — a real chunk of the Białystok aggression would just _go away_. The pamphlet he published in 1887 was the proposal. He used the pseudonym _Doktoro Esperanto_, which is also where the language got its name. _One who hopes._

The grammar he designed is, taken on its own merits, sort of beautiful. Every noun ends in _-o_. Every adjective in _-a_. Verbs conjugate by tense alone, six suffixes total, no irregularities, no person-agreement, no gendered articles, no spelling exceptions. It is almost spectacularly regular. A motivated adult can get to functional reading in weeks. I keep saying “almost” because the phonology has one or two corners — the diacritical letters, the optional “h” replacement system — that bug people, but in context those are rounding errors. As constructed languages go, the engineering is solid.

![[esperanto-suffix.png]]
Figure from Jansen (2013), _Esperanto parts of speech in functional discourse grammar_, _Linguistics_ 51(3). © De Gruyter Mouton.

It did **not** propagate. The reasons it didn’t are not flaws in the engineering, and the literature on this is reasonably consistent about what they are. Esperanto solved the wrong problem — or, more carefully, it tried to claim a slot that was being claimed in real time by someone else. Zamenhof’s bet was that an easier-to-learn second language would naturally win the international-auxiliary role. What actually fills that role is institutional power — the language of the empire, the lab, the trade hub, the army. English claimed the slot in the twentieth century not because it was destined to (in another timeline it’s French, or German, or some standardized commercial pidgin doing the work) but because the institutions that needed a cross-border lingua franca during the exact decades Esperanto was trying to grow happened to be running on English. By the time Esperanto had a real shot at the role, the role was taken. This isn’t an argument that auxiliary languages can’t propagate in principle. It’s an observation that the institutional window for one to claim the international slot is narrow, contingent on which incumbent gets there first, and effectively closed once the incumbent has momentum. Esperanto had no comparable backing. It had a community. It did not have a state, a standing army, a scientific establishment, a market.

It also wasn’t solving any problem urgently. The kinds of multilingual professionals who might have adopted it already had three or four options in motion. Esperanto’s pitch was that it was _fairer_ than the other options, and fairness — well, look at the historical record. That is not what gets selected for at the institutional level when the institutional level is making language choices.

The third miss is the one that matters for what I’m trying to get at. Esperanto borrowed the Latin alphabet wholesale, and that was not, in 1887, anything close to a neutral choice. Latin script was already the de facto global substrate for European diplomacy, scientific publication, colonial administration, and printed books in every language with imperial reach. It was, by the late nineteenth century, the visible surface of exactly the institutional power structures Zamenhof’s content layer was meant to be a neutral alternative to. Borrowing it inherited every one of those power cues. A page of Esperanto looks like a page of mildly unusual Italian because Latin script _was_ the script of the imperial nineteenth century — and neutral content riding on a non-neutral substrate doesn’t read as neutral to a reader. It reads as another European project. The script does none of the work the content was trying to do; arguably it does the opposite. Whatever a reader’s first reaction to the page is, that reaction was already settled before any of Zamenhof’s careful design choices got a chance to land.

None of which is to say Esperanto is a failure in some absolute sense. It’s the most successful from-scratch designed language in modern history. There are even native speakers — children of Esperantist parents who grew up bilingual — which is wild… but the trajectory is a hobby trajectory, not a civilization-scale one, and that’s not what Zamenhof was building toward.

![[hangul-original.png]]

_Image: Hunminjeongeum Haerye reprint, Government of Joseon, 1446. Source: Seoul National University Kyujanggak Institute for Korean Studies, via **[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Hunminjeongeum_Haerye_03.jpg)**. Public domain._
## **By royal decree, 1443**

Sejong’s project looked similar from a distance and was operationally a different animal.

He wasn’t designing a language. Korean already existed. Everyone in his kingdom spoke it. What he was designing was a writing system _for_ it — the existing Chinese-character system fit Korean phonology badly and required enough scholarly training that literacy was effectively a class boundary. Hangul was, on its face, a workaround for a phonological mismatch. In practice it was also a deliberate chip at an aristocratic monopoly on the written word. The preface to the document promulgating it more or less says that out loud: the speech of our country is not Chinese, ordinary people can’t express themselves in the script we currently have, here’s a better one.

The design itself is one of those things that’s hard to credit until you sit with it. Each letter’s shape is derived from a stylized diagram of the speech organs that produce the corresponding sound. Velar consonants share a base shape that suggests the back of the tongue. Coronal consonants share a different base. Vowels are built from three primitives — a horizontal line, a vertical line, a dot — combined according to rules that mark front/back and rounding distinctions. The script encodes its own phonology graphically. If you’ve internalized the system you can guess at letters from how the sound feels in the mouth. (As an aside: this is not how alphabets normally work. Most alphabets are accidents of which earlier scripts they descend from. Hangul is one of the few that actually has a _theory_ in it.)

![[hangul-sounds.png]]

Figure adapted by Stephen Wright (2004) from an earlier French-language source; available at [wright-house.com](http://www.wright-house.com/korean/korean-linguistics-origins.html).

Then those letters get composed into syllabic blocks — onset, vowel, optional coda, arranged into a roughly square unit that takes about the same visual real estate as a Chinese character. That last bit is a compatibility decision, and worth flagging, because it’s the kind of choice a less careful designer would not have made. Hangul could be slotted into mixed Hangul-Hanja text without disrupting the visual rhythm of the page. It didn’t pick a fight with the typesetting it had to live alongside.

![[hangul-words.png]]

Figure adapted from Shim, Bae & Sung (2022), _Korean Tokenization for Beam Search Rescoring in Speech Recognition_ (arXiv:2203.03583).

None of this would have mattered without the institutional half. Sejong was an absolute monarch. He had Hangul promulgated by royal decree. Subsequent rulers wobbled on it — there were periods, especially under elite scholarly pushback, when use of Hangul was actively discouraged — but the script never fully went away because the constituency it served was the much larger non-aristocratic population whose practical literacy actually depended on it. Two later events locked it in. Centuries of vernacular literature accumulated in Hangul (novels, women’s correspondence, religious texts) and built up legitimacy from below. Then Japanese colonization, 1910 to 1945, made suppressing Korean language part of the imperial project, and Hangul came out the other side as a marker of being Korean in a way that Chinese-character literacy had never quite been. By post-liberation, mixed-script use was on its way down and pure Hangul was on its way up. The script became the visible substrate of national identity.

That is the condition Esperanto never had. Hangul was institutionally backed, urgently useful, and identity-bearing. Each of those reinforced the others. A script you have to know to be literate in your own country, that lets you read texts you couldn’t before, and that visibly marks you as belonging to a particular cultural project, propagates without anybody having to choose to adopt it.

It’s worth pausing on the inverse case here, because the three-factor story can sound a little overdetermined if you don’t. Plenty of state-backed scripts have failed. The Soviet Union pushed Latin alphabets onto a dozen Central Asian and Caucasian languages in the late 1920s, then pushed Cyrillic onto the same languages a decade later; several of those have since reverted, and the institutional adoption never produced the durable lock-in it was supposed to. Chinese Latinization (_Latinxua Sin Wenz_) had Soviet and CCP backing in the 1930s and is, today, not the script of China. Institutional power is necessary for a designed script to propagate at scale. It’s not sufficient. Hangul’s claim isn’t that it was state-backed and therefore won; it’s that it was state-backed _and_ solving a real problem for the constituency that mattered _and_ well-designed enough that the practical affordance held up once the political winds shifted. Take any one of those out and the trajectory looks more like the Soviet Latinization story than the one we got.

I should also flag something about Hangul that doesn’t get enough credit: how good the design is on its own technical merits. Sejong wasn’t doing magic — he was running on careful empirical observation of how Korean phonology actually worked, and the system he built is more phonemically transparent than most of the alphabets currently in service. Linguists love it for this reason. None of which would have mattered if the institutional half hadn’t been there. The design quality made the propagation cheaper once it had a runway. It did not produce the runway.

## **The split, named**

The Esperanto-Hangul gap is sharp enough that it’s worth pulling a clean distinction out of, and the distinction is the actual point of this essay.

_Content_ is the linguistic system: phonology, morphology, syntax, vocabulary, the rules that compose meaning. The thing speakers learn when they learn a language.

_Substrate_ is what content rides on: the writing system, the encoding, the visible or audible surface, the packaging that lets the content travel across people, distance, or time. The thing readers encounter before they encounter the content.

Worth flagging before going further: in practice, the two leak into each other constantly. Scripts shape cognition, prestige, identity, and what kinds of language change become likely. Hangul didn’t just transport Korean — it reshaped who got to be literate, what counted as Korean literacy, and how speakers thought about the relationship between their phonology and their writing. The distinction I’m pulling out here is analytical, not absolute. I’m going to use _substrate_ and _content_ as if they were cleanly separable for the rest of the essay because the analytical move is useful, but anything that depends on treating the layers as fully independent should be taken with a tablespoon of salt.

Esperanto designed content and borrowed substrate. Hangul designed substrate and inherited content. One of those projects has spent a hundred and forty years looking for a foothold. The other was the working literacy of a kingdom inside a couple of generations.

The pattern generalizes. Designed substrates have, historically, a much better track record than designed content systems. Cyrillic — designed in the ninth century by Saints Cyril and Methodius for liturgical translation — is now the script of seven national languages. The Cherokee syllabary, designed by Sequoyah between 1809 and 1821, took Cherokee literacy from near-zero to near-universal in about a generation. The Arabic script’s spread across Persia, Central Asia, and the Indian subcontinent followed institutional adoption — by religion and empire — not anything intrinsic to the languages it was extended to. Substrate projects. They propagated.

Designed content systems have a much thinner survival list. [Volapük](https://en.wikipedia.org/wiki/Volap%C3%BCk), [Ido](https://en.wikipedia.org/wiki/Ido), [Interlingua](https://en.wikipedia.org/wiki/Interlingua), [Lojban](https://en.wikipedia.org/wiki/Lojban), [Toki Pona](https://en.wikipedia.org/wiki/Toki_Pona). Each has a small, often passionate community, and each has stayed at hobby scale. The exception that gets cited as a counterexample is Modern Hebrew, and the reason Modern Hebrew worked is precisely that the three Hangul conditions all stacked. Institutional mandate (early Zionism, then the State of Israel). Urgent problem (no shared vernacular among Jewish immigrants from forty different language backgrounds). Identity (a national project that explicitly tied linguistic revival to cultural continuity). It’s not a counterexample. It’s the same pattern at a different scale.

The lesson, more or less: substrate is the part that travels, content is the part that has to be chosen, and people overwhelmingly choose what’s already in the air around them. I’d put it as a one-liner if it would shake out as one, but it doesn’t — it wants the qualifications. Substrate travels easier than content does. Both can travel if the institutional conditions are right. Neither one travels much without those conditions, no matter how good the design is.

I think that’s the actual claim.

## **How Banks killed two birds**

Marain is unusual in this taxonomy because Banks designed both layers and didn’t pick one. He specified content — phonology, the engineered single gender-neutral pronoun, a deliberately constructed vocabulary, the morphological intent. He also specified substrate down to the bit: a 3×3 binary grid, 512 indexed states, a 9-bit packet that’s identical whether the symbol is carved, broadcast, or transmitted as light over a tightbeam laser. He was, in the substrate-vs-content sense, doing the Hangul move and the Esperanto move at the same time.

Inside the fictional frame, all three Hangul-style conditions hold for both layers, which is the part that lets the thought experiment stay coherent. The Culture’s [Minds](https://theculture.fandom.com/wiki/Mind) are an institutional substrate of essentially infinite reach — they can mandate anything indefinitely. The civilization has a named identity (post-scarcity, anti-hierarchical, conspicuously anarchist) that Marain visibly encodes by design. And the language solves a real concrete problem, which is what an interstellar civilization actually needs in a representational system: a single canonical form that survives substrate changes, lightspeed delays, and cross-cultural translation across millennia. A 9-bit number is the same number on any rendering medium. The visible glyph is one rendering of the number. The signal is the canonical thing.

Banks gave his fictional Minds the Hangul condition for the substrate, the Hebrew-revival condition for the content, and embedded both inside a civilization that could enforce them indefinitely. That’s not a small move. The thought experiment isn’t “can a language reshape thinking” in the abstract. It’s _what happens when a designed writing system, a designed language, and a civilizational mandate align and then run for long enough to compound._ Esperanto and Hangul are, between them, the closest thing the historical record has to an answer for the parts of that question we can answer empirically. Hangul says substrate-plus-mandate works on civilizational timescales. Modern Hebrew says content-plus-mandate-plus-identity can work on generational ones. Esperanto says that none of the careful design quality on either layer overcomes the absence of the institutional half.

The Culture novels are about a civilization that has run the experiment for several thousand years. Banks didn’t have to argue that the experiment worked; the books take that for granted. What he had to do was specify the experiment well enough that the substrate and content are recognizably the kind of thing that would produce that outcome, given the institutional context. Reading “A Few Notes on Marain” with the substrate-vs-content distinction in hand, that’s pretty much exactly what the technical essay is doing.

## **What is and what should never be**

Outside the fictional frame, the reconstruction project I’m working on sits in a different position. There’s no Mind enforcing adoption. There’s no civilization tied to the language. There’s no urgent problem its existence solves for a captive constituency. By every external measure it is shaped like an Esperanto-shaped project: a designed system whose adoption depends on individual people choosing to engage with it.

Which is fine.

The project isn’t optimizing for adoption. It’s optimizing for design coherence — working out what Banks specified, what falls out of those specifications mathematically, what the gaps look like, what kind of choices have to be made to fill them consistently. The substrate-vs-content distinction is still load-bearing for the project, though, because it points pretty clearly at where my hours go furthest.

The substrate layer is the layer I can actually finish. The 3×3 grid is fully specified. The 512 states are enumerable. The rotation-invariance constraint produces, automatically, the eight invariant glyphs and their semantic pairs — that’s geometry, not authorial decision. The packet structure is a small set of decisions. None of this requires institutional power. It requires careful work. And — the thing I’d want to underline — substrate is the layer that, in the unlikely event the project did acquire something like institutional traction, would be the layer that propagated. That’s the Hangul lesson. The visible surface is what carries.

The content layer — phonology, vocabulary, grammar, the tonal system if Banks had one in mind, which he might not have — is the harder problem and the part with the worse historical odds. Banks specified comparatively little here, and what the community has built on top is heterogeneous and partially incompatible across reconstructions. The project’s position has been that the content layer should be developed but with clear-eyed honesty about which parts are canonical and which are one defensible reading among several. Marain-the-language is, and will probably remain, an Esperanto-shaped artifact. Marain-the-script — the binary, the glyph table, the rendering specification — is the part with Hangul-shaped potential.

This is not a recommendation to abandon the content work. I like the content work. The grammar discussions on [r/Marain](https://www.reddit.com/r/Marain/) are the most fun part of the project on a given Saturday. It’s a recommendation to be honest about which parts of the project are which, when the question of where my limited evenings go comes up. The grammar is interesting; the substrate is _transmissible_. Engineering hours spent on the binary encoding, the glyph table, the rendering spec, the rotation-invariance properties of the writing system — those compound. Engineering hours spent on grammar accrue to a layer that has, in every comparable historical case, depended on extralinguistic forces to spread.

I should also caveat that I might be wrong about how this shakes out. The substrate-vs-content distinction is real, and the historical pattern is consistent, and the Hangul-vs-Esperanto contrast holds up well. But “this layer historically travels better” is a generalization across maybe a dozen cases, and a project this small a footprint can pretty easily violate the generalization in either direction. Maybe the grammar is what people end up caring about. Maybe nobody ends up caring about any of it. Honestly, the part of _marainkit_ I’m most attached to is just figuring out what’s actually in there… which is a different reward function than spread anyway.

## **Coming up**

The next essay (_Transmission First_) follows a thread the substrate-content distinction opens but doesn’t unfold. Banks made an unusual choice when he specified Marain’s writing system — the binary signal is the canonical form, and the visible glyph is one particular rendering of it. That’s the opposite of how natural-language writing systems work, where the visible mark is primary and any digital encoding is derivative. The inversion has consequences for how a script behaves over very long timescales, across substrate changes — paper to screen to whatever the next medium turns out to be — and for what it would mean for a representational system to outlast the technologies that originally rendered it.

Hangul has lasted nearly six hundred years and survived three substrate transitions: brush-and-ink, movable type, digital encoding. Each of those transitions required deliberate design work to preserve the script’s phonemic and visual logic. Marain, by being binary at the canonical level, is trying to remove that translation step entirely. Whether that’s coherent — and what it would actually take to build for it — is the next thing I want to work out on the page.

_This essay was developed with AI-assisted editing and revision. The underlying argument, examples, and project thinking are mine; the tooling mostly helped with structure, compression, and making me sound smarter than I actually am._

---

## **Sources and further reading**

- Iain M. Banks, “A Few Notes on Marain”. The original technical essay.
- King Sejong the Great, _Hunminjeongeum_ (1446). The promulgating document. The Lee-Ramsey edition is the standard English source.
- Forster, P. G. (1982). _[The Esperanto Movement](https://literaturo.weebly.com/uploads/8/2/9/5/8295099/the_esperanto_movement_-_peter_g._forster__1982__-_with_bookmarks.pdf)_. Mouton. The standard sociological history.
    

**Project documentation**

- `direction.md` — project scope and the substrate-content prioritization this essay defends.
- `language/README.md` — the content work, with explicit notes on which parts are canonical, inferred, or project decisions.