# Two-obstacle root search: selected maximal planar graphs

Candidate: candidate:opg37357-a01-c10-two-obstacle-samples-v1
Verdict: candidate_only
Owner: math-proof
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Base: f2f0512dcf08742d7cedf732071810c5d7f66e33

## Mathematical question and exact implication

Q1 reuses the c08 X4 obstruction and its stored solver-free propositional replay. Q2 asks for a universal ordinary obstacle bound, not a bound in a prescribed drawing. Following c09, this experiment examines maximal planar graphs. It does not impose a plane visibility drawing or any fixed vertex coordinates.

Let Ebar be the nonedges. Give each nonedge e a Boolean t_e selecting one obstacle which blocks it. If both obstacles block it, select either. Retain c08's four-point and five-point necessary orientation axioms, with one Boolean for each unordered vertex triple and the permutation signs for ordered triples.

For each ordered pair of distinct nonedges e,f and each c08 key-path clause C(e,f,P), impose BOTH

    (t_e OR t_f OR C(e,f,P)),
    (NOT t_e OR NOT t_f OR C(e,f,P)).

When the colors agree, one guard is false and C is required. When they differ, both guarded clauses are automatically true. The side variable for (e,f) can be shared between the two color cases, since only one case is active. Fix the first nonedge's color to false by renaming the two obstacles; this is not a fixed coordinate choice or a vertex-order assumption. Paths are simple and bounded by their number of edges.

Necessity proof. Take a genuine representation by at most two connected obstacles. Select a blocker for each nonedge. C08's Jordan-separation argument applies to any two nonedges assigned the SAME connected obstacle: the existence of another obstacle does not permit the selected obstacle to cross a graph edge. Therefore that pair's key-path clauses hold. Real point orientations satisfy the four- and five-point clauses. A representation can be put in vertex general position using finite strict blocking witnesses and clearance from the finite graph-edge set, without an obstacle-corner restriction. Consequently every actual two-obstacle representation induces a satisfying Boolean assignment to every finite path-depth instance here.

Only this direction is claimed. The orientation axioms need not ensure realizability, and pairwise key-path conditions need not ensure one global free-space component for every color class. SAT of the relaxation is not an obstacle construction. UNSAT with a replayed certificate and a verified necessity reduction would give a graph-level lower bound of at least three; no such UNSAT was obtained in these trials.

## Frozen graph inputs and selection

X_r has vertices N,S,a_i,b_i for i modulo r; its edges are N-a_i, S-b_i, a_i-a_(i+1), b_i-b_(i+1), a_i-b_i, and a_(i+1)-b_i. It is the capped triangulated cylinder, of order 2r+2 and size 6r. The data stores every edge and an oriented triangular-face certificate, not merely a graph name.

A legal flip removes an edge uv with incident opposite vertices a,b and adds ab when it is absent. The selected flip indices are lexicographic indices in two_obstacle.py. The ten inputs are X4, X5, X6 and selected single-flip isomorphism representatives: indices 0,8,10 for X4; 0 for X5; and 0,12,14 for X6. This is NOT exhaustive planar-graph enumeration at orders 10,12,14. The plane embedding certifies that the abstract input is planar; it does not constrain the separately quantified visibility placement.

## Actual retained trial results

All rows below have a stored exact Boolean assignment satisfying every generated clause. Counts are regenerated from the frozen bytes, not copied from an intermediate prose summary.

The retained inputs consist of four order-10 graphs (path-edge cap four),
two order-12 graphs (cap three), and four order-14 graphs (cap two).
Per-instance variable counts, clause counts, full CNF digests, and Boolean-model
digests are stored in the data and checked during regeneration. The sample
selection is not an exhaustive search of any of these orders.

The retained generator observations use Python 3.13.5, NetworkX 3.6.1 and the Z3 C library reporting 4.13.3.0. The Python z3 package is not required. The current source caps n at 14, path length at four, clauses at 220000, formula compilation at 25 seconds, and solver timeout at at most 10000 milliseconds; retained successful trials used 5000 milliseconds. The foreground process had an external finite wall-time bound. No search continues in the background.

Two earlier X5 trials exceeded the imposed 1 GiB address-space limit: a length-four instance compiled 377311 clauses under the then larger compilation cap, and a length-three instance compiled 154831 clauses. Neither produced a mathematical verdict. Reducing the path depth and increasing the explicitly bounded address-space allowance to 2 GiB permitted the length-three trial to finish. Those failures are not represented as UNSAT. The later source's lower clause cap must not be described as having generated the earlier 377311-clause trial.

## Solver-free replay and file integrity

replay.py does not invoke Z3. It verifies the graph and formula digests, regenerates the CNF, decodes a complete Boolean assignment, checks its digest, and evaluates every clause. It also checks oriented face coverage, one cyclic link per vertex, connectedness, and Euler characteristic two. Together these give a combinatorial sphere embedding certificate for the simple input graph. The proof of this certificate interpretation is a separate graph-topology premise, not a numerical solver assertion.

The final local replay passed for all ten inputs and evaluated every retained clause. It also checked all ten sphere certificates. Three altered sphere inputs (missing face, reversed face, deleted edge) were rejected. Forcing every literal of one genuine clause false was detected by the clause evaluator. These are candidate-generation checks, not a registered trusted-verifier receipt.

Data is split into ten small ASCII chunks to avoid transcription damage during GitHub transport. samples.txt is a manifest with each chunk's byte length and SHA-256 and the concatenated payload SHA-256. The payload decodes to one bounded zlib-compressed JSON object containing graph certificates, original search observations, and exact packed Boolean models. The loader checks every part before decoding and refuses trailing frames or expanded data exceeding 1 MiB. The old malformed unmerged transport frame was replaced; none of its bytes is used in the accepted local replay. Every chunk is separately digest-bound in the Web packet so transport CI checks the uploaded bytes too.

From this directory, run `python replay.py` in one process with a 45-second external wall bound. It needs Python and the local two_obstacle.py, but not NetworkX or Z3 for the replay path. Generating new graph flips requires NetworkX; new solving requires the Z3 C library. The stored models make the original solver unnecessary for checking the recorded Boolean claims.

## Conclusions and next exact target

These ten bounded relaxations are excluded as UNSAT certificates for a three-obstacle lower bound. They do not exclude the graphs themselves as obstructions after stronger conditions or longer paths, nor establish an upper bound of two. No new Q2 constant or divergent family is produced.

The next substantive target is a multi-nonedge necessary condition: every nonedge assigned one blocker must meet a SINGLE common free-space component, not just satisfy all tested pairwise path conditions. Any new obstruction must retain all placements and a checkable UNSAT certificate. An alternative upper-bound target is an explicit two-obstacle construction for the whole X_r family rather than further isolated relaxed-SAT samples. Q1's c08 geometric and formal trust obligations remain pending. No protected records are changed.

Primary literature: Berman et al., JGAA 21(6), 1107--1119 (2017), Proposition 3 and its four-/five-point/key-path reduction, https://jgaa.info/index.php/jgaa/article/download/paper452/2511/2318 . C08 independently stores the lower-bound proof data. Gimbel, Ossona de Mendez and Valtr, arXiv:1706.06992v3, distinguish ordinary from crossing-free obstacle number and prove the bipartite-planar upper bound one; no bipartite-planar obstruction search is pursued. See c09's source note for the fresh comparison with Balko et al. (2024) and the separate planar-convex variant.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
