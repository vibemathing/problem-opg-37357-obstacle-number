# C28 extension: two coupled families, exhaustive h=2 tests, and a genuine higher-order gap

Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Owner: math-computation with candidate proof audit
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Target: obligation:opg37357-root
Base: f09892bdb8e26edcdfc80edacc2790de904a70ea
Issue: #3

## 1. Reconciliation and exact new scope

The existing C28 branch first exposed guarded_cnf.py and second_check.py at
3ef98e6ba87c6cacd3e3bae26801e863a6f8c20e. Both were recovered byte-for-byte,
retained unchanged and actually executed. Later fresh-read exposed an existing
README, controls, graph/model, rank3 control, execution and ONE packet. Those
are retained; this supplement does not overwrite their proofs or historical
receipts. C22/C26/C27 and their packets are not retransported.

New material: a second coupled graph, a compact one-bit-per-target generator,
scalar exhaustive cross-check, all 23 single-edge deletion instances, exact
polygon verification of BOTH least models, and an all-length two-obstacle
construction for the shared missing-port path family. The original C28
saturated-ring and C18 rank3 results are dependencies, not claimed new here.

Both six-vertex base formulas and every indexed one-edge deletion are SAT.
The base minima are actual rational polygonal obstacle representations, not
merely abstract or pseudoline models. No obstacle-number-three graph is found.
The precise failed routes are listed below; no universal planar upper bound
or all-placement impossibility follows from these tests.

## 2. Two non-X4 coupling definitions and complete planarity certificates

A has vertices 0,...,5 and edges
  02,03,04,05,12,13,14,15,23,34,45.
Its complete nonedge list is 01,24,25,35. The three induced diamond modules
{0,1,2,3}, {0,1,3,4}, {0,1,4,5} share the MISSING port 01. The last three
nonedges are cross-module helper pairs; all are retained as target constraints.
This is the smallest chain of three successive diamond modules, not a minimum
obstruction over all planar graphs. Its rotation rows are
  0:2,3,4,5; 1:2,5,4,3; 2:0,1,3;
  3:1,4,0,2; 4:3,1,5,0; 5:4,1,0.
There are seven dart-face cycles, six triangles and one quadrilateral.

B is the original C28 octahedral three-port ring. Its edges are
  02,03,04,05,12,13,14,15,24,25,34,35;
its nonedges are 01,23,45. The modules {0,1,2,3}, {2,3,4,5}, {0,1,4,5}
are C4s, not diamonds. A second valid rotation used by the new checks is
  0:2,5,3,4; 1:2,4,3,5; 2:0,4,1,5;
  3:1,4,0,5; 4:3,1,2,0; 5:3,0,2,1.
It has eight triangular faces. This need not equal the original README's
rotation: both are auxiliary certificates of the same abstract graph.

The consumer checks the full neighbor and dart sets, closed face orbits,
connectedness and n-e+f=2. Gluing an oriented vertex disk/edge ribbon/face disk
for each item constructs a connected orientable sphere embedding. Deleting
one graph edge restricts this embedding and yields the recorded deletion
rotations. ALL obstacle placements remain unrestricted straight-line drawings;
the displayed rotations never force the cyclic order of an obstacle drawing.
certificate.json stores both full edge/face/rotation lists and variable maps.

## 3. One quantifier order, and an exact guarded relaxation

For fixed G and arbitrary injective real coordinates p, let K_p be its points
and CLOSED edge segments, and J_s(p) the free components meeting open nonedge s.
The connected-obstacle existence interface is
  exists p, labels z_s in {0,1}, components U_0,U_1,
  for every nonedge s: U_(z_s) belongs to J_s(p).
Each used label has ONE common component for its whole class. Unused labels
are harmless. The finite witness/path construction yields bounded connected
obstacles; simple-polygon extraction is a distinct C19 layer. The explicit
polygons below bypass that dependency.

A graph-level lower bound three requires negating this full existential
sentence for a proved simple planar G. The Boolean formula is only necessary:
  exists directions x, exists labels z, exists side variables q: F_G(x,z,q).
A hypothetical representation may first be regularized with C27's SINGLE
positive clearance margin before GP selection. No zero orientation is guessed
as a Boolean sign, and density alone is not used to preserve contacts.

Increasing triples give direction variables 1,...,20; odd permutations negate
literals. All ordered four-point and five-point determinant implications are
retained, exactly the two C26/C27 necessary families. They are not asserted
to decide realizability of arbitrary order types or pseudoline arrangements.
A has z variables 21,...,24 for 01,24,25,35. B has 21,...,23 for 01,23,45.
Separate q_st variables follow for ordered distinct target pairs. A thus has
36 variables; B has 29. The original B prototype's 32-variable exact-one
encoding is retained; Z_(s,0)=not z_s and Z_(s,1)=z_s maps its entire formula
to this compact one after variable renaming and tautology removal.

For EVERY simple graph path P from s=ab to b (including length five), and
another target t=cd, let C=(x_cdv: v in P except c,d), J=(x_abv: v internal).
Each of the four unguarded path disjunctions D from C27 is replaced by BOTH
  z_s OR z_t OR D,
  not z_s OR not z_t OR D.
Different labels deactivate both. Equal labels activate exactly one copy.
The same q_st serves all paths of that ordered pair. Pair-local Jordan
separation proves necessity, not simultaneous intersection for larger classes.
The generator emits a tuple origin for every direction row and the actual
(s,t,path,key-sign,side-sign,color) origin for every path row. No path uses a
nonedge. run.py --sources NAME emits the complete derived provenance table.

When directions and colors are fixed, all-positive key paths force q=true,
all-negative key paths force q=false, and mixed paths force neither. A q
exists precisely when both forces do not occur for a same-color pair.
Eliminating q by this condition is an EXACT Boolean elimination, including
for unrealizable direction tables; it is not an assumed geometric property.

## 4. Complete finite results, actual execution and mutations

A: 30 four-point + 480 five-point + 920 guarded path rows = 1,430 clauses;
   36 variables and 83 simple nonedge paths.
B: 30 + 480 + 624 = 1,134 compact clauses; 29 variables and 84 paths.
The retained exact-one B prototype has six more clauses, totaling 1,140.

ALL 1,048,576 direction words were tested. Exactly 11,904 pass the direction
clauses. A tests all 16 color words (16,777,216 direction/color pairs):
21,248 pairs survive exact side elimination, on 6,480 different directions.
B tests all eight color words (8,388,608 pairs): 15,952 survive, on 6,464 directions.
A's counts in lexicographic color order are
  196,968,436,1820,968,1396,1820,3020,3020,1820,1396,968,1820,436,968,196.
B's are 176,2600,2600,2600,2600,2600,2600,176.

The new compact generator imports no C22/C26. The bitset method handles every
word as a bit position. audit.py independently scans the entire direction
range scalarly, using a different stack path traversal and scalar pattern
matching for every color. All per-color counts and minima agree. The existing
second_check.py additionally reconstructs the full prototype clause set from
Cartesian words and counts residual unit-side clauses directly. This is
implementation diversity in ONE generator trust domain, not trusted admission.

Every single-edge deletion of A and B was regenerated and exhaustively counted:
11+12 further indexed tests, ALL SAT. Each has its own full edge list, restricted
rotation, variable/clause count, formula digest and minimum Boolean assignment
in the emitted full run.json; the saved compact observation records parent and
removed edge unambiguously. Deletion minima are NOT classified geometrically.

Sixteen damaged records were rejected: changed/reversed edge lists, missing
clause/guard, flipped direction, repeated/wrong path endpoints, row reversal,
missing exact-one row, bad color/side maps, invalid color mode, omitted five-edge
path row, duplicate row and two damaged rotations. These are distinct from
legitimate deleted-edge inputs, which were recomputed and found SAT.

The final main execution exited 0 in 10.095548 seconds, with 35 CPU seconds,
40 wall seconds, 512 MiB, one worker and 4 MiB output limits, using CPython
3.13.5, Fraction arithmetic and exact integer bitsets. Four further export
commands actually produced both DIMACS formulas and both provenance tables.
Two-coupling-execution records their precise hashes and resource identities.
One exploratory report shadowed its dimension variable with a vertex index;
computed masks/counts were unaffected, but displayed domain sizes were wrong.
The variable was renamed and all final sources rerun; no bad output is used.

## 5. Least models: genuine geometry, so no invented triple cut

Minimum order is directions, THEN labels, THEN sides, with false before true
and compact words MSB first. Both least direction words are zero, realized by
p_i=(i,-i^2), because D(i,j,k)=-(j-i)(k-i)(k-j)<0 for increasing triples.
This is not a claim that all surviving words are realizable.

A's least labels are (0,1,1,1). Only q variables 29 and 36 are true. Exact
incidence is J_01={0}, J_24={8,9,11}, J_25={8,9,10,11,12}, J_35={10,11,12}.
In particular the three label-1 targets have common component 11. One square
of half-width 1/1000 centered at (1/2,-1/2) handles 01. The other obstacle is
the convex hull of coordinate perturbations by +/-1/1000 of
  (17/6,-9), (11/4,-37/4), (10/3,-35/3).
It has seven vertices; certificate.json gives the exact coordinates and hits.
B's least model has all 29 bits false and J_01=J_23=J_45={0}. In addition to
the original README's analytical 12-corner construction, certificate.json
contains an x-monotone 26-boundary-vertex polygon directly checked by the new
polygon consumer; collinear boundary subdivision vertices are harmless.

The consumer checks all nonadjacent boundary pairs, point exclusion, CLOSED
edge contacts, every nonedge's interior interval witness and obstacle disjointness.
Minimum squared edge/boundary distances are 7442/3515625 for A and 1/32800 for B.
It has no arrangement/CNF imports. The explicit representations use two and
one polygons respectively. No valid common-component constraint can eliminate
these complete minima: in particular, claiming an empty triple intersection
in A's label-1 class would be FALSE. Other Boolean survivors remain unclassified,
not automatically real or pseudoline-realizable.

## 6. All lengths of the shared missing-port chain have at most two obstacles

Let D_m (m>=3) consist of nonadjacent poles u,v, a path w_1...w_m, and every
pole-helper edge. Its n=m+2 and e=3m-1, with nonedges uv and w_iw_j for j-i>=2.
D_4=A. Helpers placed in order on a line and poles on opposite sides give a
crossing-free auxiliary drawing: each fan is in its own halfplane and helper
edges are consecutive line intervals. The graph is simple planar.

For a DIFFERENT obstacle placement set R=m+1,
  u=(0,-R^2), v=(-1,-R^2), w_i=(i,i^2).
Let Q be the convex hull of all nonconsecutive helper-pair midpoints, and
  eps=1/(64(m+1)), P_up=Q+[-eps,eps]^2.
Every generating midpoint has y-x^2=(j-i)^2/4>=1. The convex variance identity
gives the same lower bound on Q. Since 1<=x<=m there, all points of P_up satisfy
  y-x^2 >= 1-(2m+1)eps-eps^2 > 1/4.
Every consecutive helper edge instead has
  y-x^2=(x-i)(i+1-x)<=1/4.
On a u--w_j edge, y-x^2=(j-x)(x-R^2/j)<=0. On a v--w_j edge it equals
  (j-x)(x-alpha), alpha=(R^2-j)/(j+1)>j,
so is <=0 on [-1,j]. Thus P_up avoids every graph edge and point, and all
nonconsecutive helper midpoints lie strictly inside it.

Use a second rectangle centered at (-1/2,-R^2) with half-width/height 1/16
for uv. Edges from u have x>=0, helper edges x>=1. A v-spoke has slope
(j^2+R^2)/(j+1)>1, so in x in [-9/16,-7/16] it is already >7/16 above the
rectangle's center height and misses its top at +1/16. Both poles are exterior,
uv's midpoint is interior, and P_up lies at positive x, disjoint from this box.
These are bounded filled convex polygons; m=3 permits Q to be a singleton,
whose epsilon square is nondegenerate. All internal and cross-module nonedges
have been included. No C19 tube-count assumption is needed.

Therefore FOR EVERY m>=3 there EXISTS a real two-polygon representation.
The code actually checks m=3,4,5,8,16; the all-m statement follows from the
inequalities, not extrapolation. Exact equality to two is not asserted. This
family uses shared NONEDGE ports and is not the old star/clique-edge example.
D_m cannot witness obstacle number >=3. This does not exclude other connectors,
all planar graphs, or a different all-placement growth argument.

## 7. Higher-order continuation with a real false positive

The pre-existing rank3-control uses four selected C18 targets 45,46,56,16:
  J0={1,2}, J1={0,2}, J2={0,1}, J3={0}.
The new triple_check.py entry recomputes this from exact points and graph edges,
then examines all 16 label tuples (not C18's entire target family). Pair tests
allow eight; joint-component feasibility allows six. The two false positives
are label tuples (0,0,0,1) and (1,1,1,0). The first three targets have pairwise
nonempty intersections but empty triple intersection. Hence the necessary cuts
  z0 OR z1 OR z2, and not z0 OR not z1 OR not z2
remove precisely those two assignments. These cuts are valid at THAT drawing.
They are not extracted from A/B's genuine first models, and are not universal
clauses for every placement of C18's abstract graph.

A first minimal abstract triple-ONLY system excluding two colors has five
targets and ten component types U_ij covering exactly each pair. Every triple
intersection is empty; all ten two-clause triple prohibitions exclude all 32
colorings by pigeonhole. With <=4 targets a 2+2 split avoids every monochromatic
triple. This minimality is solely for abstract triple constraints. No planar
geometric realization or all-placement forcing theorem is claimed for it.

Next atomic step: find a DIFFERENT simple planar graph whose EVERY real
placement forces a non-two-colorable higher-order demand system, with proved
chart guards; or exhibit a realization showing that proposed guard is too strong.
A fixed control, a pseudoline model, and an abstract coloring obstruction must
not be substituted for this missing placement-universal bridge.

## 8. Artifacts and assurance

run.py prints the full deterministic record, including complete deletion graph
rotations and assignments. --dimacs/--sources with diamonds or octahedron prints
the full formula/provenance. Put the existing C27 candidate directory on PYTHONPATH.
The compact two-coupling-observation.json is explicitly a derived summary, not
misrepresented as raw stdout. The raw output and four exports are preserved in
the replay attachment and regenerable from committed source. certificate.json
stores both base graphs and actual models. two-coupling-execution.json binds all
source/output digests, limits, corrected exploratory report and later triple run.

The first small triple replay was killed under its resource cap (exit -9, empty
stdout). A bounded diagnostic then succeeded; the final standalone source rerun
exited 0 in 0.621495 seconds with 20 CPU/25 wall seconds and 512 MiB bounds.
Both failed and successful statuses are retained; the failure is not a theorem.

Existing C28 README/receipts describe a blocked, unused development slab source.
That source was not recovered or retried. The newly delivered geometry_check.py
is an explicit polygon-contact consumer, not a restored slab implementation;
it imports neither that source nor any arrangement core. Published math files
use ordinary text, finite in-memory arithmetic and stdout only. No network,
process creation, filesystem reads/writes, secrets or dynamic execution occur.
Same-principal diverse implementations are not a new trusted verifier domain.

T=C19 tube/Jordan, A=incidence, P1=old X4 chain and P2=unrestricted growth remain
separate. No old root contradiction is rerun, no Result is signed, and transport
checks do not give mathematical closure. Retain the existing ring failed-route
proposal and add D_m plus the precise bounded deletion census to its candidate
scope; never edit the protected failed-routes ledger directly.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
failed_route: saturated port ring; D_m shared-missing-port path as an obs>=3 family;
bounded two-base/one-edge-deletion necessary systems all SAT
next_atomic_step: a placement-uniform higher-order incidence guard for a different
simple planar coupling, not another search of these already-SAT families.
