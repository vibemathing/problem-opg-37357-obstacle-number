# Same-budget regularization and a connected-graph cutoff

Candidate: candidate:opg37357-a01-c02-regularization-v1
Verdict: candidate_only
Primary owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: 0732f25b07b8269c68da94c0fa4dfd94dbb90adf

## Scope and dependencies

Reuse the closed-polygon conventions and the formulas Phi^V and Phi^ALL from candidate:opg37357-a01-c01-closed-contact-v1, SHA-256 20636a040864566fdae24fe5466e7571e3f748d75bf627f7aa88ef525e8b354d. Graph points are exterior to the filled polygon; GP-V means that graph points are distinct with no collinear triple; GP-ALL imposes the same condition on the combined graph-point/corner set. The graph is finite, simple, labeled, and planar as an input promise; its visibility segments need not form a plane drawing. This artifact does not decide either root question.

There are two different kinds of dependency below. R1 is a new candidate derivation in Euclidean polygon geometry, intended for formal replay. S1 is a precisely located published bound reused as a premise, not a bound proved or replayed by this agent. Their combination narrows the unrestricted-completeness gap for connected graphs. No mathematical command, solver, kernel, or verifier run is reported.

## R1. Same-corner-budget regularization

Statement. Fix a GP-V placement p_1,...,p_n and one filled closed simple polygon P with at most m corners whose visibility graph is G. There is a filled closed simple polygon Q with at most m corners for the SAME graph-point placement, with the same visibility graph, such that the combined graph-point/corner set is in general position. Every blocked pair can moreover be required to meet the interior of Q. This is a statement about the existence of another obstacle, not about the original coordinates satisfying GP-ALL.

### R1a. Remove straight corners and select a small outward offset

Delete any redundant straight corner, meaning consecutive collinear corners with opposite incident rays. This changes neither the filled set nor visibility and does not increase the number of entries. A simple polygon of positive area has at least three nonstraight corners, so the process ends with a list q_0,...,q_(r-1), r<=m, with no collinear consecutive triple. Reverse the cyclic order if necessary to make it counterclockwise.

For each original oriented side define the affine function

    h_i(x)=orient(q_i,q_(i+1),x).

For t>=0 let L_i(t) be the parallel line h_i(x)=-t. Define q_i(t) to be the intersection of L_(i-1)(t) and L_i(t). These lines are not parallel. Solving their fixed nonsingular two-by-two system gives

    q_i(t)=q_i+t*w_i

for a fixed vector w_i. No uniform bound in the input coordinates is asserted. Let C=max_i ||w_i||; it is finite. For sufficiently small t the direction of each new side agrees with its original direction, each side has positive length, and each consecutive orientation retains its nonzero sign. Distances between distinct nonadjacent original sides are positive; a side moves by at most Ct in Hausdorff distance. Hence for sufficiently small t, no nonadjacent sides meet. The new cyclic list therefore bounds a simple polygon P_t for every t in an interval [0,t_0]. This is a mitered parallel offset, not a rounded Minkowski boundary, and it introduces no new corners.

### R1b. Establish nesting, including reflex corners

Choose small disjoint corner neighborhoods and thin neighborhoods of the remaining side interiors, each avoiding nonincident boundary pieces. Such a finite cover exists for a simple polygon. In a side-interior neighborhood, moving its supporting line outward changes the local inside inequality from h_i>=0 to h_i>=-t.

In a convex-corner neighborhood the local polygon is the intersection of the two inside halfplanes; in a reflex-corner neighborhood it is their union. The same description holds after a sufficiently small offset, because the incident rays preserve their directions and turn type and no other boundary piece enters the neighborhood. A point on an old side satisfies its own inequality strictly after the offset. At an old corner both shifted inequalities are strict. Consequently every point of the old boundary is in int(P_t). The corner/side neighborhoods can be chosen with overlapping interiors, so the finitely many choices give one t_0 working for the entire boundary.

For nested simple closed curves, inclusion of the old boundary in the new bounded region implies inclusion of the old filled polygon there: a point in the old interior but outside the new polygon would connect to infinity through the unbounded complement of the new polygon, crossing the old boundary, which is already inside the new polygon. Thus

    P is contained in int(P_t), for 0<t<=t_0.

The changed region can be kept arbitrarily close to P. One precise justification is to follow the continuous family of simple polygonal boundaries q_i(s), 0<=s<=t. Every boundary point stays within Ct of the corresponding original side. A point outside the closed Ct-neighborhood of P is never crossed by this family and starts on its exterior side; its winding number stays zero throughout this boundary-avoiding homotopy. Therefore P_t is contained in the closed Ct-neighborhood of P. The polygonal separation, local wedge description, and winding-number homotopy fact are explicit geometric replay dependencies, not additional unrestricted axioms.

### R1c. Preserve allowed edges and make all blocking strict

Let K be the finite union of all graph points and edge segments. K and P are disjoint compact sets, so their distance delta is positive when K is nonempty. Choose t>0 with Ct<delta/3 and all preceding simplicity/nesting bounds satisfied. If K is empty this clearance condition is unnecessary. Then K is disjoint from P_t. For each nonedge ij choose z_ij in [p_i,p_j] intersect P. Since graph points are outside P, this witness is not an endpoint. Nesting puts every such z_ij in int(P_t), including those that were originally only tangent contacts or boundary-overlap points.

Thus the offset preserves every edge and every nonedge. It also has finitely many positive margins: distance to K and the interior distances of the chosen z_ij to the new boundary. For sufficiently small further perturbations of all polygon corners, simplicity, these exterior conditions, and the interior witnesses persist. To justify interior persistence explicitly, along the straight homotopy between sufficiently close corner lists no boundary can reach a chosen z_ij; its inside/outside class is constant. The same nonadjacent-side and nonzero-turn margins ensure every intermediate polygon remains simple.

Choose the perturbed corners sequentially inside these open neighborhoods, avoiding the finite set of lines through pairs of already chosen corners and fixed graph points, and avoiding their finite point set. Each open disk contains a point outside finitely many lines. When the last point of any triple is selected, collinearity with the earlier two is excluded. The graph points were already GP-V. The resulting Q is GP-ALL, has r<=m corners, and preserves all the margins. This completes the candidate argument for R1.

## R2. Consequence for the bounded formulas

For every integer m, the two c01 sentences Phi^V_(G,m) and Phi^ALL_(G,m) are equisatisfiable. For m<3 both are false by definition. For m>=3, the ALL-to-V implication is immediate. The reverse implication uses c01 soundness, R1, and c01 bounded completeness for ALL. This does not identify their assignment sets: c01 case A2 is still a witness accepted in GP-V and excluded in GP-ALL, while R1 constructs a different polygon accepted in GP-ALL.

The equivalence even holds with the graph-point coordinates held fixed, provided those coordinates are GP-V. It does not assert that an arbitrary perturbation works, or provide an effective universal perturbation radius.

## R3. Adversarial audit of the regularization step

1. For q=((0,0),(1,1),(-1,1)) and p=((-1,0),(1,0)), upward translation of the triangle by any positive amount loses the original tangency block. A bare appeal to small perturbation is therefore insufficient. The offset defined above instead has corners (0,-t), (1+3t/2,1+t/2), (-1-3t/2,1+t/2). For 0<t<1 it contains (0,0) in its interior while both graph points remain outside. The corner count remains three.

2. At the reflex corner (1,1) of the L-shaped polygon ((0,0),(2,0),(2,1),(1,1),(1,2),(0,2)), the two shifted supporting lines meet at (1+t,1+t). The local inside is a UNION of shifted halfplanes, not their intersection. The original corner is interior after this outward shift. Treating a nonconvex polygon as an intersection of all side halfplanes would invalidate the proof.

3. A rectangle with an extra straight corner on one side must have that corner removed before the consecutive-line intersection construction. Otherwise the two lines are parallel/coincident. Removal reduces the count and keeps the obstacle set unchanged.

4. Narrow notches and nearly flat nonzero turns require a possibly very small t. The proof takes a minimum of finitely many input-dependent positive margins; it never uses a universal numeric t. No bit-length bound or floating-point tolerance is inferred.

These are exact coordinate and continuity deductions; no executed regression test is claimed.

## S1. Published premise and the connected case

Source: Balko et al., arXiv:2206.15414v3 (21 January 2024), Section 3.1, Lemmas 12--14 and the displayed inequality on PDF page 13. For a connected n-vertex graph, n>=2, take a representation minimizing obstacle count first and total corner count second. The source supplies

    s <= 2*h*n + 6*n + 15,

where h bounds the obstacle count and s counts all obstacle corners. This premise is not an assertion about every arbitrary polygon representing the graph. Reference and scope details are in research/artifacts/source-notes/opg37357-a01-c02-cutoff-sources-v1.md.

Candidate corollary, conditional on this source premise and R1. For a connected labeled graph G on n>=2 vertices under the declared closed simple-polygon convention,

    obs(G)<=1  iff  Phi^ALL_(G,8*n+15).

Proof. The right-to-left direction is c01 soundness. If G is noncomplete and obs(G)<=1, its minimum obstacle count is one. Among such representations a minimum finite corner count exists by well-ordering. S1 bounds this count by 8n+15, and R1 converts to GP-ALL without increasing it. Then c01 completeness applies. If G is complete, place the vertices in general position and use a harmless remote triangle; 3<=8n+15. The n=1 case can likewise use a triangle separately. Labels do not change the argument because an isomorphism can relabel the same point placement.

For disconnected G, the above corollary is not claimed. Section 3.1's componentwise order-type counting reduction explicitly does not provide a global obstacle representation. Also, vertex/corner counts growing with n are not a universal bound on the NUMBER of obstacles for planar graphs. No SAT or UNSAT instance has been generated or decided here.

## Open replay tasks and continuation

Both admitted obligations remain open. R1's offset/nesting and homotopy lemmas need proof-assistant replay and statement-faithfulness review; the published combinatorial premises need a verified reuse path. A bound for a disconnected graph cannot be obtained merely by adding component encodings. Next proposed slice: give an explicit polynomial corner cutoff for one connected obstacle using a finite line arrangement, an embedded tree through nonedge witnesses, and a polygonal regular neighborhood. This would address disconnected graphs without that invalid componentwise inference.

best_verified_result: none
best_verified_candidate: none
next_obligation: obligation:opg37357-bounded-polygon-encoding
