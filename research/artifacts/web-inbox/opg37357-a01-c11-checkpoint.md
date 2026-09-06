# C11 nonterminal checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg37357-a01-c11-exporter-v1
Issue: #3
PR: #14
Branch: web/attempt-opg37357-a01-c11-sparse-quadratic-v1
Base: 6e42ac8958677c1824937ad841804086f6d117b8
Head before this checkpoint: e7d9a6492b75106a6ec7c07efe91d2ead6a4924c
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Open obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root

## Frozen byte identities

- research/artifacts/candidates/opg37357_a01_c11_sparse_quadratic_v1.py: b3b05d9657596bd898ebb5494c639ce49c69d0e4547783d27b1726763449e33b
- research/artifacts/candidates/opg37357_a01_c11_test_sparse_v1.py: 56ffcdb2cb68037e17719d0329bdd5de2b4ed2f6a56a53b59f3cf675f7b5d647
- research/artifacts/candidates/opg37357-a01-c11-export-contract-v1.md: 98f957930062a27705617c6eb236d27fa9b8fe766b3aaaab32579ea78dd484fb
- research/artifacts/web-inbox/opg37357-a01-c11.packet.json: e27f433e72d8b521048dce0f0d79482cffdc11c0efd8754bdf65dd91f25fe03b

The three candidate byte identities were also matched to freshly read Git blobs. PR metadata is actually backfilled to #14. Required checks on the final checkpoint-containing head remain to be read before any merge. Post-check/merge observations belong in Issue #3.

## Progress and limitations

New source implements c07 sparse existence with quadratic Opp/Same primitives, pinned c05 helper bytes, closed edge and polygon avoidance, strict nonedge crossings, and exact forward-ray XOR parity. It checks assertion/declaration counts and preserves refusal versus false distinctions. Regression source covers signs including zero, cyclic structure, polarity and c06 rational ray cases. Only static AST parsing and hash bookkeeping ran, not modules, exporter, tests, solver or proof assistant. The test source is not a complete SMT parser/semantic verifier.

failed_routes: [] in the canonical ledger last read; prior candidate-local mutation counter-witnesses stay relevant. Neither predicate simplification nor engineering caps produce unrestricted obstacle-number conclusions. C08--C10 root candidates remain unchanged.

next_action: after gated merge and fresh main, derive an exact unit-margin separating-line certificate for two closed disjoint segments. Treat coincident endpoints, collinear disjoint segments and positive-margin scaling explicitly; retain exterior parity. Then audit a circuit/sign lift to a conjunction of quadratic constraints with pointwise projection semantics. Do not confuse this planned next slice with executed code or an admitted proof.
