# C16: quantitative rational sparse-to-GP witness extraction

Candidate: candidate:opg37357-a01-c16-quantitative-gp-v1
Verdict: candidate_only
Owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: d7c9dbbb81ffd89cea1e15691ad32d14f3a6ece3

## 1. Frozen certificate input and claim

Fix n>=1,m>=3 and an exact rational satisfying assignment of the c07/c11
sparse formula S_(G,m). Coordinates are rational, anchors are p1=(0,0) and
p2=(1,0) when n>=2, and all crossing/prefix bits are their exact satisfying
values. This assumption is not inferred from a model label or solver response.
It must be checked by a later authorized replay.

In addition, supply rational c12 separator certificates for every hard
closed-disjointness slot, with margin TWO rather than one. Each certificate
satisfies u.a,u.b<=t-2 and u.c,u.d>=t+2. Point-side slots treat the point as
a repeated-endpoint segment. Such rational certificates exist by c12's
rational-certificate argument followed by multiplication by two. A certificate
must be supplied or verified; no unbounded separator search is prescribed.

Let x0 be only the free GEOMETRIC coordinates: d_geom=2m+2 max(n-2,0).
All bits, fixed anchors, and separator coefficients stay constant below.

Claim C16.1 (candidate): these data determine a finite list of rational
degree-at-most-two polynomials f_j with f_j(x0)>0, and an explicit rational
epsilon>0, such that every free-coordinate assignment within epsilon in
supremum norm still satisfies the sparse formula with the same bits.
A finite rational grid then gives a GP-ALL representation with exactly
m distinct nonstraight corners, preserving the original graph and anchors.

The claim is a witness-dependent extraction, not a graph-only precision
bound, a method of finding an initial witness, or a trusted verification.

## 2. Positive guards without assuming every determinant is nonzero

Choose the following strict polynomial guards, once, at the given witness.

(a) Every combined pair squared distance, and the current sign times the
signed double polygon area.

(b) At each adjacent triple, if its orientation is nonzero choose its sign
times that orientation. If its orientation is zero, choose the negative
of (a-b).(c-b), which is positive by the sparse adjacent guard. Thus a
straight subdivision is allowed initially; the selected OR branch remains
true under the later perturbation.

(c) For each hard disjointness slot with its fixed margin-two separator,
include t-u.a-1 and t-u.b-1 on the first segment, and u.c-t-1 and
u.d-t-1 on the second. All are at least one at x0. Keeping them positive
implies the margin-one certificate, and hence closed disjointness.
Duplicates in point slots can be removed but need not be.

(d) Preserve the sign of every q_ax-p_ix generic-ray difference.

(e) For each nonedge, choose ONE side with a Proper crossing, and preserve
the signs of its four orientation determinants. They are nonzero and the
two opposite-sign products remain negative. Other nonedge-side contacts
need not be preserved.

(f) For each ray-side pair put A=p_x-a_x, B=p_x-b_x, D=a_x-b_x,
T=orient(p,a,b). A and B are nonzero by (d). If A*B>0, no additional
guard is needed: the ray test remains false regardless of T or D.
If A*B<0, then D=B-A is nonzero. Moreover T is nonzero: T=0 together
with strict x-straddling would put p strictly between a and b on their
line, violating the retained point-boundary exclusion. In this case
preserve the signs of T and D. The truth of T*D>0 is then unchanged.

Each preserved nonzero sign is encoded as its sign (+1 or -1) times the
polynomial being positive. All listed coefficients are rational because
the anchors and separator coefficients are fixed rationals. Degrees are
at most two. No cubic product of orientations is needed in this list.

The crossing-bit and XOR equations need no positive guards: all their
variables have been fixed at their satisfying 0/1 values. In particular,
we do not perturb auxiliary bits and then hope their equalities survive.

## 3. Why these guards imply the full sparse predicate

Pairs stay distinct by (a). Area, adjacent guards and closed nonadjacent
side avoidance remain valid by (a)--(c), so the polygon remains simple.
Every graph point remains off the boundary by its point-side separators.
All edge-versus-side closed avoidances also remain true.

By (d) and the exhaustive cases in (f), EVERY RayHit truth value is fixed.
Thus the existing crossing-bit linkage, initial parity, XOR recurrence and
final exterior parity are unchanged. The points therefore remain exterior
under the c01 parity semantics, not merely off the boundary. Every nonedge
keeps a selected strict crossing by (e). These statements cover every c11
clause. In particular, segment containment is still excluded by exterior
parity; separator certificates alone would not exclude it.

This proof permits determinants that vanish in irrelevant nonstraddling
ray cases and initially collinear adjacent corners. Requiring all such
determinants to be nonzero at x0 would assume the desired GP conclusion.

## 4. Explicit polynomial variation bound

Expand each selected polynomial into a finite monomial sum
f_j(x)=sum_alpha c_(j,alpha) x^alpha. Coefficients and exponents are exact.
Choose rational R>=1+||x0||_infinity and define

    L_j = sum_(|alpha|>=1) |c_(j,alpha)| |alpha| R^(|alpha|-1);
    Lambda = max(1, all L_j);
    eta = min_j f_j(x0);
    epsilon = min(1, eta/(2 Lambda)).

The list is finite and nonempty; eta is a positive rational. No numerical
tolerance or unstated lower bound replaces these exact values.

For x,y in [-R,R]^d and h=||x-y||_infinity, the telescoping expansion of a
degree-k monomial as a product of k coordinate factors gives

    |x^alpha-y^alpha| <= |alpha| R^(|alpha|-1) h.

Summing coefficient-weighted bounds proves |f_j(x)-f_j(y)|<=L_j h.
If ||x-x0||_infinity<=epsilon, then x is in the box since epsilon<=1, and

    f_j(x) >= f_j(x0)-L_j epsilon >= eta/2 > 0.

Consequently every perturbation in this explicit closed coordinate box
preserves S with the fixed bits and separator certificates. The radius is
conservative and depends on the supplied witness and certificates. In
particular it may be arbitrarily small. The formula does not give a
uniform decimal precision or an NP certificate-length bound.

## 5. Finite rational grid that restores GP-ALL

Let N=n+m be the total number of graph and polygon points. Keep the
k0=min(n,2) anchors fixed and list the other N-k0 points in any fixed order.
Put M=C(N,2)+1. For a free point with original rational coordinates (a,b),
use the M by M Cartesian grid

    (a-epsilon/2 + epsilon*j/(M+1),
     b-epsilon/2 + epsilon*l/(M+1)),  1<=j,l<=M.

Every candidate is rational and differs coordinatewise from the original
point by strictly less than epsilon/2. Start with the fixed anchors; when
k points have already been chosen, exclude every line through two of them
and, for each earlier point, its vertical line. There are at most

    L_k=C(k,2)+k <= C(N,2)=M-1

lines. Each line contains at most M grid points: for a nonvertical line
there is at most one for each x-column, and a vertical line covers at most
one column. The union therefore covers at most L_k*M<M^2 grid points.
At least one candidate remains. Choose the first in lexicographic order.

The vertical exclusions also forbid equality with any earlier point,
including at the first stages when there are fewer than two earlier points.
Every final triple has a last-chosen point, unless it consists entirely of
anchors, impossible with at most two anchors. That last point avoided the
line through the other two. Hence the complete point set is GP-ALL.

All simultaneously chosen coordinates remain in the certified epsilon box,
so the entire sparse formula and fixed bits are preserved by Sections 2--4.
GP-ALL excludes straight polygon triples, giving exactly m genuine corners.
The grid search itself has a finite deterministic upper bound of
(N-k0)*M^2*(M-1) line-membership tests, with possible early exits.
This is a symbolic worst-case count of exact tests, not observed runtime.

Coordinate denominator sizes still depend on the original rational center
and epsilon. The number M alone does not bound coordinate bits independently
of the witness. No procedure for acquiring a rational initial sparse witness
or its verified margin certificates is claimed by this extraction.

## 6. Direct rational repair of the C15 diagnostic polygon

A small explicit example avoids needing to evaluate the general radius.
Take K2 with the fixed anchors. For rational 0<h<=1/4 use the polygon

    q0=(-1,1), q1=(1/2,1+h), q2=(2,1), q3=(3/2,3).

At h=0 this is the c15 raw sparse witness. In addition to q0,q1,q2,
the triple p1,q1,q3 is collinear there. Moving q1 upward removes BOTH.
Let the ordered combined list be p1,p2,q0,q1,q2,q3, with indices 0..5.
The twenty increasing-triple orientations are:

012:1; 013:1+h; 014:1; 015:3;
023:-3/2-h; 024:-3; 025:-9/2;
034:-3/2-2h; 035:-3h/2; 045:9/2;
123:-3/2-2h; 124:-3; 125:-13/2;
134:-3/2-h; 135:-2-h/2; 145:5/2;
234:-3h; 235:3-5h/2; 245:6; 345:3-h/2.

All are nonzero throughout the stated interval. The first nonadjacent
side pair q0q1 and q2q3 has disjoint x ranges. For the other pair q1q2
and q3q0, the endpoints q1 and q2 lie strictly on the same side of the
line q3q0: the corresponding orientations are 3-5h/2 and 6. Thus there
is no proper or closed contact between those sides. Adjacent sides meet
only at their endpoints by nonzero corner orientations. The signed double
area is 6-3h>0.

All polygon points have y>=1, so both anchors and their segment are exterior
and the graph edge is visible. Every qx differs from 0 and 1. Upward-ray
crossing rows remain (1,0,0,1) and (0,1,0,1), with exactly the c15 even
prefixes. At h=1/4 all coordinates are explicit rationals and the middle
corner is (1/2,5/4). This is an exact GP-ALL witness for this diagnostic
graph, not a general planar one-obstacle representation or a solver result.

## 7. Assumption attacks

- A contact-only nonedge need not survive arbitrarily small perturbations;
  the selected Proper side in (e) is essential to this proof.
- Omitting the forward-ray sign can keep even full-line parity for interior
  points. Section 2(f) preserves the actual half-ray predicate.
- Rounding the original parity bits breaks their polynomial equalities.
  They are fixed throughout; only geometric coordinates vary.
- Claiming the entire lifted set is open is incorrect: unit-margin separator
  constraints can be saturated, and sign/Boolean equations are lower-dimensional.
  We use supplied margin-two certificates and a fixed-bit coordinate box.
- Three fixed collinear anchors would prevent a GP result. The c04 gauge
  fixes at most two; the line-avoidance induction uses that hypothesis.
- Choosing M at most the number of forbidden lines gives no counting
  guarantee. The strict M>L_k inequality, not generic language alone,
  supplies the finite-grid existence argument.
- Adding a uniform lower bound on eta or a coefficient cap is unsupported.
  Small geometric gaps can require large separators and tiny epsilon.

## 8. Evidence boundary and next slice

This proof and the determinant table are hand-derived candidate mathematics.
No coefficient expansion program, grid search, geometric evaluator, solver or
proof assistant was executed. Local UTF-8/hash bookkeeping and remote transport
checks are not mathematical replay. The c15 executable write limitation remains
recorded; this artifact does not attempt to upload that blocked program.

The new deliverable is an explicit margin certificate and finite witness
extraction theorem, strengthening the qualitative c07 openness step. A verifier
must separately replay positive-guard selection, the ray zero-case argument,
the monomial variation bound, the finite line-grid count and the twenty
determinants. General correctness is not inferred from the repaired K2 example.

Source dependencies: c07 sparse GP candidate, c11 predicate contract, c12
segment certificates and c15 diagnostic fixtures at the declared base.
No outside theorem is substituted for the displayed derivations.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
next_action: freeze a verifier-facing coverage contract for margin certificates
and GP witnesses, separating coordinate truth from compiler and source-faithfulness.
