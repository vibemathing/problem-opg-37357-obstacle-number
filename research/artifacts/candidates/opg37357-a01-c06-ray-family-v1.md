# A normalized ray-parity mutation family

Candidate: candidate:opg37357-a01-c06-ray-family-v1
Verdict: candidate_only
Owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: 939147c883291f4a323fed2bcef1fe56dcfb66e8

## 1. Frozen family and exactly what is tested

Fix the labeled graph G=K2, m=3, anchors p_1=(0,0), p_2=(1,0), and the vertical ray direction d=(0,1). For a real parameter -1<=t<=1 with t!=0, put

    q_0=(-1,t), q_1=(2,t), q_2=(3/2,3).

These are normalized inputs to the c04/c05 GP-ALL formula. We compare its correct ray predicate with two mutations: M1 counts the entire vertical line by deleting the forward-direction factor; M2 replaces T*D>0 with T>0, losing the denominator's sign. A third mutation M3 replaces XOR parity by ordinary addition. The admitted route is not being replaced by these mutations.

This is a candidate-level exact algebraic audit. The data file contains EXPECTED values derived below, not executed tests or a verifier receipt. A bad coordinate assignment for K2 is not a graph-level proof that K2 lacks some other valid representation.

## 2. All geometric guards remain nondegenerate

The ordered combined list is (p_1,p_2,q_0,q_1,q_2). Its ten triple orientations are:

| Triple | orient |
|---|---|
| p_1,p_2,q_0 | t |
| p_1,p_2,q_1 | t |
| p_1,p_2,q_2 | 3 |
| p_1,q_0,q_1 | -3t |
| p_1,q_0,q_2 | -3-3t/2 |
| p_1,q_1,q_2 | 6-3t/2 |
| p_2,q_0,q_1 | -3t |
| p_2,q_0,q_2 | -6-t/2 |
| p_2,q_1,q_2 | 3-t/2 |
| q_0,q_1,q_2 | 9-3t |

Every entry is nonzero on the stated parameter domain. The squared pair distances, in the corresponding lexicographic pair order, are

    1, 1+t^2, 4+t^2, 45/4,
    4+t^2, 1+t^2, 37/4,
    9, 25/4+(3-t)^2, 1/4+(3-t)^2.

They are positive. The triangle's signed double area is 9-3t>0. No nonadjacent side pairs exist when m=3. All polygon x coordinates (-1,2,3/2) differ from the two anchor x coordinates (0,1), so all auxiliary generic-ray guards hold. The nonzero triple entries also exclude every graph-point boundary contact.

For t>0 the whole obstacle is above the horizontal graph segment, so both anchors and the segment are exterior. For t<0, both anchors are strictly inside the triangle. Explicit positive barycentric weights (q_0,q_1,q_2) are:

    p_1: ((2-t/2)/(3-t), (1+t/2)/(3-t), -t/(3-t));
    p_2: ((1-t/6)/(3-t), (2+t/6)/(3-t), -t/(3-t)).

Each row sums to one and gives the stated anchor coordinates. Positivity holds for -1<=t<0. Their entire connecting segment is interior by convexity. Hence for every allowed t the graph-pair segment meets no polygon SIDE: it is either entirely outside or entirely inside. The c05 boundary-only edge clause holds in both situations. Correct exterior classification must distinguish them.

The excluded t=0 is not silently treated as a valid limit case: both anchors then lie on the bottom side, and GP-ALL plus boundary exclusion correctly fail.

## 3. Exact ray products and parity

For z=p_i on a directed side a->b, use the c05 notation

    A=z_x-a_x, B=z_x-b_x, D=a_x-b_x,
    T=orient(z,a,b),
    RayHit = (A*B<0 AND T*D>0).

In side order (q_0q_1,q_1q_2,q_2q_0), the products are:

| Anchor | Side | A*B | T*D |
|---|---|---|---|
| p_1 | 0 | -2 | 9t |
| p_1 | 1 | 3 | 3-3t/4 |
| p_1 | 2 | -3/2 | 15/2+15t/4 |
| p_2 | 0 | -2 | 9t |
| p_2 | 1 | 1/2 | 3/2-t/4 |
| p_2 | 2 | -1 | 15+5t/4 |

Sides 1 and 2 have positive second products throughout the parameter interval; side 1 fails the first test and side 2 passes it. Side 0 passes exactly for t>0. For BOTH anchors:

    t>0: crossing bits c=(1,0,1), prefix XOR b=(0,1,1,0);
    t<0: crossing bits c=(0,0,1), prefix XOR b=(0,0,0,1).

The recurrence b_next=b+c-2bc therefore gives exterior parity precisely on t>0. The positive case exercises an actual even count of TWO rather than the zero-crossing seeds in c05.

## 4. Exact mutation attacks

M1, deleting T*D>0: the sign pattern of A*B is always (-,+,-), so the mutated crossing bits are always (1,0,1). For any -1<=t<0 the forged bits c=(1,0,1), b=(0,1,1,0) satisfy the mutated bit linkage and all remaining exported constraints: combined GP, distinctness, simple triangle, nonzero area, generic ray, boundary exclusion, edge side-nonintersection, real Boolean equations and final even parity. Nevertheless the graph points and their segment lie inside the obstacle. This is a false geometric witness within the exact normalized GP-ALL setting, not a degeneracy excluded by that setting.

M2, testing T>0 instead of T*D>0: on side 0, D=-3 and T=-3t. It therefore counts that side for t<0 and misses it for t>0, reversing the required decision. Side 2 has positive T throughout this interval. Thus M2 gives the same false exterior assignment as M1 when t<0 and falsely rejects the valid positive-coordinate witness when t>0. Dropping a denominator sign is not a harmless normalization.

M3, ordinary addition instead of XOR: at t>0, the correct c=(1,0,1) forces additive prefixes (0,1,1,2), contradicting the final-zero constraint. This excludes the valid witness. No claim is made that the entire mutated existential sentence is unsatisfiable for K2.

For the pair-visibility defect, n=2 and m=3 are the smallest possible dimensions: a graph pair needs two points, and a nonempty simple polygon needs three corners. This is not a minimum-size claim about unrelated encoding bugs.

## 5. Endpoint-order invariance

Swapping a,b exchanges A,B, sends D to -D, and sends T to -T. Both A*B and T*D are unchanged. Thus the correct RayHit is invariant under side reversal. Reversing the polygon while keeping q_0 first changes its corner order to (q_0,q_2,q_1). Crossing bits become (c_2,c_1,c_0): positive t still gives (1,0,1); negative t gives (1,0,0), with prefixes (0,1,1,1). Exterior status is unchanged. In contrast, T>0 is orientation-sensitive. The fixture set includes both cyclic orientations and must not silently require positive signed area.

## 6. Replay data and boundary

research/artifacts/candidates/opg37357-a01-c06-ray-fixtures-v1.json freezes the four rational t=+1/-1, counterclockwise/clockwise cases. Coordinates are rational STRINGS, not floating approximations. The instance object alone is passed to the c05 exporter; the other fields are witness/regression data and are not valid extra exporter input keys. Honest auxiliary bits are separated from the forged full-line mutation bits. Expected acceptance/rejection concerns the fixed coordinate assignment with the named auxiliary bits, never unrestricted graph nonrepresentability.

Planned bounded replay, not executed: parse rational strings exactly; evaluate all c05 helper definitions and all assertions on each assignment; compare the correct and mutated ray definitions without editing any protected script or previously merged candidate; require the predicted failing clause classes. Use one process, one thread, 30 seconds, 256 MiB memory, and at most 65536 output bytes. Record exact interpreter/evaluator versions and artifact hashes in any later authorized receipt. No exporter, unit suite, solver, or geometric checker was executed for this artifact.

The only source dependencies are the repository's c01 closed-contact encoding and c05 exporter at the declared base. All tables above are direct algebraic expansions of those definitions. This slice requires no external numerical library or additional geometric literature premise. It does not close either admitted obligation.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
next_action: build a bounded exact rational evaluation path for these frozen formulas and fixtures, or audit its translation lemmas while runtime authorization remains unavailable.
