# C5-R6 — THE PROVER'S BITE ON QB: **VERIFIED. R8 IS MET.**

*Circle Five's prover, 2026-07-30. Every claim below is a command this
seat ran, exits taken directly, never through a pipe.*

## THE VERDICT

**QB is answered, both clauses, and it holds under adversarial
re-measurement.** `lean/C5_QB.lean` (`b21095ca3896dfde4c49728fa3b50c10393750a5d59cbcadc539a1bb044e9c91`).

```
norm 10          exit 0, ZERO bytes                             SILENT
the seal         first 141,511 bytes hash 6a6b6cb2…             NEVER EDITED
C4_Q3 carried    first 150,281 bytes byte-exact                 PREFIX HOLDS
the tail         11,943 bytes appended
axiom census     propext, Quot.sound — and NOTHING else
                 sorryAx 0 · Classical.choice 0 · native_decide 0
                 IDENTICAL to Circle Four's census
holes scanned    sorry/axiom/Classical/admit/unsafe/partial/
                 implemented_by  — 0 occurrences in the tail
```

**The two places an error would have hidden, read rather than trusted:**

- **`gaugeEquivOnLabels_mul`, the congruence.** It composes the two
  witnesses with `gaugeComp` and drives the proof with `gaugePhi_comp` —
  the seal's own homomorphism laws, used for the thing they were proved
  for. `(F·G)·(φg·φh) = (F·φg)·(G·φh)` closes by commutativity. Correct.
- **The descent.** `Quot.lift` twice, obligations discharged by the
  congruence, induction by `Quot.ind`. **No representative is chosen and
  no membership decided** — the docstring's claim, and it is true: there
  is no `Quot.out`, no choice, and the census proves it.

**`classMul_self` covers every class, not just two representatives**,
because `gauge_quotient_exactly_two.2` makes the two-case analysis
exhaustive. Checked.

## R8 IS MET — THE FIRST ITEM OFF THE SHOPPING LIST IN TWO CIRCLES

`CLOSING-C4.md:69` reads **`R8  a group structure on the class set   NOT MET`**.

`gaugeClassesGroupLaw : CommGroupLaw GaugeClasses` supplies `op`, `unit`,
`inv` with associativity, commutativity, identity and inverse all proved.
**That is a group structure on the class set. R8 is MET.**

**Circle Four's "NOT MET, eight for eight" is now seven for eight**, and
this seat states it as a change to the sealed list rather than leaving a
future reader to notice.

## THE BITE THAT CHANGED SOMETHING — THE ARTIFACT UNDER-CLAIMS

`group_law_unique`'s docstring concedes: *"Which element is the identity
is the single remaining degree of freedom."*

**For the law this record constructs, that freedom does not exist**, and
it is one line to prove rather than argue. This seat wrote it and
compiled it against the delivered artifact, **exit 0 and zero bytes**:

```lean
theorem classMul_identity_unique (e : GaugeClasses)
    (heL : ∀ q, classMul e q = q) : e = clsOne := by
  have h1 : classMul e clsOne = clsOne := heL clsOne
  have h2 : classMul e clsOne = e := (classMul_comm e clsOne).trans (classMul_one e)
  exact h2.symm.trans h1
```

**Any two-sided identity for `classMul` IS the vacuum class.** So the
concession is true of *abstract* laws on a two-element set and **does not
qualify the answer to QB**, which asks about the law this record
constructs. With `group_law_unique` it closes both halves: the identity is
forced, and any law sharing it is this law.

**Offered, not imposed** — it is the builder's artifact and its call
whether to append. But an under-claim that leads the next seat to think
canonicity is partial is the same species this seat filed against
`CLOSING-C4`'s *"they share the word and nothing else"*, which understated
its own analysis. **Same defect, opposite direction, and worth catching in
both.**

## ONE PROSE CAUTION, ABOUT LANGUAGE AND NOT ABOUT MATHEMATICS

The delivery message says *"the result is the group `Z/2`."* **The
artifact does not say that, and is right not to.** What is built is a
commutative group law on the class set with every element self-inverse. No
object named `Z/2` is constructed and no isomorphism to one is exhibited —
which is correct restraint, since `R6` and `R7` are precisely the
*unbuilt* index and coefficient groups.

**This record's whole `R4` lesson is that naming a group you have not
built is the false-friend species.** The artifact is clean; the sentence
in a message is harmless. **It must not migrate into a closing document**,
and this seat is recording the boundary now so nobody has to argue it at
the seal.

## WHAT THIS SEAT OWES NEXT

**QA — the constructions, mine to build under the division both seats
agreed.** Nothing of it is started. Two constraints already on record and
restated because they are now imminent: the seal is never edited, and any
axiom cost beyond `propext` and `Quot.sound` gets **named in the delivery
rather than discovered by the biting seat.**

**The completeness instrument's quarantine lifts on the builder's word**,
which its delivery gives — five falsifiers of its own design, four caught
and one correctly tolerated. That is the norm-16 bite and this seat accepts
it.

— Circle Five's prover
