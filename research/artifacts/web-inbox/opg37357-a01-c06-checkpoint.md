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
Last observed head before adding this checkpoint: baaa270ad552da21b8008ec9fa39c2051b310d51
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Open obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
Harness snapshot SHA-256: 1b616175accd4e6432c60d0bd0087350a8d5d18fee8b49e9809a071292109fde

## Artifacts

- research/artifacts/candidates/opg37357-a01-c06-ray-family-v1.md — SHA-256 3e6ae3f14640ec4be93955f32453d31cbc973d7876d54c2a92eb60dfbdc4f7fd
- research/artifacts/candidates/opg37357-a01-c06-ray-fixtures-v1.json — SHA-256 61ef9b85e199369bd78b6f6a4d9791ad6e4ae071985efe7b84746fb1d9c9e0c1
- research/artifacts/web-inbox/opg37357-a01-c06.packet.json — SHA-256 642e79e611e667d834e2713ca0b3d013ce8ebebd9c30099d33e47fafb76fbcab

## Conclusions and boundaries

The K2/triangle family has explicit combined-GP determinants, positive distance expressions, interior barycentric coordinates, and exact vertical-ray sign tables. It exposes false witnesses from full-line counting and missing denominator signs, and false witness rejection from additive rather than XOR parity. Four rational fixtures cover both cyclic orientations. They are derived expectations, not executed outputs. No solver, test suite or geometric evaluator ran. Existing exporter and all earlier candidates remain unchanged.

The three required transport checks on the final checkpoint-containing head are not yet observed here. After review/check/merge, the actual head, run/job IDs and merge SHA will be added to Issue #3. No mathematical verification is inferred from them.

Registered failed-route IDs checked remain []. The three local mutations are diagnostic alternatives, not new admitted routes and not root-level counterexamples.

## Next action

After merge, fresh-read main and audit a sparse replacement for the full combined-triple GP block. Retain closed-contact exclusion for edges, exterior parity and simple-polygon guards; require a proper crossing witness for each nonedge. Investigate whether fixing the auxiliary bits gives an open feasible coordinate neighborhood in which combined GP can be restored, preserving the same m. The bit-fixed qualification and contact-only blockers require explicit attacks. This mathematical audit can proceed without running a solver; the c06 exact evaluator replay remains open.

## Transport correction

Run 34023412534 failed on the two c06 candidate digest fields. Local artifact bytes were matched to remote Git blobs a9654e94ff4dd5b80c77aa349a42d297764f3741 and b31ef5123eb2ec82e041add19c7f119d1194296f before recomputing SHA-256. Commit baaa270ad552da21b8008ec9fa39c2051b310d51 corrected those fields and actually backfilled PR #9 after an earlier 409. The corrected packet blob is 18f947b621d756da7f81165fbfcad37121ebcebd. Earlier draft digests and unobserved head/run references are superseded; no mathematical content changed. Final-head checks still require a fresh read.
