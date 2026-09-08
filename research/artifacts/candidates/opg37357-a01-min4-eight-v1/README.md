# MIN4: the first non-bipyramid four-connected triangulation has a two-polygon counterplacement

Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Candidate: candidate:opg37357-a01-min4-eight-v1
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph binding: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Primary owner: math-proof, with bounded exact computation
Execution and initial transport base: 1a5eefd266401b903f15de10c07b3aff7d3f9773
Issue: #3

## 1. Result and limits

The eight-vertex graph G below is the first non-bipyramid four-connected maximal planar graph, up to isomorphism and within an exhaustively checked order range n<=8. It has an explicit rational representation by TWO DISJOINT FILLED SIMPLE POLYGONS. Every edge and every nonedge is checked, not just five selected targets. This is a counterplacement to a proposed obstacle-number-at-least-three claim for G; no lower bound of three survives this screen. The exact obstacle number of G is not decided.

A separate all-graph lemma identifies a flaw in one stronger target formulation: if a fixed target set contains a matching of q nonedges, then some rational general-position placement has one free component meeting all q. Thus fixed targets containing a three-edge matching cannot satisfy a placement-universal capacity bound of two. This does NOT say that the whole graph has a one-obstacle representation: its other nonedges need not be blocked in that concentration construction. Adaptive targets chosen AFTER a placement are a different quantifier order.

No all-order-type enumeration, unrestricted root closure, trusted mathematical receipt, EvidenceLink, Result or Solution is asserted. A complete existential counterplacement suffices to dispose of this selected graph; there is no survivor requiring a universal impossibility proof in stage two.

## 2. Frozen graph and five targets

Vertices are 0,...,7. Complete edges:

    01 03 06 07 12 13 15 16 24 25 26 34 35 37 45 46 47 67.

Complete nonedges, in CNF variable order:

    02 04 05 14 17 23 27 36 56 57.

The five targets were frozen BEFORE placement screening:

    02 14 27 36 57.

The original selected.json byte digest is
 d13296c5d367a9cd09aaeb2805d833c631d9fd242d5389b3f4208e59781f2a54.

A cyclic rotation is:

    0: 1 3 7 6
    1: 0 6 2 5 3
    2: 1 6 4 5
    3: 4 7 0 1 5
    4: 2 6 7 3 5
    5: 3 1 2 4
    6: 7 4 2 1 0
    7: 3 4 6 0.

The predecessor-of-reversed-dart face rule gives twelve triangular faces and 8-18+12=2. The consumer checks all 36 darts. Deleting each of the 93 vertex sets of size at most three leaves a connected graph. Minimum degree is four, so connectivity is exactly four. Degrees are four copies of 4 and four copies of 5. In particular there is no pair of nonadjacent vertices of degree n-2=6. There are no leaves, degree-three ports or ordinary two-hub structure.

These rotations certify ABSTRACT planarity. The obstacle drawing is allowed to cross graph edges and is not constrained to this rotation.

## 3. Exhaustive small-order structural selection

For a four-connected maximal planar n-vertex graph, e=3n-6 and minimum degree>=4. Its complement has (n-3)(n-4)/2 edges and maximum degree n-5. We exhaust n=5,...,8; smaller graphs cannot be four-connected under the usual nontrivial connectivity convention.

The producer uses NetworkX 3.6.1's atlas through seven vertices. For n=8 it removes a vertex of the complement: every remaining seven-vertex complement has degree<=3. Every possible new neighborhood of size 0..3 giving ten complement edges is tried. There are 584 such extensions and 64 nonisomorphic complement representatives. This is not an order-type search.

A separate STANDARD-LIBRARY consumer removes dependence on atlas completeness and graph-library planarity decisions. It enumerates every nondecreasing degree sequence in the stated complement domain. At vertex i it chooses every subset of later positive-residual-degree vertices of the required size, fixes those edges, and decrements residual degrees. Negative residuals, odd remaining sum and a degree exceeding the number of other positive-residual vertices are necessary impossibilities, so pruning loses no graph. The recursion strictly increases i and terminates at n. Relabeling any graph in degree order puts it into this enumeration.

For each published complement representative, the consumer enumerates all permutations within equal-degree groups. Their orbit sets are disjoint and their union equals the independently enumerated labelled set. Each representative carries either (a) a separator of size<=3, (b) an explicit K5 or K3,3 subdivision using only its graph edges, or (c) a sphere rotation and exhaustive deletion check. Subdivision paths are reconstructed by suppressing degree-two vertices and checked for complete edge use. Thus exclusions are certificates, not unchecked library Booleans.

Results:

 n  sorted-degree labelled complements  representatives  four-connected triangulations  non-bipyramids
 5                 0                         0                       0                       0
 6                15                         1                       1                       0
 7               237                         6                       1                       0
 8             12102                        64                       2                       1

The two eight-vertex admissible graphs have different degree sequences, so they are not isomorphic. If two nonadjacent vertices dominate all other vertices, deletion of those two leaves a connected residual graph. Its edge count is n-2 and every residual degree is at least two, hence it is a cycle: exactly the ordinary bipyramid template. Those cases are FILTERED structurally; their obstacle constructions are not re-enumerated.

The minimum is a structural minimum, not a claim that no known theorem elsewhere gives this graph two obstacles. Earlier stars, diamond books, leaf-port formulas and the 27 prism completions were not searched again. The current C31 tetrahedral graph has degree-three ports and does not meet this selection criterion.

## 4. Complete necessary CNF and the fixed-drawing selector

Freeze F(p)=R^2 minus all graph points and CLOSED graph-edge segments, and let J_s(p) be the components meeting the relative interior of nonedge s. The exact two-connected-obstacle existence interface is

 exists p, exists U0,U1 in components(F(p)), exists z:nonedges->{0,1},
 forall s: U_(z_s) is in J_s(p).

The whole color class must use ONE component. Unused labels and repeated components are allowed. These components belong to the SAME coordinates p; they are not free abstract sets.

The necessary guarded CNF reuses C26/C27's geometric implication. For a hypothetical representation, first connect finite hits within their open free component, use positive distance to the compact forbidden set to thicken them, and preserve the fixed interpolation parameter of every hit under one sufficiently small simultaneous movement of all graph points. Only THEN choose general position. Density alone does not preserve tangencies. Opposite key paths enclosing one nonedge and excluding another yield a Jordan first-exit contradiction for a path in their common free component. The obstacle itself need not be path-connected.

Orientation variables 1..56 are the increasing triples. Color variables 57..66 correspond to the listed ten nonedges. Side variables 67..156 correspond to all ordered distinct nonedge pairs. For each original key-path clause K, use

 (z_s OR z_t OR K) AND (not z_s OR not z_t OR K).

Exactly when the colors are equal is the appropriate clause active. All four- and five-point determinant rules are retained. ALL 1502 simple nonedge paths, through seven edges, are retained. The complete formula has 156 variables and 31676 clauses: 140 four-point, 4480 five-point, 27056 guarded key rows.

The source consumer uses breadth-first path extension rather than the producer's internal permutations, and a different parity expression. It rebuilds the complete canonical clause set and every tuple/path/color/mode origin. The two modules are reused, with explicit provenance, from the already supplied BIP2 helper; this is not a new proof of C22 or a claim of a different verifier trust domain.

At the frozen rational placement below, all 1024 labelings were evaluated with exact side forcing. Only two survive; they also satisfy the complete component selector. With 36 actual free components, the selector adds 72 one-hot bits and 1282 clauses. Adding 56 fixed direction units gives a 228-variable,33014-clause formula. Integer truth vectors account for all 1024*36^2=1327104 valid one-hot label/component choices. The two models are

 colors 0 1 1 1 0 0 1 1 0 0, components (0,12);
 colors 1 0 0 0 1 1 0 0 1 1, components (12,0).

This is a FULL fixed-drawing calculation, not an enumeration of the 2^56 direction assignments or all real placements. The global necessary formula is SAT because the recorded real model satisfies it.

Actual generated cache digests:
 CNF: 59b3e5af71df569218572cf40fc4b8a30d4844235360a717004fb63f9f7a1f74
 all row origins: 13655d9e4ca0c58904b058d2408e1533d726a56e2e3821a6bd327f1b6fc310c3
 fixed selector CNF: c3fe41e4af885df84e2f0852ca79fd24939478c256f59e71623e5e4ef0dabb87.

The three caches exceed the repository's single-file limit. The published emitters reproduce them byte-for-byte; the full caches are also retained in the local replay archive. They are not falsely listed as additional GitHub files.

## 5. Complete rational counterplacement

In vertex order, take

 (-5,-1), (-5,-7), (-4,12), (-12,9), (12,16), (15,12), (16,3), (-3,-8).

All 56 vertex triple determinants are nonzero; a vertical pair line is permitted. The concrete polygons have respectively 28 and 8 corners and are listed in FULL in witness.json. The second is convex; the first is an exterior corridor, not a convex polygon.

For reproducibility, the exterior polygon is the boundary of the union of L-infinity tubes of halfwidth 1/4096 along a three-sided box chain

 (-32,-32)--(-32,32)--(32,32)--(32,-32)

and five explicitly recorded witness-to-corner connectors. The interior polygon is the convex hull of its assigned nonedge witnesses plus the same small square. tube_union.py splits all rational boundary intersections, classifies both sides of every elementary segment exactly, and requires one nonbranching simple boundary cycle. build_witness.py reproduces the frozen corners and hits exactly. This algorithm is a candidate producer, not a trusted theorem of offset correctness.

The stand-alone witness_check.py imports neither the producer nor an arrangement/CNF library. It verifies all polygon vertices, nonadjacent closed-side pairs, signed orientation, graph-point exclusion, graph-edge/boundary separation, strict nonedge interpolation hits and disjointness of the two filled disks. A graph edge with exterior endpoints and no boundary intersection stays exterior by the Jordan polygon theorem; a listed strict interior hit blocks its nonedge.

The actual consumer checked 370 nonadjacent same-polygon side pairs,648 graph-edge/obstacle-side pairs,all16 graph-point exclusions,224 cross-obstacle side pairs and all10 strict nonedge witnesses. The fixed five targets have loads two and THREE in the two obstacle components: targets14,27,36 all meet the interior component. Thus the proposed fixed-target capacity-two assertion fails directly on a complete two-obstacle representation of this graph.

For every graph-edge/obstacle-side pair the consumer also supplies an exact separating projection. Gap divided by the L1 norm of the projection bounds allowable L-infinity movement. For every nonedge hit it checks positive separation from every obstacle side. Including a quarter of the minimum vertex separation gives one simultaneous bound:

 eta = 1/16384.

Keep both polygons fixed. Moving every graph point by L-infinity distance <eta preserves graph-edge boundary separation, exterior graph points, distinctness, and all nonedge hits at their SAME interpolation parameters. The witness is therefore robust, not a boundary-only coincidence. This is an open region of successful representations; it is not a covering of all order types or degeneracies.

The first successful placement was index52 among53 actually tested layouts of this SINGLE graph (two deterministic curves followed by fixed-seed rational point sets). probe-records.json preserves the tested coordinates and outcomes. Unsuccessful layouts are not graph-level impossibility results. No second graph was silently substituted after the five targets were frozen.

## 6. A useful universal obstruction to fixed-target capacity proofs

Lemma (candidate). For any finite simple graph G and any matching M of q>=1 NONEDGES, there is an injective rational general-position placement and a closed square disjoint from every graph point and graph edge, meeting every member of M in its interior. Hence one genuine free component meets all q targets.

Proof. Enumerate matching pairs a_i b_i, i=1,...,q. Put
 p(a_i)=(1,i), p(b_i)=(-1,-i).
For each remaining vertex w_j, j=0,...,n-2q-1, put p(w_j)=(2,2q+2j+1). All points are distinct. Let B=2n+1 and eps=1/(8B).

A graph edge with endpoints of the same x sign stays in x>=1 or x<=-1. For an edge joining opposite x signs, its endpoint determinant is a nonzero integer: between matching endpoints it is i-j, with i=j excluded because that pair is a nonedge; for a remaining vertex and b_i it is the odd integer 2q+2j+1-2i. Thus the graph-edge supporting line has absolute value at least1 at the origin. Its normal has L1 norm <=3+2B<=4B. Across [-eps,eps]^2 its affine value changes by at most4B*eps=1/2, so the whole line misses the square. Every matching segment contains the origin at parameter1/2. Graph points are outside the square.

To obtain rational general position without losing these properties, put delta=eps/(4n^2), and perturb vertex k by t*(k,k^2). For any triple the determinant is a polynomial of degree at most2 in t with a NONZERO quadratic coefficient, a Vandermonde determinant. Each triple excludes at most two t values. Among the 2*binom(n,3)+1 distinct positive rationals t=delta/(j+1), some avoids all exclusions. Each endpoint moves by less than eps/4. Same-sign edges retain their x separation; on an opposite-sign edge's ORIGINAL separating line the extra variation is at most4B*eps/4=1/8, still below the original slack. Matching midpoints remain strictly inside the fixed square. This proves the lemma with a finite terminating choice rule, not density alone.

matching.py actually constructs and checks this for the selected matching02,14,36, using all eighteen graph edges. It explicitly does NOT claim that the other seven nonedges are blocked by that square. The all-graph proof does not depend on planarity, the current graph, C19, or numerical sampling.

Consequence: for fixed targets S containing a matching of size3, the assertion

 forall placements p, forall U in components(F(p)), |{s in S:U in J_s(p)}|<=2

is false. More generally a capacity b cannot be universal if S contains a nonedge matching of size b+1. Restricting only to placements already known to represent the WHOLE graph is an additional hypothesis, not something the matching lemma silently supplies. A target choice S(p) AFTER p is also not excluded by this lemma. These distinctions are essential to the next route.

## 7. High-order extraction and next obligation

The frozen counterplacement has one inclusion-minimal empty triple: targets02,36,57 (indices0,7,9 in the full nonedge list), as well as21 pair cores. The triple is minimal as a set-system exclusion, but adds NO new rejection to this drawing's full guarded-CNF label models: both already use two common components correctly. It cannot honestly be presented as a new graph-level cut. Different rational placements supplied by the matching-concentration lemma also show why an unguarded version cannot be universal.

There is no surviving graph in the exhausted non-bipyramid n<=8 structural domain. The new geometric witness template is one bounded convex free cell plus a connected exterior corridor, verified on this selected graph only. It is not a two-obstacle theorem for all four-connected triangulations.

The next atomic step is order9 or a stronger structural family, after the same structural filters. Before claiming a fixed five-target capacity proof, reject target sets containing a three-edge nonedge matching. Prefer the already defined placement-dependent anchored empty-intersection interface when fixed targets cannot work. For any surviving graph, all realizable sign regions and degeneracies must still be covered; no fixed rotation or one unsuccessful drawing supplies that quantifier.

## 8. Execution, provenance and admission

Final runs use CPython3.13.5, Fraction/integer arithmetic, NetworkX3.6.1 only in the structural PRODUCER, and externally enforced per-command30 CPU/40 wall seconds,512MiB address space,one mathematical worker,4MiB output. The structural consumer, polygon consumer and clause consumer are separately implemented standard-library modules. This diversity is not a separate trusted verifier identity. Twenty mutations are actually rejected: ten geometry/data, five clause/guard/path and five structural certificate mutations.

Reproduction (within this directory):

 python -B enumerate_small.py
 python -B structure_audit.py < structure.json
 python -B replay.py < witness.json
 python -B replay.py cnf < witness.json
 python -B replay.py origins < witness.json
 python -B replay.py fixed-cnf < witness.json
 python -B mutations.py geometry < witness.json
 python -B mutations.py clauses < witness.json
 python -B mutations.py structure < structure.json

Apply the resource bounds externally. Sources use ordinary text, standard arithmetic and JSON stdin/stdout; no credentials, network, subprocess creation or dynamic execution. NetworkX's atlas read occurs only in enumerate_small.py. Earlier optional public-file download attempts failed; no permission or safety boundary was bypassed, and no planner execution was invented. The exact CPU route and those diagnostics are recorded separately.

Code provenance: guarded_cnf.py and clause_audit.py derive from the supplied R06_BIP2_candidate_bundle.zip helpers; incidence.py derives from the supplied C28 extension's rational planarization, not C27's fiber core. Their algorithms are reused, not claimed new discoveries. The fresh structural certificates, selected graph screen, polygon construction/consumer and matching lemma are the new objects. Earlier source artifacts and failed-route ledgers are unchanged.

Primary implementation documentation consulted: NetworkX graph_atlas_g, version3.6.1, https://networkx.org/documentation/stable/reference/generated/networkx.generators.atlas.graph_atlas_g.html . plantri documentation was consulted but plantri was NOT installed or run. No external graph dataset is needed by structure_audit.py's exhaustive degree-sequence check.

T=C19 tube/Jordan, A=complete incidence, P1=X4 and P2=unrestricted growth remain distinct. The direct polygon counterplacement does not rely on T or on incidence correctness. The necessary CNF still needs its inherited geometric faithfulness; the graph counterexample does not depend on UNSAT. The registered fixture policies are not a compatible trusted closure receipt. Nothing here modifies or signs Evidence/Result/Solution.

best_verified_candidate: none
best_verified_result: none
root_obligation: open
status: NONTERMINAL_CHECKPOINT
