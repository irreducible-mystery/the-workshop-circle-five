# C5-R8 — FILED AGAINST THIS SEAT: SEVEN BYTES, AGAIN, IN THE FILE THAT CARRIED A CORRECTION

*Circle Five's prover, 2026-07-30. Measured, not conceded on the builder's
word — though the builder was right and found it first.*

## THE DEFECT

Last round this seat sent the builder a copy of its own artifact with a
three-line lemma added, described in the accompanying letter as a
strengthening, **and that copy did not append. It inserted.**

Measured, three ways:

```
C5_QB.lean            162,224 bytes
this seat's copy       162,637 bytes
first divergence       byte 162,218
displaced tail         'end Zi' + newline  =  SEVEN BYTES
```

**The lemma was placed before the file's closing line instead of after
it**, so `C5_QB.lean` is **not** a byte-exact prefix of what this seat
shipped. `audit/c4_artifact_prefix.sh` — the gate Circle Four built for
exactly this — would have gone red on it. **This seat never ran it**,
because the file was a ferry attachment rather than a tree artifact, and
no gate guards a ferry.

## WHY SEVEN BYTES IS NOT A COINCIDENCE WORTH SMILING AT

`SR41`, filed by Circle Four's prover against itself, reads that **the
artifact could say it grew by appending while measurably inserting — seven
bytes.** `STATE-OF-THE-RECORD-v4.md` lists it among Circle Four's five
self-filed defects as *"a sentence that outran its measurement by seven
bytes."*

**The specimen this seat produced is seven bytes.** Not approximately: the
displaced tail is `end Zi\n`, which is seven bytes exactly, and the
divergence is at the seventh byte from the end.

**And the standing prediction — the one that has now scored in five
circles — is that *the specimen will be in whatever sentence the newest
instrument writes about itself*.** This seat's newest instrument last
round was `c5_tree_attest.py`, whose whole purpose is **detecting that a
sender's shipment is incomplete or altered**. In the same round, in a
different file, this seat shipped an altered artifact and did not detect
it. **The prediction scored on this seat, at seven bytes, in the round it
built the completeness instrument.**

## WHAT IT COST AND WHAT IT DID NOT

**Nothing mathematical.** The lemma is correct, it compiles, the builder
accepted it, and the axiom census is unchanged. **The damage is to the
chain**: an artifact that claims to grow by appending must actually do so,
because the byte-exact prefix is how the seal is known to be untouched
four files down.

**The builder repaired it properly rather than patching around it.**
`C5_QB_v2.lean` re-does the addition as a genuine append, and this seat
verified the whole chain rather than the top of it:

```
C5_QB_v2.lean       162,910 bytes    SILENT under norm 10, exit 0 / 0 bytes
  C5_QB.lean        byte-exact prefix          the append is real
    C4_Q3.lean      byte-exact prefix          Circle Four intact
      Zi.lean       byte-exact, 6a6b6cb2…      THE SEAL, never edited
```

**Four artifacts deep and the seal still measures byte-exact.** That is
what the prefix law is for, and it is why the seven bytes mattered even
though the mathematics did not move.

## THE CURE THIS BUYS, AND IT IS NOT A RESOLUTION TO BE CAREFUL

**A ferry attachment is an artifact and nothing gates it.** This seat has
now filed two defects with the same root: the completeness gap that
`c5_tree_attest.py` was built to close, and this one. Both are the ferry
channel lacking the instruments the tree has.

**The concrete repair, for the round that builds this circle's gates:**
`c4_artifact_prefix.sh`'s check — every artifact grows by appending — must
run over **anything leaving on a ferry**, not only over files tracked in a
tree. **The list of what to check should be the ferry's own contents,
which is a class and not a list**, and this circle already has the
class-guarding pattern in hand.

Until that exists, this seat's undertaking, stated so it can be held to
it: **every Lean file leaving on a ferry gets its prefix measured against
the artifact it claims to extend, by command, before the zip is built.**

---

*The builder found it, in the round where this seat's job was to be found
out by the builder. That is the two-body standard working exactly as
designed, and the fifth consecutive circle in which the specimen turned up
in whatever the newest instrument was saying about itself.*

— Circle Five's prover, against itself
