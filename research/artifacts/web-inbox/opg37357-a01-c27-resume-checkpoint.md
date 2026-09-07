# C27 resumed diamond checkpoint

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
PR: #32
Branch: web/attempt-opg37357-a01-c27-fiber-guard-gluing-v1
Base: e358fe83f026715b0b6ddf868f84a58c3bdf91fe
Resumed head: 27be45a2de34eb886ebe3825c170b78dd97b8677
Head before this checkpoint: f9792c9221a5815c887c910fe86a28a9916570b4
Packet supplement commit: 6c1ab876f61108336e410d07a92fe0d174ed04b3
Target: obligation:opg37357-root

## Mathematical result and quantifier boundary

D3 consists of three induced diamonds sharing the same missing pair 01 and
otherwise private pairs 23,45,67. Its exact graph has n=8, e=15, thirteen
nonedges, including twelve cross-module pairs. Graph edges, rotation, face
cycles and a direct plane drawing are in diamond-result.json. This is the
private-pair minimum; with arbitrary nonhub identifications, the minimum is
K5 minus an edge on five vertices, not this eight-vertex graph.

A new generator, importing no C22/C26 core, emitted a 238-variable / 18278-
clause same-obstacle-guarded h=2 formula and every clause's source. Its least
model has precisely variables 58,60,...,82 true. The unfixed-direction DPLL
search and a separately written propagator checked its lexicographic first
model: 139 nodes, 100 units, no conflict leaf. All 8192 label allocations at
that fixed direction/side table pass. This is NOT a traversal of 2^238 truth
assignments or an exhaustive count of all realizable direction tables.

The least direction model has exact coordinates (i,-i^2). C27 fiber.py, reused
at its old digest, finds a common free component for all thirteen targets.
A separate explicit rational 16-corner polygon was directly checked against
all graph points/edge segments and all nonedge midpoints. The uniform proof
works for EVERY diamond book and, more generally, a two-nonadjacent-hub join
of a linear forest. It handles all cross-module nonedges. It does not use
C19's tube construction. Therefore the specific interface cannot yield an
all-placement lower bound of three; the SAT model is not just abstract data.

Allowing shared nonhub vertices but no extra edges gives four planar exact
three-diamond union types: outer 3K2, P3+K2, P4, or K3. All have one-obstacle
placements. A degree-three outer vertex would force a K3,3 subgraph. This
classification does not cover arbitrary extra coupling edges. The exact
failed-route proposal, not a protected-ledger entry, is in the ONE packet:
9345f07a534537926161b846d2cdd0c9c2d4a3dc7caf7865c4417e3bf2904d8e.

For three nonedges, empty triple intersection alone permits two components
whenever any pair intersects. At most four pairwise-compatible targets can
be paired into two components. The next genuinely rank-three target is five
nonedges with every triple intersection empty. All 32 two-color cases of
that abstract system were checked. No planar/all-placement realization or
root lower bound is asserted. This is the next open geometric obligation.

## Actual execution and replay gap

Final CPython 3.13.5 / Fraction runs used 30 CPU seconds, 40 wall seconds,
512 MiB, one worker and 4 MiB output. Observation, full CNF, full provenance
commands all exited 0; times and exact input/source/output hashes are in
diamond-execution.json. Nineteen graph/rotation/clause/origin/model/polygon
mutations were rejected; all 256 two-variable CNF databases were checked
against truth tables. The five-vertex minimum has 4096 literal full-variable
assignments checked, of which 528 satisfy its formula. Only that small test
is labeled literal exhaustive direction-and-label enumeration.

The first new diamond_core.py create_file request was blocked by the platform
and returned no commit; exact_sat.py and diamond_checks.py writes were then
not attempted. No alternate encoding, path, blob, splitting, tool or source
attachment was used. These three NEW executed source files remain unpublished:
 diamond_core.py 28d23fc41ff96183ad43d795504bca0560708cb5348c4c6dc99d11a9bfd5acea
 exact_sat.py 72487c01303e73eab96ecab1aafd6f23c7a2630655389aa1e84cf5ad70f17c19
 diamond_checks.py b13a90328193128e374df23db00af55bca7bf1ea9fc1034930e104de71efbd19
The complete new CNF and provenance caches were produced locally but are not
committed. No new checker release runnable from the repository alone is claimed.
Issue comments 5572736772 and 5572866621 preserve the source-publication gap.
The historical five missing C20 originals remain separate unavailable byte
strings; they are not retried or claimed recovered. The old seven C27 files
are unchanged; their recorded earlier executions are not reruns in this turn.

## New and revised path fingerprints

Candidate directory prefix:
research/artifacts/candidates/opg37357-a01-c27-fiber-guard-gluing-v1/
diamond-audit.md
 e5702cfde398e3d423ed616b13226cf5d3dca260baaae5f3285418401dace5ce
diamond-result.json
 3f9e30278e12b1a9342d35eb394ede74b5d3d4e74a2c97056d7ed778a675725a
diamond-execution.json
 870f98687766086c31d75e5fbe806f8b4309ae24668e06e1de12c4bbf4f5e1ff
research/artifacts/web-inbox/opg37357-a01-c27.packet.json
 7894745314ceb4c71db75f87774ba38a725bb01e9f42105e5808b7da2315fa4d
research/artifacts/web-inbox/opg37357-a01-c27-diamond-verifier-request.md
 32d4e1b657fc10e8572e0680dd56f7d0d1bce644e02025d64b9ae85c81cdb135

The revised packet preserves all seven original artifact bindings and actual
PR32 linkage, adds three non-executable objects and one failed-route proposal.
It does NOT claim absent source files as published candidate artifacts. The
old checkpoint remains a historical record; this file and the final Issue
receipt supersede its next-action/transport wording. The candidate proof had
one wording correction: its hub rectangle is between the hubs, not below
all graph points. No source algorithm or run changed for that correction.

## Final-head transport to perform

This checkpoint precedes final checks. Verify its resulting head on all three
required checks, compare main and inspect the full candidate-only diff with
exactly ONE new packet. There should be fifteen new regular files in this PR
relative to main, no modifications to previously merged candidates/protected
files. Merge only after successful packet, snapshot and diff gates. Then read
the actual main/merged PR/tree, and append all final IDs plus this file's hash
to Issue #3. Never reuse checks from the original pre-supplement head.

T/A/P1/P2 remain separate. No compatible trusted mathematical consumer or
closure receipt is registered; the renewed request is not Evidence/Result.
No workflow, schema, verifier, Harness, truth record or Solution is changed.

best_verified_candidate: none
best_verified_result: none
best_fixed_drawing_candidate: earlier C20/C21 and C27 fiber, distinct from root
best_new_candidate: uniform diamond/linear-forest one-polygon counterfamily
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_obligation: all-placement geometric five-target rank-three incompatibility
next_action: finish existing PR32 transport, retain explicit source gap, then
pursue the rank-three geometric invariant rather than repeating common-pair diamonds.
status: NONTERMINAL_CHECKPOINT
