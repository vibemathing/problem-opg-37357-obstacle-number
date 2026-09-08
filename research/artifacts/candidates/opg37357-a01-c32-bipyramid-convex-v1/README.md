# Cyclic bipyramids: a uniform two-convex-obstacle counterfamily

Candidate: candidate:opg37357-a01-c32-bipyramid-convex-v1
Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph binding: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Issue: #3
Execution/base revision: 1a5eefd266401b903f15de10c07b3aff7d3f9773
Primary owner: math-proof, supported by bounded exact computation.

## 1. New delta and the two-stage decision

The seven-vertex pentagonal bipyramid is a new nonleaf seed. Its six nonedges
were fixed before screening and ALL are retained. A full all-simple-path
necessary h=2 CNF and complete common-component selectors accept an explicit
real placement. Two disjoint filled CONVEX polygons represent the whole graph.
The counterplacement therefore negates an all-placement lower bound three for
this seed; this is not merely a SAT relaxation or one bad drawing.

The construction extends symbolically to EVERY cyclic bipyramid B_N, N>=4:

    for every N>=4 there exists an injective placement and two disjoint
    filled convex polygon obstacles representing B_N.

Thus this entire minimum-degree-four family cannot supply obs>=3. This is
not a uniform upper bound for all planar graphs, nor a proof obs(B_N)=2.
No candidate survived stage one for a stage-two universal lower-bound proof.
No all-order-type enumeration or unsatisfiability proof is claimed.

Fresh main advanced while the initial local tetrahedral-port result was being
checked. The same graph, SAT counts and triple cut were already merged in C31
at 1a5eefd266401b903f15de10c07b3aff7d3f9773. They are NOT retransported here.
Instead this packet uses the published C31 compiler and polygon checker by
exact blob identity, and adds only this different graph family and proof.
C27 star/diamond gluing and C29's 27 prism connectors are not re-enumerated.
The N=4 octahedron is only a boundary regression of the uniform formula, not
an additional claimed discovery or another connector SAT census.

## 2. Frozen seed and abstract planarity

B_N is the join of two nonadjacent hubs u,v with the cycle on leaves l_1,...,l_N.
Its edges are u-l_i, v-l_i, l_i-l_(i+1), and l_N-l_1. Thus |V|=N+2, |E|=3N.
For N>=4 every leaf has degree four and each hub has degree N. There are no
leaf ports. The added closing cycle edge is essential: this is NOT the old
join of two hubs with a linear forest.

For the seed N=5, u=0,v=1,l_i=i+1. Its complete edges are

    02 03 04 05 06 12 13 14 15 16 23 26 34 45 56.

The six frozen targets, also the COMPLETE nonedge list in variable order, are

    01 24 25 35 36 46.

Put the cycle on an equator of the sphere and the hubs in opposite hemispheres.
Each hemisphere is triangulated by its hub spokes. The disjoint hemispheres
provide a simple sphere embedding, hence abstract planarity for every N.
The seed's directed triangular faces are

    023 132 034 143 045 154 056 165 062 126.

A successor-of-reversed-dart rotation is

    0:2,6,5,4,3   1:2,3,4,5,6   2:0,3,1,6
    3:0,4,1,2     4:0,5,1,3     5:0,6,1,4     6:0,2,1,5.

All 30 directed edges occur once; 7-15+10=2. This auxiliary embedding is
never imposed on obstacle placements. The actual seed representation has ten
proper graph-edge crossings, which the problem convention permits.

## 3. Uniform explicit construction

Fix an arbitrary integer N>=4. Set

    M=N^2+1, epsilon=1/[16(N+1)],
    delta=1/[32(M+N^2+1)], q=-M-1/2.

Place u=(0,-M), v=(0,-M-1), and l_i=(i,i^2), 1<=i<=N.
Let D_N consist of all nonadjacent cycle pairs (i,j): j>=i+2, excluding (1,N).
Let Q_N be the convex hull of their midpoints

    m_ij=((i+j)/2,(i^2+j^2)/2), (i,j) in D_N.

D_N is nonempty for N>=4. Even if Q_N is a segment, adding a square gives a
nondegenerate convex polygon. The two CLOSED filled obstacles are

    P_0=[-delta,delta] x [q-1/8,q+1/8],
    P_1=Q_N + [-epsilon,epsilon]^2.

All witnesses use interpolation parameter 1/2. The sole hub nonedge uv is
assigned to P_0; every leaf diagonal is assigned to P_1. These are all nonedges.
The two polygons are disjoint because P_0 has x<=delta<1, whereas P_1 has
x>=2-epsilon>1. No qualitative tube-to-polygon result is a premise.

### 3.1 P_1 stays strictly inside the cycle polygon

For each consecutive side k,k+1 define

    L_k(x,y)=y-(2k+1)x+k(k+1).

At a leaf l_i its value is (i-k)(i-k-1), a nonnegative even integer. At a
nonedge midpoint at least one endpoint is not k or k+1, hence L_k(m_ij)>=1.
By affinity L_k>=1 throughout Q_N. Under the square thickening, L_k decreases
by at most (2k+2)epsilon<=2N epsilon<1/8, so it stays strictly positive on P_1.

For the closing side l_1-l_N define U(x,y)=(N+1)x-N-y. At l_i,
U=(i-1)(N-i). Since (1,N) is excluded from D_N, at least one diagonal endpoint
is internal and contributes at least N-2. Consequently U>= (N-2)/2>=1 on Q_N.
Thickening reduces U by at most (N+2)epsilon<1/8. Thus P_1 is strictly below
the closing chord as well as strictly above every consecutive side.
These are exactly the interior halfplanes of the strictly convex leaf polygon.
In particular every whole closed cycle edge avoids P_1, including the NEW
closing edge. Omitting this last inequality would not prove the cyclic case.

### 3.2 Hub spokes avoid P_1

At every diagonal midpoint y-x^2=(j-i)^2/4>=1. Convexity of x^2 implies
that y-x^2>=1 throughout Q_N. Its x coordinates lie in [1,N]. At any point
of P_1, therefore,

    y-x^2 >= 1-(2N+1)epsilon-epsilon^2 > 3/4.

For a hub of depth h in {M,M+1}, its segment to l_j has, for 0<=x<=j,

    y=-h+(j+h/j)x,
    y-x^2=(j-x)(x-h/j)<=0,

since h>N^2>=j^2. Every entire hub spoke is at or below the parabola, whereas
P_1 is strictly above it. Leaf points themselves are on the parabola and the
hubs are below it. Thus all graph points and spokes avoid P_1.

### 3.3 The hub rectangle avoids every graph edge

All graph segments have x>=0. On 0<=x<=delta, upper-hub spokes have y>=-M,
above P_0's top -M-3/8. Lower-hub spokes have

    y<=-M-1+delta(N+M+1)<=-M-31/32,

below P_0's bottom -M-5/8; here N+M+1<=M+N^2+1. Cycle segments have x>=1.
The hub points are outside the rectangle. The point (0,q), the midpoint of uv,
is strictly inside P_0. Every m_ij belongs to Q_N and has an epsilon-square
neighborhood inside P_1, so every leaf nonedge is strictly blocked. This proves
the complete visibility equivalence for the two filled convex polygons.

### 3.4 General position and termination

Leaf-triple determinants are nonzero Vandermonde products. For i<j,
D((0,-h),l_i,l_j)=(j-i)(ij-h) is nonzero, and D(u,v,l_i)=i>0.
Hence vertex general position holds for all N, despite the vertical hub line.
The construction is finite: O(N^2) rational midpoints, their finite convex hull,
a Minkowski sum with four corners, and one rectangle. The source caps N at 24
for bounded execution; the preceding symbolic proof has no such cap. The six
executed sizes are regression checks, not an induction or an asymptotic argument.

## 4. Exact seed polygons and direct checks

For N=5 the points are

    (0,-26),(0,-27),(1,1),(2,4),(3,9),(4,16),(5,25).

P_0 is [-1/1664,1/1664] x [-213/8,-211/8]. The ordered corners of P_1 are

    (191,479)/96, (193,479)/96, (289,959)/96,
    (385,1631)/96, (385,1633)/96, (383,1633)/96,
    (335,1393)/96, (239,817)/96, (191,481)/96.

They are strictly convex and have 4 and 9 corners. Exact rational winding and
closed-segment tests check 29 nonadjacent polygon-side pairs, 195 graph-edge/
polygon-side pairs, 14 vertex exclusions and all six strict midpoint hits.
The full input and witness are in observation.json and the deterministic report.
No image recognition or floating geometry is used.

## 5. Complete guarded CNF and what was actually decided

The existing C31 guarded_cnf.py is reused, not copied into this packet. It
enumerates every simple path twice (DFS and internal permutations), includes
all ordered four- and five-point implications, and reconstructs every retained
row from its source via a second parity rule. Seed totals are

    71 variables = 35 directions + 6 label bits + 30 ordered-pair side bits;
    6630 clauses = 70 four-point + 1680 five-point + 4880 guarded path rows;
    395 paths: 20 length2, 55 length3, 90 length4, 130 length5, 100 length6.

There is no path-length truncation and no increasing-label path restriction.
Every path clause R for s,t is replaced by

    (z_s OR z_t OR R) AND (not z_s OR not z_t OR R).

Necessity uses C27's common-free-component Jordan lemma, not a plane rotation:
oppositely sided key paths can be subdivided at crossings and loop-erased to
form a graph-edge Jordan curve. It separates the relative interiors of the two
nonedges. A path joining their witnesses in ONE free component would cross that
curve at its first exit, a forbidden graph-edge hit. This gives one side choice
for every retained path of an ordered target pair. Different labels do not
activate the common-component premise. The four/five families follow from the
four-point area sum and five-point determinant product identities.

To handle any hypothetical nongeneric representation, join finitely many
assigned nonedge hits within each open free component. The compact path union
has positive distance d from graph points and closed edges. Thicken by d/4,
keep the obstacles fixed, and move endpoints by one common eta<d/8, also below
a quarter of vertex separation. Fixed nonedge interpolation parameters keep
their hits interior; closed edges retain clearance. Only then choose general
position inside the safe box. This is a necessary existence reduction, not
an assumption that every original placement is generic or planar.

The unfixed-direction necessary CNF is SAT by its displayed full assignment.
Only the 64 colorings at the CONSTRUCTED direction table were exhausted. No
2^35 direction enumeration, real quantifier elimination, or global lexicographic
minimum is claimed. Direction true IDs are 1..5 and 26..35. The witness's full
true-variable list is

    1,2,3,4,5,26,27,28,29,30,31,32,33,34,35,
    37,38,39,40,41,53,54,65,66.

All other variables are false. Labels use little-endian integer codes: word62
assigns 01 to label0 and the other five nonedges to label1; word1 exchanges them.
These are the two accepted labels at this placement. This is a realizable
straight-point table, not merely a pseudoline assignment.

## 6. Full common-component selectors and higher-order audit

The reused C27 fiber code computes TWENTY free components for the seed drawing.
Its entire incidence on the six nonedges is

    J_01={0},
    J_24=J_25=J_35=J_36=J_46={18}.

For each obstacle label introduce one-hot variables u_(r,j) choosing ONE of
these actual components. Add z_s OR OR_(j in J_s) u_(0,j), and
not z_s OR OR_(j in J_s) u_(1,j). This adds 40 variables and 394 clauses.
With the original formula and 35 fixed-direction units there are 111 variables
and 7059 clauses. All 64*20^2=25,600 label/component-pair cases were evaluated;
only (word62,0,18) and (word1,18,0) survive. Their full CNF models also pass.

This profile has a topological explanation for EVERY constructed B_N drawing.
The open convex cycle polygon contains no spokes, since those lie below the
parabola. It is one free component and every leaf diagonal lies wholly inside
it. The relative hub segment x=0 is connected and free, in another component.
The cycle is a Jordan boundary separating these components. The other free
components created by spoke crossings are unused by any target nonedge.

Consequently every inclusion-minimal empty intersection consists of the hub
nonedge and ONE leaf diagonal. The complete higher-order audit is rank two:
any empty family of three or more targets contains one of these disjoint pairs.
There is NO irredundant higher-rank clause to extract from this real model, and
no faithful clause can eliminate its actual two-obstacle representation.
Inventing a ternary prohibition would not advance the universal quantifier.
This is a proved higher-order limitation of this family, not a claimed new
rank-three obstruction. The desired new higher-order forcing remains open.

## 7. Executions, failures, source reuse and next obligation

The frozen new sources are bipyramid.py and replay.py. Runtime dependencies are
C31 guarded_cnf.py and witness_check.py, and C27 fiber.py, all materialized from
fresh connector-read text and matched to their complete Git blob identities.
They are not reuploaded. The executions use exact Fraction/integer arithmetic,
CPython3.13.5, one worker, 30 CPU/40 wall seconds, 512 MiB and 4 MiB output caps.
Six sizes N=4,5,6,8,12,20 passed the same explicit construction and 16 damaged
source/graph/model/polygon controls were rejected. A mutation refusal does not
assert that the damaged graph lacks obstacle representations.

Run from this candidate directory:

    PYTHONPATH=../opg37357-a01-c31-tetra-wall-v1:../opg37357-a01-c27-fiber-guard-gluing-v1 python -B replay.py

The --cnf and --origins flags emit the complete seed formula and path/row
provenance. Both caches and the full fixed-incidence report were actually
emitted and hashed. They are included in the local replay bundle, but are
not separately committed when source emitters suffice. observation.json is
an explicitly identified compact projection of actual report.json, not raw
stdout. execution.json preserves actual stdout hashes and every command.

Three preliminary convex orders of this NEW graph were checked before the
uniform construction. Two had fixed-direction infeasibility; a third admitted
a two-component cover. None is an all-placement negative. These observations
are development checks, not additional graph families or a complete order census.
The precise new failed-route proposal excludes ALL B_N, N>=4, from an obs>=3
lower-bound construction, using the uniform explicit polygons. It does not
exclude arbitrary nonleaf couplings or all minimum-degree-four planar graphs.
No protected failed-route ledger is edited.

Next atomic step: use a different simple planar graph, not a cyclic bipyramid
or tetrahedral face-port graph, and seek a realizable non-Helly incidence core
whose necessary guards can be certified across its placement regions. The
missing bridge remains universal coverage of ALL realizable placement regions,
including the positive-clearance reduction for degeneracies. Neither the
complete selector calculation at one drawing nor this family's upper bound
supplies that bridge for a different graph.

C29 integer3/fractional2 and C31 guarded Jordan-word results are retained as
prior candidates. No new version of those computations, no trusted verifier
receipt, EvidenceLink, Result, Solution, or unrestricted root closure is made.
The exact obstacle number of even the seed remains unproved across placements.

Reasoning audit: graph and all six targets frozen; dependencies pinned; explicit
convex polygons and strict witnesses; exact closed-contact tests and mutations;
all-N inequalities rather than finite inference; finite loop/hull termination;
empty-component behavior and label reuse separated; no unjustified symmetry
quotient, rotation restriction, probabilistic claim, or hidden order-type leap.
