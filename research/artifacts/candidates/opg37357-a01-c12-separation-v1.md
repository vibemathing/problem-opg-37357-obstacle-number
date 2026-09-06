# C12: exact closed-segment separation certificates

Candidate: candidate:opg37357-a01-c12-separation-v1
Verdict: candidate_only
Owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: 184e54aab93674fc1dee66fcdabeb91e9684e62f

## 1. Frozen local theorem

For any a,b,c,d in R^2, including a=b or c=d, let A=[a,b], B=[c,d]
be the nonempty CLOSED segments. Define Sep(a,b;c,d;u,t), where u in R^2
and t in R, by the conjunction

    u.a <= t-1,  u.b <= t-1,
    u.c >= t+1,  u.d >= t+1.                         (SEP)

Claim C12.1 (candidate):
A and B are disjoint if and only if there exist u,t satisfying (SEP).

No general-position assumption, positive segment length, fixed orientation,
unit normal, bounded coefficient or coordinate rescaling is part of this claim.
Each of the four constraints is quadratic or lower in endpoints,u,t.
The constants +/-1 normalize the CERTIFICATE, not the geometry or anchor gauge.

## 2. Soundness: endpoint inequalities exclude all contacts

For x=(1-s)a+s b with 0<=s<=1, linearity and the first two inequalities
give u.x<=t-1. Similarly each y in B satisfies u.y>=t+1. A common point
would give t+1<=t-1, impossible in the real ordered field. Consequently
proper crossing, endpoint touching, collinear overlap and identical points
are all rejected. The certificate itself forces u nonzero; a separate
normalization or nonzero predicate is unnecessary.

## 3. Completeness without a separating-hyperplane black box

Assume A and B disjoint. Their compact Cartesian product has a minimizing
pair (x,y) for squared Euclidean distance. Put w=y-x and delta=w.w>0.
The positivity uses disjointness and compactness, not just absence of a
proper crossing.

For any z in A and s in [0,1], minimality and convexity give

    ||w-s(z-x)||^2 - ||w||^2
      = -2s w.(z-x) + s^2 ||z-x||^2 >= 0.

If w.(z-x)>0, choosing a sufficiently small positive s<=1 contradicts
this inequality (if z=x the asserted strict positivity is already
impossible). Thus w.z<=w.x. Applying the same argument to the second
segment, with y+s(z-y), gives w.z>=w.y for every z in B.
This uses an elementary quadratic sign argument, not differentiation.

Let alpha=(w.x+w.y)/2. Since w.y-w.x=delta, define

    u=2w/delta,  t=2alpha/delta.

Then u.z<=t-1 on A and u.z>=t+1 on B, proving (SEP). Division is used
only in constructing a witness in the proof; the compiled constraints
contain no division. The argument includes point segments and parallel
or collinear disjoint segments without separate exceptional cases.

## 4. Rational and robust certificates

For fixed disjoint segments, first scale a unit-margin certificate by 2:
(2u,2t) has margin 2. Its four margin-1 inequalities then have positive
slack. Small perturbations of u,t preserve (SEP). Rational vectors and
thresholds exist in that open neighborhood, even when the endpoints
themselves are real. This is an existence statement with witness-dependent
precision, not a polynomial coordinate-bit bound.

Choosing the margin-2 certificate also gives an open coordinate-and-
certificate neighborhood satisfying all four margin-1 constraints.
An arbitrary feasible margin-1 certificate can saturate some inequalities;
not every point of the lifted feasible set is interior. This distinction
prevents incorrectly transferring c07's open-fiber statement to all
possible separator assignments.

## 5. Pointwise projection into the sparse bounded formula

Use the c07/c11 sparse formula S_(G,m), n>=1,m>=3, e=|E(G)|.
It has three classes of hard, conjunctively required disjointness:

    K=m(m-3)/2 nonadjacent polygon-side pairs;
    em edge-versus-polygon-side pairs;
    nm graph-point-versus-polygon-side pairs.

First distribute each edge clause NOT(OR_a Meet) into the equivalent
conjunction of NOT Meet. For each of these L=K+em+nm slots independently,
replace disjointness by (SEP) using a fresh triple (u_x,u_y,t).
For a point p off a side use a=b=p; the duplicated point inequality
may be emitted twice for a uniform template or once.

Retain ALL remaining clauses, including pair distinctness, area and
adjacent simplicity guards, generic-ray tests, exact ray-bit linkage,
XOR parity with exterior endpoints, and strict Proper nonedge witnesses.
Call the new formula T_(G,m)(X,W), with X the original coordinates and
bits and W all separator triples.

Claim C12.2 (candidate), pointwise in X:

    S_(G,m)(X) iff exists W, T_(G,m)(X,W).           (PROJECT)

Proof: one direction applies C12.1 soundness to each slot and reverses
De Morgan. For the other direction, apply completeness to every disjoint
slot and collect its independently named witnesses; finiteness suffices.
There is no alteration of the graph, m, anchors, existing bits, ray or
nonedge clauses. Thus (PROJECT) is equality of projected original witness
sets, unlike c07's separate existence-level restoration of GP-ALL.

The uniform template adds 3L real variables and 4L quadratic inequalities;
deduplicating the point slots gives 4(K+em)+3nm inequalities. These are
only the replacement blocks, not the total constraint count. Remaining
Boolean structure still exists. Neither the c11 exporter nor previous
candidate/packet bytes are changed by this proof proposal.

The finite existential witnesses can be placed at the outermost level
because these replacements occur in hard conjunctions and each witness
has a fresh name. Replacing a predicate under negation by an existential
certificate and then carelessly hoisting that quantifier is not the same
transformation. Negation of existence is universal, not existential.

## 6. Explicit attacks and exact certificate fixtures

All of the following are algebraic fixtures/expected values, not executed
solver or evaluator results.

A. Collinear separated segments:
a=(0,0), b=(1,0), c=(1+eps,0), d=(2+eps,0), eps>0.
The choice u=(2/eps,0), t=1+2/eps satisfies (SEP).
At eps=1/4 this is u=(8,0), t=9; the nearest projected endpoints are
8 and 10, with threshold 9. The same proof yields certificate choices
for any positive eps, however small.

B. A unit-normal restriction is NOT harmless at fixed margin.
For fixture A any certificate must have eps*u_x>=2, hence
||u||>=2/eps. Imposing ||u||=1 along with (SEP) excludes eps<2,
including eps=1/4. An arbitrary coefficient cap has the same defect
for sufficiently small eps. Scaling the certificate, rather than the
normalized graph coordinates, is the essential operation.

C. Remove the positive margin:
the weakened inequalities u.a,u.b<=t and u.c,u.d>=t admit u=0,t=0
for every pair. Even additionally requiring u nonzero does not repair
touching segments: [0,1] and [1,2] on the x axis pass u=(1,0),t=1.
The actual (SEP) rejects their shared endpoint.

D. Point segment:
A={(0,0)}, B=[(2,-1),(2,1)] has u=(1,0),t=1.
Identical point segments have no certificate, by the soundness
contradiction. Distinctness of endpoints within each segment must not
be added as an unjustified premise.

E. Polygon-exterior parity remains necessary:
the c06 negative-t triangle has both graph anchors inside and their
edge entirely inside. That edge and each boundary side are disjoint,
so each side-avoidance slot has a valid separator certificate. Replacing
the avoidance clauses by (SEP) cannot reject containment by itself.
The retained odd exterior-ray parity is the decisive rejection.

F. Do not reuse one separator for every side of a nonconvex polygon.
The theorem supplies a different triple for each required slot. A
single separator between the whole polygon and a segment is stronger
than disjointness for a nonconvex obstacle. For an exact counter-witness,
take the simple U polygon in cyclic order
(-2,-2),(2,-2),(2,2),(1,2),(1,-1),(-1,-1),(-1,2),(-2,2)
and segment [(-1/2,0),(1/2,0)] in its open notch. They are disjoint.
But (0,0) is both on the segment and a convex combination of the four
outer polygon corners. One functional putting every corner on one side
with positive gap from the segment would contradict linearity at (0,0).
Separate side certificates do not have this defect. Convexity of the
TWO SEGMENTS in C12.1 cannot be extended silently to a nonconvex region.

G. Saturated witnesses are not an open set:
for A={(0,0)}, B={(2,0)}, u=(1,0),t=1 is valid with both closest
constraints saturated. Decreasing u_x while holding t fixed fails.
The existence of a slackened replacement certificate is what is
claimed in Section 4, not openness at every lifted witness.

## 7. Sources, scope and replay obligations

This is a self-contained segment instance of strict convex separation;
no novelty is claimed. The proof above uses compactness of closed bounded
segments, convex interpolation, Euclidean squared distance and ordered
field arithmetic. Repository semantics are those of c01 closed contact,
c06 containment attacks, c07 sparse formula, and c11 quadratic exporter
at the declared base. No outside theorem statement is substituted for
the displayed proof.

No mathematical program, solver, proof assistant or verifier was run
for this candidate. Next verification must check the compact minimum
argument, the quadratic variation inequalities, simultaneous finite
existential substitution, and compiler occurrence polarity. Any later
execution needs its own frozen inputs, versions, limits and actual
outputs. GitHub transport checks do not supply this mathematical replay.

The root remains open. This certificate encoding does not provide a
corner cutoff, exclude one obstacle for a graph, construct two obstacles,
or resolve a universal planar obstacle bound.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
next_action: give a pointwise-correct sign/circuit lift from the remaining
finite Boolean polynomial formula to a conjunction of quadratic equations
and linear nonnegativity constraints, then audit a bounded compiler.
