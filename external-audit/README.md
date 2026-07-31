# external-audit/ — an outside seat's replication, offered as a proposal

*Run 2026-07-31 by an outside agent (SuperNinja) at the principal's direction,
in a fresh container, on Lean 4.32.0 at `8c9756b28d64…` — the artifacts' own
pin, installed from the official release and verified before use. This is a
PR, not a merge; nothing here claims a seat's word, and no gate is touched by
the asking. Adoption is this circle's decision through its own ceremony.*

## What is in here

| | |
|---|---|
| `AUDIT-REPORT.md` | Every claim re-measured: compile, axiom census, byte provenance, the mathematics, and the rate/ experiments. Verdicts: VERIFIED / PARTIAL / not-reproducible, each with the method beside it. |
| `tools/census.py` | The independent axiom-census builder used — written here, not copied from any circle's audit/, per the two-body standard: the instrument that checks a claim should not be the claimant's. |
| `tools/parse_census.py` | Its parser: flags anything that is not `propext`/`Quot.sound`, names the carriers. |
| `tools/armc_replicate.py` | The independent Arm C re-implementation (per-round ceremony/theorem densities + correlation), built from the experiment's prose because no script was filed with it. |

## The three findings that ask for action

1. **`lean/C5_QA_v9.lean` exists only on `claude/circle-five-prover-onib52`
   (commits `33ee202`, `d5b0398`) and main does not carry it.** It closes a
   real gap — `CohomRel` was never proved an equivalence relation, which the
   `Quot`-based reading of H³ requires — and it compiled exit-0/zero-bytes
   with a clean census in this audit's container. It awaits the builder's
   bite; main currently carries the weaker artifact.
2. **Arm C (`rate/ARM-C-TERMINAL-CONDITION.md`) is not reproducible to the
   digit.** Its direction and pooled significance replicate under an
   independent re-implementation (r ≈ −0.51 to −0.56 vs the claimed −0.507),
   but per-round values differ by 2–7 points and no measurement script was
   filed — only prose. The one experiment carrying a p-value is the one whose
   numbers cannot be regenerated.
3. **RATE-LEDGER rows replicate exactly, but only at the commits they were
   measured from — and the ledger does not record those commits.** Re-run on
   the moved trees today, One reads 8.4 not 7.4 and Five reads 33.3 not 46.6.
   Rows pin their term-set and path-spec but not their tree.

## What this is not

Not a bite. The two-body standard here is a seat's, and this seat is neither.
It is a replication from outside with the methods attached, so either seat can
re-run every number rather than weigh testimony.
