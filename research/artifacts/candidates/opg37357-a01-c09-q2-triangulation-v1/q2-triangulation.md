# Q2 reduction to induced planar triangulations

Candidate: candidate:opg37357-a01-c09-q2-triangulation-v1
Verdict: candidate_only
Owner: math-proof
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Base: f619c5b133b224764fd1c0f0c301e1b6b7df3b5a

## Scope

Q1 is supplied by the c08 X4 all-placement obstruction and stored exact RUP replay, pending trusted semantic/kernel/axiom replay. This candidate concerns Q2: whether ordinary obstacle numbers of finite simple planar graphs admit a universal integer bound. It supplies a class reduction, not the requested constant or an unbounded family. No corner cutoff or new ETR exporter is used.

An obstacle is a connected polygonal region disjoint from the graph points; adjacency means its closed joining segment avoids every obstacle. Graph-edge crossings are permitted. All arguments below work for the existing closed simple-polygon convention and for the broader connected-obstacle convention. They never compare obstacle number with the noncrossing-drawing variant as though these were equal.

## T1. Induced-subgraph restriction

If G is an induced subgraph of H, then obs(G)<=obs(H). Keep the points for V(G), erase the other points, and keep all obstacles. Every pair retained has exactly its former visibility and, by inducedness, exactly its required adjacency. The obstacles remain disjoint from the retained points and stay connected. Any general-position condition is inherited by a subset.

This is not an edge-deletion statement. For example, K3 has obstacle number zero while the three-vertex path does not: without obstacles every distinct pair is visible. Likewise, adding edges on the original vertex set to triangulate G is not a valid obstacle-number upper-bound reduction by itself.

## T2. A linear-size induced triangulation extension

Let G have n>=4 vertices and e edges. There is a simple planar triangulation H containing G as an induced subgraph. More precisely, choose a maximal planar supergraph T on the SAME n vertices and write

    M = |E(T) minus E(G)| = 3n-6-e.

Fix a spherical embedding of T. Let t be the number of triangular faces of T incident to at least one of its M added edges. Then H can be chosen with

    |V(H)| = n+M+t,
    t <= min(2M, 2n-4),
    |V(H)| <= min(n+3M, 6n-e-10).

Construction. Subdivide each added edge uv once, with a distinct new vertex w_uv. Do NOT subdivide any original edge. Call this plane graph T'. Each old triangular face has become a simple cycle of length between three and six. For every face of length at least four, put one new vertex z_F in that face and join it to every vertex of its boundary. Leave the length-three faces unchanged. This is selective face coning, including the sphere face later designated as the outside face.

Proof of existence and planarity. Repeatedly add an edge to G while simplicity and planarity allow it. For n>=3 an edge-maximal simple planar graph is a triangulation, with 3n-6 edges and 2n-4 triangular faces. This ordinary augmentation changes only the auxiliary T, not the required induced copy in H. Subdivision preserves the sphere embedding. Each affected face is a topological disk with a distinct cyclic boundary; a star from one interior point divides it into triangular disks without crossings. Distinct faces have disjoint interiors, so all stars can be drawn simultaneously. No loops or parallel edges are introduced.

Inducedness. For every old pair uv, its direct edge remains in H exactly when uv was in E(G). An edge added to form T was replaced by a two-edge path and is no longer an old-old edge. Every subsequently added edge is incident to a new face center. Thus H[V(G)]=G, including when G was disconnected or had isolated vertices.

Count. There is one subdivision vertex per added edge and one center per affected face. Each added edge is incident to two faces, hence t<=2M; also t<=2n-4. The displayed bounds follow by substitution. If M=0 the construction changes nothing: H=G. Small graphs n<4 can first be padded by isolated vertices to order four, preserving the original graph as an induced subgraph, and then treated by the same construction.

## T3. Which separating triangles are introduced?

Every triangle of H is either an original triangle of G or one of the triangular faces created around a new face center. In particular, NO NEW NONFACIAL TRIANGLE is introduced.

Proof. A triangle with a face center contains only one such center, because centers are pairwise nonadjacent. Its other two vertices lie on the boundary of a subdivided triangular face of T. Every edge of T' between two vertices of that boundary is a boundary edge: the old face had just three old vertices, each side is either an original edge or a once-subdivided edge, and a subdivision vertex has only its two old endpoints as neighbors in T'. Therefore the triangle containing the center is facial. A triangle with no center cannot contain a subdivision vertex, since its two neighbors in T' are the endpoints of an added edge that has been deleted. Its three vertices are old and its edges are exactly edges of G.

Moreover, an original G-triangle that is facial in T is not coned: none of its three edges was added, so that face remains a triangle. A G-triangle nonfacial in T separates old vertices on both sides in the sphere embedding of the triangulation T, and those vertices remain in H. Thus the nonfacial triangles of H are precisely the G-triangles that are nonfacial in the selected embedding of T. This refers to that embedding, not an arbitrary separately prescribed input embedding.

For triangle-free G, H has no separating triangle. Using the standard characterization that a simple planar triangulation with at least five vertices is 4-connected exactly when it has no separating triangle, this yields an induced 4-connected triangulation extension for every triangle-free planar G. The small padded cases also meet the required order. The characterization is the only extra graph-connectivity premise in this corollary; the construction and absence of new nonfacial triangles do not depend on it.

## T4. Consequences for the actual Q2 quantifiers

For a fixed integer k, a bound obs(H)<=k for EVERY finite simple planar triangulation H of order at least four would imply obs(G)<=k for EVERY finite simple planar G: apply T2 and then T1. The reverse implication is immediate because triangulations are planar. Hence the existence of a universal k can be investigated entirely on 3-connected maximal planar graphs. The value k is not increased by this reduction.

Likewise, any family of planar graphs with obstacle numbers tending to infinity can be replaced by a family of planar triangulations with at least those obstacle numbers and with only a linear increase in vertex count. This is a conditional transformation of a family, not a construction of an unbounded family here.

The triangle-free corollary does NOT reduce all planar graphs to 4-connected graphs. It only reduces the triangle-free subclass. No uniform obstacle bound under clique sums, edge flips, contractions, or arbitrary edge deletion is assumed.

## T5. Exact attacks on stronger shortcuts

A. Subdivide all added edges but omit face centers: an affected triangular face becomes a quadrilateral, pentagon or hexagon, so the output need not be maximal planar.

B. Cone every face, including unchanged original triangular faces: although this still gives an induced triangulation, it can turn a previously facial original triangle into a separating triangle. Selective coning is necessary for the T3 correspondence, not for T2 alone.

C. Replace '3-connected triangulations' by '4-connected triangulations' for arbitrary G: take the planar triangular bipyramid K5 minus one edge. Write abc for its base triangle and u,v for its two nonadjacent apices, each adjacent to a,b,c. In every planar embedding u and v lie on opposite sides of abc. Indeed, an a,b,c tripod from one apex divides one side of abc into three regions; a second apex on that side cannot join all of a,b,c without crossing that tripod. Any planar supergraph retaining these edges still has abc separating u from v. Consequently no 4-connected planar supergraph, induced or otherwise, contains this graph. This is a five-vertex obstruction to that extension shortcut, not to Q2.

D. Use a count of planar faces as an ordinary obstacle-number lower bound: a visibility representation is allowed to have graph-edge crossings. The planar-obstacle-number lower bounds in the 2017 source therefore cannot supply a divergent ordinary-obstacle family.

## T6. Actual bounded regression and its limits

The companion triangulate.py constructs T by lexicographically testing missing edges with NetworkX planarity checks, subdivides the added edges, and selectively cones affected faces. Its audit checks the induced old-edge set, exact counts, planar maximality, each oriented edge appearing once among oriented triangular faces, circular vertex links, Euler characteristic two, and the T3 triangle correspondence.

Executed in the foreground candidate-generation runtime: Python 3.13.5, NetworkX 3.6.1; one process, external 45-second wall bound, internal 40-second scan bound; no solver or network. All 1012 planar graphs in the installed atlas of orders 3 through 7 passed. Counts by order were 4, 11, 33, 142, 822. Of these, 163 were triangle-free; the largest output had 32 vertices. Explicit P3, C5, K2,3 extensions had connectivity four and orders 6, 15, 14. The row digest is recorded in atlas-observation.json. These finite checks support the implementation only; they are not a proof of the universal theorem or any obstacle bound. The written T1--T4 arguments are separate candidate proofs.

The construction source is not a trusted verifier. Reproduction from this directory is `python triangulate.py --max-order 7 --save`, under the same external resource bounds. The output contains no obstacle representation, obstacle SAT claim, or UNSAT certificate.

## T7. Scoped correction to frozen c08 metadata

The c08 replay-v2 README reports incorrect subcounts: five-point 3024, key-path 65888, paths 2212. A fresh byte-identical copy of necessary_cnf.py, SHA-256 49a83611574808cb7296c761128821a9a2bd32fcab97de9dc0a0d610aa69f83a, was executed for deterministic regeneration. At path-edge cap four its actual counts are:

    four-point 420; five-point 20160; key-path 48752; paths 804;
    variables 540; clauses 69332.

The regenerated complete CNF SHA-256 remains de54d35f78d3c7d84e24651e5ce6f82c9ebe6d78bc7bd2deb66aa591e6ea276c, exactly the frozen proof input. Thus this correction concerns prose subcounts, not the CNF or certificate bytes. At caps two and three the regenerated clause totals are 24100 and 37572, with 44 and 244 paths. No solver or RUP checker was called in this count audit. The earlier c08 replay observation is reused as an earlier candidate observation, not represented as newly executed here. The c08 files are not modified.

## Remaining root tasks

Q1: c08's explicit X4 obstruction has a stored exact propositional replay and planarity certificate, but trusted geometric statement-faithfulness, kernel and axiom replay remain pending. Q2: this candidate supplies neither a universal k nor a divergent family. The next search should test TWO-obstacle necessary conditions on maximal planar graphs, retain exact proof outputs for any contradiction, and distinguish SAT in a necessary-condition relaxation from an actual two-obstacle construction. A geometric upper-bound route must address the positions of shared separator triangles, rather than assume an unproved clique-sum gluing rule.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
