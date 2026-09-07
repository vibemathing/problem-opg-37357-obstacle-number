# C28 reconciliation of two implementation stacks

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Issue: #3
PR: #33
Base: f09892bdb8e26edcdfc80edacc2790de904a70ea

## Preserved records and what actually changed

The initial three-source package is guarded_cnf.py, second_check.py and
controls.py, with the existing C27 fiber.py dependency. Its execution.json
records the 2026-09-07T15:37:21.362471+00:00 run (exit 0, 2.135539 seconds).
That source and record remain unchanged. Its 32-variable octahedron formula,
15,952 projected models, original 12-corner analytical witness, realized
four-target ternary control, and precisely scoped saturated-ring failure
remain the original C28 results. README.md continues to describe that package.
The earlier nine-file manifest described that initial package, not every
later file added to the branch.

A full PR read then found five additional sources: guarded.py, exhaust.py,
audit.py, geometry_check.py and run.py. They were not part of the initial
execution. At pinned head 1ae96270bce27bae60e34ff482a7b81a54cbc791 they were
read in full, matched to their complete Git blobs, and audited as ordinary
finite mathematical code. They do not contain network, child-process,
dynamic-code, credential or repository-file-access operations. Their control
entry prints stdout. No source is removed or overwritten by this reconciliation.

The additional geometry_check.py is a direct polygon-boundary consumer,
NOT the blocked slab_geometry.py finite-segment decomposition source. The
blocked source was never retried under an alternate encoding/path/channel
and is not imported by either published runner. C27 Fiber remains the actual
finite-segment incidence dependency. The original safety-block record in
Issue #3 comment 5572877352 and execution.json is preserved.

## Separate actual replay of the concurrent extension

A new local run started at 2026-09-07T16:06:57.073885+00:00 on CPython 3.13.5
Linux, with exact Fraction/integer computation. It used 35 CPU seconds (36
hard), 40 wall seconds, 512 MiB address space, 4 MiB file output, and one
mathematical worker. It exited 0 after 10.048397 seconds. This is a new run,
not a rewrite of either another operation's run or the initial 2.135539-second
record. Frozen sources, import census, limits and compact results are in
reconciliation-execution.json, SHA-256
6f6546f7e030977d87864dbb8f2297b086087e246151d21b452e2b62a6daf6a2.

Reproduce from the C28 directory:

    PYTHONPATH=.:../opg37357-a01-c27-fiber-guard-gluing-v1 python -B run.py

Stdout is deterministic ordinary JSON, 23,830 bytes, SHA-256
8d085ef01516e6f20a278a98892a1d859105b3f9817bfb2dc196c6ddf80926f8.
Stderr is empty. This run imports the previously matched original
 guard ed_cnf.py (spelled guarded_cnf.py in the executable import), second_check.py
and unchanged C27 fiber.py alongside the five additional sources.
The spaced prose above is not another file or an alternate source payload.

Observed results:
- Shared-port diamond chain on six vertices: 36 variables, 1,430 clauses,
  21,248 extendible direction/color pairs; minimum direction/color words (0,7)
  in that stack's MSB-first convention. Direct checking accepts its two
  disjoint polygons with 4 and 7 vertices.
- Octahedron: 29 variables, 1,134 compact clauses, 15,952 projected pairs;
  minimum (0,0). The complete renaming/substitution from the original
  32-variable exact-one formula is checked. Direct checking accepts the
  extension's 26-boundary-vertex polygon. This is not the original 12-corner
  polygon and does not silently change its analytical assurance.
- All 23 indexed single-edge deletions of the two base graphs are SAT.
  The regenerated minima for these deletion cases are not claimed to carry
  polygon representations. They are models of a necessary system only.
- Sixteen corrupted formula-source or rotation records are rejected.
- Five shared-port-chain sizes m=3,4,5,8,16 pass direct polygon checking.
  A universal statement for every m requires the separate inequalities in
  two-coupling-extension.md, not extrapolation from this list.

The two labeling conventions are deliberately distinct. The initial package
uses two exact-one bits per target and little-endian words. The compact
extension uses one bit per target and MSB-first words. The octahedral full
formula equivalence is explicitly checked, not inferred from equal counts.

## Mathematical audit boundaries

All graph rotations certify abstract planarity only. No obstacle placement
is constrained to respect a plane embedding. The geometric first models
really satisfy their edge/nonedge visibility conditions. Consequently they
cannot be removed by any faithful extra common-component clause: an alleged
empty intersection for their used color class would be false.

The original C18 four-target control has two used labels with pairwise
compatibility but an empty monochromatic triple. Its six valid colorings
remain a fixed-drawing result. The extension's different abstract five-target
triple-only system is non-two-colorable, but no planar realization or
placement-universal forcing theorem is supplied for that system. These are
not interchangeable with C29's separately coordinated results and are not
claims about an unrestricted planar graph's obstacle number.

The current ring and shared-port-chain constructions do not yield a lower
bound three. Their exact failure scopes are given in README.md and the
extension manuscript. Neither scope negates all possible cross-module
constructions. The next growth obligation is an all-real-placement implication
for higher-order incompatibilities on a different simple planar family,
including its planarity, real-chart feasibility and common-component semantics.

## Candidate/transport boundary

This supplement introduces no second packet, no new PR and no duplicated
C19/C20/C21/C22/C25/C26/C27 source. Keep the single C28 packet and PR #33;
include the final complete file census and exact head in its checks and
checkpoint. Existing historical execution records retain their own scope.
A passing transport check, same-agent code diversity, this replay or a merge
is not a trusted mathematical receipt. No EvidenceLink/Result/Solution,
registry, workflow, Harness, schema or truth ledger is changed.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: reconcile the final one-packet manifest and head, complete normal
protected transport, then continue the all-placement ternary growth obligation.
