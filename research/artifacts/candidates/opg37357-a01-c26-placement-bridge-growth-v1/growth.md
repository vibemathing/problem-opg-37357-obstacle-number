# C26: lower-bound amplification interfaces and an X4-copy obstruction

Candidate: candidate:opg37357-a01-c26-growth-interface-v1
Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Owner: math-proof
Target: obligation:opg37357-root
Base: c299659f0c7f505a1e9739e6d8329fbde48c30ff

## 1. A correctly guarded many-obstacle necessary system

Fix a finite G and a GP placement. Assign each nonedge s to ONE obstacle
which hits it. Different obstacles may hit it too; this choice loses no
representation. Let z_(s,r) mean that s is assigned color/obstacle r, with
at least one and at most one of these bits true, for 1<=r<=h.
Retain the orientation rules [4],[5] from README.md globally. For every
ordered pair s=ab,t=cd, retained path P, and r, replace each [K] clause C by

    not z_(s,r) OR not z_(t,r) OR C.                 (G_h)

The pair-local separation lemma proves necessity: when s,t share obstacle r,
one side works for their key paths. When their assigned colors differ, the
corresponding guarded clauses are already true. The same side variable for
an ordered pair may be reused for all r because exact-one colors allow at
most one r for which both guards activate. Per-color side variables would
also be valid, but are unnecessary.

This extension is not the incorrect demand that ONE side rule hold between
nonedges blocked by unrelated obstacles. It has 21h additional color bits
for X4; retaining the 420 side bits is sufficient. At h=1 unit color bits
reduce the system to the exact old CNF. No new SAT/UNSAT claim for h>=2 is
made. The finite truth audit tests the guard and key-variable elimination,
not satisfiability over all orientations.

For a fixed orientation table, make a conflict graph R_4 on the nonedges:
join s,t when either ordered direction has two retained key paths on opposite
sides, so both choices of its side variable are forced. The colored path
part of G_h has an extension iff this graph is h-colorable. In one direction
a shared color would activate contradictory side requirements. In the other,
choose a proper coloring; for every same-color ordered pair choose its
unconflicted forced side (or false if neither side is forced); all other
pairs have inactive guards. This assertion concerns the key part conditional
on orientation rules; arbitrary unrealizable orientation tables still need
not represent graph drawings.

Consequently, for a genuine drawing, h obstacles give a proper coloring of
R_4. An all-placement lower bound would follow from a proof that every
REALIZABLE orientation table gives chromatic number >h, or from UNSAT of
the entire necessary G_h over all orientation variables. A handful of
geometric conflict graphs is not such a proof.

## 2. Hyperedges and genuinely additive demand

Let J_s be the free-component incidence sets of a fixed drawing. Suppose
none is empty. Form a finite incompatibility hypergraph M_p on nonedges,
whose hyperedges are all inclusion-minimal nonempty sets S with

    intersection_(s in S) J_s = empty.

Every color class of nonedges can be handled by one connected obstacle iff
it contains no such hyperedge: if its total intersection were empty, a
finite inclusion-minimal empty subfamily would be a hyperedge. Conversely
choose one component in each nonempty color class's common intersection
and connect finitely many witnesses within it. Thus, under the explicit
connected/exterior convention, the fixed-drawing optimum equals the weak
chromatic number of M_p. Empty target lists have value zero. A target with
J_s empty is a singleton hyperedge and makes a representation impossible;
this is handled as infinity rather than colored normally.

Pair-key conflicts supply only SOME rank-two hyperedges. C18's selected
three-target example has pairwise common components but an empty triple
intersection, illustrating why rank-two information alone can be weaker.
This is a finite reformulation of the incidence-cover condition, not a new
all-placement obstruction.

Additive-demand lemma. Let S_1,...,S_t be disjoint target classes. Assume
at a drawing that (i) each class needs at least r_i distinct obstacle labels,
and (ii) no connected obstacle can hit a target of S_i and a target of S_j
for i!=j. Then every representation needs at least sum_i r_i obstacles.
Proof: select a hitting obstacle for each target. Condition (ii) makes the
sets of labels used by different classes disjoint, and (i) lower-bounds each
cardinality. Summing gives the claim. A graph-family lower bound requires
these hypotheses for EVERY hypothetical placement (with classes possibly
chosen after the placement). Nothing here imposes the hypotheses by fiat.

A more flexible capacity version: if t local demands each require r labels
and any one obstacle can participate in at most b of them, count pairs
(demand, participating label). There are at least rt and at most bh, so
h>=ceil(rt/b). A uniform constant b is the missing geometric/combinatorial
hypothesis, not something implied by induced-subgraph inheritance.

These are amplification-capable inequalities. Their utility depends on
constructing planar graphs which FORCE cross-demand incompatibility or
bounded capacity at all placements. The next obstruction shows why the
simplest X4-template approach does not force it.

## 3. Induced X4 copies in a planar graph share no nonedge

Theorem (candidate, all finite planar ambient graphs). For distinct vertex
sets A and B each inducing X4 in a planar graph G,

    (nonedges inside A) intersect (nonedges inside B) = empty.

This is a statement about induced copies in the abstract planar G, not a
restriction that its obstacle drawing be plane.

First, X4 is 4-vertex-connected and maximal planar. Planarity follows from
two four-cycle wheels capping a triangulated antiprism annulus; the annulus
has faces (a_i,b_i,a_(i+1)) and (a_(i+1),b_i,b_(i+1)). Capping its two boundary
cycles by N and S gives an explicit sphere embedding, hence a planar graph.
There are 10 vertices and 24=3*10-6 edges. The full finite 4-connectivity
certificate consists of a spanning tree after each of the 176 deletion sets
of sizes 0,1,2,3. growth.py constructs these and a different union-find
consumer checks their exact deletion census, graph-edge membership,
acyclicity and spanning property. These 176 cases EXHAUST the deletion
condition for this fixed graph, not arbitrary graph order. Minimum degree
is four (also checked), so the connectivity is exactly four.

Fix ANY plane embedding of the ambient planar G and restrict it to A.
Every face of the induced X4 is bounded on the sphere by a triangle. Indeed
its connected embedding has f=2-10+24=16 faces; 4-connectivity excludes
bridges and repeated face boundaries, and every face has length at least
three. The sum of face lengths is 2*24=48=3f, so all have length three.
No plane-embedding uniqueness theorem is needed.

Since A and B have the same cardinality but are distinct, choose v in B-A.
In the restricted embedding v lies in an open triangular face f of A, with
boundary vertex set T of cardinality three. Its boundary is a Jordan curve.
Any path in G from inside f to outside its closure must meet T, because it
cannot cross an edge of A in the plane embedding.

Suppose B had a vertex w outside the closure of f. In the induced B graph,
removing T intersect B (at most three vertices) would separate v from w,
contradicting B's 4-connectivity. Therefore ALL vertices of B are in the
closure of f. In particular A intersect B is contained in T; there is no
other A vertex inside an A face. T is a clique in A and in G. Any pair of
vertices shared by the copies is consequently an EDGE, not a nonedge.
This proves the theorem. The argument applies also to the exterior face
by working on the sphere; it is not a hidden bounded-face assumption.

The plane embedding used in this proof is solely an auxiliary certificate
of the ABSTRACT overlap constraint. Actual obstacle placements can cross
edges arbitrarily. The theorem quantifies over the ambient planar graph
itself before choosing any obstacle placement.

## 4. A sharp limitation of copy-only lower-bound amplification

Define H_X(G) with the nonedges of G as vertices and one hyperedge N_A
consisting of all 21 internal nonedges of each distinct induced X4 copy A.
The C22 obstruction, combined with the placement bridge, implies that every
obstacle assignment is a proper weak coloring of this hypergraph: if all
21 targets of a copy were assigned to the SAME connected obstacle, keeping
only that copy's vertices and that obstacle would contradict the one-obstacle
X4 candidate. This is conditional on acceptance of that candidate chain.

The theorem of section 3 says all nonempty hyperedges N_A are PAIRWISE
DISJOINT for planar G. Color one nonedge in each N_A red and its remaining
20 nonedges blue; color all other nonedges arbitrarily. This is a proper
2-coloring. Thus, if any copy exists,

    chromatic(H_X(G)) = 2.

No copying count, no number of vertices, and no triangular clique-sum of
X4 blocks changes this fact. Consequently the relaxation consisting ONLY
of these monochromatic-copy prohibitions can NEVER prove obstacle number
at least three for a planar graph. This is a proof-method limitation, NOT
an upper bound of two on G's actual obstacle number. Cross-block key-path
clauses and higher incompatibility sets are extra information not present
in this relaxation; they may still be useful.

The explicit 17-vertex,45-edge test glues two X4 copies on their triangle
(0,2,3). The copies have disjoint 21-target sets and a displayed proper
2-coloring of those demand sets. The example verifies the finite certificate
format; the universal theorem above, not this one example, proves the barrier.
A separate abstract Fano hypergraph control has weak chromatic number three;
it demonstrates that the general coloring interface can express a growing
lower bound. It is explicitly NOT realized as the incompatibility hypergraph
of any planar graph drawing, and supplies no planar obstacle-number example.

## 5. Next obligation and assurance boundary

Candidate-local layers remain separate: A is the fixed incidence interface,
T is the thin-disk/Jordan corner construction, P1 is the all-placement X4
bridge/old contradiction, and P2 is uniform graph-order control. The new
barrier is about one proposed P2 proof method, not a counterexample to P2.
It is suitable for a failed-route PROPOSAL named 'X4-copy-nonmonochromatic-only',
not a direct edit to the protected failed-routes ledger.

Next actionable growth lemma: force a cross-block key-path conflict or an
inclusion-minimal empty common-component set that is NOT confined to one
induced maximal planar block; obtain a lower bound on the chromatic number
of this enlarged demand system uniformly over all realized placements.
Before claiming additive growth, prove the palette-disjointness or capacity
hypothesis in section 2. The all-placement X4 lower bound stays two until
this is supplied. Guarded h=2 constraints are a finite falsifier for proposed
compositions; a SAT result would only reject that necessary-condition route,
not certify a two-obstacle drawing.

Sources: C22 universal key-path argument and CNF; C25 placement atlas; C23
incidence optimum; classical polygonal Jordan separation and Euler's planar
formula. The overlap argument is supplied explicitly, with no novelty claim.
The newly executed finite arithmetic/graph checks have no separate verifier
trust domain. No compatible trusted invocation/closure receipt is registered.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
status: NONTERMINAL_CHECKPOINT
