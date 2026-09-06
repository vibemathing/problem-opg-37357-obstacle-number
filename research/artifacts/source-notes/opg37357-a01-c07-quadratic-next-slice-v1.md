# Quadratic sign-factorization: next formalization slice

Status: candidate_only
Owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base for this source note: 853be12e7783f3b4843e98416a9cbbd29f2d41bf

This is a derived mathematical note for a subsequent exporter candidate, not an executed program or a mathematical receipt. It does not change c05's immutable exporter or the c07 packet's registered proof artifact.

## Exact scalar identities

For arbitrary real u,v, define

    Opp(u,v) := (u<0 AND v>0) OR (u>0 AND v<0),
    Same(u,v) := (u<0 AND v<0) OR (u>0 AND v>0).

Then u*v<0 iff Opp(u,v), and u*v>0 iff Same(u,v). These follow by the real ordered field sign cases. If either argument is zero, both predicates are false, exactly as required for the strict product comparisons. No nonzero premise is silently imposed on a predicate's callers.

In particular Opp is NOT the unrestricted complement of Same: at u=0,v=1, both are false. Replacing Opp with NOT Same would therefore admit zero-product cases. No weak-inequality replacement is permitted.

## Application to the geometry primitives

For segment endpoints a,b,c,d, set

    o1=orient(a,b,c), o2=orient(a,b,d),
    o3=orient(c,d,a), o4=orient(c,d,b).

Replace the two quartic products in Proper by

    Opp(o1,o2) AND Opp(o3,o4).

This is pointwise equivalent on ALL coordinate assignments, including collinear or coincident cases. Full closed Meet still consists of this Proper disjunct together with its four endpoint-On disjuncts. Endpoint touching and collinear overlap remain handled by On; they are not absorbed into the strict crossing predicate.

For the normalized vertical-ray primitive, keep

    (z_x-a_x)*(z_x-b_x)<0

and replace

    orient(z,a,b)*(a_x-b_x)>0

by

    Same(orient(z,a,b),a_x-b_x).

The first product is already quadratic in coordinates. The second comparison is now a Boolean combination of quadratic and linear comparisons, rather than a cubic polynomial comparison. The exact denominator sign and forward-ray direction are retained. Alternatively both products may be split by Opp/Same, with the same pointwise semantics.

For c01's unfixed ray direction d, each cross-product quantity A, B, D and T has degree at most two in the coordinate and direction variables. Replacing A*B<0 by Opp(A,B) and T*D>0 by Same(T,D) also gives only quadratic atoms, without normalizing d.

## Degree audit

After nonrecursive macro expansion, orient, squared distance, the dot product in On, polygon signed area, and the adjacent-corner dot product have degree at most two. Real Boolean equations c(c-1)=0 and the XOR equation b_next=b+c-2bc are quadratic. Anchor and generic-ray equalities or inequalities have degree at most two. Finite conjunction, disjunction and negation do not increase polynomial degree. General-position determinants, when retained, are quadratic as well.

Consequently the c01 bounded formula, the c04/c05 normalized formula, and the proposed c07 sparse formula can each be expressed using a Boolean combination of polynomial comparisons of degree at most two. The product splitting introduces no new variables and only a constant-factor expansion per affected primitive. This is NOT a claim that an unexpanded arithmetic product has lower degree, nor that a single conjunction of quadratic constraints has been produced without additional Boolean encoding.

The degree reduction is pointwise equivalence of predicates. It does not rely on the c07 open-neighborhood lemma and remains valid for c06's malformed ray-witness regression inputs. The sparse-GP reduction, in contrast, is an existence-level argument and still requires its separate proof.

## Required regression and continuation

A subsequent standalone sparse exporter must preserve closed avoidance for graph edges and nonadjacent polygon sides, explicit boundary exclusion, exact ray linkage, strict Proper witnesses for nonedges, and XOR parity. Compare the old and split predicates on all nine sign pairs from {-1,0,1} squared, then use the c06 interior/exterior and orientation fixtures plus c07's contact-only triangle. These are planned tests, not reported outputs.

No claim about SAT, UNSAT, running time, polynomial coordinate bit size, or an unrestricted obstacle-number bound follows from this algebraic rewrite. The next implementation must receive a new candidate ID, immutable path and packet after the preceding PR is actually merged and main is freshly read.
