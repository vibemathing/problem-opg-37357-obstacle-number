# Cycle c03 checkpoint

verdict: candidate_only
Issue: #3
PR: #6
branch: web/attempt-opg37357-a01-c03-global-cutoff-v1
base_revision: cc14e9659434d61b2d945ea0f5f59f15c0efdd0c
packet_commit_before_checkpoint: 14622bdbbb9b31b4a342ae5f82bd5c0e14f62a80
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg37357-a01-c03-global-cutoff-v1
route_status: active; geometric replay and statement-faithfulness pending
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root

## Artifact identities

- research/artifacts/candidates/opg37357-a01-c03-global-cutoff-v1.md
  SHA-256: 8a552e9ca7d743e8ed3571041d695882f478c2afdd5d6310b764998a46a58a65
- research/artifacts/source-notes/opg37357-a01-c03-global-sources-v1.md
  SHA-256: c12bb046176ae663986133dd9a30081c532dc25ef69ede2da237f1b1b16e88ba
- research/artifacts/web-inbox/opg37357-a01-c03.packet.json
  SHA-256: 09306bb2ccd28ab5359a814b2b9c6b53423a908768e5f00eab5cc23e77c4ad11

## Progress and negative knowledge

A single eligible free-space component now yields an embedded tree with N=2t-1+k vertices, then a simple polygon with at most 8N-4 corners. The resulting explicit bound is B(n,e)=8e^2+8*binom(n,2)+4, with no graph-connectedness assumption. The construction handles holes or nonpolygonal shape in the input connected obstacle by replacing it, not by asserting such shapes already satisfy the bounded formula. It retains disjointness from graph points and edge segments as a named convention.

The audit excludes arbitrary portals on blocked portions of supporting lines, omitted isolated-point punctures, intersecting or overlapping spokes, cyclic thickening, convex-hull shortcuts, and stationary nonedge witnesses during graph-point perturbation. These are candidate-local conclusions, not protected failed-route records.

Transport status at creation: the packet has the actual Issue/PR bindings. Required checks must be read for the new head including this checkpoint before merge; no outcome is predicted here. No solver, geometry library, kernel, or mathematical verifier was executed. The renewed PDF screenshot request failed; only text-based prior-art comparisons were used.

## Next action

After actual transport checks pass and this PR is merged, refresh main and start a new unique packet on the same target. Prove exact-m padding by inserting distinct ordered corners on a side and perturbing within robust margins, rather than duplicate-corner padding. Then normalize a generic ray to the vertical direction by an invertible affine change of coordinates, checking that two graph anchors can be fixed simultaneously. Isolate rational-witness existence from any unsupported polynomial coordinate-bit bound. These changes will prepare a smaller explicit formula exporter.

next_obligation: obligation:opg37357-bounded-polygon-encoding
