# C17: pruned witness trees and a smaller polygon-corner cutoff

Candidate: candidate:opg37357-a01-c17-pruned-tube-cutoff-v1
Verdict: candidate_only
Owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Requested cycle base: 2cebd7ca9ba4051dd0c3178835e2f4b58cea293c

## 1. Exact scope

Use distinct graph points, closed straight graph-edge segments, and a filled bounded closed simple polygon disjoint from all graph points and graph edges. Graph edges may cross. No plane-layout or convex-obstacle constraint is imposed. Let n and e be graph order and size, k=C(n,2)-e, and

    B17(n,e)=max(3,2e^2-e+3*C(n,2)).

Candidate theorem: if a fixed placement admits a connected obstacle avoiding all graph points/edges and meeting every nonedge, that placement admits a simple polygon with at most B17 corners. Allowing graph points to move also yields a GP-ALL representation within the same bound. The first assertion preserves the placement; the GP assertion does not.

This refines c03 without withdrawing its larger bound 8e^2+8*C(n,2)+4. Neither bound is trusted mathematical Evidence here. Root source-faithfulness must confirm the exterior-point, connected-obstacle and closed-filled conventions separately. A harmless polygon also represents a complete graph, so the existence test concerns obstacle number at most one, not exact minimal obstacle number one.

## 2. Tree-neighborhood lemma with all joint corners counted

Let T be a finite embedded plane straight-line tree with N>=2 vertices, E=N-1 edges and L leaves. Edges have positive length and intersect only at their common endpoints. For every open U containing T, there is a filled simple polygon P with T contained in int(P), P contained in U, and at most 2E+L corners.

Choose small radii r_v>0 so that the closed vertex balls of radius 2r_v are disjoint, contained in U, and avoid nonincident tree edges. Also require r_u+r_v<length(uv) for every edge. Finiteness and compact separation permit these choices.

At a nonleaf vertex v order its outgoing unit directions d_i counterclockwise; write n_i for their counterclockwise perpendiculars. Use one common width delta>0, chosen sufficiently small after the radii and angles. Put

    R_i=v+r_v*d_i-delta*n_i,
    L_i=v+r_v*d_i+delta*n_i.

For the sector of angle theta_i in (0,2*pi) from d_i to d_(i+1), join L_i to R_(i+1) through

    w_i=v+delta/sin(theta_i/2)*b_i,

where b_i is the unit direction of that sector's bisector. The two joining pieces are on the offset lines facing the sector. In coordinates v=0,d_i=(1,0), the point is (delta*cot(theta_i/2),delta). At theta_i=pi the two offset lines coincide; use the straight join and omit the artificial middle point.

Together with the caps R_i--L_i these joins form a local polygon J_v. Choose delta/r_v so small that port angular windows are disjoint, every w_i lies within radius r_v/2, and the projection of every OTHER ray's port onto d_i is strictly less than r_v. The last condition follows from d_i dot d_j<1 for distinct rays and sufficiently small delta. Each sector join sweeps its polar angle between its two ports, with exactly one radial intersection at every intermediate angle. The caps fill the remaining angular windows. Therefore the boundary is a simple radial graph and J_v is a star-shaped disk containing v strictly inside. It lies within radius 2r_v. For every incident i all its vertices, and therefore its filled polygon, satisfy d_i dot (x-v)<=r_v. Near each cap it contains a terminal strip of positive length and width 2delta. Opposite collinear rays are covered by the straight-join case.

At a leaf use the rectangle with rear vertices v-delta*d +/- delta*n and front vertices v+r_v*d +/- delta*n. The leaf point is strictly interior. Its two rear vertices are its cap turns.

For edge uv attach a width-2delta rectangle between its two corresponding port caps, along the truncated center segment from u+r_u*d to v-r_v*d. This center segment has positive length. The finitely many truncated edge segments are pairwise disjoint compact sets. Nonincident vertex balls and edge pieces have positive separation. By shrinking delta, connector rectangles are disjoint, avoid nonincident local polygons, remain in U, and meet their endpoint polygons exactly in their designated port caps. The endpoint supporting-plane property excludes any other endpoint intersection.

The union is a disk: root the tree and attach each new connector rectangle and child disk along single, distinct boundary intervals. These tree attachments cannot create a hole or a cycle, and unintended contacts were excluded. The boundary is one simple polygonal Jordan curve and its filled region is exactly the union. The center tree is strictly interior, including all attachment centers.

Port caps disappear in the union. The connector long sides and their adjoining sector pieces are collinear at every port, so port corners do not survive. A nonleaf vertex contributes at most deg(v) sector turns; a leaf contributes two rear turns. Thus

    corners(P)<=sum_(deg(v)>=2)deg(v)+2L=2E+L.

Redundant straight boundary points can be removed. Reflex sectors, high degree and global orientation are all allowed. There is no geometry-independent positive width: sectors approaching zero or 2*pi require smaller delta. For N=1 use a separate small triangle.

## 3. Marked free-space cells and pruning

Let K be the union of the closed graph-edge segments and graph points. The connected obstacle lies in one open component U of R^2 minus K. Each nonedge meets U in a relative-open interval, since its endpoints lie in K. Components of this planar open set are polygonally path connected.

Let ell<=e count the distinct supporting lines of graph edges. Their arrangement has at most

    f<=1+ell*(ell+1)/2

open 2-cells. Removing graph points from an open cell leaves it polygonally path connected. An eligible cell belongs to U. Join eligible cells only across a relatively open arrangement-edge interval in U avoiding arrangement vertices and graph points. Their adjacency graph is connected: perturb a compact polygonal path in U, within its positive separation from K, to avoid the finitely many arrangement vertices and to cross supporting lines transversely. Its cell sequence then uses permitted adjacency intervals. No general-position assumption on those lines is made.

Choose a distinct witness for each nonedge, avoiding arrangement vertices and graph points. It may lie on an open piece of a supporting line; assign it to either adjacent eligible cell. Otherwise assign it to its open cell. Mark assigned cells. In a spanning tree of the eligible-cell graph prune unmarked leaves until its minimal subtree spanning the marked cells remains. Let its cell count be t<=f. If t>=2 every leaf cell is marked.

AFTER choosing witnesses, choose one distinct portal in U per retained cell-tree edge, avoiding every witness. Each available interval is open. Within each retained cell choose one center and connect it by straight spokes to its assigned witnesses and incident portals. Exclude the finitely many center positions on lines through two endpoints or through an endpoint and a graph point. Convexity and these line exclusions make spokes avoid K and intersect only at their own center. Different cell interiors are disjoint; their only shared tree points are designated common portals. A witness on an arrangement line is attached only to its assigned cell.

This constructs an embedded straight-line tree in U with

    N=2t-1+k,   E=2t-2+k.

## 4. Count and small cases

Assume k>=2. If t=1 the center has degree k>=2. If t>=2 every internal cell center has at least two portals, and a leaf cell is marked, so its center has a portal and a witness. Portals have degree two. The tree leaves are therefore EXACTLY its k witnesses. The neighborhood lemma yields

    corners<=2E+k=4t-4+3k
             <=4f-4+3k
             <=2ell*(ell+1)+3k
             <=2e*(e+1)+3*(C(n,2)-e)
              =2e^2-e+3*C(n,2).

The polygon avoids K and contains every nonedge witness strictly inside. No graph-point movement occurred.

For k=1 choose a small triangle in U containing the one witness. Do not apply L=k to the center-plus-witness tree: that tree has TWO leaves. For k=0 place a harmless triangle beyond the finite graph drawing. This proves the candidate B17 formula in all cases.

For planar n>=3, substitution of e<=3n-6 gives B17<=(39*n^2-153*n+156)/2. The expression 2e^2-e increases on nonnegative integers because its next difference is 4e+1. At n=10,e=24 the new algebraic count is 1263 versus c03's 4972. These are counts, not observed exports or timing data, and do not bypass exporter caps.

## 5. GP, rationality and verification boundary

The compact polygon is disjoint from K and hence has positive clearance from all graph edges and points. Each nonedge contains an interior witness. Choose a rational interpolation parameter in an open interval of such interior parameters for each nonedge. Remove redundant straight polygon corners. Small joint movement of graph points and polygon corners preserves simplicity, exterior points, edge avoidance, and the interior status of these fixed-parameter witnesses. Choose rational coordinates in this neighborhood off all finitely many combined-triple lines. This gives GP-ALL without increasing the corner count.

This is a moving-endpoint robust-interior argument, not arbitrary perturbation of contact-only blockers. The unit-direction offset construction need not preserve rational coordinates; rationalization is a subsequent step. C16's quantitative radius applies only after an actual rational sparse witness and its certificates have been supplied. It does not construct the unknown representation from G or bound coordinate bits by graph order. C04's padding and affine normalization remain separate replay dependencies when using a fixed-m formula.

No bounded-m UNSAT is upgraded without verification of the cutoff, formula and source-faithfulness. No offset construction, grid, evaluator, exporter, solver or proof assistant was executed for this candidate.

## 6. Adversarial checks

An unpruned three-arm star with center (0,0) and leaves (1,0),(-1,1),(-1,-1), only two marked, has L=3, not 2. Its three sector turns and six cap turns give nine, not 2E+2=8, turns in this construction. Pruning the unused arm removes this counting defect. This is not a lower bound for every possible polygon.

The single-witness tree likewise has L=2 and a four-corner rectangle; the separate triangle is needed. Small/reflex angles prohibit a fixed universal width. Opposite rays require the explicit coincident-line case. Ignoring joints or using mismatched port widths would invalidate the count. Isolated graph points remain excluded, and witness/portal selection must avoid spurious identifications. Finally, existence at one placement and existence after moving to GP are distinct statements.

## Sources and continuation

The cell/witness method refines research/artifacts/candidates/opg37357-a01-c03-global-cutoff-v1.md. The local radial-disk, pruning and 2E+L count are supplied here, not imported as a theorem from an offset library. C04, C07 and C16 provide normalization and witness context. No novelty or optimality claim is made. All topology, geometry-to-formula and source-faithfulness obligations remain for trusted replay. Earlier artifacts and protected records are unchanged.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
next_action: construct and audit a three-nonedge pairwise-compatible but jointly incompatible component class in a fixed GP drawing, and derive a placement-guarded exclusion rather than a graph-level lower bound.
