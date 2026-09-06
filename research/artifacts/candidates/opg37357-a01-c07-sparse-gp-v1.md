# Sparse general-position encoding by robust crossing witnesses

Candidate: candidate:opg37357-a01-c07-sparse-gp-v1
Verdict: candidate_only
Owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: 853be12e7783f3b4843e98416a9cbbd29f2d41bf

## 1. Frozen bounded question and new formula

Let N_(G,m) denote c04/c05's normalized exact-m GP-ALL sentence for one filled closed bounded simple polygon. Graph vertices are exterior; touching the obstacle blocks a pair. Graph-edge crossings are not forbidden. The first graph point is fixed to (0,0), and, when n>=2, the second to (1,0); the ray is vertical. No third graph point is fixed. All other coordinates are free. Planarity is an input promise, not a layout constraint.

For n>=1 and m>=3 define S_(G,m) by making precisely these three changes to N:

1. Remove ALL combined-triple noncollinearity conjuncts. Keep every combined pair's distinctness.
2. For each nonedge replace OR_a Meet(p_i,p_j,q_a,q_(a+1)) by OR_a Proper(p_i,p_j,q_a,q_(a+1)).
3. For each cyclic polygon corner explicitly add

       orient(q_(a-1),q_a,q_(a+1)) != 0
         OR dot(q_(a-1)-q_a,q_(a+1)-q_a)<0.

Everything else is retained: nonadjacent polygon sides cannot even touch; signed area is nonzero; graph points are not on polygon sides; q_(a,x)!=p_(i,x); crossing bits exactly encode the forward vertical ray; prefix parity uses XOR with first and final value zero; every EDGE avoids closed Meet with EVERY polygon side. In particular, no proper-only avoidance test is substituted for an edge or for polygon simplicity.

For m<3 use false; for n=0,m>=3 use true, as in c05. S uses only the same real coordinate and real Boolean variables as N. This artifact changes no previous exporter file.

Claim S1 (candidate): S_(G,m) and N_(G,m) are equisatisfiable. Consequently, conditional on c01/c04's candidate proofs, S exactly expresses EXISTENCE of a GP-ALL representation with at most m corners. An arbitrary satisfying coordinate assignment of S need not itself be GP-ALL. The equivalence is existence-level, not equality of witness sets.

## 2. From N to S

In N, each graph-pair/polygon-side call has four distinct endpoints and no collinear triple. The four endpoint-on-segment cases of Meet are therefore impossible, and Meet equals Proper on those calls. Every nonedge thus has a proper crossing witness. Each adjacent polygon triple is noncollinear, so the newly added adjacent guard holds. Deleting the other triple guards cannot invalidate the assignment. The same coordinates and auxiliary bits satisfy S.

## 3. From S to an open coordinate neighborhood

Take a satisfying assignment of S. By the c01 polygon conditions its ordered sides form a simple polygon: the adjacent guard excludes backtracking while allowing straight subdivision corners; nonadjacent closed sides are disjoint. By c01's explicit boundary exclusion, generic-ray and parity conditions, all graph points are exterior. Nonedges cross a side properly and therefore meet the obstacle; edges avoid the entire obstacle because their exterior-to-exterior segment misses its boundary. These conclusions need no combined-GP premise.

The crossing equations force each c to 0 or 1. Starting at b_0=0, the recurrence b_next=b+c-2bc forces each prefix b to 0 or 1 as well. FIX ALL THESE BITS at their satisfying values. Only continuous coordinates, other than the fixed anchors, will be varied. The full feasible set including the bit variables is not being claimed open.

Claim S2 (candidate): in this fixed-bit, fixed-anchor coordinate space, every satisfying assignment of S has an open neighborhood consisting of satisfying assignments. The following arguments cover every retained constraint.

(a) Distinctness, nonzero area, and the adjacent guard are open conditions. The latter is a union of the open sets orient!=0 and dot<0. A straight-through corner with dot<0 therefore also has an allowed neighborhood.

(b) Disjoint CLOSED segments have positive distance by compactness. If each endpoint moves by less than epsilon, each point with a fixed interpolation parameter moves by less than epsilon. The two moved segments stay at distance at least delta-2*epsilon, where delta is their original separation. Choosing epsilon<delta/2 preserves disjointness. This covers nonadjacent polygon sides and edge-versus-polygon-side constraints, including initially collinear but disjoint segments. The point-versus-side version covers boundary exclusion. No assumption that every relevant orientation is nonzero is needed here.

(c) For each nonedge select one proper crossing side at the given assignment. Its two strict straddling products remain negative under sufficiently small changes. Thus that chosen crossing, and hence the entire nonedge disjunction, persists. This is the step for which mere contact is insufficient.

(d) For a graph point z and a directed polygon side a->b, put

       A=z_x-a_x, B=z_x-b_x, D=a_x-b_x, T=orient(z,a,b).

The explicit generic-ray guards give A!=0 and B!=0. If A*B>0, the ray predicate is false throughout a small neighborhood, whatever T or D may do. If A*B<0, the side endpoints have different x coordinates, so D!=0. In that case T cannot vanish: a collinear z whose x coordinate lies strictly between a_x and b_x would lie on the side, contrary to boundary exclusion. Thus T*D has a nonzero sign and its truth is stable. This proves local constancy of RayHit without GP-ALL. A vertical side is harmless: then A=B!=0 and it is in the first case.

(e) Since each ray truth value is fixed locally, its linkage to the already fixed crossing bit remains true. All real-bit and prefix equations remain unchanged. The parity endpoints remain zero. These are equalities in the fixed bits, not open constraints in freely varying bits.

There are finitely many pairs, corners, nonedges and ray tests. Intersect their neighborhoods and take a sufficiently small product of open coordinate boxes contained in the intersection. All constraints of S are then preserved. The number of polygon entries and all graph labels stay unchanged.

## 4. Restoring GP-ALL within the same m and gauge

Starting from the product neighborhood in S2, choose the free points sequentially. Begin with the one or two fixed anchors, which are distinct rational points. At each step select the next point in its assigned open box while avoiding every line through two previously selected points. A finite union of lines cannot cover a nonempty open box. Moreover the complement is open and contains rational points, so the selected point may be rational.

This procedure produces a combined point set with no three collinear: in any triple, its last-selected point was chosen off the line through the other two. Pairwise distinctness and all other S constraints already hold throughout the neighborhood. A box may also be chosen inside the small Euclidean disk required by the clearance proof. There is no restriction from future fixed points because the only fixed points were the initial at-most-two anchors.

The resulting coordinates satisfy every deleted triple condition and still satisfy S. Proper implies Meet for every nonedge, so they satisfy N. The polygon has exactly the same m entries; GP-ALL makes all its corners nonstraight. This proves the S-to-N direction of S1, conditional on the explicitly referenced polygon/parity facts. It also supplies rational normalized witnesses, but gives neither a uniform coordinate precision nor a polynomial bit-size bound.

No regularization of contact-only blockers, no change in corner budget and no unrestricted cutoff is used in this argument. The c02 offset construction and c03 global cutoff are not dependencies of S1.

## 5. Constraint-count reduction

For n>=1,m>=3, the number of separate assert commands in an S exporter following the c05 block layout would be

    C(n+m,2) + m(m-3)/2 + m + 1 + 5nm + 2n + C(n,2).

This replaces C(n+m,3) triple assertions by m adjacent guards. Declarations are unchanged and polynomial degree remains at most four. The expanded text also contains the visibility disjunctions, so its size is O((n+m)^2+n^2*m+nm), not merely the number of assert commands. All bounds concern numeric n,m, not their succinct binary encoding.

Hand-derived syntactic counts, not executed output or a performance benchmark:

| n | m | old N assertions | proposed S assertions |
|---|---|---|---|
| 1 | 3 | 28 | 27 |
| 2 | 3 | 56 | 49 |
| 2 | 4 | 83 | 67 |
| 3 | 3 | 90 | 73 |
| 24 | 64 | 123521 | 13849 |

The final row no longer exceeds the c05 default 60000-assertion cap on this count alone. It does not certify the separate byte cap, execution time, solver acceptance or satisfiability. The existing c05 source still emits N; an S exporter must be a new candidate with its own tests and digest.

## 6. Adversarial audit of the openness argument

A. Contact-only nonedges do not give S2. Let G have two nonadjacent anchors (0,0),(1,0), and use the triangle

    q_0=(1/2,0), q_1=(1/2,1), q_2=(-1/2,1).

All graph points are exterior, every vertical-ray guard holds, the polygon is simple, and the pair segment touches only q_0. A variant retaining closed Meet for nonedges accepts this nongeneric coordinate witness. The first anchor's crossing bits are (0,1,1) with prefixes (0,0,1,0); the second anchor's crossing and prefix bits are all zero. Raising only q_0's y coordinate by any sufficiently small positive epsilon preserves the other constraints and these bits but makes the nonedge segment disjoint from the obstacle. Hence no whole open coordinate neighborhood at the original witness preserves the contact-only formula. The strict Proper requirement rejects that witness from S. This attacks the local-openness premise, not the existence-equivalence of some other regularized encoding.

B. Bit variables cannot be perturbed along with coordinates. At a c=0 solution of c(c-1)=0, arbitrarily small nonzero c values fail the Boolean equation. The proof fixes all bits before taking a neighborhood.

C. The adjacent guard is retained as an explicit, possibly redundant simplicity condition; no irredundancy claim is made. For m>=4, adjacent overlap puts the shorter side's nonshared endpoint on the longer side. Its other incident side is nonadjacent to that longer side, violating closed nonintersection. For m=3, the nonzero-area guard excludes collinearity. Retaining the guard makes the open-condition argument direct. In contrast, replacing closed avoidance by proper-only avoidance for graph edges would reintroduce c01's tangency fake witnesses.

D. The ray direction factor cannot be omitted. c06 already gives false interior witnesses in GP-ALL if full-line crossings or the wrong denominator sign are used. A density argument cannot repair an incorrect ray predicate.

E. Three prescribed collinear anchors would prevent any GP-ALL perturbation. Only the c04 one/two-anchor gauge is claimed here. Arbitrary fixed graph coordinates are outside S1's input contract.

## Sources, replay, and continuation

Repository sources at the declared base: c01 closed-contact encoding, c04 normal form, c05 exporter and export contract, and c06 ray family. All new deductions above are candidate mathematical arguments from those definitions. No external theorem search hit is used to certify this equivalence, and no executable mathematical check was performed. Verification must replay polygon separation/parity, the compact-separation bound, finite-product neighborhood construction, rational line-avoidance, and the exact formula translation. Checking a few examples cannot establish S1.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
next_action: implement S in a separately frozen bounded exporter, retain closed-avoidance and ray guards, and add c06 and contact-only regression specifications. Do not alter earlier immutable packets or protected ledgers.
