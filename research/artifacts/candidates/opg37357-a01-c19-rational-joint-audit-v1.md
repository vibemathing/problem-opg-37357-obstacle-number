# C19 companion: exact check of the acute/reflex six-corner fixture

Candidate: candidate:opg37357-a01-c19-rational-joint-audit-v1
Verdict: candidate_only
Owner: math-proof
Target: obligation:opg37357-bounded-polygon-encoding
Base: 05e200eb918ff174a3f35c66769cbaf19a22750e

This is a direct rational-coordinate derivation, not a geometric script run.
It checks A8 of the companion four-lemma proof without assuming L4.

Let a=1/100, d=(3/5,4/5), and n=(-4/5,3/5). The tree consists of
[(0,0),(4,0)] and [(0,0),4d]. Its vertices number three; E=2 and L=2.

In cyclic order let
q0=(401/100,-1/100), q1=(401/100,1/100), q2=(1/50,1/100),
q3=(1207/500,1601/500), q4=(1199/500,1607/500),
q5=(-1/50,-1/100).
Write e_i=[q_i,q_(i+1)] with indices modulo six.

The six sides lie on:
e0: x=401/100;
e1: y=a, with 1/50<=x<=401/100;
e2: n dot x=-a;
e3: d dot x=401/100;
e4: n dot x=a;
e5: y=-a.

## All nine nonadjacent side pairs are disjoint

e0 is disjoint from e2,e3,e4 because all their x coordinates are
at most 1207/500 < 401/100.

e1 is disjoint from e3 because every point of e3 has y>=1601/500>a.
The intersection of e1's supporting line with e4's supporting line
solves -(4/5)x+(3/5)(1/100)=1/100, giving x=-1/200.
This is outside e1's x interval, so e1 and e4 are disjoint.
e1 and e5 lie on distinct horizontal lines.

e2 and e4 lie on distinct parallel lines. Every point of e2 has y>=a,
so e2 and e5 are disjoint. Finally e3 has y>=1601/500>-a, so e3 and e5
are disjoint. This lists 3+3+2+1=9 pairs.

All adjacent supporting-line directions are nonparallel:
vertical, horizontal, d, n, d, horizontal in cyclic order.
Consecutive closed segments therefore meet exactly at their listed common
endpoint. Vertices are distinct. The boundary is a simple six-sided polygon.

## The entire tree is interior

The origin is not on the boundary. Its positive horizontal ray crosses
e0 once, in the side interior, and no other side: e1,e5 are horizontal
at nonzero y; e2,e3 have positive y; e4 meets y=0 at x=-1/80<0.
Thus the origin is in the bounded region by the Jordan polygon parity
criterion (the ray avoids vertices and is transverse).

For [(0,0),(4,0)], the segment is disjoint from every boundary side.
It misses e0 since x<=4<401/100 and misses e1,e5 by y=0.
It misses e2,e3 by positive y. Its only possible hit with e4 has
x=-1/80<0. A connected segment missing the Jordan boundary cannot move
from the bounded component to the unbounded one, so this whole segment
lies in the interior.

For the second tree segment x=t*d, 0<=t<=4, n dot x=0 rules out e2,e4.
Its d dot x=t<=4 rules out e3. Its x coordinate is at most 12/5, ruling
out e0. Its y coordinate is nonnegative, ruling out e5. It reaches y=a
at t=1/80, where x=3/400<1/50, outside e1. It too misses the entire
boundary and starts at the interior origin. Hence it is entirely interior.

This verifies a fixed rational fixture with six actual corners, exactly
2E+L=6. It is not a proof for arbitrary trees, not a test of arbitrary
neighborhood widths, and not a graph-level obstacle-number bound.
The general theorem still uses the four-lemma manuscript.

The Jordan parity fact used here is documented in Jeff Erickson,
Simple Polygons, 2023 notes, section Point-in-Polygon Test:
https://jeffe.cs.illinois.edu/teaching/comptop/2023/notes/01-simple-polygons.html
The required ray hypotheses were checked above. No numeric library, solver,
geometric evaluator or proof assistant was executed. All fractions and
inequalities are displayed algebraic statements for review.
