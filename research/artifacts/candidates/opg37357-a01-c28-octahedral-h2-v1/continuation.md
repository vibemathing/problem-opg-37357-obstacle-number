# PR34 continuation: exact SAT replay and anchored common-component cuts

Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3; existing PR: #34
Fresh continuation base: 61943c788f95f91874b99b77f06b4b8c898a6db7
Owner: math-proof, with bounded math-computation support

## 1. Reuse, rather than inventing another candidate

The remote state already contains the completed C27 candidate and two open
C28 candidates. PR34 owns the octahedral package; PR33 owns the port-ring and
its two-coupling extension. The two had collided on generic C28 inbox names
and candidate IDs. This continuation preserves every original PR34 mathematical
blob and gives only its transport bindings the c28-octahedral namespace. The
old generic IDs in immutable historical prose are descriptive aliases, not
new admitted records. PR33's different files must not be overwritten.

The four PR34 source bytes replayed here were fresh-read at
 a4ac73869b14b442905f3a83d526007fc5f98b2a
and their full Git blob hashes and SHA-256 were matched before execution.
resume_check.py is a new entry point using those unchanged files. It does
not rerun the C27 fiber core, the original checks.py entry or PR33's extension;
those older execution records retain their own explicitly different scopes.

## 2. What the SAT witness settles

The graph has vertices 0,...,5 and complement {01,23,45}. Three induced
K4-minus-edge modules have vertex sets {0,1,2,4}, {2,3,0,4}, {4,5,0,2};
connectors are 13,15,35. Their union is simple, planar, and uses three disjoint
nonedge ports. Six vertices is minimal for that specified disjoint-port
requirement, not a theorem of global minimum order among all module designs.
The stored rotation has eight triangular face orbits and Euler value two.

For a hypothetical representation the quantifiers are:
there exist injective real coordinates p, at most two connected obstacles,
for every nonedge s a chosen label r and an interior hit in the component of
that obstacle, then orientation variables and per-ordered-pair side variables.
After robust regularization as in C26 the direction signs are nonzero. For
pairs assigned the same label the key-path clauses apply. For different
labels they are guarded off. No component membership is asserted merely
because two Boolean labels are equal; that implication belongs to a real
representation, not arbitrary satisfying assignments of the relaxation.

The new run checks every origin for the complete 1,140-clause formula:
30 four-point, 480 five-point, 624 guarded key-path, six exact-one-label clauses.
There are 32 variables: twenty orientation bits, six assignment bits, six
side bits. All 84 simple paths are retained, including five-edge paths.
No C22/C26 generator or C21/C25 geometry is imported.

Two methods agree on 15,952 projected direction-label models and 807,232
complete direction-label-side models. They cover all 2^20 directions and all
eight labels; the second method partitions all 536,870,912 direction/tail
completions, rather than testing a collection of sampled directions. This is
Boolean exhaustiveness, not enumeration of all real coordinate realizations.

The least model, False before True in variable-ID order, makes 1..20 false,
21,23,25 false, 22,24,26 true, and 27..32 false. Its exact placement is
p_i=(100i,-100i^2). The previously stored 16-corner single filled polygon passes
192 closed graph-edge/obstacle-side tests, 104 nonadjacent obstacle-side tests,
all graph-point exclusions, strict nonedge midpoint tests, and the rotation
check. Sixteen damaged inputs are rejected. All eight connector-mask formulas
were also replayed as SAT; this entry does not repeat their old fiber geometry.

Thus the saturated graph is not an obstacle-number-three candidate: it has
an explicit genuine one-obstacle representation. There is no missing faithful
geometric condition that could eliminate THIS minimum model. General SAT
survivors still need real realizability, complete incidence, and a common
component for each chosen label. Neither SAT nor the count is itself a proof
that every survivor has coordinates.

## 3. A more targeted rank-three growth interface

Let C be a nonempty finite set of free components and let J_s subset C be
complete incidence sets for ALL nonedges of a fixed drawing. Empty J_s are
permitted and represent infeasibility. Put

 M_u = {s : u not in J_s},     R_u = intersection over s in M_u of J_s,

where an empty intersection is C. Then

       tau <= 2  if and only if  there exists u in C with R_u nonempty.   (1)

Proof. A cover {u,v} works precisely when every target missed by u is hit
by v, equivalently v belongs to R_u. This includes a one-component cover,
empty target families, and repeated u=v. Conversely any v in R_u gives a
cover, since targets not in M_u are already hit by u. If some J_s is empty,
all R_u are empty and no finite obstacle cover exists, as required.

Consequently tau>2 has a finite certificate: for EVERY u choose a nonempty
subfamily S_u of M_u with empty total intersection. If |S_u|<=3, it is an
anchored rank-three exclusion. Its two checks are essential:
(a) u misses EVERY selected target; (b) their TOTAL common intersection is
empty. A missing anchor, a hit anchor, or a merely pairwise condition does
not establish (1). Given an at-most-two obstacle representation, use u as
the first obstacle's component; all of S_u would have to share the other
component, contradicting (b). This is a certificate for one drawing unless
its existence is proved for every placement.

The precise remaining graph-level target is

 exists simple planar G, forall injective placements p, forall u in C_p,
 exists S_u subset M_u(p), 1<=|S_u|<=3, intersection J_s(p)=empty.

It would imply obs(G)>=3 under the explicit connected/exterior convention.
It is not obtained from an abstract hypergraph or one C18 drawing. The
statement replaces an unnecessarily rigid demand for the SAME five targets
at every placement by an anchored choice allowed to depend on p and u.
No graph satisfying this universal target is supplied in this packet.

If |C|<=3 and R_u is empty, a core of size at most three always exists:
for each v in C select one target in M_u omitting v; these at most |C|
targets have empty intersection. This proof permits repetition before taking
a set. More generally |C| is a valid core-size bound, not the constant three.

## 4. Exact counterexample to rank-three completeness

Abstractly take C={0,1,2,3,4}, J_0={0}, and
 J_i={1,2,3,4} minus {i}, i=1,2,3,4.
One component must cover J_0, so it is 0; no single remaining component hits
all four other targets. Thus tau=3: component 0 plus any two distinct members
of {1,2,3,4} suffices, and two cannot suffice.

For anchor 0 the four missed targets have empty joint intersection but EVERY
proper subfamily has nonempty intersection. Therefore there is no anchored
rank-three exclusion at 0. A rank-four exclusion is necessary at that anchor.
Other anchors have two-target cores {J_0,J_i}. This is an exact five-target,
five-component set-system counterexample to the claim that rank-three anchored
certificates always suffice. No planar geometric realization is claimed.
Do not reject a real two-cover model by fabricating such incidence data.

## 5. Actual finite checks and assurance limits

anchored_triples.py compared (1) against exhaustive two-label assignments for
all 38,877 ordered set systems with 1..3 components and 0..5 targets. It
checked 20,867 no-two-cover systems and the same number of rank-three
certificates. The rank-four counterexample and four damaged certificate tests
were also run. Selected C18 masks [6,5,3,1] reproduce the eight pairwise and six
joint-component two-label assignments, with exactly two removed by the triple.
This is incidence replay of the pinned mathematical control, not a new
execution reconstructing C18 coordinates.

Both new commands use only ordinary Python memory operations and JSON stdout.
Their external 35 CPU/40 wall seconds, 512 MiB, one worker and 4 MiB output
bounds, actual exit codes, dates, hashes and observed counts are recorded in
continuation-execution.json. No network, subprocess, secret access, dynamic
execution, or file I/O is in either new mathematical source. The resource
wrapper is separate from the published mathematical code.

T (C19 tube/Jordan), A (complete arrangement/incidence), P1 (X4 lower-bound
chain) and P2 (placement-universal growth) remain distinct. The direct polygon
check does not need T. Abstract incidence certificates depend on A when used
for actual drawings. The trusted registry still needs a compatible consumer
and statement-faithfulness/axiom/closure binding; model agreement is not that
receipt. No protected record, workflow, Harness, verifier, Evidence, Result,
or Solution is edited. The original five C20 byte strings remain unavailable;
this continuation does not attempt to recover them from digests.

Reasoning audit: finite domains and empty cases fixed; (1) proved both ways;
core selection decreases a finite omitted-component set; all test loops have
explicit finite bounds; no stochastic search or placement compactness is used.
Failure is limited to the named coupling and to rank-three completeness, not
to every h=2 route. Novelty of these finite set-system identities is not claimed.

best_verified_candidate: none
best_verified_result: none
next_obligation: force anchored empty intersections uniformly over placements
for a different planar coupling, allowing rank four when rank three is incomplete.
root_status: open
