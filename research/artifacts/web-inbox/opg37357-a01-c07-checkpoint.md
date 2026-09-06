# c07 checkpoint: sparse GP proof candidate

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg37357-a01-c07-sparse-gp-v1
Issue: #3
PR: #10
Branch: web/attempt-opg37357-a01-c07-sparse-gp-v1
Base revision: 853be12e7783f3b4843e98416a9cbbd29f2d41bf
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Open obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root

## Frozen SHA-256 values

- research/artifacts/candidates/opg37357-a01-c07-sparse-gp-v1.md: 4a733bb1bfbd8bf539b59e8d25d812538d2ff86eeae7fae95db536a678c65109
- research/artifacts/web-inbox/opg37357-a01-c07.packet.json: bb4b3f4179c06b4e04f0ed4c5807574984692422223e8d560242e63e407ae91a

## Mathematical progress

S requires robust proper crossings for nonedges, retains closed avoidance for edges, and removes the combined-triple GP block. A fixed-bit coordinate-neighborhood argument restores GP-ALL without changing m. The explicit adjacent guard is retained but is not claimed irredundant. A contact-only triangle witness attacks the weaker local-openness argument. Bit perturbations and three fixed collinear anchors are excluded from the proof's scope. Syntactic count savings are not measured solver performance. No mathematical checker or exporter ran.

Registered failed-route IDs checked at the base: []. No protected ledger was modified. The corrected initial minimality wording is preserved in branch history rather than presented as a separate admitted route.

## Transport and continuation

PR metadata is backfilled in the packet. The final checkpoint-containing head and its three required checks have not yet been read here; actual review/run/job/merge observations must be appended to Issue #3 before starting another cycle. CI and merge are transport only.

next_action: fresh-read main after this PR's gated merge, then prepare a separately frozen sparse exporter. A further exact simplification is available: replace strict products of orientation polynomials by opposite-sign or same-sign Boolean cases, yielding a degree-at-most-two formulation. Retain strict zero handling and all boundary/ray conditions; do not increase claims from coordinate witnesses to unrestricted obstacle-number conclusions.
