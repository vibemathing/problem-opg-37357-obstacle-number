# C12 nonterminal checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg37357-a01-c12-separation-v1
Issue: #3
PR: #15
Branch: web/attempt-opg37357-a01-c12-separation-v1
Base: 184e54aab93674fc1dee66fcdabeb91e9684e62f
Head before this checkpoint: ddb920bf075f9dd414d682cdebcdf2829d32333e
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Open obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root

Candidate: research/artifacts/candidates/opg37357-a01-c12-separation-v1.md
Candidate SHA-256: cce97a52da846818a2a17b7ac72742fe2bc6899ca223d6bb7e6c2d4abeeda1d6
Packet: research/artifacts/web-inbox/opg37357-a01-c12.packet.json
Packet SHA-256: 297d0c5926f1d0cc472230aa06aec29f23ca876ceebc700f16762c4205f90e67

The actual proof blob matches the frozen bytes; actual PR fields are backfilled. Checks on the final checkpoint-containing head remain to be read. Post-check/merge observations must be appended to Issue #3, not inferred from this file.

The candidate gives a closest-pair completeness proof for four unit-margin endpoint inequalities and exact per-slot projection back to S. Point segments and collinearity are included. Seven explicit audits exclude zero margin, unit-normal/coefficient caps, containment shortcuts, common separators for a U-shaped obstacle, and false claims of openness at every saturated certificate. No mathematical program or verifier ran.

failed_routes: [] in canonical ledger at this base. Rejected shortcuts are candidate-local mutations, not new admitted failed routes and not root counterexamples.
next_action: after merge and fresh main, freeze the total positive/negative/zero sign gadget and arithmetic/Boolean circuit lifting proof. Preserve reciprocal nonnegativity and the zero equation. Separate real equivalence of square slack from rational extension, and retain quadratic wire variables rather than substituting cubic products. Both admitted obligations remain open.
