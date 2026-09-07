# C28: exhaustive two-label octahedral interface, with a realized minimum model

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Primary owner: math-computation
Base: f09892bdb8e26edcdfc80edacc2790de904a70ea
Issue: #3

## 1. Fresh-state correction and deliverable

PR #32 was already merged at this base. Its final head is
27be45a2de34eb886ebe3825c170b78dd97b8677; merge SHA is the base above.
Run 34136533643 has successful final jobs: packet 101788719885, snapshot
101788719845, diff 101788719497. Its ten additions and one packet are retained,
not overwritten, reopened or duplicated. C27 fiber.py was freshly retrieved,
byte-matched (SHA-256 7209f677207695d220f7766286fdd94867f75d88a42d35b36cdfdef8d709ba35),
and reused for new fixed-input incidence checks. C27 did not contain this
six-vertex exhaustive CNF/model. C22/C26's X4 clauses are not regenerated here.

The present finite h=2 system is SAT. Moreover its lexicographically least
Boolean model has the explicit rational single-filled-simple-polygon realization
below. Thus the octahedron is not an obstacle-number-three candidate. This is
not merely failure of a solver relaxation to decide realizability.

All eight precisely specified connector variants also have SAT assignments,
real coordinates and a common free component, as checked with C27. This rules
out THIS finite family as a growth construction; it does not classify every
possible gluing of diamonds or bound the obstacle number of all planar graphs.

## 2. Frozen graph, three modules and a plane rotation system

Vertices are 0,...,5. Complete edge list:
02,03,04,05,12,13,14,15,24,25,34,35.
Complete nonedge list in variable order: s0=01, s1=23, s2=45.

The modules are the induced diamonds on {0,1,2,4}, {2,3,0,4}, {4,5,0,2}.
Each has five edges and a different missing pair (01,23,45 respectively).
They share the central triangle 024. The three inter-tip connectors are
13,15,35. Taking any subset of these connectors gives the eight variants.
The empty subset has nine edges; the full subset is the twelve-edge octahedron.
We are freezing the octahedral alternative in the task, not identifying all
three missing pairs with one another or claiming to cover every diamond book.

Rotation lists (cyclic, successor convention):
0: 2,5,3,4
1: 2,4,3,5
2: 0,4,1,5
3: 0,5,1,4
4: 0,3,1,2
5: 0,2,1,3

The face permutation (a,b)->(b,next_b(a)) gives:
024,035,043,052,125,134,142,153.
All 24 darts occur once; there are eight triangular faces and 6-12+8=2.
More explicitly, the four triangles incident to 0 and the four incident to 1
are disks coned over the common equator 2,4,3,5; gluing them gives a sphere.
Deleting one face supplies a plane embedding. Removing any subset of the
three connector edges preserves simplicity and planarity; the restricted
rotations are explicitly checked for all eight graphs. The later visibility
coordinates need not be a plane drawing and are not used as a planarity proof.

Six vertices is the minimum number permitting THREE VERTEX-DISJOINT target
nonedges. No claim of minimum order among all planar graphs/modules is made.

## 3. Quantifiers and obstacle-component semantics

For an injective real placement p, K consists of all graph points and CLOSED
graph-edge segments. Every used obstacle is a nonempty connected subset of
R^2 minus K. Let J_s(p) be the set of free components meeting the relative
interior of nonedge s. A representation with at most two obstacles implies

  exists U0,U1, exists c_s in {0,1}, forall s: U_(c_s) in J_s(p).

The component names may repeat; two obstacles need not lie in different
components. An unused label imposes no demand. Given this finite cover,
connect chosen nonedge witnesses by polygonal paths in each selected open
component. C20 supplies that existence equivalence; C19 is a separate step
when a general polygonal disk/corner bound is wanted. The explicit polygon
in section 6 needs neither C19 nor a tube implementation.

The necessary Boolean sentence is exists x,z,q: F_G(x,z,q). Here x is the
orientation table of ONE placement shared by all modules; z assigns all
nonedges to the same two labels globally; q selects sides for ordered pairs
of distinct nonedges. For a genuine representation at a GP placement, x is
fixed by its coordinates before any q is selected. The same q must work for
ALL graph paths for that ordered pair. The C26/C27 common-component Jordan
argument supplies necessity. An arbitrary degenerate representation first
gets a compact replacement with positive edge clearance and interior hit
margins, and then one common GP perturbation; mere density is insufficient.

UNSAT of this relaxed Boolean sentence would exclude all actual placements.
SAT alone usually does not give a placement. This packet instead exhibits
coordinates AND a polygon for its minimum model. Nothing converts fixed-drawing
failure into an all-placement graph bound. The canonical root's second part
still has exists h forall planar G exists placement, with unbounded graph order.

## 4. Every variable, path and clause

x_abc for increasing triples a<b<c are variables 1,...,20, lexicographically.
x_abc means det(p_b-p_a,p_c-p_a)>0. Odd permutations negate a literal.

z_(s0,0),z_(s0,1),z_(s1,0),z_(s1,1),z_(s2,0),z_(s2,1) are variables 21,...,26.
For each target include (z0 OR z1) AND (not z0 OR not z1).

Side variables 27,...,32 correspond in order to
(s0,s1),(s0,s2),(s1,s0),(s1,s2),(s2,s0),(s2,s1).
Each means the chosen left side of the directed first nonedge. Every key
clause is cross-module because the three targets belong to different modules.

Retain all four- and five-point orientation implications from the determinant
identities, for every ordered tuple of distinct vertices. For (a,b,c,d):
  not x_abc OR not x_acd OR not x_adb OR x_bcd.
For (a,b,c,d,e), put A=not x_abc OR not x_acd OR not x_ade OR not x_abe:
  A OR x_abd OR not x_ace;
  A OR not x_abd OR x_ace.
These are NECESSARY algebraic conditions, not claimed sufficient for realizability.

For ordered nonedges ab,cd and EVERY simple graph path P from a to b, let
C=(x_cdv: v in P minus {c,d}), J=(x_abv: v internal to P), q=q_(ab,cd).
Use four unguarded expressions:
  OR C     OR not q OR OR J;
  OR C     OR q     OR OR not J;
  OR not C OR not q OR OR J;
  OR not C OR q     OR OR not J.
For EACH r=0,1 prefix EACH expression with not z_(ab,r) OR not z_(cd,r).
No side requirement between differently assigned obstacles is activated.

All simple paths are enumerated by permutations of distinct internal vertices,
including paths with FIVE edges. There is no four-edge truncation on six
vertices. Each nonedge has 28 such paths, for 84 total. The second consumer
reconstructs them by all internal-vertex WORDS and rejects repetitions and
nonedges, not by the producer's permutation method or old DFS/frontier code.
The generator imports neither C22 nor C26. Its signed clauses and per-row
sources are audited by a separate implementation. Each key origin names its
actual two nonedges, color, side variable, mode and full graph path.

After dropping tautologies and duplicates there are 1,140 clauses:
30 four-point, 480 five-point, 6 exact-one, 624 guarded key-path.
The formula has 32 variables. Raw DIMACS SHA-256:
8ff2ede8552a931ff6396381a76f5961eaa0135c5227ceb72d8fbecdcb98f4aa.
The 1,140-row source table SHA-256 is
74b15181d4c3c1b1b2924060ac528ba5d0c771692d76cbda0c5265bb7ffc7814.
Both byte streams were actually emitted, not estimated from a planned run.

## 5. Exhaustion: not an early SAT hit

The first checker treats all 2^20 direction assignments as positions in exact
integer bitsets. For EACH of the eight valid two-label assignments it substitutes
all exact-one z bits. Every remaining nonorientation clause has at most ONE
side literal. Accumulate the direction positions forcing each side true and
false. Exactly their intersection is inconsistent. This is a complete existential
elimination of the six sides, not fixing those sides in advance or sampling them.
Every bit position has its intended literal truth, by induction in the repeating
bit-plane construction; disjunction/intersection implement the corresponding
Boolean operations pointwise.

The second checker does not import the first. It branches on direction prefixes,
prunes only when a fully assigned orientation clause is false, and counts every
pruned prefix's full set of completions. At each surviving leaf it tests the
remaining 8*64 label/side assignments simultaneously in a 512-bit truth table,
using the original clauses as input. Thus it explicitly includes every side
extension, not the first checker's unit-elimination construction. It accounts
for all 2^20*512=536,870,912 direction/label/side assignments with exact-one z
already represented, and checks the complement partition of direction prefixes.

Both find 11,904 direction assignments satisfying the orientation rules. This
is NOT stated as a count of geometrically realizable drawings. Projected counts
for color strings 000,001,010,011,100,101,110,111 are
176,2600,2600,2600,2600,2600,2600,176.
The sum is 15,952 direction-label pairs. The second checker counts 807,232 FULL
satisfying assignments including sides. The first covers 8,388,608 direction-label
pairs without an early stop. Counting includes monochromatic labels because the
question is AT MOST two obstacles; requiring both labels used would still leave
15,600 projected pairs and would not rescue this proposed lower bound.

## 6. Minimum model and an actual polygon

With False before True and variables ordered 1,...,32, the minimum is
x_1=...=x_20=False; (z0,z1)=(False,True) for all three targets;
q_27=...=q_32=False. This is Boolean lexicographic minimality, not smallest
coordinates, fewest corners or a minimum graph among all possible constructions.

Take p_i=(100i,-100i^2), i=0,...,5. All increasing triple determinants are
-10000*(j-i)*(k-i)*(k-j)<0, exactly the first twenty bits. Parallel disjoint
pair lines and multiple crossings are allowed; a C25 Dstar chart is not needed.

The closed filled simple polygon has this boundary in order:
(-10,100),(49,100),(49,-51),(51,-51),(51,100),
(249,100),(249,-651),(251,-651),(251,100),
(449,100),(449,-2051),(451,-2051),(451,100),
(510,100),(510,200),(-10,200).

It is a horizontal bar with three disjoint narrow rectangular fingers. Each
finger overlaps the bar, there are no holes, and the displayed boundary is
simple. The exact checker tests all 104 nonadjacent boundary-side pairs and
all adjacent turns. All six graph points are outside. All 192 graph-edge /
polygon-side pairs have empty closed intersection. Since each graph edge has
an outside endpoint, it cannot enter the polygon without meeting its boundary.
The three nonedge midpoints (50,-50),(250,-650),(450,-2050) are strictly inside.
This proves the asserted visibility pattern directly. The polygon is connected,
bounded, closed and filled; no obstacle/graph boundary contact is used.

It realizes the minimum Boolean model using label 1 only. A harmless remote
second obstacle could be supplied if a definition insisted on listing two
nonempty obstacles; the parameter under study is at most two. The exact
C27 free-space calculation also puts all three target sets in component 0.
Because the graph is not complete, zero obstacles do not represent it. Under
the frozen polygon convention, this gives an obstacle-number-one CANDIDATE
for this particular graph, with no novelty claim and no trusted admission.

## 7. All eight connectors and the exact failed-route proposal

For connector masks 0,...,7 (bits 13,15,35), the edge counts are
9,10,10,11,10,11,11,12; nonedge counts are 6,5,5,4,5,4,4,3.
Projected direction-label SAT counts are respectively
224056,62300,62300,21248,62300,21248,21248,15952.
All their label/direction spaces were exhausted: 226,492,416 pairs altogether.
For each graph the minimum direction bits are all false and the actual points
p_i above have common free component 0. The stored compact observation gives
all edges, nonedges, rotation, minimum model, component incidence witnesses and
complete formula hashes. C27 was used only for those fixed geometry calculations,
not as the Boolean generator or second exhaustive checker.

This is a finite exact counterfamily to the proposed OCTAHEDRON / THREE-DIAMOND
CENTRAL-TRIANGLE + SUBSET-OF-TIP-CONNECTORS interface. It is not a theorem that all
possible diamond couplings are two-label satisfiable. The full octahedron has
the direct polygon; general polygon extraction for connector variants still
refers separately to C19/C20, rather than a generated tube polygon.
No fabricated missing ternary constraint is attached to the minimum model:
its nonedges already have a genuine common component. A clause declaring that
actual common intersection empty would be false, not a repair of this model.
The corresponding precise failed-route proposal is in the packet. Protected
failed-routes records are untouched. Do not repeat this eight-graph search.

## 8. Next layer: a sharp ternary target-count threshold

For any finite collection of nonempty incidence sets J_s, one label can cover
a target class exactly when its full intersection is nonempty. A certified empty
TRIPLE F={a,b,c} yields the clause not z_(a,r) OR not z_(b,r) OR not z_(c,r), for
each r. It is valid only with an actual geometric certificate (or an all-placement
topological proof), not from an abstract hypergraph or one inconvenient layout.

The selected C18 triple is replayed with C27: incidences are {1,2},{0,2},{0,1}.
All pairs intersect and the triple does not. Exactly SIX of its eight two-label
assignments survive. This cannot force three obstacles. More generally, with
at most FOUR targets, constraints forbidding monochromatic triples or larger
sets never rule out two labels: partition the targets into two groups of size
at most two. This argument covers any collection of rank-at-least-three demands,
not just the tested example, and assumes no additional pair incompatibilities.

Five is sharp at the ABSTRACT interface: forbid all ten triples on five targets.
Every two-coloring has a color class of size at least three, so all 32 fail.
An explicit set system realizing these incidences abstractly has one component
for each pair of five targets, incident only to that pair. Every pair shares a
component, no triple does, and its minimum component cover is three. No planar
graph/drawing realization of that set system is asserted; the field is null.

The next actionable all-placement lemma is therefore: construct a planar family
such that every placement has t selected nonedges and no free component meets
three of them. Then every component covers at most two, giving h>=ceil(t/2).
For the first h=2 obstruction t=5 suffices. We prove only this implication and
the sharp abstract threshold, NOT existence of the required planar family.
The all-placement topological forcing, not another abstract coloring run, is
now the open obligation. Empty individual J_s would instead mean no representation
at that drawing and must not be confused with a resource refusal.

## 9. Execution, replay and trust boundaries

From this directory, with the existing C27 directory on PYTHONPATH:
  PYTHONPATH=../opg37357-a01-c27-fiber-guard-gluing-v1 python -B checks.py
  PYTHONPATH=../opg37357-a01-c27-fiber-guard-gluing-v1 python -B checks.py --cnf
  PYTHONPATH=../opg37357-a01-c27-fiber-guard-gluing-v1 python -B checks.py --sources

The first outputs the full formula, all row sources, witness and full observation.
The latter two output byte-pinned DIMACS and the actual per-row source table.
Run externally with 30 CPU seconds, 40 wall seconds, 512 MiB address space,
one worker and 4 MiB output. All three final commands actually exited 0.
execution.json binds CPython version, source hashes, elapsed times and outputs.
The published observation is a compact summary; full stdout is a deterministic
cache, not a trusted receipt. There are sixteen rejected mutations: three stale
edge deletions, three altered key paths/targets, three flipped coordinate-bound
directions, three omitted clause families, two invalid label assignments,
a shallow finger missing a nonedge and a reversed vertex rotation.

The five new sources have no file/network/process access, dynamic evaluation,
credentials or environment reads. Checks print stdout. C27 fiber is reused by
path/hash rather than republished. The source is entirely ordinary text; no
previously rejected C20 source is recovered, encoded or resubmitted.

T (C19 tube/Jordan), A (component computation), P1 (existing X4 all-placement
bridge) and P2 (placement-universal growth) remain separate. No registered
compatible mathematical consumer or closure receipt is currently available;
fixture policies and transport checks do not supply one. A new verifier request
binds the current scope. No EvidenceLink, Result, Solution, registry, schema,
Harness, workflow or protected ledger is modified.

Source context: C26 guarded-color interface, C27 finite-segment core and checkpoint,
C25 distinction between realizability and sign consistency. For terminology,
Berman et al., JGAA 21(6), 2017, DOI 10.7155/jgaa.00452, journal abstract at
https://jgaa.info/index.php/jgaa/article/view/paper452 (retrieved 2026-09-07).
That source is not claimed to prove the new counts or this polygon. No images,
floating comparisons or external SAT solver are used.

best_verified_candidate: none
best_verified_result: none
best_h2_candidate: exhaustive SAT octahedron, realized minimum model, eight-connector finite rejection
next_obligation: five-target all-placement triple-separation, or a different uniform-upper-bound route
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
