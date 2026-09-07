# C19 fixed-placement audit checkpoint

verdict: candidate_only
scope: C17 fixed-placement special-case bound only
mathematical_deliverable: reviewable_four_lemma_proof
best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
unrestricted_one_obstacle_completeness: open
registered_failed_routes: empty at base; no protected ledger changes

## Bindings and observed transport

Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Issue: #3
PR: #24
Branch: web/attempt-opg37357-a01-c19-fixed-placement-audit-v1
Base: 05e200eb918ff174a3f35c66769cbaf19a22750e
Harness: 1.2.4
Harness snapshot SHA-256: 4181effe1481eb1454130d2d6c87a7c327ef84e39b28d051fc496870d08864d1
Proof commit: 1f35cb9fe73a97a037efc10c98a751e157fde745
Rational companion commit: 7189ba00e73da4accf315b6110632a4185a25fb3
Packet creation commit: 7870323eaaf1cf17cf20c5ff12e5020f95b8d58c
Actual PR binding commit: 3c87c71f9af0cf5ff489f8b470647222175b3957

This file is written before final-head checks and merge. Its own commit will
be part of the head that must pass the three required checks. Definitive
check-run IDs, merge SHA and post-merge file reads belong to Issue #3.
The PR fields have actually been backfilled to #24, not merely planned.

## Frozen artifact bytes

- research/artifacts/candidates/opg37357-a01-c19-fixed-placement-proof-v1.md
  SHA-256 7167f0f258ad4a990ef9f5ba2763bb815dffecde59bbc561152aeb75874e8796
  Git blob 00940f1bd417f0bef607bd39b5b5407b40c1a218; 30405 bytes.
- research/artifacts/candidates/opg37357-a01-c19-rational-joint-audit-v1.md
  SHA-256 b442480658e6fcd15dc089e34c14e9fc5b8be2d6097453cc345868db7edee437
  Git blob 1bbfdbaa1a90e332a4f4ce236c60e7e0ea375b4e; 3530 bytes.
- research/artifacts/web-inbox/opg37357-a01-c19.packet.json
  SHA-256 3d8dea4f6da1c97805a604b9306a22669798182dc1014bb04799edfd0a42643c
  Git blob 7138cc52a539c38583a08ead8ab6ad1b061efc86; 6648 bytes.

## Mathematical audit conclusions

The four lemmas reconstruct the conditional bound without moving any graph
point: common open free component and segment-interior witnesses; connected
eligible punctured-cell graph; pruned embedded spoke/portal tree; and an
arbitrarily thin disk neighborhood with at most 2E+L corners for N>=2.
The final count is max(3,2e^2-e+3*C(n,2)); k=0/1 use separate triangles.

The proof makes the local radial-joint and global boundary-splicing steps
explicit. Straight port continuations contribute no corners. Opposite rays,
reflex sectors, arbitrarily small angular gaps and the one-vertex exception
are not omitted. Ten adversarial cases reject stronger shortcuts rather than
provide a counterexample to the stated theorem. The companion checks the
six-corner rational fixture by all nine nonadjacent side-pair tests and by
boundary avoidance of both entire tree segments, without assuming the tree
lemma itself. These are exact displayed algebraic arguments, not test outputs.

C03's idea is reconstructed. C04/C07/C16 were read but graph-moving GP or
normalization arguments are not premises. C18 only supplies the incompatible
common-component diagnostic; no fixed drawing is promoted to a graph-level
obstacle lower bound. C17 and all prior candidates remain unchanged.

No geometry program, solver, grid search or proof assistant ran. Python
3.13.5 was used only for document/byte bookkeeping. The proof is in the
candidate-generation trust domain, not a separately admitted verifier domain.

## Next action and stop scope

Complete the current PR's final-head web-attempt-packet, web-harness-snapshot,
and web-pr-diff-boundary checks; review the full allowed-path diff and merge
only when all pass with a synchronized base. Then fresh-read main, the merged
PR and artifact blobs; append the actual transport receipt to Issue #3.
The sole requested mathematical deliverable is a reviewable special-case
proof, now preserved here. Subsequent work is external review of the frozen
proof, especially radial joints and boundary splicing, not a new root launch.
No transportation or CI event closes the open mathematical obligations.
