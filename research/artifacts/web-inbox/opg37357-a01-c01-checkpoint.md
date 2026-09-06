# Cycle c01 checkpoint

Verdict: candidate_only
Issue: #3
PR: #4
Branch: web/attempt-opg37357-a01-c01-closed-contact-v1
Cycle base: fae37538c3d7b76e3ea977c3c734b455146f357f
Packet commit before this checkpoint: 7633d2a330531c72417b9a8bdcfecb99e4f90d39
Harness: 1.1.2
Harness snapshot SHA-256: 1b616175accd4e6432c60d0bd0087350a8d5d18fee8b49e9809a071292109fde
ProblemContract SHA-256: 10fb03f159d4818c5141567a77390e1351fda77c9810ac45d66dd7d4e14aa4f5

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg37357-a01-c01-closed-contact-v1
route_status: active; candidate submitted; mathematical verification pending
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root

## Frozen artifacts

- research/artifacts/candidates/opg37357-a01-c01-closed-contact-v1.md
  SHA-256: 20636a040864566fdae24fe5466e7571e3f748d75bf627f7aa88ef525e8b354d
- research/artifacts/source-notes/opg37357-a01-c01-sources-v1.md
  SHA-256: 21408fb1d8d43bb621a678df5325c30ca06a95b3ca1122fd165e7dac2a3e8125
- research/artifacts/web-inbox/opg37357-a01-c01.packet.json
  SHA-256: ad887f9e89268cedf5d96ade781e59f9e7c62055c1624b77344f0f0097e79a5f

## Progress and negative knowledge

The candidate gives exact closed-contact primitives, a polygon simplicity specification, exterior membership using generic rays and real parity bits, and bounded-equivalence arguments for two explicitly separated general-position conventions. It includes seven exact hand-derived adversarial cases. Rejected simplifications include dropping exterior membership, using only proper crossings, omitting collinear interval bounds, allowing nonadjacent polygon contacts, letting a parity ray hit corners, requiring graph edges to be noncrossing, and padding with duplicate corners. These are candidate-local diagnostics, not entries in the protected failed-route ledger and not graph-level obstructions.

## Current blockers and transport state

No mathematical verifier has replayed this candidate. No Lean/SMT/CGAL run is reported. Three required GitHub checks still need to be read at the latest head after this checkpoint commit; their outcome is not predicted here. All PR fields have been populated in the packet. The source note's initially incorrect JGAA volume/pages were corrected from publisher metadata before merge. A local archive retrieval failed, so only connector reads were used for repository content; local hashing is bookkeeping, not verification evidence.

## Next action

After actual checks pass, merge this candidate PR and refresh main. Start a new immutable packet on the same admitted route/target. Audit arXiv:2206.15414v3, Section 3.1: its connected-graph minimal-representation bound gives at most 8n+15 corners when h=1. Its componentwise counting encoding is explicitly not a global obstacle representation, so this cannot be extended to disconnected graphs by merely concatenating component encodings. Check Section 5, Lemma 22, separately. A same-corner-budget GP-V to GP-ALL conversion remains to be supplied before transferring a cutoff between those conventions. No source theorem is treated as an admitted repository result.

next_obligation: obligation:opg37357-bounded-polygon-encoding
