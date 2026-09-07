# C29: exhaustive two-label prism interfaces and a ternary integer-cover gap

Candidate: candidate:opg37357-a01-c29-prism-rank3-v1
Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Primary owner: math-computation
Repository: vibemathing/problem-opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Base: f09892bdb8e26edcdfc80edacc2790de904a70ea
Issue: #3

## 1. Outcome and fresh-state separation

All 27 specified three-module prism-completion necessary h=2 formulas are SAT.
This rules out those formulas as all-placement obstruction certificates; it is
NOT an obstacle-number bound for all planar graphs. A new exact six-target/four-
component profile has integer cover three, while its pairwise incompatibilities
admit eight two-label models and its fractional weighted bound is only two.
Four ternary clauses remove every one of those eight models. That profile is
realized at a specific rational drawing, not forced at all placements.

Fresh main already contained C27. A separate C28 octahedral draft was advancing
on its own branch during this turn. Its existing sources were read, byte-matched
and replayed, but NONE was modified or retransported here. This C29 branch holds
only the new prism family and six-target profile. Source docstrings retain their
pre-publication development tag C28: exact executed bytes were not changed merely
to rename comments. The candidate identity, paths and packet are C29. C22/C25/C26/
C27 and the single Issue #3 are reused. No X4 CNF, old RUP or failed copy-only
amplification is repeated.

## 2. One quantifier order

For an injective placement p of finite simple G, let K(p) be all vertex points
and CLOSED graph-edge segments, F(p)=R^2 minus K(p), and J_s(p) the free components
meeting the relative interior of nonedge s. The exact connected-obstacle interface
for at most two obstacles is

  exists p, exists U_0,U_1 in components(F(p)), exists z:nonedges->{0,1},
  for every s: U_(z(s)) belongs to J_s(p).

The finite nonedge witnesses and polygonal connecting paths inside each selected
U_r are existential AFTER p,U,z. Components and incidence must arise from this
same p; they are not free abstract objects. Unused labels are allowed, repeated
components can be merged, and F(p) is nonempty. C20/C27 supply the fixed-component
argument; C19 separately supplies simple-polygon conversion and corner bounds.

To derive GP Boolean directions from any hypothetical representation, first use
C26/C27's robust replacement, not density alone: finite path unions T_r have
positive d_r=dist(T_r,K); thicken by epsilon_r=d_r/4. A single movement
eta<min_r(d_r/8), also below a quarter of the vertex separation, preserves every
closed-edge clearance and every nonedge hit at its fixed interpolation parameter.
Only then select GP points in the safe open coordinate box. Initial tangencies,
collinear vertices, overlapping supports and unbounded obstacles do not warrant
turning a zero determinant into a Boolean sign. Crossed graph edges remain allowed.

The necessary finite implication is

  geometric two-obstacle existence -> exists chi,z,side: Phi_(G,2).

Chi consists of GP vertex-triple signs. Its necessary axioms do not decide real
realizability. SAT does not construct coordinates or components; UNSAT would need
this geometric implication to obtain a graph lower bound. C25's quartic signature
realizability and the unbounded graph-order root quantifier are not eliminated.

## 3. Minimal seed within a declared template and all 27 planar completions

Use disjoint two-vertex columns (0,3),(1,4),(2,5). Three C4 modules are the cycles
0143,1254,2035. Complete edge list: 01,02,03,12,14,25,34,35,45.
Complete nonedge list: 04,05,13,15,23,24.
The rotation system is

  0:1,2,3   1:0,4,2   2:0,1,5
  3:0,5,4   4:1,3,5   5:2,4,3.

Its oriented faces are 021,345,0143,1254,2035; every dart occurs once and
6-9+5=2. The three lateral quadrilaterals form a cylinder capped by two triangles,
so this is an explicit sphere embedding. In each quadrilateral independently
choose no diagonal, its first diagonal or its second: exactly 27 ternary codes
0..26, not all planar graphs or all planar supergraphs. There are 1,6,12,8 cases
with 9,10,11,12 edges respectively. Six vertices is minimal ONLY for the chosen
three-disjoint-two-vertex-column template, not a global obstacle-number minimum.

All 27 have the explicit plane drawing
  p0=(0,0),p1=(12,0),p2=(0,12),p3=(2,2),p4=(8,2),p5=(2,8).
Each added diagonal stays in its own convex quadrilateral face. Face interiors
are disjoint, so selected diagonals cannot cross. Every added pair was a nonedge,
so the graph stays simple. The code also checks every disjoint-edge pair, every
vertex/nonincident-edge contact, and all rotations. This drawing is used ONLY
for planarity, not as the obstacle placement or a restriction on placements.

The seed has 54 simple nonedge paths of lengths two through five; ALL are retained.
Forty-two are not contained in any single module. Source records list every path
and each edge's module membership. Clauses couple ordered target pairs across
modules, not merely separate local demands that each require two labels.

## 4. Guarded CNF and a separate clause consumer

For the seed, variables 1..20 are increasing triple orientations. Odd permutations
negate the corresponding literal. Variables 21..32 encode z_(s,r), in lexicographic
nonedge order then r=0,1. For each s use (z_s0 OR z_s1) and
(not z_s0 OR not z_s1). Variables 33..62 are separate side choices for all ordered
pairs of distinct nonedges. A label is assigned to ONE obstacle, not a fresh
component chosen independently for each nonedge.

Every ordered quadruple contributes
  not chi_abc OR not chi_acd OR not chi_adb OR chi_bcd.
For every ordered quintuple put
  A=not chi_abc OR not chi_acd OR not chi_ade OR not chi_abe
and add A OR chi_abd OR not chi_ace, and A OR not chi_abd OR chi_ace.
The determinant implications are precisely C26's necessary rules, not fixed
coordinate substitutions or sufficient realizability axioms.

For ordered nonedges s=ab,t=cd and a graph path P from a to b, put
C=(chi_cdv for v in P excluding c,d), J=(chi_abv for internal vertices).
For each r add (not z_sr OR not z_tr) to EACH of
  OR C     OR not side_st OR OR J;
  OR C     OR side_st     OR OR not J;
  OR not C OR not side_st OR OR J;
  OR not C OR side_st     OR OR not J.
The same side_st works for every P for this ordered pair. Exact-one labels allow
reuse across r, because only one r can activate both guards. C26/C27's pair-local
Jordan argument applies when both targets hit the same connected obstacle or
free component. It does not impose that rule on different obstacles.

producer.py imports no C22/C26 code. It enumerates internal vertex permutations
and parity inversions. audit.py imports neither that producer nor C22/C26: it
uses a layered path census, cyclic-minimum orientation parity and the negation
of each forbidden truth assignment. It checks the COMPLETE canonical clause
set and every source, not only the plausibility of rows supplied by the producer.
The final all-simple-path seed has 62 variables and 2,106 clauses:
30 four-point,480 five-point,12 exact-one,1,584 guarded key clauses.
An earlier four-edge-only exploratory formula had 1,914; it is not the final one.

Actual emitted complete seed CNF: 56,388 ASCII bytes, SHA-256
c3e3bec408a9ef49c70b594cacbcace29f05a2adbb95dc3b36dfa1dfad7b5df2.
Actual emitted JSON formula WITH all sources and paths: 123,844 bytes, SHA-256
977708c3a8002d715c5a277cadcafa29263fc224fd92c5de341d0fdd21bd6c9d.
These deterministic output caches are regenerated by --cnf and --formula; they
are not claimed to be separately stored files. The frozen source, graph and
emitters supply the entire conditional CNF, not an unpublished prerequisite.

## 5. Complete Boolean decision and smallest models

For q orientation bits, bit j of an integer truth vector represents assignment
j in 0..2^q-1. Alternating finite blocks represent each variable, OR/AND act
bitwise, and complements are masked to exactly 2^q bits. Thus every orientation
is evaluated, not sampled. Here q=20 and 11,904 of 1,048,576 assignments satisfy
the necessary direction axioms. We do NOT claim they are all realizable.

For each fixed two-label choice, a residual key clause contains at most one side
literal. Evaluate all such clauses with that side=false and with side=true;
the union is EXACT existential elimination. Different side variables only occur
in their own pair's rows, so eliminating them separately accounts for all side
assignments without an exponential side loop. The code compares these CNF masks
with directly derived opposite-key-path forcing masks on EVERY orientation.
It then checks all 2^k valid one-hot label choices, retaining both color symmetries.
Invalid raw color-bit assignments fail exact-one clauses, not a hidden sampling
filter. A separate scalar coloring enumeration grouped by conflict-graph codes
agrees with every per-label count.

For the seed: 67,108,864 projected orientation/color assignments; 48,060 satisfy;
6,648 direction tables extend and 5,256 direction-rule survivors do not extend.
Every one of the 27 formulas is SAT. Across these labeled instances the complete
projected domain is 536,870,912 assignments, with 924,356 satisfying pairs.
This is NOT a count of geometric drawings or distinct unlabeled graphs.

family-results.json freezes all 27 codes, counts, full smallest models and CNF/
raw-output hashes. Graphs and rotations are exactly regenerated by seed.completion.
The minimum order is the lexicographic full variable BIT vector, with0 before1.
All seed direction bits are0, all six targets use label1, and label0 is unused.
Prefix masks and the first failed row for each forced-true side certify minimality.
Every final model is checked against every clause. No successful SAT result is
relabeled as a graph lower bound or as complete real quantifier elimination.

## 6. Actual geometry for the seed and remaining relaxation gaps

The smallest seed direction table is realized by p_i=(i,-i^2),i=0..5.
The pinned C27 exact finite-segment fiber core finds ten free components and
common component0 for all six targets:
  04:{0,7,9};05:{0};13:{0,3,4};15:{0,1,2};23:{0};24:{0,6,8}.
controls.json contains rational witnesses and the complete fiber output. This
is a real common-component control, not merely an abstract SAT assignment.
Connected-obstacle existence uses C20's finite path argument; simple polygons
use C19 separately. No polygon is exported or claimed for all 27 completions.
Reflection, coordinate swap and scale10^-40 controls also passed.

Other Boolean survivors still require real realizability AND one common component
for each ENTIRE color class. Pair-key constraints supply only some pairwise
incompatibilities. Even all pairwise compatibility tests can miss a whole-class
empty intersection, as the next realized control demonstrates.

## 7. New six-target ternary interface and fractional gap

Let U={0,1,2,3}; the six target incidence sets are all two-element subsets of U.
The minimal empty subfamilies are three complementary pairs and four triangles
on three component names. Pair incompatibilities form a matching, admitting
EIGHT two-label assignments. Adding the four ternary empty-intersection conditions
removes ALL eight. rank3.py checks all64 assignments and supplies for each empty
subfamily S and each U a named member of S missing U. The projected clause is
  OR_(s in S) not z_sr, r=0,1.
No abstract clause is mislabeled as a universal geometric fact.

The integer cover is exactly THREE: selecting at most two components leaves a
two-element complement, which is itself an uncovered target; any three cover
all targets. Pairwise-intersecting families of two-element sets have a common
point unless they contain a triangle, so the seven listed exclusions are complete.
The C27 weighted capacity method alone cannot certify three: summing four unit
component-load bounds counts every target twice, giving2*sum(w_s)<=4. Equal
weights1/3 attain total2. The dual fractional cover assigns1/2 to all four
components, also total2. Integer3 versus fractional2 is exact, not a float LP.

A rational geometric realization exists at ONE drawing. Draw K4 at
(0,0),(12,0),(0,12),(3,3). For each edge ab let m=(p_a+p_b)/2 and
v=(-(y_b-y_a),x_b-x_a)/100. Add isolated graph points m-v,m+v and select their
nonedge. There are16 graph points but only the6 K4 edges. Each selected segment
crosses precisely its chosen edge near its midpoint. A radius-one midpoint ball
misses every other K4 edge and endpoint; each offset has norm<1. Its two sides
therefore lie in the two adjacent faces. Finite punctures do not split those
open faces. The six adjacent-face pairs of this plane K4 are all pairs of its
four faces. Exact C27 replay confirms the incidence and complete target intervals.

This is only SIX SELECTED TARGETS at ONE FIXED drawing. It is not the optimum
for all114 nonedges there, and not obs>=3 for the abstract graph. Nothing forces
the twelve isolated vertices to those faces at every placement. Supplying such
placement-universal coupling, without breaking simple planarity, is now the gap.

Generally, eliminating a component selector for each label yields all minimal-
empty-subfamily monochromatic exclusions. Every minimal empty family has size
at most the number of components: choose, for each component, one target omitting
it; these already have empty intersection, so minimality forbids a larger family.
This is NOT a universal rank-three bound. The exact finite audit checks all4-target
profiles on3 components (4,096 profiles and65,536 two-label assignments), including
empty incidence sets; rank<=3 projection agrees with direct component selection
in every case. The fixed4-component/six-target example is separately checked.

## 8. Execution, source safety and reproduction

Sources are ordinary UTF-8 memory operations plus JSON/text stdout: no network,
subprocess, dynamic evaluation, secrets or file writes. C27 fiber.py is only a
previously delivered geometry comparator, SHA-256
7209f677207695d220f7766286fdd94867f75d88a42d35b36cdfdef8d709ba35.
It is not republished. The new CNF cores share no C22/C26 implementation.

Run from this directory:
  python -B run_census.py --completion 0
  python -B run_census.py --completion 26
  python -B run_census.py --cnf
  python -B run_census.py --formula
  PYTHONPATH=../opg37357-a01-c27-fiber-guard-gluing-v1 python -B controls.py
For any code, producer.make(6,seed.completion(code)['edges']) regenerates all rows
and sources. Apply external30 CPU seconds,40 wall seconds,512MiB,one worker and
4MiB stdout per command. Actual CPython3.13.5 exact-integer/Fraction runs and
fingerprints are in execution.json. scripts/compute_plan.py was freshly requested
and returned404; the explicit local CPU route is not a fabricated planner run.

All27 final ALL-PATH censuses were actually executed. Fourteen malformed-clause,
source, path, one-hot, metadata, literal and rotation mutations were rejected;
all27 exact planar drawings and three affine controls passed. One outer long batch
reached a wall limit, was not counted as a mathematical NO, and was split into
smaller batches with per-instance persisted records. Final successful records
cover every code once. Earlier four-edge-only results are historical, not mixed
into the frozen final CNF count. Emission hashes bind the actual full output.

## 9. Failure proposal, sources and next obligation

Only these27 specified prism necessary formulas are rejected as an UNSAT route.
Do not infer all planar h=2 formulas are SAT or every direction here extends.
The failure proposal is candidate-local; protected failed-route records are
unchanged. The next target is a simple planar construction that forces a ternary
integer obstruction for EVERY real placement, or a justified universal upper
placement construction. Neither is supplied by a fixed K4-and-isolated-points
layout or the fractional relaxation.

Separate layers remain T=C19 tube/Jordan; A=C20/C27 fixed incidence; P1=C22/C26 X4
bridge/contradiction; P2=the present guarded relaxation and still-open placement-
universal growth. Neither the old X4 RUP nor original five missing C20 sources
are rerun/recovered here. No geometry-to-root closure is inferred from CI.

Primary source context, rechecked at abstract/definition level only:
Berman et al., JGAA21(6),1107-1119(2017), DOI10.7155/jgaa.00452, connected obstacles;
Gimbel/Ossona de Mendez/Valtr, arXiv:1706.06992, distinguishes ordinary obstacle
number from the crossing-free planar obstacle number. No bound for the latter is
substituted for the former; no source full text or novelty claim is supplied.
https://jgaa.info/index.php/jgaa/article/view/paper452
https://arxiv.org/abs/1706.06992

Registry inspection found no compatible trusted consumer/closure invocation.
The verifier request is not a receipt. Statement-faithfulness, universal code
correctness and both unrestricted root questions remain open. No EvidenceLink,
Result or Solution is signed or directly edited.

best_verified_candidate: none
best_verified_result: none
best_h2_candidate: full SAT census plus ternary integer-component interface
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: force or disprove the ternary pattern for all placements; do not
repeat these27 cases as proposed UNSAT obstructions. NONTERMINAL_CHECKPOINT.
