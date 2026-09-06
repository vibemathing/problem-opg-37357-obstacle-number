# Closed-contact bounded polygon encoding (candidate v1)

Candidate: candidate:opg37357-a01-c01-closed-contact-v1
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Owner: math-formalization
Verdict: candidate_only

## 1. Frozen scope and definition mapping

The root asks separately whether some finite planar graph has obstacle number greater than 1 and whether a universal obstacle-count bound exists for all finite planar graphs. This artifact answers neither root question. Its input is a fixed finite simple labeled graph G=([n],E) and an integer m. Planarity is an input promise, not an additional constraint on the visibility drawing. Crossing graph edges are allowed.

An obstacle here is the filled CLOSED bounded region of a simple polygon, including its boundary. Every graph point must be outside this closed region. A pair is visible precisely when its closed connecting segment is disjoint from the obstacle. Thus tangency and boundary overlap block visibility. Segments are not blocked merely by crossing another graph edge.

Two deliberately distinguished interpretations are provided:
- GP-V: graph points are distinct and no three graph points are collinear. Polygon corners may have collinearities and contacts with graph-pair segments.
- GP-ALL: all graph points and polygon corners are distinct and no three of their union are collinear. This matches the explicit general-position convention in Gimbel--Ossona de Mendez--Valtr, arXiv:1706.06992v3, Section 1. GP-ALL is the main bounded target; GP-V is a diagnostic extension, not a silently substituted theorem.

The formula counts polygon list entries, allowing redundant straight corners in GP-V. Removing such entries can only reduce their count. A nonempty simple polygon requires at least three entries. For m<3 the formula is false. A harmless remote triangle is allowed, so satisfiability implies obstacle number AT MOST one, not exactly one; a noncomplete graph needs at least one obstacle. Complete and empty graphs are not omitted.

Allowed background: finite graph basics, the ordered real field, and Euclidean polygon geometry. The geometric proof uses the polygonal Jordan separation and transverse-ray parity facts, not a new oracle axiom. These facts, and their faithful encoding, remain replay obligations for a proof assistant. No solver or kernel run is claimed.

## 2. Polynomial primitives

For two-vectors a,b write cross(a,b)=a_x*b_y-a_y*b_x and dot(a,b)=a_x*b_x+a_y*b_y. Set

    orient(a,b,c) = cross(b-a,c-a)
    distinct(a,b) := dot(a-b,a-b)>0
    On(a,b,c) := orient(a,b,c)=0 AND dot(c-a,c-b)<=0
    Proper(a,b,c,d) := orient(a,b,c)*orient(a,b,d)<0
                       AND orient(c,d,a)*orient(c,d,b)<0
    Meet(a,b,c,d) := Proper(a,b,c,d)
                     OR On(a,b,c) OR On(a,b,d)
                     OR On(c,d,a) OR On(c,d,b).

On is exact closed-segment membership: on the supporting line, c=a+t(b-a), and its dot product is t(t-1)*||b-a||^2. Meet is exact closed-segment intersection, including a shared endpoint, a T-contact, and collinear overlap. In the absence of endpoint-on-segment cases any intersection is interior to both segments and transverse, hence the two strict straddling tests apply. Conversely straddling gives that unique intersection by solving the two line equations. Degenerate zero-length sides are separately excluded below.

Every displayed nonzero test can be replaced by (f<0 OR f>0), and every logical negation can be pushed to polynomial sign tests. There are no square roots, divisions, angle functions, integer quantifiers, or hidden universal real quantifiers.

## 3. A polygon with r entries

For a fixed r in {3,...,m}, introduce real coordinates q_0,...,q_(r-1), interpreted cyclically with q_r=q_0 (an alias, not a duplicate free variable). Let e_a=[q_a,q_(a+1)]. Require:

    distinct(q_a,q_b) for 0<=a<b<r;
    NOT Meet(q_a,q_(a+1),q_b,q_(b+1)) for all nonadjacent side pairs;
    orient(q_(a-1),q_a,q_(a+1)) != 0
        OR dot(q_(a-1)-q_a,q_(a+1)-q_a)<0, for every a;
    sum_a cross(q_a,q_(a+1)) != 0.

The adjacent-side condition allows opposite collinear rays (a redundant straight corner), but forbids backtracking along the same ray. Nonadjacent sides cannot even touch. Consequently the cyclic piecewise-linear parametrization is injective except at its identified start/end, and its image is a simple closed polygonal curve. The final signed-area guard is redundant for a simple polygon, but makes the zero-area exclusion explicit. Orientation may be clockwise or counterclockwise.

## 4. Exterior graph points via a generic ray and real Boolean bits

Introduce p_1,...,p_n. Require their pairwise distinctness and orient(p_i,p_j,p_k)!=0 for every i<j<k. Require NOT On(q_a,q_(a+1),p_i) for every i,a.

Use one shared auxiliary real vector d with dot(d,d)>0 and

    cross(d,q_a-p_i) != 0 for every i,a.

This is an auxiliary choice, not an extra restriction on valid representations: finitely many nonzero vectors q_a-p_i exclude only finitely many directions, so a common d exists. In particular, no tested ray hits a polygon corner.

For z=p_i, a=q_a, b=q_(a+1), define

    A=cross(d,a-z), B=cross(d,b-z), D=cross(d,b-a),
    T=cross(a-z,b-a),
    RayHit(z,a,b;d) := A*B<0 AND T*D>0.

Derivation: a+t(b-a) lies on the full line z+s*d for a unique t in (0,1) exactly when A*B<0. Here D=B-A is nonzero. Taking cross products with b-a gives s=T/D, and s>0 is equivalent to T*D>0. No denominator sign is dropped.

For each i,a introduce reals c_(i,a), b_(i,a) and require

    c_(i,a)*(c_(i,a)-1)=0;
    (c_(i,a)=1 AND RayHit(p_i,q_a,q_(a+1);d))
        OR (c_(i,a)=0 AND NOT RayHit(p_i,q_a,q_(a+1);d));
    b_(i,0)=0;
    b_(i,a+1)=b_(i,a)+c_(i,a)-2*b_(i,a)*c_(i,a);
    b_(i,r)=0.

Use r crossing bits and r+1 parity bits per graph point. Starting from zero, the recurrence stays in {0,1} and is exactly exclusive-or, so the final equation requires an even number of ray crossings. A generic ray crosses the boundary transversely only at side interiors. Travelling from a sufficiently distant point, which is outside a bounded polygon, every such crossing exchanges the bounded and unbounded sides. Thus a nonboundary z has even parity exactly when z is exterior. The explicit On exclusions prevent boundary points from being mistaken for exterior points. This encodes the UNBOUNDED complementary component even for a nonconvex obstacle.

## 5. Visibility and the existential sentence

For every i<j require

    if {i,j} in E: AND_a NOT Meet(p_i,p_j,q_a,q_(a+1));
    if {i,j} not in E: OR_a Meet(p_i,p_j,q_a,q_(a+1)).

Let F^V_(G,r) be the conjunction of Sections 3--5. Let F^ALL_(G,r) additionally require pairwise distinctness and nonzero orientation of every triple of the combined list (p_1,...,p_n,q_0,...,q_(r-1)).

    Phi^X_(G,m) := OR_(r=3)^m EXISTS(all variables of F^X_(G,r)) F^X_(G,r),
    where X is V or ALL.

Each disjunct has its own polygon and auxiliary variables. Finite disjunction commutes with existential quantification after renaming. All index conjunctions and disjunctions are explicitly expanded over the fixed finite input. This is an existential-real/semialgebraic sentence. Each polynomial has total degree at most four, with the notation above fully expanded. GP-ALL contributes O((n+r)^3) tests; visibility contributes O(n^2*r), simplicity O(r^2), and exterior membership O(n*r). Enumerating r<=m is polynomial in n+m, not necessarily in the bit length of binary m. No dummy coincident corners are used to pad smaller polygons.

## 6. Candidate soundness and bounded completeness

Claim C1 (primitive fidelity): On, Meet, and RayHit have the meanings proved in Sections 2 and 4.

Claim C2 (geometric fidelity): the simplicity constraints produce a filled simple polygon, and the parity constraints put every p_i strictly in its exterior.

Claim C3 (soundness): suppose one disjunct of Phi^X is satisfied. C2 supplies an allowed obstacle and the required general position. If {i,j} is an edge, its segment has no boundary intersection. A connected path starting in the exterior cannot enter the filled polygon without meeting the boundary; hence the segment avoids the entire obstacle. If {i,j} is a nonedge, its required boundary intersection is an intersection with the closed obstacle. The visibility graph is therefore exactly G, with r<=m corners. This also treats disconnected graphs and isolated vertices.

Claim C4 (bounded completeness, separately for each X): take a representation of the declared kind with r<=m corners. Its ordered boundary satisfies Section 3. Choose a shared generic d outside the finite excluded set. Define c by actual ray intersections and b by their prefix parities. Every exterior point has final parity zero. Edges miss the boundary. A nonedge whose endpoints are exterior and whose segment meets the closed obstacle necessarily meets its boundary: if an intersection point is interior, follow the segment from an exterior endpoint to its first encounter with the closed polygon. Thus every required nonedge disjunction holds. These coordinates and bits satisfy F^X_(G,r). C3 and C4 give exact equivalence for the declared bounded model, not a proof of either root question.

Candidate dependency order: C1 -> C2 -> C3/C4. A formal replay must supply polygonal separation/parity lemmas and audit the definition mapping; this document is a mathematical candidate, not a compilation artifact.

## 7. Small adversarial cases and rejected simplifications

All cases below are exact coordinate deductions, not reported solver runs. Minimality is claimed only where explicitly stated.

A1. Omit exterior membership: q=((0,0),(6,0),(0,6)), p=((1,1),(2,1)), G=K2. The graph segment lies entirely inside the triangle but meets no polygon side. Boundary nonintersection alone falsely declares it visible. Two graph points and three corners are minimal for this pair-visibility defect.

A2. Replace Meet by Proper: q=((0,0),(1,1),(-1,1)), p=((-1,0),(1,0)). The pair segment touches only q_0. It is blocked in GP-V closed-obstacle semantics, despite having no proper crossing. For G=K2 a proper-only visibility test admits a fake witness; for the empty two-vertex graph it rejects this valid witness. GP-ALL intentionally excludes this contact. This does NOT show that GP-ALL and GP-V differ at graph-existence level. Again n=2,r=3 is minimal for a pair and a polygon.

A3. Use only weak orientation products without interval bounds: [(0,0),(1,0)] and [(2,0),(3,0)] are collinear and disjoint. All orientations vanish. On's dot-product bound is necessary.

A4. Test only proper intersections for polygon simplicity: the cyclic pentagon ((0,0),(2,0),(1,1),(1,0),(0,1)) has distinct corners, no adjacent backtracking, and no proper crossing, but q_3 touches the interior of its nonadjacent bottom side. Full Meet rejects it. No minimum-corner claim is made for this case.

A5. Drop generic-ray constraints: z=(1,1) inside q=((0,0),(2,0),(1,2)), d=(0,1). A strict straddling counter misses the top-vertex hit and returns zero crossings. The required cross(d,q_2-z)!=0 excludes this erroneous auxiliary assignment.

A6. Impose noncrossing graph edges: K4 drawn at the four corners of a square with a remote triangle obstacle is a legitimate GP-V witness with crossing diagonals. A plane-drawing constraint excludes this witness. This is a witness-level diagnostic, not a claim that K4 has no alternative plane representation.

A7. Pad r<m with repeated corners: this violates distinctness and simplicity; use the finite disjunction instead. For m<3, false is correct for one nonempty simple polygon, even when obstacle number zero is possible.

## 8. Unrestricted completeness boundary and next work

This artifact provides no proved or reused cutoff B(n) such that every unrestricted one-obstacle representation has a representative with at most B(n) corners. It does not assert that no such theorem exists: arXiv:2206.15414 is a newly found source lead for a later audit. A finite collection of UNSAT results for chosen m values rules out only those bounded models.

To connect to other obstacle conventions one must also audit conversion of arbitrary connected polygonal obstacles (possibly with holes), open versus closed obstacles, and any perturbation from vertex-only to combined general position. Merely saying 'perturb' does not prove preservation of the SAME corner bound in a closed-contact representation. The canonical contract is less explicit on these conventions than the present atomic target; no contract edit is made.

Next action: audit the obstacle-complexity bound and connectedness hypotheses in Section 3.1 of arXiv:2206.15414, then construct a faithful bounded formula exporter with exact degeneracy regressions. Both admitted obligations remain open. best_verified_result: none. best_verified_candidate: none.

## Sources and replay

See research/artifacts/source-notes/opg37357-a01-c01-sources-v1.md. Replay should expand every finite-index formula, test A1--A7 using exact rationals, prove polygonal separation and parity, and compare both GP modes. The web profile declares no command-execution capability; no Lean/SMT/CGAL execution or verification receipt is asserted. SHA computation and GitHub structural checks are transport bookkeeping only.
