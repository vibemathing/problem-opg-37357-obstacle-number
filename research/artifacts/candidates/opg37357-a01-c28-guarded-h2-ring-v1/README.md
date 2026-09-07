# C28: exhaustive h=2 port-ring test and a realized ternary interface

Candidate: candidate:opg37357-a01-c28-guarded-h2-ring-v1
Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Primary owner: math-computation (proof and semantic audit included)
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Target: obligation:opg37357-root
Base: f09892bdb8e26edcdfc80edacc2790de904a70ea
Issue: #3

## 1. Outcome and exact scope

The first fully enumerated coupled h=2 instance in this packet is SAT, not
an obstacle-number-three candidate. All 2^20 orientation assignments and
all eight exact-one two-label assignments were covered. All six side bits
are eliminated symbolically at each ordered target pair; together
this accounts for all 64 side assignments, without a SAT solver. Two separately
written counting methods agree on 15,952 extendible direction/label pairs.

More decisively, the minimum SAT orientation is realized by p_i=(i,-i^2),
i=0,...,5, and the stored 12-corner polygon blocks precisely the three
nonedges. This is an actual counterexample to the proposed all-placement
lower bound FOR THIS GRAPH. It is not a counterexample to C22/C26 or the root.
No novelty claim is made for the obstacle number of this small known graph.

The template is new, not the prohibited induced-X4-copy relaxation: three
K2,2 modules share nonedge terminal pairs, and every mixed-module simple
key path is included. This is minimal only in the declared template of
three disjoint two-terminal groups. Global minimality over planar graphs,
or successful obstruction growth, is NOT claimed.

The whole exact port-ring template is then excluded as an amplification
family: t=3 has the displayed one-obstacle representation; every t>=4
produces a nonplanar graph. Deleting module edges would define a DIFFERENT
interface and introduce new nonedges; it is not excluded by that theorem.

Pre-publication fresh-read found C27/PR32 newly merged. Its X4 audit,
fiber method and star-gluing counterfamily are not retransported. C28 reuses the already-published C27 fiber dependency for this h2/rank3 test,
without copying that source or repeating its geometric theorem.

The next layer has been implemented rather than merely named: the byte-pinned C27 rational
finite-segment vertical-fiber consumer recovers free-component incidence.
The two NEW CNF cores import neither C22 nor C26. A four-target slice
of C18 supplies a genuinely two-used-label assignment satisfying every pair
compatibility test but violating a ternary common-component constraint.
The ternary interface rejects precisely two of eight pair-compatible labelings.
Neither that slice nor the full C18 drawing gives an all-placement lower bound.

## 2. Graph, modules, rotation system and minimality boundary

Let A_i={2i,2i+1} for i=0,1,2. Module M_i contains all four edges joining
A_i to A_(i+1), indices modulo 3. Thus the complete edge list is

02,03,04,05,12,13,14,15,24,25,34,35,

and the complete nonedge list is s0=01,s1=23,s2=45. Equivalently G=K_{2,2,2}.
Modules are the cycles (0,2,1,3), (2,4,3,5), (4,0,5,1).
There are no missing pairs BETWEEN distinct terminal groups in this saturated
instance. Coupling is through shared nonedge ports and mixed-module paths,
not through unlisted cross-group nonedges. Each target belongs to two modules.

The cyclic neighbor lists below specify an orientable rotation system:

0: 2,4,3,5       1: 2,5,3,4       2: 0,5,1,4
3: 0,4,1,5       4: 0,2,1,3       5: 0,3,1,2

The dart rule (u,v)->(v,next_v(u)) has eight triangular orbits, stored in
graph.json. Every one of the 24 darts occurs once, the graph is connected,
and n-e+f=6-12+8=2. Equivalently these are the eight faces obtained by putting
poles 0,1 on opposite sides of the equatorial cycle (2,4,3,5). This supplies
an explicit sphere embedding and proves simple planarity. No plane-drawing
restriction is placed on any hypothetical obstacle representation.

Three distinct two-terminal groups require six vertices; under the rule
'include all four edges of every cyclic port module', these twelve edges
are forced. That is the entire minimality claim. graph.json records all
84 target paths and the module of every path edge. Seventy-two paths use
more than one module. Each target has 4 length-two, 8 length-three,
8 length-four and 8 length-five paths. ALL simple paths are included here,
not C26's length-four truncation. For example 0-2-4-1 traverses all three
modules and is an origin for guarded clauses concerning target 01.

## 3. One quantifier order for geometry, components, labels and orientations

Fix G. For injective p put K(p)=all graph points plus CLOSED graph edges and
F(p)=R^2 minus K(p). Let J_s(p) be the components meeting the relative
interior of nonedge s. Under the explicit connected-obstacle convention,

exists p, exists U_0,U_1 in components(F(p)), exists f:nonedges->{0,1},
for every s: U_(f(s)) is in J_s(p)

is equivalent to existence of at most two connected obstacles. Each used
color must use ONE component, not a component chosen afresh for each target.
Unused colors impose no demand. Repeated chosen components are allowed and
can be merged. The equivalence follows from the finite witness/path argument
of C20/C23: connected obstacles lie in one open component; conversely connect
the finitely many assigned witnesses inside that component. Conversion to
simple polygon obstacles is a separate qualitative C19 dependency. The direct
polygon counterexample in section 6 does not depend on that conversion.

For a graph-level lower bound three the required statement is the negation
of this entire existential sentence, for a proved planar G. One fixed p
with no two-color extension is insufficient.

To obtain the necessary Boolean formula, FIRST regularize a hypothetical
representation. Finite assigned path unions have positive distance d from K.
Choose a closed epsilon-neighborhood with 0<epsilon<d/3, and preserve each
nonedge interpolation parameter. All endpoints may move by a common
eta<min(epsilon/2,(d-epsilon)/2,one quarter minimum vertex distance). Then
all graph edges retain clearance and every assigned hit stays interior.
Only after establishing this open neighborhood choose vertex general position.
Density alone is not the argument. For several colors use the minimum of
the finitely many positive margins. This requires no C25 quartic decoder.

Thus a hypothetical geometric representation gives

exists orientation bits chi, exists exact-one label bits z, exists side bits q:
Phi_G,2(chi,z,q).

The formula ranges over ALL Boolean directions, including unrealizable ones.
UNSAT would be a sound route to a geometric impossibility, conditional on
semantic acceptance. SAT alone need not supply geometry. Here the minimum
model additionally has an explicit rational polygon representation with the
analytic proof below; this is not trusted admission.

## 4. Exact guarded CNF and clause provenance

Increasing vertex triples have orientation variables 1,...,20, in lexicographic
order; positive means counterclockwise. Permutation parity changes a literal's
sign. Variables 21,22 are z_(01,0),z_(01,1); 23,24 are z_(23,0),z_(23,1);
25,26 are z_(45,0),z_(45,1). Each target has clauses (z0 OR z1) and
(not z0 OR not z1). At most two obstacles does not require using both labels.

Variables 27,...,32 are q_(s,t) in lexicographic ordered DISTINCT nonedge-pair
order. For each simple graph path P from a to b, s=ab,t=cd, put
C=(chi_cdv : v in P except c,d) and J=(chi_abv : v internal to P).
For each r=0,1 append guard (not z_(s,r) OR not z_(t,r)) to each of

OR C     OR not q OR OR J;
OR C     OR q     OR OR not J;
OR not C OR not q OR OR J;
OR not C OR q     OR OR not J.

The same q serves all paths of the ordered pair. Exact-one labels allow it
to be shared between colors because only one color can activate both guards.
When colors differ every guarded clause is satisfied regardless of q.
When colors agree, C26's PAIR-LOCAL Jordan separation lemma applies: opposite
forcing key paths would separate s from t by graph-edge pieces, preventing
one connected obstacle from hitting both. When C is mixed all four clauses
are vacuous; when C is constant, all-positive J forces q=true, all-negative
J forces q=false, and mixed J forces neither. No spatial order is assumed
for unrelated paths or obstacles.

The four/five-point orientation families are the necessary determinant rules
from C22/C26, now instantiated on SIX vertices. No X4 CNF or source is copied.
The new generator enumerates internal vertex permutations, while the second
source audit enumerates Cartesian words and filters repeated vertices/edges.
Neither imports C22/C26. After tautology deletion and deduplication there
are exactly 1,140 clauses: 30 four-point, 480 five-point, 624 guarded-key,
and 6 exact-one clauses. The 3,150 raw clauses include every path/color/mode.
Each stored/generated final row has an explicit valid source. The second
consumer reconstructs the full expected clause SET and order, not just counts.

The complete CNF and row origins are deterministic derived outputs from
controls.py --bundle (key cnf.json). Their full byte hash is in execution.json
and observation.json. They are not uploaded as another large duplicate cache.
The runnable sources and minimum model are the delivered certificate interface.
The final three-source implementation, graph, model and compact observations
are the published package; the blocked development source in section 9 is not.

## 5. Exhaustive result, and why this covers directions rather than samples

A Python integer of 2^20 bits holds one bit per orientation assignment.
The generator constructs variable truth planes by periodic-block arithmetic.
The second consumer independently constructs them by repeated doubling.
OR/AND/complement evaluate a clause/formula at EVERY one of those assignments.
Periodicity follows by induction on the bit variable index; there is no
floating arithmetic, randomized sampling, SAT timeout or symmetry quotient.

For each of the eight exact-one labelings, all residual clauses contain at
most one side literal. Let P_i mark assignments forcing q_i and N_i those
forcing not q_i. An extension exists precisely outside P_i intersect N_i
for all six sides. This existential elimination accounts for ALL 64 side
assignments. The generator obtains P_i,N_i from paths; the second consumer
gets them directly from the published residual clauses. Their complete counts
agree. Domains are fixed at six vertices and twenty orientation variables.

Total orientation assignments: 1,048,576.
Total direction/label pairs: 8,388,608.
Orientation tables satisfying the orientation clauses: 11,904.
Those with at least one two-label extension: 6,464.
Extendible direction/label pairs: 15,952.
For color codes 000 and 111: 176 directions each.
For each of the other six color codes: 2,600 directions.
Hence 15,600 pairs actually use both labels.

These counts do not assert that all 11,904 or 6,464 direction tables are
realizable. What is complete is Boolean enumeration of this precisely frozen
NECESSARY system. In particular no universal 'all planar guarded systems are
SAT' theorem follows from this one test.

Minimum is defined by the tuple (orientation integer, color integer, side
integer), with increasing variable indices as little-endian bits. It is
(0,0,0). All twenty orientation bits are false, z=(1,0,1,0,1,0), and all six
q bits are false. Every clause is directly evaluated again against the model.
This is not a claim of minimizing an unspecified solver order or graph size.

## 6. A concrete geometric counterexample to the proposed lower bound

Let p_i=(i,-i^2), i=0,...,5. For i<j<k the orientation is
-(j-i)(k-i)(k-j)<0, so these points realize the minimum orientation table.
Take the following polygon vertices in boundary order:

(49/100,2), (451/100,2), (451/100,-2051/100),
(449/100,-2051/100), (449/100,1), (251/100,1),
(251/100,-651/100), (249/100,-651/100), (249/100,1),
(51/100,1), (51/100,-51/100), (49/100,-51/100).

This is one horizontal rectangular bar with three pairwise disjoint downward
fingers, attached on disjoint boundary intervals. Its boundary is the listed
simple orthogonal cycle. Simplicity also follows by reading its rectilinear boundary: the three
finger x-intervals are disjoint and attach only to the same top bar. The
final published runner does not claim a general polygon-boundary checker.
The three nonedge midpoint witnesses are (1/2,-1/2), (5/2,-13/2), (9/2,-41/2).
They lie strictly inside the fingers, 1/100 above their bottom sides.

For an analytic edge-clearance check, write q=a+1/2 for a=0,2,4. Inside the
finger, |x-q|<=1/100. Any graph edge spanning this x has integer endpoints
i<=a,j>=a+1, but cannot be the missing pair (a,a+1). Thus
(x-i)(j-x)>= (49/100)(149/100)=7301/10000. The chord is
 y=-x^2-(x-i)(j-x).
Since x+q<=901/100, x^2>=q^2-901/10000, hence every such graph edge has
 y<=-q^2-64/100.
The finger bottom is -q^2-26/100, giving a gap of at least 38/100.
The top bar has y>=1, while every graph edge has y<=0. Graph points have
integer x and y<=0, so are in neither bar nor fingers. This proves closed
edge and point avoidance and strict nonedge blocking, without image judgment.
The graph is noncomplete, so zero obstacles cannot represent it; the displayed
counterexample makes this template's obstacle parameter exactly one.

The already-published C27 fiber dependency also reconstructs the entire free incidence: 23 components,
with all three target sets equal to the exterior singleton {0}. Twenty-three
components do not mean twenty-three obstacles are needed. The minimum is
one because only that component is needed to hit all targets.

## 7. Why more complete port-ring modules cannot rescue this family

For t>=3 let R_t have distinct two-point groups A_i and all four edges
between consecutive groups in the cycle C_t, with no other edges.
It is simple, connected, has n=2t and e=4t; each edge lies on its module's
4-cycle, so no bridge occurs. For t=3 it is the graph just handled.
For t>=4 it has no triangle: a triangle would need three distinct groups,
each pair adjacent on C_t, which does not happen. If it were planar,
Euler and face lengths at least four would give e<=2n-4. But e=2n.
Therefore R_t is nonplanar for every t>=4.

The only planar member with at least three modules is consequently R_3,
which has the explicit one-obstacle representation above. This is a complete
failure result FOR THIS EXACT saturated cyclic K2,2-port construction. It is
not the already-known C26 X4-copy barrier, and not a conclusion about all
three-module constructions or all planar graphs. The packet includes a new
failed-route proposal; it does not append the protected failed-routes ledger.

## 8. A new executable rank-three continuation, with two colors really used

Use the exact C18 drawing as a control, not as an abstract-graph lower bound:
points (-20,0),(0,20),(20,0),(0,-20),(1,8),(-2,-7),(30,1),
edges 01,12,23,03,02. The final replay through C27 Fiber, without importing
C20/C21/C25 arrangement code, gives three components. For selected targets
s0=45, s1=46, s2=56, s3=16 it returns

J0={1,2}, J1={0,2}, J2={0,1}, J3={0}.

The only minimal empty PAIR is {s0,s3}. It admits eight of the 16 labelings,
all using both labels. The additional minimal empty TRIPLE {s0,s1,s2} gives,
for each r, the clause

not z_(s0,r) OR not z_(s1,r) OR not z_(s2,r).

It excludes color codes 7 and 8, leaving codes 1,3,5,10,12,14. These six
are exactly the labelings whose every color class has a common component.
In code 7, the first three targets have color 1 and the last has color 0.
Every same-color PAIR has a component, but color 1's total intersection is
empty. It is a real geometric false positive of even COMPLETE pair-incidence
constraints, so a fortiori of the weaker pair-key constraints. No orientation
unrealizability is needed to produce this gap.

This is minimal in number of selected targets for a monochromatic-triple
failure with both labels actually used: three targets in one color require
at least a fourth in the other. It is not a minimal graph theorem.
rank3-control.json stores the rational input, incidence, all label lists,
explicit z indices and guarded empty-set clauses. The full C18 graph's
65,536 labelings are also checked and none represents it with two obstacles
AT THAT DRAWING; this is only a regression control. The four-target slice
itself is representable by two components, not a three-obstacle lower bound.

A triple clause is valid only after proving that its three targets cannot
meet one component. For this fixed drawing the final C27-based replay checks that fact.
For the root, one must obtain a chart-uniform implication over every real
placement, or cover all realizable charts by verified conditions. The code
has not supplied that universal hypothesis. Dropping it would repeat the
fixed-to-unrestricted quantifier error. Rank-three cuts are not claimed
complete for arbitrary inputs: minimal empty sets may have larger size.

## 9. Reused exact geometry and the blocked development source

The final replay uses the EXISTING C27 Fiber class, imported normally from
its repository-relative candidate directory. It works on finite CLOSED
segments and vertical free intervals, not infinite support-line barriers.
Its critical events, overlap/vertical handling, component correspondence and
nonedge interval completeness are already documented in C27; that theorem
and source are not duplicated here. The new tests add the octahedral model
and the four-target ternary interface.

C27 dependency path: research/artifacts/candidates/opg37357-a01-c27-fiber-guard-gluing-v1/fiber.py
SHA-256: 7209f677207695d220f7766286fdd94867f75d88a42d35b36cdfdef8d709ba35
Git blob: 1d00079aafa49149e08c13dcb5c837e886982e5d
The actual local replay bytes were checked against both identities.

During development a separate slab_geometry.py write was blocked by the
platform safety check, with no commit. Its original source was not retried,
renamed, encoded, attached or uploaded through an alternate path. Its hash
and operation are recorded in Issue #3 comment 5572877352 and execution.json.
It is NOT a published dependency, NOT used by the final runner, and NOT a
trusted receipt. Using the already-merged C27 dependency does not recover
or publish that blocked source. No files in C27 are modified.

The final numerical checks establish the specified component incidences and
exact Boolean counts. The 12-corner positive obstacle is justified by the
explicit analytical clearance proof in section 6; the final runner does NOT
claim to replay a general polygon-simplicity checker. Earlier development
outputs are superseded for reproducibility by the final published-source run.
The current C27 geometry caps and candidate assurance still apply. Timeouts,
size refusals or arithmetic failures are not mathematical NO answers.

## 10. Real execution, mutations, artifacts and continuation

Put the existing C27 directory on PYTHONPATH, then run `python -B controls.py` for the compact report;
`python -B controls.py --bundle` emits all derived data as ordinary JSON.
The six-vertex exhaustive CNF consumer, the actual C27 rational-incidence replay,
rotation/dart census, fifteen degenerate geometry controls and fifteen damaged
input/model/rotation rejections have actually run. The two color engines
use different arithmetic construction and different side-elimination inputs.
All mathematical sources are ordinary text. No source contacts a network,
starts a process, evaluates dynamic code, accesses credentials or writes files.
The control entry only prints stdout. No old C20 source is recovered or retried.

Final bounded execution identity, source/dependency/input/output digests, command, resource
limits and exit status are in execution.json. The three source files, graph,
minimum model, rank-three control and compact observations are delivered.
The complete CNF/origin and fiber tables are reproducible derived outputs of
the same command and are explicitly hashed; they are not claimed separately
stored in the repository. No full chat or hidden reasoning is saved.

Layers: T=C19 tube/Jordan/B17; A=C20/C21 plus the already-delivered C27
finite-segment consumer; P1=C22/C26 X4 lower-bound candidate, unchanged; P2=this failed port-ring
attempt and rank-three interface. P2 still requires exists G planar forall p
no two-component cover to obtain even a first lower bound three, and a family
with growing lower bounds (or a uniform upper construction) to settle Q2.
None of these quantifiers is closed by the current SAT census or PR checks.

Fresh registry research/verifiers.json remains the fixture-policy registry,
blob b93b32955eb94c3b4ee82f045f7bbb85fd900f05. There is no compatible registered
consumer invocation plus statement-faithfulness/axiom/closure receipt for this
work. Same-agent implementation diversity is not a new verifier trust domain.
The candidate request may ask for such a gate; it cannot create Evidence,
Result or Solution. Both admitted obligations remain open.

Sources/dependencies: current C22 README, C25 README, C26 growth/bridge and
Issue #3 checkpoint at the declared base. Primary prior-art scope check:
Berman et al., Graphs with Obstacle Number Greater than One, JGAA 21(6),
1107-1119 (2017), DOI 10.7155/jgaa.00452, article abstract at
https://jgaa.info/index.php/jgaa/article/view/paper452 . No source text is copied.
The small graph counterexample, finite census and direct geometry are supplied
here rather than inferred from published numerical layouts.

Reasoning audit: explicit domain/negation; separate planar rotation and obstacle
placement; every clause source and complete Boolean range; uniform margins
before GP; rational counterexample; Euler obstruction to family scaling;
finite decreasing loop bounds and resource ceilings; empty/single targets and
contact degeneracies handled; no symmetry quotient or probabilistic inference.
No publication novelty, all-signature realizability or trusted closure claimed.

best_verified_candidate: none
best_verified_result: none
best_growth_candidate: complete h2 SAT census and explicit rejection of saturated port rings;
realized rank3 clauses remove two pair-compatible, two-used-label false positives
next_obligation: a planar, nonsaturated coupled module whose empty-triple clauses
are forced for every REALIZABLE placement chart; do not reuse R_t or the
C26 copy-only relaxation as an obstacle-number growth argument
status: NONTERMINAL_CHECKPOINT
