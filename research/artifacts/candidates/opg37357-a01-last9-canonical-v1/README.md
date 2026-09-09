# LAST9: the remaining nine-vertex class has a two-polygon cap lift

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
best_verified_result: none
best_verified_candidate: none
Repository: vibemathing/problem-opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph binding: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Primary owner: math-proof
Base: 7593b2f8aac2cde225560efc2e39a59080ef2916
Coordination: Issue #3

## 1. Exact outcome, selection and definitions

Only canonical word 001001111001011011001101011101110101, degree sequence 4^4 5^4 6, is screened. NEXT9's byte-pinned catalog supplies its identity as the remaining four-connected maximal planar class of order nine. Its graph, rotation and targets were frozen before geometry with input SHA-256 a34d735d773d2499582b048914772954bbe55246fe7a71e86d1f12db0a9a4973. No previous graph search or catalog enumeration is repeated.

The exhibited rational drawing has TWO DISJOINT CLOSED FILLED SIMPLE POLYGONS representing every edge and every nonedge. Hence obs(G)<=2 is a candidate conclusion for this graph and its isomorphic copies. It is not a claim that the exact value is two, nor a uniform planar upper bound. An existential whole-graph counterplacement excludes this single proposed all-placement obs>=3 assertion without enumerating all real-coordinate regions.

Graph points are distinct and exterior to both obstacles. Edges are closed straight segments, and crossings between graph edges are allowed. A filled simple polygon is its polygonal Jordan boundary together with the bounded interior. All nonedge witnesses are strict interior points. These stronger upper-witness conventions satisfy the ProblemContract's visibility definition, but statement-faithfulness is still a separate requested review, not a signed admission.

## 2. Frozen graph and abstract structure

All 21 edges on 0,...,8:

    03 06 07 08 12 15 17 18 24 25 28 34 36 38 45 46 48 56 57 67 78.

All 15 nonedges in color-variable order:

    01 02 04 05 13 14 16 23 26 27 35 37 47 58 68.

Five targets frozen before screening: 01,02,04,05,13. Every test still requires the WHOLE complement.

Rotation (face successor is predecessor of the reversed dart):

    0:3,8,7,6       1:2,5,7,8       2:4,5,1,8
    3:0,6,4,8       4:3,6,5,2,8     5:6,7,1,2,4
    6:7,5,4,3,0     7:1,5,6,0,8     8:7,0,3,4,2,1.

All 42 darts lie in fourteen triangular faces, with 9-21+14=2. All 130 vertex deletions of size at most three were checked connected. Degrees 4,4,4,4,5,5,5,5,6 exclude leaves and the nonadjacent dominating pair. These are ABSTRACT graph checks. They do not impose this rotation on an obstacle drawing.

## 3. Search order and the exact two-obstacle witness

The cap test was done first: eight degree-four inverse-expansion choices, the first isomorphism to the supplied NB8 parent witness for each eligible choice, and 64 explicitly listed rational new-point probes. None had exactly the required four visible neighbors. This rejects those particular proposals only; it is NOT a cap-nonexistence theorem.

The subsequent finite coordinate search proposed 157 placements of this SAME graph; 148 were in vertex general position and nine were skipped for collinearity. There were 107 failed general-position probes before the final batch, followed by 40 failed convex permutations. The successful probe is batch 2, step 40 (zero based). The seed and every proposed input/result are in probe-records.json. A failed coordinate probe is not an infeasible order-type shard.

Successful points in vertex order:

    (3,-9),(7,-49),(8,-64),(6,-36),(5,-25),
    (2,-4),(1,-1),(4,-16),(0,0).

These lie on y=-x^2 with permuted labels and have no three collinear vertices. Parallel support lines and nonvertex concurrence need not be removed.

witness.json lists every corner of a 32-corner exterior slit band and a 5-corner convex interior polygon. It also lists a strict interpolation parameter and hit for all 15 nonedges. Obstacle labels are

    1 1 0 0 0 0 0 0 0 1 1 0 0 0 0.

Thus multiple targets share a genuinely connected filled obstacle, not independently chosen components. The exterior band has a slit and is a disk, not a filled annulus. No conclusion rests on a picture.

The existing NB9 winding/orientation consumer and the NEW parity_check.py both verify the exact complete certificate. The latter imports no construction, arrangement, CNF, or NB9 geometric predicates: it solves segment-intersection parameters directly and uses horizontal-ray parity. Each method checks 469 nonadjacent within-polygon side pairs, 777 graph-edge/obstacle-side pairs, 160 cross-obstacle side pairs, all 18 point exclusions and all 15 strict hits. Adjacent sides meet only at their common endpoint. The boundaries are disjoint and not nested.

Finite predicates imply filled-region visibility as follows. A verified simple polygonal boundary is a Jordan curve and its filled bounded region is a disk. A graph segment starts outside it. If it entered the interior, continuity yields a first boundary hit; the closed-segment intersection checks prohibit that. Each nonedge has an explicit strict interior hit. Consequently the visibility graph is exactly G. Different implementations here are still in the generator trust domain; they are not a separately signed verifier receipt.

## 4. The conditional cap lemma DOES hold for an explicit parent

The failed initial probes do not prevent another parent placement. The successful full witness supplies one, and every cap premise is checked afterwards rather than inferred from drawing appearance.

Delete vertex 1 and restore edge 27. The eight old labels in the saved parent are 0,2,3,4,5,6,7,8. Let B be the exterior obstacle and P the final interior pentagon. Set

    Q = P intersect {12x+y <= 127/4},
    C = P intersect {12x+y >= 127/4}.

Q is a pentagon and C a quadrilateral. Their common boundary chord has endpoints

    (2347/512,-2977/128), (39551/7680,-19231/640).

Their complete corners are in cap-certificate.json. Exact convex clipping proves Q union C=P and Q intersect C is precisely this nondegenerate proper chord. Neither an unrecorded bridge nor a hole filling is used.

The two consumers check all three stages:

- parent with B,Q: 8 vertices,18 edges,10 strict nonedge hits;
- insert p_1=(7,-49), before removing 27: 9 vertices,22 edges,14 strict nonedge hits;
- add C to Q and delete edge27: 9 vertices,21 edges,15 strict nonedge hits.

The inserted point has exactly the intended old neighbors 2,5,7,8, verified from the complete intermediate visibility graph. All other incident nonedges were already blocked. Since the closed cap C is a subset of the final P, the verified final disjointness also proves it misses B, every graph point and every retained/new graph edge. The deleted segment27 has strict cap hit

    (1263/256,-1741/64), parameter785/1024 from p_2 to p_7,

where 12x+y=32>127/4. The point is also strictly interior to P, hence strictly interior to C.

These are all hypotheses of NEXT9's conditional cap-transfer lemma. For completeness, the topological step removes the common chord from the two boundary curves and joins the two remaining boundary arcs. Their interiors are disjoint; the resulting curve is a simple polygonal Jordan curve bounding the union disk. Old nonedges stay blocked when an obstacle is enlarged; new nonedges were already blocked in the point-insertion stage; all intended edges avoid the cap and old obstacles; the restored parent edge becomes blocked. Thus the SAME two obstacles suffice. The parent representation is given explicitly in parent-witness.json, not just asserted to exist.

A single successful instance is not an unconditional expansion-monotonicity theorem. In particular, a point insertion without a cap would leave edge27 visible and would fail to represent G. The cap data were mutated as a negative control; the intermediate representation explicitly still contains the restored edge.

All actual old and new nonedge hits are strict. Because finitely many compact edges avoid compact obstacles, their distances are positive; hits also have positive boundary distances. Take eta less than one quarter of the minimum of these distances and distinct-point distances. Moving every vertex by less than eta moves every whole edge and every fixed-parameter hit by at most eta (in the same norm). Fixed obstacles therefore preserve all visibility/blocking. Only INSIDE this uniform safe neighborhood may genericity be invoked. No numerical margin is claimed here, and mere density is not substituted for preservation.

## 5. Complete guarded CNF and scope

The existing NB9 producer and NEXT9 lossless signed16 source consumer are reused unchanged and SHA-bound. Domain: n<=9, at most15 nonedges; finite raw/unique/path caps remain unchanged. A resource refusal is an error, never UNSAT.

For G the full formula has 84 direction variables,15 colors and210 ordered-pair sides:309 variables. All 5117 simple paths through eight edges produce 124844 distinct clauses:252 four-point,10080 five-point,114512 guarded key rows. The consumer reconstructs every row and its actual path/tuple source using different breadth-first and parity methods. Nothing is inferred from counts alone.

For a necessary key clause K and targets s,t, same-label guarding is

    (z_s OR z_t OR K) AND (not z_s OR not z_t OR K).

One ordered target pair shares its side variable across every path. A true representation yields finite witnesses in one open free component per obstacle; polygonal paths and positive clearance allow safe general position. Opposite key paths then give the C26/C27 Jordan first-exit contradiction. This is a necessary implication for real placements, not sufficiency or realizability of arbitrary direction bits.

The quantified geometric interface is

    exists p, exists U0,U1 in components(R^2 minus K(p)), exists z,
    forall nonedges s, U_(z_s) intersects relint(s).

All components come from the SAME placement. A label class uses one component for its entire family. Graph crossings are allowed. Rotations, SAT and fixed-incidence tests do not remove the existential real-coordinate quantifier.

Complete actual DIMACS:5039369 bytes, SHA-256
584e549b15e2b3b8a9e112d7fcc72ce092216f5caca7f2c44a6ee74835d543e1.
Complete actual origins:5578839 bytes, SHA-256
110d7c0ac8897f9a8102cc670e2e7efd10a0b84d23407d2a6fbeb730e7189c85.
The executed local dispatcher emitted each in two ordered parts. That dispatcher was later blocked at publication; neither it nor the large caches is a repository file. The inherited producer and consumer remain individually available as prior modules.

## 6. Fixed incidence, Helly gap and anchors

The local supplied plane_reference.py observation has61 components. The locally executed set interface consumes that frozen table and reports geometric_completeness_replayed=false; its new dispatcher is publication-blocked. This is NOT a new general arrangement release or trusted completeness proof; the direct polygon/cap conclusions require neither.

At the displayed direction table, all32768 colorings are projected exactly through side constraints. The only relaxed models have codes1539 and31228. Complete component selection yields (1539;0,39) and(31228;39,0), with431 variables and128620 clauses. Exact masks represent32768*61^2=121929728 legal label/component cases; all3721 ordered component pairs are considered. Both complete assignments are checked clause by clause.

All inclusion-minimal empty target intersections are extracted:39 pairs and one triple {04,16,27}. At this placement its pairwise intersections are {0},{41},{42}, while the triple intersection is empty. Neither actual coloring makes that triple monochromatic. Thus this model supplies NO additional cut eliminating a false relaxed label. Adding a cut rejecting the real representation would be unsound.

For each anchor u, M_u is the set of targets it misses and R_u is the intersection of the J_s over s in M_u, with empty intersection equal to the whole component universe. Two-cover existence is equivalent to some R_u being nonempty. Here R_0={39},R_39={0}; the remaining59 anchors have empty cores. Anchors and incidence are computed AFTER p. They must not be frozen as universal combinatorial constraints over all placements.

The failed coordinate probes were finite inputs, not certified UNSAT shards. No2^84 direction census, realizable-region coverage or all-placement lower bound is claimed. The existential full witness already excludes this single graph as an obs>=3 proposal.

## 7. Reproducibility and outcome boundaries

Published new mathematical code: parity_check.py and cap_verify.py. Existing NB9/NEXT9 dependencies are SHA-bound in provenance.json and are not copied. Run the ALREADY delivered direct entry python -B cap_verify.py from this directory under external35 CPU seconds,40 wall seconds,512MiB,one worker,5MiB output. It checks parent, insertion and final geometry with both consumers. The new replay.py dispatcher was blocked by platform safety with NO commit, was not retried through another path/tool/encoding/attachment, and is excluded from this delivery. Local modes polygon,cap,structure,audit,interface,mutations,guard,path,omit,flip,cnf0,cnf1,origins0,origins1 were actually executed, but a repository-only one-command replay of those auxiliary modes is NOT claimed. Exact CPython version, actual exits/times and input/source/output hashes are in execution.json. Mathematical modules contain no network, subprocess or dynamic evaluation.

Thirteen corrupted polygon certificates are rejected by BOTH consumers; three cap-identity corruptions and four clause corruptions are rejected. Tests cover missing nonedges, edge insertion/deletion, endpoint-only hits, wrong label, boundary contacts, duplicated corners, nesting/contact, missing guard, flipped direction, incomplete clauses and wrong paths. They supplement, not replace, the proof of finite-predicate semantics.

The historical generic plane_reference helper and the one-time coordinate/offset search are generation-domain support, not the standalone witness checker. No old blocked plane_with_outer.py or margin_build.py was reuploaded or routed through a different channel. Exploration sources and fully enumerated probe inputs have their exact fingerprints recorded; no hidden reasoning transcript is saved.

Relative to NEXT9's four-class catalog and previously saved upper-bound candidates, no untested nine-vertex four-connected maximal-planar class remains. This is a finite dependency-based screening conclusion, NOT a theorem for all planar graphs. No ten-vertex graph is researched in this packet. Existing one-obstacle lower-bound work, polygon/Jordan semantics, general incidence completeness and placement-universal growth remain separate obligations.

The failed-route proposal excludes ONLY this canonical class and its relabelings as an obs>=3 candidate. Future work needs a new isomorphism class (at least order ten in this catalog-based lane), or an explicitly stronger representation-preserving theorem with its local premises proved. Do not repeat LAST9, NB9, NEXT9, MIN4, or the excluded bipyramid/diamond/prism families.

Statement-faithfulness: pending. Trusted closure: none. No EvidenceLink, Result or Solution is self-signed. The root and bounded-polygon-encoding obligations remain open. CI and merge are transport only.
