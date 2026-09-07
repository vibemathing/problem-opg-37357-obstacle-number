# Octahedral h=2 resume checkpoint, PR34

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Issue: #3
Branch: web/attempt-opg37357-a01-c28-octahedral-h2-v1
Original reviewed source head: a4ac73869b14b442905f3a83d526007fc5f98b2a
Synchronization base: 61943c788f95f91874b99b77f06b4b8c898a6db7
Packet: research/artifacts/web-inbox/opg37357-a01-c28-octahedral.packet.json

## Fresh result

PR32 and diamond successor PR35 were already merged. Their files are unchanged.
PR33 has different ring/ternary source and is not overwritten or represented by
PR34. Generic C28 packet/request names and candidate IDs are disambiguated here.
All nine original octahedral mathematical blobs are preserved exactly. The old
checkpoint and request survive at octahedral-prefixed paths; their older base
and pending-check text are historical, not current transportation claims.

Both checkers were actually rerun from byte-matched source. CPython 3.13.5;
30 CPU seconds, 40 wall seconds, 512 MiB and 4 MiB output cap. Exit 0;
elapsed 3.679828 seconds; stdout 167132 bytes, SHA-256
c1253fab8831d4926d41b4bcdc62df6b8afcaf530436c340f162a04d8fb5cbd6.
The appended resume execution record (not a trusted receipt) has SHA-256 89058cf32a5017393d0cd4da604bb95b9189baf4044361a31ec4859258e29c4f.

Counts: 1140 clauses, 32 variables, all 84 simple paths; 2^20 directions;
8 labels and all 64 side choices accounted for; 15952 projected models,
807232 full models. Sixteen mutations rejected. All eight connector masks
SAT. The least model has x all false, z pairs (false,true), q all false;
it is realized by the existing integer placement and sixteen-corner polygon.
192 graph-edge/polygon-side and 104 nonadjacent polygon-side checks pass.
No false ternary cut can remove this genuine common-component model.

The precise failed-route proposal excludes only the eight specified graphs.
The next implication is: if EVERY placement of some planar G has five target
nonedges with no common component for any triple, two labels are impossible.
This geometric forcing hypothesis is NOT proved. The triple-only abstract
threshold is five; C18's one triple retains six two-label assignments.
T (tube/Jordan), A (fixed incidence), and P (real placement and all graph orders)
remain separate. No trusted closure, EvidenceLink, Result or Solution.

## Delivery instructions

The branch is synchronized by a history-preserving merge, no force. The diff
must contain only the nine preserved candidates, one newly namespaced packet,
the preserved request and initial checkpoint, this checkpoint, and the new
resume execution JSON. Inspect all three checks at the FINAL head, compare
against current main, review the full allowed diff, then protected squash merge.
Record final head/check IDs/merge/main in Issue #3 after a fresh read. No second
packet is added to this PR. This file does not anticipate a merge result.

best_verified_candidate: none
best_verified_result: none
best_h2_candidate: complete octahedral SAT with a genuinely realized minimum
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: placement-universal higher-rank incidence forcing, not repeating this SAT family
