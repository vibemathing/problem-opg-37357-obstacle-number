# Source-faithfulness note: bounded polygon encoding

Verdict: candidate_only
Binding: attempt:web-20260906-opg37357-a01; obligation:opg37357-bounded-polygon-encoding.
Retrieval date: 2026-09-06. No external repository was operated on.

## S1. Definition convention and the two invariants

John Gimbel, Patrice Ossona de Mendez, Pavel Valtr, *Obstacle Numbers of Planar Graphs*, arXiv:1706.06992v3 (7 September 2017), Section 1, PDF pages 1--2.
Locator: https://arxiv.org/pdf/1706.06992v3

The introduction uses closed connected polygonal obstacles, excludes graph points from obstacles, and requires general position of the combined graph-point/corner set. It discusses neighborhood and hole-removal conversions without a fixed corner budget. It separately defines planar obstacle number by requiring noncrossing graph edges. Therefore GP-ALL is the main bounded interpretation in our candidate, while GP-V is a named extension; we must not add a plane-drawing constraint to the ordinary obstacle-number target. Its statement about a constant planar-graph bound is historical context, not a current-status certificate. Page 1 was inspected as a rendered PDF as well as parsed text.

## S2. Existing result relevant to the first root question

Leah Wrenn Berman, Glenn G. Chappell, Jill R. Faudree, John Gimbel, Chris Hartman, Gordon I. Williams, *Graphs with Obstacle Number Greater than One*, JGAA 21(6), 1107--1119 (2017), DOI 10.7155/jgaa.00452. Preprint arXiv:1606.03782v2 (6 April 2017); Proposition 5.3(2) refers to this preprint version. Journal metadata was checked at the publisher and corrected before merge.
Locators: https://jgaa.info/index.php/jgaa/article/view/paper452 ; https://arxiv.org/pdf/1606.03782

The article reports ordinary obstacle number 2 for the icosahedron graph. Proposition 3.5 alone concerns OUTSIDE obstacle number and must not be substituted for Proposition 5.3. The source's connected-obstacle convention is broader than this candidate's bounded simple-polygon model. No supplied SAT certificate has been replayed here. This is a prior-art and statement-faithfulness flag for the first root question, not repository admission or a newly discovered planar obstruction. It supplies no universal constant for the separate second question.

## S3. Polygon predicate semantics

CGAL 6.0, *2D Polygons: Global Functions*, entries is_simple_2 and bounded_side_2.
Locator: https://doc.cgal.org/6.0/Polygon/group__PkgPolygon2Functions.html

The documented simplicity condition allows consecutive sides to meet at their shared corner only. Bounded-side classification distinguishes boundary points and uses odd/even crossings. Our formula is not a CGAL call: it replaces a specially handled horizontal ray with an existentially selected generic direction and represents parity by real Boolean bits. This documentation is a semantics cross-check, not an execution receipt or a formal proof of our encoding.

## S4. Follow-up lead, not yet imported into candidate C1

Martin Balko et al., *Bounding and computing obstacle numbers of graphs*, arXiv:2206.15414, Section 3.1. Locator: https://arxiv.org/abs/2206.15414

A source search located a total obstacle-vertex bound in the counting argument for connected graphs. The precise minimality, connectedness, general-position, and outside-obstacle hypotheses require a separate audit before using any numeric cutoff. C1 deliberately does not infer unrestricted completeness from this lead.

## Protected inputs

All repository inputs are at base fae37538c3d7b76e3ea977c3c734b455146f357f. ProblemContract digest: 10fb03f159d4818c5141567a77390e1351fda77c9810ac45d66dd7d4e14aa4f5. The admitted target asks for a bounded encoding; no literature hit closes its formal verification or the root. Existing failed-routes ledger was empty.
