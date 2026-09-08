# MIN4 nonterminal checkpoint

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
PR: #38
Branch: web/attempt-opg37357-a01-min4-eight-v1
Base: 1a5eefd266401b903f15de10c07b3aff7d3f9773
Recovered candidate head: 4d0f3fd426bc3a9945807b7ea0bc51eaa93af28a
Verification-request commit: 57b19d190cd403b1aa83cd89de65113bbca124c1
Packet creation: 33dc1d94ab0539ba5a9d53ea36d9df3e4a18508c
Actual PR38 backfill / head before this checkpoint: 55fb31d3e343e7094c60ec93f0f7023bd6cfb1bc
Harness 1.2.4 snapshot: 4181effe1481eb1454130d2d6c87a7c327ef84e39b28d051fc496870d08864d1

## Exact outcome

The first non-bipyramid four-connected maximal planar structural class occurs at eight vertices. The complete edge set is
01 03 06 07 12 13 15 16 24 25 26 34 35 37 45 46 47 67.
The full complement is 02 04 05 14 17 23 27 36 56 57; the five preselected targets are 02,14,27,36,57. No leaf or nonadjacent dominating pair exists.

The entire graph has an explicit rational two-filled-simple-polygon representation, with 28 and 8 corners. All graph edges and all ten nonedges are included. Interior obstacle hits 14,27,36, so the proposed fixed-five capacity-two condition fails on a full representation. No exact one-versus-two value is claimed. No graph from the retained non-bipyramid structural screen through eight vertices remains for stage-two all-placement impossibility analysis.

The universal matching-concentration lemma is separately scoped: any q pairwise vertex-disjoint nonedges can share a free square at some rational GP placement avoiding all graph points/edges. It does not block all other nonedges. Consequently an unconditional capacity-two claim for fixed targets with a size-three matching is impossible; placement-dependent target choices and hypotheses of a complete representation are different quantifiers.

Full necessary CNF: 156 variables,31676 clauses,1502 simple paths. The real coordinate direction table admits exactly two of1024 labelings, not an enumeration of all2^56 directions. Full clause origins are checked. The recorded 228-variable fixed selector computation is drawing-specific and does not replace coordinate realizability or an all-placement proof.

## Reuse and actual checks

The existing fifteen candidate files were retained unchanged. Earlier shorthand counting thirteen omitted selected.json and probe-records.json; the fresh PR filename list has all fifteen. The only continuation additions are the verification request, ONE packet and this checkpoint. No duplicate branch or second packet was created. PR35/PR36 and all older candidates remain unchanged.

The candidate execution record contains actual bounded delivered-consumer runs and twenty negative tests. Limits are30 CPU/40 wall seconds,512MiB,one worker,4MiB stdout. The current resumed local check independently rebuilt the same numerical witness: its serialized2658-byte source matched Git blob d2670108fa280ae1c8822ba690cacdae5549b109 and SHA-256 c0d21807e630be1e0af0da8c8dbc5ec19124ad6d469aa56fc9807b6713931ca1. Direct rational boundary checks accepted it. This is not a trusted receipt.

The Atlas-based structural producer and standard-library degree/orbit/certificate consumer have different roles. The consumer includes complete degree-sequence coverage and checked nonplanarity/separator certificates, not an appeal to a library boolean alone. Existing source/observation hashes are those recorded in execution.json; no blanket claim to have recalculated every remote file is made.

## Publication and admission gap

The earlier incidence.py write was blocked without a commit. Its dependent general reconstruction/tube pipeline remains unpublished; no alternate publication route was attempted. The delivered check_candidate.py does not depend on it and can replay the complete two-polygon witness plus CNF/source checks. Do not call the entire incidence pipeline a repository-only runnable release. Large CNF/source caches are deterministic emitter output, not additional uploaded files.

The verifier request is research/artifacts/web-inbox/opg37357-a01-min4-eight-verifier-request.md. No compatible registered geometry/structural closure consumer was identified. Fixture policies, AI review, CI and merge are not mathematical Evidence. No truth ledger, registry, schema, Harness, workflow, Evidence, Result or Solution is edited.

## Selected frozen SHA-256 locators

Candidate prefix: research/artifacts/candidates/opg37357-a01-min4-eight-v1/
witness.json: c0d21807e630be1e0af0da8c8dbc5ec19124ad6d469aa56fc9807b6713931ca1
structure.json: 94df9f2bf7b85706cae6bc9afb94a591d045c3c999255d397d4a20a46a824151
selected.json: d13296c5d367a9cd09aaeb2805d833c631d9fd242d5389b3f4208e59781f2a54
check_candidate.py: b162bb02da1f10c1791da2bdadcfa951a65abb1d6b2f471ffd527ea351c54625
clause_audit.py: 4eec6c0740e223902961e6ef19b4b4b2ae3c5572cd57fca0098e22d2ccff9b11
guarded_cnf.py: 86814275e9ec2a3d723bc43d1cb043634a9daa9cd4e732cfa50566c2b8d81412
structure_audit.py: 39aa286e7a74cc0c3fa762b7c2137c221ef2b02e3549a9f1550a278ea2a9da1f
matching.py: 09674da06f2d60cfcf51db1c40c9890b4882be70098a7179dac6567cbdcb3c64

Failed-route proposal fingerprint: 10ad5ccc3293d6bb483ea6fa28de89c4a9f57c5490b2d3e614f1f0bc18fae2dd.
This is candidate-local, not a protected ledger entry.

## Transport next action

This checkpoint precedes the final-head checks. Read the full eighteen-file diff, confirm exactly one new packet and only allowed additions, then require web-attempt-packet,web-harness-snapshot,web-pr-diff-boundary SUCCESS on the exact final head. Merge only under normal protection. Afterwards reread PR,main,commit trees and append actual check IDs/merge SHA to Issue #3. Earlier runs cannot serve as final-head checks.

best_verified_candidate: none
best_verified_result: none
best_current_candidate: complete rational two-polygon counterplacement plus fixed-target matching barrier
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_atomic_step: order at least nine or another structural family; fixed targets must avoid the size-three matching obstruction, or use adaptive anchored incidence cores. Any retained graph still requires every realizable region and relevant degeneration boundary, not a fixed rotation.
root_status: open
