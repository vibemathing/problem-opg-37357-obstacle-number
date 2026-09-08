# NB9: the frozen nine-vertex edge expansion has a two-polygon counterplacement

Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Candidate: candidate:opg37357-a01-nb9-edge-expansion-v1
Repository: vibemathing/problem-opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph binding: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Base: d21e5e28613b18e6960a0ce68b0b3051356ac8b5
Issue: #3
Primary owner: math-proof, supported by bounded exact computation

## 1. Exact result and reuse

The ONE nine-vertex graph frozen in the supplied NB8 next-input has a rational representation by two disjoint closed filled simple polygons. Therefore it is not an obstacle-number-at-least-three candidate. No lower bound of two, minimum polygon-corner count, graph-order minimum or theorem for all nine-vertex graphs is asserted. No all-order-type census is claimed. An existential whole-graph counterplacement suffices to reject this particular universal lower-bound proposal.

MIN4/PR38 was fresh-read as already merged. The supplied 26+8 and remote 28+8 eight-vertex witnesses concern isomorphic graphs; the map from supplied NB8 labels to MIN4 labels is (4,1,3,6,0,7,2,5), checked against all edges. No old census, witness search, X4 proof, star/diamond/bipyramid/prism enumeration or original C20 source recovery is repeated. The nine-vertex graph is different, not a duplicate packet for those results.

The inherited full next-input SHA-256 is 057e3ff6ed7d7605157a2ce8d4046aff7a00cab268a54c617edd73a73ca6542c. input.json retains its exact graph, rotation, plane coordinates and operation, while omitting the already-supplied deletion-tree cache. Its own digest is separately recorded.

## 2. Frozen graph and abstract planarity

Vertices are 0 through 8. Complete edges:

    03 05 06 07 08 12 13 14 16 17 24 25 27 28 34 35 36 45 58 67 78.

Complete nonedges, in color-variable order:

    01 02 04 15 18 23 26 37 38 46 47 48 56 57 68.

This replaces NB8 edge02 with vertex8 adjacent to0,2,5,7. Degrees are 5,5,5,5,4,5,4,5,4. The exact input rotation has fourteen triangular face orbits, every one of42 darts once, and9-21+14=2. A separate actual check of all130 vertex deletions of size at most three found connected residual graphs. There are no leaves or two nonadjacent vertices dominating all others. These facts concern the abstract simple planar graph only; they do NOT constrain an obstacle drawing to a plane rotation.

All fifteen nonedges, not an adaptively selected subset, are tested. No theorem of capacity two for fixed targets is assumed. The MIN4 matching-concentration warning remains in force.

## 3. A complete rational geometric certificate

In vertex order use

    (14,-17), (-2,16), (16,-2), (-8,8), (8,13),
    (-20,1), (-3,19), (-12,-12), (4,1).

Every increasing vertex-triple determinant is nonzero. witness.json lists ALL24 exterior and6 interior polygon corners, not an image or an incomplete path. The first polygon is a band with a slit around the boundary of the finite segment complex. It is a disk, not a filled annulus with a hole silently removed. The second polygon is an inset of a bounded face; convexity is NOT assumed. The file also gives one exact parameter0<t<1 and strict interior hit for every nonedge.

Assigned obstacle indices, in the above nonedge order, are

    1 0 0 0 1 1 0 0 1 0 1 1 0 0 1.

The direct consumer polygon_verify.py imports neither the construction nor an arrangement/CNF library. Its actual checks cover261 nonadjacent same-polygon side pairs,630 graph-edge/polygon-side pairs,144 cross-obstacle side pairs, all18 graph-point exclusions and all15 strict hits. Adjacent sides may meet only at their common endpoint, with no overlap; all other contacts are rejected. Ray winding uses exact rationals and distinguishes boundary membership.

Why these finite predicates prove the candidate statement: each checked boundary is a simple polygonal Jordan curve of positive signed area. Its filled bounded region is a disk. A graph edge has exterior endpoints and is disjoint from the entire boundary; were it to enter the bounded component, its continuous segment would first hit that boundary. Thus the WHOLE closed edge avoids the filled obstacle. Each listed interpolation point is in the bounded interior and blocks its nonedge. Disjoint boundaries and exterior sample points rule out nesting of the disks. Consequently the two displayed disks represent exactly the graph. No completeness assumption about the arrangement or a SAT solver is needed for this upper witness.

The local margin computation additionally produced630 edge/side and234 hit/side strict-separation certificates, all checked by verify_margin. One simultaneous L-infinity bound is eta=1/155648. Keeping both obstacles fixed, moving each endpoint by less than eta preserves all edge visibility and nonedge hits at the SAME interpolation parameter. For a projection normal v, a point moves in projection by at most eta*||v||_1; the verified gap is larger. Vertex separation is also checked. This is a positive-clearance argument, not density alone. Margin-generation source publication is blocked as detailed below; the direct polygon result does not depend on that auxiliary numerical margin.

## 4. Compiler extension and resource boundary

The supplied NB8 compiler had n<=8 and at most12 targets. The extension admits n<=9 and at most15 targets, with caps2000000 raw clause attempts,250000 canonical clauses,14000 paths per target and20000 total paths. Exceeding a cap is an error, NEVER UNSAT. The loops are finite: internal-vertex permutations have length at most n-2; paths have at most n-1 edges; all tuple and target-pair loops have explicit finite domains. The separate consumer uses breadth-first simple-path extension and a different orientation-parity expression.

The polygon consumer already admits5<=n<=16 and at most128 corners per polygon. Its predicate domain did not need to be silently enlarged for n=9. This cycle does not claim an execution of the earlier existential-real polygon compiler.

For this graph the complete formula has84 orientation,15 color and210 ordered-pair side variables:309 total. It contains128148 clauses (252 four-point,10080 five-point,117816 guarded key rows), from ALL5208 simple paths through eight edges. Every canonical row has a tuple or actual target-pair/path/mode/color origin. Both complete row sets and all origins agree.

For each original necessary path row K, same-color guarding is

    (z_s OR z_t OR K) AND (not z_s OR not z_t OR K).

The same side variable serves every path for one ordered target pair. Four-point and five-point rules are retained globally. C26/C27's necessity is reused: connect finitely many assigned hits inside the obstacle's OPEN free component, regularize inside a uniform positive clearance, then choose vertex general position. Opposite key paths give a graph-edge Jordan curve separating the two target segments; a path in a common free component would have a forbidden first exit. This is a necessary implication for actual placements, not sufficient realizability of arbitrary direction bits.

Thus the geometric quantifier is

    exists p, exists U0,U1 in components(R^2 minus K(p)), exists z,
    forall nonedges s: U_(z_s) meets the relative interior of s.

The components belong to the SAME p. One color has one component for its entire target class. Unused colors and repeated components are permitted. Coordinates and all nonedge hits precede the Boolean abstraction. Crossed graph edges are allowed throughout.

Full emitted DIMACS:5187269 bytes, SHA-256
6ee78d2b5fe1e5bfb2e4e79f9fa0b5ee8460fd2724db5dd2ba8a1fec7b90f199.
Full emitted row-origin JSONL:5730135 bytes, SHA-256
0702dd8e7c97ee74211394eb3f8a8591babc19e59317c8bd614017d8d891afad.
These are reproducible caches, not oversized repository files. The two source parts concatenate in a then b order.

## 5. Fixed incidence, whole-color intersections and anchored constraints

The local exact planarization observed46 free components. fixed-incidence.json freezes all fifteen incidence sets and the witness-byte binding. This data is not a list of components allowed to vary independently of p. Generic incidence reconstruction source was blocked; delivered interface replay explicitly reports geometric_completeness_replayed=false. The data's geometric completeness is a SEPARATE candidate layer, not an assumption needed for the direct polygon witness.

At the displayed coordinates, all32768 labels were considered after exact side-variable elimination. Clause residual forcing agrees with a separate path-local forcing derivation. Exactly two labels survive. Adding two one-hot component selectors and84 direction units gives401 variables and130334 clauses. Finite truth masks account for all32768*46^2=69337088 valid label/component cases; all2116 component pairs are visited. The two solutions are

    label code19761, components(0,22);
    label code13006, components(22,0).

Codes use target index i as bit i. Both full Boolean witnesses are regenerated by replay.py interface and checked against every joint clause. This is ONE fixed direction/coordinate input, NOT2^84 directions, all realizable order types or the full coordinate space. No lexicographic minimum over all direction tables is asserted.

All32767 nonempty target subsets are covered by the minimal-core extraction. Its51 inclusion-minimal empty intersections are ALL pairs. There is no additional nonredundant ternary Helly cut in this model, and no spurious relaxed label left to eliminate. Adding a cut that rejects either actual polygon assignment would be unsound.

For anchor u put M_u={s:u not in J_s} and R_u=intersection_(s in M_u) J_s, with empty intersection equal to all components. A two-cover exists iff some R_u is nonempty: u covers its hit targets and a v in R_u covers everything u misses. The stored table gives R_0={22}, R_22={0}; the other44 anchors have empty cores. These anchor sets are computed AFTER the placement and may change with it. No universal rank-three bound or universal anchor obstruction follows.

## 6. Execution, publication and exact stop boundary

Actual CPython3.13.5 executions use integer/Fraction predicates. Per command:30 CPU seconds,40 wall seconds,512MiB address space, one worker,8MiB regular-file limit. Actual stdout sizes and hashes are recorded; the two provenance parts are each below3MiB. No GPU, Lean, SMT, RUP replay or registered mathematical-verifier run is claimed.

The original local geometry/margin audit rejected20 mutations. The delivered replay entry actually reran13 geometry mutations and four clause mutations (omitted row, removed guard, flipped direction, invalid path). An extra local trailing newline was reconciled against the real remote Git blob before the exact-byte audit and selector were rerun. One outer multi-command wall limit interrupted provenance transport bookkeeping; the missing second part was rerun alone and its concatenation verified. No timeout was interpreted mathematically.

Two ordinary create_file calls were blocked by indeterminate platform safety, with NO commit: plane_with_outer.py and margin_build.py. Their executed SHA-256 values are recorded in source-reuse.json and the verifier request. They were NOT retried under another name, encoding, blob, channel or attachment. replay.py imports neither. Direct polygon checking, full CNF generation/audit and supplied-set selector replay ARE delivered. Generic geometric-incidence reconstruction and generation of the auxiliary margin certificate are NOT repository-only replay surfaces. The blocked source is not an admission blocker invented from an old profile label.

Run from this directory, under the external bounds above:

    python -B replay.py polygon
    python -B replay.py audit
    python -B replay.py interface
    python -B replay.py mutations
    python -B replay.py guard
    python -B replay.py omit
    python -B replay.py flip
    python -B replay.py path
    python -B replay.py cnf
    python -B replay.py origins-a
    python -B replay.py origins-b

Only one frozen nine-vertex structure was screened. Failed numerical placements were finite probes, not order-type shards certified infeasible. There is no survivor to which an all-placement UNSAT theorem must now be attached: the WHOLE graph already has the displayed counterplacement. Unvisited realizable regions remain unenumerated but cannot rescue its proposed obs>=3 conclusion. The exact graph-level obstacle number one versus two is unresolved.

The failed-route proposal excludes only this graph and its isomorphic relabelings as an obs>=3 candidate. The next atomic step is a different isomorphism class after structural/template filtering, or a separately proved representation-preserving expansion lemma. Do not repeat this nine-vertex search, the NB8 census, or the prohibited bipyramid/diamond/prism families. T (polygon topology), A (incidence completeness), P1 (old X4 chain), and placement-universal growth stay separate.

best_verified_result: none
best_verified_candidate: none
root_obligation: open
statement_faithfulness: pending
trusted_closure: none

A compatible registered mathematical consumer and closure receipt have not been obtained. No EvidenceLink, Result or Solution is signed by this candidate generator. GitHub checks and merge, if successful, are transport only.
