# C20: finite arrangement characterization for one fixed drawing

Candidate: candidate:opg37357-a01-c20-finite-arrangement-theorem-v1
Verdict: candidate_only
Mathematical deliverable: finite-arrangement-characterization proof draft
Overall status: NONTERMINAL_CHECKPOINT (executable source publication blocked)
Owner: math-proof; exact-rational implementation is a candidate computation
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: 524c1e402d85e513de58a20f9b7a73bbde0a4e10

## 1. Exact domain, quantifiers and the two stages

Fix a finite simple labeled graph G with n vertices, e edges, and an
INJECTIVE placement p:V(G)->R^2. Keep every coordinate fixed. Let S be the
finite set of graph points and K the union of S and all CLOSED graph-edge
segments. Crossings, overlapping edge segments, coincident supporting
lines, parallel lines, concurrent lines, collinear graph vertices, and a
graph vertex inside a nonincident edge are permitted. A drawing whose
nonedge is entirely in K simply fails the condition below; it is not
silently rejected as a genericity violation. No planarity of this drawing
or of the abstract graph is needed for the characterization.

Let N be the COMPLETE list of nonedges, k=|N|=C(n,2)-e, and I_s the
relative interior of the segment of s. The following are equivalent:

(A) A NONEMPTY connected set O subset R^2 minus K meets every nonedge.
(B) One connected component U of R^2 minus K meets every I_s.
(C) In the complete finite certificate below there is a component label
    common to all recorded nonedge-component incidence sets.

These are existence assertions, not assertions that a supplied arbitrary
connected obstacle has interior, is compact, or can itself be retained.
They remain equivalent when (A) separately requires the chosen obstacle to
be bounded and path connected, or compact and path connected. A bounded
open path-connected obstacle can also be chosen. One must not demand a
nonempty bounded obstacle that is simultaneously open AND closed in R^2.

Stage 1 proves (A)<->(B)<->(C) without C19's tube/Jordan lemma. The finite
characterization is valid for real coordinates when the comparisons are
understood mathematically. An algorithm on arbitrary unencoded real
numbers is NOT claimed. The implementation is for all rational injective
placements, within explicit resource limits; it does not need the proposed
fallback assumption forbidding vertices inside nonincident edges.

Stage 2 extracts an embedded witness tree of the C19 type and, conditional
on the separately frozen C19 tree/tube/Jordan proof, obtains a bounded
filled simple polygon with at most

    B17(n,e)=max(3,2e^2-e+3*C(n,2))

corners. A component label alone gives no corner count; the size-controlled
spoke/portal tree and the tube lemma supply that further implication.
No code here produces or checks a tube polygon for arbitrary inputs.

The negation of the characterization would require the SAME fixed p to
satisfy one side but not the other. A negative certificate for one drawing
is not a counterexample to existence at another placement of G, nor an
unrestricted obstacle-number lower bound.

## 2. Stage 1a: obstacle and common free component

K is compact, so F=R^2 minus K is nonempty and open. Every connected
component of F is open: a small connected ball in F around any point of a
component belongs to that component. In a component U, the points reachable
from a fixed point by finite polygonal paths form a relatively open set;
its relative complement is open for the same small-ball reason. Therefore
U is polygonally path connected. Non-path-connected examples of arbitrary
planar sets cannot be substituted for this OPEN subset of the plane.

For (A)->(B), the connected nonempty O is contained in one component U.
A hit z of a nonedge cannot be a graph endpoint or any other point of K.
Thus z=(1-t)p_i+t p_j for 0<t<1. A small ball about z lies in U, hence a
nonempty parameter interval about t also lies in U. The hit may originally
have been a tangency to O or O may have empty interior: the openness used
is that of F and U, not of O. Finitely many undesired parameter values can
be excluded when choosing witnesses.

For (B)->(A), select one witness for each nonedge and join them to one
base point by finitely many polygonal paths in U. Their union is nonempty,
bounded, compact and path connected, contained in U, and hits all targets.
This gives the compact version without any Jordan argument or corner bound.
For an open version, thicken this compact path union by a sufficiently
small positive distance; compact separation from the closed complement of
U keeps it in U, and the union of balls centered on a connected path set is
open, bounded and path connected. Neither construction need contain O.

If k=0, (B) is vacuous once any component is chosen. Such a component always
exists because K is compact and cannot equal the plane. A point outside a
large box containing K supplies a nonempty compact obstacle. A small remote
ball or triangle supplies the other versions. Thus the convention for the
intersection of an empty family in (C) is ALL component labels, not empty.
The case n=0 is included. This removes an otherwise common vacuity bug.

## 3. Stage 1b: the finite certificate

### 3.1 Lines and refined lower-dimensional faces

Take all DISTINCT infinite supporting lines of graph edges; number them
0,...,ell-1, ell<=e. For rational coordinates write each as a x+b y+c=0
with primitive integer coefficients, gcd one and the first nonzero
coefficient positive. This deduplicates coincident lines, including edges
with reverse endpoint order. Parallel lines remain different lines.

For each line l choose the rational parameterization r+t d, where
r=(-c/a,0) if a is nonzero, otherwise r=(0,-c/b), and d=(-b,a).
Its cut parameters are ALL its intersections with other nonparallel lines
AND ALL graph points that lie on that line. Deduplicate and sort them.
The refined open 1-faces are all consecutive open intervals and the two
unbounded rays, including the whole line only if there is no cut. Record
line index, both bounds (null means infinity), and a rational interior
sample. Artificial cuts at graph points are essential: graph-edge endpoints
need not be intersections of two supporting lines.

Record every point in S union A0 as a zero-face, where A0 is the set of
line intersections. Points of S off all lines are isolated punctures of
2-cells. A zero-face is forbidden precisely when it lies in K. It must NOT
be treated as a free portal merely because it is a graph-edge endpoint.

Each refined open 1-face is either wholly forbidden or wholly free.
Indeed, a graph segment on that line can change membership only at its
endpoints, which are cuts. A segment on a different line can hit it only
at an arrangement intersection, also a cut. Graph points on the line are
cuts. Therefore testing the sample against all CLOSED edge segments and
S decides the entire open face. An entire supporting line is not a barrier.

### 3.2 Full-dimensional cells and complete enumeration

A 2-cell is represented by the strict sign vector of all line equations.
Every feasible sign vector determines one open convex intersection of
halfplanes, hence one cell; distinct vectors represent distinct cells.
The certificate gives the sign vector and a sample off S for every cell.
The cell means its punctured version C minus S when used as part of F.
It is nonempty and polygonally path connected: two of its points can be
joined through an intermediate point in C avoiding the finitely many lines
through either endpoint and a puncture.

The producer enumerates cells from the two sides of EVERY refined 1-face,
including forbidden faces and unbounded faces. At face sample q of line i,
use q +/- h(a_i,b_i). For every other line j, q is not on j and h can be
chosen so that

    |h*(a_j*a_i+b_j*b_i)| < |a_j*q_x+b_j*q_y+c_j|.

Thus only sign i changes; the two points lie in precisely the incident
cells. The implementation starts with a factor-two smaller bound and
chooses from n+1 positive rational values to avoid S. Each graph point
excludes at most one of those values, even considering both signs.

This enumeration is COMPLETE. If ell>0, any cell has a boundary point in
an open 1-face: from a point in the cell choose a segment to the opposite
side of one of the lines, avoiding all finitely many line-intersection
points and graph points at its first boundary crossing. Its first crossing
is on a single line, in the relative interior of a 1-face. Refining that
face by finitely many graph points does not remove all such points. Hence
the cell occurs on a sampled face side. If ell=0, the plane is the single
cell; a sample off the finite S is selected explicitly.

No enumeration of all 2^ell sign vectors, floating LP, bounding-box cutoff,
or assumed general-position cell formula is used. The usual upper bound
f<=1+ell*(ell+1)/2 follows by insertion of distinct lines; refinement of
1-faces by graph points does not add 2-cells.

### 3.3 Portal graph and its exact topological meaning

Build a graph Q with one vertex per punctured 2-cell. For each FREE refined
open 1-face, add an edge between its two incident cells and keep the face
sample as a portal. Parallel edges are harmless. Forbidden faces add no
edge. Compute connected-component labels of this finite graph, with
canonical labels ordered by the smallest cell index. For each zero-face,
record all incident cells: these are exactly the enumerated sign vectors
that agree with all NONZERO signs of the point. To see sufficiency, join
the point to the cell sample; all inequalities are strict before the
point, so the point belongs to that cell's closure.

Claim: components of Q are in bijection with components of F.

Soundness follows by connecting through a free portal: a small ball around
it avoids K, and the two punctured incident cells are path connected.
Thus every graph path in Q lies within one true free-space component.
Every free point is incident to at least one such cell, since an open ball
cannot be covered by finitely many lines or points.

For completeness, assign a Q-label to all free points. In a cell use its
label. On a free open 1-face the incident labels agree by its portal edge.
At a free zero-face, choose a small ball disjoint from K and from lines
not passing through that point. The sectors of the finitely many incident
lines are cyclically adjacent through free face pieces in that ball. The
corresponding incident cells therefore have one label. This also handles
a free point of concurrence; a forbidden zero-face is not used. A point
of S is always forbidden, including isolated punctures.

This label assignment is locally constant throughout F: a sufficiently
small ball meets only the listed incident cells and free lower faces.
Consequently it is constant on every connected component of F. Combined
with soundness and the fact that every free point reaches an incident
cell in a small ball, it gives the asserted bijection. Zero-faces need
not be added as graph vertices: when free, their local cell connectivity
is already present via free 1-faces; when forbidden, they cannot be crossed.

### 3.4 Nonedge incidence, including collinear and boundary cases

For each nonedge p_i p_j parameterized by 0<t<1, split [0,1] at 0,1,
every isolated intersection with a supporting line, and every graph point
on the nonedge. In particular, endpoints of collinear covering graph edges
are included. Record the cuts and EVERY open parameter interval between
consecutive cuts; choose its midpoint as sample.

On each interval membership in K is constant. Off supporting lines, no
graph edge can occur. If the nonedge is collinear with a supporting line,
coverage changes only at the graph endpoints already inserted; intersections
with other lines are cuts. A graph point is also a cut. A free interval
sample lies either in one 2-cell or in one free refined 1-face. It cannot
lie on two different supporting lines without being a cut, since a
positive-length nonedge cannot lie along two different lines. Record the
cell/face locator and its unique component label. Unioning these labels
gives the exact incidence set J_s of the relative nonedge interior.

Why may zero-length cut hits be ignored? A free cut point has a free ball,
so a nearby open parameter interval also belongs to its component. Thus
there is never a component visited ONLY at one free isolated parameter.
A cut point in K cannot serve as a witness. This argument would fail if K
were not closed; the present finite closed-segment domain is essential.

It now follows that (B)<->(C): a true free component meets every I_s iff
its corresponding Q-label lies in the intersection of all J_s. A negative
certificate supplies, for EVERY component label, an entire nonedge whose
incidence set omits that label. Pairwise intersection of the J_s is not
substituted for their total intersection.

## 4. Stage 2: a size-controlled rational tree and the polygon bound

When the intersection is nonempty choose one common label. For each nonedge
choose a fresh point in one of its free intervals with that label, avoiding
all earlier witnesses and graph points. If the interval lies on a refined
face, assign its witness to just one incident cell. Open intervals contain
more points than any finite forbidden list.

Choose a breadth-first tree of the component's cell graph rooted at a
marked cell. Retain the union of paths from all marked cells to this root.
This is exactly a subtree whose every leaf is marked. Retain t cells.
Choose fresh distinct portal points on its t-1 edges, AFTER choosing
witnesses, so they do not coincide with any witness. Subdivision of an
open arrangement face into smaller refined intervals does not affect this
construction or the bound t<=f.

For each retained cell connect its center to all assigned witnesses and
portals. The center must be strictly inside the cell and avoid all lines
through pairs of endpoints and all endpoint--graph-point lines, as in C19.
The implementation makes this a FINITE rational selection, not a retry
loop with an unsupported eventual-success assertion. Around a strict cell
sample choose a rational box whose halfplane signs stay strict. In that
box use the rational parabola

    q(t)=sample + (epsilon*t, epsilon*t^2), 0<t<1.

Include vertical lines through every forbidden point. If there are L
forbidden lines, each cuts this nondegenerate parabola in at most two
points. Trying t=j/(2L+2), j=1,...,2L+1, therefore succeeds. This includes
point avoidance. No square roots or trigonometric arithmetic are executed.

Convexity puts a center-to-boundary spoke strictly in its own cell before
the endpoint. The excluded lines prevent hitting punctures or overlapping
another spoke. Different open cells have disjoint interiors; globally
distinct endpoints rule out unwanted contacts. Therefore the resulting
geometric graph is embedded. Its combinatorial data is

    N_T=2t-1+k, E_T=2t-2+k, L_T=k  (only for k>=2).

The checker does not merely trust this argument on a supplied tree. It
checks all vertex coordinates against K, all entire tree edges against K,
all nonincident edge pairs for CLOSED intersection, all incident pairs for
same-ray overlap, connectivity, E_T=N_T-1, complete witness coverage, roles,
leaf degrees and the numerical corner inequality. Witness parameters must
be strictly between 0 and 1 and agree with the supplied coordinates.

C19's separately frozen L4 gives a simple polygonal disk surrounding this
tree in F with at most 2E_T+L_T corners. It treats straight degree-two
vertices, opposite rays and reflex angles via matched offset ports and
Jordan-disk splicing. Thus

    2E_T+L_T = 4t-4+3k
      <= 2ell*(ell+1)+3k
      <= 2e*(e+1)+3*(C(n,2)-e)
       = 2e^2-e+3*C(n,2).

For k=1 only one rational witness is needed, and for k=0 a remote rational
point is used. A small triangle handles either case. The single-vertex
tree is NOT put into the numerical 2E_T+L_T lemma. No affine change or GP
perturbation of the drawing occurs. Rational tube polygon generation is
not implemented, and C19's topology remains a candidate proof dependency.

C19 dependencies frozen at this base:
- fixed-placement proof SHA-256 7167f0f258ad4a990ef9f5ba2763bb815dffecde59bbc561152aeb75874e8796;
- rational-joint companion SHA-256 b442480658e6fcd15dc089e34c14e9fc5b8be2d6097453cc345868db7edee437.
Their exact local bytes were matched to the fresh repository blob identities.
C17 and C18 were reread; no earlier candidate was edited or promoted.

## 5. Executable contract and assurance boundary

Four standard-library-only Python files were implemented locally for this candidate:
geometry.py (rational validation and predicates), arrangement.py (complete
arrangement transcript and witness-tree construction), checker.py (canonical
arrangement rederivation plus direct tree validation), selftest.py (frozen
regressions and mutations). They are NOT present in the repository: the first
geometry.py write was blocked by the platform safety check, with no commit.
No alternative source-upload route was attempted. The other source files
were not submitted after that block. The following commands describe the
local replay and are pending repository source publication:

    python checker.py build INPUT.json > CERT.json
    python checker.py check INPUT.json CERT.json
    python selftest.py OUTPUT_DIRECTORY

An input is {"points":[[x,y],...],"edges":[[i,j],...]}; labels are zero based.
Coordinates are JSON integers or exact rational strings p/q. An optional
nonedges list must equal the ENTIRE complement, not just selected pairs.
Duplicate points, duplicate edges, loops, booleans-as-coordinates and floats
are invalid. Declared limits are n<=16, ell<=24, at most 256 bits per input
rational numerator/denominator, 1,000,000 bytes per input/certificate and
1,000 tree vertices. A work counter and external CPU/memory/time limits
bound each execution. Resource refusal is NOT mathematical rejection.

The rational arithmetic handles the full degenerate domain stated in
section 1, including a vertex inside a nonincident edge. This is not a
claim that all arbitrary large rational instances fit the fixed resource
caps, that all real inputs have machine encodings, or that any floating
approximation faithfully represents a rational input.

Checker acceptance means that the complete arrangement fields match exact
rederivation AND the supplied construction passes the applicable direct
checks. Cells or nonedge intervals cannot simply be omitted to fake an
empty intersection. The rederivation intentionally shares arrangement
code with the producer: it is NOT a separately trusted implementation.
The separate pairwise tree geometry checks add a different check surface
for positive certificates. Formal source-to-semantics replay and an admitted
consumer are still needed for high-assurance verification.

The negative output is named fixed_drawing_exists=false, never graph
obstacle number greater than one. The implementation does not enumerate
placements, run an SMT solver, or create an EvidenceLink.

## 6. Adversarial suite and actual finite observations

The stored execution covers 23 inputs, including empty targets, no lines,
isolated punctures, collinear forced witnesses, coincident lines, partially
covered lines, overlapping segments, a vertex on a nonincident edge,
forbidden and free concurrence, rational crossings, bounded free cells,
inside/outside incompatible targets, a gap of width 10^-40, nearly parallel
lines, and C18 under scaling, reflection and relabeling. It also checks all
160 labeled graphs on each three-point subset of the 2-by-3 integer grid,
using a separate three-point reference decision. These finite observations
do not replace the general proof above.

Sixteen certificate mutations and five invalid-input mutations are rejected.
They include deleted cells, omitted cuts, treating a whole line as a barrier,
opening a blocked face, forged component labels, omitted targets, fabricated
common labels, wrong negative exclusions, endpoint witnesses, identified
tree vertices, deleted tree edges, wrong corner counts, centers in K,
unknown vertex roles, wrong line signs and wrong zero-face status.

C18's original drawing produces 12 cells, 15 refined open 1-faces and 3
free-space components. In the canonical label order, uv has {1,2}, uw has
{0,2}, vw has {0,1}; the common intersection is empty, although all pairwise
intersections are nonempty. The complete graph's other nonedges are also
checked. Its 35 published-in-repository expected determinant values and
three specified crossings were actually recomputed exactly in this round.
This is still only a fixed-drawing negative control. The orientation-pattern
transfer clause from C18 is not tested or used as a graph-level obstruction.

The three-point collinear case with edge [(-1,0),(0,0)] and graph point
(1,0) is positive, with witnesses on y=0 and an embedded three-vertex tree.
Changing the only edge to [(-1,0),(1,0)] makes missing subsegments wholly
forbidden, so the condition is negative. These test the extra domain rather
than evading it. The square-cycle diagonal control gives a positive tree
inside the bounded component. Complete certificates for positive and
negative controls accompany the inputs and compact observations. Source
SHA-256 fingerprints are recorded, but the source files remain unpublished.

Execution versions, bounds, code fingerprints, exit status and output
hashes are recorded separately in execution.json. No floating geometry,
image inspection, CAS, solver or proof assistant was used.

## 7. Reasoning discipline, verification request and scope closure

Dependency DAG: compact K and finite graph/plane facts -> (A)<->(B);
refined faces + sign-cell completeness -> Q-component bijection;
parameter interval completeness -> (B)<->(C); common label + finite
center exclusions -> embedded tree; C19 L4 + displayed counts -> B17.
No implication to an all-placement lower bound appears in this DAG.

Invariants: K never moves, graph points are never treated as portals,
pruning retains all marks, exact rationals never become floating values,
and witnesses cover precisely the full complement. Monovariants: sorted
finite cut lists are traversed once; BFS visits a cell once; the retained
subtree removes all unused branches; center selection has at most 2L+1
trials. Boundaries: k=0/1, ell=0, unbounded faces and forbidden zero-faces
are explicit. Symmetry is tested by exact reflection/relabeling; no quotient
assumes a general-position representative. Probability is inapplicable.
Small gaps change rational values, not logical predicates; resource limits
are reported separately. Negative tests target completeness, not just SAT
witness syntax.

The current registry contains fixture-policy verifier identities, but no
registered consumer/action for this arrangement certificate was found.
The only current workflow is the three-job candidate transport gate. The
web principal has no evidence-signing ability. A verifier request specifies
the frozen inputs and first missing gate: an admitted compatible consumer
and faithful statement mapping. No fixture verifier is impersonated, no
workflow is changed or dispatched to manufacture a receipt, and no truth
record is edited. The user's authorization to start admission does not
supply the missing verifier capability.

Sources: C19/C17/C18 at the declared base. For topology used in Stage 2,
Jeff Erickson, Simple Polygons (2023), Jordan Polygon Theorem and
Point-in-Polygon Test, retrieved 2026-09-07:
https://jeffe.cs.illinois.edu/teaching/comptop/2023/notes/01-simple-polygons.html
CGAL 6.0.2 Arrangement_on_surface_2 documentation is a terminology and
isolated-vertex/split-edge cross-check, not a code or proof dependency:
https://doc.cgal.org/6.0.2/Arrangement_on_surface_2/classCGAL_1_1Arrangement__on__surface__2.html
No source full text is copied.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
unrestricted_one_obstacle_completeness: open
next_action: resolve the explicitly recorded source-publication block without
bypassing the platform check, then replay the fixed certificate through a
registered compatible verifier; do not promote local execution or CI.
