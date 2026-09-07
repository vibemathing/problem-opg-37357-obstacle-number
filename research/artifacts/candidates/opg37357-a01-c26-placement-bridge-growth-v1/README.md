# C26: the realized-placement to X4-CNF bridge, clause by clause

Candidate: candidate:opg37357-a01-c26-placement-cnf-bridge-v1
Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Primary owner: math-proof
Repository: vibemathing/problem-opg-37357-obstacle-number
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Base: c299659f0c7f505a1e9739e6d8329fbde48c30ff
Issue: #3

## 1. Frozen claim and what this packet closes only at draft level

Let G=X4, with N=0, S=1, a_i=2+i, b_i=6+i, i modulo 4.
Edges are N a_i, S b_i, a_i a_(i+1), b_i b_(i+1), a_i b_i,
a_(i+1) b_i. There are ten vertices, 24 edges and 21 nonedges.
The input placement is arbitrary injective REAL coordinates, not a sampled
layout, not a plane drawing, and not necessarily in general position.
Let K be all graph points and CLOSED graph-edge segments. An obstacle here
is a nonempty connected subset of R^2 minus K, hitting every nonedge.
It need not be bounded, closed, open, polygonal or path connected itself.

Candidate bridge theorem: existence of such an obstacle at ANY placement
implies satisfiability of the EXACT C22 CNF with SHA-256

de54d35f78d3c7d84e24651e5ce6f82c9ebe6d78bc7bd2deb66aa591e6ea276c.

For a realized C25 Dstar signature, the same implication uses its W signs
to obtain orientation bits; it does not assume that arbitrary accepted sign
tables are realizable. The signature decoder is neither invoked at n=10
(outside C25's executable cap) nor used to remove this premise.

This packet supplies a complete natural-language bridge and an executable
origin for EACH of the 69,332 clauses. It does not resubmit C22, rerun its
old RUP proof, or produce a trusted mathematical receipt. Given the separately
frozen C22 propositional contradiction, this bridge gives the all-placement
X4 lower-bound candidate. The prior-art attribution and trusted acceptance
of the whole chain remain separate. Q2's uniform integer is NOT proved.

The bridge is not a sufficiency statement: SAT of necessary clauses need
not give coordinates or an obstacle. This direction matters also for the
h-color extension in growth.md.

## 2. Arbitrary coordinates: normal-form lemma with quantified margins

K is compact and closed. F=R^2 minus K is open. A component U of F is open:
a sufficiently small connected ball in F around any of its points belongs
to U. It is polygonally path connected: the points reachable by finite
polygonal paths from one point, and their relative complement, are open
in U, using those balls. Connectedness then gives all of U.

A connected nonempty obstacle O is contained in one component U. Every
nonedge hit is a strict segment-interior point, since endpoints belong to K.
Choose one hit z_s=(1-t_s)p_i+t_s p_j with 0<t_s<1 per nonedge. A free ball
around z_s gives a nonempty interval of parameters in U even if the original
obstacle only touched the nonedge. Join finitely many hits in U by finitely
many polygonal paths. Their union T is nonempty, compact and path connected,
avoids K, and has positive distance d from K.

Set 0<epsilon<d/3. The CLOSED epsilon-neighborhood O' of T is bounded,
compact and path connected. It avoids K and contains B(z_s,epsilon) for
all selected hits. Keep O' fixed. If every graph point moves by less than
eta<min(epsilon/2,(d-epsilon)/2), then every point on each graph edge moves
by at most eta using the same interpolation parameter. Graph edges stay
disjoint from O'. Each moved hit (1-t_s)p'_i+t_s p'_j is still inside O'.
Shrink eta further below one quarter of the minimum pairwise graph-point
distance, preserving injectivity.

Within this nonempty coordinate box choose graph points in GP (no three
collinear), successively avoiding finitely many lines. For the stronger
Dstar used by C25 also avoid vertical pair lines and parallel distinct pair
lines. These are zero sets of finitely many NONZERO coordinate polynomials;
the product cannot vanish on an open box. Shared-vertex pair-line determinants
are vertex-triple determinants; disjoint pairs can be chosen nonparallel,
so no forbidden polynomial is identically zero. Rational points are also
available in the resulting nonempty open region. No bit-size bound follows.

The direction is: hypothetical representation at p -> hypothetical robust
representation at SOME p' -> CNF assignment. We are NOT projecting the signs
of an arbitrary degenerate p directly to Boolean orientations. No claim that
tau(G,p) stays unchanged under every perturbation is used. Graph-edge crossings
are retained as allowed. C19's thin-disk lemma and its corner bound are not
premises: O' need not be a simple polygon.

For k=0 a remote harmless obstacle works; for k=1 one witness suffices. X4
has k=21, so the empty-target caveat never shortcuts this bridge. Multiple
obstacles admit the same regularization with finitely many assigned hits
per obstacle and a minimum over their finitely many positive margins.

## 3. Boolean variables and the C25 projection

Write D(a,b,c)=det(p_b-p_a,p_c-p_a). For increasing triples use variables
x_abc=(D(a,b,c)>0), numbered lexicographically 1,...,120. For other orders,
the literal is negated exactly for an odd permutation. GP supplies D!=0,
so this is exact complementation, not an unsupported interpretation of zero.

For each ordered pair ab,cd of distinct lexicographic nonedges introduce one
side variable s_ab,cd, numbered 121,...,540. Distinct nonedges may share one
endpoint; they may not coincide. The side s=true means that every relevant
cd-key a--b path has some internal vertex strictly left of directed ab.
There is a SEPARATE side for every ordered pair, not a global side for ab.

For increasing i<j<k, with C25's unnormalized directed pair lines L_ij and
L_ik, their two-direction determinant satisfies

    W_(ij),(ik) = D(i,j,k).

Thus a REALIZABLE Dstar signature supplies all 120 orientation bits using W.
For nonincreasing triples use the same permutation parity as the compiler.
Delta signs, including their forced zeros at graph vertices, are unnecessary
for these NECESSARY clauses. This does not say W signs determine the full
free-space incidence: C24/C25 already give a counterexample to that stronger
assertion. Nor does it say a locally consistent abstract W-table is realizable.

## 4. Four-point clauses

For each ordered distinct tuple (a,b,c,d), exact expansion yields

    D(b,c,d)=D(a,b,c)+D(a,c,d)+D(a,d,b).

If the three determinants on the right are positive, the left is positive.
The implication is precisely

    not x_abc OR not x_acd OR not x_adb OR x_bcd.       [4]

If its premise is false, the corresponding negated literal already satisfies
[4]. This covers all real GP placements, all permutations and sign reversals.
There are 420 distinct nontautological canonical clauses after the exact
compiler's parity substitution and duplicate removal. These are final row
counts, not raw pre-canonical counts from the paper.

## 5. Five-point clauses

For each ordered distinct (a,b,c,d,e), translating a to the origin and
expanding the 2-by-2 determinants gives

    D(a,b,d) D(a,c,e)
      = D(a,b,c) D(a,d,e)+D(a,b,e) D(a,c,d).

When D(a,b,c),D(a,c,d),D(a,d,e),D(a,b,e) are positive, the right side is
positive. The two nonzero factors on the left therefore have the SAME sign.
The conjunction expressing their equivalence under this premise is

    A OR x_abd OR not x_ace;
    A OR not x_abd OR x_ace,                            [5]

where A is the disjunction of the four negated premise literals. If any
premise determinant is negative, A is true. Thus BOTH clauses hold, in
all orders, with no assumption of realizability completeness of these rules.
Canonicalization leaves 20,160 clauses of this family.

## 6. The key-path separation lemma, including self-crossing graph paths

A cd-key a--b graph path has all its vertices in one CLOSED halfplane of
the line cd. Convexity makes this equivalent to the whole polygonal walk
being there. Delete c,d from its list of orientation tests, since their
determinants are identically zero. All remaining determinants are nonzero
in GP. Their list C is NONEMPTY: at least one of a,b is not c or d.
The path is key exactly when all literals in C have the same truth value.

The internal-vertex list J relative to ab is also NONEMPTY: ab is a nonedge,
so a graph path from a to b uses at least two edges. Every internal vertex
is strictly on one side of ab. If no side can serve all key paths, there is
one key path all of whose internal vertices are left of ab and another
all of whose internal vertices are right of ab. Call them P+ and P-.
Their interiors as geometric walks lie in the respective OPEN halfplanes:
segments between two strict same-side vertices stay strict, and an endpoint
segment is strict except at a or b.

A graph-theoretically simple path need not be geometrically simple. Subdivide
the finitely many segments at all crossing/contact points and erase loops
in the resulting finite connected graph. Distinct graph-edge segments cannot
overlap on a nontrivial interval in GP, since that would force three graph
vertices collinear; adjacent ones meet only at their common endpoint. Thus
subdivision is finite even with many edges concurrent at one crossing.
Take a simple a--b graph path in this subdivision. Its geometric realization
is a simple polygonal arc made solely of pieces of the original graph edges.
It stays in the prescribed open halfplane except at its endpoints. Apply
this separately to P+ and P-, obtaining arcs A+ and A-.

The arcs share exactly a,b. A+ together with [a,b] is a simple polygonal
Jordan curve enclosing a disk above ab. Its bounded region cannot enter the
other halfplane: every point there has a ray to infinity avoiding the curve.
The same statement holds below ab for A-. Near any point of (a,b), compact
separation from the non-base sides provides a small ball in which the two
disks occupy the two opposite half-balls. Splicing the disks along [a,b]
therefore gives a Jordan disk with boundary A+ union A-, and ALL of (a,b)
strictly inside it. This is a planar Jordan argument, not an assumption that
the original graph drawing is crossing-free.

Both key paths lie in the SAME closed halfplane of cd, because they share
an endpoint in {a,b} minus {c,d}, whose sign relative to cd is strict and
fixed. Their Jordan curve and its bounded region lie in that halfplane.
For the latter assertion use the same escaping-ray argument for points in
the opposite open halfplane. The bounded region, being open, contains no
point of the boundary line cd. The open segment (c,d) also misses the curve:
a segment between graph vertices in this closed halfplane meets line cd
only at a graph endpoint on the line or lies along it. GP permits only c,d
as such graph endpoints; a positive interval along the line would require
the graph edge cd, which is absent. Intersections introduced by subdivision
cannot change this fact. A shared endpoint a=c causes only an allowed
boundary contact at c, not in (c,d).

Thus (a,b) is inside the Jordan curve and (c,d) is outside it. Any connected
obstacle avoiding graph-edge pieces avoids the curve and must lie in one
component of its complement. It cannot hit both segments. Contradiction.
Therefore at least one side serves all cd-key a--b paths.

The same lemma is PAIR-LOCAL: even in a many-obstacle drawing, it applies
whenever ab and cd are hit by the SAME connected obstacle. It does not require
that that obstacle also hit every other nonedge. This fact drives growth.md.

## 7. Four clauses per retained path and exact existential elimination

For an ordered pair ab,cd and a retained path P write C=(x_cdv: v in P,
v not in {c,d}) and J=(x_abv: v internal to P). The four raw clauses are

    OR C     OR not s OR OR J;
    OR C     OR s     OR OR not J;
    OR not C OR not s OR OR J;
    OR not C OR s     OR OR not J.                     [K]

If C has both signs, OR C and OR not C are both true, so every clause holds.
If C is constant, one of those two disjunctions is false. The other pair of
clauses then says: s=true requires a positive internal vertex, and s=false
requires a negative internal vertex. The side lemma supplies ONE s for ALL
retained key paths. It is not chosen anew for each path.

For a constructive selection from the retained set: an all-positive key
path forces s=true, an all-negative key path forces s=false, and a key path
with both internal signs imposes no restriction. The separation lemma says
both force types cannot occur under a common obstacle. Choose the forced
value if present, otherwise choose false. This also handles no retained key
path. The code project returns a pair of conflicting paths if both types
occur at the supplied fixed drawing; that diagnostic is not an all-placement
lower bound on its own.

The primary paper uses an auxiliary key bit z per path. Let A=OR C,
B=OR not C, U=(not s OR OR J), V=(s OR OR not J). Its four clauses are
(A OR z),(B OR z),(not z OR U),(not z OR V). Existentially eliminating z
is EXACTLY (A OR U),(A OR V),(B OR U),(B OR V): if A and B are true take
z=false; otherwise z must be true and U,V must hold. This proves the signed
four-clause layout without keeping z. The finite Boolean audit exhausts all
1<=|C|<=5 and 1<=|J|<=3, both side values, without assuming independence of
geometrically repeated literals; checking all Boolean patterns is stronger.

Only simple graph paths with at most FOUR edges are retained. The universal
side lemma applies to all of them. Omitting longer-path constraints is a
relaxation, so UNSAT of the retained formula remains sufficient for an
obstruction; completeness of the path truncation is never asserted. C26 uses
bounded-depth DFS, while the byte-pinned C22 compiler uses layered expansion.
Both enumerate all labels, not merely increasing paths. There are 804 retained
paths and 420 side variables. Final key clauses number 48,752.

## 8. Complete row attribution and finite executable checks

clause_bridge.py does not import C22's compiler. It constructs each raw
clause with its ordered-tuple or (side variable, exact path, mode) origin,
canonicalizes literal parity/order, drops tautologies and duplicates, and
retains the lexicographically first origin. No mathematical information is
lost: a tautology is true; duplicates are the same conjunct; signed literal
reordering does not change a disjunction.

controls.py separately imports the frozen C22 root_cnf ONLY as a comparison
oracle. It compares every clause, its order and variable count, verifies each
origin uses actual graph edges, simple paths and the correct endpoints, and
recomputes the complete DIMACS digest. All 69,332 rows match, split as
420+20,160+48,752, with 540 variables. No single row is merely assumed to
have arisen from a valid graph path. The generated attribution table has
69,332 rows, 1,530,158 bytes and SHA-256
666420da3374818cafa9fa8805acab65740c373e1fbb9ad3af01e5d12d4813f7.
It is a reproducible derived output, not a duplicate stored CNF/proof. Emit
it by --origins; it is not saved as an oversized single repository file.

New actual checks include all 5,040 four-point identities, all 30,240
five-point identities and 120 W projections on one ten-point rational set;
1,736 complete Boolean key-elimination cases (each also checks both color
guard values); four actual one-polygon fan controls whose FULL CNFs are
satisfied; four fixed X4 controls with explicit conflicting paths; a GP
self-crossing key-path fixture with an exact loop cut; and a GP shared-endpoint
fixture. The positive controls verify graph-edge avoidance and strict interior
nonedge midpoint blocking against every closed polygon side. These finite
checks do not quantify over every real placement; sections 2--7 supply the
candidate universal proof. The initial crossed fixture had an unwanted
collinear triple and failed its GP assertion. Only its auxiliary c,d points
were repaired, then the final source was rerun; the failed run is disclosed.

Run, from this directory and with existing C22 on the module search path:

    PYTHONPATH=../opg37357-a01-c22-root-hints-v1 python -B controls.py
    PYTHONPATH=../opg37357-a01-c22-root-hints-v1 python -B controls.py --origins

Apply externally 35 CPU seconds, 40 wall seconds, 512 MiB address-space,
one process and a 4 MiB output cap. All new sources are readable UTF-8.
The math modules have no file/network/process/credential/dynamic-code access;
the control entry only adds JSON or text stdout. Inputs n<=10 and retained
path length<=4 are explicit executable caps. The theorem is not limited to
rational coordinates. The full C22 RUP was NOT replayed in this round; its
unchanged candidate receipt and 1,827-line contradiction are separate frozen
dependencies, bound by the exact same CNF digest.

## 9. Faithfulness, dependencies and remaining gates

Layer T: C19 thin-tree disk/Jordan count B17. NOT a premise of this bridge.
Layer A: C20/C21 fixed arrangement and C25 realized-signature interpretation.
Only the open-free-component normal form and the exact W projection are used
here. No root conclusion follows from one C18 drawing or a decoder's unverified
realizability flag.
Layer P1: this universal implication + the separately frozen C22 contradiction
+ X4 planarity and canonical statement-faithfulness. Candidate-level proof
chain is reviewable, but there is no trusted closure receipt.
Layer P2: uniform h over all finite planar G. Addressed only by the growth
interfaces and the genuine obstruction to X4-copy-only amplification in
growth.md. No growing planar obstacle lower bound is claimed.

The primary paper defines obstacles as connected sets and gives the key-path
necessary conditions. The canonical contract uses the shorter phrase polygonal
obstacles. Interpreting each polygonal obstacle as connected makes its class
no larger than the class excluded here. If disconnected unions were counted
as one obstacle, this bridge would not cover that changed meaning. Positive
degree of X4 forces graph points outside obstacles even if that requirement
were implicit; its absence of true twins also excludes coincident vertices
as detailed in C22. This packet leaves the semantic admission check explicit.

Primary provenance: Berman et al., Graphs with Obstacle Number Greater than
One, JGAA 21(6), 1107--1119 (2017), DOI 10.7155/jgaa.00452, Lemmas 1--3,
Observation 2, Proposition 3. Retrieved 2026-09-07. Source uses clockwise
bits; C22/C26 consistently use counterclockwise, with all tuples included.
https://jgaa.info/index.php/jgaa/article/download/paper452/2511/2318
The primary statement is necessary, not sufficient; the auxiliary-key
elimination above is an exact comparison. No novelty claim is made for X4.

Fresh research/verifiers.json still has fixture policies, no compatible
registered consumer for the universal geometric implication and colored
extension. A verifier request binds these frozen files and C22 inputs.
No EvidenceLink, Result, Solution, registry, workflow or protected record is
edited. User authorization to continue does not grant evidence_signing.

Reasoning audit: assumptions and negation frozen; dependencies P1/P2/T/A
separate; witnesses/identity expansions explicit; counterexamples target only
stronger shortcuts; path depth and finite graph sizes bound all loops;
GP/reflection/zero-event/small-k cases are separated; no probability or
unjustified compactness of placement space is used. Computation is finite.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: test guarded h=2 key-path constraints across different rigid blocks,
not only X4-copy nonmonochromatic demands; request the separate trusted bridge
and C22 trace acceptance. Root remains NONTERMINAL_CHECKPOINT.
