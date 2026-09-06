# Source comparison for the global cutoff candidate

Verdict: candidate_only
Target: obligation:opg37357-bounded-polygon-encoding
Retrieved: 2026-09-06

Balko et al., *Bounding and Computing Obstacle Numbers of Graphs*, arXiv:2206.15414v3, 21 January 2024. Locators: https://arxiv.org/pdf/2206.15414 ; https://arxiv.org/abs/2206.15414

The introduction, PDF page 2, expresses fixed-drawing obstacle number by faces that collectively meet every nonedge. Lemma 22, PDF pages 22--23, sketches a general complexity bound O(e^2+n) and an ETR reduction. Section 3.1, PDF page 7, warns that its componentwise counting description need not be a global obstacle representation.

Our c03 artifact gives its own explicit one-obstacle construction through safe arrangement portals, a tree, and a polygonal neighborhood. Its constants are derived there, not attributed to the paper. The bound is intentionally coarse and does not improve the cited asymptotic result. It includes graph-point exclusions even for isolated vertices. No source certificate or mathematical proof assistant was replayed. PDF text was retrieved; the renewed screenshot request failed, and no figure-based claim is made.

Repository dependencies: c01 encoding and c02 perturbation discussion at cc14e9659434d61b2d945ea0f5f59f15c0efdd0c. This source note neither amends their frozen files nor changes either open admitted obligation.
