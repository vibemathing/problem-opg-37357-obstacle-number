# C27 supplement: the shared-nonedge diamond h=2 interface is SAT

Candidate: candidate:opg37357-a01-c27-diamond-audit-v1
verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Base: e358fe83f026715b0b6ddf868f84a58c3bdf91fe
Resumed PR: #32; original head 27be45a2de34eb886ebe3825c170b78dd97b8677
Owner: math-proof, with bounded exact computation

## 1. What was recovered and the exact new scope

The existing PR already had seven C27 candidate files, its real PR32 packet,
verification request and checkpoint. Its directory did NOT contain a diamond
graph, CNF or model file. No corresponding old byte strings were present in
the available local artifacts. Consequently this supplement does not claim to
have recovered an unrecorded graph. It freezes the following precise reading
of three diamonds sharing a nonedge, and additionally covers the smaller
variants obtained by identifying their other vertices. Earlier C22/C26 clauses
and the rejected X4-copy route are not regenerated as new research.

A diamond is an induced K4 minus one edge. Let D_r have nonadjacent hubs
0,1 and r disjoint pairs a_i=2+2i,b_i=3+2i, for 0<=i<r. Its complete edge set is

    {0a_i,0b_i,1a_i,1b_i,a_i b_i : 0<=i<r}.

No additional edges are implicit. All r modules share the SAME missing pair
01, not a clique. D_3 is vertex-minimal under the requirement that the two
nonhub vertices of each module be private: eight vertices and fifteen edges.
It is NOT globally vertex-minimal among three distinct diamonds with arbitrary
identifications. The global minimum is K5 minus 01 on five vertices, considered
in section 7. These are different graph scopes, not interchangeable layouts.

The new conclusion is stronger than SAT of a necessary relaxation: every D_r,
r>=1, has a displayed one-filled-simple-polygon representation. The same
construction covers joins of two nonadjacent hubs with a disjoint union of
paths. Therefore this precise diamond interface cannot prove obs>=3. This is
not a claim about arbitrary extra cross-module edges or other planar gadgets.

## 2. Complete D3 graph, rotation and cross-module targets

Edges, with each unordered pair written increasingly:

    02 03 04 05 06 07 12 13 14 15 16 17 23 45 67.

Nonedges in variable order:

    01 24 25 26 27 34 35 36 37 46 47 56 57.

The first is the shared internal demand; the other twelve are ALL cross-module
nonedges. None is dropped. A cyclic rotation system is

    0: 2 3 4 5 6 7       1: 7 6 5 4 3 2
    2: 0 1 3             3: 0 2 1
    4: 0 1 5             5: 0 4 1
    6: 0 1 7             7: 0 6 1.

Its faces, using the predecessor-of-reversed-dart convention, are

    023, 0314, 045, 0516, 067, 0712, 132, 154, 176.

The checker covers each of the 30 directed edges once, checks connectedness,
and checks 8-15+9=2. A direct straight plane drawing independently explains
planarity: place the hubs at (0,0),(2,0), and vertex i+1 at (1,i), 1<=i<=6.
Hub edges lie in the two open half-strips, and matching edges connect adjacent
points on x=1. No nonincident vertex lies on an edge and no nonincident edge
pair meets. The checker verifies these assertions with exact rationals.
The same construction works for arbitrary r. The obstacle drawing below is
DIFFERENT and is allowed to have crossings, as the contract permits.

## 3. Quantifiers and the complete conditional CNF

A hypothetical representation first has real coordinates p and at most two
connected obstacles O_0,O_1 avoiding K (all graph points and closed graph edges).
Choose one hitting obstacle for EACH nonedge. Write z_(s,r) for this assignment,
with exactly one of z_(s,0),z_(s,1) true. Each used O_r lies in one open component
U_r of R^2 minus K; every assigned nonedge meets U_r. Paths between its finite
hits are taken INSIDE U_r, not assumed to lie in an arbitrary connected O_r.
C26's positive-clearance replacement allows a GP coordinate choice before
Boolean orientation signs are used. Empty obstacle labels are permitted:
the root asks for AT MOST two obstacles.

At GP coordinates x_ijk means orient(p_i,p_j,p_k)>0 for i<j<k. Variables 1..56
are these triples in lexicographic order. For target index i=0..12, put

    z_(target_i,0)=57+2i, z_(target_i,1)=58+2i.

For ordered distinct target indices i,j, use a side variable

    s_(i,j)=83+12i+j-1_(j>i),

giving variables 83..238. These side bits are separate for each ordered pair.
The complete source table records actual ab,cd, the graph path P, r and mode.
Paths use ALL labels and up to four edges; internal-vertex permutations are
enumerated rather than importing C22's frontier or C26's DFS.

For a path P from a to b and distinct nonedge cd, set
C=(x_cdv : v in P except c,d), J=(x_abv : v internal to P). Odd orientation
permutations negate literals. The four key rows K are

    OR C     OR not s OR OR J;
    OR C     OR s     OR OR not J;
    OR not C OR not s OR OR J;
    OR not C OR s     OR OR not J.

For each r=0,1 prefix EVERY such row by not z_(ab,r) OR not z_(cd,r).
Only a same-obstacle assignment activates it; different labels do not assert
that the two nonedges share a component. For a common label, the pair-local
first-exit/Jordan argument in C26 supplies one side for all its key paths.
We reuse that necessary implication, not the old X4 computation.

Four-point and five-point direction clauses are generated for this graph's
eight vertices from their determinant identities; they have tuple sources,
not fictitious nonedge sources. Exact-one clauses are also explicit. The
quantifier order of the relaxation is

    exists x exists z exists s: direction_rules(x) AND exact_one(z)
                              AND all same-label-guarded path rows.

It is a consequence of an actual representation, not a sufficient coordinate
realizability test. An abstract SAT model by itself would leave geometric
realizability and higher common-component intersections unresolved.

Actual canonical totals: 238 variables, 18,278 clauses, split into
140 four-point, 4,480 five-point, 26 exact-one and 13,632 guarded key clauses.
There are 204 retained graph paths. For a concrete CROSS-module path, ab=24,
cd=01, P=(2,0,4), r=1 has final rows

    8673: -1 -3 -8 -58 -60 95
    8747: -1 -3  8 -58 -60 -95
    9531:  1  3 -8 -58 -60 95
    9605:  1  3  8 -58 -60 -95.

Source consumer source_clause independently reconstructs every row from its
tuple/path record, using a different literal-parity expression and independently
computed variable indices. It checks graph-edge membership, endpoints, path
length, label guard, all canonical signs and the full row census. No new
producer imports C22/C26 or the C21/C25 arrangement implementation.

## 4. SAT, the lexicographic minimum and exactly what was exhausted

The least full Boolean vector, in variable order 1..238 with 0<1, is:

    variables 58,60,62,64,66,68,70,72,74,76,78,80,82 are true;
    EVERY other variable is false.

Thus all 56 direction signs are negative, all targets use label 1, and all
156 side bits are false. A complete finite DPLL procedure, with no assumed
coordinate signs, found this model. A separately written list-based unit
propagator checked the search tree and the minimal branching variable at each
node. It visited 139 nodes, made 100 forced assignments and had no conflict
leaf before reaching the first model. It also matches truth-table answers
and least models for all 256 databases of nonempty nontautological clauses
on two variables. Solver timeouts/caps are errors, never UNSAT.

This is a full-variable SAT decision with a lexicographic proof by propagation
and ordered search. It is NOT a literal enumeration of 2^238 full vectors,
and no exhaustive count of all eight-point orientation tables is claimed.
For SAT such a count is unnecessary: an actual model already prevents UNSAT.
Additionally, bit-parallel truth-table evaluation checked ALL 8,192 exact-one
two-label allocations at the least direction/side assignment; all pass,
including all 8,190 allocations using both labels. This latter test FIXES the
directions and is not mislabeled as an all-direction enumeration.

The least model's direction bits ARE realizable: take p_i=(i,-i^2), 0<=i<8.
All increasing triple determinants are negative. Its complete side projection
matches the least model, not merely its direction prefix. The separately reused
C27 fiber core reconstructs 24 free components and finds component 0 common
to ALL thirteen nonedges. Thus this model does not expose a missing triple
constraint for this graph. Fiber correctness and the general polygon-extraction
lemma remain their own candidate layers. Section 5 supplies an additional
explicit polygon, so the graph-level upper witness does not depend on trusting
that fiber conclusion alone.

CNF (559,184 bytes) SHA-256:
b1123e8b099542a9fbe16d47e36b45f45b8c3c365cabfd58750015aca055bdfc
Full row-source TSV (675,263 bytes) SHA-256:
24ed849f34e70df5561b69f65864428207f188b35579e3ecef3fc95d2519a643

Both complete outputs were actually emitted and hashed. They are deterministic
flat caches generated by the locally executed CLI, not hand-expanded repository
files or a second copy of old X4 clauses. The intended --cnf and --sources CLI
was run locally, but its source publication is pending after a platform block.
The complete least-model assignment, graph, rotation, geometric witnesses and
compact finite observations are stored in diamond-result.json; it is derived
from the actual stdout whose separate hash is preserved. No complete source
release or repository-only replay is claimed.

## 5. A one-simple-polygon representation for EVERY diamond book

More generally, let F be a disjoint union of c nontrivial paths on N>=2 vertices,
ordered so each path occupies a consecutive integer interval. Form G by adding
two NONADJACENT hubs, each adjacent to all N path vertices. D_r is c=r,N=2r.
There are no other edges. This class includes overlapping three-diamond paths,
not just modules with private vertices.

Set M=N^2+1, epsilon=1/16, H=(N+1)^2, q=-M-1/2, and

    delta=1/[32(M+N^2+1)].

Place u=(0,-M), v=(0,-M-1), and leaf l_i=(i,i^2), 1<=i<=N.
Let b(x), 1<=x<=N, be the polygonal line through (i,i^2+epsilon), inserting
(i+1/2,i^2+i+1/2-epsilon) exactly when l_i l_(i+1) is NOT an edge of F.
The obstacle boundary, in order, is

    (-2,q-1/8), (delta,q-1/8), (delta,q+1/8), (-1,q+1/8),
    (-1,H), (1,H), [all vertices of b in increasing x], (N,H+1), (-2,H+1).

Its filled region is the union of a horizontal hub-hit rectangle, a left
vertical corridor, a top bridge and the region b(x)<=y<=H+1. These pieces meet
along full intervals or rectangles, not isolated points. The listed boundary
is simple: the bottom chain is strictly x-monotone in x>=1; the left corridor
has x<=-1; the top bridge is above H; and the hub-hit rectangle lies strictly
between the two hubs and below all leaf points. Their only boundary transitions are the displayed consecutive
ones. This supplies a Jordan polygon without invoking C19's tube construction.
It has N+c+7 corners, hence 3r+7 for D_r (16 for D3).

Graph-edge avoidance follows from explicit inequalities. For either hub,
write its depth as h=M or M+1. Its edge to l_j has

    y=-h+(j+h/j)x,
    y-x^2=(j-x)(x-h/j)<=0 for 0<=x<=j.

All vertices of b are STRICTLY above the parabola, with offsets epsilon or
1/4-epsilon. Convexity of x^2 implies every interpolating piece stays above
it. Thus all hub edges and graph points avoid the leaf part. On a path edge
interval b is exactly that chord plus epsilon, so path edges avoid it too.
All graph segments have nonnegative x and y<=N^2, avoiding the left corridor
and top bridge. In 0<=x<=delta the lower hub's edges have height at most
-M-1+delta(N+M+1)<=-M-31/32, below the rectangle's bottom -M-5/8; the upper
hub's edges have y>=-M, above its top -M-3/8. Here
N+M+1<=M+N^2+1 for N>=2. No edge enters the hub-hit rectangle.

The missing hub segment has midpoint (0,q), strictly inside its rectangle.
For a leaf nonedge i,j, use its midpoint x=(i+j)/2 and chord height
x^2+(j-i)^2/4. If j=i+1 it is an inserted gap tooth and the midpoint is
above b by epsilon. If j-i>=2 and x is integral, b=x^2+epsilon. If x is
half-integral, b is either x^2+1/4+epsilon or x^2+1/4-epsilon. In every case
the nonedge midpoint is STRICTLY above b and below H+1. It is also strictly
between x=1,N. This checks ALL cross-component/nonmodule nonedges, not only
internal diamond demands. One obstacle therefore suffices.

The graph is not complete because uv is absent, so zero obstacles do not
suffice. This gives obs_ext(G)=1, and the witness is already a filled simple
polygon. The coordinates are GP: leaf-triple determinants are Vandermonde
products; hub/leaf/leaf determinants are (j-i)(ij-h)<0; D(u,v,l_i)=i>0.
Vertical uv does not invalidate this vertex GP or the Boolean clauses.
The all-N proof is given above; finite tests alone are not used as induction.

For D3 the two hubs are (0,-37),(0,-38), leaves (i,i^2), 1<=i<=6.
The full 16-vertex polygon and every strict midpoint witness are in the result.
A new ray-parity/closed-segment checker, separate from the fiber algorithm,
checks polygon simplicity, all graph vertices, all edge/boundary pairs and all
nonedge witnesses. The finite suite covers r=1,2,3,4,5,6,8,12.

## 6. Exact failed route, not a root conclusion

The family D_r cannot yield obs>=3: for every r there EXISTS the displayed
one-obstacle placement. This negates an all-placement lower-bound assertion
for any member, not just a necessary CNF trick. It does not assert that EVERY
placement has one obstacle, nor that any two-color assignment is geometrically
realizable, nor that arbitrary extra cross-module edges preserve the witness.
The failed-route proposal is attached to the EXISTING C27 packet, without an
edit to the canonical failed-routes ledger or a new fake admitted Route.

## 7. All unions of exactly THREE diamonds on one missing pair

Permit identifications among the nonhub vertices, but require three distinct
induced diamonds and that the complete graph be exactly their union. The
outer graph F then has exactly three distinct edges and no isolated vertices.
The hubs are universal to F and nonadjacent. If F has a degree-three vertex w,
then hubs u,v,w and its three neighbors form a K3,3 subgraph. This is nonplanar:
a simple bipartite planar graph on six vertices has at most 2*6-4=8 edges,
by Euler and the absence of faces shorter than four, whereas K3,3 has nine.
Thus planarity forces maximum degree at most two.

The complete remaining list is 3K2, P3 disjoint-union K2, P4, or K3. The first
three are covered by section 5; their graph sizes are respectively (8,15),
(7,13),(6,11). The final case gives (5,9), namely K5 minus uv. Its only nonedge
can be blocked by a small square. Explicit rational coordinates, square,
rotation and six face cycles are stored. All 4,096 assignments to its ten
direction bits and two label bits were literally checked; 528 satisfy the
90 direction clauses and two exact-one clauses. This small truth-table check
must not be confused with a full truth-table enumeration for D3.

No graph with four vertices can contain three DISTINCT induced four-vertex
diamonds: it has only one four-subset. Therefore five is globally minimal in
this precise union class. This classification excludes the ENTIRE planar
three-diamond/common-missing-pair union interface, including the vertex-sharing
versions. It does not classify all possible multi-module planar constructions.

## 8. Immediate next interface: what a triple can and cannot force

Let J_s be the nonempty set of free components meeting target s. A target
class can use one connected obstacle iff its J_s have a common member. The
h-obstacle problem is an at-most-h cover of these sets (C23/C26), not merely
pairwise compatibility. However, for three targets, an empty triple intersection
alone cannot force three obstacles if any pair has a common component: use
that component for the pair and any component for the third. For three targets,
tau>=3 is equivalent to PAIRWISE DISJOINT incidence sets (assuming each nonempty).
For at most four targets with every pair compatible, pairing the targets gives
a two-component cover. Thus an h=2 obstruction using only new rank-three
information needs at least FIVE pairwise-compatible targets.

A precise finite next certificate is the ten triples of a five-target set.
Require every triple to have empty common-component intersection. Every two-
label assignment has a monochromatic triple by pigeonhole, so two components
cannot cover the five targets. The abstract incidence with one component for
each pair realizes exactly this set system: each component covers two targets,
all pairs intersect, all triples fail, and minimum cover is three. The checker
stores a failing triple for each of the 32 two-label assignments.

This is currently an ABSTRACT incidence certificate, NOT a planar drawing and
NOT an all-placement graph invariant. Its geometric/all-placement realization
is the next obligation. The selected C18 three-target pattern has six valid
two-label allocations, confirming why that triple alone would not suffice.
The root remains open; no numerical or abstract five-target example is promoted.

## 9. Runs, mutations, publication and admission

Final sources actually ran on CPython 3.13.5, exact rationals, with external
30 CPU / 40 wall seconds, 512 MiB address space, one worker and 4 MiB output.
The observation, complete CNF and complete source-table commands all exited 0.
Their exact times, bytes and SHA-256 are in diamond-execution.json. The new
producer and list consumer import no C22/C26 code. C27 fiber.py is reused at
SHA-256 7209f677207695d220f7766286fdd94867f75d88a42d35b36cdfdef8d709ba35;
its copied bytes were matched. The old C27 full suite was NOT rerun this turn.

Nineteen mutations are rejected: malformed graphs, rotation changes, wrong
path/origin/guard/literal, invalid exact-one assignments, corrupted search tree
or model, graph-point contact, blocked added hub edge, removed gap teeth,
and displaced obstacle. There are also 256 exhaustive two-variable solver
controls. These validate finite interfaces, not universal code correctness.

Reproduce from this candidate directory:

    python -B diamond_checks.py
    python -B diamond_checks.py --cnf
    python -B diamond_checks.py --sources

The three locally executed sources do only finite memory arithmetic plus
stdout. The first diamond_core.py create_file request was nevertheless blocked
by the platform safety check and returned no commit. The other two source
writes were not attempted. No renamed, split, encoded, blob, alternate-tool
or source-attachment workaround was used. Consequently the commands above
are reproduction instructions for the pending source, NOT commands runnable
from this PR alone. All three fingerprints and the exact gap are in the
execution record and verification request. The external wrapper is not published. No network, subprocess, dynamic
execution, credentials, host paths or old C20 source recovery is included
in the separate mathematical/data publication.
The existing seven C27 files remain unchanged; only this supplement and its
artifacts are added to PR32's ONE packet. The packet's existing PR binding
is reused. No prior merged Candidate is transported again.

T: C19 tube/Jordan remains separate; the explicit polygon here does not use it.
A: C27 fiber checks fixed drawings only; the polygon proof has a separate path.
P1: C22/C26 X4 bridge remains untouched and is not rerun.
P2: the precise diamond interface fails, and a five-target rank-three capacity
    invariant for all placements is still missing.
The registry still lacks a compatible trusted mathematical invocation/closure
gate; a request is not a receipt. No Evidence/Result/Solution or protected
record, schema, Harness, verifier or workflow is changed.

Sources: C23 set-cover interface, C26 same-obstacle implication, C27 fiber;
all mathematical constructions and checks above are explicit. Ordinary connected
obstacle convention agrees with the primary article abstract: Berman et al.,
JGAA 21(6), 2017, DOI 10.7155/jgaa.00452 (publisher page reread 2026-09-07).
No novelty claim is made. Canonical statement-faithfulness remains a gate.

best_verified_candidate: none
best_verified_result: none
next_obligation: construct all-placement five-target rank-three incompatibility,
  or prove a uniform upper bound; do not repeat the ruled-out common-pair diamonds.
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
status: NONTERMINAL_CHECKPOINT
