# C13 nonterminal checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg37357-a01-c13-quadratic-lift-v1
Issue: #3
PR: #16
Branch: web/attempt-opg37357-a01-c13-quadratic-lift-v1
Base: 6e4728e350dc8f47a2dd2e2eb2c77c344a82bd55
Head before this checkpoint: b12d53a3a7775d993a2e13b6e409472f3b6ace4e
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Open obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root

Candidate: research/artifacts/candidates/opg37357-a01-c13-quadratic-lift-v1.md
Candidate SHA-256: c047581ba545bf9ce2855b746d02b7840894ae40ab260e88f8affe8f490bf030
Packet: research/artifacts/web-inbox/opg37357-a01-c13.packet.json
Packet SHA-256: bc5314fb85dd7baaffe70500b592d88940943a48da4af246d31d795609af019a

Actual PR metadata is backfilled; candidate bytes match the fresh Git blob.
Required checks on the final checkpoint-containing head are not yet observed
here. Append actual checks/review/merge to Issue #3 and use fresh main for the
next cycle.

The total sign gadget preserves positive, negative and zero cases, including
under NOT and unused Boolean branches. Arithmetic wires and Boolean induction
give exact pointwise projection to a conjunction of quadratic equations and
linear nonnegativity. Seven mutation counter-assignments catch missing
nonnegativity/zero/one-hot constraints, additive OR, shared reciprocal names,
disconnected truth bits and arbitrary auxiliary bounds. Rational extensions
are distinguished from real-only square-slack extensions. No mathematical
compiler, evaluator, solver or proof assistant ran.

failed_routes: [] in canonical ledger last read; candidate-local mutations
are not root-level counterexamples and do not change the admitted route.
next_action: implement a bounded typed acyclic circuit-to-quadratic compiler,
then explicitly bridge c11 polygon predicates to that circuit format. Separate
generic circuit correctness from the missing polygon front-end translation;
do not claim the end-to-end geometric statement from generic compiler output.
