# C15 nonterminal checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg37357-a01-c15-circuit-construction-v1
Issue: #3
PR: #18
Branch: web/attempt-opg37357-a01-c15-polygon-circuit-v1
Base: 642573645569c9d2942abff288ff3e2a5e7bb8fb
Head before this checkpoint: 4db52007993822369e9a6caa2038acb46136049d
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Open obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root

## Artifacts

- research/artifacts/candidates/opg37357-a01-c15-circuit-construction-v1.md:
  e98e1dd637f3bee7e0eb423f550ef3f66b0655ccc65143d6e95a70ec1947aeb5
- research/artifacts/candidates/opg37357-a01-c15-fixtures-v1.json:
  f778c4f626bd12e471528b4e8ed6f4c524bf67fed4c07a0056051950b6cccb88
- research/artifacts/web-inbox/opg37357-a01-c15.packet.json:
  54be21167b9962cd025be7345f0845b37f627598a942f248c13859a7f875ba5a

Actual PR metadata is backfilled. Final checkpoint-containing head checks
remain to be read. Post-check/merge observations go to Issue #3.

## Progress and nonterminal limitation

The mathematical circuit construction fixes every original-symbol mapping,
primitive, clause index family and final conjunction. Sparse straight-corner
acceptance and strict contact-only nonedge rejection are exact hand-derived
fixtures, not executed outputs. No front-end source was committed: its
create_file call was blocked by platform safety checking and returned no
commit, as recorded in Issue comment 5563068341. It was not retried by another
upload route. This PR contains only a separate non-executable construction
proof and input data, not that source. Mathematical implementation/replay
remains open.

failed_routes: [] in canonical ledger at this base.
next_action: after checks/merge and fresh main, derive an explicit certificate
for rational sparse-to-GP perturbation. Supply positive-margin per-slot
separators; select strict sign branches and one Proper witness per nonedge;
bound every polynomial change in a rational box. Choose each free point from
a finite rational grid avoiding earlier-pair lines while keeping anchors/bits
fixed. This addresses the witness-extraction gap without needing blocked
executable publication. No graph-only precision or root conclusion follows.
