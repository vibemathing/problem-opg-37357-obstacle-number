# c05 checkpoint: exporter source frozen for transport checks

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg37357-a01-c05-exporter-v1

Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Open obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
Base revision: 79cdfcaad9ab63d9ea7d84a3b1d1d8341fd0e571
Harness snapshot SHA-256: 1b616175accd4e6432c60d0bd0087350a8d5d18fee8b49e9809a071292109fde
Issue: #3
PR: #8
Branch: web/attempt-opg37357-a01-c05-formula-export-v1
Last observed head before adding this checkpoint: de13b00ac49e557c47dd199617edaf55fa18cbe4
Transport state: PR fields backfilled; required checks on the final checkpoint-containing head are not yet observed here. The post-check/merge observation belongs in the same Issue #3 thread.

## Frozen artifact digests

- research/artifacts/candidates/opg37357_a01_c05_exporter_v1.py: 46f7dd6e2ca9cdf2148efd763fae6cad6ebab33e79aecf0ee4510b93df827403
- research/artifacts/candidates/opg37357_a01_c05_test_exporter_v1.py: 5eb41f5dd57127fc465df99f11dd11a532b8011bf00b46390e5761c84cc44ab6
- research/artifacts/candidates/opg37357-a01-c05-export-contract-v1.md: 054f7091491a05e28500815c396a1c7ddee6c70790b20a4946dc733fa96843be
- research/artifacts/web-inbox/opg37357-a01-c05.packet.json: 90f38f9713b7f83bd007990dff0f206626a79f664c6019a93e0563eb15b41e22

## Progress and limitations

The candidate translates the c04 normalized formula into deterministic bounded QF_NRA text. It explicitly distinguishes export success, mathematical false, invalid input, resource refusal, I/O failure, and internal failure. Regression sources contain exact expected counts and two rational witness seeds. Only Python 3.13.5 AST parsing and digest bookkeeping were executed; no exporter run, test run, solver run or mathematical receipt exists.

Registered failed-route IDs checked at the base: []. Rejected local shortcuts remain documented in c01--c04. c05 additionally excludes accepting Boolean labels as integers, duplicate JSON keys, duplicate reversed edges, and returning a false formula on resource refusal. No protected ledger was changed.

## Next bounded action

After required checks and a candidate-only diff permit PR #8 merge, fresh-read main and continue on a new c06 branch bound to the same admitted target. Build exact rational assertion/witness regressions with NONZERO even ray crossing counts; the current positive seeds have zero ray crossings. A triangle with corners (-1,1),(2,1),(3/2,3) above anchors (0,0),(1,0) gives crossing bits (1,0,1). A companion triangle (-1,-1),(2,-1),(3/2,3) puts both anchors inside and must give odd ray parity. These expose dropping the forward-ray sign test or replacing XOR with ordinary addition. Save only algebraic deductions and test inputs, not unexecuted output claims.

Current mathematical dependency: replay of c01/c04 geometry and source-to-formula translation remains open. Transport checks cannot supply that replay. No terminal mathematical status is asserted.
