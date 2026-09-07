# C29 nonterminal continuation checkpoint

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
PR: #36
Branch: web/attempt-opg37357-a01-c29-prism-rank3-v1
Mathematical execution base: f09892bdb8e26edcdfc80edacc2790de904a70ea
Synchronized packet base: 61943c788f95f91874b99b77f06b4b8c898a6db7
Non-force sync commit: 1059b792c8fa8c50ae3a8a76f6cb80a781627c25
Packet creation commit: b650e9633a32ee4e05626b4506fd025c637aa778
Actual PR36 backfill commit / head before checkpoint: 56fc47947a5a99397f0e4e6fc96a8121b26b7b72
Target: obligation:opg37357-root
Harness 1.2.4: 4181effe1481eb1454130d2d6c87a7c327ef84e39b28d051fc496870d08864d1

## Complete finite result, not root closure

All 27 labeled face-diagonal completions of the three-C4 triangular prism
are SAT under the necessary h=2 formula. All simple paths of up to five edges
are included. Every direction bit and every valid two-label assignment was
covered, with exact side-variable elimination and a separate semantic-mask
check. Total 536870912 projected assignments and 924356 satisfying pairs.
The seed has 62 variables,2106 clauses,54 paths,42 cross-module paths;
67108864 projected assignments and48060 satisfying pairs. Each lexicographically
smallest full assignment and full CNF digest is in family-results.json.
Producer and consumer import no C22/C26 generator. Full sources are runnable.

The seed's minimum direction table is actually realized by p_i=(i,-i^2).
C27's pinned exact fiber finds a common component for all six nonedges. This
is not a realization proof for every SAT table or every family completion.
The rotations and exact plane drawing of all27 are separate planarity certificates.

The new rank-three profile has six targets, incidence all pairs of four
components. Pair-only constraints admit8 two-label models; four ternary
exclusions remove all8. Its integer cover is3 but fractional weighted bound2.
Six selected targets of one rational K4-plus-isolated-points drawing realize
this incidence. It is NOT a statement about every placement of that graph,
or even an exact cover claim for all its nonedges. The isolate positions are
not forced by the abstract graph. The general component-selector elimination
retains every minimal empty target family, not just pairs or triples.

Actual checks: 14 mutations rejected;27 plane drawings;3 affine controls;
4096 four-target incidence profiles on3 components,65536 label cases.
CPython3.13.5 exact integer/Fraction, per-command30CPU/40wall seconds,512MiB,
one worker,4MiB stdout. One outer batch timeout was resolved by smaller
bounded batches; all27 final all-path runs have persisted successful records.
Full seed CNF/source caches are actually emitted and hash-bound, but not
claimed to be separate uploaded files. execution.json preserves this distinction.

## Exact failed interface and missing placement condition

Failed-route proposal fingerprint:
e4be5daf44a9e2b2d222be4185b1a87fcdbe7de3ec5c43590ab25b6bae0142ed
Only these27 necessary formulas are excluded as an UNSAT path. This does not
prove every planar h=2 interface SAT and does not settle the root.

Next placement lemma: construct a simple planar coupling whose EVERY real
placement forces a ternary integer-cover obstruction, including the same
component per obstacle label, or give a precise counterexample to that proposed
coupling. A single drawing's empty triple intersection does not suffice.
Do not retry the X4-copy-only or finite prism UNSAT proposals unchanged.

T=C19 tube/Jordan; A=C20/C27 fixed incidence; P1=C22/C26 X4;
P2=placement-universal growth and unbounded graph order remain separate.
No compatible trusted consumer/closure invocation appears in the fixture
registry. The verifier request is not a receipt; no Evidence/Result/Solution
or protected record/schema/Harness/workflow/governance was edited.
Original five C20 byte strings remain unavailable; no recovery is asserted.
Other concurrent C28 work was left untouched. A later main candidate was
synchronized through a real two-parent commit and a non-force fast-forward.

## Frozen file SHA-256

Candidate prefix: research/artifacts/candidates/opg37357-a01-c29-prism-rank3-v1/
README.md: c6c259fb0c866c71b0725c68bd22dc35d86e3e78c6619eef52a756905127ae5b
seed.py: 8557e38e9519cfae085601b1394b41a90d2067422321d01c14759f623d6c58b6
producer.py: 2228e0ecce7aedc35ab322fa8be2636b32e3709ca7bbc171da15b1fc9f874a44
audit.py: 0c9d0551e4b4f2b99d33e707c286694e0d70bedb0f8c84f944bd02edca3090b0
run_census.py: 991b5fe7f1b99d1ce4f34700d27772897923941420c7b14db9e0330ae53e813e
controls.py: a1a4b0841dab508b484fc1f960b6139037907394a0d86bcc38074148ae48adc3
rank3.py: 73211f05be70855eb5ca991c07b03f5981dfc9107c557a220e9a0e9ba0ecec53
family-results.json: fc1bf96a85d9370e811b56231f919572063110b08ae06f7354873174dbd40689
controls.json: db9daf351d0357886fbf270c54ef3ea52d6b1c9489fb9093f96ef0976098ce58
execution.json: dbefbc52fed25f1e1f2ed9df3cb6a30e8b87a50aa75f8b88f6704ee9f3ca0e68
research/artifacts/web-inbox/opg37357-a01-c29.packet.json:
  6082d44693c764f90a4df6e88b21801c86187b549740a7be53a48239c0c0a362
research/artifacts/web-inbox/opg37357-a01-c29-verifier-request.md:
  5621e4a83db056c91b8dd5a77bdbb1334047ab75879398873cebd652950b77c8

This file precedes its own final-head checks. Its complete bytes/hash and
actual final commit, three check IDs, merge SHA and latest main belong in
Issue #3's fresh post-merge receipt. Require current baseline synchronization,
all three final-head checks success and a13-file candidate-only diff with
exactly one new packet before protected squash merge. Never infer success
from an earlier check run or a write request alone.

best_verified_candidate: none
best_verified_result: none
best_h2_candidate: exhaustive finite SAT census and realized ternary integer gap
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: finish final-head transport, then attack the all-placement ternary
coupling obligation. NONTERMINAL_CHECKPOINT; no background execution claim.
