# c09 root checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_locally_replayed_q1_candidate: c08 replay-v2 X4 proof package

Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Open obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
Base: f619c5b133b224764fd1c0f0c301e1b6b7df3b5a
Harness snapshot SHA-256: 1b616175accd4e6432c60d0bd0087350a8d5d18fee8b49e9809a071292109fde
Branch: web/attempt-opg37357-a01-c09-q2-triangulation-v1
Issue: #3
PR: #12
Head immediately before this checkpoint: a9a48c604c6d65c0a729a2b1475ef4ca7dd79666
Packet: research/artifacts/web-inbox/opg37357-a01-c09-q2-triangulation-v1.packet.json
Packet SHA-256: 0d717f462407ae804b0732ea924ad6f2b05e2f4fe03b68fc77c7e77ee22f72ae

## Frozen candidate hashes

The following files are under research/artifacts/candidates/opg37357-a01-c09-q2-triangulation-v1/:
- q2-triangulation.md: 1fbbe9c96dd367a8aea133c103eff7d43b3f093dab3ed854e7d77a442af422c4
- triangulate.py: 811c280b2280738b7ae9ba7adffdb10850255c376d54826ceb76b086373f2c26
- atlas-observation.json: 718c4a8aff5e9a6409b5e603e684162c3977cf7a1a2414271c8ae8aecabe976e
- c08-count-audit.json: 8c9e81bb4b33224b4269cfe35d8495880514c4b2c2e72088ad14a1ed4208b518
- examples.json: ffdc02f498a4f2fe665bc2b8a19fb77b14f926fabdd31d1305b48e87459d4712

These local bytes were matched to freshly fetched remote Git blob identities before packet backfill. Final-head transport checks are not yet recorded here; their observation belongs in Issue #3.

## Substantive progress

Q2 is reduced to maximal planar graphs by a linear-size INDUCED triangulation extension. Selective coning preserves the absence of separating triangles for triangle-free inputs. K5 minus an edge prevents extending every planar input to a 4-connected planar graph. All 1012 planar atlas inputs of orders 3--7 passed finite construction regressions; these are not obstacle searches. C08's inaccurate prose subcounts are corrected without changing its full necessary-CNF hash or proof input. No Q2 constant or divergent family is claimed.

Registered failed-route IDs checked: []. Local rejected shortcuts: ordinary edge-deletion monotonicity, unrestricted 4-connected extension, and using planar-convex lower bounds for ordinary obstacle number.

## Next bounded root step

After actual checks and merge, refresh main and continue with two-obstacle all-placement necessary conditions on maximal planar graphs. Keep proof output for any UNSAT and exact Boolean assignments for relaxed SAT. A two-color assignment for nonedges is necessary, not a geometric representation; do not infer obs<=2 from that relaxation alone. The trusted Q1 semantic/kernel/axiom replay remains open. No background work or terminal status is asserted.
