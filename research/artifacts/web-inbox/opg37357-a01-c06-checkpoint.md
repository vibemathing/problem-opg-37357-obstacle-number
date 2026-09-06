# c06 checkpoint: exact ray-parity family

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg37357-a01-c06-ray-family-v1

Issue: #3
PR: #9
Branch: web/attempt-opg37357-a01-c06-ray-parity-v1
Base revision: 939147c883291f4a323fed2bcef1fe56dcfb66e8
Last observed head before adding this checkpoint: c663dce031b51c436fcdb9fd48077a37b3dc5b7c
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Open obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
Harness snapshot SHA-256: 1b616175accd4e6432c60d0bd0087350a8d5d18fee8b49e9809a071292109fde

## Artifacts

- research/artifacts/candidates/opg37357-a01-c06-ray-family-v1.md — SHA-256 33b3c820b96f39778b81c2e6b5b6f5942f918ef488e6707bd2bcd1e9f1a58f4e
- research/artifacts/candidates/opg37357-a01-c06-ray-fixtures-v1.json — SHA-256 c9582a663ae515b6b967089a98f55a2ea63c9a091495f7297400c1d79450ce9e
- research/artifacts/web-inbox/opg37357-a01-c06.packet.json — SHA-256 a0a58449d28b5cf3cfd208af5d59daea4bfa072d963cc3691cad3c92c137649f

## Conclusions and boundaries

The K2/triangle family has explicit combined-GP determinants, positive distance expressions, interior barycentric coordinates, and exact vertical-ray sign tables. It exposes false witnesses from full-line counting and missing denominator signs, and false witness rejection from additive rather than XOR parity. Four rational fixtures cover both cyclic orientations. They are derived expectations, not executed outputs. No solver, test suite or geometric evaluator ran. Existing exporter and all earlier candidates remain unchanged.

The three required transport checks on the final checkpoint-containing head are not yet observed here. After review/check/merge, the actual head, run/job IDs and merge SHA will be added to Issue #3. No mathematical verification is inferred from them.

Registered failed-route IDs checked remain []. The three local mutations are diagnostic alternatives, not new admitted routes and not root-level counterexamples.

## Next action

After merge, fresh-read main and audit a sparse replacement for the full combined-triple GP block. Retain closed-contact exclusion for edges, exterior parity and simple-polygon guards; require a proper crossing witness for each nonedge. Investigate whether fixing the auxiliary bits gives an open feasible coordinate neighborhood in which combined GP can be restored, preserving the same m. The bit-fixed qualification and contact-only blockers require explicit attacks. This mathematical audit can proceed without running a solver; the c06 exact evaluator replay remains open.
