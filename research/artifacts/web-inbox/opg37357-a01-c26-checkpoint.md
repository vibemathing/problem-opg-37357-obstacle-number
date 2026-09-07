# C26 root continuation checkpoint

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
PR: #31
Branch: web/attempt-opg37357-a01-c26-placement-bridge-growth-v1
Base: c299659f0c7f505a1e9739e6d8329fbde48c30ff
Head before checkpoint: 0e631460782ea3074dc498c1a58736178eeda9ca
Packet creation commit: cf6839e80030adf42d182ec6a963e71e7b510f0c
Actual PR binding commit: 0e631460782ea3074dc498c1a58736178eeda9ca
Target: obligation:opg37357-root
Harness 1.2.4 snapshot: 4181effe1481eb1454130d2d6c87a7c327ef84e39b28d051fc496870d08864d1

## Candidate proof and actual execution

C22 and C25 were reread at the base. C26 now gives the universal hypothetical
real-placement-to-C22-CNF implication, including compact free-component
regularization, GP replacement, W orientation projection, every signed clause
family, geometric loop erasure for crossed key paths, shared endpoints and
exact key-variable elimination. The 14-case degeneration atlas marks which
cases have executed controls and which are proof arguments only.

The new source-origin compiler uses a different path traversal and matches
EVERY C22 row and its complete DIMACS SHA-256. There are 540 variables and
69332 clauses: 420 four-point, 20160 five-point and 48752 key-path. The derived
origin table is reproducible by --origins, has 69332 rows/1530158 bytes and
SHA-256 666420da3374818cafa9fa8805acab65740c373e1fbb9ad3af01e5d12d4813f7.
It is not an additional oversized or duplicated repository proof file.

Actual final-source CPython 3.13.5 exact execution: 1736 Boolean elimination
cases; 5040+30240 determinant identities and 120 W projections; four positive
polygon controls; four numerical X4 controls; exact crossed/shared-endpoint
fixtures; 176 deletion-tree certificates and finite coloring controls.
Bounds: 35 CPU seconds, 40 wall seconds, 512 MiB, one mathematical process
and 4 MiB output. Exit code 0. A first GP test failed and its repaired final
source was rerun; execution.json preserves that distinction. The old C22 RUP
was NOT rerun this cycle and remains a separately frozen dependency. No
trusted mathematical execution, kernel proof or admission is claimed.

## Growth advance and ruled-out shortcut

Same-obstacle guards extend the necessary key-path CNF to h colors. At a
fixed orientation, the guarded key constraints admit h labels iff the graph
of opposite-key-path conflicts is h-colorable. This is a necessity interface,
not a placement-construction or realizability solver.

The new all-planar overlap lemma: different induced X4 copies share only a
clique. Proof: each copy is 4-connected and maximal planar; in an auxiliary
plane embedding, a vertex of another copy lies in a triangular face, whose
three boundary vertices would separate that copy if it extended outside.
Thus all shared vertices lie on that face triangle, so no nonedge is shared.
The resulting nonmonochromatic-copy-demand hyperedges are disjoint and admit
an explicit two-coloring. Therefore X4-copy-only demands cannot yield a
planar obstacle lower bound of three. This is a limitation of that relaxation,
NOT an upper bound of two for the actual graph. No protected failed-route
ledger is changed. Do not retry this shortcut by adding more identical blocks.

Amplification-capable candidate: t demands each requiring r labels yield
h>=ceil(rt/b) if each obstacle label can participate in at most b demands.
The ALL-PLACEMENT geometric capacity bound, or equivalent cross-demand
incompatibility, remains missing. The abstract Fano hypergraph is only a
finite coloring control and has no claimed planar obstacle realization.

## Exact remaining quantifiers and separate layers

T: C19 tube/Jordan and B17; not a premise of the new normal form or CNF bridge.
A: C20/C21 arrangement and C25 realized-signature interpretation; no fixed
negative drawing or abstract unverified sign table gives a graph lower bound.
P1: C26 universal clause bridge plus C22 frozen propositional contradiction,
X4 planarity and faithful connected-polygonal semantics; trusted gate open.
P2: exists h forall finite planar G exists placement with <=h obstacles,
or its negation forall h exists planar G forall placements requiring >h.
The constant X4 lower bound and the copy-only barrier do not settle P2.

next_obligation: force cross-block key-path conflicts or higher-rank empty
common-component sets for every realized placement, then prove a uniform
obstacle-capacity bound. Test proposed h=2 necessary systems before claiming
an amplification family. SAT of a relaxation is not a two-obstacle drawing.

## Frozen new files

Prefix: research/artifacts/candidates/opg37357-a01-c26-placement-bridge-growth-v1/
README.md
  9cbaf03bb94fdf7bd0c5f28ec1533770540407cfcefc87c5429b83e1e2725343
growth.md
  00ee415ad060be05d242897dfdb6ee41b02be61dc4e740040b5c0d1852d5545b
clause_bridge.py
  a1395be250d45f5476e2d9734736127486a1d66b608b96179f58692f23da855b
growth.py
  3fc815d746b9e5b2a1bc697a42ab0d8f4164b7a8ea1fb98d1a9bb91a9ea1be39
controls.py
  150709c9bdb0ebfeeb57f9857aaecd75837607cb54f61ad77d4b5eb1e33ca741
degeneracy-atlas.json
  2d4ca8edb38103f254cc0fab596f5bf36d996a9dbbff175dcde303bbbed4d6c0
observation.json
  9944852f3e0564bc89f86d0b7569185df3bdb83c0d70a9257b4ebb3a11a5a6fd
execution.json
  eba1aec821ad3632d9b72274f43a6a6435f955de5117088be1b51cb89d42eda2
research/artifacts/web-inbox/opg37357-a01-c26.packet.json
  e2ba91ccd20ca7d2218d47ad5ef9fc19f47724793cd1f8bf20ce9f3614cb098c
research/artifacts/web-inbox/opg37357-a01-c26-verifier-request.md
  1b7f7ed21d84db635fbfd53108a8a144f29f94ce96b075871581de6fc2cdf062

All eight candidate blobs match the actual locally hashed bytes. The packet
is bound to actual PR31. This checkpoint is written before final-head checks;
its own hash, final head, three check IDs, merge SHA and latest main belong
in the final Issue #3 receipt. Require synchronized base, all checks success
and full allowed-path diff review before protected squash merge.

The three new sources are delivered plain text without network, child-process,
dynamic-execution or file-access operations. Prior candidates are unchanged.
The original five C20 source byte strings remain unavailable; C21 is already
a delivered separate replacement and this did not stop root work.

The fresh verifier registry still provides fixture policies and no compatible
trusted invocation/closure receipt for the bridge or growth claims. The scoped
request is saved, not impersonated as a receipt. No EvidenceLink/Result/Solution,
workflow, schema, Harness, governance or truth ledger is modified.

best_verified_candidate: none
best_verified_result: none
best_fixed_drawing_candidate: C20 characterization and previously delivered C21 replay
best_placement_candidate: C26 full clause bridge with C22 frozen contradiction
best_growth_candidate: guarded color/capacity interface and X4-copy-only barrier
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
registered_failed_routes: empty at fresh base; new limitation is candidate-local
next_action: finish this final-head transport, then continue the cross-block
all-placement capacity obligation from the actual merged main. Root nonterminal.
