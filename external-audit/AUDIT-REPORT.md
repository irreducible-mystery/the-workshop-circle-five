# Independent Audit — Circle Five, its mathematics, and the rate/ experiments

*Run 2026-07-31 in a fresh sandbox. Nothing below was accepted from the record's
own prose; every number was re-measured here. Where I could not re-measure, I
say so. Method followed the instruction given: verify my own capabilities with
small cheap trials before any full run, and audit the experimenters' supplied
results by re-running rather than reading.*

---

## 0. Capability check, done before anything expensive

- Sandbox: 3.8 GiB RAM, 2 CPUs, ~3.6 GiB free disk. Tight; the elan toolchain
  manager was skipped in favour of the official release tarball (534 MB).
- Installed **Lean 4.32.0 from the leanprover/lean4 GitHub release**.
  `lean --version` reports commit `8c9756b28d64dab099da31a4c09229a9e6a2ef35` —
  **byte-for-byte the pin the artifacts claim.**
- Trial 1: a one-line theorem — exit 0, 0.5 s.
- Trial 2: the smallest artifact, `C5_QB.lean` — exit 0, **zero bytes of
  output**, 18 s. Only after that did the full runs proceed.

## (a) The Lean claims — VERIFIED, independently, in this container

**Compilation (norm 10: exit 0, zero bytes):**

| file | claimed | measured here |
|---|---|---|
| `C5_QA_v8.lean` (247,545 B) | exit 0, silent | **exit 0, 0 bytes, 23 s** |
| `C5_QB_v2.lean` (162,910 B) | exit 0, silent | **exit 0, 0 bytes, 18 s** |
| `C5_QA_v9.lean` (branch, 253,927 B) | exit 0, silent | **exit 0, 0 bytes, 21 s** |

**Axiom census — my own script, not theirs** (comment-stripping tokenizer +
`#print axioms` on every theorem, then a parser that flags anything that is not
`propext`/`Quot.sound`):

- `C5_QA_v8`: 403 theorems found, 393 census lines parsed clean + 10 primed
  names (`mul_assoc'` etc.) hand-checked — **105 axiom-free, 108 propext-only,
  3 Quot.sound-only, 177 both. Nothing else. `sorryAx` = 0,
  `Classical.choice` = 0.**
- `C5_QB_v2`: 299 theorems — 92 / 105 / 2 / 100, same pattern, zero violations.
- `symbolOf_mul` depends on **propext alone** — exactly as claimed in R13.
- v9: same profile; the two new theorems `cohomRel_symm` and `cohomRel_trans`
  are present and clean.

**Hole scan (my own, whole file, wide token list):** the only real hit is the
disclosed `set_option maxHeartbeats 1000000` at QA line 3573 — an elaboration
budget, not a kernel weakening. Their disclosure was accurate.

**Byte-level provenance — every R13 claim reproduced exactly:**

- v7 = 236,062 bytes, sha256 `1edbe7e6…` ✔
- QB_v2 tail after byte 150,281 = 12,629 bytes, sha `3e93db0c…`, found in v7
  **at offset 221,197** ✔ (their stated offset is exact)
- The full seven-link prefix chain (141,511 / 150,281 / 167,235 / 177,245 /
  185,143 / 197,490 / 218,648) reproduces every stated hash prefix ✔
- v7 is a byte-exact prefix of v8; v8 of v9 ✔
- **Cross-repository check they could only assert:** the innermost 141,511
  bytes are byte-identical to circle-two's sealed `lean/Zi.lean`
  (`6a6b6cb2…`), and the 150,281-byte prefix is byte-identical to
  circle-four's `C4_Q3.lean`. The seal really is carried, unmodified, at the
  bottom of every Circle Five artifact.

**Negative control I planted myself** (because a checker nobody has tried to
fool is a belief, their words): flipped `e = clsOne` to `e ≠ clsOne` in the
final QB theorem → **exit 1 with a type mismatch**. The silence of the real
files is earned.

**One finding of my own, in Circle Five's favour but past main:** the branch
`claude/circle-five-prover-onib52` carries `C5_QA_v9.lean` plus letter R14.
**Exact location, so nobody has to hunt for it:** commits `33ee202` ("A gap of
this seat's, found by being asked: CohomRel was never proved an equivalence
relation", 2026-07-31 13:45 UTC, adds `lean/C5_QA_v9.lean`, 253,927 bytes,
git blob `e6250c16…`) and `d5b0398` ("R14 — the gap, the retirement, and a
live neighbour, for the builder", 13:50 UTC). Both sit on the branch *after*
`85b562c`, the merge that created main's current tip — so main carries v8 and
knows nothing of v9. The gap it closes is genuine and the prover found it
post-capstone — `H3 := Quot CohomRel`
quotients by the *equivalence closure*, so the R4 docstring ("quotient of the
cocycle group by the coboundary subgroup") is exact only if `CohomRel` is
already an equivalence; only reflexivity had been proved. v9 adds symmetry and
transitivity. **This repair is not on `main` and is unbitten by the builder.**
If you want main to carry the strongest artifact, that merge is pending
ceremony.

## (b) The mathematics itself — SOUND, and the charge is honestly answered

I read the load-bearing definitions rather than the headers (the headers have a
convicted history of overclaiming — the v8 append itself documents one:
"R1 the COMPLEX" was claimed built in a banner when `d3_d2` did not yet exist).

- **QA/R1–R3 are real constructions, not shells.** `Coch2/3/4` are function
  spaces over `Bool` (the index group Z₂) into `Un` (the unit subtype of the
  hand-rolled Gaussian integers); `coch*Group` prove the abelian group laws
  pointwise; `d2`/`d3` are the standard inhomogeneous coboundaries for the
  trivial action; `d3_d2 : d3 (d2 g) = c4e` closes the complex;
  `IsCocycle3 f := d3 f = c4e` is literally a kernel condition.
- **The QA identification is settled by computation, not resemblance.**
  `pentagon_is_cocycle_equation` proves the sealed pentagon LHS/RHS *equal*
  the cocycle equation's two sides on the index group by 16-way case analysis
  (`cases … <;> rfl`), with the admissible-locus guard shown vacuous there —
  no extra hypotheses smuggled in, which is exactly what the charge asked to
  be checked.
- **R4's distinction is answered the strong way.** `gaugePhi_mul_d2raw`
  proves the sealed gauge factor is the *inverse of a coboundary*; the
  coboundaries are proved a subgroup (`coboundary_one/mul/inv`); therefore
  "differs by a gauge" = "differs by a coboundary" and the quotient is the
  quotient Circle Four built — not a different one, not neither.
- **QB is answered with both clauses.** `gaugeClassesGroupLaw` constructs the
  law; `group_law_unique` proves *canonicity* in a strong form (any operation
  with the vacuum as two-sided identity and right inverses agrees with
  `classMul` everywhere — associativity not even assumed), and the prover's
  appended bite closes the last degree of freedom (any two-sided identity IS
  the vacuum class).
- **The capstone `three_groups_one_group`** bundles H³ ≅ Z₂ ≅ sealed classes
  as groups with the triangle commuting, and after the v8 append all three
  legs are stated against a single structure (`AbGroup`), with the
  `AbGroup`↔`CommGroupLaw` round-trips proved by `rfl` — the R13 defect
  (two unjoined notions of "group") is genuinely repaired, not papered over.
- The axiom footprint (`propext` + `Quot.sound` only, no `Classical.choice`,
  no `decide`-hidden natives beyond kernel evaluation) means every one of
  these is kernel-checked constructive-with-quotients content.

Verdict: **QA and QB are answered affirmatively and the artifacts support the
answers.** The one open item is procedural, not mathematical: v9's equivalence-
relation repair sits on a branch awaiting the builder's bite.

## (c) The rate/ experiments — MIXED: ledger exact, Arm C only partially reproducible

The experimenters' own repo (`workshop2`) was cloned; it holds the
predictions, experiments, and claims ledger that `rate/` in the circle repos
only points to.

**RATE-LEDGER rows — REPLICATED EXACTLY.** Running their `rate.py`
(sha `4dd680a5…`, matching all four proposed copies) at the historical commits
each row was measured from reproduces every figure to the digit:

| circle | claimed | measured here | at commit |
|---|---|---|---|
| One | 1150 / 148613 / 7.4 / 62 / 70 | identical | `e0b09a5` |
| Two+Three | 269 / 226503 / 36.8 / 134 / 135 | identical | `31a7cab` |
| Four | 299 / 45755 / 46.4 / 5 / 35 | identical | `7709f58` |
| Five | 0 / 21070 / 46.6 / 0 / 14 | identical | founding `6f7d8d5` |

A caveat the ledger itself should carry: **rows are commit-relative and the
ledger does not record the commit.** Re-run today on the moved trees, One reads
8.4 not 7.4 and Five reads 33.3 not 46.6. Each row records its term-set and
path-spec but not the tree it measured; pinning the commit per row would close
that.

**Arm C — DIRECTION AND SIGNIFICANCE REPLICATE; THE PER-ROUND NUMBERS DO NOT,
AND CANNOT BE CHECKED.** I rebuilt the per-round measurement from the stated
method ("`theorem` occurrences per 1,000 words in a round's own letters",
ceremony per TERMS v1) with my own script, both with the full term set and
with `charge`/`norm` stripped (the control's stated correction):

- My pooled result: n=21, **r = −0.51 to −0.56, t = −2.6 to −3.0** depending
  on term-set variant, kernel-round mean ≈ 33–36 vs no-theorem mean ≈ 43–48.
  Their claim: r = −0.507, t = −2.56, p ≈ 0.019, means 34.9 / 48.4.
  **The finding survives an independent re-implementation.**
- But individual rounds differ by 2–7 ceremony points (e.g. their C3-R1 54.3
  vs my 49.6; their C4-R0 62.5 vs my 55.4), and a few theorem densities
  disagree (their C3-R4 2.0 vs my 1.3). **No measurement script was shipped
  with Arm C** — only prose describing one — so the exact file set, term
  stripping, and word tokenizer are unrecoverable. The experiment is honest
  about its statistics but is **not reproducible to the digit from what was
  filed.** That is precisely the class of defect ("reading a value through a
  layer that transforms it") this record convicts elsewhere.
- **P9 pre-registration: the commit order holds** (`96a2b5c` registers P9 at
  12:11:27; `f9784c5` lands results at 12:14:49) — but the gap is **three and
  a half minutes**, same agent, same session. It is sequencing, not blinding.
  Their own disclosure that the Circle Three arm was "informed, not blind" is
  accurate and, if anything, understated: with a 3.5-minute window the C4
  "blind" arm rests entirely on the claim that per-round numbers were not yet
  computed, which cannot be verified from the outside. The honest score
  remains what they wrote: direction replicated out of sample, significance
  did not (C4 alone: their t = −1.33; mine −1.7 to −1.93).
- The claimed counter-example (C4-R6 high on both) and the time-confound
  caveat both reproduce in my numbers. The self-criticism sections are
  accurate.

**Arm A/B control:** Arm B's C3 column matches the Arm C table (same
measurement, internally consistent). Arm A's snapshot ratios (25 → 5.18) come
from `history/floor-snapshots/`, which exists, but the "bench" counting method
is again script-less prose; unverified beyond existence of the inputs.

## Summary table

| claim | verdict |
|---|---|
| Lean 4.32.0 @ 8c9756b2, exit 0 / zero bytes on QA_v8, QB_v2, v9 | **VERIFIED here** |
| Axiom census: propext + Quot.sound only; symbolOf_mul propext-alone | **VERIFIED (my own census)** |
| Prefix chain, merge offset 221,197, all R12/R13 byte claims | **VERIFIED to the byte** |
| Seal carried byte-exact from circle-two through circle-four into every C5 artifact | **VERIFIED (cross-repo)** |
| QA answered: pentagon = cocycle condition, no hidden hypotheses; quotient = Circle Four's | **VERIFIED (read + compiled)** |
| QB answered: group law constructed, canonical | **VERIFIED (read + compiled + my negative control)** |
| R13 two-groups defect repaired in v8 | **VERIFIED** |
| CohomRel equivalence gap + v9 repair | **VERIFIED, but on a branch, unbitten, not on main** |
| RATE-LEDGER four rows | **REPLICATED EXACTLY at historical commits; commit-pinning missing** |
| Arm C direction + pooled significance | **REPLICATED with my own implementation** |
| Arm C per-round numbers | **NOT reproducible to the digit — no script filed** |
| P9 "registered before measuring" | **Commit order verified; 3.5-minute window — weak as blinding** |

## What I would file back at the circle

1. **Merge and bite v9.** The equivalence-relation gap is real, the repair is
   real, and main currently carries the weaker artifact.
2. **Arm C should ship its script.** The one experiment in `rate/` whose
   numbers cannot be regenerated is the one that carries a p-value.
3. **Pin ledger rows to commits.** A row that silently drifts when the tree
   grows is a state measurement wearing a rate instrument's name — their own
   self-test's sixth blind spot, live in their own ledger.
