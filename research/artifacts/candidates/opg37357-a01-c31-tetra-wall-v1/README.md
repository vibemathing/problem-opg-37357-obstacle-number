# C31: a nonleaf tetrahedral port counterplacement and a guarded Jordan-word cut

Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Candidate: candidate:opg37357-a01-c31-tetra-wall-v1
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph/DAG binding: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Issue: #3
Execution base: 1ae28cbfb434b792fafc76514afc6cd0641d7316
Primary owner: math-proof; exact finite computations support the candidate.

## 1. Outcome and quantified scope

One new eight-vertex graph was selected, with six target nonedges frozen BEFORE
screening. Its first tested placement has TWO explicit filled simple polygon
obstacles representing the WHOLE graph. This negates the proposed all-placement
obstacle-number-at-least-three assertion for this graph, rather than showing only
that a relaxed CNF is SAT. It is the counterplacement branch of the requested
atomic obligation. No candidate remained after this screen for stage-two universal
lower-bound analysis. No enumeration of all order types is claimed or needed to
verify this existential counterexample. The graph's exact obstacle number is not
claimed: it may have a one-obstacle placement elsewhere.

From the SAME first model we extract a genuinely ternary restriction missed by
the complete key-path relaxation. Three real graph triangles provide a direct
Jordan separation certificate. We prove its validity throughout a 129-sign real
semialgebraic region, including eleven zero signs. This is a universally quantified
GUARDED lemma, not a universal claim that all placements lie in that region.
A graph-automorphism relabeling of the actual polygon representation demonstrates
why the guard cannot be removed. This symmetry control is not another graph search.

C27's star/gluing audit, the diamond supplement PR35, C28's eight connectors and
C29's 27 prism interfaces are not re-enumerated. The prior local leaf-port argument
(core with at most one nonedge plus leaves) is also not this construction: every
new port here has degree THREE. The protected failed-route ledger was empty at
the audited base; prior failures are candidate-local proposals, not missing facts
to be rediscovered. No previous candidate or protected record is modified.

## 2. Frozen graph, six targets and abstract planarity

Let core vertices be 0,1,2,3, with all six K4 edges. For each i=0,1,2,3 add port
4+i adjacent to each core vertex OTHER THAN i. There are no port-port edges.
The complete edge list is

    01 02 03 05 06 07 12 13 14 16 17 23 24 25 27 34 35 36.

Complete nonedges, in Boolean variable order, are

    04 15 26 37 45 46 47 56 57 67.

The six initially selected targets are 45,46,47,56,57,67. The four remaining
nonedges are also retained in EVERY visibility and CNF test. Degrees are
6,6,6,6,3,3,3,3: this is not a leaf-port extension. Minimality among all possible
nonleaf couplings is not asserted.

For an abstract sphere embedding, start with a tetrahedral K4 and put port 4+i
inside the face opposite i, joining its three boundary vertices. The four open
faces are disjoint, so these operations give a simple planar graph. Orient the
original faces as 021,013,123,203. Replacing each face by three gives the twelve
oriented triangular faces in input.json. A matching rotation is

    0:1,6,3,5,2,7      1:0,7,2,4,3,6
    2:0,5,3,4,1,7      3:0,6,1,4,2,5
    4:1,2,3            5:0,3,2
    6:0,1,3            7:0,2,1.

With predecessor-of-reversed-dart convention, the consumer checks all 36 darts,
connectedness, the exact twelve face cycles, and 8-18+12=2. This is a certificate
of ABSTRACT planarity, never a premise that a visibility drawing has this rotation.
In fact the explicit obstacle drawing below has 27 proper crossings of graph-edge
pairs. Those crossings are allowed, not defects to eliminate.

## 3. Direct two-filled-polygon counterplacement

Place p_i=(i,-i^2), 0<=i<8. For i<j<k,

    D(i,j,k)=-(j-i)(k-i)(k-j)<0,

so the vertex placement is injective and in general position. The first closed,
filled obstacle is the simple polygon with boundary vertices in this order:

    (77/20,-6159/400), (33/8,-3327/200), (33/8,-169/10),
    (17/4,-189/10), (5,-249/10), (21/4,-583/20),
    (6,-359/10), (49/8,-409/10), (25/4,-843/20),
    (7,-489/10), (7,2), (33/8,2),
    (33/8,-3323/200), (77/20,-6151/400).

The second is the closed square

    (349/100,-1601/100), (351/100,-1601/100),
    (351/100,-1599/100), (349/100,-1599/100).

The polygons are disjoint: the first has x>=77/20, whereas the second has
x<=351/100<77/20. Their corner counts are 14 and 4. The following strict interior
hits use (1-t)p_a+t p_b for the increasingly ordered nonedge ab:

    target  04     15   26   37     45   46   47     56   57   67
    t       31/32  5/8  3/8  25/32  1/2  1/8  23/30  1/2  1/6  1/2
    label   0      1    1    0      0    0    0      0    0    0.

witness_check.py uses rational determinants, exact closed-segment intersection,
and winding number; it does not import the component algorithm. It checks all
79 nonadjacent polygon-side pairs, nonzero adjacent turns/area, all 16 graph-point
exterior tests, all 324 graph-edge/polygon-side pairs, and the ten strict hits.
A polygon with these simplicity tests is a Jordan polygon. A graph edge with an
exterior endpoint cannot enter its filled region without meeting its boundary,
so the edge/boundary exclusions certify the ENTIRE closed edge, not sampled points.
Every nonedge has an interior hit. These finite exact checks establish the stated
visibility pattern at the candidate level, independently of any general tube
construction or incidence-to-polygon conversion.

Thus the new graph has a candidate upper witness obs(G)<=2. At this particular
placement its minimum connected-component cover is exactly two (section 5), but
this does NOT establish obs(G)=2 after minimizing over all placements. All six
originally selected port-port targets use obstacle 0, directly invalidating the
proposed target-capacity forcing for this graph.

## 4. Complete guarded key-path necessary formula

For any finite injective placement let K be all graph points and CLOSED graph
edges. Every connected obstacle avoiding K lies in one component of the open
set R^2 minus K. Each open component is polygonally path connected. Assign each
nonedge to ONE hitting obstacle; this loses no representation even if both hit it.
For each used label, choose its finite interior segment hits and join them by
polygonal paths in that component. The resulting compact union T_r has positive
d_r=dist(T_r,K). Its closed d_r/4-neighborhood avoids K and contains all chosen
hits in its interior. Keep these neighborhoods fixed while moving endpoints by
eta<min_r(d_r/8), also smaller than a quarter of the minimum vertex separation.
Every closed edge retains clearance, and each nonedge hit moves by at most eta
when its interpolation parameter is held fixed. Only THEN choose GP endpoints
in the nonempty safe coordinate box. This proves existence at some GP placement
from a hypothetical arbitrary one. It does not preserve any specified guard
region, and does not assume an arbitrary connected obstacle is itself a path.
These broader connected neighborhoods suffice for a necessary lower-bound system;
the direct polygons in section 3 do not depend on their polygonal conversion.

At GP placements use variables 1..56 for D(i,j,k)>0, increasing triples in
lexicographic order; odd permutations negate a literal. Variables 57..66 are
one label bit z_s per nonedge in section 2 order, with False=obstacle 0. Variables
67..156 are one side per ordered pair of distinct nonedges, lexicographic pair
index order. A side is shared by all paths for that ordered pair.

Four-point rules are necessary from

    D(b,c,d)=D(a,b,c)+D(a,c,d)+D(a,d,b).

Five-point rules are necessary from

    D(a,b,d)D(a,c,e)=D(a,b,c)D(a,d,e)+D(a,b,e)D(a,c,d).

If the four right factors are positive, the two nonzero left factors have equal
signs. All ordered four- and five-tuples are included. These are NECESSARY rules,
not a real order-type realizability decision procedure.

For nonedges ab and cd, and graph path P from a to b, let
C=(x_cdv : v in P except c,d) and J=(x_abv : v internal to P). The four rows are

    OR C     OR not side OR OR J;
    OR C     OR side     OR OR not J;
    OR not C OR not side OR OR J;
    OR not C OR side     OR OR not J.

Why one side exists for targets meeting the same free component: if opposite
choices were forced, two cd-key paths would have all internal vertices strictly
on opposite sides of ab. Subdivide graph-edge crossings and erase loops to get
two simple arcs in those opposite halfplanes, intersecting only at a,b. Their
union is a Jordan curve in K with the whole open ab in its bounded region.
The two key paths lie in the SAME closed halfplane of cd: they share an endpoint
not in {c,d}, and GP makes its sign strict. The bounded Jordan region misses the
line cd; open cd also misses the curve, since a graph edge in that halfplane can
meet the line only at c/d or be the absent edge cd. A polygonal path in a common
free component from an ab hit to a cd hit would have a first exit across this
Jordan curve, contradicting avoidance of K. Crossing graph edges do not change
this argument. This is the C26/C27 pair-local implication, not an X4 calculation.

Every row R above is guarded by same obstacle assignment:

    (z_s OR z_t OR R) AND (not z_s OR not z_t OR R).

When labels differ both are true; when they agree precisely the appropriate
copy is active. Paths use all labels with no repeated vertex, up to SEVEN edges.
DFS and a separate internal-permutation census agree on 1,290 paths:
99 for each of 04,15,26,37, and 149 for each port-port target. The 108,000 raw rows
normalize to 24,012 clauses: 140 four-point, 4,480 five-point, 19,392 guarded key.
There are 156 variables. Every surviving row has a tuple/path/label/mode origin,
reconstructed by a second parity/index calculation. This checks every produced
row; complete generation follows the explicit loops and dual path census, not a
claim that this source consumer is a trusted general completeness verifier.

At the displayed real directions ALL 1,024 label words were tested. Sides were
eliminated exactly using residual unit forces; the 16 passing label words are

    6,7,14,15,70,71,78,79,944,945,952,953,1008,1009,1016,1017.

The displayed witness uses word 6. Its FULL signed 234-variable assignment after
adding component selectors is in observation.json; its prefix satisfies every
original clause. No global lexicographic minimum or 2^56-direction enumeration
is claimed. The unfixed-direction relaxation is SAT because this actual full
assignment exists, not because finite failures imply an all-placement conclusion.

## 5. Actual common-component selectors, not independent per-target choices

The unchanged byte-pinned C27 Fiber implementation produces 39 free components.
In nonedge order the COMPLETE incidence sets are

    04:0,3,13,14,24,29,35     15:7,11,14,24,38
    26:17,20,22,24,34        37:0,24,25,27,29,34,37
    45:0                    46:0,35,38
    47:0,34,35,37,38         56:0
    57:0,34,37              67:0.

They agree with the initial exact plane-subdivision screening implementation.
The full C27 event/fiber/interval report was emitted locally with --fiber. Components
0 and 24 cover all targets. Because J_45={0} and 0 is absent from J_15, one
component cannot cover everything at this placement. This fixed optimum is two.

Introduce one-hot y_(r,U) for each label r and all 39 actual components, and add

    z_s OR OR_(U in J_s) y_(0,U),
    not z_s OR OR_(U in J_s) y_(1,U).

The component sets are supplied by the SAME placement, not unconstrained SAT
objects. An unused label may pick any component; repeated selections are allowed.
There are 78 extra variables and 1,504 extra clauses, giving 234 variables and
25,516 clauses before fixing the 56 direction bits (25,572 with their units).
Enumerating all 1,024 label projections and all 1,521 component pairs by two
methods gives eight compatible label/selector assignments:

    6,7,14,15,1008,1009,1016,1017.

The eight other key-path models are false positives for whole-color-class
incidence at these coordinates. This is not an all-real coordinate solver.

## 6. New symbolic triangle-wall certificate extracted from the first model

The targets 15,26,47 have pairwise intersections {24},{38},{34}, respectively,
but empty total intersection. Use the three actual graph triangles

    C0=013, C1=035, C2=036.

For a point avoiding these triangle boundaries let its word be its three strict
inside/outside bits. Each triangle is Jordan in any GP straight placement; its
edges need not form faces of the complete drawing. A connected free component
has one constant word, because crossing one triangle's boundary would hit K.

For the displayed coordinates, cutting each target segment at the triangle edge
SUPPORTING-line crossings gives these sets of possible words on open intervals:

    W15={010,011,100},
    W26={000,001,011,100},
    W47={000,001,010}.

These are conservative supersets of the words attained by true free nonedge
pieces; other graph edges may remove pieces but cannot create a missing word.
There is no word common to all three, although every pair shares a word. Hence
no actual free component can meet the three targets. A free point at a discarded
support-line cut has a small free ball and a neighboring segment interval with
the same triangle word, so sampling all open intervals omits no feasible word.

### An explicit guard that makes this a theorem for a region of REAL placements

There are seven distinct wall edges: 01,03,05,06,13,35,36. For each target uv and
wall edge e=ab define polynomial quantities

    A_e=D(a,b,u), B_e=D(a,b,v), H_e=A_e-B_e.

Along uv its line test is A_e-t H_e. Record the signs of A_e,B_e,H_e for each of
seven edges and the signs of

    N_ef=A_e H_f-A_f H_e

for every unordered pair of wall edges. Also record the three triangle orientation
signs. In total this is 3+3*(3*7+21)=129 evaluated signs of degree at most FOUR.
The ordered sign vector is frozen in input.json; jordan-certificate.json contains
every polynomial origin and the interval/word certificate as non-executable data.
Eleven signs are zero and are retained.

Let Gamma(p) assert equality to this complete sign vector. For any REAL GP
placement satisfying Gamma, A,B,H signs determine whether each supporting-line
root t=A/H is in (0,1), is an endpoint, or lies outside; H=0 is a constant test.
A=B=0 for a target and wall edge is excluded by GP and the distinct nonedge/edge
identities. Signs of N_ef together with H_e,H_f order all pairs of finite roots,
including equal roots. On each ordered interval, the signs of A-tH are fixed by
these data. The triangle orientation signs convert those edge tests to inside
bits. Thus the sets W15,W26,W47 are precisely the same throughout Gamma, even
though their numerical crossing parameters vary. This proves the guarded lemma
without calling C25's entire signature decoder or assuming straight-line edge
crossings are governed by an abstract planar rotation.

Consequently, for EVERY real GP p and any connected-obstacle labeling at p,

    Gamma(p) -> (z15 OR z26 OR z47)
                AND (not z15 OR not z26 OR not z47).

These are variables 58,59,63. Appending the two consequences at the frozen
placement removes exactly the eight false positives of section 5, leaving its
eight genuine component-cover labelings. This still leaves the actual word-6
representation and is NOT an obs>=3 proof. The guard region is not asserted to
cover all placements or all realizable order types. Robust GP regularization in
section 4 does not put an arbitrary representation inside Gamma.

## 7. An ACTUAL representation rejects unconditional globalizing of the cut

The permutation sigma=(0 1)(2 3)(4 5)(6 7) is a graph automorphism. Set
p'_v=p_sigma(v), retain both exact polygons, and transport the nonedge-hit data.
If an increasing target reverses its mapped endpoints, replace t by 1-t. The
polygon checker accepts this complete relabeled representation. Now targets
15,26,47 map to old 04,37,56 and are ALL assigned obstacle 0. Their proposed
unguarded ternary cut is false in a real two-polygon representation of the SAME
labeled graph. The guard signs change, as explicitly checked. This rules out
mistaking one real-region exclusion for an unrestricted geometric law.

## 8. Execution, provenance and replay boundary

Four new math sources executed locally using rational/integer arithmetic, JSON
stdin and stdout. No new source imports a C22/C26 generator. The polygon checker
has no arrangement import. C27 Fiber was reused unchanged by path/hash, not
republished. Its SHA-256 is
7209f677207695d220f7766286fdd94867f75d88a42d35b36cdfdef8d709ba35.

PUBLICATION GAP: witness_check.py and guarded_cnf.py were accepted by GitHub.
The subsequent jordan_words.py create_file request was blocked by platform safety,
with no commit. It was not retried by another name, encoding, blob, tool or source
attachment. replay.py was not uploaded afterward because its complete local run
depends on that missing module. Both executed source hashes remain in execution.json;
a hash is NOT source delivery. This package is not a repository-only replay of the
full incidence/Jordan/mutation suite. The non-executable proof and complete numerical
certificate remain available for direct audit; they are not an encoded source dump.

The two explicit polygons ARE separately replayable from the delivered sources:

    python -B witness_check.py < witness.json

A standalone bounded execution of this command also exited zero; its exact run
is separately recorded. The delivered CNF source can be invoked on the complete
input graph without importing the missing source:

    python -c "import json; from guarded_cnf import build,dimacs; print(dimacs(build(json.load(open('input.json'))['graph'])),end='')"

The command above is a repository reproduction instruction, not a claim that a
new repository-side computation took place. Five earlier local replay modes were
report, --cnf, --origins, --fiber and --guard. Their complete outputs and executed
hashes are preserved, while their full driver is publication-pending.

All five final commands actually exited zero on CPython 3.13.5. Each command was
externally capped at 35 CPU seconds, 40 wall seconds, 512 MiB, one worker and
4 MiB output. Full elapsed times, output sizes/digests, input/source hashes and
exploratory repairs are in execution.json. The report rejects 18 mutations,
including deletion of an ACTUAL z guard, flipped orientation/root-order signs,
removed equality signs, nongraph walls, false profiles, malformed paths/rotation,
polygon self-crossing, vertex contact, and an interior-hit error. A mistaken
initial t=1/18 for target 47 was corrected to23/30; that bad hit remains a mutation.
No timeout or source-transfer problem was treated as a mathematical negative.

Complete deterministic outputs actually emitted:

    complete.cnf: 830986 bytes
    ec3fad6534f15d8d584ed70de1cdb0b30d4bf2a159fa31ff778fde6481298003
    clause-origins.jsonl: 1195942 bytes
    acb8e8bf3597f184d6d97431428d370d9c85a536f47bd54a7fba2203495e1718
    fiber-report.json: 35765 bytes
    653ff1e65f005074ebb80bf0aab78d2c2f8ee4bebde25426df00a186241d031a
    jordan-guard-complete.json: 26297 bytes
    70e983b8547353bb75df0f842b8c1d33ce509231f94a86acc9497add9d2f25d0

These are actual local output caches, not additional repository files. The CNF
is regenerable from the delivered compiler. The origin cache exceeds the per-file
repository limit and its original flat emitter is part of the unpublished driver;
do not claim a repository-only flat-cache replay. The local data package retains
these cache bytes, but excludes the blocked source and its full driver. The compact
jordan-certificate.json preserves the same parsed certificate as the pretty-printed
--guard output, with a separately computed byte hash.
Code diversity, finite tests, CI and PR merge are not a trusted verifier receipt.
Universal code correctness and natural-language proof acceptance remain open.

## 9. Precise failed route and next atomic obligation

Reject only the proposed all-placement lower bound for the full eight-vertex
four-face degree-three-port tetrahedral coupling (and its isomorphic relabelings).
The two polygons also reject a capacity premise limiting one component to two of
its six frozen port targets: obstacle0 already hits all six. This does not exclude
all stacked triangulations, arbitrary other nonleaf couplings, or the planar root.
A precise failed-route PROPOSAL is in this packet; the protected ledger is not
edited. Do not enumerate this seed or its isomorphs again as an obs>=3 candidate.

The next graph must be genuinely different, not another star, diamond, prism
connector or this tetrahedral face-port seed. Apply the Jordan-word compiler to
its actual cycle walls and frozen nonedges. A lower-bound certificate must cover
ALL relevant real semialgebraic regions after safe regularization, or rule out
the remaining feasible regions; otherwise retain an explicit counterplacement.
Three-point order-type signs alone are not substituted for the higher crossing-
order predicates. The first open bridge is still this all-placement region cover,
not another fixed-incidence obstruction.

Dependencies: C26/C27 key-path necessity and robust perturbation; C27 exact Fiber
for the fixed-incidence comparator; polygonal Jordan separation proved in the
special triangle/polygon settings above. C29's fixed K4 cover3/fractional2 example
is prior context, not an all-placement premise. No novelty claim is made for the
obstacle number of this small graph. C19 tube/corner bounds, C22 X4 contradiction,
and root unbounded graph-order questions are unchanged and were not rerun.

The registered policies at the audited base are fixtures, not a compatible trusted
geometric/closure invocation. No EvidenceLink, Result or Solution is produced.
best_verified_candidate: none
best_verified_result: none
source_publication_gap: jordan_words.py blocked; replay.py not uploaded
best_new_candidate: explicit two-polygon counterplacement plus guarded Jordan-word lemma
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
status: NONTERMINAL_CHECKPOINT
