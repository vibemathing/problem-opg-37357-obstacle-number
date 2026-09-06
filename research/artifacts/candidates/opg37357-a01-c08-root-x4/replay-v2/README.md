# Q1: a 10-vertex planar obstruction, with a replayable Boolean certificate

Candidate: candidate:opg37357-a01-c08-x4-root-proof-v2
Verdict: candidate_only
Primary owner: math-proof
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Base revision: 853be12e7783f3b4843e98416a9cbbd29f2d41bf
Issue: #3

## Claim and attribution

The finite simple planar graph X4 below has no visibility representation using at most one connected obstacle. Consequently the existential question Q1 has a positive answer under the ordinary obstacle-number convention. This is not a new graph-theoretic result: Berman, Chappell, Faudree, Gimbel, Hartman and Williams, JGAA 21(6), 1107--1119 (2017), DOI 10.7155/jgaa.00452, journal Proposition 3, already give obs(X4)=2. This package reconstructs their necessary-condition method and supplies a fresh, compact, solver-free-replayable RUP certificate for the lower bound. It does not reconstruct the two-obstacle upper-bound drawing or claim that order 10 is minimal.

The mathematical chain here is explicit: planar witness; arbitrary one-obstacle representation implies general-position representation; that representation satisfies the generated CNF; the stored RUP proof derives the empty clause. No particular visibility drawing, vertex coordinates, obstacle shape, number of polygon corners, or affine gauge is imposed on the lower-bound CNF. The exact plane drawing is used ONLY for planarity.

Both admitted obligations remain open in repository state. Local exact replay, the literature theorem, and this proof candidate do not supply the required trusted kernel/axiom/faithfulness receipts or authorize Result admission. Q2 is not answered by this package.

## 1. The graph and its planar certificate

Use vertices N=0, S=1, a_i=2+i, b_i=6+i, with i modulo 4. The edges, for each i, are

    N a_i, S b_i, a_i a_(i+1), b_i b_(i+1), a_i b_i, a_(i+1) b_i.

There are 10 vertices, 24 distinct edges, and 21 nonedges. This is the skeleton of two 4-wheels joined by an alternating 8-cycle, the paper's X4 up to labeling. The certificate lists all edges and 16 oriented triangular faces. It also supplies these rational coordinates, in vertex order:

    (0,0), (23/56,23/56), (1,0), (0,1),
    (177/812,345/812), (345/812,177/812),
    (25/56,25/56), (471/1624,863/1624),
    (3/8,3/8), (863/1624,471/1624).

The exact replay checks distinct points, all 192 point/nonincident-edge incidences, and all 184 pairs of vertex-disjoint edges. No forbidden contact or crossing occurs. Shared-endpoint overlaps would put one endpoint on the other edge and are excluded by the incidence checks. Thus these coordinates give a straight-line planar drawing. The face/dart incidence and V-E+F=2 checks are supplementary; Euler's equation alone is not being used as a planarity test.

## 2. Definition faithfulness and general position without a corner cutoff

An ordinary obstacle is connected and disjoint from every graph point and every closed edge segment; a nonedge is blocked when its connecting segment meets the obstacle. The connectedness requirement is essential: declaring an arbitrary disconnected union to be one obstacle changes the invariant. Allowing the single obstacle to have holes, to be unbounded, or to be a nonpolygonal connected set only strengthens the following impossibility claim.

Even under a reading of the contract that omits an explicit vertex-exclusion clause, X4's positive minimum degree forces it: a vertex on an obstacle would make its incident edge segment meet that obstacle. Distinct placement is standard. If it were not expressly required, coincident vertices of this graph would have to be adjacent true twins, because their incident segments to every other vertex coincide. Direct inspection of the displayed adjacency lists gives no true twins in X4. Coincident nonadjacent points are also impossible because their zero-length nonedge would be unblocked. Hence no extra restriction is introduced for this witness.

Suppose such a representation exists. Let K be the union of the finite vertex set and closed graph-edge segments. A connected obstacle lies in one component U of the open set R^2 minus K. Components of this open planar set are polygonally path connected: the subset reachable by finite polygonal paths is both relatively open and relatively closed, using balls contained in the open set.

Choose one point of the obstacle on each nonedge. It is an interior point of that segment and belongs to U. Join the finitely many chosen points by polygonal paths inside U. Their union is compact, connected, and has positive distance from K. A sufficiently thin finite union of closed rectangles and small squares around these paths is still connected, stays in U, and contains all chosen points in its interior. This replacement need not be a simple polygon; the key-path argument only requires a connected obstacle.

The edge clearances and the interior blocking margins are now positive. Small simultaneous movements of graph vertices preserve them: for a witness z=(1-lambda)p_i+lambda p_j, retain lambda in (0,1) and move z by the same formula with the moved endpoints. Successively choose the new vertex positions outside the finitely many lines through previously chosen pairs. This gives distinct graph points with no collinear triple and still one connected obstacle. Thus proving impossibility for such general-position placements proves it for all original placements. No numeric corner bound or normalization is used.

## 3. Orientation identities

Write O(a,b,c)=det(b-a,c-a), and let x_abc mean O(a,b,c)>0. Use one Boolean variable for each increasing triple; an odd permutation negates its literal. Our sign convention is counterclockwise rather than the paper's clockwise convention; all rules below hold with either consistent choice.

For four distinct points the identity

    O(b,c,d)=O(a,b,c)+O(a,c,d)+O(a,d,b)

implies the clause

    not x_abc OR not x_acd OR not x_adb OR x_bcd.

For five distinct points, the determinant identity

    O(a,b,d) O(a,c,e)
      = O(a,b,c) O(a,d,e) + O(a,b,e) O(a,c,d)

shows that if x_abc,x_acd,x_ade,x_abe are all true, then O(a,b,d) and O(a,c,e) have the same nonzero sign. With H the disjunction of the negations of those four antecedents, add

    H OR x_abd OR not x_ace;
    H OR not x_abd OR x_ace.

The generator instantiates these rules for EVERY ordered 4-tuple and 5-tuple of distinct vertices, then canonicalizes literals, removes tautologies, and deduplicates. These are necessary conditions on every realizable order type; no claim that they characterize realizability is needed. Their canonical block sizes for X4 are 420 and 3024 clauses.

## 4. Connected-obstacle key-path separation lemma

Fix distinct nonedges ab and cd; they may share one vertex. An a-b path is a key path relative to cd when all its vertices lie in one closed halfplane bounded by the line cd. General position ensures that vertices other than c,d lie strictly on one side or the other.

Lemma. If the representation has only one connected obstacle, there is a side of line ab such that EVERY key a-b path relative to cd has an internal vertex strictly on that side.

Proof. Otherwise there are two key a-b paths whose internal vertices are entirely in opposite open halfplanes bounded by ab. Their open polygonal walks lie in these respective halfplanes. Although graph edges may cross, each such finite walk contains a simple polygonal a-b arc obtained by erasing geometric loops. The two arcs have disjoint interiors, meet only at a,b, and form a polygonal Jordan curve made of graph-edge pieces. The open segment ab is inside this curve.

Both paths lie in the SAME closed halfplane bounded by cd: they share a and b, at least one of which is not on cd. The bounded region of their Jordan curve is contained in that halfplane and its interior misses the boundary line. The curve itself misses the open segment cd. Indeed, any of its pieces lying on cd would have to be an edge with endpoints c,d, which is absent; general position prevents all other vertex-on-line events except possibly the endpoints c,d themselves. The open segment cd is therefore outside the curve. One connected obstacle disjoint from the graph-edge curve cannot meet both complementary components. It cannot block both nonedges. This contradiction proves the lemma.

The use of loop erasure makes the argument applicable to crossing visibility drawings; graph planarity is not assumed within this lemma.

## 5. The actual finite CNF

For every ordered pair (ab,cd) of distinct canonically ordered nonedges introduce one side variable s_ab,cd. There are 21*20=420 such variables, together with 120 triple variables, for a total of 540.

Enumerate every simple a-b path with at most FOUR EDGES. For such a path P, let C be the list of literals x_cdv for vertices v of P other than c,d, and let J be the list x_abv for its internal vertices. For each of the lists C and -C add

    C OR not s_ab,cd OR J;
    C OR s_ab,cd OR -J.

Here a list inside a clause denotes disjunction, and -C/-J negate every literal. If P is key, either C or -C is entirely false, forcing an internal vertex on the chosen side. If it is not key, each list has a true literal and imposes no side condition. These clauses are also obtained by eliminating the path-indicator variable from the paper's clauses (4)--(7).

The four-edge cap makes the conditions WEAKER, not stronger, than requiring every path. Hence UNSAT with this cap is sufficient for a lower bound. SAT at a smaller cap has no representability implication. No fixed vertex order around a circle, no planarity constraint on the hypothetical drawing, and no symmetry unit clause is used.

The deterministic generator returns 2212 paths across the 21 nonedges and 65,888 canonical key-path clauses. Together with the two orientation blocks this is 69,332 clauses. The ASCII DIMACS SHA-256 is

    de54d35f78d3c7d84e24651e5ce6f82c9ebe6d78bc7bd2deb66aa591e6ea276c.

Every one-obstacle placement would supply a satisfying assignment by Sections 2--4. The next section supplies a finite contradiction instead.

## 6. Exact RUP proof and checker

The package encodes a 60,632-byte ASCII RUP proof with 1,827 additions, ending in the empty clause. Its decompressed SHA-256 is

    9d16206d67cb450cbaaa4920fe83a5d463584a612f29367e0f2da4a8acd6ec5e.

For each proposed clause C the checker temporarily assumes all literals of C false and performs exact unit propagation using the original CNF and previously accepted clauses. It accepts C only if this produces a contradiction. Unit propagation is sound under every satisfying Boolean assignment; therefore every accepted clause is implied by the input. Induction on proof lines shows that acceptance of the final empty clause certifies propositional inconsistency. No SAT solver, geometry solver, floating arithmetic, or Z3 proof rule is trusted by this replay.

The checker verifies literal ranges, clause syntax, no repeated or opposite literals, exact graph identity, CNF and proof hashes, byte caps, a finite replay time cap, presence of a final empty clause, and absence of subsequent lines. The optional self-test compares accepted propagation implications with truth tables for 10,206 small cases and rejects four malformed/nonproof cases. Those regressions are not themselves a universal verification of the checker implementation; its soundness argument and kernel translation remain review obligations.

Actual execution in the candidate sandbox: Python 3.13.5; Z3 C library 4.13.3.0 generated an initial UNSAT proof in 5.139 seconds. Six bounded proof-core reruns reduced the certificate; the final RUP proof was replayed against the FULL original CNF, not merely an unchecked core. A separately written standard-library Python checker passed. The saved replay-observation.json is its actual stdout. Generation and replay were both within this candidate trust domain and are not a trusted verifier receipt.

Search scope: X4 path caps 2 and 3 returned SAT; cap 4 returned UNSAT with proof. X3 at cap 4 returned SAT as a control. No enumeration of all graphs of any order, no minimal-obstruction result, and no search for obstacle number greater than 2 is claimed.

## 7. Reproduction and exact transport boundary

Run from repository root in a bounded environment:

    python research/artifacts/candidates/opg37357-a01-c08-root-x4/replay-v2/replay.py --self-test

Use one process, one thread, 1 GiB memory, 60 seconds wall time, and at most 64 KiB captured stdout/stderr. Only the Python standard library is needed. Slower environments may refuse on the explicit replay timeout; refusal is not a mathematical answer.

The replay-v2 directory is a self-contained package. During text transport a single base64 character was omitted from certificate.json. Rather than silently changing proof expectations, materialize.py specifies ONE fixed text delta and checks both the exact stored-byte SHA-256 and exact decoded-package SHA-256. Unknown input changes are rejected. It writes nothing. The reconstructed package is then decoded and the unchanged proof hash and all RUP lines are checked. This is a lossless transport encoding of the already replayed certificate, not permission to repair arbitrary failed proofs.

Stored transport SHA-256: b4668771fd98f902ebc6c8fc73e7db2a6a5c103660ccfed6e20c442f73505dc5.
Reconstructed package SHA-256: 440c92278e01888c19bbb341958eca1320da6f28362d66343d0eb3e8e8cce697.

The parent directory also contains preserved, unfinished earlier producer/proof-part files with different labeling and encoding. Replay-v2 does NOT import or concatenate those files and makes no validation claim about them. No previous candidate was overwritten. The reproduction command above is the authoritative entry point for this candidate version.

## 8. Root conclusion and remaining assurance tasks

Assuming an ordinary one-connected-obstacle representation of X4 yields a satisfying assignment to the CNF; its exact RUP refutation contradicts this. Section 1 certifies X4 planar. This forms a full mathematical Q1 proof candidate, rather than another encoding-infrastructure claim or a fixed-drawing UNSAT test.

Remaining trusted tasks: verify the graph-to-contract mapping, determinant identities and key-path separation/regularization; replay the frozen bundle in an admitted verifier trust domain; translate/check the Boolean checker or proof in the accepted kernel; perform the required axiom and statement-faithfulness audits. No protected record is appended here. The existing root node includes Q2 as well, so Q1 alone would not close that root even after trusted replay.

best_verified_result: none
best_verified_candidate: none
locally_replayed_candidate: candidate:opg37357-a01-c08-x4-root-proof-v2
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: pursue Q2 on induced triangulation supergraphs, preserving the distinction between induced-subgraph monotonicity and unsupported edge-deletion/minor monotonicity.
