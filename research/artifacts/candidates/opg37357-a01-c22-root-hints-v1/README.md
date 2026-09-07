# C22: all-placement X4 soundness and explicit unit-reason replay

Candidate: candidate:opg37357-a01-c22-root-hints-v1
Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Base: 367de3b7c3008832ef07028453192b6291ee4fec
Primary owner: math-proof

## 1. What is new, and which quantifiers are being addressed

C21 is already on this base. Its separately implemented strict-cell consumer
replays all four C20 certificates without importing the original arrangement
core. The old five C20 source byte strings are still unavailable; their hashes
are not recoverable source. C21 is a named functional replacement, not a claim
that those old bytes have been recovered. This cycle does not republish C21.

This cycle instead audits Q1's ALL-PLACEMENT lower-bound implication for the
explicit planar graph X4 and converts the existing C08 RUP proof to a more
transparent proof interface. The new consumer checks only named unit/conflict
clauses, not search, watch lists, a SAT solver or geometry. The two-watch
producer and reverse-dependency trimmer are untrusted inputs to that consumer.
The actual trace is reproducible from the already-merged C08 proof and these
five small plaintext sources. Its hash is frozen; it is a derived cache, not
a second copy of the existing root certificate or a new trusted receipt.

The root contains two different questions:
Q1: exists finite planar G, forall injective placements p, no one-obstacle
representation of G exists at p.
Q2: exists integer h>=1, forall finite planar G, exists a placement p and a
representation using at most h obstacles.

A bad C18 placement has no implication of the form forall p. The following
Q1 chain has no coordinate constraint on the hypothetical obstacle placement.
Its rational graph drawing serves ONLY to prove that the abstract X4 is planar.
Q1 is published prior art, not claimed new; Q2 remains open in this project.

## 2. Fixed abstract graph and conventions

Use vertices N=0, S=1, a_i=2+i, b_i=6+i, i modulo 4. The edges for each i are
N a_i, S b_i, a_i a_(i+1), b_i b_(i+1), a_i b_i, a_(i+1) b_i.
There are ten vertices, 24 edges and 21 nonedges. graph() lists this set and
16 triangular faces. The existing rational coordinate certificate is checked
by 192 vertex/nonincident-edge tests and 184 pairs of disjoint graph edges;
no crossing or contact occurs. The graph also has positive minimum degree
and no true twins, checked explicitly.

The ordinary-obstacle convention is: graph points and CLOSED graph-edge
segments are excluded from every connected obstacle, and every nonedge must
meet some obstacle. The obstacle may have holes, need not be bounded, and
need not itself be path connected in the lower-bound implication. Enlarging
the allowed obstacle class only strengthens the resulting impossibility.
The mapping of this convention to the canonical polygonal-obstacle wording
is a separate statement-faithfulness gate, not silently admitted here.

Even if a putative definition did not explicitly state injectivity, X4 removes
the usual loophole. Positive degree excludes a vertex location from every
obstacle because an incident closed graph edge contains that location. Two
coincident nonadjacent vertices would then be visible. Two coincident adjacent
vertices would have identical visibility to every other vertex, hence would
be true twins. X4 has neither exception. This is not a general license to
omit injectivity for arbitrary graphs.

## 3. From arbitrary real coordinates to a GP hypothetical representation

Assume a one-connected-obstacle representation of X4 at arbitrary injective
real coordinates. Let K be the compact union of its points and closed edges.
The obstacle lies in one open component U of the complement. Components of
an open subset of the plane are polygonally path connected: the polygonally
reachable class is open and relatively closed in its connected component.
For each nonedge choose an interior segment hit in U. Openness gives an open
parameter interval even when the old obstacle only touched the segment.

Join these finitely many hits by finitely many polygonal paths in U. Their
compact connected union T has positive distance from K. A sufficiently small
closed distance-neighborhood of T is compact and connected, still misses K,
and contains all selected hits in its interior. No claim of a simple polygon
or the C19 corner bound is needed for this step.

Perturb the graph points jointly by less than the edge-clearance margin and
less than every hit's interior margin. For a nonedge retain its interpolation
parameter t in (0,1); its moved hit is (1-t)p'_i+t p'_j. This moves by at most
the maximum endpoint displacement, so it remains in the same obstacle.
Every moved graph edge stays disjoint. Within this nonempty coordinate box,
choose the points sequentially outside the finitely many lines through earlier
pairs. The new hypothetical representation has no three collinear graph points.

Thus existence at ANY original placement implies existence at SOME GP placement,
which is enough for a lower bound. We do not assert that every fixed drawing
can be moved while still being the same drawing, nor use C20's negative control.

## 4. Universal geometric restrictions at GP placements

Write D(a,b,c)=det(b-a,c-a) and x_abc=(D(a,b,c)>0). Odd permutations negate a
literal; increasing triples get variables 1,...,120. No orientation is fixed.

The four-point identity is
D(b,c,d)=D(a,b,c)+D(a,c,d)+D(a,d,b).
Therefore three positive terms on the right imply positivity on the left.

The five-point determinant identity is
D(a,b,d) D(a,c,e)
 = D(a,b,c) D(a,d,e) + D(a,b,e) D(a,c,d).
It follows by expanding the determinants after translating a to 0.
If D(a,b,c),D(a,c,d),D(a,d,e),D(a,b,e) are positive, the product on the left
is positive, so its two nonzero factors have equal signs. These implications,
for every ordered tuple, give the two orientation clause families. They need
not characterize all realizable order types: necessity is sufficient here.

For distinct nonedges ab and cd, possibly sharing one endpoint, call an a--b
graph path a cd-key-path when it lies in one CLOSED halfplane of the line cd.
A one-obstacle representation has a choice of side of line ab such that every
such key-path has an internal vertex strictly on that chosen side.

Here is the separation argument including crossed graph paths. If neither
side works, there is a key-path whose internal vertices are all strictly above
ab and another whose internal vertices are all strictly below ab. Subdivide
the geometric walks at their finitely many crossings and erase loops to obtain
simple polygonal a--b arcs in their respective open halfplanes. The arcs still
consist of pieces of graph edges. They meet only at a and b. The upper arc
with segment ab bounds a disk above ab, and the lower one with ab bounds a
disk below ab. Splicing along ab gives a simple closed curve made only of
graph-edge pieces whose bounded region contains the WHOLE open segment ab.
This uses polygonal Jordan separation, not that the original drawing is plane.

Both original key-paths lie on the same side of line cd: they share a,b and
at least one of these endpoints is not c or d. GP puts that endpoint strictly
on one side. Their simple arcs and the bounded region therefore lie in that
closed halfplane, with the bounded region strictly off the boundary line.
The open segment cd misses the curve (otherwise GP would force a graph edge
cd) and is outside the bounded region. A connected obstacle disjoint from the
curve cannot hit both open ab and open cd. This contradiction proves the rule.
The case of one shared endpoint changes none of these strict-interior claims.

## 5. The exact finite formula, including path truncation

For every ordered pair of distinct canonical nonedges ab,cd introduce one
side variable s; there are 21*20=420. For a graph path P let C be the list of
x_cdv for vertices v of P other than c,d, and let J be the list of x_abv for
internal vertices of P. The four clauses used are

  OR C    OR not s OR OR J;
  OR C    OR s     OR OR not J;
  OR not C OR not s OR OR J;
  OR not C OR s     OR OR not J.

When P is not a key-path both premise disjunctions have a true literal. When
P is a key-path one premise disjunction is false and these clauses enforce
the chosen side's internal-vertex requirement. This is an existential side
choice for ab,cd, not a globally fixed side or a witness at numeric coordinates.

The compiler retains all simple paths of at most FOUR edges, generated by
finite layered extension with no repeated vertex. Deleting longer-path clauses
is a relaxation of necessary conditions. A contradiction in the relaxed formula
is consequently still a valid all-placement obstruction. Increasing labels only
is NOT used. Duplicate clauses and tautologies are handled explicitly; the
canonical signed-literal ordering is byte-pinned by the full DIMACS hash.

The regenerated counts are 420 four-point, 20160 five-point and 48752 key-path
clauses, with 804 paths in the path census: 69332 clauses and 540 variables.
These are the corrected C09 counts, not the older erroneous C08 subcounts.
CNF SHA-256: de54d35f78d3c7d84e24651e5ce6f82c9ebe6d78bc7bd2deb66aa591e6ea276c.

## 6. Explicit reasons and the small consumer's proof principle

A row consists of [new clause id, clause C, positive existing-clause ids].
Assume the negation of each literal of C. At each listed reason the consumer
requires that its clause is not satisfied and has at most one unassigned
literal. One remaining literal is forced true; zero means a contradiction,
which must be the final reason. Reasons may reference only previous clauses.
The consumer rejects duplicate/opposite literals, bad types, future ids, steps
after a conflict, and a proof not ending with the empty clause.

Soundness is by induction on rows. Under any model of the current database
and not C, each unit step is forced by a clause already in the database. A
conflicting reason therefore rules out that model, so the database entails C.
Adding C preserves its models. At the final empty clause there can be no model
of the original CNF. This argument uses consistency of the partial assignment;
that consistency follows initially from the nontautological C and thereafter
because each new literal is unassigned, not opposed to an existing assignment.

The producer may be wrong and the trimmer may be wrong without making the
consumer's logical rule validly accept a false derivation: their only interface
is this finite list. This separation is a code-design check, not a separate
verifier trust domain. Source compilation, geometric semantics and arithmetic
execution are still distinct obligations.

Actual local replay accepts all 1827 existing C08 additions, ending at clause
71159. The raw producer uses 84272 reason steps; reverse dependency trimming
leaves 29267. The canonical JSON trace is 250638 bytes with SHA-256
f9a6f8e4369c456f014974656b17944e4946401e6a20ec7350e6646efd71adb2.
The trace is generated deterministically by --emit-hints; no external solver or
unpublished file is needed. The already-published C08 RUP remains the canonical
proof input, SHA-256 9d16206d67cb450cbaaa4920fe83a5d463584a612f29367e0f2da4a8acd6ec5e.

## 7. Reproduction, finite tests, and source audit

From this candidate directory, with the existing repository checkout:

  python replay.py ../opg37357-a01-c08-root-x4/replay-v2/certificate.json
  python replay.py ../opg37357-a01-c08-root-x4/replay-v2/certificate.json --emit-hints

The second command emits the complete derived trace as ordinary JSON. A separate
caller can pass the parsed rows to hint_check.verify with root_cnf.compile_cnf's
clauses, without using the producer in that consumer. The old C08 text delta is
not a proof repair: its input, corrected package and decoded proof are each
hash-locked. No old file is edited. It consumes an already-published compressed
proof DATA file; it is not a workaround for the unrelated C20 source block.

The actual run used CPython 3.13.5 under 35 CPU seconds, 40 wall seconds and
512 MiB address-space limits; one process and no network. observation.json is
its compact output. Among all 256 databases of nonempty nontautological clauses
on two variables, 160 unit-refutable cases were accepted and each had no truth-
table model. Rejected cases are NOT claimed satisfiable or a completeness test
for all propositional proofs. Twelve malformed reason traces were rejected.

The five new sources are ordinary readable UTF-8. Four modules are pure memory
operations. replay.py only reads one named, size- and hash-locked local JSON
file and writes stdout. No network, subprocess, dynamic import/evaluation,
credentials, environment secrets, shell invocation or filesystem mutation is
present. Arithmetic and resource failures remain failures, not counterexamples.

## 8. Source faithfulness, layer obligations, and continuation

Primary source: Berman, Chappell, Faudree, Gimbel, Hartman and Williams,
Graphs with Obstacle Number Greater than One, JGAA 21(6), 1107--1119 (2017),
DOI 10.7155/jgaa.00452. Lemmas 1--3 and Observation 2 supply the necessary-rule
provenance; Proposition 3 supplies the already-known X4 lower bound. The source
uses clockwise literals; using counterclockwise consistently reverses every
orientation without changing these implications. Its Figure 4 upper drawing
is not numerically reconstructed or needed by this lower-bound replay.
https://jgaa.info/index.php/jgaa/article/download/paper452/2511/2318

Candidate-local obligations are separate from protected admitted record ids:
T: C19's tree/tube/Jordan corner-count proof (not a premise of this Q1 replay).
A: C20/C21 fixed-drawing arrangement completeness and second-core replay.
P1: the arbitrary-placement regularization, key-path topology, and CNF compiler
faithfulness above, plus the frozen propositional proof for X4.
P2: a bound on min_p tau_G(p) UNIFORM over all finite planar G, or a family
forcing that minimum to diverge. P2 is not implied by P1 or a numerical drawing.

The current registry contains fixture policies, not a compatible registered
consumer for this unit-reason proof and its geometric theorem. The candidate
PR workflow checks transport only. A trusted process must bind an actual
consumer fingerprint and receipt, axiom/escape audit and statement-faithfulness
to this frozen candidate before admission. No such receipt is invented here.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_obligation: P2, preserve its exists-h/forall-G/exists-placement order; audit
the minimum component-cover formulation and simultaneous obstacle corner count.
A merge is not the end of the root research.
