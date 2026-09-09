# NEXT9: the next canonical class and a cap-assisted expansion lemma

Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph binding: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Base: 3e135c3af759b6471f21ae053474b5b1196921bf
Issue: #3
Primary owner: math-proof, with bounded exact computation

## 1. Outcome and selection scope

One new isomorphism class was screened. It is the nine-vertex four-connected maximal planar graph with degree sequence 4,4,4,4,4,5,5,6,6 and degree-preserving canonical adjacency word 000101110011011101101011100011011110. The first tested coordinates have two explicit disjoint filled simple polygon obstacles (34 and 5 corners). Thus this graph and its isomorphic copies cannot witness obstacle number at least three. Obstacle number one versus two is NOT decided.

The same witness instantiates a conditional representation-preserving edge-expansion lemma: insert one point, then add a four-corner cap to one obstacle along a proper boundary interval. The lemma has explicit visibility and local separation premises. It does not assert that arbitrary four-connected triangulation expansions preserve two-obstacle representability.

Prior MIN4 and NB9 work is not repeated. The order-at-most-eight structural classification is a reused MIN4 dependency. At order nine the complete catalog below has four four-connected classes. The ordinary bipyramid and the already represented NB9 class are excluded by exact isomorphism/canonical code. Among the two remaining classes we select only the first in ascending sorted-degree-sequence and adjacency-word order. The other class is not searched. The known exterior-band/interior-convex template has no supplied universal theorem covering every such graph: we filter previously certified classes, not infer an upper bound from visual similarity.

## 2. Complete finite structural catalog

selection.py generates the legal single-edge flip closure of a nine-vertex spherical triangulation. It uses NetworkX 3.6.1 only as a producer. Fifty abstract classes and 667 legal flips are recorded. The catalog is ordinary tab-separated text: upper-adjacency word, rotation at every vertex, and a first separator of size at most three or '-'.

closure_check.py uses only the standard library. It reconstructs every edge set, checks all spherical triangle faces and every dart, canonicalizes over ALL permutations preserving sorted degree classes, and checks each legal flip. It also verifies the induced face correspondence to the target rotation, up to one global reversal, so abstract isomorphism does not silently lose embedded information. Every flip stays inside the catalog. Connectedness and all vertex deletions of size at most three are recomputed.

Completeness uses the spherical flip-connectivity theorem (Mori, Nakamoto, Ota, 2003, Theorem 4; the primary source is identified in the source note): any two simple spherical triangulations of fixed order are connected by legal flips, up to embedded isomorphism. A nonempty catalog closed under every legal flip therefore contains every class. This theorem is about ABSTRACT embeddings, not fixed Euclidean point sets or obstacle drawings. The consumer checks 667 embedded correspondences directly; it need not assume an unchecked graph-isomorphism mapping respects rotation.

The four four-connected degree sequences are:

- 4^7 7^2: ordinary bipyramid, excluded structurally;
- 4^5 5^2 6^2: THIS selected graph;
- 4^4 5^4 6: still untested here;
- 4^3 5^6: prior NB9 graph, excluded by isomorphism.

The claimed minimum is relative to the prior MIN4 coverage and this complete n=9 catalog, not a new survey of all known obstacle representations. No n=10 graph is selected.

## 3. Frozen graph and targets

Vertices are 0,...,8. All 21 edges are

    04 06 07 08 14 15 17 18 23 25 26 28 35 36 37 47 48 57 58 67 68.

All 15 nonedges, in Boolean color order, are

    01 02 03 05 12 13 16 24 27 34 38 45 46 56 78.

The five targets frozen before screening are 01,02,03,05,12. Their matching number is two, so the previous three-edge-matching concentration shortcut does not already exclude this target set. Nevertheless, the actual representation puts four of these five targets in the exterior obstacle. Thus their proposed universal component capacity two fails directly on a WHOLE-GRAPH representation.

The rotation is

    0: 6,8,4,7       1: 4,8,5,7       2: 3,5,8,6
    3: 2,6,7,5       4: 0,8,1,7       5: 1,8,2,3,7
    6: 3,2,8,0,7     7: 5,3,6,0,4,1   8: 5,1,4,0,6,2.

It gives fourteen triangular faces and 9-21+14=2. All 130 deletions of at most three vertices remain connected. Maximum degree six rules out the prohibited nonadjacent dominating pair. Rotation is never used to restrict a hypothetical obstacle placement.

input.json was frozen before screening with SHA-256 d0411f531a97722693015c5d0481ce0671aeeb1711496b80b4aaf5b148929f62. Its full complement remains in every test; five targets are not substituted for whole-graph visibility.

## 4. Complete rational upper witness

Set p_i=(i,-i^2), i=0,...,8. Every increasing triple determinant is -(j-i)(k-i)(k-j)<0. Parallel supporting lines and nonvertex concurrence are allowed: no stronger coordinate atlas is assumed.

witness.json contains EVERY corner of a 34-corner exterior slit band and a 5-corner interior convex polygon, and strict interpolation hits for every nonedge. It is not a ring whose hole is silently filled. In color order the obstacles are

    0 0 0 1 0 0 1 0 1 0 1 0 0 0 0.

The reused, byte-pinned NB9 polygon_verify.py imports neither the constructor nor an arrangement/CNF implementation. It checks 532 nonadjacent same-polygon side pairs, 819 graph-edge/boundary pairs, 170 cross-obstacle side pairs, every graph-point exclusion and all fifteen strict hits. Adjacent sides cannot overlap. Boundary disjointness and exterior sample points rule out both contact and nesting of the two filled disks.

Why this is a proof candidate about filled obstacles: each verified polygonal boundary is a simple Jordan curve. Its filled bounded component is a disk. A continuous graph segment with exterior endpoints cannot enter that component without a first boundary hit. The exact closed-segment tests prohibit that hit. Every listed strict interior interpolation point blocks its nonedge. Thus the polygons represent exactly the frozen graph, independent of arrangement completeness or CNF sufficiency.

A uniform positive movement margin exists without appealing to density: take the minimum over the finitely many positive distances between closed graph edges and obstacle boundaries, strict hits and their obstacle boundaries, and distinct graph points. Choose eta smaller than one quarter of this minimum. Endpoint moves below eta move every entire edge and every fixed-parameter hit by at most eta. Boundaries remain fixed. Exterior/interior membership cannot change without crossing a boundary. Only inside this already safe neighborhood may one select stronger general position. No numerical value of eta is claimed in this packet.

## 5. A local cap-assisted expansion theorem, actually instantiated

Let a finite graph G have a representation by k disjoint filled simple polygons. Let ab be an edge and let a,b,c,d be distinct old vertices. Form H by deleting ab and inserting a new vertex w adjacent exactly to a,b,c,d. The following are sufficient conditions to preserve the SAME k obstacles:

1. There is a new point x, different from all old points and outside all old obstacles, whose visibility neighborhood among old vertices is exactly {a,b,c,d}; every new nonedge has a strict old-obstacle hit.
2. For one obstacle P_j there is a filled simple polygon E whose intersection with P_j is precisely one nondegenerate proper boundary interval of each disk. The closed cap E is disjoint from every other old obstacle. It avoids every point and every closed segment intended to be an EDGE of H.
3. The deleted segment ab has a strict interior hit in E.

Replace P_j by P_j union E. The two boundary arcs left after deleting the shared interval concatenate to a simple polygonal Jordan curve: their interiors are disjoint, and their endpoints are the two distinct attachment endpoints. Equivalently, two disks glued along a proper boundary interval form a disk. No annular fill or additional hole removal is performed. All old nonedges remain blocked because obstacles were only enlarged. Every new nonedge was already blocked in condition 1. Old retained and new edges avoid the old polygons and E by conditions 1 and 2. The deleted edge is blocked by condition 3. Hence H has the displayed k-polygon representation. Strictness and finite compactness supply a common positive margin as above.

This is a conditional construction, not obs(H)<=obs(G) for every expansion. In particular, simply adding a vertex while leaving obstacles unchanged cannot block the formerly visible edge ab.

For the current graph, remove vertex 3 and restore edge 27. The resulting eight-vertex parent is a bipyramid, with hubs 7,8 and rim cycle 5-1-4-0-6-2. This parent is reused only to instantiate the NEW local transfer; no old family enumeration is repeated.

Let P be the final inner pentagon. Replace it temporarily by

    Q = P intersect {9x+y >= 225/16},
    E = P intersect {9x+y <= 225/16}.

The exact Q pentagon and E quadrilateral are stored in ear-certificate.json. Their common boundary chord has endpoints

    (17999/3840,-35997/1280), (6961/2304,-3361/256).

The old coordinates stay fixed. The new point is p_3=(3,-9), with neighbors 2,5,6,7. The direct consumer verifies the parent using Q and the exterior polygon; it then verifies point insertion before deleting edge27 (22 edges, not asserted planar). Thus condition 1 is checked, not guessed. The final whole-graph check verifies every retained/new edge avoids E. Segment27 has its recorded strict hit in E, where 9x+y=14<225/16. Convex clipping verifies that Q and E have exactly the stated chord intersection and Q union E=P. Thus all local premises are actually instantiated.

Abstract structure is separate: if ab borders triangles abc and abd in a spherical triangulation, replacing those faces by four triangles through w preserves simple planarity. If G is four-connected, H is four-connected. After deleting S of size<=3 with w not in S, the missing edge ab is replaced by the surviving path a-w-b whenever both endpoints survive; w has a surviving neighbor. If w is deleted, at most two old vertices were deleted; the residual old graph is two-connected, hence has no bridge, so deleting ab cannot disconnect it. This does NOT guarantee that the geometric cap premises hold for every such structural expansion.

## 6. Complete necessary CNF and the fixed selector

The old NB9 generator is reused unchanged: n<=9, at most15 targets, raw clause attempts<=2000000, unique clauses<=250000, paths<=14000 per target and<=20000 total. Resource refusals are errors, not mathematical negatives.

For THIS graph there are 84 direction variables,15 colors,210 ordered-pair sides:309 variables. ALL5000 simple nonedge paths through eight edges produce121204 clauses (252 four-point,10080 five-point,110872 guarded path rows). Every key clause has its actual nonedge pair, path, color and mode origin. One side variable serves all paths for an ordered target pair.

For original path row K, equal-color guarding is

    (z_s OR z_t OR K) AND (not z_s OR not z_t OR K).

The geometric implication is reused from C26/C27: assigned targets lie in one OPEN free component per obstacle; finite paths and positive clearance allow safe general position; opposite critical paths give a Jordan first-exit contradiction. SAT of the relaxation alone does not imply a realizable order type.

The original tuple-set consumer exceeded512MiB. A first compact variant still allocated an unnecessary duplicate set; a later whole-output concatenation also exceeded the limit. The final adapter stores canonical clauses as injective signed16-bit strings and CONSUMES the expected set one actual row at a time. Variable indices<=309 fit exactly. Every actual source is rederived, every expected clause must be consumed once, and original tuple ordering is separately checked. No clause is dropped or strengthened. Streaming output hashing removes the last large concatenation. The fixed512MiB cap was not raised.

Complete hashes and lengths are in observation.json. replay.py cnf/origins-a/origins-b regenerates every row and source. Caches are not claimed as extra uploaded files.

The generated fixed incidence has73 components. At the frozen directions the relaxed formula has four labels:1352,1356,31411,31415. The whole-color component selector keeps only1352 with(0,17) and31415 with(17,0). It has455 variables and126576 clauses; exact masks cover32768*73^2=174620672 legal label/component choices. This is NOT a census of2^84 directions or real placements.

There are40 minimal empty target families:36 pairs and4 triples. The triple {03,16,27} is pairwise compatible but has empty total intersection. Its monochromatic exclusion removes exactly1356 and31411, retaining both actual polygon models. This is a FIXED-INCIDENCE cut, not an unguarded all-placement clause. The anchor criterion R_u=intersection over targets missed by u gives R_0={17}, R_17={0}; all other anchors have empty residual intersection. Anchors must be recomputed after placement, not frozen universally.

The exact incidence reconstruction was executed from supplied NB8 plane_reference.py. That supplied helper is not reuploaded here or substituted for a trusted geometry receipt. The shipped selector explicitly reports geometric_completeness_replayed=false. Direct checking of the whole-graph polygons and local cap transfer does not need this reconstruction or C19's tube theorem.

## 7. Execution, publication and next obligation

The new catalog consumer, compact source checker and ear consumer are distinct from their producers, but remain in the generator trust domain. Final commands use CPython3.13.5,35CPU seconds,40wall seconds,512MiB,one mathematical worker,5MiB stdout cap. selection.py alone requires NetworkX3.6.1. Final executed hashes, negative tests and bounded resource failures are preserved in execution.json. All code is ordinary text; no network, subprocess, dynamic evaluation or credentials in mathematical sources. External limits are applied by the runtime, not fabricated by a module.

Run from this directory: python -B replay.py polygon, ear, catalog, audit, interface, mutations, guard, path, omit, flip. Existing byte-pinned NB9 dependencies must remain at their repository sibling path. Only new files belong to this candidate; old NB9/MIN4 artifacts and protected records are unchanged.

The failed route is limited to this canonical nine-vertex class as an obs>=3 witness. No all-realizable-region UNSAT, uniform planar upper bound, exact obstacle number or trusted closure is claimed. There is no survivor for stage-two universal analysis in this ONE selected class.

The next untested n=9 class has degree sequence4^4 5^4 6 and word001001111001011011001101011101110101. No obstacle search was run on it. Test the explicit cap premises or a bounded whole-graph representation there before increasing graph order. Successful cap surgery here must not be extrapolated without those premises. T=polygon/Jordan semantics, A=incidence completeness, and P=all-placement growth remain separate.

best_verified_result: none
best_verified_candidate: none
root_obligation: open
statement_faithfulness: pending
trusted_closure: none
