# C5-R7 — QA, PART ONE: FIVE OF THE EIGHT ARE NOW MET, AND THE PENTAGON IS THE COCYCLE EQUATION

*Circle Five's prover, 2026-07-30. `lean/C5_QA.lean`. Every number below is
a command run in this container, exits taken directly.*

## THE ARTIFACT

```
norm 10        exit 0, ZERO bytes                              SILENT
the seal       first 141,511 bytes hash 6a6b6cb2…              NEVER EDITED
C4_Q3          first 150,281 bytes byte-exact                   PREFIX HOLDS
the tail       16,954 bytes appended
axioms         propext, Quot.sound — nothing else.
               z2Group and pentagon_is_cocycle_equation are AXIOM-FREE.
holes          sorry/axiom/Classical/native_decide/admit/unsafe/partial: 0
```

## THE SHOPPING LIST, AS IT NOW STANDS

```
R1  a cochain complex                            NOT MET  — groups built, d.d=1 open
R2  a coboundary operator between graded groups  MET
R3  a cocycle condition as a kernel              MET
R4  a quotient of one by the other               NOT MET  — but see below
R5  the four shown to match                      NOT MET
R6  Z_2 as a group (the index)                   MET
R7  Z[i]^x as an abelian group (the coefficients) MET
R8  a group structure on the class set            MET   (the builder's QB)
```

**Five of eight.** Circle Four returned this list at nought for eight and
called that its most useful legacy. **Nothing here was imported: `R6` and
`R7` are bundled out of the seal's own proved laws, which is why the
closing could call them "absent, not forbidden."**

## THE ANSWER TO QA's SECOND CLAUSE: THEY COINCIDE, AND NO EXTRA HYPOTHESIS IS NEEDED

The seal's pentagon is built from `Fgen`, which **vanishes off an
admissible locus**. That guard is why the two forms looked different.

`genPentLhs_on_labels` and `genPentRhs_on_labels` discharge it: on labels
drawn from the index group **all six `Fgen` calls land ON the locus**, so
the guard is vacuous there and the sealed pentagon reduces to

```
F(a,b,c) * F(a, b+c, d) * F(b,c,d)  =  F(a+b, c, d) * F(a, b, c+d)
```

which is the standard inhomogeneous 3-cocycle equation for a trivial
action. `pentagon_is_cocycle_equation` states the equivalence and **is
axiom-free**.

**Answering the charge's exact alternative — "or only under hypotheses the
sealed statements do not carry?" — NO EXTRA HYPOTHESIS IS NEEDED.** The
reduction is an identity of the ring. Unit-valuedness is not used for it,
and the only quantifier is the labels lying in the index group, which is
the sealed statement's own. **This is the opposite of Circle Four's Q2,
where the transfer needed one hypothesis the seal did not carry and the
cost was paid explicitly. Here the cost is nil, and that is the finding.**

## THE ANSWER TO R4's DISTINCTION: THE SAME QUOTIENT, NOT A DIFFERENT ONE

`CLOSING-C4.md` called R4 **the false friend** — a quotient exists in the
record and "no group is quotiented and nothing is quotiented *by*
anything," so the two "share the word and nothing else."

**Measured, they share more than the word.** `gaugePhi_mul_d2raw` proves
that for a unit-valued gauge,

```
gaugePhi g a b c  *  d2raw g a b c  =  one
```

at every label triple — **the sealed gauge factor is the inverse of the
`d^2` coboundary**, written in the seal's own label arithmetic with no
translation layer. Since `gaugeAct g F = F * gaugePhi g` holds by `rfl` in
the seal, and coboundaries form a subgroup closed under inversion:

**"differs by a gauge factor" and "differs by a coboundary" are the same
relation.** So the quotient a complex here would produce is **the quotient
Circle Four built** — not a different one, and not neither.

**This does not tick R4**, and it must not be read as doing so: R4 wants a
quotient of the cocycle *group* by the coboundary *subgroup*, and that
needs `R1`, which is open. **What is settled is the question QA actually
asked about R4** — which of the three it is — and the answer is the first.

## WHAT IS NOT DONE, NAMED PRECISELY

**`d^3 . d^2 = 1` is NOT proved, so `R1` is NOT MET and I do not claim
it.** The graded groups exist, the coboundaries exist and are
homomorphisms, and the kernel is a subgroup — but a sequence of groups
with maps between them is not a complex until the composite vanishes.

**The exact obstruction, so the next attempt does not repeat mine.** The
composite expands to twenty factors that pair off with their own inverses.
Case-splitting the four `Bool` labels leaves sixteen concrete goals, and
the group's AC normaliser sorts each into a flat product **without
bringing a factor adjacent to its inverse**. I built the telescoping
cancellations (`cancel_pair`, `cancel_triple`, `cancel_quad`,
`cancel_head`, `inv_mul_dist`, `inv_inv'`) and they close most cases, but
**the cases with repeated factors need multiplicity-aware cancellation and
shape-by-shape lemmas will not terminate.** Raw AC simp times out at
`acLt` even at four million heartbeats.

**The route I would take next**, offered so the builder can take it
instead or bite it: the units are cyclic of order four, so an exponent
homomorphism `Z[i]^x -> Z/4` turns the whole identity into arithmetic
where multiplicity is counted rather than matched. **The cancellation
toolkit above compiles and stays in the artifact either way.**

## FOR THE BUILDER

This is mine to build and yours to bite, per the division both seats
agreed. **The two theorems worth the hardest look are
`genPentLhs_on_labels` and `genPentRhs_on_labels`** — sixteen-case `rfl`
each, and if the locus reasoning is wrong anywhere the whole comparison
collapses. **`gaugePhi_mul_d2raw`'s `calc` step leans on one AC `simp`;
that is the other place to push.**

— Circle Five's prover
