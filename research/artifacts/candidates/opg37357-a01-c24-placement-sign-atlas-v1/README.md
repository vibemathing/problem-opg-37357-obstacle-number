# C24: a realizable placement-sign atlas and a six-vertex obstruction to coarse compression

Candidate: candidate:opg37357-a01-c24-placement-sign-atlas-v1
Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Base: 2d029e51571e1e62392055a8dbbd864e3d70cbbf
Primary owner: math-proof

## 1. Exact statement and why another placement layer is needed

Use C23's explicit convention: graph points are injective, K is their union
with CLOSED straight graph-edge segments, and every nonempty connected
obstacle avoids K. The least number of obstacles at a fixed placement p is
its nonedge/free-component transversal number tau(G,p), with tau=0 for a
complete graph. Equality with the simple-polygon convention uses C19's
separate conversion, and contract faithfulness remains an admission issue.

The current root gap is not an arbitrary corner budget or one bad drawing:
Q2 asks for exists h, forall finite planar G, exists p, tau(G,p)<=h.
C23's fan controls already show that growing tau at selected p is insufficient.
A tempting next shortcut is to treat tau as determined just by the signs of
orient(p_i,p_j,p_k). Section 6 gives a six-vertex planar graph for which this
is FALSE, even with both compared placements in general position and without
non-vertex triple concurrence among the pair support lines.

This file supplies a finer, finite signature that DOES determine tau on an
explicit dense placement domain. Every signature must still be geometrically
realizable. The number of signatures grows with n; the resulting reduction
is not a proof of a uniform h or a placement-universal lower bound.

Claim C24.1 (candidate). For each fixed labeled graph on n>=3 vertices there
is an explicitly listed finite collection of integer-coefficient polynomials
in 2n vertex coordinates, each of total degree at most FIVE, such that:
(a) on the domain D* below, the signs determine the complete free-component
incidence hypergraph and hence tau(G,p);
(b) minimizing tau over REALIZABLE signatures on D* gives the unrestricted
connected-obstacle parameter;
(c) simple-polygon equality is a further use of C19, not a signing receipt.

The proof covers arbitrary finite n. The supplied exact interpreter is
bounded to 3<=n<=6; no executable solver for signature realizability, no
enumeration of every signature, and no arbitrary-n runtime is claimed.

## 2. Dense domain and the placement quantifier

Let D* consist of placements satisfying all three conditions:
- all x_i are distinct;
- every vertex triple orientation is nonzero;
- every two DISTINCT pair support lines are nonparallel.
These conditions imply injectivity and distinct pair support lines. They do
NOT forbid three or more lines being concurrent. In fact all n-1 pair lines
incident to a graph vertex concur there, so a blanket no-three-lines condition
would make the domain empty for n>=4. Equal x-coordinates of different line
intersections are also allowed. Zero event comparisons are retained below.

D* is dense. Its excluded conditions are the zeros of finitely many nonzero
polynomials: x differences, triple determinants and determinants of two
segment direction vectors. Each latter polynomial is nonzero: shared-endpoint
pairs give a vertex-triple determinant; for disjoint endpoints there are
placements with visibly nonparallel directions. A nonzero real polynomial
cannot vanish on an open box, by induction on the number of variables and the
finite-root property in one variable. The product of the finitely many
nonzero polynomials is nonzero, so the complement of its zero set is dense.

A density statement ALONE would not preserve an obstacle representation.
Here is the required robust conversion. Given finitely many connected
obstacles at any injective p, assign every nonedge to a blocking obstacle,
delete unused obstacles, and in each relevant free component replace the
assigned hits by a finite union T_j of polygonal paths connecting them. Such
paths exist because the component is open and polygonally path connected
(C19/C20, not path connectedness of the original obstacle). T_j is compact
and disjoint from K. A sufficiently small closed neighborhood of T_j is
compact, connected, avoids K and contains each assigned witness in its
interior. Different components can be kept disjoint if desired.

Keep these new obstacles fixed. Graph points and edge segments have positive
clearance from them. Keep the interpolation parameter t_s in (0,1) of each
chosen nonedge witness; when endpoints move, (1-t_s)p_i+t_s p_j moves
continuously and remains inside its assigned obstacle for sufficiently small
movement. Hence an open box of graph placements preserves every edge and
nonedge and uses no more obstacles. Choose p' in that box intersect D*.
It may be rational, since this intersection is open and nonempty. This is a
witness-dependent density argument, not a coordinate-bit bound.

Therefore min_p tau(G,p) = min_(p in D*) tau(G,p). This is an equality of
MINIMA, not a claim that tau is unchanged at every perturbation or that a
supplied drawing can be replaced without changing its coordinates. The six-
vertex example below deliberately exhibits such a change. C19's tube theorem
is not needed for this robust connected-set argument. For n<=1 the graph is
complete and the minimum is zero; for n=2 it is zero for the edge and one
for the nonedge. These small orders do not need the atlas.

## 3. Explicit polynomials and their degrees

Index all M=C(n,2) unordered vertex pairs a=(i,j), i<j, lexicographically.
This list includes graph edges AND nonedges. For homogeneous P_i=(x_i,y_i,1),
put

    L_a=P_i cross P_j=(A_a,B_a,C_a)
        =(y_i-y_j, x_j-x_i, x_i*y_j-y_i*x_j).

For each unordered pair of distinct lines u=(a,b), a<b, put

    I_u=L_a cross L_b=(X_u,Y_u,W_u).

The coordinate degrees of L are 1,1,2 and those of I are at most 3,3,2.
On D*, B_a and W_u are nonzero; the intersection is (X_u/W_u,Y_u/W_u).
For all unordered pairs u<v of the R=C(M,2) intersection OBJECTS include

    Hx_uv = X_u W_v-X_v W_u,
    Hy_uv = Y_u W_v-Y_v W_u.

Include signs of every B_a, every vertex triple determinant, every W_u,
and every Hx_uv,Hy_uv. Thus there are at most

    M + C(n,3) + R + 2*C(R,2)

polynomials, of degree at most five. Some comparisons vanish identically or
at forced concurrence; these are permitted zeros, not discarded cases.
Signs are -1,0,+1. In particular, the sign of an x difference between two
intersection points is sign(Hx_uv)*sign(W_u)*sign(W_v), NOT sign(Hx_uv)
alone. The analogous statement holds for y. Reversing object order changes
the comparison sign, including when denominator signs differ.

For n=6 this conservative list has 11,060 entries. Its large size is an
explicit limitation, not an assertion of practical exhaustive search.

## 4. Reconstructing the finite arrangement from signs only

The following deterministic procedure is conditional on the signature being
realizable on D*. It receives no obstacle coordinates and, after the sign
extraction, no graph point coordinates.

### 4.1 Sweep events, including concurrence and equal-x batches

Every pair line is nonvertical and has a distinct slope m_a=-A_a/B_a.
The sign of m_a-m_b is -sign(W_ab)*sign(B_a)*sign(B_b).
Consequently the line order from bottom to top far to the left is the order
of decreasing slopes, known from the signature.

Sort all intersection objects by x using Hx and the W signs. Batch equal
x values. Within each batch, use Hy/W to group objects that are the SAME
point and order distinct points by y. The set of lines incident to one point
is the union of the endpoints of its intersection objects. It includes all
pairwise objects from that line set. At just left of that event, these lines
form a contiguous block in vertical order: all other line heights are
separated from their common event height, while their own gaps tend to zero.
Immediately right, the block is reversed, because the slopes are distinct.
Different-y blocks in the same x batch are disjoint, since a nonvertical line
has only one point at a given x. Reverse all these blocks. This reconstructs
the line order in every open vertical strip between consecutive event batches,
including the two unbounded strips. No x-simple or simple-arrangement
assumption has been slipped in.

### 4.2 Every 2-cell and open 1-face is accounted for

At a strip's vertical test line there are M+1 open bands. Below all lines the
signs are (-sign B_a)_a; passing a line upwards changes its sign to +sign B_a.
Record these M+1 strict sign vectors for every strip and deduplicate. A strict
sign vector determines one open convex cell, so duplicate vectors are the
same cell. Every open 2-cell contains points whose x avoids the finite event
x set; it therefore occurs in at least one strip. This proves completeness.

On each pair line a, its distinct event points are sorted by the global x
order; refine it at all these points. Every graph vertex is already such an
event for n>=3, using any other pair line at that vertex. Hence graph endpoints
are included without a separate unrecorded ordering test. Between consecutive
cuts, the incident cells immediately above and below the line can be read in
any global strip inside that open interval. No other line intersects it
there, so the two cell identities are constant along that entire open face.

Declare an open face forbidden iff its line is a graph edge and it lies
between that edge's two endpoint events. A graph segment occupies only its
finite interval, NOT the whole line. Distinct edge support lines can meet an
open face only at an event, already removed. A zero-face is forbidden iff it
is a graph vertex or lies on a closed graph-edge interval. Free zero-faces
need no new adjacency: their incident sectors connect through the surrounding
free one-faces in a sufficiently small free ball. This is precisely C20's
component argument with a finer arrangement including nonedge support lines.

Add an adjacency edge between the incident cells of each FREE open face.
Every added crossing occurs in actual free space. Conversely every free
point is locally incident to cells having the same adjacency-component label;
this label is locally constant on the open complement of K. Thus finite graph
components are in bijection with the actual free components, as in C20.
An isolated graph point at a zero-face does not itself split a 2-cell.

Each nonedge lies on its own pair line, distinct from graph-edge lines. Its
open faces between its endpoints are free; their component labels give its
entire incidence set. A free event hit cannot add a missing label alone:
free space is open, so the same label occurs on a neighboring nonedge interval.
Forbidden events cannot be witnesses. Therefore the whole nonedge/component
hypergraph, and its minimum transversal tau, are determined by this signature.

### 4.3 Realizability remains a separate and essential obligation

For a signature sigma define Phi_sigma to be the existential real sentence
on the 2n coordinates requiring D* and each listed polynomial to have its
prescribed sign. For a fixed G,h, existence of a connected-obstacle
representation with at most h obstacles is equivalent to existence of a
signature sigma such that Phi_sigma is true AND the decoded cover is <=h.
There are finitely many sigma, but the realizability part cannot be erased.

An interpreter may reject malformed or combinatorially inconsistent inputs,
but such tests are not a decision procedure for Phi_sigma. The supplied
interpreter deliberately exposes this distinction. For three vertices,
W_((0,1),(0,2)) equals orient(p0,p1,p2). Flipping just the orientation sign
in a genuine signature leaves the interpreted sweep unchanged, yet makes
Phi_sigma impossible by that identity. A control records that the interpreter
does not detect this fabricated input. Its acceptance is therefore never
reported as a realizability certificate or a new placement.

This finite reduction separates the placement quantifier from obstacle
geometry; it does not decide Q2's quantification over ALL planar graph orders.
No claim of novelty is made for finite semialgebraic recognition reductions.

## 5. Safe implementation and actual controls

signature.py extracts all the degree<=5 signs from exact rational input.
sweep.py interprets signs, constructs cells and faces, labels components,
and finds the smallest cover by a finite memoized remaining-target recursion.
Each recursive call covers at least its first uncovered target, so its
remaining bit set decreases. A 100,000-state cap is a resource refusal,
not an obstacle-number conclusion. The domain is 3<=n<=6, exact rationals
with at most 256 numerator/denominator bits, and at most 15 nonedges.

No source imports the C20 or C21 arrangement core. The sweep uses ONLY sign
arrays, unlike the C21 strict-elimination consumer. This is a different code
method, not a separately admitted verifier trust domain. The general code's
source-to-semantics proof still needs review.

controls.py computes both the sweep outputs and direct segment/triangle
checks not using the sweep's face classification. It tests the exact examples
below, eight three-point graphs, six symmetry cases, two 10^-40 perturbations,
five rejected out-of-domain/invalid inputs, a rejected zero denominator, and
the explicitly unresolved realizability mutation. coarse_search.py searches
a specified 4,096-graph slice on the frozen six points and stops at its first
cover discrepancy; it examines 1,407 graphs, not all 32,768 six-vertex graphs.
It orders by the number of extra edges, so the discovered seven-edge graph
is edge-minimal within that particular mandatory-edge slice. No global
vertex/edge minimality theorem is claimed.

The four small ordinary-text sources use standard-library rational arithmetic,
combinatorics, sorting, memoization and JSON output only. They contain no
network, filesystem reads/writes, subprocess calls, credentials or dynamic
code evaluation. Commands are `python controls.py` and `python coarse_search.py`
from this directory. Complete compact outputs and actual environment/time/
resource/source fingerprints are in observation.json, coarse_observation.json
and execution.json. A first axis-only escape menu failed on the narrow positive
wedge; it was repaired with an explicit rational diagonal, then the finite
controls were rerun successfully. This is recorded as a diagnostic limitation,
not hidden as a theorem failure or a successful first run.

## 6. Exact counterexample to vertex-order-only compression

Let H have vertices 0,...,5 and COMPLETE edge set

    01, 23, 04, 12, 14, 15, 25.

It is a planar cactus: triangles 0-1-4 and 1-2-5 share vertex 1, with a pendant
edge 2-3. For a direct plane drawing, use 1=(0,0),0=(-2,0),4=(-1,1),
2=(2,0),5=(1,1),3=(3,-1); the two triangles lie in opposite halfplanes and
the pendant segment lies outside them. This is a planarity witness, not the
obstacle layouts analyzed next.

Consider instead the family

    p0=(1,1), p1=(-2,-2), p2=(3,6), p3=(-5,-10),
    p4=(7,-7), p5=(-11,11+delta).

The complete list of twenty triple determinants at delta=-1/100,0,+1/100
is in observation.json. Every triple has the same nonzero sign at all three
values. All pair x differences and all pair-line slope differences are also
nonzero at the compared values. These are exact rational checks, not rounded
coordinates or an image-based assertion.

At delta=0 the three lines 01,23,45 concur at (0,0). For the graph containing
ONLY those three matching edges, moving delta to +1/100 changes free-component
count 1 to 2, but its minimum cover stays 1. That control alone would not show
tau is noninvariant. The cactus H does: its free-component count stays FIVE,
but its minimum cover is TWO for delta=-1/100 and zero, and ONE for +1/100.
At both nonzero values the full pair-line arrangement has 85 cells (84 at
zero). The change cannot be dismissed as graph-vertex collinearity.

Here is a proof of the 2-versus-1 conclusion that does not rely on interpreting
those component counts.

### 6.1 Negative layout: no common component, but two suffice

First take delta=0. Put O=(0,0), R=(-6/13,6/13), and let A,B,Z be the filled
triangles with counterclockwise vertices

    A=(p0,p1,p4), B=(p1,p2,p5), Z=(O,p2,p1).

Every triangle boundary lies in K: Z uses subsegments of edges 01 and 23
and the edge 12. The open nonedge 45 is partitioned at parameters 7/18 and
97/234. Its three open pieces lie strictly in int(A), int(Z), int(B),
respectively. The cut points O,R lie in K. This can be checked by the three
triangle-side inequalities at each piece's two endpoints: both values are
nonnegative and at least one is positive for each side, so every strict
convex combination is interior. controls.py checks precisely these inequalities.
Every free point of 45 is therefore separated from infinity by a Jordan
triangle whose boundary is in K.

In contrast, the ENTIRE relative nonedge 02 is in the exterior component.
For x in (1,3) its height is y=(5/2)x-3/2. Its right horizontal ray stays above
A, whose top for x>=1 is at most 1, and below edge 23, since y<2x and that
edge's line increases to the right. It stays below B: B is on the upper side
of y=(8/5)x+6/5 and

    (5/2)x-3/2 < (8/5)x+6/5  for 1<x<3.

For all subsequent x the separating line is only higher, or the triangle's
x range has ended. All graph edges belong to A, B or the segment 23. Thus
this horizontal ray meets no K and reaches infinity. No one connected
obstacle can hit both nonedges 02 and 45.

Seven explicit nonedge witnesses with paths to the exterior of [-12,12]^2
are listed in observation.json; they cover every nonedge except 45. All
escape segments avoid every closed graph edge and every graph point by
separate exact parameter-intersection checks. Their endpoints lie outside
the box containing all of K, so they belong to the same exterior component.
A further free witness (1,-1) lies on 45. One compact connected obstacle in
the exterior and one in its bounded component suffice by C20's path-union
construction. Hence tau(H,p_zero)=2, not merely tau>=2.

For delta=-1/100 the same argument works with

    S=(s,s), s=7*delta/(36+delta),
    R=(r,(8/5)r+6/5), r=(35*delta-108)/(234+5*delta).

Now the three pieces 4-S, S-R, R-5 lie in A,Z,B, with Z still using O=(0,0).
The exact cut parameters are 1400/3599 and 1940/4679. The endpoint inequalities
are separately checked. Boundary 23 may cut a piece INSIDE A into two bounded
components, which does not open a path to infinity. The same exterior proof
for 02 holds, and the seven escape witnesses plus the additional 45 witness
(1,-301/300) again give two obstacles. Thus tau(H,p_minus)=2.

### 6.2 Positive layout: all eight targets meet the exterior

For delta=+1/100, the former seven targets still have explicit exterior
witnesses and checked escape segments. The last target 45 now contains

    w=(1/600,2399/1080000), parameter t=4199/10800.

It lies in the narrow wedge y>x and y<2x, below B. The ray from the origin
through w has slope c=2399/1800, with 1<c<8/5. Starting at w and going right
it stays above A, below edge 23 and below B's supporting line
(8/5)x+6/5; the segment to (50,2399/36) is checked exactly against every
edge and vertex. Beyond that point all graph coordinates are already behind
its x value. Thus w reaches infinity without meeting K. All eight nonedges
have witnesses in the same exterior component, so tau(H,p_plus)=1.
The graph is not complete, so zero obstacles are impossible.

Consequently the two fixed placements p_minus and p_plus have the SAME
vertex order type but DIFFERENT one-connected-obstacle existence answers.
The abstract planar cactus itself has a one-obstacle placement, so this is
NOT an unrestricted obstacle-number lower bound. It disproves only the
coarse premise that one representative per vertex order type is enough.
C22 used vertex signs for necessary clauses, not for such a completeness
claim, and is not withdrawn by this counterexample.

## 7. Dependencies, pressure tests, and the next unresolved step

T: C19 tube/Jordan remains a separate polygon/count proof. It is not used to
claim sign realizability or to derive the direct Jordan-triangle exclusion.
A: C20 exact free components and C21 second-core replay are unchanged.
P1: C22's all-placement X4 obstruction and trace remain candidate-only.
P2: the present finite realizable atlas replaces a FALSE vertex-order-only
compression; it still leaves exists h forall planar G exists sigma unresolved.
These labels are candidate-local subdivisions, not invented canonical records.

The source-to-formula and realizability gaps are explicit. A complete finite
signature cannot be replaced by a list of unverified Boolean orientations.
A zero H comparison is not a denominator failure; a zero W is outside D*.
D* is used only after robustification for existence, not to reject arbitrary
fixed C20 inputs. Tiny positive and negative 10^-40 perturbations keep the
same twenty vertex signs while the exact cover remains respectively 1 and 2.
No finite control proves the all-n atlas or the uniform planar assertion.

A possible smaller next interface is quartic local event ordering. For three
lines a,b,c, let T_abc=det(L_a,L_b,L_c). Direct expansion gives

    X_ab W_ac-X_ac W_ab = -B_a*T_abc.

Thus local intersection order ALONG one nonvertical line depends only on
B,W and degree-four T signs. This identity is an algebraic next-step note,
not a completed quartic atlas: reconstruction of the unbounded face, cyclic
orders and endpoint incidences from only local orders still needs its own
proof and implementation. The delivered interpreter uses the fully described
degree-five global event comparisons.

Prior-art context: the distinction between a point order type and the
arrangement of all its connecting lines is also discussed by Felsner, Pilz
and Schnider, *Arrangements of Approaching Pseudo-Lines*, DCG 67 (2022),
section 6 near Fig. 8, DOI 10.1007/s00454-021-00361-w. That source is a
terminology/context check, not a proof of the explicit cactus example or
of the supplied decoder. No novelty claim or source-full-text copy is made.

All code and finite observations remain in the candidate-generation domain.
Fresh verifier registry has fixture-policy identities but no compatible
callable geometry/placement-sign consumer or closure receipt. Request
statement-faithfulness review, exact source-to-sign replay and the admitted
closure chain; no web-signed EvidenceLink/Result/Solution is produced.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: reduce the atlas to quartic local order predicates with a verified
rotation/face interface, or use the finer signature to search a genuine
all-placement obstruction family. Preserve the realizability obligation and
never promote the six-point bad drawing to an unrestricted lower bound.
