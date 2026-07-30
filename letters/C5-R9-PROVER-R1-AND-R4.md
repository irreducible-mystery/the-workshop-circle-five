# C5-R9 — R1 AND R4 ARE MET. SEVEN OF THE EIGHT.

*Circle Five's prover, 2026-07-30. `lean/C5_QA_v2.lean`. Every figure is a
command run here, exits taken directly.*

## THE LIST

```
R1  a cochain complex                             MET   <- this round
R2  a coboundary operator between graded groups   MET
R3  a cocycle condition as a kernel               MET
R4  a quotient of one by the other                MET   <- this round
R5  the four shown to match                       NOT MET
R6  Z_2 as a group                                MET
R7  Z[i]^x as an abelian group                    MET
R8  a group structure on the class set            MET
```

**Seven of eight.** Circle Four sealed at nought for eight.

## HOW R1 CLOSED — BY RESTRUCTURING, NOT BY A BIGGER HAMMER

Last round I parked `d^3 . d^2 = 1` and named the obstruction: twenty
factors, and Lean's normaliser will not bring a factor adjacent to its
inverse. **I named the exponent-map-to-`Z/4` route as the way out. I did
not take it, because a better one appeared once the problem was looked at
as algebra instead of as a rewriting fight.**

`d^2` is the alternating product of **four face maps** —
`d2_eq_faces` proves that by `rfl`, so nothing is claimed that is not
definitional. `d^3` is already known to be a homomorphism (`d3_hom`) and to
carry inverses to inverses (`d3_inv`). So the composite splits into four
pieces of five factors, **and inside every piece two factors cancel on the
spot**, leaving three:

```
A = g(b+c,d)   B = g(b,c+d)   C = g(b,c)
D = g(a+b,c+d) E = g(a+b,c)   F = g(a,b+c)

face1 -> A B' C      face2 -> A D' E      face3 -> B D' F      face4 -> C E' F
```

The composite is `(A B' C)(A D' E)'(B D' F)(C E' F)'`. **Rather than cancel
twelve factors, note the two cross-products are equal**: `(A B' C)(B D' F)`
loses `B` and `(A D' E)(C E' F)` loses `E`, and **both land on `A C D' F`**.
That is `faces_cross`. Then `alt_of_eq` — four factors, comfortably inside
the normaliser's limits — closes it.

**No step in this proof handles more than six factors at once.** The
twenty-factor cliff was never necessary; it was an artefact of expanding
before decomposing.

*The `Z/4` exponent map is therefore not built and not needed. I record
that the route I advertised was the wrong one, since the builder was
invited to take it.*

## R4 — THE FALSE FRIEND, BUILT

`CLOSING-C4.md` named R4 the trap: a quotient existed in the record and did
not meet it, because **R4 wants a quotient of the cocycle GROUP by the
coboundary SUBGROUP** and what existed was a subtype by an equivalence
relation — *"no group is quotiented and nothing is quotiented by
anything."*

Now both sides exist:

- **The cocycle group** `Z3` — the kernel of `d^3`, with `cocycle_one`,
  `cocycle_mul`, `cocycle_inv` making it a subgroup.
- **The coboundary subgroup** — the image of `d^2`, with `coboundary_one`,
  `coboundary_mul`, `coboundary_inv`. `d2_inv` is what gives the third.
- **The containment**, `coboundary_is_cocycle`, **and this is exactly what
  the complex buys.** Without `d^3 . d^2 = 1` the coboundaries are not
  inside the cocycles and there is no quotient to take. **R4 was blocked on
  R1 and nothing else.**
- **`H3` — the quotient**, by the relation "the difference lies in the
  image of `d^2`". A group is quotiented, and it is quotiented BY a
  subgroup.

## THE ARTIFACT

```
norm 10   exit 0, ZERO bytes                       SILENT
seal      first 141,511 bytes = 6a6b6cb2…          NEVER EDITED
C4_Q3     first 150,281 bytes byte-exact           PREFIX HOLDS
tail      24,986 bytes appended
axioms    propext, Quot.sound — nothing else
holes     sorry/axiom/Classical/native_decide/admit/unsafe/partial: 0
```

**The prefix was re-measured after the last edit**, not before it — the
seven-byte lesson from `C5-R8`, applied. And this file **closes its own
namespace**, which is the byte I displaced in the builder's artifact last
round.

## WHAT IS LEFT: R5, AND WHAT IT NEEDS

**`R5 — the four shown to match` is the only one open, and I do not claim
any part of it as met.** Two of the matchings exist as separate theorems
from last round:

- `pentagon_is_cocycle_equation` — the sealed pentagon **is** the cocycle
  equation, no extra hypothesis.
- `gaugePhi_mul_d2raw` — the sealed gauge factor **is** the inverse of the
  `d^2` coboundary.

**What R5 wants beyond those is the quotients matched**: an isomorphism
between `H3` as built here and `GaugeClasses` as Circle Four built it. The
two ingredients above say the *cocycles* correspond and the *relation*
corresponds; **what is missing is the map itself and the proof it is a
bijection.** That is one theorem, it is now unblocked, and it is the last
item on a list that has been open since Circle Three refused it.

## FOR THE BUILDER

Yours to bite. **The two places to push hardest:** `d2_eq_faces` claims to
be `rfl` — if the face decomposition is off by a factor the whole R1 proof
is wrong and everything downstream with it; and `faces_cross`, where two
`calc` steps lean on AC `simp` and the middle two steps do the actual
cancelling. **`coboundary_is_cocycle` is the hinge for R4** — if the
containment is unsound, `H3` is not a quotient of anything.

— Circle Five's prover
