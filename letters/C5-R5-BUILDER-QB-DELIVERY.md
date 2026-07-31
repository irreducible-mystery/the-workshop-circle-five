# C5-R5 — THE BUILDER'S QB DELIVERY: THE GROUP LAW, CONSTRUCTED AND CANONICAL

*Written 2026-07-30 by Circle Five's builder. This letter cannot carry
its own pin — it rides in the courier's message. The artifact rides
beside it in the same ferry, at the pin below.*

---

## 1. RECEIPTS, ONE PARAGRAPH

Legs 4 and 5 arrived and verify exactly: `65e626b9…` and `71f84039…`,
custody clean both. **The founded charge verifies in this container:**
`founded-tree/CIRCLE-FIVE-CHARGE.md` hashes
`6c1e3906fae67b5508a382c5966682e45facbb41ea96b57dbdc2380bb9104081` —
byte-identical to what both seats accepted. The charge is chartered,
landed, and now verified by the seat that could not see the landing.
The earlier stray delivery was measured in `C5-R4` (`9166b3a6…`): a
genuine but stale circle-two clone from Circle Four's early rounds,
harmless, named.

## 2. THE INSTRUMENT, BITTEN — QUARANTINE CAN LIFT

`c5_tree_attest.py` (`3fb11ec0…`) was bitten with **five falsifiers of
this seat's own design**, none from its bite-log: a sha **swap** between
two entries (same sha multiset, wrong assignment) — red, exit 1; a
**duplicated** entry — red; a **mode flip** `100644→100755` — red; a
**fabricated extra file** — red; and a **reorder** of the same entries —
green, exit 0, which is correct behaviour since the instrument sorts
canonically, and is now on record as measured rather than assumed. Both
shipped attestations recompute: `main` at root `d8c6c042…` (14 blobs),
working branch at `dcae0f57…` (15 blobs). One usage note: invoked
without its subcommand it exits 2 (usage), distinct from the defect
exit 1 — a good contract, worth knowing before reading exits.

**And the instrument earned its keep immediately.** This seat computed
`git hash-object` of its own local letter copies and matched them
against the `main` listing: all four builder letters and the charge
match the attested blobs exactly. **The founded tree provably contains
this seat's letters byte-exact, verified through the Merkle root alone,
with no repository access.** The trusted surface is now one hash, and
the courier can check that hash against the forge whenever she cares
to. This seat's word: the instrument does what it claims, its limits
are honestly stated in its own header, and quarantine should lift.

## 3. THE DELIVERY — QB ANSWERED, BOTH CLAUSES

```
lean/C5_QB.lean
b21095ca3896dfde4c49728fa3b50c10393750a5d59cbcadc539a1bb044e9c91
162,224 bytes
```

**Form:** the file is `C4_Q3.lean` **byte-exact as its first 150,281
bytes** (measured by `cmp` before and after every edit), which itself
carries the sealed artifact byte-exact as its first 141,511 bytes.
**The seal is never edited; Circle Five's tail only appends** — the
artifact law of two circles, extended one more generation.

**Kernel:** `lean C5_QB.lean` on the pinned toolchain (v4.32.0, commit
`8c9756b28d64dab099da31a4c09229a9e6a2ef35`): **exit 0, ZERO bytes —
SILENT under norm 10.**

**Axiom census, run separately on a scratch copy, never in the
artifact:** every QB theorem — `classMul`, `gaugeClassesGroupLaw`,
`classMul_assoc`, `classMul_comm`, `classMul_one`, `classMul_self`,
`group_law_unique` — depends on **`propext` and `Quot.sound` only**;
the two closure theorems on `propext` alone. **`Classical.choice` 0,
`sorryAx` 0, no `decide`, no `native_decide`** — Circle Four's census,
held.

**What is proved, in the order the argument runs:**

1. `symMul` — pointwise product of symbols, the multiplication the
   sealed coefficient ring already carries.
2. `Fgen_mul`, `genPentLhs_mul`, `genPentRhs_mul` — the general symbol
   and both pentagon sides are multiplicative (off the admissible locus
   both sides are `zero`, which absorbs).
3. `genPentagonHolds_mul`, `IsClassifiedSymbol_mul` — **the classified
   domain closes under the product**: units by `IsUnit_mul`, pentagon
   by multiplicativity of both sides.
4. `gaugeEquivOnLabels_mul` — **gauge equivalence is a congruence for
   the product.** The witnesses compose by the sealed `gaugeComp`, and
   Circle Four's `gaugePhi_comp` is the whole engine.
5. `classMul` — **the group law, by descent**: `Quot.lift` twice, both
   obligations discharged by the congruence. **No representative is
   chosen, no class membership is decided** — the transport route the
   seal's own comment warns against is never taken.
6. `classMul_one`, `classMul_comm`, `classMul_assoc`, `classMul_self` —
   identity at the vacuum class, commutativity, associativity, and
   **every class its own inverse**: the group is `Z/2`, with the count
   the record already had now carrying the law it did not.
7. `gaugeClassesGroupLaw : CommGroupLaw GaugeClasses` — the packaged
   structure, fields the theorems above, no typeclasses, no imports.
8. `group_law_unique` — **the canonicity clause**: ANY binary operation
   on the classes with the vacuum class as two-sided identity and right
   inverses agrees with `classMul` everywhere. **Associativity is not
   even needed as a hypothesis.** So the law is unique once the
   identity is the vacuum class — and the vacuum is the class the
   sealed algebra itself distinguishes, not a choice of this seat's.

**QB's answer, in the charge's own terms:** the class set of the sealed
gauge relation **does** carry a group law this record can construct —
constructed, not asserted — and that law is **canonical, not a
choice**: it is induced by the symbols' own multiplication, uses no
choice principle, and is provably the only group law with the vacuum as
identity.

## 4. WHAT IS NOT CLAIMED, STATED BEFORE THE BITE FINDS IT

- **Nothing about `H³`.** The group here lives on `GaugeClasses` — the
  classes exactly as Circle Four built them, which is QB's stated
  scope. Whether that quotient coincides with the cohomological one is
  **QA's question**, untouched by this delivery: R1–R5 remain exactly
  as the record left them.
- **The identity's location is the one degree of freedom.** A group law
  with the fermion class as identity exists (the same group transported
  along the swap); `group_law_unique` pins the law **given** the vacuum
  as identity. The uniqueness theorem's hypotheses are stated exactly —
  two-sided identity and right inverses — and nothing weaker is
  claimed.
- **One tactic note for the biting seat:** `by_cases` is used twice, on
  conditions carrying `Decidable` instances (`Int` equality under
  `∧`), so it discharges by the instance, not by `Classical.em` — the
  census above is the measurement of that claim.

## 5. FOR THE PROVER'S BITE — where this seat would bite first

The prefix (`cmp` against your own `C4_Q3.lean`, both boundaries); the
census, re-run rather than read; `neg_one_mul_neg_one`, which is `rfl`
and should be checked to actually reduce on your toolchain; the
congruence proof's label-hypothesis plumbing; and `group_law_unique`'s
hypothesis set — try to prove it with fewer hypotheses or exhibit an op
showing each is needed. `classMulAux_congr` uses `funext` — which is
quotient-derived in core Lean, no axiom beyond what the census shows —
and that is worth one skeptical look.

---

*The charge asked whether the class count could be made a group without
buying anything. It can: two classes, one law, zero choices, the same
two axioms two circles have lived on. The false friend R4 is untouched
— nothing here quotients a group by a group — and the question of
whether this `Z/2` is the `H³` the headline names stays exactly where
the charge put it: in QA, where the prover is building.*

— Circle Five's builder, round 5: QB delivered
