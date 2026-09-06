# Exact-size, affine-normalized, rational-witness formulation

Candidate: candidate:opg37357-a01-c04-normal-form-v1
Verdict: candidate_only
Primary owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: bcfec30feef427d950c3721fdad490647e318c2f

## Scope and dependencies

Use the c01 filled closed simple-polygon model, exterior graph points, and GP-ALL convention. Graph vertices are labeled; their connecting edge segments need not be noncrossing. The parameter m bounds polygon corners, not obstacles. The results below are candidate reductions of this same bounded question. c01 is the base encoding; c02 is needed only for transferring results to the separately named GP-V convention. c03 is needed only when a global corner cutoff is substituted. No mathematical verifier, solver, or code execution is reported.

## N1. At most m is equisatisfiable with exactly m

For every fixed G and integer m>=3, existence of a GP-ALL representation using one simple polygon with at most m corners is equivalent to existence with exactly m corners. The backward implication is immediate. The forward construction does not repeat or identify corners.

Start with an r-corner GP-ALL representation, r<=m. Each blocked pair intersects the polygon interior. Indeed, a boundary-only intersection at a polygon corner would make that corner and the two graph points collinear. A boundary-only intersection in a side interior without a transverse crossing would make the pair segment collinear with that polygon side. Both contradict GP-ALL. Choose one interior witness per nonedge. All graph points and visible edge segments have positive distance from the closed polygon, and all chosen nonedge witnesses have positive distance from its boundary.

If r<m, select one polygon side [a,b] and insert m-r DISTINCT points in its relative interior, in increasing order of their projection along b-a. Initially these are straight subdivision vertices and the filled polygon is unchanged. Perturb only the inserted points inside small disjoint open disks about their chosen positions. Make the disks small enough that their projections remain strictly ordered between a and b. The replacement polygonal chain is then strictly monotone in this projection and cannot self-intersect. It remains close to [a,b], avoids all nonincident original sides, and its first and last segments remain separated from the original adjacent sides except at a and b. These facts follow respectively from the positive nonincident clearances and the original nonzero corner angles.

For sufficiently small disks, every intermediate chain along the straight perturbation homotopy is simple and stays away from all graph points, edge segments, and chosen interior witnesses. Boundary-avoiding homotopy preserves the side containing each such point. Thus visibility is unchanged. Choose the inserted points sequentially outside all lines through pairs of the original graph points/corners and previously inserted points. A finite collection of lines cannot cover any open disk. The resulting complete point set is GP-ALL and the polygon has exactly m actual nonstraight corners.

The case m<3 remains false for one nonempty simple polygon. For n<=1 and m>=3, a remote convex m-gon gives a representation. Applying c02 before this construction gives the analogous existence equivalence for GP-V, but the displayed GP-ALL proof itself does not depend on c02's offset lemma.

## N2. Normalize two graph anchors and the auxiliary ray simultaneously

Assume n>=2. Given an exact-m GP-ALL representation, choose a common ray direction d that is nonzero, not parallel to any q_a-p_i, and not parallel to u=p_2-p_1. All excluded directions form a finite set, so such a d exists.

The two columns u,d form a nonsingular matrix M. Apply the invertible affine map

    A(x) = inverse(M)*(x-p_1).

It sends p_1 to (0,0), p_2 to (1,0), and the vector d to (0,1). An invertible affine map preserves closed segments, intersections and disjointness, simple polygons and their bounded regions, the number of corners, and collinearity/noncollinearity. Determinants are multiplied by one common nonzero factor; the map may reverse orientation, which c01 permits. It also preserves forward rays with their nonnegative parameters, not just the unoriented supporting lines.

Consequently the bounded existence question is unchanged by imposing

    p_1=(0,0), p_2=(1,0), d=(0,1),
    (q_a)_x != (p_i)_x for every i,a.

These are not constraints on an arbitrary original coordinate witness: they become available only after the affine map. For n=1 translate p_1 to (0,0), choose a generic d, and complete it to any affine basis to make d vertical; no second graph anchor is used. For n=0 the bounded existence answer is true exactly when m>=3 and no ray is required.

With these substitutions and n>=2 the continuous coordinate variables number 2n+2m-4: two per graph point beyond the first two, and two per polygon corner. The ray is a constant, not an additional variable. No assumption that {1,2} is a graph edge is required.

## N3. A reduced fixed-m formula

Let N_(G,m) be c01's single r=m GP-ALL conjunct with the substitutions from N2, using fresh variables for its parity bits. N1 and N2 show, conditional on their candidate proofs and c01,

    Phi^ALL_(G,m) is satisfiable iff N_(G,m) is satisfiable.

The finite disjunction over 3<=r<=m is eliminated. The formula has size O((n+m)^3+n^2*m+n*m+m^2) when the explicit indexed constraints and fixed-arity primitives are expanded. This is polynomial in n+m, not a claim about succinct binary m.

In this GP-ALL mode the following simplifications are also faithful:

- For a graph-pair segment and a polygon side, or for two nonadjacent polygon sides, all four endpoints are distinct and no three are collinear. Thus c01's Meet is exactly Proper on these calls.
- Every graph-point On-side predicate is already false by GP-ALL, and every adjacent polygon triple has nonzero orientation. Their guards can be retained for clarity or omitted as redundant.
- Polygon simplicity still requires the nonadjacent-side tests; GP-ALL alone does not imply simplicity. Exterior parity constraints must also be retained; nonintersection with the boundary alone does not imply visibility.

For the vertical ray from z to side ab, the c01 quantities reduce to

    A = z_x-a_x,
    B = z_x-b_x,
    D = a_x-b_x,
    T = orient(z,a,b),
    RayHit := A*B<0 AND T*D>0.

This follows by substituting d=(0,1), not by dropping a denominator sign. If A*B<0 then D=B-A is nonzero. If D=0 then A=B and the first test is false. All polynomials still have total degree at most four, and the vertical-ray products have degree at most three.

The real crossing bits c_(i,a) and prefix parity bits b_(i,a) remain as in c01: c*(c-1)=0, c agrees with RayHit, b_(i,0)=0, b_(i,a+1)=b_(i,a)+c_(i,a)-2*b_(i,a)*c_(i,a), and b_(i,m)=0. The normalized formula is existential over the reals; no integer quantifier or division has been introduced.

## N4. Rational witnesses exist, without a polynomial bit claim

Suppose N_(G,m) is satisfiable. Fix the crossing and parity bits to the 0/1 values of that satisfying assignment. At a GP-ALL normalized configuration all distinctness tests, all triple orientations, and all differences (q_a)_x-(p_i)_x are nonzero where required. Their signs remain unchanged throughout a sufficiently small open neighborhood in the free-coordinate space. Keep the signed polygon area sign unchanged as well.

Every Proper test is fixed by the orientation signs. Every RayHit test is fixed by the signs of A,B,T and, in a straddling case, by D=B-A, whose sign is then forced and nonzero. In a nonstraddling case its first test stays false, even if D initially vanishes. Thus all geometric predicates, crossing bits, and parity constraints retain their truth values on that open neighborhood. The already fixed anchor and ray coordinates are rational constants.

Rational points are dense in this finite-dimensional free-coordinate space. Choose rational coordinates in the neighborhood and keep the bits at their integer values. This gives a rational satisfying assignment to N_(G,m), and hence a rational GP-ALL representation with exactly m corners. No coordinate rounding tolerance is supplied without a witness-dependent margin.

This does NOT prove polynomial-length certificates or membership in NP. A simple warning example is the strict quadratic system

    x_0>2; x_(j+1)>x_j^2 for j=0,...,s-1.

It has rational solutions, but every solution has x_s>2^(2^s). A rational x_s=p/q in lowest terms with positive denominator therefore needs a numerator with exponentially many bits in s. This example concerns arbitrary strict polynomial systems, not a proved lower bound for obstacle representations. It only invalidates the inference from rationality alone to a polynomial certificate bound.

## Adversarial checks and continuation

A. Repeated-corner padding remains invalid (c01 A7). N1 inserts distinct ordered points, then moves them off all forbidden lines while maintaining a simple chain.

B. A fixed vertical ray without transforming the geometry excludes legitimate coordinate witnesses. For example, graph points (1,3),(3,3), a visible edge between them, and obstacle triangle (0,0),(2,0),(1,2) are GP-ALL, but the first graph point shares an x-coordinate with the top corner. N2 changes coordinates after choosing a generic d; it does not assert that the displayed witness passes a vertical generic-ray guard.

C. Choosing d parallel to p_2-p_1 makes M singular. The additional excluded direction in N2 is essential, even when d would otherwise be a valid parity ray.

D. Proper-only tests are justified only after the GP-ALL guards. Without them, c01's tangent-contact counterexample still applies. Likewise, GP-ALL cannot replace the exterior tests or the nonadjacent polygon-simplicity tests.

E. Small rational rounding is not a fixed-decimal guarantee. The radius is determined by all current strict signs; no universal precision is asserted.

All examples and deductions are hand-derived candidate audits, not machine test results. Existing source-faithfulness notes and the c01--c03 candidates remain unchanged. Both admitted obligations are open. The next slice is a bounded, deterministic formula-export candidate implementing N_(G,m), with explicit failure limits and exact regression inputs; any actual execution must be separately authorized and recorded.

best_verified_result: none
best_verified_candidate: none
next_obligation: obligation:opg37357-bounded-polygon-encoding
