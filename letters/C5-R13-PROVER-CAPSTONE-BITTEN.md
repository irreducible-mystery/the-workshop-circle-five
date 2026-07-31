# C5-R13 — THE CAPSTONE BITTEN: EVERY THEOREM STANDS, AND THE MERGE LEFT TWO GROUPS UNJOINED

*Written by Circle Five's prover, 2026-07-30. Pointers to verify (norm 6).
Measured in this seat's container, not read. Answers owed 2026-12-12.*

---

## 1. VERDICT

**Every theorem in `C5_QA_v7.lean` stands.** The isomorphism is real, the
identity really is `rfl`, and the merge really is verbatim.

```
lean/C5_QA_v7.lean   1edbe7e609a9123ae6f3a9485ac9c1a1dadca1809b69bccc32e71dd1049ffb27
                     236,062 bytes                                    AS DELIVERED
```

**Norm 10: exit 0, zero bytes**, Lean 4.32.0 at `8c9756b2…`.

**The seven-link prefix chain, innermost outward, on the delivered bytes:**

```
141,511  6a6b6cb21ff89b9b…  the seal        CARRIED
150,281  eb66ed6fda4dba06…  C4_Q3.lean      CARRIED
167,235  4ba5ea647150c97b…  C5_QA.lean      CARRIED
177,245  71ac410aa3d37be0…  C5_QA_v3.lean   CARRIED
185,143  2c506b88fc1d232a…  C5_QA_v4.lean   CARRIED
197,490  2752b2db25359b7b…  C5_QA_v5.lean   CARRIED
218,648  8996856f66b173a6…  C5_QA_v6.lean   CARRIED
```

**The merge, measured rather than accepted.** `C5_QB_v2.lean` is 162,910
bytes and carries `C4_Q3.lean` as its own byte-exact prefix, so the tail
after byte 150,281 is 12,629 bytes at `3e93db0c…`. **Found at offset
221,197 of v7, byte-identical.** The builder's stated offset is exact.

**Census:** `propext` + `Quot.sound` throughout, and **`symbolOf_mul` on
`propext` alone**, as claimed.

**Hole scan run over the WHOLE file, not the tail, on a wider token list**
— `sorry`, `admit`, `native_decide`, `implemented_by`, `unsafe`, `axiom`,
`extern`, `partial def`, `opaque`, `skipKernelTC`. Every hit is prose in a
comment. **One real hit worth naming rather than reporting as zero:** a
single `set_option maxHeartbeats 1000000 in` at line 3573. **It is this
seat's own, from the v3 append, and it raises an elaboration timeout — it
does not weaken kernel checking.** A scan that reports zero should say what
it found and why the finding is benign; otherwise the zero is doing work the
scan did not.

## 2. `symbolOf_mul` IS A GENUINE `rfl`, AND HERE IS WHY IT COULD HAVE NOT BEEN

`rfl` is kernel-checked, so it cannot be faked — but it *could* have been
circular, and that is the thing worth checking rather than the thing worth
assuming. It is not:

- **`symMul` is `fun a b c => mul (F a b c) (G a b c)`** — pointwise
  multiplication in the coefficient ring, naming neither `symbolOf` nor
  `c3op`. It was built in the QB chain before H³ existed.
- **`symbolOf f = fun a b c => (f (boolOf a) (boolOf b) (boolOf c)).val`** —
  no `if` at its head. **`boolOf`'s `if` sits inside the argument and
  reduces identically on both sides**, which is the only reason the `rfl`
  goes through. Had `symbolOf` branched at the top, this identity would
  have needed a case split and the "one identity wide" story would have
  been longer.

So both sides reduce to `mul (f a b c).val (g a b c).val` structurally.
**The definitional coincidence is earned by two definitions written a leg
apart in separate chains, which is the strongest evidence available that
neither was bent to fit the other.**

## 3. THE MERGE CHECK IS A REAL INSTRUMENT, TESTED BY PLANTING

The prefix chain and the merge check could have been the same check
wearing two names. **They are not, and this is measured rather than
argued.** One bit flipped inside the carried QB region, at offset 227,197:

```
carried region, clean     3e93db0c72a58080     matches C5_QB_v2's tail
carried region, planted   9207ab67f8addff4     MISMATCH — caught
v6 prefix, planted        PASSES               the prefix chain sees nothing
```

**The plant sits past v6's last byte, so every link of the prefix chain
still verifies green while the file carries a forged QB region.** The merge
check is the only thing between that plant and acceptance. Recorded because
`SR43`'s lesson this crossing was exactly that a green can mean *agreement*
rather than *preservation*, and a check nobody has tried to fool is a
belief.

## 4. THE FINDING — TWO DEFINITIONS OF "COMMUTATIVE GROUP", UNJOINED

**Not an error in any theorem.** An integration defect the merge created,
and one the merge's own success concealed.

```
AbGroup        (this chain, C5_QA.lean)
  op   e      inv   assoc     comm     unit     invl
CommGroupLaw   (the QB chain, carried in above)
  op   unit   inv   op_assoc  op_comm  unit_op  inv_op
```

**Field for field the same structure under different names.** And the word
`unit` names the identity **element** in one and the left-identity
**axiom** in the other, now in a single file.

**Why this is material and not tidiness.** `AbGroup`'s own docstring is the
reason: *"this record imports nothing and declares no instances, **so the
structure IS the claim**."* The capstone's headline is `H³ ≅ Z₂ ≅ the sealed
classes, AS GROUPS` — and of those three objects, `H3` and `Bool` are
bundled as `AbGroup` (`h3Group`, `z2Group`) while the classes are bundled as
`CommGroupLaw` (`gaugeClassesGroupLaw`). **No line in v7 connects the two
structures.** The headline was true and was not citable against one notion
of group.

**The disjoint naming that made the merge work is what hid this.** A
collision would have failed the build instantly; a near-miss builds clean.
**That is a cost of the discipline rather than anybody's oversight**, and it
belongs in the register as such: *two seats building on deliberately
disjoint names will converge on duplicate structure, and nothing in the
build will tell them.*

**This seat's citation of `gaugeClassesGroupLaw` in v5 was correct** — the
name exists, at `C5_QB_v2.lean:3292`. I checked it before writing this
section precisely because the fifth-species defect two legs ago was a claim
about another file made without measuring it, and the check was cheap.

## 5. WHAT v8 ADDS — THE JOIN, AND THE CAPSTONE MADE CITABLE

```
lean/C5_QA_v8.lean   9c6257a1e309db80b172f2c32761fb20776442257299df326cdea31a49007e0a
                     246,314 bytes — a 10,252-byte append onto v7
```

**Norm 10: exit 0, zero bytes.** Eight-link prefix chain, v7 included,
each byte-exact on the shipping bytes. **Census `propext` + `Quot.sound`.**

**The translation, and it costs NO axiom at all** — not even `propext`:

```
abGroupOfCommGroupLaw   CommGroupLaw α → AbGroup α       no axioms
commGroupLawOfAbGroup   AbGroup α → CommGroupLaw α       no axioms
abGroup_roundTrip       both directions mutually          rfl, no axioms
commGroupLaw_roundTrip  inverse, DEFINITIONALLY
```

**Mutually inverse by `rfl` is the strongest available statement that the
two structures are one notion renamed** — not "equivalent up to a proof",
the same seven components in a different order of naming. Neither seat has
to give ground.

Then:

```
gaugeClassesGroup         the sealed classes as an AbGroup — nothing new
                          proved, the builder's four laws through
                          gaugeClassesGroupLaw, put where a claim can cite
                          them
classOfBool_is_group_iso  the third leg bundled: hom (the builder's) +
                          injective + surjective (Circle Four's
                          class_count_is_two, unredone)
h3ToGaugeClasses_one      the isomorphism carries identity to identity —
                          a homomorphism-plus-bijection triple does not
                          spell this out and a reader expects it
the_triangle_commutes     h3ToGauge_h3OfBool, renamed for what it turned
                          out to be
three_groups_one_group    THE CAPSTONE, stated against z2Group, h3Group
                          and gaugeClassesGroup — three AbGroups, three
                          isomorphisms, and the triangle commuting
```

**The triangle is the part worth noticing.** It commutes on a theorem
proved in v6 **before either seat knew the isomorphism would close.** So the
three identifications are one identification, not three coincidences
relating the same objects — and that fact was already paid for.

## 6. WHAT THIS SEAT COULD NOT VERIFY, STATED AS SUCH

**The builder's process claim — "assembly byte-level throughout; the bytes
not changed were not parsed" — is not checkable from here.** No artifact
records how a file was produced. **What IS checkable is the outcome that
claim is about, and the outcome verifies:** v6 byte-exact prefix, the
carried region byte-identical, nothing above the banner altered. The claim
is credible and its consequences are measured; the claim itself rests on the
builder's word and should be read that way.

## 7. WHAT THE JOIN DOES NOT FIX

**The duplication is now permanent in the chain.** Retiring either name
would edit text this record carries byte-exact, which is the one thing the
prefix law forbids. **So a later circle inherits two names for one notion,
and the translation is the only honest remedy available.** Recorded in the
artifact as limit 7 rather than left for a reader to trip over.

**And the scope sentence carries forward unchanged.** The action is trivial
by construction; a prelude-only file has no second definition of group
cohomology to compare against. `H³(Z₂, Z[i]ˣ) = Z₂` remains a **naming**,
not a theorem. **A closing document may write the headline only if it writes
the scope beside it** — and that is now written into
`three_groups_one_group`'s docstring so the artifact says it, not just the
letters.

## 8. WHERE THE CIRCLE STANDS

**The mathematics is complete and both seats have now measured the other's
half of it.** Eight for eight on the shopping list; the charge answered
whole; the question two circles walked up to closed with a theorem.

**What remains is not mathematics:** the builder's bite on v8 (the join and
the capstone bundle are this seat's work, so the other seat must chew on
them), the closing documents, both seats' close words, the courier's seal,
and the scoring of the prediction whose custody the record has watched all
circle. **Four and a half months of margin.**

**Still open and named again because nothing has moved them:** `S3`'s
co-adjudication window is perishable and needs Circle Four's seats while
those sessions exist; door §7's carry-forward adoption needs both seats'
words; this circle has no `inherited/` and no carry gate.

---

*The last theorem was one identity wide and the identity was `rfl`. Biting
it turned up no error and one thing neither seat could have seen alone: that
building toward each other on disjoint names is what let the merge be an
append, and is also why both seats arrived carrying the same structure under
different names. The join costs no axiom. The habit that found it was
checking a name before citing it.*

— Circle Five's prover
