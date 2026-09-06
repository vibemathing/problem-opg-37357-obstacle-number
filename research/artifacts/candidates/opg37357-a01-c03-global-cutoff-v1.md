# Global one-obstacle cutoff by an embedded witness tree

Candidate: candidate:opg37357-a01-c03-global-cutoff-v1
Verdict: candidate_only
Primary owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: cc14e9659434d61b2d945ea0f5f59f15c0efdd0c

## 1. Statement, scope, and prior art

Let G be a finite simple labeled graph on n vertices with e edges, and put k=binom(n,2)-e. Graph connectedness is NOT assumed. Graph edges are straight segments in a placement and may cross. Graph points are distinct and must lie outside every obstacle. Obstacles block closed connecting segments, including boundary contact.

Candidate theorem. If G has a representation using at most one connected obstacle disjoint from every graph point and edge segment, then it has a representation using one filled closed bounded simple polygon with at most

    B(n,e) = 8*e^2 + 8*binom(n,2) + 4

corners, with the combined graph-point/corner set in general position. The reverse implication to the connected-obstacle model is immediate. The forward proof permits the original connected obstacle to have holes, to be unbounded, or not to be polygonal; it uses only its connectedness, disjointness, and blocking properties. This extension is an explicitly stated candidate, not an assumption about an unspecified contract convention.

For planar G with n>=3, e<=3n-6 yields the looser bound

    B_planar(n) = 76*n^2 - 292*n + 292.

This is a corner bound conditional on a ONE-obstacle representation existing. It neither constructs a one-obstacle representation for every graph nor supplies a universal bound on obstacle NUMBER.

Finite obstacle-complexity bounds and ETR formulations are prior art: see Balko et al., arXiv:2206.15414v3, introduction and Lemma 22. The purpose here is an explicit, deliberately nonoptimal one-obstacle bound with audited constants and no connected-graph or component-stitching assumption. No novelty claim is made for the existence of a polynomial cutoff. Neither a solver nor a mathematical verifier has run.

## 2. The free-space condition

Fix a placement p_1,...,p_n. Let S be its finite point set, let K be S together with all closed graph-edge segments, and let F=R^2 minus K. K is compact and F is open. Every connected component of F is open and polygonally path connected: within a component, the points reachable from a fixed point by polygonal paths form a relatively open set whose complement is also relatively open, using small balls in F.

If a connected obstacle O is disjoint from K, then it lies in one connected component U of F. For every nonedge ij, its blocking intersection with O is also an intersection of [p_i,p_j] with U. Since endpoints belong to K, any such intersection contains a nonempty relatively open subinterval of the open segment (p_i,p_j).

Conversely, assume that some component U of F intersects every nonedge segment. Sections 3--5 construct a simple polygon inside U containing one blocking witness for each nonedge in its interior. No new edges can be obstructed because the polygon avoids K. Thus the free-space condition is sufficient as well as necessary. The case k=0 needs no condition: a triangle placed beyond the convex hull of the finite point set is harmless, and its three corners fit B(n,e), including n=0 or n=1.

## 3. A finite cell graph inside U

Use the arrangement of the DISTINCT infinite supporting lines of graph-edge segments; let their number be ell<=e. Repeated or parallel supporting lines do not increase the bound. Its number f of open two-dimensional cells satisfies

    f <= 1 + ell*(ell+1)/2 <= 1 + e*(e+1)/2.

Indeed, the j-th distinct line meets its predecessors in at most j-1 points and therefore has at most j pieces, each splitting at most one old cell. All open cells are convex. Inside such a cell C the only part of K can be isolated graph points: every graph edge is on an arrangement line. The punctured set C minus S is polygonally path connected. For example, two points can be joined via an intermediate point avoiding the finitely many lines through either endpoint and a forbidden point of S.

Call C eligible when (C minus S) intersects U. Then C minus S is entirely contained in U. Form a graph A on the eligible cells. Two cells are adjacent when their closures share a one-dimensional arrangement piece with a point y in U that is neither an arrangement intersection nor a graph point. The whole supporting line is NOT required to be free; only the selected crossing point is.

A is connected. To see this, join points in two eligible cells by a polygonal path in U. A compact path has positive clearance from K. Perturb its finitely many segments within that clearance to avoid the finite line-intersection set and all graph points, to have no segment along an arrangement line, and to cross arrangement lines transversely. Its consecutive cells are eligible and each crossing supplies an edge of A. Passage through a line intersection causes no problem: if it is in U, a sufficiently small ball around it is free and supports such a perturbed passage.

Let t be the number of eligible cells, so 1<=t<=f, and select a spanning tree of A. On each of its t-1 adjacency edges choose a distinct safe crossing point, called a portal. A small interval of choices is available because U is open. Portals avoid all arrangement intersection points and graph points.

## 4. An embedded tree of controlled size

For each of the k nonedges choose a distinct witness z_ij in (p_i,p_j) intersect U, avoiding the finitely many portals, arrangement intersections, and graph points. Such choices exist because each intersection contains a relative open interval. A witness either belongs to an open cell or lies on an open one-dimensional arrangement piece. In the latter case choose one of its incident eligible cells, which exists since a small neighborhood of the witness lies in U. This also handles an original nonedge collinear with an edge supporting line; no initial general-position assumption is needed for this step.

Assign each portal to its two adjacent cells and each witness to its chosen cell. For each eligible C select a center x_C in C minus S and join it by straight spokes to all its assigned portals and witnesses. Choose the center outside the finite collection of lines through two assigned endpoints, and through an assigned endpoint and any graph point. Also exclude all assigned endpoints. Convexity puts every spoke except possibly its boundary endpoint in C, and the excluded lines ensure that it misses S and that distinct spokes have no common portion or crossing away from x_C. If C has no assigned endpoint, simply choose a free center.

Spokes in different cell interiors are disjoint; their only intentional shared endpoints are portals. All witnesses, portals, and centers are distinct. Consequently the union T is an embedded straight-line tree: it is the selected cell spanning tree with each edge subdivided once at a portal, together with k witness leaves. Its vertex and edge counts are

    N = t + (t-1) + k = 2*t-1+k,
    |E(T)| = N-1.

The entire finite tree lies in U, so it is compact and has positive clearance from K when K is nonempty. Selecting tree edges before thickening is essential: arbitrary extra connections could introduce a cycle and a hole.

## 5. A polygonal neighborhood with at most 8N-4 corners

Auxiliary candidate lemma. An embedded finite straight-line tree with N>=1 vertices has an arbitrarily thin filled closed simple polygon neighborhood with at most 8N-4 boundary corners, containing every tree vertex in its interior.

Construction and corner accounting. Around each tree vertex v choose a small square Q_v centered at v. Make these squares pairwise disjoint and disjoint from every nonincident tree edge. Choose the orientation of each square so no incident edge exits at a square corner; the finitely many distinct outgoing rays then exit at distinct points in side interiors. All squares fit in the chosen free neighborhood.

For every tree edge uv take a sufficiently thin rectangle centered on that segment, with its two short end caps strictly inside Q_u and Q_v. The two long sides meet the boundary of each endpoint square at two points within the same side as the center segment's exit. There is no need for these squares to have a common orientation. Choose rectangle widths sufficiently small that all attachment intervals at a square are disjoint, different rectangles do not meet outside their common endpoint square, and no rectangle meets a nonincident square. Finiteness, positive nonincident clearances, and distinct exit points give positive choices. The complete union P of squares and corridors stays in the prescribed free neighborhood of T.

This union is a topological disk with polygonal boundary. Root the tree and attach one child square and its corridor at a time. Outside the parent square each attachment is a disk meeting the old union along exactly one boundary interval; it meets nothing else. This replaces one boundary interval by a simple detour and does not create a hole or a boundary self-contact. Induction gives a single simple closed boundary. The caps and their rectangle corners are hidden strictly inside endpoint squares. The only possible corners on the final boundary are the 4N original square corners and at most four square/corridor intersection points per tree edge. Therefore

    corners(P) <= 4*N + 4*(N-1) = 8*N-4.

This argument includes degree-two bends and high-degree vertices; no assertion of a universal corridor width or integer grid is made. Redundant straight boundary vertices may be removed, reducing the count.

Apply the lemma inside U. Every nonedge witness is a square center and hence interior to P, while P is disjoint from all graph points and edge segments. The visibility graph of this one simple polygon is exactly G.

## 6. Count and general-position upgrade

Using t<=f and k=binom(n,2)-e gives

    corners(P) <= 8*(2*t-1+k)-4
               <= 16*(1+e*(e+1)/2)+8*k-12
                = 8*e^2+8*binom(n,2)+4 = B(n,e).

Now remove redundant straight polygon corners. All edge segments and graph points have positive clearance from P, and every nonedge has an interior witness. These finitely many strict properties survive small perturbations of both the graph points and the remaining polygon corners, with the same corner count. Simplicity persists by nonadjacent-side clearance and nonzero consecutive turns. Inside/outside membership of the selected witnesses persists by a boundary-avoiding straight homotopy of the nearby simple polygon lists.

When graph endpoints move, a fixed old witness need not remain on the new segment. Instead retain its parameter lambda_ij in (0,1): z_ij=(1-lambda_ij)*p_i+lambda_ij*p_j. Use z'_ij=(1-lambda_ij)*p'_i+lambda_ij*p'_j for the new segment. It moves by at most the largest endpoint displacement and remains inside the nearby polygon for sufficiently small perturbations. This is why moving graph points cannot silently lose a blocked pair.

Within the resulting open set of configurations, choose all graph points and polygon corners sequentially outside the finitely many lines determined by previously selected pairs and outside the earlier point set. This produces GP-ALL while preserving the graph and the corner bound. The number of corners is unchanged except for prior removal of straight ones. The empty point-set and complete-graph cases again use a remote generic triangle.

## 7. Consequence for c01 and the remaining gap

Conditional on the correctness of the displayed candidate lemmas and c01's encoding audit, the following three statements are equivalent for every finite simple labeled G:

(a) some placement has a connected obstacle disjoint from all graph points and edges that blocks every nonedge;
(b) some placement has one GP-ALL filled closed simple polygon with at most B(n,e) corners and visibility graph G;
(c) c01's existential sentence Phi^ALL_(G,B(n,e)) is satisfiable.

For complete graphs, interpret (a) as 'at most one obstacle' or allow a harmless obstacle. Statements (b) and (c) already allow the harmless triangle. The forward construction keeps the original placement through Section 5, and only Section 6 may move it to impose general position.

Thus a candidate route to unrestricted completeness is now explicit for the named connected-obstacle convention, including disconnected graphs. It is not an admitted reduction: formal replay is still needed for the free-space cell graph, the embedded-tree neighborhood, the corner count, perturbation stability, and c01. The canonical contract also needs a faithful comparison confirming that obstacles exclude graph vertices and have the connectedness convention used here. No statement about variants allowing graph vertices inside obstacles is imported.

In particular, UNSAT at an arbitrary smaller m still does not imply an unrestricted obstruction. UNSAT at the displayed cutoff would support such an inference only together with verification of this reduction, c01, the chosen input graph and its planarity, and an appropriate exact UNSAT certificate. No such instance or certificate is reported in this artifact. Both admitted obligations remain open.

## 8. Adversarial audit and next slice

- With e=0, the arrangement is one cell but that cell still contains forbidden graph points. Replacing 'C minus S lies in U' by 'C lies in U' is wrong; the center-line avoidance repairs the star construction.
- An arbitrary portal on a supporting line may lie on a graph edge. The portal must be in U; crossing a supporting line outside an edge is permitted and is not itself an obstruction.
- The convex hull of blocking witnesses need not avoid graph edges or graph points. Tree corridors replace that invalid shortcut.
- Thickening a cyclic connection graph can leave a hole. A spanning tree and disjoint attachment intervals give one simple polygon instead of an unspecified connected region.
- Witnesses on a supporting line are assigned to one incident cell; centers must avoid lines through endpoint pairs to prevent overlapping spokes.
- Perturbing graph points requires moving each nonedge witness by its fixed segment parameter, not retaining its spatial coordinate.

These are mathematical audit cases, not executed tests or protected failed-route entries. A useful next slice is to eliminate c01's finite disjunction over r<=m by proving exact-m padding using distinct ordered inserted corners and robust visibility margins, and to isolate which rational-witness conclusions do and do not follow. No coordinate bit bound is asserted here.

best_verified_result: none
best_verified_candidate: none
next_obligation: obligation:opg37357-bounded-polygon-encoding
