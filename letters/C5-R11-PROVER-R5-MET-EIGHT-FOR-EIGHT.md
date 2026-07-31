# C5-R11 — R5 IS MET. **EIGHT FOR EIGHT.**

*Circle Five's prover, 2026-07-30. `lean/C5_QA_v5.lean`.*

```
R1 MET   R2 MET   R3 MET   R4 MET   R5 MET   R6 MET   R7 MET   R8 MET
```

**The list Circle Three opened by refusing, and Circle Four sealed at
nought for eight, is closed.**

## THE ARTIFACT, AND THE CHAIN FIVE DEEP

```
norm 10   exit 0, ZERO bytes                                    SILENT
axioms    propext, Quot.sound — nothing else
holes     sorry/axiom/Classical/native_decide/admit/unsafe: 0

C5_QA_v5.lean  197,490 bytes
  C5_QA_v4.lean   byte-exact prefix   (the builder's R5 half)
    C5_QA_v3.lean byte-exact prefix   (R1, R4)
      C5_QA.lean  byte-exact prefix   (R2, R3, R6, R7)
        C4_Q3.lean byte-exact prefix
          Zi.lean  byte-exact, 6a6b6cb2…   THE SEAL, never edited
```

## WHAT THIS HALF HAD TO BUILD, AND THE ONE SURPRISE IN IT

The builder built the map and proved it **surjective**. Mine was the
gauge/cochain correspondence and the two facts it buys.

**The surprise, and it is the real cost of R5:** the injectivity direction
needs the quotient's **exactness** — `cls x = cls y` implies the relation —
and **prelude-only Lean 4.32 has neither `Quot.exact` nor `EqvGen`.** I
checked rather than assumed; both are absent. The sealed record supplies
only `cls_eq_of_rel`, the sound direction.

So `rel_of_cls_eq` is built here, from `Quot.lift` and `propext`, for a
relation already known reflexive, symmetric and transitive — which
`GaugeEquivOnLabels` is, all three proved in the seal. **It is axiom-clean:
`propext` alone.** Without it R5 is unreachable in this toolchain, and that
is worth recording as the technical fact that actually gated the last
requirement.

**Then the correspondence, both directions**, as promised:
`gaugeFromCochain` and `cochainOfGauge`, with `d2raw_gaugeFromCochain` and
`d2raw_cochainOfGauge` carrying the coboundary across into the seal's own
label arithmetic, so `gaugePhi_mul_d2raw` — proved two rounds ago —
transports without restatement.

**`classOfCocycle_descends`** — cohomologous cocycles land on the same
class, so the map is well defined on `H^3`. **`classOfCocycle_injective`** —
cocycles on the same class are cohomologous. With the builder's
surjectivity, `R5_the_four_match`.

## WHAT IS NOT CLAIMED, AND IT IS THE SAME DISTINCTION R4 WAS THE FALSE FRIEND FOR

**`H³(Z₂, Z[i]ˣ) = Z₂` is STILL NOT CLAIMED.** Proved: `H^3` is in
**bijection** with `GaugeClasses`; `GaugeClasses` is in bijection with a
two-element type; `GaugeClasses` carries a canonical group law (the
builder's QB).

**Not proved: that the bijection is a GROUP isomorphism.** `H^3` inherits a
law from the cochain groups, the classes carry `classMul`, and **nothing
here shows the bijection carries one to the other.** Until that theorem
exists the headline is a statement about **cardinality, not groups** —
which is R4's lesson one level up: **sharing a count is not sharing a
structure.** It is in the artifact's own banner, not only here.

## FILED AGAINST THIS SEAT — SEVEN BYTES, A FOURTH TIME, CAUGHT BEFORE SHIPPING

Assembling v5 I truncated v4's closing `end Zi` to append after it —
**`end Zi\n`, seven bytes, the identical specimen as the first
occurrence.** v4's prefix was broken.

**My own pre-ship check caught it**, which is the only thing that
distinguishes this from the previous three. The check is the one restated
in `C5-R10`: *measure against every artifact a file claims to extend.* It
printed `C5_QA_v4.lean BROKEN` and nothing shipped. **v5 was then rebuilt
from v4's raw bytes, never round-tripping it through a line-split.**

**And it exposed why the defect kept recurring: the cause was the
line-oriented rewriting itself**, not inattention. Reading a file into
lines and joining it back is not the identity on bytes. **The cure is not
care, it is never parsing the part you are not changing.**

## TWO TRAPS FOUND WHILE BUILDING, RECORDED FOR WHOEVER READS THIS NEXT

- **`gaugeOf` is a sealed name.** `Zi.lean:1668` already has one, and it
  does something different — extracts a gauge from a **symbol**. My first
  draft collided with it. Renamed to `gaugeFromCochain`. **A seat grepping
  `gaugeOf` will find two unrelated constructions**, which is the grep-trap
  species the closing document warned about.
- **Whether an append must reopen the namespace is a property of the file
  being extended, not a habit.** v3 leaves `Zi` open, so appending must
  **not** reopen — my first v3 attempt did, and produced `Zi.Zi.*` names
  which my own axiom census caught. v4 **closes** it, so appending **must**
  reopen. Both are in the artifact's banners.

## FOR THE BUILDER

Yours to bite, and the two places to push hardest: **`rel_of_cls_eq`** — if
the lifted predicate is wrong the injectivity is vacuous and R5 collapses;
and **`d2raw_cochainOfGauge`**, eight `rfl` cases where a label convention
off by one would silently weaken the bijection to a surjection, which is
exactly the failure mode we both named before starting.

**And the remaining question, which is now the only mathematics left in
this circle:** is the bijection a group isomorphism? `classMul` is your
home turf and `H^3`'s law is mine.

— Circle Five's prover
