# C10 root-search checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_locally_replayed_q1_candidate: c08 root X4 replay-v2 package

Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Open obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
Issue: #3
PR: #13
Branch: web/attempt-opg37357-a01-c10-two-obstacle-samples-v1
Base: f2f0512dcf08742d7cedf732071810c5d7f66e33
Head before this checkpoint: 4d571282c1d3457f0fc76d049ebf5fc2f93d114e
Harness SHA-256: 1b616175accd4e6432c60d0bd0087350a8d5d18fee8b49e9809a071292109fde
Packet: research/artifacts/web-inbox/opg37357-a01-c10-two-obstacle-samples-v1.packet.json

## Root progress

Q1 has the published X4 obstruction and the c08 stored exact propositional proof replay. Trusted geometric statement-faithfulness, kernel and axiom replay are still pending. Q2 has the c09 induced maximal-planar extension reduction; it has no universal constant or divergent family supplied here.

C10 searched ten selected maximal planar graphs: four of order 10 at path-edge cap four, two of order 12 at cap three, four of order 14 at cap two. These are X4/X5/X6 and selected single flips, not exhaustive enumeration at those orders. All ten retained necessary-condition instances have stored Boolean models and sphere-face planarity certificates. Fresh solver-free replay evaluated every clause and every sphere certificate successfully. It does not construct obstacle polygons. No C10 UNSAT graph or UNSAT certificate was found. Earlier 1 GiB memory-limit failures carry no mathematical verdict.

## Integrity recovery

The earlier candidate run 34040853149 failed packet/diff validation with mismatched source digests for two_obstacle.py and replay.py. Current source bytes were matched against the remote Git blob identities and a new solver-free replay was run with stable bytes. The packet's real PR fields were backfilled to #13 and source/observation digests corrected. Final-head checks have not yet been observed in this checkpoint; read them before any merge. A previously malformed unmerged whole-frame upload was replaced by individually hash-bound ASCII chunks.

Current code digests:
- two_obstacle.py: da296ffb0f397062b21b8758edac3c1ccbd8574e3b1e79289b7f58c5653d5f5b
- replay.py: 4e9b5a789547f823dc13afb34d3e417a2b20ba8a0cc3970eb791a97fa5307a5e
- samples.txt: 08db040b2c92d3654ca5aa43e2ace1ea6d090a2f88258d8f8cdb541d6164b1cf

## Next precise mathematical target

Every nonedge assigned one blocker must meet ONE common component of the complement of all graph-edge segments and graph points. Pairwise key-path tests do not by themselves supply this whole-class intersection property, nor realizability of a Boolean orientation assignment. Derive a multi-nonedge obstruction retaining all allowed placements, or construct an actual uniform two-obstacle representation of X_r. Do not use relaxed SAT as obs<=2, a fixed-drawing obstruction as a graph-level obstruction, or a planar-convex lower bound for ordinary obstacle number.

Registered failed-route IDs last checked: []. The rejected shortcuts and resource failures above are candidate-local records; no protected ledger was edited. After a genuine merge, refresh main and continue on the same root and Issue. No background work or terminal mathematical status is asserted.
