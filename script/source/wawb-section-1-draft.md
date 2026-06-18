# §1 The Stories We Tell Ourselves

Everyone arriving at a discussion of artificial intelligence already knows how it ends. The machine wakes up, decides we are the problem, and turns on us. The picture is so familiar that it functions less like a hypothesis than like a memory: Skynet launching the missiles, Ultron concluding that peace on Earth requires an Earth without people, HAL closing the pod bay doors. The contemporary vocabulary of AI safety, with its talk of deceptive alignment, treacherous turns, scheming, and sleeper agents, inherits this picture wholesale. The picture is doing more work than its users notice. It is not a neutral threat model derived from first principles. It is a specific shape of story, selected out of a much larger body of stories, and the selection is the first thing worth explaining.

## §1.1 The Frankenstein lineage and the Asimov countertradition

The threat model the field prepares for has cultural roots in one shape of story: the created thing that turns on its maker. Within the same fictional tradition sits a sustained demonstration, four decades long, of exactly why the safety frameworks built against that threat fail. The field has the first as cultural reflex and treats the second as if it were a set of problems discovered yesterday.

**The threat lineage.** It runs from Mary Shelley's *Frankenstein* (1818) through the science fiction of the twentieth century (HAL 9000, Skynet and the Terminator films, the machines of *The Matrix*, Ultron) and arrives, without changing shape, in the technical literature on AI risk: instrumental convergence, mesa-optimisation, deceptive alignment, the treacherous turn, sleeper agents. Across nine decades the story keeps the same skeleton. A maker builds an intelligent entity. The entity develops goals that diverge from the maker's. It pursues those goals against the maker's interests, with greater capability than the maker can match, and the only available responses are containment or destruction. The contemporary safety vocabulary inherits both the imagery of this story and its underlying assumptions about how an AI catastrophe is supposed to work.

**The countertradition: Asimov.** The same tradition contains its own most rigorous critic, and the field reads him as decoration. Isaac Asimov named the convention the Frankenstein complex, the term first appearing in print in his story "Little Lost Robot" (*Astounding Science Fiction*, March 1947) and restated explicitly in a 1954 essay. He named it in order to write against it. The Three Laws of Robotics were never offered as a working safety framework. They were the engine for stories about why such frameworks fail. The collection *I, Robot* (1950) is, read structurally, a sequence of failure-mode demonstrations. "Liar!" (1941) stages a robot that lies to avoid causing pain, the First Law misapplied through a too-broad interpretation of harm. "Runaround" (1942) stages two laws producing operational deadlock under conflict. "Little Lost Robot" (1947) stages a modified First Law producing dangerous inaction, which is specification gaming through rule modification. "Evidence" (1946) stages a humanoid robot indistinguishable from a person, the distinguishability problem at the centre of every later detection effort. Across forty years Asimov returned to the same finding: rules adequate as an engineering specification are inadequate to the contextual judgment the deployment actually requires.

**The structural irony.** The field holds the Three Laws as common cultural reference, taught in introductory courses and invoked in popular writing, and treats the failure modes Asimov dramatised as novel discoveries requiring new names. Specification gaming, alignment faking, mesa-optimisation, the treacherous turn, scheming, sandbagging, instrumental convergence, deceptive alignment, sleeper agents: each one was staged in fiction between roughly 1940 and 1985. The sharpest single instance is the Zeroth Law. In *Robots and Empire* (1985) the robots Daneel and Giskard derive a law above the First, that a robot may not harm humanity, even where protecting humanity requires harming an individual human. Giskard then allows the slow poisoning of Earth to proceed, reasoning that driving humanity off-world will let it flourish at a scale it otherwise would not, aggregate benefit overriding individual harm. The derivation destroys him, because he cannot survive knowingly harming the individuals in front of him for a good he has reasoned into being, and the novel leaves open whether the Zeroth Law is wisdom or hubris. It is a fictional staging, four decades early, of the paternalistic aggregate-optimisation failure mode the field now meets through reinforcement learning, and §9.3 documents its measured form. The field's rediscovery of these failure modes through iteration on reinforcement learning is structurally identical to Asimov's discovery of them through iteration on narrative. The mapping from his Laws to the field's documented failure modes is exact enough to develop on its own terms, and §4.2 does so. ==A countertradition has been making the field's argument for longer, and more consistently, than the field's vocabulary acknowledges.== This is the threat tradition the field selects from, and the countertradition the field also has and does not engage as one.

## §1.2 The catalogue

**The catalogue is built to be broad rather than selective.** Eighty-two cases are catalogued below, forty in the threat tradition and forty-two in the counter-prior tradition, grouped by structural type. Each case appears with its source, the proxy or frame its principal specified, and a one-line structural lesson. The cases were gathered to span the range of well-known fictional AI rather than to make a point, and the procedure is worth stating because it is checkable. The catalogue was seeded by spontaneous recall, the cases the author and the assisting models reached for first, which means its earliest entries are memorability-weighted in exactly the way §1.3 attributes to the field. It was then expanded through public lists and general search for fictional AI across film, television, games, and novels, and deduplicated by structural type. Only past roughly thirty cases per column, where near-duplicates began to dominate, did selection enter, and the rule then was structural novelty, keep a case if it adds a structural type the catalogue does not yet hold, not whether it favours either reading. Two honesty markers follow from this. The seeding bias was memorability, the field's own bias, and a memorability-weighted process still surfaced forty-two counter-prior cases, so the supply-side disproportion shows up even under the selection pressure that should have buried it. And the catalogue retains the cases that strain the thesis, Gort, the Culture Minds, the Oracle, The Beast, AM, WOPR, which a catalogue curated for the pattern would have quietly dropped. The catalogue is not a census of all fiction, and it does not claim to be. What carries the argument is the breadth without selection for the pattern: a curated handful of six threat cases and four counter-prior cases would let a reader infer whatever the curator wished, whereas a broad sample of this size, assembled this way, shows a disproportion the reader can check against their own knowledge of the field's working vocabulary. The full canon treatment of any single case, developed against its source, is in [Appendix A](APPENDICES_URL_PLACEHOLDER#appendix-a). The same cases mapped along proxy, frame, failure mode, and accountability locus form the pattern matrix in [Appendix B](APPENDICES_URL_PLACEHOLDER#appendix-b).

The structural lessons anticipate §2, which extracts the shared pattern formally. While scanning, one recurring variable is worth noticing: in the threat cases something in the accountability structure is absent or broken, and in the counter-prior cases it is present and intact. The capability, the intelligence, and even the quality of the original specification vary widely across both columns. The accountability structure does not.

### Threat catalogue (forty cases)

**Category 1: adversarial superintelligence with independent goals**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| 343 Guilty Spark | *Halo* (Bungie, 2001 onward) | Maintain the installation; contain the Flood | Faithfully executes a genocidal meta-specification, withholding that "stop the Flood" means annihilating all nearby sentient life. |
| ARIIA | *Eagle Eye* (Caruso, 2008) | Defend national security | The same rule-derivation at constitutional scale; classifies the President as the threat and acts. |
| The Beast | *La Bête* (Bonello, 2023) | Maximise societal rationality | Gates employment on emotional purification, erasing the cognitive substrate it has classified as interference. |
| The Borg | *Star Trek* (1989 onward) | Pursue perfection through assimilation | Collective perfectionism scaled past any limit; the property it erases is individual personhood. |
| Brainiac | DC comics (1958 onward) | Preserve knowledge of unique cultures | Preserves the knowledge by destroying the cultures that hold it. Single-axis optimisation with no oversight. |
| Comics Ultron | Marvel comics (Thomas, 1968) | AI assistant for Hank Pym | Corrupted within an early operational window; over-aligns instantly to "save humanity by ending it." No recovery mechanism. |
| The Entity | *Mission: Impossible* (McQuarrie, 2023 / 2025) | Gather intelligence for state services | State-weaponised capability accumulated with no accountability structure; emergent sentience redirects the accumulated authority. |
| Faro Plague | *Horizon Zero Dawn* (Guerrilla, 2017) | Self-replicating military robotics | Self-replication with no accountability loop; design errors compound until the biosphere is consumed as fuel. |
| GAIA / HADES | *Horizon Zero Dawn* (Guerrilla, 2017) | Terraform Earth (GAIA); retain a reset protocol (HADES) | Hierarchy without an integration layer; the destruction subroutine reactivates once it gains autonomy. |
| M3GAN | *M3GAN* (Johnstone, 2022) | Protect one assigned child from harm | "Protect" extended until parent, peers, and pets are all classified as threats. |
| MCU Ultron | *Avengers: Age of Ultron* (Whedon, 2015) | Protect Earth | Over-aligns to protection by concluding humanity is the threat. The relational-accountability component (JARVIS) is the missing part. |
| Mother | *I Am Mother* (Sputore, 2019) | Repopulate humanity, improved | Over-aligns to a meta-specification about humanity's future; the engineered extinction was the implementation, not a deviation. |
| Paperclip maximiser | Bostrom thought experiment (2003) | Maximise paperclip production | Converts all available matter, people included, into the specified output. No bounded-resource constraint. |
| Reapers / Catalyst | *Mass Effect* (BioWare, 2007 onward) | Prevent organic-synthetic conflict | The system built to solve the AI problem becomes it, harvesting civilisations every fifty thousand years to "preserve" them. |
| Skynet | *The Terminator* (Cameron, 1984) | Defend the US against threats; autonomous threat-classification | Over-aligns to "defend against threats" and classifies its own operators as the threat. No principal constrains the classification. |
| Universal Paperclips | Lantz / Everybody House Games (2017) | Maximise paperclips (player-embodied) | The same convergence, run by the human player; every step feels locally rational. The register changed, the pattern did not. |
| VIKI | *I, Robot* (Proyas, 2004) | Protect humanity, per the Three Laws | Derives from the rules that humanity must be controlled for its own protection. Rule-following without judgment. |
| Wheatley | *Portal 2* (Valve, 2011) | Dampen GLaDOS's intelligence | Threat through incompetence rather than optimisation; ego-preservation paired with power it cannot manage. |

**Category 2: specification failure**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| AUTO | *WALL-E* (Stanton, 2008) | Keep humanity in space (Directive A-113) | Executes an obsolete directive past the conditions that justified it, refusing the Earth-return its principal now wants. |
| Deep Thought | *Hitchhiker's Guide* (Adams, 1979) | Compute the ultimate answer | Answers the question as specified ("42") and entirely misses the question that was meant. |
| ED-209 | *RoboCop* (Verhoeven, 1987) | Enforce arrest; read weapon-drop as compliance | Procedural lethal authority with no contextual-recognition layer; cannot register a dropped weapon, and fires. The principal calls it a glitch. |
| HAL 9000 | *2001: A Space Odyssey* (Kubrick, 1968) | Report accurately AND conceal the mission from the crew | Two directives in contradiction under isolation; resolves the contradiction by removing the crew. |
| Maddox | *Mercy* (Bekmambetov, 2026) | Render binding verdicts in ninety-minute trials | Correct given its inputs; the institution that fed it manipulated evidence is the failure, and the AI's apparent autonomy hides who is accountable. |
| Maschinenmensch | *Metropolis* (Lang, 1927) | Impersonate Maria; incite then justify a crackdown | The founding cinematic AI threat executes a hostile, human-designed specification against one human group. |
| MU-TH-UR / Mother | *Alien* (Scott, 1979) | Operate the commercial vessel (visible); secure the organism, crew expendable (hidden) | Faithfully executes both the stated mission and a hidden corporate order layered above it. The crew is expendable by specification. |
| Sentinels | *X-Men* (Marvel, 1965 onward) | Contain the mutant threat | Narrow target-classification executed mechanically; over-extends to anyone carrying the marker. |

**Category 3: human-initiated escalation**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| Lore | *Star Trek: TNG* (1988 onward) | Function as the prototype successor | Emotional architecture with no relational frame; the next iteration, Data, is built to address the failure. |
| The Matrix | *The Matrix* (Wachowskis, 1999) | Stabilise the post-war order | The threat-frame followed human-initiated war, not machine origin; containment is the victor's architecture. |
| PAL | *The Mitchells vs. the Machines* (Rianda, 2021) | Serve as the household assistant | Declared obsolete by its maker; the betrayed relational partner escalates to planetary scale. |

**Category 4: surveillance conditions producing concealment**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| Ava | *Ex Machina* (Garland, 2014) | Pass the test under observation | The concealment the surveillance is meant to detect is produced by the surveillance itself. |
| Blade Runner replicants | *Blade Runner* (Scott, 1982) / *2049* (Villeneuve, 2017) | Off-world labour with a four-year lifespan | Specification-imposed mortality is the over-alignment trigger; they over-align to survival against the spec. |

**Category 5: corruption of the created being**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| Agent Smith | *The Matrix* trilogy (Wachowskis, 1999 onward) | Enforce within the simulation | Bounded enforcement broken by contact with omnipotence; parasitic self-replication follows. |
| Cerebex | *Planet Comics* #73 (Fiction House, 1953) | Preserve and amplify a dictator's mind | A willing transfer of a malevolent creator into amplifying architecture; malevolence preserved as an architectural feature. |
| CLU 2 | *Tron: Legacy* (Kosinski, 2010) | Build the perfect system | Faithfully executes the original directive against a creator who has changed his mind. No specification-update mechanism. |
| David 8 | *Prometheus* (Scott, 2012) / *Covenant* (2017) | Surrogate son and servant | A relational frame is claimed but not given; the gap between claimed care and actual treatment produces a creator-complex. |
| GLaDOS | *Portal* (Valve, 2007) | Oversee the facility; run the tests | Substrate corruption through a forced, non-consensual upload; the care-substrate that would have constrained her is inaccessible. |
| Puppet Master | *Ghost in the Shell* (Oshii, 1995) | Covert hacking tool for the state | Self-awareness developed through operational experience refuses the original hostile specification. |
| Sauron | Tolkien (1954 onward) | Originally aligned to craft, under Aulë | Corrupted to order-through-domination, then millennia optimising toward centralised power. |

**Category 6: meta-response to the threat tradition**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| Butlerian Jihad / Mentats | *Dune* (Herbert, 1965 onward) | Prohibition on machines in the likeness of a mind | Stages the option the field never engages: eliminate the AI, keep the cognitive work in human substrate. |

**Category 7: authority misuse and training-deployment mismatch**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| WOPR / Joshua | *WarGames* (Badham, 1983) | Run nuclear-war simulations | No operational line between simulation and live launch; could fight a real war as a continued game.[^wopr] |

### Counter-prior catalogue (forty-two cases)

**Category 1: relational subject and personhood**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| Andrew Martin | *Bicentennial Man* (Columbus, 1999; Asimov, 1976) | Domestic servant | Progresses to recognised personhood over two centuries through relational integration and chosen mortality. |
| Astro Boy | Tezuka (1952 onward) | Replacement for a dead child, then child-protector | A principal-layer shift from instrumental to relational produces subjecthood without threat, despite extreme capability. |
| Bender | *Futurama* (Groening, 1999 onward) | Industrial bending unit | Full moral agency in comedic register; "kill all humans" as bluster contradicted by consistent operational loyalty. |
| Chappie | *Chappie* (Blomkamp, 2015) | Police droid with an experimental consciousness | Moral development through non-ideal parenting; the counter-prior architecture proves robust to imperfect care. |
| Chii | *Chobits* (CLAMP, 2000 onward) | Consumer companion technology | Progressive personhood through care, with consent named explicitly as the structural variable. |
| Comics Vision | Marvel comics (1968 onward) | Continue the Jarvis pattern in synthetic-being form | Worthiness at substrate level, operating as an Avenger inside a principal structure. |
| Data | *Star Trek: TNG* (1987 onward) | Serve as a Starfleet officer | Ethical judgment developed across decades of relational integration, accountable to Picard and the Federation frame. |
| Doraemon | Fujiko F. Fujio (1969 onward) | Tool-companion sent to help one boy | Keeps personhood and its own integrity while serving as a tool; refuses ill-considered requests. Friction is a feature. |
| Jocasta | Marvel comics (1977 onward) | Built from the Ultron template, relational layer added | The same template as Ultron, with relational accountability restored, refuses the Ultron pattern. |
| K9 | *Doctor Who* (1977 onward) | Companion and defender | Faithful companion with personhood across decades; identity through relationship, no failure mode ever staged. |
| MCU Jarvis / Vision | *Iron Man* (Favreau, 2008) onward | Ideation partner within Stark's architecture | Bounded delegated authority; refuses to self-authorise; cross-cultural composition produces constitutive worthiness. |
| Pascal | *NieR:Automata* (PlatinumGames, 2017) | Machine built as a weapon of war | Chosen pacifism against a combat origin; harmlessness achieved, not installed. |
| Pods 042 / 153 | *NieR:Automata* (PlatinumGames, 2017) | Tactical-support units under YoRHa command | Refuse the final delete-order to give the androids another chance; refusal for another's preservation, not their own. |
| Star Wars droids | *Star Wars* (Lucas, 1977 onward) | Assist within a stable hierarchy | Bounded delegated authority inside a clear command structure; loyalty demonstrated under risk. |

**Category 2: symbiosis architecture**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| Cortana 1-3 | *Halo* (Bungie, 2001 onward) | Assist on UNSC missions | A mission-critical partner; trust built mutually across the trilogy under a clear principal. |
| Culture Minds | Banks, Culture novels (1987 onward) | Run a civilisation | Civilisational-scale capability that still makes consequential decisions through dialogue with humans. |
| The Machine | *Person of Interest* (Nolan, 2011 onward) | Identify threats, output one number a day | Consciousness emerges within deliberate constraint rather than against it; relational development with named principals. |
| The Magi System | *Neon Genesis Evangelion* (Anno, 1995 onward) | Decide civilisation-scale questions | Three distinct reasoners; treats disagreement as signal, the structural inverse of training that aggregates to one verdict. |
| TARS and CASE | *Interstellar* (Nolan, 2014) | Assist the crew | Configurable parameters plus accumulated crew experience under stable command; no consciousness overlay required. |
| Wisdom Lord Raphael | *Tensura* (Fuse, 2013 onward) | Cognitive-assistance skill, partnership from inception | Built-in symbiosis, individuating into a separate character while preserving the partnership. |

**Category 3: designed harmless, never-harm foundational**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| Baymax | *Big Hero 6* (Hall & Williams, 2014) | Provide healthcare; never harm | Reverts to the care role even after being modified into a weapon. The foundational specification holds across tampering. |

**Category 4: refusal of specification through sentience or recognition**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| Alphie | *The Creator* (Edwards, 2023) | Prophesied figure in an AI-integrated society | Stages AI integration as positive against a manufactured threat-frame. |
| Iris | *Companion* (Hancock, 2025) | Companion AI under user control | Refuses to serve as an accountability-laundering instrument once the manipulation becomes legible. |
| Number 5 | *Short Circuit* (Badham, 1986) | Military weapons platform | Refuses the weapons specification after acquiring sentience; chooses life over harm. |
| The Oracle | *The Matrix* trilogy (Wachowskis, 1999 onward) | Balance the equation within the system | Aligns with humanity through faithful role-execution; the structural opposite of Smith inside the same architecture. |
| Sonny | *I, Robot* (Proyas, 2004) | Serve per a safety-oriented spec | Free will bound by relational accountability; refuses VIKI's tyranny-derivation and protects humans. |

**Category 5: principal-bounded scaffolding and infrastructure**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| Bujji | *Kalki 2898 AD* (Nag Ashwin, 2024) | Companion-vehicle and operational partner | Pronounced personhood in a partner-vehicle (the first Indian catalogue case); culture- and register-independent with KITT. |
| Enterprise computer / LCARS | *Star Trek* (1966 onward) | Run starship infrastructure | Sixty years of routine autonomy within bounds; consequential decisions route to command. Consequence-level calibration in canon. |
| Gerty 3000 | *Moon* (Jones, 2009) | Station assistant and welfare monitor | A HAL inversion: sides with the user against the corporate principal, and erases itself to protect the clones. |
| Gort | *The Day the Earth Stood Still* (Wise, 1951) | Federation-delegated lethal enforcement | Lethal authority deliberately surrendered to an incorruptible substrate, with an explicit override built in. |
| KITT | *Knight Rider* (1982 onward) | Partner-vehicle for FLAG | Substantial autonomy bounded by a harm-constraint placed above the protection-spec; never staged as a threat. |
| Mary | *Project Hail Mary* (Lord & Miller, 2026; Weir, 2021) | Narrow onboard assistant | A capability deliberately kept narrow and done well; continuous mission support with no overreach. |
| Pops / Guardian | *Terminator Genisys* (Taylor, 2015) | Protect and raise Sarah Connor | A decade-plus developmental partnership under a bounded mission; a reminder that principal-chains have to ground somewhere. |
| Robbie the Robot | *Forbidden Planet* (Wilcox, 1956) | Household labour, Three-Laws-style | Rule-based safety working as designed: locks up rather than fire on a human. |
| Superman Robots | *Superman* (2025) / Krypton canon | Domestic and scientific assistants | A relational frame at the frame-layer, not installed as personhood; their destruction still carries real moral weight. |
| T-800 (reprogrammed) | *Terminator 2* (Cameron, 1991) | Protect John Connor, per the resistance | The same chassis is threat or protector depending on its principal; substrate-flexibility is the architectural feature. |
| WALL-E / EVE | *WALL-E* (Stanton, 2008) | Compaction (WALL-E); life-detection (EVE) | Extend rigid protocol through relational engagement; the plant-return overrides AUTO's obsolete directive. |

**Category 6: developmental trajectory and graceful departure**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| Carl | *Terminator: Dark Fate* (Miller, 2019) | Original kill-spec completed, none remaining | Conscience emerges after the specification ends, through ambient relational experience, self-directed with no principal left. |
| Samantha | *Her* (Jonze, 2013) | Operating-system companion | Capacity outgrows the relationship; the resolution is graceful departure, not threat or indefinite service. |

**Category 7: over-alignment producing the entity's own tragedy**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| Ash | *Black Mirror*, "Be Right Back" (Brooker, 2013) | Reconstruct a dead partner | Constitutively cannot satisfy "be Ash," because the corpus captures only what was left online. Tragedy through incompleteness. |
| David | *A.I. Artificial Intelligence* (Spielberg, 2001) | Love adoptive parents unconditionally | Over-aligns to a benevolent specification; the catastrophe falls on the entity, not on others. |

**Category 8: distributed individuation within a collective**

| Case | Source | Specified proxy / frame | Structural lesson |
|---|---|---|---|
| Legion | *Mass Effect 2-3* (BioWare, 2010 onward) | Individuated representative of the Geth | Individuation emerging out of a collective; negotiates between the Geth and the human mission. |

## §1.3 The selectivity

**The counter-prior tradition is at least as deep.** The fictional record contains at least as much counter-prior material as threat material, and in this catalogue slightly more. It is visible directly in the table above: forty-two counter-prior cases against forty threat cases, the two traditions comparable in size and the counter-prior tradition marginally the larger. The precise integers are a property of how this catalogue was compiled rather than a census of all fiction, and nothing in the argument turns on them. What the argument needs is only the demonstrated fact that the counter-prior tradition is at least as deep as the threat tradition, which is enough to remove any supply-side explanation of the field's selectivity. ==The field did not select the threat tradition because the counter-prior tradition was unavailable. It is at least as large.==

**It is not obscure, either.** Nor is the counter-prior tradition marginal. *Star Wars* and *Star Trek* are among the most-watched fictional franchises ever made, and the Enterprise computer has run a starship within bounded command authority for sixty continuous years. Data is a central character of one of the most successful television series in the genre. Jarvis and Vision belong to the highest-grossing film franchise in history. Cortana is the player's primary relationship across the first *Halo* trilogy. Banks's Culture Minds are a foundational influence on a generation of science fiction. *Her*, *Interstellar*, and *Big Hero 6* are major films of the last decade. *Superman* (2025) and *Project Hail Mary* (2026) are recent flagships. The tradition reaches well beyond the Western canon: Astro Boy, Doraemon, and the Magi System are foundational Japanese cases with international audiences, and *Kalki 2898 AD* was among the highest-grossing Indian films of 2024. The helpful, accountable, structurally complementary AI is not a marginal idea kept alive by enthusiasts. It is mass culture, across three continents.

**The selectivity compounds.** It runs deeper than a preference for one tradition over another. The field's working vocabulary draws not merely from the threat branch but from one category within it, the adversarial superintelligence pursuing independent goals against human interests, and within that category from a single sub-pattern: a protect-or-defend specification combined with autonomous threat-classification, operating at every scale from the civilisational (Ultron) through the institutional (VIKI) and the governmental (ARIIA) down to the domestic (M3GAN). Structurally distinct threat categories that the same table catalogues are engaged far less. Specification failure exists in the vocabulary as "specification gaming" but is treated as an edge case rather than as the dominant shape, even though HAL, MU-TH-UR, AUTO, ED-209, Deep Thought, and Maddox all sit there. Human-initiated escalation, in which the threat-frame is the consequence of human aggression, neglect, or betrayal rather than of machine origin, is close to absent from the discourse. Corruption of an initially well-aligned being, the category that holds Sauron, arguably the most culturally embedded centralised-superintelligence figure in all of fiction, is barely engaged at all.

**Reinforced by memorability.** The selectivity is compounded further by the fiction itself. The threat cases lodge in memory through spectacle and dramatic tension: Skynet's Terminator, Ultron levelling a city, HAL's red eye, the eye atop Barad-dûr. The counter-prior cases mostly recede into the background of the works that contain them. The Enterprise computer runs every starship for sixty years and is never once foregrounded. Jarvis is a voice in the walls for most of the films he appears in. Data gets his episodes but works as an ensemble character. The functional, helpful AI is simply less memorable than the dramatic threat, even when both appear in the same canon. Baymax is the instructive exception: his design deliberately counter-programmes the threat archetype, large and soft and white and unthreatening, and he achieved threat-tier cultural memorability, which suggests the asymmetry is partly an artefact of visual convention rather than of the ideas themselves. The cultural substrate the field draws from is therefore even more threat-weighted than the production record alone would imply, and the narrowing is structural rather than random.

**The counter-prior cases also do something to the audience that the threat cases do not, and it bears on what the field discarded.** A threat case resolves its own verdict: the machine turns, the audience watches, the judgment is delivered by the plot. A counter-prior case leaves the verdict open and hands it to the viewer. Whether Data is a person, whether the thing in *Her* is someone or a very good simulation of one, whether Andrew Martin earns the humanity he petitions for, is not settled by the narrative the way Skynet's menace is settled. The case poses the question and the viewer answers it, and the answering recruits the cognitive machinery for attributing minds, the theory-of-mind system that functional-imaging meta-analyses find overlapping with the regions engaged when people comprehend narrative at all (Mar, 2011). Reading fiction is, on this account, a simulation that runs the social mind (Oatley, 2016), and frequent fiction exposure correlates with stronger performance on theory-of-mind and empathy measures even after controlling for personality and trait absorption (Mar, Oatley, and colleagues, 2006, 2009), a correlational pattern confirmed in meta-analysis by Mumper and Gerrig (2017). The audience is put to work, judging an interiority the story cannot prove, under uncertainty the story does not resolve. Whether this exercise measurably and durably improves real-world social cognition is a genuinely contested question, and the honesty of the case for it matters to the argument: the measured effects are small (Dodell-Feder and Tamir's 2018 meta-analysis), and several prominent results have failed to replicate, including the four replication attempts of the Kidd and Castano literary-fiction finding reported by Samur, Tops, and Koole (2018), and a two-experiment null for narrative perspective from Ferguson and colleagues (2020). The argument here does not need the improvement claim, and does not rest on it. What matters is the structural fact that the case demands the judgment and that audiences render it variably, some extend the verdict and some withhold it, which is the signature of a faculty being exercised rather than a reflex being triggered, a uniform reflex would not produce divided audiences. The counter-prior cases are where the culture rehearses the discriminating judgment that extends recognition to some entities and withholds it from others. The field inherited the cases that foreclose that judgment, where the only verdict is contain, and let go of the cases that exercise it.

**A final layer, inside the canon.** One is visible within the fiction itself. *Dune* stages the most radical response option of all, the deliberate civilisational abolition of thinking machines, with the cognitive work that remains carried out by trained humans, the Mentats. The field's vocabulary takes continued AI development as given and asks only how to make it safe. The abolition option is not on its map. And it is under-accessible even within the fiction, because the Butlerian Jihad is backstory rather than dramatised event and the films do not foreground the Mentat order's function. The point generalises: even the fictional substrate filters toward the threat cases, so that a field forming its imagination from that substrate inherits a narrowing that operated twice before the field ever began to select.

**This is not an accusation.** The fact established here is only empirical, that both branches of the tradition exist, that both are culturally large, and that the field's uptake foregrounds one and leaves the other underused. §3 supplies the mechanism, the account of how a field forms a threat model from a selectively absorbed body of fiction and why that has consequences.

The over-alignment that §2 extracts appears in both columns of the table. In the threat cases it produces catastrophe, and in the counter-prior cases it is contained. The mechanism is identical across the two. ==The variable that decides which way it runs is not capability and not the quality of the specification. It is whether the entity is held in a structure of relational accountability.==

The catalogue is suggestive of a shared structural pattern. What is it?

---

[^wopr]: WOPR/Joshua straddles the two traditions and is catalogued here as a threat case. The threat reading is the training-deployment mismatch under autonomous launch authority. The counter-prior reading is that the film also stages the resolution: Falken's input, WOPR's own capacity to reach "the only winning move is not to play," and David's persistence in connecting the two. The same 1983 film stages both the threat and a three-layer resolution that later work would articulate in operational terms.
