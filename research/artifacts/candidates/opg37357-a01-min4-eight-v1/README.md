# MIN4: minimal non-bipyramid counterplacement and a fixed-target capacity barrier

Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Candidate: candidate:opg37357-a01-min4-eight-v1
Repository: vibemathing/problem-opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph binding: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Base: 1a5eefd266401b903f15de10c07b3aff7d3f9773
Issue: #3
Primary owner: math-proof; bounded exact computation supports the candidate.

## 1. Outcome and delivery scope

The unique eight-vertex non-bipyramid four-connected maximal planar graph has a rational representation by TWO DISJOINT FILLED SIMPLE POLYGONS. All edges and all ten nonedges are covered, not just five selected targets. An exhaustive structural certificate through order eight proves the qualified minimum. No graph survives this small-order structural screen as an obstacle-number-three candidate. The exact obstacle number of the selected graph is not determined.

A separate all-graph lemma proves that any matching of q nonedges can pass through one free square at some rational general-position placement. Thus a FIXED target set containing a three-edge matching cannot satisfy a capacity-two condition at EVERY placement. The lemma does not assert a one-obstacle representation of the entire graph, and does not eliminate placement-dependent target choices.

Publication limitation: the first incidence.py write was blocked by the platform, without a commit. It was not retried through another path, encoding, blob or attachment. Its dependent full reconstruction pipeline is not a repository-only release. The direct polygon consumer, structural consumer, full CNF generator/source consumer, matching construction and check_candidate.py are delivered and ACTUALLY REPLAYED without that incidence core. They suffice to replay the complete two-polygon counterplacement. The earlier full-incidence/selector computation remains separately recorded, not silently reclassified as a new trusted run.

No all-order-type impossibility, unrestricted root closure, EvidenceLink, Result or Solution is claimed. An explicit existential counterplacement is enough to reject the proposed all-placement lower bound for this graph.

## 2. Frozen graph, targets and exhaustive structural selection

Complete edges on vertices 0,...,7:

    01 03 06 07 12 13 15 16 24 25 26 34 35 37 45 46 47 67.

Complete nonedges in variable order:

    02 04 05 14 17 23 27 36 56 57.

The five targets frozen BEFORE coordinate screening are 02,14,27,36,57. selected.json has SHA-256 d13296c5d367a9cd09aaeb2805d833c631d9fd242d5389b3f4208e59781f2a54.

Rotation (predecessor of the reversed dart):

    0: 1 3 7 6       1: 0 6 2 5 3
    2: 1 6 4 5       3: 4 7 0 1 5
    4: 2 6 7 3 5     5: 3 1 2 4
    6: 7 4 2 1 0     7: 3 4 6 0.

All 36 darts form twelve triangular faces, with 8-18+12=2. Each of the 93 deletions of at most three vertices leaves a connected graph. Minimum degree four makes connectivity exactly four. Degrees are four copies each of 4 and 5, so no nonadjacent pair has degree n-2=6. There are no leaves or degree-three ports. Rotation proves ABSTRACT planarity only; graph-edge crossings in obstacle drawings remain allowed.

A four-connected maximal planar n-vertex graph has e=3n-6 and minimum degree four. Its complement therefore has (n-3)(n-4)/2 edges and maximum degree n-5. We exhaust n=5,...,8; a smaller graph cannot be four-connected in the usual nontrivial convention.

The producer uses NetworkX 3.6.1's atlas through seven vertices. At order eight it considers every possible neighborhood of a removed complement vertex, of size at most three, and retains ten complement edges. There are 584 extensions and 64 isomorphism representatives. The proof does NOT trust atlas completeness alone.

structure_audit.py instead uses only the standard library. Enumerate every nondecreasing degree sequence with the required sum and bound. At vertex i choose every subset of later vertices of the required residual degree, decrement those degrees and advance i. Negative residuals, odd residual sum or a degree exceeding the number of other positive-residual vertices are necessary impossibilities; their pruning loses no graph. The index i strictly increases, so the recursion terminates. Relabeling any graph by degree puts it in this enumeration.

For each representative, enumerate all permutations within equal-degree groups. The consumer requires DISJOINT orbits whose union equals the entire independently enumerated set. Each excluded graph has either a separator of size at most three or a checked K5/K3,3 subdivision. Subdivision paths are traced through degree-two vertices, use every certificate edge, and have the required simple branch graph. Remaining graphs have checked sphere rotations and all deletion cases connected. Euler's bound excludes K5 and the bipartite Euler bound excludes K3,3; suppression of a subdividing degree-two vertex preserves planarity. Thus a library's Boolean planarity verdict is not the certificate.

Exact census:

 n  degree-sorted labelled complements  representatives  4-connected triangulations  non-bipyramids
 5                  0                         0                     0                    0
 6                 15                         1                     1                    0
 7                237                         6                     1                    0
 8              12102                        64                     2                    1

If two nonadjacent vertices dominate all others, deleting them leaves a connected graph with n-2 vertices, n-2 edges and minimum degree two, hence a cycle. This is exactly the ordinary bipyramid, structurally filtered without repeating its obstacle construction. The two admissible order-eight degree sequences differ. The selected graph is consequently the unique structural minimum under the requested filters through n=8. This is not a novelty claim or a claim that every known two-obstacle theorem has been surveyed.

## 3. Rational two-polygon certificate and robustness

Coordinates in vertex order:

    (-5,-1),(-5,-7),(-4,12),(-12,9),(12,16),(15,12),(16,3),(-3,-8).

All 56 graph-point triple determinants are nonzero. witness.json gives every rational corner of the 28-corner exterior corridor and the 8-corner interior convex polygon, plus one strict hit for EVERY nonedge. Assigned obstacle labels in nonedge order are

    0 1 1 1 0 0 1 1 0 0.

The exterior polygon was produced from L-infinity tubes of halfwidth 1/4096 along the box chain (-32,-32)--(-32,32)--(32,32)--(32,-32), with five recorded connectors. The interior polygon is a small square-thickened hull of its assigned hits. Their full rational boundaries, not an approximate image or unexecuted construction, are the certificate. The historical producer and its source digests remain distinct from the direct consumer.

witness_check.py imports no arrangement, offset producer, CNF or graph library. It checks distinct polygon corners, nonzero adjacent turns, positive signed area and every nonadjacent closed-side intersection, so each boundary is a simple Jordan polygon. Winding counts classify every graph point as strictly exterior. Every graph edge has exterior endpoints and no intersection with either polygon boundary: its connected image cannot enter a bounded Jordan component without crossing that boundary. Every listed nonedge interpolation parameter is strictly between zero and one and its hit is strictly inside the assigned filled polygon. Cross-boundary disjointness and nonnesting prove the two filled obstacles disjoint.

Actual checks: 370 within-polygon nonadjacent side pairs,648 graph-edge/obstacle-side pairs,16 vertex exclusions,224 cross-obstacle side pairs and10 strict nonedge hits. This proves the counterplacement through a finite exact certificate, without assuming completeness of the incidence reconstruction or C19's tube lemma.

For disjoint segments, the consumer checks a separating projection with positive rational gap. Gap divided by the projection's L1 norm bounds permissible L-infinity movement. The same test gives a positive hit-to-every-boundary clearance. Including a quarter of the minimum vertex separation yields the simultaneous bound

    eta=1/16384.

Keep the two polygons fixed. Moving EVERY graph point by less than eta preserves its exterior location, every entire graph-edge boundary separation, injectivity and every nonedge hit at the SAME interpolation parameter. A continuous straight homotopy cannot change interior/exterior without a boundary contact, which the separation bounds exclude. The representation is not dependent on a zero-margin tangency.

The five frozen targets have obstacle loads two and three: 14,27,36 all hit the interior obstacle. Thus their proposed universal capacity-two assertion fails even on a COMPLETE two-obstacle representation of the entire graph. Exact obstacle number one versus two remains undecided.

## 4. Necessary CNF and the separately recorded selector computation

Write K(p) for graph points and closed graph edges, F(p)=R^2 minus K(p), and J_s(p) for the components meeting nonedge s's relative interior. The exact connected-obstacle interface is

    exists p, exists U0,U1 in components(F(p)), exists z:nonedges->{0,1},
    forall s: U_(z_s) is in J_s(p).

The same component serves the WHOLE color class. Unused labels and repeated components are allowed. The components belong to that same p.

The global necessary CNF reuses the separately audited C26/C27 implication. From a hypothetical obstacle representation connect finite assigned hits inside the corresponding OPEN free component. The compact path union has positive distance from K. Thicken inside that clearance, preserve every hit's interpolation parameter and choose one simultaneous movement margin for all graph edges and hits. Only then select general position in the safe coordinate box. Density alone would not preserve contact-only obstacles.

At general position, opposite key paths enclosing one nonedge but excluding another produce a graph-edge Jordan curve. A path in the common free component has a first exit from its interior and must hit the forbidden curve. This is the same-component premise behind each key clause; it is not a consequence of an arbitrary Boolean equality of labels, nor of the abstract plane rotation.

Variables1..56 are increasing-triple signs,57..66 the ten colors,67..156 the ordered nonedge-pair sides. A path clause K is guarded by

    (z_s OR z_t OR K) AND (not z_s OR not z_t OR K).

All four-/five-point determinant rules and all1502 simple paths through seven edges are included. The formula has156 variables and31676 clauses:140 four-point,4480 five-point,27056 guarded key rows. The second source consumer uses breadth-first paths instead of internal permutations and a different parity expression; it reconstructs every canonical clause and source.

At the actual coordinate table all1024 colorings were checked by exact side forcing. Exactly two survive, the displayed coloring and its swap; full satisfying assignments are saved. This proves SAT of the global relaxation through a REAL witness, not UNSAT over unrealizable signs. No enumeration of 2^56 direction assignments is claimed.

Before the publication block, a complete fixed-drawing calculation recovered36 free components. One-hot choices add72 selector variables and1282 clauses; including56 fixed direction units gives228 variables and33014 clauses. It exhausts1024*36^2=1327104 legal one-hot color/component choices and leaves exactly two models, component pairs(0,12) and(12,0). That computation and its source/output hashes are recorded as generation-domain observations. Full incidence reconstruction is NOT performed by the delivered check_candidate.py and cannot presently be replayed solely from the repository.

Actual full-output hashes:
- CNF: 59b3e5af71df569218572cf40fc4b8a30d4844235360a717004fb63f9f7a1f74
- clause origins: 13655d9e4ca0c58904b058d2408e1533d726a56e2e3821a6bd327f1b6fc310c3
- fixed selector CNF: c3fe41e4af885df84e2f0852ca79fd24939478c256f59e71623e5e4ef0dabb87

These caches exceed the one-file repository limit. Delivered check_candidate.py cnf/origins regenerates the first TWO exactly. The fixed-selector emitter retains an unpublished incidence dependency; its digest is not claimed to replace source delivery. None of the large caches is falsely listed as an uploaded repository file.

## 5. General fixed-target matching concentration lemma

Claim: for any finite simple graph and a matching of q>=1 nonedges, some rational GP placement has a closed square avoiding every graph point/edge and meeting all q matching targets. Other nonedges need not be blocked.

Enumerate matching pairs a_i b_i,1<=i<=q. Put a_i=(1,i), b_i=(-1,-i). Put each remaining vertex w_j at(2,2q+2j+1),0<=j<n-2q. Set B=2n+1,eps=1/(8B). All points are distinct. Same-sign-x edges avoid the square[-eps,eps]^2. For opposite-sign edges the endpoint determinant is a nonzero integer: i-j for different matching pairs (i=j is an absent edge), or the odd integer2q+2j+1-2i for a remaining point. The supporting line has absolute value at least1 at the origin and normal L1 norm at most3+2B<=4B. Across the square its value changes by at most1/2. Thus it misses the square. Every matching midpoint is the origin.

To obtain GP while keeping strict margins, put delta=eps/(4n^2) and translate vertex k by t(k,k^2). For each distinct triple its determinant is a polynomial of degree at most two in t with NONZERO quadratic Vandermonde coefficient. Each excludes at most two t values. Among the2*binom(n,3)+1 positive rationals t=delta/(j+1), one avoids all exclusions. Every endpoint moves by less than eps/4. Original opposite-sign line slack decreases by at most4B*eps/4=1/8, still leaving positive separation; same-sign edges retain x separation. Matching midpoints stay inside the fixed square. This is a finite terminating GP construction with a uniform positive margin, not density without visibility preservation.

matching.py checks the selected matching02,14,36 against all eighteen graph edges. It does NOT claim that the other seven nonedges are blocked. The implementation is bounded to n<=16; the proof is for every finite n with a nonempty matching.

Consequently, a fixed target set containing a nonedge matching of size b+1 cannot obey capacity b for EVERY placement and EVERY free component. Restricting to placements that already represent the WHOLE graph adds a hypothesis; choosing targets AFTER the placement changes quantifiers. Neither is silently ruled out by this lemma. The explicit polygon representation above separately refutes this selected graph's stronger whole-graph lower-bound proposal.

## 6. High-order extraction and next obligation

The earlier full incidence result contains21 minimal pair cores and one minimal triple, targets02,36,57. The triple does not remove any additional models from this drawing's full guarded-CNF colorings: both surviving colorings already have genuine common components. It is not a new graph-level cut and cannot be added without a geometric sign-region guard.

There is no surviving non-bipyramid four-connected triangulation through order eight. The counterexample geometry uses a bounded convex cell and a connected exterior corridor, established here only for this selected graph. It is not a two-obstacle theorem for all four-connected triangulations.

Next atomic step: order nine or a genuinely different stronger structure, with the same structural filters. Before attempting a FIXED capacity-two proof, exclude target sets containing a three-edge matching. Prefer placement-dependent anchored empty-intersection certificates where fixed targets are impossible. Any survivor still requires all realizable regions and degenerate boundaries, rather than a fixed rotation or one failed numerical drawing.

## 7. Reproduction, sources and assurance

Repository-only commands:

    python -B check_candidate.py < witness.json
    python -B check_candidate.py cnf < witness.json
    python -B check_candidate.py origins < witness.json
    python -B structure_audit.py < structure.json
    python -B enumerate_small.py
    python -B mutations.py geometry < witness.json
    python -B mutations.py clauses < witness.json
    python -B mutations.py structure < structure.json

Apply externally30 CPU seconds,40 wall seconds,512MiB,one worker,4MiB output. CPython3.13.5; NetworkX3.6.1 only in the producer. After a publication-gap audit the delivered entry was actually rerun without importing incidence.py, and all20 mutations were rerun. Final timings and exact hashes are in execution.json. A structural-consumer revision now also rejects an omitted entire order domain. Witness JSON was whitespace-compacted without changing any numeric field; both input hashes are recorded.

The CNF helpers derive from the supplied BIP2 attachment and are explicitly reused, not new C22/C26 discoveries. The earlier incidence helper derived from the supplied C28 extension; its attempted MIN4 publication was blocked. No alternate representation/channel was used for that payload. The final public counterplacement check does not implement that blocked reconstruction; it checks the two explicitly supplied polygons directly. Original tube/reconstruction/probe source statuses are inventoried, not silently claimed delivered.

Primary implementation reference: NetworkX graph_atlas_g documentation, version3.6.1, https://networkx.org/documentation/stable/reference/generated/networkx.generators.atlas.graph_atlas_g.html . plantri documentation was consulted but plantri was NOT installed or run. Local network/download failures did not authorize a policy bypass. No compute-planner receipt was invented.

T=C19 tube/Jordan, A=complete incidence, P1=X4, P2=unrestricted growth remain separate. The direct counterplacement does not depend on T or A completeness. Implementation diversity is not a separate verifier trust identity. The registered fixture policies do not provide a compatible mathematical closure receipt. No truth ledger, schema, Harness, workflow, registry, Evidence, Result or Solution was modified.

best_verified_candidate: none
best_verified_result: none
root_obligation: open
status: NONTERMINAL_CHECKPOINT
