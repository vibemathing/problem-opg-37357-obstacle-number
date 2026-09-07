# C19: C17 fixed-placement audit, with four explicit lemmas

Candidate: candidate:opg37357-a01-c19-fixed-placement-proof-v1
Verdict: candidate_only
Mathematical stage: reviewable proof draft
Primary method owner: math-proof
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: 05e200eb918ff174a3f35c66769cbaf19a22750e
Audited C17 Git blob: 57a79e70d5e25f47b3bab7ca65f90c83d08ea38c
Audited C17 SHA-256 (existing packet binding): 15b6e9e0547e7889d683cd8139f3a0faecc3886e749fa25f8796efb63f28d2ab

## 0. Frozen statement, negation, and audit outcome

Let G be a finite simple labeled graph with n vertices and e edges. Fix an
injective map p:V(G)->R^2, with arbitrary REAL coordinates. Write S=p(V(G)),
K=S union the CLOSED straight segments representing graph edges, and
k=C(n,2)-e. Crossings, collinear graph points, overlapping edge segments,
coincident supporting lines, and disconnected G are allowed. The drawing
will not be translated, normalized, perturbed, or otherwise changed.

Assume there is a connected set O contained in R^2 minus K which meets
every closed nonedge segment [p_i,p_j]. For k>0, O is necessarily nonempty.
We do not assume O is open, has interior, is path connected, is bounded,
or is polygonal. Its only uses are connectedness, avoidance, and hitting.

The exact target is the existence of a bounded filled simple polygon P
such that P is disjoint from K, P meets every nonedge segment, and

    corners(P) <= B17(n,e) = max(3, 2e^2-e+3*C(n,2)).

A filled simple polygon means the simple polygonal Jordan boundary together
with its bounded complementary region. Straight subdivision points are not
counted as corners. The construction below actually places a point of each
nonedge in int(P). P need not contain O.

The exact negation would be a G, fixed p and O satisfying these assumptions
for which no such P with at most B17 corners exists. None of the diagnostic
counterexamples to stronger intermediate assertions below has this scope.

Outcome: the target has the four-lemma proof below. It is a reviewable
candidate proof, not a verifier receipt, kernel run, or admitted Result.
The argument repairs an imprecise eligible-cell phrase and makes the port
and Jordan-disk steps explicit; it does not change B17 or move graph points.
Both the unrestricted completeness claim and the root remain OPEN.

Dependencies: L1 -> L2; (L1,L2) -> L3; L4 is a separate tree lemma;
(L1,L2,L3,L4 and the final count) -> the target. Standard background is
finite graph theory, Euclidean compactness/continuity, and the Jordan
Polygon Theorem. No C04, C07, or C16 perturbation theorem is used.

## 1. L1: one free component and selectable segment-interior witnesses

Claim. If k>0, one open component U of F=R^2 minus K meets the relative
interior of every nonedge in a nonempty relatively open interval. One can
choose mutually distinct witnesses, avoiding any prescribed finite set.

K is a finite union of compact segments and points, hence is closed and
compact. F is open. Every component U of F is open: a sufficiently small
open ball about any x in U lies in F; being connected and meeting U, that
whole ball belongs to U. Such a component is polygonally path connected.
Indeed, the set of points reachable from a fixed point by finite polygonal
paths in U is relatively open, and so is its complement, using balls in U.
Connectedness makes the reachable set equal to U.

The connected set O lies in one component U of F, regardless of whether O
itself is path connected. For each nonedge ij pick a hit z in O intersect
[p_i,p_j]. Neither endpoint belongs to O, since endpoints are in K. Thus

    z=(1-t0)*p_i+t0*p_j, with 0<t0<1.

Choose rho>0 with B(z,rho) contained in U. If
|t-t0| < rho/||p_j-p_i|| and t remains in (0,1), the corresponding point
of the nonedge lies in that ball. Injectivity ensures the denominator is
positive. This proves the interval assertion. A nonempty interval minus
finitely many points is nonempty; choosing witnesses successively avoids
a prescribed finite set and all previously chosen witnesses.

Boundary clarification. The initial hit may be only a tangency to the
boundary of O, and int(O) may be empty. The witness is interior to the
NONEDGE and belongs to the OPEN FREE SPACE. It need not be interior to O,
or even remain in O after the finite exclusions. It will become interior
to the new polygon in L4. Hits at graph endpoints or on graph-edge
segments are impossible under O intersect K empty.

## 2. L2: eligible-cell graph, without a general-position assumption

Let L_1,...,L_ell be the DISTINCT supporting lines of graph-edge segments.
Then ell<=e, with ell=0 permitted. Their finite arrangement has at most

    f <= 1+ell*(ell+1)/2

open two-dimensional cells. Inserting the j-th distinct line produces at
most j pieces, because its previous intersection points number at most
j-1. Each piece splits at most one previous cell. This gives the stated
induction, starting from one cell at ell=0. Parallel lines and concurrent
intersections only decrease this count; coincident lines are counted once.

Let A0 be the finite set of intersections of distinct nonparallel lines.
Each open cell C is convex, and no graph edge enters C. The set C minus S
is polygonally path connected: for x,y in it, choose h in C outside S and
the finitely many lines through x and a forbidden point, or y and a
forbidden point. Then [x,h] union [h,y] lies in C minus S. The finite
exclusion cannot cover an open cell.

Call C eligible if (C minus S) intersects U. Consequently

    C minus S is contained in U.

It is NOT necessary that C itself be contained in U: isolated graph
points can puncture it. This is the precise reading used in this audit.

Use one vertex per eligible cell. Two cells are adjacent if they share
an open one-dimensional arrangement face with a point in U minus S.
That face already excludes A0. Only a local free interval is required;
an entire supporting line need not be free.

This finite graph is connected. Choose x,y in two eligible open cells and
a polygonal path gamma in U between them. Its image is compact and has a
positive distance from the closed complement of U (use any small radius
if that complement is empty). Slightly perturb its internal vertices,
leaving x,y fixed, with displacements smaller than this distance. Every
point on a perturbed segment, at the same interpolation parameter, stays
within the maximum endpoint displacement of the old segment. The path
therefore stays in U.

Here the perturbation concerns an AUXILIARY PATH, not the fixed drawing.
It can be chosen with no vertex on an arrangement line and no segment
through any point of A0. To justify existence explicitly, first subdivide
if needed so no segment has two fixed endpoints. Choose each internal
vertex in its small open ball avoiding all arrangement lines, preceding
vertices and both fixed endpoints, and lines through its predecessor and points of A0. For the
last internal vertex also exclude lines through y and points of A0.
These are finitely many points and lines. The choices make every segment
avoid A0. A segment parallel to an arrangement line misses that line;
every actual crossing of a line is transverse and away from A0.

There are finitely many crossings. Each crossing lies in U, so a small
interval of the crossed arrangement face is free. The consecutive open
cells traversed by the path are eligible and adjacent in the defined
graph. They give a walk between the two selected cells.

By L1 choose the k witnesses distinct and outside A0 union S. A witness
not on any supporting line belongs to one eligible open cell. A witness
on a line lies in an open arrangement face. A ball around it in U meets
BOTH incident open cells, so both are eligible; assign the witness to
just one of them. Thus witnesses on arrangement edges require no
perturbation of the drawing and are not discarded.

## 3. L3: pruning, embedded spokes, and the exact leaf count

For now assume k>=2. Mark every cell assigned at least one witness.
Choose a spanning tree of the connected eligible-cell graph. Repeatedly
delete an UNMARKED leaf and its incident edge. Marked cells and their
connectivity are invariant. The number of tree vertices strictly decreases
at each deletion, so the procedure terminates. It leaves a tree on t<=f
cells containing all marked cells; if t>=2 every leaf cell is marked.
If all marks are on one cell, the remaining tree may have t=1.

For each of the t-1 retained cell-tree edges choose one portal on an
available free open interval of its shared arrangement face. Choose
portals AFTER all witnesses, avoiding every witness and earlier portal.
There are finitely many exclusions and each interval is open. Portals
are in U, not in S or A0, and are globally distinct.

For each retained cell C let D_C consist of its assigned witnesses and
incident portals. Choose x_C in C outside:
- S and all endpoint points;
- every line through two distinct members of D_C;
- every line through a member of D_C and a member of S.

These are finite exclusions from an open set, so such a center exists.
Connect x_C by straight spokes to all members of D_C.

All these spokes lie in U. For an endpoint y in C this follows from
convexity and avoidance of S. For y on the boundary of C, the half-open
segment [x_C,y) lies in C: each defining open-halfplane inequality remains
strict before its last point. Its last point is already in U. Lines
through endpoints and graph points were excluded, so no spoke hits S.
No graph-edge segment lies in C.

There are no extra spoke intersections or contacts. Within one cell,
two different spokes share only their center: another common point
would put the center and both endpoints on one line. The same exclusion
prevents passing through a third assigned endpoint. A spoke in one
cell, except for its designated boundary endpoint, is in that cell's
INTERIOR. Therefore spokes from different cells cannot meet in their
interiors or touch another cell boundary at an unintended place.
Globally distinct witnesses/portals leave only the intended common
portals. Centers in different open cells are distinct.

The resulting geometric union is therefore an embedded straight-line
tree, not just an abstract tree with a potentially intersecting drawing.
Its abstract graph is the cell tree with each edge subdivided by its
portal, and one additional pendant witness per nonedge. Consequently

    N_T = t+(t-1)+k = 2t-1+k,
    E_T = 2(t-1)+k = 2t-2+k.

Its leaves are exactly the witnesses. Portals have degree two. If t>=2,
a nonleaf cell center has at least two portals; a leaf cell center has
one portal and at least one witness because pruning made it marked.
If t=1, its only center has degree k>=2. Thus no center is a leaf and

    L_T=k.

This last equality is deliberately NOT claimed for k=1. A center joined
to a single witness has TWO leaves. The final theorem treats k=0 and
k=1 directly rather than inserting a false leaf count.

## 4. L4: a thin polygonal disk with at most 2E_T+L_T corners

Tree lemma. For a finite embedded straight-line tree T with N_T>=2,
and ANY open neighborhood W containing its entire geometric realization,
there is a filled simple polygon P with

    T contained in int(P), P contained in W,
    corners(P) <= 2E_T+L_T.

An embedded tree here has distinct vertices, positive-length straight
edges, and intersections only at shared endpoints. Thus two outgoing
rays at one vertex can never coincide in direction: that would make
two edge segments overlap. Opposite rays ARE allowed.

### 4.1 Choose radii before choosing a common width

For each vertex v choose r_v>0 such that the closed balls Bbar(v,2r_v)
are pairwise disjoint, lie in W, and avoid every nonincident tree edge.
Also require r_u+r_v<length(uv) for every edge. All the restrictions
are strict and finitely many, so compactness and embeddedness give choices.

At a nonleaf vertex order the outgoing unit vectors d_i cyclically.
Let n_i be d_i rotated counterclockwise by pi/2, and let theta_i in
(0,2pi) be the counterclockwise gap to d_(i+1). Their sum is 2pi.
We will use ONE common half-width delta>0 throughout the tree, small
enough for every vertex and every connector.

At a vertex with r=r_v define the right and left port endpoints

    R_i=v+r*d_i-delta*n_i,
    L_i=v+r*d_i+delta*n_i.

For the sector with beta_i=theta_i/2 in (0,pi), let b_i be its unit
bisector, and set

    w_i=v+(delta/sin(beta_i))*b_i.

This is defined also for reflex sectors theta_i>pi. In coordinates
v=0,d_i=(1,0), it is exactly (delta*cot(beta_i),delta). The line from
L_i to w_i is the left offset line of ray i; the line from w_i to
R_(i+1) is the right offset line of ray i+1. For theta_i=pi those
lines coincide: use their single straight segment, not an extra turn.

Choose delta small enough that:
(a) delta<r_v/2 for all vertices;
(b) alpha_v=arctan(delta/r_v)<theta_i/2 for every sector;
(c) ||w_i-v||=delta/sin(theta_i/2)<r_v/2 for every sector;
(d) for all distinct incident directions i,j,
    d_i dot (r_v*d_j +/- delta*n_j) < r_v.

Condition (d) follows at delta=0 from d_i dot d_j<1; it persists for
small positive delta. Conditions (a)--(c) also have positive choices
because all angles are fixed and there are finitely many of them.
There is NO uniform lower bound on delta over changing drawings.

### 4.2 The local joint really is a disk, including reflex sectors

At a nonleaf vertex form the cyclic chain of port caps R_i--L_i and
sector chains L_i--w_i--R_(i+1), omitting w_i at a straight sector.

Here is an explicit nonintersection argument. In the coordinates above,
the polar angles of L_i, w_i, and R_(i+1), on that sector's unwrapped
interval, are alpha_v, beta_i, and theta_i-alpha_v. They are strictly
increasing. The angular increment on EACH joining segment is
beta_i-alpha_v, which is between 0 and pi even when theta_i>pi.
The cap's increment is 2alpha_v<pi. A straight segment between two
nonzero vectors with positive angular difference less than pi
intersects every intermediate ray once and meets no other ray in
that angular interval: it is one side of the nondegenerate triangle
with their common origin. Equivalently, its positive determinant
makes its polar angle strictly monotone.

For the first sector segment the determinant is explicitly

    det((r,delta),(delta*cot(beta_i),delta))
      = delta*(r-delta*cot(beta_i)) > 0,

since |delta*cot(beta_i)|<r/2 by (c). Reflection across the sector
bisector gives the same positive determinant for the second segment.
At theta_i=pi their union is a straight side with no radial degeneracy.

The caps and sectors partition one complete turn without overlaps.
The whole chain is therefore the radial graph of a positive continuous
piecewise-defined radius rho(phi). It is a simple closed polygon.
The filled radial set
{v+s*rho(phi)*(cos(phi),sin(phi)):0<=s<=1}
is a disk J_v: the displayed radial map from the closed unit disk
is a continuous bijection with continuous inverse. In particular v
lies strictly inside J_v. All boundary vertices lie within distance
2r_v; each radial triangle does too.

For every incident i, the whole J_v satisfies

    d_i dot (x-v) <= r_v,

with equality EXACTLY on its own port cap. This holds at the two
port endpoints; it is strict at all other ports by (d), at each w
by (c), and at v. It then holds on all radial triangles. The two
sides adjoining a port continue inward on the parallel offset
lines d_i dot (x-v)<r_v. Thus the port has an inward rectangular
collar of positive length and width 2delta.

At a leaf, whose only outgoing direction is d, instead take the rectangle

    v+s*d+t*n,  -delta<=s<=r_v, -delta<=t<=delta.

It lies in the chosen ball for small delta, contains v strictly
inside, has the required front port cap and collar, and contributes
only TWO rear turns once that front cap is glued away.

### 4.3 Connectors have only the intended intersections

For an edge uv oriented by d=(v-u)/||v-u||, with n its perpendicular,
use the rectangle

    u+s*d+t*n,
    r_u<=s<=||v-u||-r_v, -delta<=t<=delta.

Its center segment has positive length. Its end caps are exactly
the port caps at u and v; the left/right ordering reverses at v,
but the cap SET is identical.

The finitely many truncated center segments are disjoint compact
sets. They have positive pairwise separation. They also have
positive separation from nonincident closed vertex balls, which
were chosen disjoint from the full nonincident edges. Finally they
are compact subsets of W. Reduce the same delta further to make
the connector rectangles mutually disjoint, disjoint from every
nonincident J_v, and contained in W. Earlier strict angle conditions
remain valid under this reduction.

For an INCIDENT endpoint polygon the supporting-plane inequality
in 4.2 gives more than a small-clearance argument: the connector
is on the opposite side of that plane and intersects J_v exactly
in the designated cap. The other cap intervals on that joint are
disjoint, including their endpoints, by the disjoint polar windows.
This rules out pinches and unintended corner-only contacts.

### 4.4 Disk gluing and equality with the filled Jordan region

Root the abstract tree and grow a connected rooted subtree. Start
with J_root, already a disk. To add a child, first glue its connector
along its single exposed parent cap, and then glue its local disk
along the far connector cap. The intersection with everything
previously attached is EXACTLY the specified boundary interval.
At its interior both pieces have collars on opposite sides.

For completeness, the elementary disk-splicing fact used here is:
two closed disks joined along one nondegenerate proper boundary arc,
with no other intersection, form a closed disk. Identify the disks
with the upper and lower closed half-disks, sending the common arc
to their common diameter. Such boundary parametrizations extend
radially in the disk parameter domains supplied by the induction
hypothesis; the glued maps give a continuous bijection
from a disk to the union, hence a homeomorphism by compactness and
the Hausdorff property. This also describes the boundary directly:
delete the common arc interiors and concatenate the two remaining
boundary arcs. They have disjoint interiors, so this is one simple
closed curve, not two curves or a self-touching curve.

In our straight-cap setting the relative interior of the cap is
interior to the planar union by the collars. Each remaining boundary
point away from the cap remains exposed; the cap endpoints lie on
the spliced polygonal boundary. Thus this boundary is exactly the
topological boundary of the union.

The Jordan Polygon Theorem says that a simple closed polygonal
curve has two complementary components, one bounded. The union
here is compact; membership is locally constant off its boundary,
so its unbounded complementary side is outside the union. The
bounded side contains a point of the original disk's interior and
therefore lies entirely in the union. The union is precisely the
curve PLUS its bounded region. In particular we are not filling
an unnoticed hole that might contain a forbidden graph point.

Induction applies for every finite rooted subtree: the induction
hypothesis is the disk and exposed-cap property just proved; one
child extends it by the two splicings above. The number of absent
tree vertices decreases by one until all N_T vertices are present.
No cycle edge is ever added. This supplies the global Jordan-disk
argument, not just local simplicity of isolated joints.

Every original tree vertex is interior to its joint. The initial
edge portions lie inside the joint except at their port centers;
the middle portions lie inside connectors. The port centers are
interior after gluing by the collars. Hence the ENTIRE tree, not
only its selected vertices, lies in int(P).

### 4.5 Count every surviving corner

Every internal port cap disappears. At each of its endpoints the
joint side and connector side lie on the SAME offset line.
The joint approaches the port from d_i dot (x-v)<r_v, whereas the
connector leaves toward larger projection. They form a straight
continuation, not a reversal. Port endpoints add ZERO final turns.

Each nonleaf joint has at most deg(v) sector turns; a theta=pi
sector has none. Each leaf has exactly two possible rear turns.
A connector has no corner beyond its four port endpoints, which
were just accounted for. Thus

    corners(P)
      <= sum_{deg(v)>=2}deg(v)+2L_T
       = (2E_T-L_T)+2L_T
       = 2E_T+L_T.

Removing redundant straight boundary vertices does not change P.
For N_T=1, E_T=L_T=0, so this numerical tree bound is NOT asserted.
Any sufficiently small triangle around the sole vertex replaces it.
This is an explicit exception, already required by the polygon
minimum of three corners.

## 5. Assemble the bound without moving the drawing

For k>=2, use the compact embedded tree of L3 in the open set U.
Apply L4 with W=U. The resulting filled P avoids K and contains
every selected nonedge witness in its interior. The graph points
and the edge segments have not changed at any step. Its corners obey

    corners(P)
       <= 2E_T+L_T
        = 2(2t-2+k)+k
        = 4t-4+3k
       <= 4*(1+ell*(ell+1)/2)-4+3k
        = 2ell*(ell+1)+3k
       <= 2e*(e+1)+3*(C(n,2)-e)
        = 2e^2-e+3*C(n,2).

For k=1, L1 supplies a witness z with a small ball in U. Put a
nondegenerate triangle inside that ball with z strictly interior;
for example use z+eta*(1,0), z+eta*(-1,1), z+eta*(-1,-1)
with eta sufficiently small. Its three corners satisfy B17.
For k=0 choose a triangle outside a disk containing the compact K.
This also treats n=0 and n=1 and does not require a nonempty O.
These cases prove precisely the displayed maximum with 3.

The role of e is only ell<=e. No inequality for planar graph size
is needed, no embedding of G is changed, and no generic position
of the graph coordinates is assumed.

## 6. Exact-coordinate adversarial audit

All checks here are direct coordinate/definition arguments, not
executed geometry tests or an exhaustive search. They attack
stronger shortcuts; they do not give a counterexample to the
frozen theorem.

A1. Tangency and empty interior. With two isolated graph points
(-1,0),(1,0), the filled triangle with corners (0,0),(-1/4,1/2),
(1/4,1/2) blocks the nonedge only at its bottom corner. The nonedge
does not enter int(O). Even the singleton O={(0,0)} satisfies the
connected-set hypothesis. Requiring a witness in int(O) is false;
requiring a witness in the open free component is valid.

A2. Witness forced onto an arrangement line. Put A=(-1,0), B=(0,0),
C=(1,0), with the sole edge AB. The rectangle
[1/4,3/4] times [-1/4,1/4] is a connected obstacle hitting both
nonedges AC and BC. Every such segment witness lies on y=0, the
only supporting line; no witness can lie in an OPEN 2-cell.
Distinct choices (1/3,0),(2/3,0) are handled by L2's incident-cell
assignment. The drawing is not perturbed.

A3. Coincident lines and unsafe portals. Use A=(-3,0), B=(-2,0),
C=(2,0), D=(3,0), with edges AB,CD. There is just one DISTINCT
supporting line. A small triangle about (0,0) blocks all four
nonedges without touching the drawing. The portal (0,0) is free;
(-5/2,0) is on a graph edge and is forbidden. Counting the entire
supporting line as a barrier or allowing arbitrary portals fails.

A4. Concurrent lines at a free point. Use the three disjoint edges
[(2,0),(3,0)], [(0,2),(0,3)], [(2,2),(3,3)] on their six endpoints.
The lines y=0,x=0,y=x concur at (0,0), but a unit ball there is
free. A path from (1/2,1/4) to (-1/2,-1/4) through the origin is
replaced by the polygonal chain through (1/4,1/2),(-1/2,1/4).
It avoids the origin and stays in the free unit ball. Thus
concurrence does not disconnect the eligible-cell graph.
None of these auxiliary path changes moves a graph vertex.

A5. Punctured cells. For the edgeless drawing with graph points
(-1,0),(0,0),(1,0), the only open cell is R^2, NOT a subset of U.
The open free component is R^2 minus these points. A proposed
spoke from (1/2,0) to (-1/2,0) hits the forbidden point (0,0).
This is why L2 uses C minus S and L3 excludes endpoint--graph-point
lines. It is also a literal counterexample to unqualified
'eligible C is contained in U'.

A6. Pruning and k=1. A star at (0,0) with leaves (2,0),(0,2),
(-2,0), only the first two marked, has three leaves, not two.
An unmarked leaf must be removed. A center joined to only one
witness has E_T=1 and L_T=2, not L_T=k=1. The one-nonedge theorem
case uses a triangle instead of that erroneous substitution.

A7. Opposite rays and N_T=1. The path (-2,0)--(0,0)--(2,0) has
E_T=2,L_T=2. The rectangle [-21/10,21/10] times [-1/10,1/10]
has only four turns, consistent with the upper bound six.
At its degree-two center both sectors are straight and contribute
no turn. For the sole vertex (0,0), the expression 2E_T+L_T is zero;
a literal version including N_T=1 is false, so L4 excludes it.

A8. One acute and one reflex sector with a fully rational polygon.
Take the two-edge tree from (0,0) to (4,0) and to (12/5,16/5).
The unit outgoing directions are (1,0) and (3/5,4/5). With delta=1/100
the two sector joints are (1/50,1/100) and (-1/50,-1/100).
After suppressing straight ports the six boundary vertices, in order,
are

    (401/100,-1/100), (401/100,1/100),
    (1/50,1/100), (1207/500,1601/500),
    (1199/500,1607/500), (-1/50,-1/100).

They are the offset lines and rear caps of L4, including its reflex
sector, with 2E_T+L_T=6. For example the differences along the two
nonhorizontal long sides have ratio dy/dx=4/3. Simplicity and tree
containment follow from the explicit radial-and-splicing proof,
not from an image of these coordinates. This is a local tree
diagnostic, not an obstacle-number sample for a new graph.

A9. No universal tube width. For rational 0<s<1 take outgoing
unit vectors (1,0) and ((1-s^2)/(1+s^2),2s/(1+s^2)).
The inner joint is (delta/s,delta). With port radius 1, s=1/100
and delta=1/10 it lies at (10,1/10), outside the intended local
ball and potentially beyond the tree edge. One must first fix s
and then choose delta, for instance small enough that delta/s<1/4.
The complementary reflex sector imposes the same small-scale issue.
At s=0 the outgoing directions coincide and the tree is not embedded.

A10. Common component is a hypothesis, not a pairwise inference.
The freshly read C18 seven-point diagnostic has the three incidence
sets {T,Btm}, {T,O}, {Btm,O}. Their total intersection is empty.
It cannot satisfy L1's common-component conclusion or the original
connected-obstacle hypothesis for the selected triple. Hence it
does not contradict this conditional upper bound. No existing
C18 numeric table or CNF was newly evaluated or promoted here.

## 7. Source-faithfulness and reasoning-discipline record

C17 is the audited target, not evidence for itself. C03 supplies the
earlier cell/tree idea; L1--L3 above reconstruct it with the puncture,
endpoint and portal exclusions spelled out. C04 (exact-m padding
and affine normalization), C07 (sparse-to-GP existence), and C16
(quantitative rational GP extraction) were freshly read but are
NOT logical premises of this fixed-placement proof. None may be
used here to move a fixed collinear graph drawing. C18 is used
only for the failed pairwise-component shortcut.

The sole named external topological theorem used for identifying
the filled region is the Jordan Polygon Theorem, in Jeff Erickson,
*Simple Polygons*, Computational Topology notes, 2023 edition,
section 'Proof of the Jordan Polygon Theorem', retrieved 2026-09-07:
https://jeffe.cs.illinois.edu/teaching/comptop/2023/notes/01-simple-polygons.html
It applies because each spliced boundary was first proved to be
a finite simple closed polygonal curve. It supplies separation
into bounded and unbounded components, not the 2E_T+L_T count.
Disk gluing and the radial homeomorphism are proved explicitly
above; no geometry-library offset theorem is assumed.

Definitions/quantifiers/negation: frozen in section 0.
Witness construction: L1--L4, with finite choices in open intervals
and open cells; this is an existence construction over real input,
not a claimed executable algorithm for arbitrary real obstacles.
Pressure tests: A1--A10, including false strengthened assertions.
Invariants: fixed K, witness retention during pruning, nonintersecting
spokes, and the disk/exposed-cap property during tree attachment.
Monovariants: cell count decreases during pruning; unattached vertex
count decreases during rooted disk assembly. Both are nonnegative
integers. The final states imply L_T=k and a single filled disk,
respectively, rather than merely stopping.
Extremal check: arrangement count is worst-case over all distinct
lines; parallelism and concurrence cannot increase it.
Symmetry: all local formulas use cyclic directions and dot products;
reflection reverses cyclic order but leaves counts and intersections
unchanged. No quotient discards a symmetric fixed configuration.
Scale: widths depend on the finite drawing's positive gaps and
angles. This proves existence at each scale, not uniform precision.
Probability: not applicable; no random or average-case argument.
Induction: L2's line insertion and L4's rooted attachment each have
a stated base, valid step, and finite covered domain.
Verification: no geometry script, solver, grid program, or proof
assistant ran. Only document/byte bookkeeping and GitHub transport
may run for this candidate. Finite diagnostics are not the proof.

This review remains in the candidate-generation trust domain. It
creates no verifier receipt, EvidenceLink, Result, or root closure.
The complete special-case argument is available for external review;
trusted topology/geometry replay and the separate full-contract
faithfulness decision remain outside this deliverable.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
unrestricted_one_obstacle_completeness: open
next_action: external review of this frozen four-lemma proof, especially
the radial-joint and boundary-splicing assertions; do not infer an
obstacle-number lower bound or launch another root task from transport.
