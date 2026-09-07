# C27: component-guarded X4 audit and a geometric failure of additive gluing

Candidate: candidate:opg37357-a01-c27-fiber-guard-gluing-v1
Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Primary owner: math-proof (bounded exact computation as a supporting method)
Repository: vibemathing/problem-opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Base: e358fe83f026715b0b6ddf868f84a58c3bdf91fe
Issue: #3

## 1. Scope, fresh-state reuse and new objects

Fresh main already contained C26's geometric-to-CNF bridge and copy-only
amplification barrier. Those files, C22's contradiction and C25's quartic
atlas are not retransported or silently edited. C27 adds:

- a new exact-coordinate finite-segment vertical decomposition, importing
  NONE of C20, C21 or C25's arrangement/decoder code;
- a separate source-record consumer for all 69,332 C22 clauses, with actual
  common-component guards checked against that decomposition;
- an actual two-polygon witness against removing the same-obstacle guard;
- an explicit all-r planar clique-gluing family with arbitrarily many local
  demands but ONE convex obstacle, rejecting generic additive/capacity shortcuts;
- a weighted component-cover lower-bound interface with its placement quantifier.

The frozen graph/obstacle convention is a finite simple labeled G, injective
real vertex points, K the union of all graph points and CLOSED graph-edge
segments, and nonempty connected obstacles avoiding K. Each nonedge must be
hit. Graph-edge crossings are allowed. The implementation accepts rational
coordinates; it does not approximate arbitrary real inputs by floats.

The X4 conclusion is still only a single-obstacle LOWER-BOUND CANDIDATE,
conditional on the frozen C22 propositional contradiction and final semantic
acceptance. C22's RUP is not rerun here. No tested bad drawing is an all-placement
obstruction by itself. No uniform bound for all planar graphs is claimed.

## 2. Continuous bridge: paths, one margin, and first exit

For any fixed G, K is closed and compact, so F=R^2 minus K is open. Each
component U of F is open and polygonally path connected: small free balls
make the polygonally reachable set from one point and its relative complement
open; connectedness of U leaves no unreachable point. A connected obstacle
O is contained in one such U, even if O itself is not path connected.

For each nonedge choose a hit z_s=(1-t_s)p_i+t_s p_j, 0<t_s<1. Endpoints are
excluded because they are in K. Since U is open, a nonempty parameter interval
around t_s is also in U, even when the original hit is only a tangency to O.
Join the finite witnesses by finite polygonal paths in U. Their union T is
compact and path connected, disjoint from K. For nonempty K set d=dist(T,K)>0.
If K is empty there are no graph nonedges and the remote-obstacle case is direct.

Choose epsilon=d/4 and O'=T+closed_ball(0,epsilon). Then O' is compact and
path connected, dist(O',K)>=3d/4, and every z_s has a ball of radius epsilon
inside O'. Keep O' FIXED while moving the drawing. If

  max_i ||p'_i-p_i|| < eta,
  0<eta<min(d/8, min_(i<j)||p_i-p_j||/4),

all graph points stay distinct, every entire moved closed edge stays at least
3d/4-eta away from O', and every moved nonedge witness with the SAME t_s stays
within eta<epsilon of z_s, hence in int(O'). This is ONE positive margin for
all edges and all targets, not a separate uncontrolled perturbation per clause.
For k=0 choose a remote small disk; for k=1 the path union can be a singleton.
For finitely many obstacles first assign finite targets, discard unused ones,
and take the minimum of the finitely many corresponding positive margins.

Only after this margin is supplied do we choose a new GP placement in the
safe coordinate box. Avoid the finitely many triple-determinant zero sets;
for C25's stronger chart also avoid vertical pair lines and parallel distinct
pair lines. These are nonzero polynomials, so their product has zero set with
empty interior. This gives existence in the ALREADY SAFE box; density alone
would not keep boundary-only contacts blocked. We do not assert that the old
obstacle, old signs, or fixed-drawing optimum survives every perturbation.
The new obstacle need not be a simple polygon; the lower-bound implication
allows a larger class. C19's corner-count theorem is not used here.

At GP coordinates put D(a,b,c)=det(p_b-p_a,p_c-p_a). Let ab and cd be distinct
nonedges (one common endpoint is permitted). Suppose graph a--b paths P+ and
P- lie in one closed halfplane of cd, with all their internal vertices strictly
on opposite sides of ab. Their geometric walks lie strictly above/below ab
except at a,b. Subdivide at every geometric crossing and erase loops. In GP,
different graph edges cannot overlap in an interval, so this is a finite
subdivision even at multiple concurrence. It yields two simple arcs meeting
only at a,b. Their union Gamma is a polygonal Jordan curve made from K.
The two half-disks glued along [a,b] put the WHOLE (a,b) in its bounded region D.

Both paths must use the SAME closed halfplane of cd: they share an endpoint
outside {c,d}, whose sign is strict. The curve and bounded region stay in that
halfplane (any point in the opposite halfplane has an escaping ray). Since D
is open, it misses the line cd. The open segment (c,d) misses Gamma as well:
in GP, a graph segment in that halfplane can touch the line only at c or d,
or be the absent edge cd. Shared endpoints do not change this open-segment fact.

Here is the requested path-crossing order without assuming O is path connected.
If a component U met both nonedges, choose z in U intersect (a,b), w in U
intersect (c,d), and a continuous polygonal path gamma:[0,1]->U between them.
It starts in D and ends outside its closure. The connected interval of times
starting at 0 on which gamma remains in D has a supremum t*. By continuity,
gamma(t*) belongs to boundary(D)=Gamma: it cannot be outside closure(D), and
if it were in the open D that initial interval would extend. This is the
FIRST EXIT from D and hence a forbidden hit in K, contradicting gamma subset U.
Thus J_ab intersect J_cd must be empty whenever both opposing key paths exist.
No pictures, crossing-free obstacle drawing, or unjustified path in O is used.

## 3. Clause faithfulness and complete source output

Variables x_ijk for increasing triples, in lexicographic order, mean D(i,j,k)>0.
Odd permutations negate literals; GP is essential for complementing a sign.
For X4 there are 120 such variables. For each ordered distinct pair of its 21
nonedges use a separate side variable, numbered 121,...,540. One side is shared
by ALL retained paths for that ordered pair; it is not reselected per path.

Four-point clauses have an ordered quadruple origin and NO nonedge pair:

  D(b,c,d)=D(a,b,c)+D(a,c,d)+D(a,d,b),
  not x_abc OR not x_acd OR not x_adb OR x_bcd.

Five-point clauses have an ordered quintuple origin and NO nonedge pair:

  D(a,b,d)D(a,c,e)=D(a,b,c)D(a,d,e)+D(a,b,e)D(a,c,d).

Under positivity of abc, acd, ade, abe, the two left factors have the same sign.
If A is the disjunction of the four negated premises, the two clauses are
A OR x_abd OR not x_ace, and A OR not x_abd OR x_ace.
Assigning fictitious nonedges to these algebraic clauses would be wrong.

For a key-path row the source specifies its ordered nonedges ab,cd, exact graph
path P from a to b, and mode 0..3. Let C=(x_cdv: v in P except c,d) and
J=(x_abv: v internal to P). Both lists are nonempty. All C literals equal means
P is cd-key. The four raw clauses, in mode order, are

  OR C     OR not s OR OR J;
  OR C     OR s     OR OR not J;
  OR not C OR not s OR OR J;
  OR not C OR s     OR OR not J.

When C is mixed both premise disjunctions are true. Otherwise one pair enforces
that the internal path has a vertex on the chosen side. An all-positive key
path forces s=true; an all-negative key path forces s=false. The first-exit
lemma forbids both forces whenever J_ab and J_cd share a component. Choose the
forced value if there is one, and false if neither is forced. This supplies
one value for ALL relevant paths. Four-point and five-point identities hold
without any obstacle premise. If one obstacle blocks every nonedge, every
ordered pair has a common component and ALL the unguarded clauses follow.

Only paths of at most four edges are retained. They form a subset of the paths
covered by the lemma. Dropping longer-path clauses is a relaxation of necessary
conditions; UNSAT of that relaxation suffices. Duplicate/tautology removal and
literal sorting preserve conjunction semantics; no increasing-label-only path
restriction is made.

C26's frozen compiler is reused as an UNTRUSTED origin producer. guards.py uses
a different cyclic-minimum parity rule, direct tuple/path membership checks,
and reconstructs each row without importing that compiler. Its path comparison
enumerates internal-vertex permutations instead of C26's DFS. Exact input and
CNF digest are frozen. All 69,332 source rows reconstruct the original clauses:
420 four-point, 20,160 five-point and 48,752 key rows, 540 variables, 804 paths.
CNF SHA-256 remains
  de54d35f78d3c7d84e24651e5ce6f82c9ebe6d78bc7bd2deb66aa591e6ea276c.

The --sources entry ACTUALLY emitted every row as ordinary TSV:
  row_id, family, ab_or_dash, cd_or_dash, tuple_or_path, mode.
It has 1,807,486 bytes and SHA-256
  79f40490af759056950eea71182747e402d31c593e3f2e16357042bdb019d4b6.
This derived table can be regenerated from repository source; it exceeds the
one-file candidate limit and is not stored as an oversized repository file.
The full emitter, frozen producer and digest are the reproducibility interface.
It is not a new proof trace or a replay of C22's existing RUP contradiction.

## 4. A third geometry core: finite-segment vertical fibers

fiber.py receives points and graph edges, not support-line signs. Let X contain
all graph-point x-coordinates and the x-coordinate of every pairwise segment
intersection. Collinear intersections contribute overlap endpoints. All entries
are exact rationals; zero-width/touching cases are not merged by a tolerance.

Between consecutive x-events, every nonvertical segment is either present
throughout the open slab or absent throughout it. Present segments have a fixed
vertical order, since all their intersections are events. Coincident walls are
deduplicated. The open regions between successive affine wall heights are bands;
they are convex and contain no graph-point puncture (all point x values are events).
They give one node each, including the unbounded bands and outer slabs.

At an event x0, intersect K with the vertical line. This is a finite union of
CLOSED vertical intervals and points: vertical edges contribute intervals;
other edges and all graph vertices at x0 contribute points. Merge overlapping
or touching closed intervals exactly. Each complementary open y-interval gives
one fiber node. Its sample y is unequal to every adjacent slab-wall endpoint
height, since those endpoints are in K. Its rank among the limiting heights
therefore identifies one adjacent band on each side, joined to this fiber node.
Different samples in the same free fiber interval have the same rank: any rank
change would cross a forbidden endpoint height within that free interval.

Soundness: a free fiber sample has a free ball, and strict height inequalities
persist just to either side. Thus each graph link has a local free path; every
band and fiber interval is path connected. Graph connectivity is real connectivity.
Completeness: every point of F lies in a band or free fiber interval. Assign its
finite graph component label. Near a free event-line point all nearby regions
are precisely its fiber and the linked neighboring bands, so the label is locally
constant. Away from event lines it is constant within a band. Therefore no true
connected component can split into different labels. These statements prove a
bijection between finite graph components and pi_0(F), with no GP assumption.
The empty drawing gives one whole-plane band; isolated points do not disconnect it.

For each nonedge split its parameter interval at graph points on it, all x-events
it crosses, and all intersections/overlap endpoints with actual graph edges.
Every open subinterval is wholly forbidden or in a single free node. A vertical
nonedge remains in one event fiber but is split at all edge/point hits there.
A free isolated cut point has a free ball and thus a neighboring free subinterval
of the same component. Forbidden cut points cannot block a nonedge. Unioning the
subinterval labels gives its COMPLETE incidence J_s and the common intersection.
The report contains samples, events, bands, fiber gaps, links, labels and every
nonedge interval; it is not just a count of faces or a Boolean flag.

The implementation uses only rational integer comparisons. It imports none of
C20/C21/C25. A second combinatorial finite check planarizes segments at their
crossings, deduplicates overlaps and computes E-V+components+1; this checks the
component COUNT, not by itself the incidence theorem. Different implementations
in this same generation domain still are not different trusted verifier domains.

## 5. Executed degeneration atlas and same-obstacle mutation

The theorem domain is arbitrary finite injective REAL drawings. fiber.py is
bounded to rational inputs with n<=32, edges<=128, input numerators/denominators
<=256 bits, <=1000 x-events and <=20000 decomposition nodes. Exceeding a cap
raises an error, never a mathematical negative. CNF production is capped by the
reused C26 interface at n<=10 and path length<=4. No C25 decoder is run on X4.

B_a=0: vertical lines only invalidate a direct Dstar chart call; the fiber core
and GP determinant clauses remain applicable. The swapped X4 control has four
vertical pair lines and passed. W_ab=0: parallel lines similarly do not invalidate
GP clauses; each X4 control has 50 parallel pair-line pairs. Delta=0: nonvertex
concurrence is permitted. On p_i=(i-5,(i-5)^2), pair lines (1,6),(3,7),(4,9)
concur at (0,4) away from graph vertices; this exact event is checked. Forced
vertex concurrence is also retained, not perturbed into a simple arrangement.

Graph-vertex collinearity/overlap: Boolean orientation projection is refused,
not assigned a fabricated bit. Arbitrary fiber incidence remains supported;
for the universal implication use the hypothetical-representation margin of
section 2 before GP projection. Whole nonedges covered by a UNION of graph
edges yield empty incidence, even if no single edge covers the nonedge.
Partial support-line coverage, isolated punctures, contact-only blocking,
vertical gaps, near-parallel edges, shared nonedge endpoints and geometrically
self-crossing paths have separate exact controls in checks.py.

Actual observations: 18 drawing fixtures, all 160 graphs on the 20 three-point
subsets of a 2-by-3 integer grid, 16 rejected mutations, and four GP X4 drawings.
All four X4 inputs have 82 free components. Each has 106 ordered opposing-path
conflicts; every conflict has disjoint target-component sets. Every algebraic
row and every key row activated by actual common incidence passes: 47,132 active
rows per X4 drawing. False UNGUARDED rows for disjoint-component pairs are recorded
as inactive, not as failed single-obstacle implications. All data are finite tests.

The self-crossing path control has points
  (-2,0),(2,0),(2,4),(-2,4),(0,-2),(-7,-11/2),(-8,-15/2)
and edges 02,13,23,04,14. The upper walk 0-2-3-1 crosses itself at (0,2),
while 0-4-1 lies below. All 35 vertex triples are noncollinear. The code records
actual disjoint component sets and a shared-endpoint key pair as well.

Here is an ACTUAL representation against deleting the many-obstacle guard.
Take points (-2,-2),(2,-2),(2,2),(-2,2),(6,0), edges 01,03,12,23, and rectangles
  O1=[-1/4,1/4] x [-1/4,1/4],
  O2=[7/2,9/2] x [-3/2,3/2].
All graph points/edges avoid both closed polygons. Their six nonedge witnesses
are stored exactly in observation.json. Targets 02 and 14 are in different
components. Paths 0-3-2 and 0-1-2 are 14-key and force opposite sides of 02.
The two obstacles can block those two targets separately. Accordingly a shared
side requirement without a same-obstacle guard is invalid for this representation.
The actual projection also records false row 4 for targets 13,24, source path
1-2-3/mode 0: clause (-7 OR 8 OR -10 OR -24) is false in its displayed assignment.
This is a counterexample to the UNGUARDED MULTI-obstacle extension, not to any
C22 claim with its original one-obstacle premise. No global minimality is claimed.

For h obstacles one may assign each target to one obstacle. The correct row C
for targets s,t and color r is not z_(s,r) OR not z_(t,r) OR C. This implication
is justified by the pair-local first-exit lemma. SAT of its necessary relaxation
still does not construct a placement or h obstacles.

## 6. Exact clique-gluing counterexample: arbitrarily many demands, one polygon

Reject the proposed general rule that sums of positive local obstacle demands
become additive merely because planar blocks are glued along cliques. A stronger
explicit diagnostic than an abstract coloring is available.

For EVERY integer r>=3 let G_r=K_(1,r), with center 0 and leaves 1,...,r.
Place
  p_0=(0,-r^2), p_i=(i,i^2) for 1<=i<=r.
Put q_ij=(p_i+p_j)/2 for 1<=i<j<=r, Q_r=conv{q_ij}, and
  epsilon=1/(64(r+1)), P_r=Q_r+[-epsilon,epsilon]^2.
P_r is a bounded filled convex polygon with nonempty interior; remove redundant
collinear hull points. The construction is finite and rational. Each q_ij lies
in its interior because the open epsilon-square about q_ij is contained in P_r.

For any midpoint q_ij, q_y-q_x^2=(j-i)^2/4>=1/4. For a convex combination q
of such midpoints, the variance identity yields
  q_y-q_x^2 = sum lambda_a*(q_(a,y)-q_(a,x)^2)
             + sum lambda_a*q_(a,x)^2-(sum lambda_a*q_(a,x))^2 >=1/4.
Also 1<=q_x<=r. For |u_x|,|u_y|<=epsilon, therefore
  (q_y+u_y)-(q_x+u_x)^2
    >=1/4-(2r+1)epsilon-epsilon^2 >0.
The strict inequality follows from (2r+1)/(64(r+1))<1/32 and epsilon^2<1/4096.
Every point of P_r is strictly above the parabola y=x^2.

On graph spoke 0j, the point with 0<=x<=j has
  y=-r^2+(j+r^2/j)x,
  y-x^2=(j-x)(x-r^2/j)<=0,
since j<=r. Thus every whole CLOSED graph edge avoids P_r. The leaves lie on
the parabola and the apex below it, so all graph points are exterior. All
nonedges are leaf pairs and their midpoints are strictly inside P_r. Hence
  obs_ext(G_r)=1 for every r>=3,
with zero excluded because G_r is not complete. This proof does not use C19.

The drawing is itself plane: two spokes can meet only at the center since
leaf directions are distinct. Equality of slopes i+r^2/i and j+r^2/j for i<j
would give ij=r^2, impossible. It is vertex-GP as well: leaf triple determinants
are nonzero Vandermonde products, and D(0,i,j)=(j-i)(ij-r^2) !=0.

Now write G_r as the union of H_i=G_r[{0,1,i}], 2<=i<=r. Each H_i is an
INDUCED P3 with sole internal nonedge 1i. Distinct blocks intersect exactly in
the CLIQUE edge 01. Their union has r+1 vertices, r distinct edges, no loops
or parallel edges, and the plane drawing above proves simple planarity.
There are t=r-1 distinct internal demands, each with local obstacle number one.
ALL cross-block leaf pairs ij are additional nonedges and are blocked by the
SAME P_r; they have not been omitted to manufacture the counterexample.

Thus this clique-gluing construction has t arbitrarily large but needs one
obstacle, not the sum t. One obstacle participates in every one of the t demand
blocks, so no constant participation capacity follows from clique overlap alone.
This rejects that proposed composition rule. It does NOT reject C26's conditional
capacity inequality or the possibility of a stronger X4-specific construction.
In particular these P3 blocks have local lower bound ONE, not X4's TWO.

Smallest instance of this two-distinct-P3-along-K2 route: r=3, four vertices,
points (0,-9),(1,1),(2,4),(3,9), edges 01,02,03. A CCW obstacle has vertices
  (383,639)/256, (385,639)/256, (641,1663)/256,
  (641,1665)/256, (639,1665)/256, (511,1281)/256, (383,641)/256.
The blocks are {0,1,2} and {0,1,3}. Distinct connected induced blocks with a
positive obstacle number need at least three vertices each; two distinct such
three-vertex blocks sharing an edge need at least four union vertices. This
qualifies minimality only for this rule/construction, not all amplification ideas.
Actual code checks r=3,4,5,7,12,20, including every graph edge and EVERY nonedge.
The all-r statement follows from the inequalities, not that finite sample.

## 7. A usable growth obligation: weighted component capacity

For one drawing let J_s be complete nonedge-component incidence. Its connected-
obstacle optimum is the minimum component cover: one component per connected
obstacle gives the lower inequality; finite witnesses joined by polygonal paths
within each selected open component give the converse. Empty targets require
zero obstacles; an empty J_s makes all representations impossible. Simplicity
of extracted polygon obstacles is a separate C19 qualitative step.

Let nonnegative weights w_s satisfy, for EVERY actual free component U,
  sum_(s: U in J_s) w_s <= 1.
If h connected obstacles cover all targets, their at most h component labels
H satisfy
  sum_s w_s <= sum_(U in H) sum_(s:U in J_s) w_s <= |H| <= h.
Therefore h>=ceil(sum_s w_s). Components with no hit contribute zero. An obstacle
meeting many nonedges consumes that component's complete load; repeated obstacles
in one component cannot improve the counting argument. This is a finite certificate
inequality, not an appeal to unverified linear-programming output.

For an all-placement graph-family lower bound f(r), the missing hypothesis is:
  for every injective placement p of G_r, there exist such weights w_s(p)
  with total > f(r)-1 (or some nonedge has empty incidence).
Weights may depend on the placement. Exhibiting them for selected numerical
layouts does not satisfy this universal quantifier. If true for f(r)->infinity,
this would negate the uniform-h root. No such family is asserted in C27.

The exact checker accepts C18 weights 1 on targets 04,05,26, giving the known
fixed-drawing bound three, and rejects weight 1 on both local targets 12,13
of the four-vertex star: its sole component would have load two. This latter
rejection pinpoints the unproved step in naive additivity. Next actionable
obligation is a planar construction forcing these component loads uniformly
across all placements, possibly via cross-block key paths or higher-rank demands.
The already-merged copy-only X4 barrier must not be repeated as a growth proof.

## 8. Reproduction, audit repairs, and admission gaps

From this directory with the ALREADY MERGED C26 module on the search path:
  PYTHONPATH=../opg37357-a01-c26-placement-bridge-growth-v1 python -B checks.py
  PYTHONPATH=../opg37357-a01-c26-placement-bridge-growth-v1 python -B checks.py --sources
Apply externally: 30 CPU seconds, 40 wall seconds, 512 MiB address space,
one mathematical worker, and 4 MiB output limit. The command prints JSON or TSV;
mathematical modules do not read/write files, use a network, create subprocesses,
access credentials/environment variables, or dynamically evaluate code.
Execution.json records actual versions, source/output fingerprints and exit codes.
The external bounded runner is not a hidden operation inside the uploaded code.

Three exploratory defects were corrected before the frozen successful runs:
(1) the three-point reference wrongly checked coverage by ONE edge, not their
union; it failed on collinear points with two consecutive covering edges;
(2) the public intersection helper with raw integer inputs returned floats;
explicit Fraction conversion and a type regression fixed this (model inputs
were already rational); (3) a preliminary crossed fixture had a collinear triple,
so its replacement is checked by all 35 triples. These are recorded repairs,
not suppressed test failures or purported counterexamples to X4's true premise.

Candidate-local layers remain separate, without editing the admitted DAG:
T: C19 tree/tube/Jordan proof and B17; no polygon is extracted from a fiber graph.
A: C20/C21 arrangement, C25 realized-signature decoding, and this new fiber model.
P1: C26/C27 common-component-to-key clauses, regularization, plus C22's FROZEN
propositional contradiction and abstract X4 planarity. No new RUP run is claimed.
P2: weighted growth certificates for ALL placements; the clique-additivity route
is rejected, but the unrestricted uniform bound is not decided.

The canonical short polygonal-obstacle contract must still be faithfully mapped
to connected exterior obstacles, and a trusted verifier must accept the universal
implication and the frozen contradiction. Research/verifiers.json at this base
still registers fixture policies, not a compatible mathematical consumer/action.
No EvidenceLink, Result or Solution is produced. The original five C20 source
byte strings remain unavailable; their fingerprints are not recovered code. They
are not retried, duplicated or claimed delivered in this packet.

Source provenance: C22/C25/C26 at the stated base. The geometric clause families
are published prior art: Berman et al., Graphs with Obstacle Number Greater than
One, JGAA 21(6), 1107-1119 (2017), DOI 10.7155/jgaa.00452, Lemmas 1-3,
Observation 2, Proposition 3. Primary source compared this round:
https://jgaa.info/index.php/jgaa/article/download/paper452/2511/2318
Only statement comparisons are retained, not source full text. No novelty claim
is made for X4's known obstruction or convex representations of stars.

Reasoning audit: first-exit continuity and one uniform margin are explicit;
finite event/interval lists and traversal give termination; exact arithmetic
keeps degeneracies; source origins bind each row; empty/single targets, infinity,
verticals and boundary contacts are distinct. Minimality is qualified. All-r
star inequalities and weighted sums are symbolic proofs, not finite inference.
Reflection/coordinate swap/tiny scaling are controls, not a quotient of placements.
No probability argument is used. Universal code correctness and trusted admission
remain open despite successful bounded checks and transport.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: seek a planar graph family with placement-universal weighted component
capacity or genuinely cross-block incompatible demands; retain the audited X4
single-obstacle candidate and submit it to a compatible registered trusted gate.
