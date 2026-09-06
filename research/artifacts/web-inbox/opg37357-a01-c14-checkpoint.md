# C14 nonterminal checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg37357-a01-c14-compiler-v1
Issue: #3
PR: #17
Branch: web/attempt-opg37357-a01-c14-circuit-compiler-v1
Base: 3ee1546d580fa56b9b5b25b5d3ec82caeabb8f6d
Head before this checkpoint: 46347b9dd6449a3e5c494c934c10b20172b4c513
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Open obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root

## Frozen artifacts

- research/artifacts/candidates/opg37357_a01_c14_circuit_compiler_v1.py: 1b86f1cbe20ff9bc27682d4a36868ce80149d6b8d435b8c3ef1ca3ae2d979fcf
- research/artifacts/candidates/opg37357-a01-c14-circuit-contract-v1.md: 0373d52a185396b654ecc33704ec079885edaad84dbcfe3c53d839b9548be49e
- research/artifacts/candidates/opg37357-a01-c14-fixtures-v1.json: fc17f5ca16492fc685fb660020bb76fddaa2f947b14706f18abe6db26deb9ce8
- research/artifacts/web-inbox/opg37357-a01-c14.packet.json: e4b5ea484551f2e7884a61db0c09b3a173b050f1dce6f3dd42af6c1914eedf1c

The actual PR number is backfilled. Checks on this final checkpoint-containing
head still need to be read; post-check/merge observations belong in Issue #3.
Code and contract blob identities matched fresh remote reads. The required
packet gate must check every frozen candidate digest, including the fixtures.

## Progress and explicit limits

The typed compiler implements c13 with earlier-node indices, separate
arithmetic/Boolean namespaces, exact rational constant equations, total
sign gadgets and root assertion. Complete positive/zero/negative assignments
exercise sign-versus-truth and final-root coverage. Constants and invalid
references are separate fixture classes. Only static AST and byte bookkeeping
were executed; no module, compiler, fixture evaluator, SMT parser or solver ran.

A reference's namespace is fixed by its schema field. Two equal numerical
indices in different arrays are different symbols; the validator cannot infer
that a producer intended a different, otherwise valid index. Source-to-circuit
faithfulness therefore remains essential even for well-typed input.

failed_routes: [] in canonical ledger last read. Candidate-local mutations
include omitted sign/zero/one-hot constraints, shared reciprocal witnesses,
bounded auxiliary ranges, wrong OR and incomplete assertion coverage.
None is a root-level graph obstruction.

## Continuation

After gated merge, fresh-read main and begin c15 on this same bounded target:
construct the circuit directly from indexed polygon predicates instead of
parsing unrestricted SMT text. First freeze the bijection from c11 free real
symbols to x-indices, including all parity bits. Constant anchors must remain
constant nodes rather than unconstrained input wires. Compare against c11's
exact-m sparse formula, not c05's all-triple-GP formula.

Build arithmetic DAG nodes for orientation, dot products and area; Boolean
nodes for Meet/Proper, adjacent guards, generic forward-ray parity and
edge/nonedge clauses. A blockwise induction must show the resulting circuit
root equals the entire c11 conjunction for each original assignment. Then c13
and c14 apply without changing n,m, labels or geometry. Guard against omission
of the final parity endpoints/root and against treating unsupported input as
false. Replaying the resulting frozen circuit remains a separate authorized
verification task. The unrestricted completeness gap and root questions are
not closed by any of these transport or compiler candidates.
