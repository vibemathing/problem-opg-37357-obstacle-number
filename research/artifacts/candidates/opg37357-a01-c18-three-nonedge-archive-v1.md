# C18: archive of the existing three-nonedge component diagnostic

Candidate: candidate:opg37357-a01-c18-three-nonedge-archive-v1
Verdict: candidate_only
Owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Transport base: 9decdb4f205623bc848d39f4dde8cb84f4c1e4a9

## Provenance and execution status

This file transports the mathematical object already recorded before the current transport-only request in Issue #3 comment 5563305025 (created and last updated 2026-09-07T00:17:58Z) and the preceding chat summary. Source locator:
https://github.com/vibemathing/problem-opg-37357-obstacle-number/issues/3#issuecomment-5563305025

Only conclusions, explicit data, scope and verification dependencies are preserved. This is not a transcript or an execution receipt. No new mathematical research, enumeration, determinant evaluation, solver run, formula update or proof-assistant run was performed during this archival transaction. Every numerical item below is an already-derived EXPECTED value pending mathematical replay.

## Fixed labeled input

The vertex order is A,B,C,D,u,v,w. Coordinates are exact integers:

    A=(-20,0), B=(0,20), C=(20,0), D=(0,-20),
    u=(1,8), v=(-2,-7), w=(30,1).

The complete edge set is {AB,BC,CD,DA,AC}. Thus u,v,w are isolated graph vertices. Graph-edge segments and all graph points are excluded from the obstacle. The obstacle under discussion must be connected; the polygon model is filled and closed, with exterior graph vertices. Graph edges are not required to be noncrossing in the general problem, although this diagnostic drawing has that property.

Write T for the open upper triangle ABC with its isolated point removed, Btm for the open lower triangle ACD with its isolated point removed, and O for the unbounded component outside ABCD with its isolated point removed. These are the three free-space components in the recorded argument.

## Already-derived incidence and crossing data

Parameters below refer to (1-s) times the first endpoint plus s times the second endpoint of the named nonedge.

| Nonedge | Free-space components met | Only graph-edge crossing | Parameter | Crossing point |
|---|---|---|---|---|
| uv | {T,Btm} | AC | 8/15 | (-3/5,0) |
| uw | {T,O} | BC | 1/2 | (31/2,9/2) |
| vw | {Btm,O} | CD | 5/8 | (18,-2) |

The recorded additional check is that vw reaches the infinite supporting line y=0 at parameter 7/8 and point (26,0), beyond the finite edge AC. The segment uw stays above AC. A supporting-line hit is not automatically an edge-segment hit.

Every two of the selected nonedges have a common component, but the intersection of all three component-incidence sets is empty. A connected obstacle disjoint from the drawing lies in one component, so it cannot meet all three selected nonedges. The C03 free-space witness-tree construction is the cited dependency for making one connected polygon that meets any selected pair while avoiding the graph drawing. These statements concern the selected constraints at the fixed coordinates, not a representation of every nonedge of the graph.

This is a candidate counter-witness to replacing whole-class common-component compatibility by pairwise compatibility. It is not an all-placement obstacle-number lower bound.

## All 35 previously recorded orientation determinants

Use orient(a,b,c)=(b_x-a_x)(c_y-a_y)-(b_y-a_y)(c_x-a_x). The tables fix ordered triples, not merely unordered sets. Values are copied from the earlier mathematical checkpoint without a new evaluation.

The four outer triples ABC, ABD, ACD, BCD each have determinant -800.

For an outer pair XY, entries in the next table mean orient(X,Y,u), orient(X,Y,v), orient(X,Y,w):

| XY | u | v | w |
|---|---:|---:|---:|
| AB | -260 | -500 | -980 |
| AC | 320 | -280 | 40 |
| AD | 580 | 220 | 1020 |
| BC | -220 | -580 | 220 |
| BD | 40 | -80 | 1200 |
| CD | -540 | -300 | 180 |

For an outer point X, entries mean orient(X,u,v), orient(X,u,w), orient(X,v,w):

| X | uv | uw | vw |
|---|---:|---:|---:|
| A | -291 | -379 | 368 |
| B | -51 | 341 | 848 |
| C | 309 | -99 | 48 |
| D | 69 | -819 | -432 |

Finally orient(u,v,w)=456. The 4+18+12+1 listed values are all nonzero, which is the earlier candidate general-position audit. This is a stored expected-value table, not an observed successful test or a verifier certificate.

## Preserved placement-guarded exclusion

For a larger graph containing the five specified motif edges and the three specified nonedges, additional graph segments or points can only refine the free-space components. The existing candidate claim extends the obstruction when the seven selected points have the displayed orientation SIGN pattern, or its reflection. It is not conditioned on the displayed determinant magnitudes.

Let H be the conjunction of the 35 orientation sign literals for one chosen pattern, and let c_(s,j) mean that nonedge s is assigned to connected blocker j. The recorded necessary clause is

    (OR over literals h in H of NOT h)
    OR NOT c_(uv,j) OR NOT c_(uw,j) OR NOT c_(vw,j).

The reflected pattern is handled with its corresponding sign literals. The transfer from this finite sign pattern to the same geometric incidence obstruction is a pending statement-faithfulness dependency. Boolean orientation assignments must not be assumed geometrically realizable. No existing CNF has been modified, strengthened by execution, or solved in this transaction.

## Full-drawing scope warning

The same fixed drawing also has nonedges uA, vD and wC with singleton free-space incidence T, Btm and O, respectively. Hence the whole drawing requires blockers in all three components. The selected triple's cover number two must not be described as a two-obstacle representation of the entire drawing. No claim here quantifies over all placements of the abstract seven-vertex graph, and no universal planar-graph bound follows.

## Reproduction obligations, not execution claims

A later authorized audit should freeze these coordinates and edge set, evaluate all listed determinants exactly, check each finite-segment crossing and interpolation parameter, verify the component-incidence sets after deleting graph points, and replay the connected-obstacle component argument. It must separately check sign-pattern transfer, reflection, and the larger-graph refinement clause. Invalid geometric witnesses, nonrealizable Boolean patterns and tool failures are not graph-level counterexamples.

Repository dependencies at the transport base include research/artifacts/candidates/opg37357-a01-c03-global-cutoff-v1.md for the free-space construction and the existing frozen ProblemContract/obligation graph for semantics. No outside source text or new source claim is imported. The current transport only moves the previously recorded material from coordination text into a hash-bound candidate file.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
next_action: finish this one-packet transport and final reconciliation; resume mathematics only after the transport-only request is satisfied.
