# Cycle c04 checkpoint

verdict: candidate_only
Issue: #3
PR: #7
branch: web/attempt-opg37357-a01-c04-normal-form-v1
base_revision: bcfec30feef427d950c3721fdad490647e318c2f
packet_commit_before_checkpoint: da818927b0325ba5fd9204d24b360b3e5c20c9b4
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg37357-a01-c04-normal-form-v1
route_status: active; formal replay and statement-faithfulness pending
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root

## Artifact identities

- research/artifacts/candidates/opg37357-a01-c04-normal-form-v1.md
  SHA-256: 5fc93064a9e6ded6305c0c6db7f19ae59a18674bce353aebd149b283a06d7d60
- research/artifacts/web-inbox/opg37357-a01-c04.packet.json
  SHA-256: 034fca2409d14cb42c52d697ee5d079c1d247754ff8d311744c29c1d75d538c8

## Progress and rejected shortcuts

The candidate replaces the at-most-m size disjunction by one exact-m GP-ALL formula, without duplicate corners. It simultaneously fixes two graph anchors and the ray using an invertible affine map, and gives the resulting vertical-ray polynomial. It also identifies an open strict-sign neighborhood producing rational coordinate witnesses. This is not a polynomial coordinate-bit bound or an NP-membership result.

Rejected shortcuts: duplicate padding; fixing a ray direction in unchanged coordinates; selecting a ray parallel to the anchor difference; using proper-only intersections without GP-ALL; dropping exterior membership or polygon simplicity; inferring a fixed rounding precision or polynomial-length certificate from rational density.

## Transport and verification

The packet contains the actual PR number and URL. At checkpoint creation the three required checks still need to be read on the new head containing this file; no result is predicted. No solver, compiler, kernel, or mathematical verifier has been executed. No protected record has been changed. Source references point to the prior frozen c01/c02 candidates, not new external claims.

## Next action

After actual candidate checks and merge, refresh main and produce a bounded deterministic SMT-LIB exporter for the normalized formula. Include strict input validation, explicit resource refusals, buffered output, real parity bits, cyclic adjacency tests, and exact small regression inputs. Keep invalid input and resource exhaustion distinct from a mathematical false formula. The exporter and proposed tests must remain candidate material until a separately authorized runtime executes them with recorded versions, limits, and exact inputs.

next_obligation: obligation:opg37357-bounded-polygon-encoding
