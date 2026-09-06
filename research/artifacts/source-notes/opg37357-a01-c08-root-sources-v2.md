# Root-source audit: Q1 answered; Q2 not supplied by the retrieved theorems

Verdict: candidate_only
Attempt: attempt:web-20260906-opg37357-a01
Target: obligation:opg37357-root
Retrieved: 2026-09-06
Base: 853be12e7783f3b4843e98416a9cbbd29f2d41bf

## Berman et al.: exact Q1 theorem and proof scope

Leah Wrenn Berman, Glenn G. Chappell, Jill R. Faudree, John Gimbel, Chris Hartman, Gordon I. Williams, Graphs with Obstacle Number Greater than One, Journal of Graph Algorithms and Applications 21(6), 1107--1119 (2017), DOI 10.7155/jgaa.00452.
Publisher: https://jgaa.info/index.php/jgaa/article/view/paper452
Journal PDF: https://jgaa.info/index.php/jgaa/article/download/paper452/2511/2318

The JOURNAL version's Proposition 3, printed page 1113, states ordinary and outside obstacle number 2 for X4, the icosahedron, and X6. X4 has ten vertices. Lemmas 1--3 and formulas (1)--(7) supply the orientation/key-path necessary conditions. The lower-bound proof reports UNSAT using three solvers; upper bounds are exhibited by two-obstacle drawings. This result answers Q1, not merely a fixed-drawing or outside-obstacle version. Preprint proposition numbers differ; the journal proposition number is used here. The paper does not certify that ten is the minimum planar order.

The publisher's abstract and PDF text were read; the Proposition 3 page was also inspected as an image. The journal's late discussion, Conjecture 10 on printed page 1117, proposes obs(G)<=2 for planar G. It is a conjecture, not a proved universal k. A preprint statement about the dodecahedron must not supersede the journal's one-obstacle representation. The legacy author software URL could not be recovered reliably; no original binary/certificate reproduction is claimed.

Our c08 replay-v2 separately implements the NECESSARY-condition construction; all execution belongs to the same candidate-generation trust domain. The chosen path cap is four edges, a weakening sufficient because its resulting formula has an explicit RUP refutation. The new certificate is not a copy of the article's solver output. The program omits path-indicator variables by resolution; the written soundness argument supplies this exact statement difference. Coordinate data are exclusively a planarity certificate.

For the contract's closed-segment convention, the lower bound extends to any one connected obstacle disjoint from vertices/edges, including holes or unbounded shapes. The README gives a finite positive-clearance general-position conversion with no corner budget. X4's nonzero degree and absence of true twins handle possible literal omissions of vertex exclusion or point injectivity in the terse contract. Counting a disconnected union as one obstacle would be a different invariant and is not imported.

## Gimbel--Ossona de Mendez--Valtr: ordinary versus plane

John Gimbel, Patrice Ossona de Mendez, Pavel Valtr, Obstacle Numbers of Planar Graphs, arXiv:1706.06992v3; GD 2017 proceedings, LNCS 10692, pp. 67--80, DOI 10.1007/978-3-319-73915-1_6.
https://arxiv.org/abs/1706.06992
https://arxiv.org/pdf/1706.06992

Theorem 1 gives maximum PLANAR obstacle number n-3 for n>=4. That invariant requires a crossing-free visibility drawing. It implies an n-dependent upper bound for the ordinary invariant, not a universal constant and not an ordinary lower bound. Theorem 4 gives ordinary obstacle number at most one for bipartite planar graphs; for order at least three the noncomplete cases need one. Thus the planar bipartite subclass is not a search source for Q1 under these conventions. The introduction distinguishes the two invariants explicitly; its relevant page was inspected as an image. Some displayed min/max wording in parsed text is not used as an extra theorem.

## Balko et al. and later search boundary

Martin Balko, Steven Chaplick, Robert Ganian, Siddharth Gupta, Michael Hoffmann, Pavel Valtr, Alexander Wolff, Bounding and Computing Obstacle Numbers of Graphs, SIAM Journal on Discrete Mathematics 38(2), 1537--1565 (2024), DOI 10.1137/23M1585088.
https://arxiv.org/html/2206.15414v3

Theorem 1's growing lower bound is for unrestricted graphs, not planar graphs. The paper explicitly separates fixed drawings, convex obstacles, and ordinary obstacle number. No universal planar k is obtained from its counting, vertex-cover, or fixed-polygon results. Its account of an eight-vertex co-bipartite obstruction is not a planar-obstruction assertion.

Additional bounded searches on 2026-09-06 used combinations of planar graphs, obstacle number, constant, at most two, 2025, and 2026. No source proving a uniform ordinary-obstacle bound or a planar unbounded family was located. EuroCG 2026's Planar Convex Obstacle Number of Trees concerns BOTH a convexity restriction and a plane-drawing restriction; its title/result is not a Q2 answer. This search result is not an exhaustive current-open-status certificate.
https://eurocg26.fernuni-hagen.de/program-wednesday.html

## Consequence for this repository

Q1 has a published positive answer and now a locally replayed root-focused certificate candidate for a concrete graph. Q2 remains mathematically unclosed by our current work. The next root slice reduces Q2 to maximal planar graphs using INDUCED triangulation supergraphs, not unsupported monotonicity under adding/deleting edges. No records or Result admission are changed by this note.
