# C16 checkpoint: quantitative rational GP extraction

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg37357-a01-c16-quantitative-gp-v1
Issue: #3
PR: #19
Branch: web/attempt-opg37357-a01-c16-quantitative-gp-v1
Base: d7c9dbbb81ffd89cea1e15691ad32d14f3a6ece3
Head before adding this checkpoint: 80db79573784fb753dc955d79b2e6a7debabbd70
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Open obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
Harness SHA-256: 1b616175accd4e6432c60d0bd0087350a8d5d18fee8b49e9809a071292109fde

## Frozen artifacts

- research/artifacts/candidates/opg37357-a01-c16-quantitative-gp-v1.md: SHA-256 53c3d959567bfeb93b0a67792a69c23b4cb64c8930954427a34fb9e5e10cfb67
- research/artifacts/web-inbox/opg37357-a01-c16.packet.json: SHA-256 0afbfb47033c8cb0f5b3b7bdaa31c8df93225432cb02adb852b4349219a709e1; PR fields backfilled to #19. The remote blob af42f11b2b4d2709ec48b25f082a2b6e919013cf matches the locally serialized bytes.

## Scope

The proof begins with an exact rational sparse satisfying witness and supplied margin-two separation certificates, not a solver label. It derives positive coordinate guards, a witness-dependent radius, finite rational grid avoidance, and the explicit K2 repair. No grid, exporter, evaluator, solver or proof assistant was executed. The c15 executable publication limitation is not retried by this non-executable proof. Earlier candidates and protected ledgers remain unchanged.

The current final-head checks have not yet been observed at checkpoint creation; read all three and the diff before merge. Actual run/job/review/merge receipts will be appended to the same Issue #3.

## Next action

After gated merge, fresh-read main and audit c03's unrestricted connected-obstacle cutoff. In particular separate its cell-connectivity construction, witness-tree thickening, and final moving-endpoint general-position argument. Investigate pruning unmarked cell-tree leaves and a corner-counted offset neighborhood rather than repeatedly exporting the same sparse formula. A changed cutoff must have a new immutable candidate and must retain the source-faithfulness gap and root obligations.

Registered failed-route IDs at the latest inspected base: []. Candidate-local rejected shortcuts remain in prior artifacts. None of these transport or checkpoint states is mathematical admission.
