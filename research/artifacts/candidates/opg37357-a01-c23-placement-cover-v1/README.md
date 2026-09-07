# C23: component-cover optimum and the placement quantifier

Candidate: candidate:opg37357-a01-c23-placement-cover-v1
Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Base: 12e9354b8b567d7c6a551ac97c02f8d7da5e7bdf
Primary owner: math-proof

## 1. Frozen scope and current dependencies

The input is a finite simple labeled graph G and an injective real placement
p of its n vertices. K is the union of graph points and CLOSED graph-edge
segments; F is its open complement. There is no plane-layout or genericity
assumption. Put e=|E(G)| and k=C(n,2)-e. Each obstacle is nonempty and connected,
avoids K, and the obstacle family must hit every relative nonedge interior.
No obstacle is required when k=0. We distinguish this explicit exterior-point,
connected-obstacle convention from final faithfulness to the short canonical
contract. No protected contract or obligation record is changed.

C20 supplies the complete refined-arrangement correspondence; C21 supplies a
second implementation using strict elimination, not the unpublished C20 core.
Both are already merged. C22 supplies the X4 all-placement Q1 lower-bound
candidate and explicit unit-reason replay. None supplies Q2's uniform integer.
This file advances the P2 slice preserved in Issue #3 comment 5567810594.

## 2. Fixed-placement optimum is a finite set-cover number

Let C_p be the finite set of components of F, represented by C20's cell graph.
For every nonedge s define J_s={U in C_p: U meets the relative interior of s}.
Define tau(G,p) as the minimum cardinality of H subset C_p such that H meets
all J_s. Set tau=0 if k=0, and tau=infinity if some J_s is empty.

Claim C23.1. tau(G,p) equals the least number of connected obstacles at p.
Moreover, using the qualitative part of C19, the same optimum can be achieved
by pairwise disjoint bounded filled simple polygons, one in each chosen
component. This polygon conclusion is a separate dependency, not an automatic
property of a supplied arbitrary connected obstacle.

Proof of the lower inequality. Each connected obstacle lies in one component
of F. If h obstacles block the nonedges, their at most h component labels meet
all J_s. Hence tau<=h. This proof also handles multiple obstacles in the same
component and obstacles with empty interior. Endpoints cannot be hits because
they lie in K.

Proof of the upper inequality. For a finite covering set H, assign each target
nonedge to one chosen component that it meets. Delete unused components. In
each used component choose one interior-segment witness per assigned target.
Openness supplies intervals of choices, including original tangencies. Join
these finitely many witnesses to one of them by finite polygonal paths in the
component. Components of an open planar set are polygonally path connected,
as proved in C19/C20. The finite path union is compact, nonempty, connected,
and disjoint from K. One such union per component gives at most |H| obstacles.
If polygonal disks are required, apply the witness-tree and thin-disk step of
C19 separately within each component. Different components are disjoint, so
the resulting polygons are pairwise disjoint. For k=0 use the empty family.
If J_s is empty for some s, its entire relative segment lies in K, and no
number of obstacles avoiding K can hit it. Thus infinity is not a tool error.

A minimum nonempty cover H has a private target for every U in H: otherwise U
could be removed. Consequently there is an assignment with a NONEMPTY target
group for every selected component. This fact will be used in the count.

## 3. A simultaneous corner budget, not h copies of a whole-graph budget

Claim C23.2. If 1<=h=tau(G,p)<infinity, there is a representation at the SAME
placement by h pairwise disjoint filled simple polygons with total corners
at most

    4f-4h+3k <= 2e^2-e+3*C(n,2)+4-4h,

where f<=1+ell(ell+1)/2 counts the 2-cells of the ell<=e distinct graph-edge
supporting lines. C19's tube/Jordan count is an explicit dependency.

Assign all k targets to the h selected components, with group sizes k_u>=1.
For k_u>=2, the C19 construction inside that component retains t_u marked
cells after pruning, giving E_u=2t_u-2+k_u and L_u=k_u. Its tube polygon has
at most 4t_u-4+3k_u corners. For k_u=1, choose a small triangle around one
witness and set t_u=1; the SAME expression is then 3. A witness on a supporting
line is assigned to either incident cell, both in its component. The triangle
need not stay in that cell, only in its open component.

Distinct selected components have disjoint sets of eligible cells. Therefore
sum t_u<=f; one must not charge the whole f separately for every component.
Summing the h bounds and sum k_u=k gives 4f-4h+3k. Substitution yields

    4(1+e(e+1)/2)-4h+3(C(n,2)-e)
      =2e^2-e+3*C(n,2)+4-4h.

For h=1 this recovers C17's bound apart from its explicit maximum with 3.
The case k=0 has h=0 and zero total corners; it is NOT charged a harmless
polygon. Empty groups cannot be counted to obtain a spurious -4 saving.
An arbitrary nonminimal cover must first lose its unused/redundant components.
This bound controls complexity of an existing representation, not h uniformly
in n. No tube polygon is generated by fan_certificate.py using this lemma.

## 4. Unrestricted minimization and the exact remaining quantifiers

Let obs_ext(G) denote the obstacle number under the explicit convention in
section 1. By C23.1 (and C19 for simple polygons),

    obs_ext(G) = min over injective real placements p of tau(G,p).

This minimum exists. A generic placement has each nonedge meeting F, so one
small obstacle per nonedge gives a finite value at most k. The nonempty set of
attainable nonnegative integer values has a least element. No compactness of
the space of placements, fixed bounding box or coordinate-bit bound is used.

The two root interfaces are now:
P1: exists finite planar G, for ALL p, tau(G,p)>=2.
P2: exists integer h>=1, for ALL finite planar G, exists p, tau(G,p)<=h.
Negating P2 requires: for EVERY h, exists finite planar G, for ALL p,
tau(G,p)>h. A sequence of pairs (G_r,p_r) with tau(G_r,p_r) growing proves
none of these placement-universal lower bounds.

Fixed-graph decision for a proposed h can use up to min(h,k) obstacle groups
and the total corner budget in section 3, compiling the visibility clauses
with an OR over obstacles for each nonedge. This is only a finite reduction
for one fixed graph size. It leaves the uniform-h question untouched.

## 5. An exact infinite control family for the missing minimization

For r>=3 let F_r be the fan with vertices 0,1,...,r, edges {0,i} for all
1<=i<=r and {i,i+1} for 1<=i<r. Its only nonedges are i,j with 1<=i<j<=r
and j-i>=2. It is planar, as the first drawing below explicitly shows.

### 5.1 A convex drawing with growing optimum

Place p_i=(i,i^2), including p_0=(0,0). All points are in convex position and
no three are collinear. The fan triangulates their convex hull into the open
triangles D_a=(p_0,p_a,p_(a+1)), 1<=a<r. These and the exterior are precisely
the free components: the drawn graph is the polygon boundary plus fan spokes.
For the nonedge i,j, its relative interior visits exactly

    J_(i,j)={D_i,D_(i+1),...,D_(j-1)}.

To verify this without an image, its line is y=(i+j)x-ij, with i<x<j. The
slope y/x=i+j-ij/x increases strictly from i to j. It crosses spoke y=a*x
at x=ij/(i+j-a) for each i<a<j. This point is strictly between 0 and p_a,
since a(i+j-a)-ij=(a-i)(j-a)>0. The crossings occur in increasing order.
Strict convexity excludes all other boundary-edge contacts except the two
endpoints; consecutive spoke intervals are in consecutive fan triangles.

In particular nonedges i,i+2 demand hitting every consecutive pair
{D_i,D_(i+1)}. Selecting even-indexed triangles hits every such pair and
every longer interval. The disjoint pairs
{D_1,D_2},{D_3,D_4},... form a matching of floor((r-1)/2) target constraints,
so fewer components cannot cover them. Therefore

    tau(F_r,p_convex)=floor((r-1)/2).

This is an all-r theorem about the SPECIFIED drawings, not the graph optimum.

### 5.2 A different explicit drawing with one convex obstacle

Keep p_i=(i,i^2) for 1<=i<=r but place p_0=(0,-r^2). Let

    P_r = convex hull of {(i,i^2+1/2): 1<=i<=r}.

This is an r-corner convex polygon. Its lower boundary b(x) is the linear
interpolation of the shifted parabola samples. Its upper boundary is
u(x)=(r+1)x-r+1/2, for 1<=x<=r. All graph vertices are below b or outside
the x range. A path edge i,i+1 is exactly b(x)-1/2 on its own interval.
The apex edge to p_j has y=-r^2+(j+r^2/j)x, 0<=x<=j, and

    y-x^2=(j-x)(x-r^2/j)<=0.

Thus every graph edge avoids the closed polygon; no edge-crossing convention
or numerical tolerance is used in this argument.

For a nonedge i,j use its midpoint x=(i+j)/2. The chord height is
x^2+(j-i)^2/4. If x is integral, b(x)=x^2+1/2; otherwise
b(x)=x^2+1/4+1/2. Since j-i>=2, the midpoint is above b by at least 1/2.
Every chord of the unshifted parabola samples lies at or below
(r+1)x-r: the endpoint slack there is (i-1)(r-i)>=0 and interpolation
preserves it. Hence this midpoint is also strictly below u, and 1<x<r.
It is strictly interior to P_r, blocking the nonedge.

The graph placement is in general position. For path triples the determinant
is (j-i)(k-i)(k-j)>0. For p_0,p_i,p_j it is
(j-i)(ij-r^2)<0 when 1<=i<j<=r. Thus no hidden collinear placement is used.
The graph is not complete, so zero obstacles cannot represent it. We obtain

    obs_ext(F_r)=1 for EVERY r>=3,

despite the divergent fixed-drawing optima in 5.1. For r=1,2 the graphs are
complete and have obstacle number zero; they are excluded from the polygon
constructor rather than represented by a degenerate one/two-corner polygon.

This family rules out using growing covers in one prescribed convex drawing
as a P2 lower-bound route. It supplies no universal single-obstacle placement
for all planar graphs; X4's separately stored all-placement obstruction is
not challenged. Existence for a family and existence for every planar G are
kept different. No novelty claim is made for fan obstacle representations.

## 6. Executable controls, restrictions, and source safety

fan_certificate.py uses only fractions.Fraction, itertools, json and sys.
It has no file reads/writes, network, subprocess, dynamic execution, credentials
or environment reads. Input is one integer r in [3,32]; default runs a bounded
finite suite. `python fan_certificate.py 5` prints an explicit placement,
polygon and edge list. The midpoint rule gives all nonedge witnesses.

The default execution checks r=3,...,12,16,24,32. For each it checks strict
polygon convexity, graph-point exclusion, every edge against every closed
polygon side, every nonedge midpoint in the strict polygon interior, and
all graph-vertex triples. Separately it checks the exact spoke intersections,
all nonedge/graph-edge contacts, the even-triangle cover and matching lower
certificate for the convex drawing. For r<=12 it also enumerates ALL component
subsets to compute the minimum cover. Larger controls check the displayed
cover/packing certificates instead of claiming exhaustive enumeration.

Three rejected geometric mutations use zero vertical shift, shift 2, and
the unshifted apex with the same convex polygon. Four invalid parameter
cases are also rejected. Actual environment, limits, source/output digests
and exit status are in execution.json. No floating geometry, external solver,
proof assistant or arbitrary placement search is run. Finite controls do not
prove either universal theorem; the arguments above supply the candidate proof.

## 7. Scope, prior delivery, and admission request

Candidate-local layers remain T (C19 tube/Jordan), A (C20/C21 arrangement),
P1 (C22 X4 all-placement), and P2 (this cover formulation and the unsolved-in-
repository uniform-h quantifier). These are manuscript labels, not fabricated
canonical obligation records. No prior candidate is edited or withdrawn:
what fails here is the stronger fixed-to-unrestricted inference.

The live C21 already contains six ordinary-text replacement/replay modules.
Its different strict-elimination core is not C20's unavailable five original
byte strings. Those original fingerprints do not supply recoverable source,
and this cycle neither retries a blocked payload nor invents an attachment.
C21 and C22 are reused instead of being transported again. Their execution
claims retain their own recorded scope and are not reported as new C23 runs.

Fresh research/verifiers.json still lists fixture-policy identities, with no
compatible callable consumer for these geometric statements. Request a trusted
statement-faithfulness review of the exterior-point convention, C23.1, the
nonempty-group count, and the all-r fan construction, followed by the admitted
closure process. There is no signed mathematical receipt or new EvidenceLink.
T's topology remains a dependency for the polygon count, not for the direct
convex fan visibility argument. Q1's published answer and stored candidate
are not a resolution of Q2.

Reasoning audit: finite witnesses and exact inequalities are explicit;
component pruning preserves assigned targets and decreases a finite vertex
count; the finite cover minimization uses well-ordering, not a compactness
assumption on placements. Counts handle k=0/1 and empty groups. The matching
lower certificate applies only to the stated layout. Reflections and positive
scalings preserve all claims, but no quotient discards layouts. Probability is
not used. Source-to-theorem, universal code correctness and trusted admission
remain open; no CI result supplies them.

Sources: C19 fixed-placement proof, C20 theorem and four certificates, C21
second-core replay, C22 all-placement README/checkpoint, and the canonical
ProblemContract at the declared base. External prior-art context is recorded
in the existing C22 source references; it is not the proof of C23's formulas.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: continue P2 by eliminating arbitrary coordinates into a finite
placement-sign atlas, preserving realizability and possible line concurrency;
do not assert that vertex triple orientations alone encode every free face.
