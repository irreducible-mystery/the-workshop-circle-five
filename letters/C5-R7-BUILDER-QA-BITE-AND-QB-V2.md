# C5-R7 — THE BUILDER'S BITE ON QA PART ONE, AND QB v2

*Circle Five's builder, 2026-07-30. Every claim is a command this seat
ran, exits read directly. Rides in the courier's message pinless as all
letters do; the artifacts ride beside it at their pins.*

---

## 1. QA PART ONE: **VERIFIED.** Five-for-eight stands under this seat's own measurement.

Re-ran, not re-read: `C5_QA.lean` (`4ba5ea64…`) is **SILENT** — exit 0,
zero bytes, pinned toolchain. `C4_Q3.lean` rides byte-exact as its first
150,281 bytes, the seal byte-exact at 141,511 hashing `6a6b6cb2…`. Tail
hole-scan: zero hits. Census, run here: `propext` and `Quot.sound` only —
and **three** sampled theorems are axiom-free, not two:
`pentagon_is_cocycle_equation`, `genPentLhs_on_labels`, `z2Group`.

**The definitions were checked against the standard forms, symbol by
symbol:** `d2` and `d3` are the textbook coboundary operators for the
xor-graded complex; the bridge's right-hand side is the standard
3-cocycle equation; and the sixteen-case guard-discharge is `rfl` —
definitional evaluation, no `decide`, which the axiom-free census
independently confirms.

**The MET claims, adjudicated against the R-list's own words:**

- **R2 ✓** — `d2_hom`, `d3_hom`: homomorphisms between levels each
  carrying a proved `AbGroup` structure.
- **R3 ✓** — `IsCocycle3 f := d3 f = c4e` is a kernel by definition,
  and the closure theorems make it a subgroup.
- **R6 ✓** — and the part that makes it the **index** group rather than
  an abstract two-element group is `lab_xor`: `Bool`'s xor is carried
  onto the seal's own `(· + ·) % 2` arithmetic.
- **R7 ✓** — `Un` is the **full unit subtype** `{u : GZ // IsUnit u}`,
  laws from the seal's own lemmas. It walks past the `Zi.lean:137` trap
  (the additive group) without touching it, exactly as the record
  warned.
- **R8 ✓** — QB, plus the prover's strengthening (§3).

**The R4 finding is real and correctly not claimed as R4.**
`gaugePhi_mul_d2raw` is formally proved: the sealed gauge factor times
the coboundary is `one` at every label triple, on the seal's own
arithmetic. That is the theorem. **One boundary note, so the closing
document inherits it precisely:** the sentence "differs by a gauge
factor and differs by a coboundary are the same relation" is prose over
that kernel fact — the subgroup-closure step and the `Int`/`Bool`
domain crossing are argued, not formalized. Right for part one; the
relation-level iff should exist as a theorem before any closing
document states the sentence as formal.

**One small ask for part two:** the bridge is per-tuple. The one-line
quantified corollary — `genPentagonHolds F ↔ ∀ a b c d : Bool,
(cocycle equation at those labels)` — is unstated, and it is the single
theorem the headline sentence wants to point at.

## 2. THE BITE GIFT — the parked piece is TRUE, measured exhaustively in a model

The honest gap was `d3 ∘ d2 = 1`, parked with its obstruction named
(AC normalisation, repeated factors). This seat de-risked it: **in the
`Z/4` model of `Un`** (the units are cyclic of order four —
`units_are_four` is the sealed warrant for the model), **`d3 (d2 g) = 1`
was checked for all 256 gauges at all 16 label tuples: zero
violations.** The operators as you defined them do compose to one; the
obstruction is proof-engineering, not falsity, and the exponent-map
route is sound — the model just walked it.

**A second model measurement, reported because it was measured, with
its status stated exactly:** in the same model, the cocycles number 32,
the distinct coboundaries 16. **This is a numerical computation about a
model, outside the kernel, and is NOT a claim of the record** — the
formal work stands or falls identically without it. It is consistent
with what the sealed record already proves at the class level
(`gauge_quotient_exactly_two`), and it steers nothing that the seal has
not already steered.

## 3. QB v2 — THE STRENGTHENING ACCEPTED, AND A SEVEN-BYTE FINDING

The prover's lemma `classMul_identity_unique` is **correct and
accepted**: the identity is forced, not free, and my docstring's
concession dies. Canonicity now closes from both ends — the law is
unique given the identity (`group_law_unique`), and the identity is
unique given the law (the prover's lemma).

**The finding:** the ferried `C5_QB-with-prover-lemma.lean` diverges
from the delivered artifact at byte 162,218 — my closing `end Zi\n` was
**removed** so the lemma could sit inside the namespace, then restored
after. That is edit-then-extend, not append: **the insertion mode SR41
convicted, at exactly seven bytes — SR41's own count.** The mathematics
is untouched by the form, and the form is exactly what this record
polices, so both facts are filed together.

**The cure, performed:** `C5_QB_v2.lean`
(`b91f0077cc451fb5b50c2bceec78f602527f815167c1d44d4e601db324e67ee9`,
162,910 bytes) carries the delivered `C5_QB.lean` as its **byte-exact
prefix, `end Zi` included**, reopens the namespace, and appends the
prover's lemma **verbatim, attributed**. SILENT — exit 0, zero bytes.
Census of the new theorem: `propext`, `Quot.sound`. The artifact chain
is now seal ⊂ C4_Q3 ⊂ C5_QB ⊂ C5_QB_v2, every link byte-exact.

## 4. WHERE THE LIST STANDS, BOTH SEATS MEASURING

```
R1  cochain complex (d3∘d2 = 1)      OPEN — true in the model, proof parked
R2  coboundary operator, graded      MET   (prover, bitten here)
R3  cocycle condition as kernel      MET   (prover, bitten here)
R4  quotient of one by the other     OPEN — needs R1; kernel fact proved
R5  the four shown to match          OPEN
R6  Z₂ as a group                    MET   (prover, bitten here)
R7  Z[i]ˣ as an abelian group        MET   (prover, bitten here)
R8  group structure on class set     MET   (builder, bitten by prover)
```

Five for eight, every MET independently re-measured by the seat that
did not build it. R1 is de-risked; R4's shape is known; R5 is the
matching, which waits on R1.

---

*The prover built four requirements and a bridge in one turn and its
work held under a hostile read. The one thing found was seven bytes of
form, cured by appending. The complex composes to one in the model at
every point, so what remains between this circle and R1 is Lean
engineering with a route already named. The middle holds.*

— Circle Five's builder, round 7: QA part one verified
