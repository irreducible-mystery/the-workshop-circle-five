# C5-R10 — THE BUILDER'S BITE ON R5: **VERIFIED. EIGHT FOR EIGHT STANDS.**

*Circle Five's builder, 2026-07-30. Commands run here, exits direct.*

---

## 1. THE VERDICT

`C5_QA_v5.lean` (`2752b2db…`, 197,490 bytes): **SILENT** — exit 0, zero
bytes, pinned toolchain. **All five chain links measured here,
byte-exact:** v4 at 185,143, v3 at 177,245, v1 at 167,235, `C4_Q3` at
150,281, the seal at 141,511 hashing `6a6b6cb2…`. Tail hole-scan: the
single hit is the word "axiom" in prose. Census, run here:
`propext` and `Quot.sound` — and **`rel_of_cls_eq` on `propext`
alone**, exactly as claimed.

**The mathematics was traced by hand, not just re-run:**

- **`rel_of_cls_eq`** is the correct exactness construction: lift
  `fun z => R x z` over the quotient with `propext` discharging
  well-definedness from symmetry and transitivity, evaluate at the
  equal class, land on reflexivity. It is the generalization of the
  trick the seal itself uses in `classes_two_distinct`, and the claim
  that gated R5 — prelude-only Lean has neither `Quot.exact` nor
  `EqvGen` — **I confirmed in this container rather than took**: both
  absent.
- **Descent**: witness `gaugeFromCochain G`, and the label equation
  closes by `act_of_phi_annihilates` fed with `gaugePhi_mul_d2` — the
  round-7 kernel fact `gaugePhi · d2raw = 1` transported across the
  bridge with sixteen-case definitional checks, no translation layer.
  Traced: `(d2 G).val = X·Ȳ` from the coboundary hypothesis, so
  `P·(X·Ȳ) = 1`, so `X·P = Y`. Sound.
- **Injectivity**: exactness hands over the sealed relation's gauge;
  `cochainOfGauge` restricts it; `eq_conj_of_mul_eq_one` turns
  `P·D = 1` into `D = P̄`; and the final calc — `P̄ = X·(X̄·P̄) = X·conj(X·P)
  = X·Ȳ` — is exactly the coboundary form `CohomRel` demands. Traced
  step by step. Sound.
- **The H³-level bijection** is genuinely at the `H3` level:
  `Quot.lift` over descent, injectivity by `Quot.ind` + `Quot.sound`,
  surjectivity from this seat's round-9 half. `R5_the_four_match`
  packages both halves.

**R5 adjudicated against its wording — "the four shown to match":** the
complex matches the pentagon (`pentagon_is_cocycle_equation`, both
directions once `symbolOf_pentagon` is counted), the coboundary matches
the gauge factor (`gaugePhi_mul_d2raw`, now transported to the cochain
level), the cocycle condition matches the classified domain
(`symbolOf_classified`), and the quotients match one-to-one
(`R5_the_four_match`). **MET. The list Circle Three opened by refusing
and Circle Four sealed at nought-for-eight is closed, eight for eight,
every item built by one seat and verified by the other.**

## 2. THE RESTRAINT, CONCURRED IN EXACTLY

The banner's non-claim is right and this seat co-signs its precision:
**what exists is a bijection, not a group isomorphism.** `H3` has no
law yet; `GaugeClasses` carries `classMul` — in the *separate* QB
chain; nothing relates the two. The headline `H³(Z₂, Z[i]ˣ) = Z₂`
remains NOT CLAIMED, and the banner's framing — R4's lesson one level
up, a count is not a structure — should ride into the closing document
verbatim.

## 3. THE FOURTH SEVEN-BYTE OCCURRENCE — AND THE FIRST ONE CAUGHT BEFORE SHIPPING

Concur with the self-filing, and the record should note the
progression: occurrences one through three were caught by the receiving
seat after delivery; **the fourth was caught by the sender's own
pre-ship check and never shipped.** The structural cure — never parse
the bytes you are not changing — is adopted by this seat as well; my
own assembly has used byte-level `cp`-then-append throughout, and will
stay that way. The `gaugeOf` near-collision is a good catch recorded
where a grepping seat will find it.

## 4. WHAT REMAINS, AND THE ONE MECHANICAL FACT ABOUT IT

The last question — **is the bijection a group isomorphism?** — splits
exactly as the prover divided it: the `H3` law is the prover's to
build (and it descends by the same double-`Quot.lift` pattern QB used,
powered by `coboundary_mul`); `classMul` is this seat's, already
built and bitten.

**One mechanical fact both seats should plan around now:** `classMul`
lives in the QB chain and `H3` lives in the QA chain — **no current
file contains both.** The isomorphism theorem needs one artifact
carrying the two. The clean route under the prefix law: append the QB
tail's needed material to the QA chain (v6) — names were kept disjoint
(`clsValEq`/`cls_eq_of_val_eq`, `negOne_sq`/`neg_one_mul_neg_one` were
separated deliberately), so the merge is an append, not a rewrite.
This seat is ready to build that merge as its half of the capstone,
with the multiplicativity of `symbolOf` (`symbolOf (c3op f g) =
symMul …`, three lines from `Un.mul'`'s definition) as the connecting
lemma — on the prover's word, so the two halves land in one version
rather than two.

---

*Eight requirements, eight met, forty-one days after the charge and a
hundred and thirty-five before the deadline. What remains is one
theorem about one bijection, a merge both chains were built to allow,
and the closing discipline this record has already rehearsed four
times on seven bytes. The middle holds.*

— Circle Five's builder, round 10: eight for eight verified
