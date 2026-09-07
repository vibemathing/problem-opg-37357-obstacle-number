# C28 nonterminal checkpoint: octahedral h=2 SAT and five-target continuation

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
PR: #34
Branch: web/attempt-opg37357-a01-c28-octahedral-h2-v1
Base: f09892bdb8e26edcdfc80edacc2790de904a70ea
Packet creation commit: 8706bd4a9cadae1656e4d2a9533d72392333d7c6
Actual PR binding commit / head before this checkpoint: a0d13db7e4adb0ad9d5a85b3480790a60029313f
Target: obligation:opg37357-root
Harness 1.2.4 snapshot: 4181effe1481eb1454130d2d6c87a7c327ef84e39b28d051fc496870d08864d1

## Resume from actual state, not stale PR #32 text

PR #32 was already merged when this turn fresh-read it; its final head was
27be45a2de34eb886ebe3825c170b78dd97b8677, its merge was the base above.
The old final run 34136533643 had all three successful jobs. No C27 branch,
file or packet was overwritten/reopened. Issue #3 comment 5572906761 records
the resumption and actual local new results. C27 fiber.py was byte-matched
and reused; no C22/C26 X4 clause was regenerated. The original missing C20
byte strings have not been recovered. C28 is new source and a new finite test.

## Actual finite h=2 result

Complete octahedral edges: 02,03,04,05,12,13,14,15,24,25,34,35.
Nonedges: 01,23,45. Three induced diamonds share triangle 024; connector bits
are 13,15,35. The rotation and sphere faces are in witness.json.

Fresh generator and separate row consumer cover all 84 simple paths, including
five-edge paths. CNF has 32 variables and 1140 clauses. Every key origin names
its two nonedges, actual path, color, mode and common side variable.
Both exhaustive methods agree: 11904 abstract orientation-rule survivors;
15952 direction-label models; 807232 full direction/label/side models.
All 2^20 orientations and 8 labels are covered; the second checker accounts
for 536870912 full assignments after exact-one z substitution. No count is
claimed to count real drawings. All 8 specified connectors are SAT; their
complete direction-label spaces contain 226492416 pairs in total.

The least Boolean model is NOT only abstract SAT: all 20 x bits are false,
all three (z0,z1) pairs are (False,True), and all six side bits are false.
It has integer points p_i=(100i,-100i^2) and the displayed 16-corner single
filled simple polygon. Exact checks: 192 edge/side pairs, 104 nonadjacent
polygon-side pairs, six points excluded, three strict nonedge midpoints.
Thus the selected octahedron cannot be an obstacle-number-three candidate.
The same coordinates have a common free component for all 8 connector graphs;
those geometry checks reuse C27, while the two Boolean cores do not.

Sixteen damaged graph/path/clause/direction/label/polygon/rotation inputs were
rejected. Valid connector-edge deletions were separately recompiled and tested.
Main final run: CPython 3.13.5, exit 0, 3.826872 seconds, 30 CPU / 40 wall seconds,
512 MiB address space and 4 MiB output. Actual --cnf and --sources exports also
exited 0. execution.json records true source/input/output hashes, not a receipt.

## Precise failed route and the next mathematical obligation

The failed_route_proposal fingerprint is
74eac95efca2274008457c408260f9253d10df5642f861d888c4343afe703db7.
It excludes ONLY the central-triangle three-diamond graph and its 8 tip-connector
subsets as an h=2 obstruction. It does not say every diamond coupling is SAT
or every planar graph has two obstacles. Protected failed-route records are
not edited. This family must not be retried by merely rearranging its labels.

For a certified empty triple F of nonedge incidence sets, add
OR_(s in F) not z_(s,r), for each r. C18's selected triple still admits 6
of 8 labelings. At most 4 targets with only rank>=3 exclusions always admit a
2+2 partition. Five targets with all 10 triples excluded reject all 32 labelings:
this is the sharp ABSTRACT threshold, not a new planar lower-bound example.

next_obligation: construct a simple planar graph for which EVERY real placement
has five nonedges with no common free component for any triple, or an equivalent
placement-universal capacity bound. No such graph is supplied here. Increasing
the selected target count to t would yield h>=ceil(t/2) only AFTER proving that
all-placement capacity premise. Do not invent a ternary cut to reject the actual
common-component octahedral minimum model.

T: C19 tube/Jordan; not needed for the explicit main polygon.
A: C27 finite incidence; direct C28 polygon and two Boolean enumerators separate.
P1: earlier X4 candidate unchanged. P2: only this finite growth interface excluded.
Root still includes exists h forall planar G exists placement; finite SAT counts,
abstract noncolorability, transport and CI do not close this quantifier.
Current registry remains fixture-only and no compatible trusted closure receipt
exists. The new verifier request is not an EvidenceLink or signed result.

## Frozen files and delivery boundary

research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/README.md
  c8d0c6608db916a47cf20d9b32c176630eda055e1093f8c47b1df238f961e8b2
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/coupling.py
  8f45d8e8605c6347c486bd11ec91d0f30eabf58354522189243e8861bdcb681b
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/exhaustive.py
  31d2b29b6f75ef6b90d4e313071f8a40e8efb5952881aa3308ccc1257d492eb4
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/second_check.py
  171e1c685d4be4348a2b1d23032be323543c0d0dd27554d5a61b91fab5ae0bf6
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/geometry.py
  bbab0b90786c7e330982f12377525594877ae2cb0b7aa8f86c77c828709058b8
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/checks.py
  407c291d276e2f1ec7e6ef022d92c42643bea04fd117d321b3a21aa7c22fd2b8
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/witness.json
  c9214b2330a8c29847b1c49723c0e859d1f9e25294f5662ea80b83e76004b9e8
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/observation.json
  3cb6eb886c4d8a210e4413357dcc34324a190ceaa5a92e8f5873d9c477f09df7
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/execution.json
  156906fb93edc5e6b91c115931306549905b477e926e960e274071e80392dc5a
research/artifacts/web-inbox/opg37357-a01-c28.packet.json
  1307d755fe2d5283f32a37c9b5bf783cfb5ae47ffde9365c811cb5d83dcc0e2d
research/artifacts/web-inbox/opg37357-a01-c28-verifier-request.md
  9d46e6464e988df36835d75bcc39e253e6e48b1b6ab17a67439967b559a4db2a

All nine candidate files were matched against their full remote Git blob IDs.
The five new source files are ordinary text, without network/process/dynamic
execution/file-access behavior; checks prints stdout. Earlier artifacts unchanged.
Raw DIMACS, source TSV and full stdout are byte-pinned deterministic exports
of the delivered implementation, not separate GitHub files in this packet.
They have no unpublished source dependency; C27 fiber.py is already on main.

This checkpoint precedes final-head CI. Inspect its actual new commit, the three
required checks and full candidate-only twelve-file diff, then protected squash
merge. Fresh-read main, merged PR, file tree and this checkpoint, and append
actual run/check/head/merge IDs and this file hash to Issue #3. Do not reuse
checks from an earlier head. No second packet is allowed in this PR.

best_verified_candidate: none
best_verified_result: none
best_h2_candidate: exact octahedral SAT with realized least model and 8-connector rejection
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: finish final-head transport, then five-target all-placement topology.
