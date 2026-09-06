# Root-source update and statement comparison (c09)

Verdict: candidate_only
Retrieved: 2026-09-06
Target: obligation:opg37357-root

## Q1: exact journal statement, not just an outside-obstacle result

Berman, Chappell, Faudree, Gimbel, Hartman, Williams, *Graphs with Obstacle Number Greater than One*, JGAA 21(6), 1107--1119 (2017), DOI 10.7155/jgaa.00452. Journal Proposition 3 (PDF page 7) gives ordinary obstacle number two for X4, the icosahedron, and X6. Figure 4 and the next paragraph identify X4 as planar of order ten. PDF pages 7--8 were inspected as images. This directly addresses Q1 under the connected-obstacle convention. The separate outside-obstacle statements are not substituted for it. Our c08 proof/replay package supplies its own frozen lower-bound certificate; the source is prior art, not new mathematical admission.

https://jgaa.info/index.php/jgaa/article/download/paper452/2511/2318

## Q2: ordinary, planar-drawing, and convex variants

Gimbel, Ossona de Mendez, Valtr, *Obstacle Numbers of Planar Graphs*, arXiv:1706.06992v3 (7 September 2017). Section 1 uses closed connected polygonal obstacles and excludes graph points from them. It explicitly asks about a constant for ordinary planar-graph obstacle number. Theorem 1 concerns the DIFFERENT invariant that forbids graph-edge crossings; its value n-3 is not an ordinary-obstacle lower bound. Theorems 3--4 give ordinary one-obstacle representations for PURE-2-DIR and bipartite planar graphs (apart from complete-graph zero cases). Hence bipartite planar graphs are not useful targets for an ordinary >1 obstruction under these conventions. Empty and singleton inputs must be handled separately rather than copying a source's shorthand exceptional list.

https://arxiv.org/pdf/1706.06992

Balko et al., *Bounding and Computing Obstacle Numbers of Graphs*, arXiv:2206.15414v3 (21 January 2024), SIAM J. Discrete Math. 38(2), 1537--1565 (2024), DOI 10.1137/23M1585088. The literature discussion distinguishes the fixed plane-drawing optimization from ordinary obstacle number and notes their discrepancy. Its complexity/corner bounds do not furnish a universal obstacle-count constant for planar graphs. No such conclusion is imported.

https://arxiv.org/html/2206.15414v3

The EuroCG 2026 official Wednesday program includes *Planar Convex Obstacle Number of Trees* by Di Giacomo, Haase, Kindermann and Liotta. The stated linear lower bound requires BOTH convex obstacles and a crossing-free drawing. It does not show ordinary obstacle numbers of trees or planar graphs are unbounded. The program is an author-submitted abstract, not a proof replay.

https://eurocg26.fernuni-hagen.de/program-wednesday.html

Fresh searches combined 'obstacle number' with 'planar graphs', 'constant', '2024', '2025', '2026', 'Hamiltonian', and 'triangulations'. They did not locate a theorem giving an ordinary universal planar constant or an ordinary unbounded planar family. This records the bounded retrieval outcome, not an exhaustive literature-completeness certificate or a reason to stop research.

## Graph-theoretic reuse and computation inputs

Therese Biedl, *Triangulating planar graphs while keeping the pathwidth small*, arXiv:1505.04235, states the ordinary edge-augmentation fact used to obtain T. Our induced extension is separately proved by subdivision and selective face coning; the source is not cited as stating that exact construction or its vertex count.

https://arxiv.org/abs/1505.04235

Bose, Jansens, van Renssen, Saumell, Verdonschot, *Making triangulations 4-connected using flips*, arXiv:1110.6473, Computational Geometry 47(2) (2014), 187--197, DOI 10.1016/j.comgeo.2012.10.012. The no-separating-triangle characterization is the standard connectivity premise used for the triangle-free corollary; the quantitative edge-flip theorem is not used and would not preserve inducedness.

https://arxiv.org/abs/1110.6473

NetworkX official graph_atlas_g documentation identifies the installed atlas as the graphs through order seven. The actual audit recorded NetworkX 3.6.1 and Python 3.13.5. Atlas regressions check only the induced-triangulation implementation; they do not enumerate obstacle representations.

https://networkx.org/documentation/stable/reference/generated/networkx.generators.atlas.graph_atlas_g.html

No external GitHub repository was operated on. No raw paper, full chat, private runtime path, or trusted verification receipt is stored here.
