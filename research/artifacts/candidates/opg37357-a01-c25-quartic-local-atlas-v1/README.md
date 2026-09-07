# C25: a quartic, line-local placement atlas

Candidate: candidate:opg37357-a01-c25-quartic-local-atlas-v1
Verdict: candidate_only
Status: NONTERMINAL_CHECKPOINT
Primary owner: math-proof
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Target: obligation:opg37357-root
Base: ce90129ba27e425efd4228ff024b3686aa9a4588
Issue: #3

## 1. Resumption, exact scope and nonterminal boundary

Fresh main already contained C21--C24. C21 is the delivered second exact
consumer of C20's four certificates, using strict Fourier--Motzkin elimination
instead of the old producer's face-side samples. It is not retransported here.
This cycle actually reruns that code and records a new bounded observation.
The five original C20 source byte strings remain absent, both from their
current remote directory and from the available local artifacts. Their
recorded hashes cannot reconstruct them; no original-source safety audit,
attachment or successful retry is claimed. C25 is new mathematics and new
ordinary-text code, not a disguised resubmission of the rejected source.

The new placement lemma improves C24's degree-five atlas. It determines the
complete fixed-placement incidence hypergraph using only degree-at-most-four
signs. It does NOT prove that every abstract signature is realizable. It does
NOT prove the uniform obstacle bound asked by the second root question.

Use the explicit convention of C23: a finite simple labeled graph G, an
injective real placement p, K consisting of its graph points and CLOSED
straight edge segments, and nonempty connected obstacles disjoint from K.
Every nonedge must be hit. Let tau(G,p) be the least number of free-space
components meeting all nonedges, with tau=0 for a complete graph. C20/C23
relate this number to connected obstacles. C19 is needed separately when
converting the selected connected sets into bounded filled simple polygons.
No numerical placement is a graph-level lower bound.

For n>=3 define D* by: all vertex x-coordinates are distinct, no three graph
points are collinear, and distinct vertex-pair support lines are nonparallel.
All M=C(n,2) pair lines are used, including NONEDGES. Their forced concurrence
at graph vertices remains; additional line concurrence is also permitted.

**Candidate theorem.** For fixed labeled G, on D* the signs listed below
uniquely determine its nonedge/free-component incidence hypergraph up to
component relabeling, and hence tau(G,p). Minimization over REALIZABLE such
signatures gives the unrestricted connected-obstacle parameter, using the
separate robust-minimum argument in section 6. The theorem covers every
finite n; executable tests and limits are explicitly smaller.

The precise counterexample target would be two realizations in D* of the
same signature with different incidence hypergraphs/tau. None of the controls
below gives such a pair. The old vertex-order-only signature DOES have this
failure, as already recorded in C24.

## 2. Only three kinds of signs, with exact degrees

For homogeneous P_i=(x_i,y_i,1), index pair a=(i,j), i<j, and write

    L_a=P_i cross P_j=(A_a,B_a,C_a)
       =(y_i-y_j, x_j-x_i, x_i*y_j-y_i*x_j).

Include the following signs, with indexed pairs/triples in increasing order:

    b_a       = sign(B_a);
    w_ab      = sign(W_ab),  W_ab=A_a B_b-B_a A_b;
    d_abc     = sign(Delta_abc),  Delta_abc=det(L_a,L_b,L_c).

B has degree 1, W degree 2, and Delta degree at most 4: every determinant
term contains one entry from each column, of degrees 1,1,2. The list length is

    M + C(M,2) + C(M,3).

For n=6 it is 15+105+455=575, compared with C24's conservative 11,060.
As n grows this is O(n^6) rather than O(n^8) sign entries. This counts inputs,
not runtime or a feasible enumeration of all sign vectors. B and W are
nonzero on D*; Delta zeros MUST be retained, notably at graph vertices.
Antisymmetric W and alternating Delta supply values for all ordered indices.

No vertex-triple signs are additionally necessary: for three vertex indices,
a W between two pair lines sharing a vertex is a signed copy of that vertex
orientation. Nonzero W for all distinct pair lines already enforces this
part of D*. B also excludes coincident vertices. The decoder nevertheless
checks endpoint order/concurrence consistency explicitly.

## 3. Local intersection order: a factorization instead of a global sweep

Let I_ab=L_a cross L_b=(X_ab,Y_ab,W_ab). Its x-coordinate is X_ab/W_ab.
For three distinct lines a,b,c, direct expansion gives

    X_ab W_ac-X_ac W_ab = -B_a Delta_abc,

and therefore

    x_ab-x_ac = -B_a Delta_abc/(W_ab W_ac).                 (1)

For example, X_ab=B_a C_b-C_a B_b; substituting this and the two W expressions
into the left side factors out -B_a and leaves the displayed 3-by-3
determinant. There is no division by Delta, so concurrence is included.
Division by B or W is used only where D* asserts nonzero values.

Equation (1) determines every comparison between intersection points ON THE
SAME LINE using four signs. Equality holds precisely when Delta_abc=0.
Because a pair line is nonvertical, equal x on that line means the same
point. Thus on each line a we recover the ordered groups of all other lines
meeting it at each distinct event point. Each concurrence has a full group,
not several artificially perturbed crossings.

The old global comparisons of two disjoint intersection objects are no longer
needed. This proof does not rely on proving that arbitrary global sweep-event
swaps commute: it reconstructs faces locally, so unrelated events never need
a relative order. This bypasses the remaining global-event-order proof step
identified in the preceding C24 checkpoint without weakening its realizability
condition.

At graph endpoint p_i of pair line (i,j), choose k distinct from i,j.
The cut made by pair line (i,k) locates p_i. Every line incident to i gives
the same cut. No other pair line passes through p_i on D*, since that would
make three graph vertices collinear. The distinct cuts p_i,p_j and their
order are consequently recoverable. No supplied graph coordinate is moved.

## 4. Reconstruct all cells, faces and component incidence locally

### 4.1 Covectors of open one-dimensional faces

Fix an open interval of line a between consecutive recovered event groups,
allowing either unbounded end. For b!=a the side of its intersection x_ab
on this interval is known from the local order. Substituting line a's equation
into line b's equation gives

    L_b(x,(-A_a*x-C_a)/B_a) = -(W_ab/B_a)*(x-x_ab).         (2)

Hence the signs of all L_b, b!=a, on the face are determined. Only sign a is
zero. A sufficiently small displacement to either side of the face changes
only sign a, so replacing that zero by -1 or +1 gives its two incident
full-dimensional cell covectors. This reasoning does not treat a supporting
line as forbidden; we have not yet applied the graph-edge mask.

Collect the two covectors of EVERY face of EVERY pair line and deduplicate.
A strict sign vector is an intersection of open halfplanes, hence an open
convex cell when feasible. All covectors produced from a realization are
feasible by the face-side argument. Conversely, every full-dimensional cell
has a relative-interior face point in its boundary. To see this, choose an
interior point and a point across one of its bounding halfplanes; a generic
connecting segment first exits across exactly one line, avoiding the finite
intersection set. A finite refinement cannot remove all such boundary points.
Thus every cell appears among the collected face-side covectors. Since M>0
for n>=3, the whole-plane/no-line exception does not arise in this theorem.

This proves completeness without global strip ordering, a coordinate bounding
box, or a generic-position assumption on intersections of three lines.
The all-pair arrangement may have more cells than the edge-only arrangement
in C20, but it describes the same complement after free faces are joined.

### 4.2 Closed graph edges occupy only finite intervals

Each pair support line is distinct from every other pair support line on D*.
For a line corresponding to a graph EDGE ij, forbid exactly its open faces
between the recovered endpoint cuts p_i,p_j. All other open faces on that
line remain free. Lines corresponding to NONEDGES have no forbidden open
face from graph-edge coverage. Other graph edges meet them only at event
points, not along any open face.

At an event, its zero-face is forbidden exactly when it is a graph vertex
or lies in a CLOSED graph-edge interval. This status also follows from the
local ranks, using inclusive rather than strict endpoint comparisons. The
current code reports open faces; zero-face status is supplied by this rule,
not by pretending every event is freely crossable.

Construct a finite graph with the recovered two-dimensional cells as vertices
and one adjacency for each FREE open one-face. A free portal has a small ball
avoiding the closed compact K, so connected cells really belong to one free
component. At a free multiple intersection, all local sectors are joined via
free nearby one-face pieces. Therefore assigning a finite-graph component
label to every free point is locally constant, including at concurrence.
This is the C20 component argument with an explicitly finer arrangement.
It proves the exact bijection between finite graph components and components
of R^2 minus K. Forbidden events are never used as portals. Every graph point
is an event in the all-pair arrangement, even when it is graph-isolated.

### 4.3 Nonedge labels and the minimum cover

For nonedge ij, take all its open faces between p_i and p_j. They are free;
union their component labels to obtain J_ij. This set is complete: a free
isolated event hit has a free ball and hence a neighboring nonedge interval
with the same label. An event in K cannot be a witness. The graph endpoints
are forbidden. These facts account for every relative-interior parameter.

Thus the signature determines the entire hypergraph (J_s)_s, and tau is its
minimum component transversal. The empty nonedge family has tau=0. On D*,
every nonedge has a free interval, so the transversal is finite; there is no
need to infer that from an untrusted Boolean existence flag. C20's arbitrary
fixed degenerate drawings, including a nonedge wholly in K, remain supported
by C21 rather than silently inserted into this D* signature domain.

## 5. Executable contract and pressure tests

quartic_signature.py extracts B,W,Delta signs from exact rational points.
local_decode.py receives only n, those signs and the graph edge list. It has
no access to coordinates, the extractor's arithmetic, C20 or C21. It checks
array sizes and exact types, nonzero denominators, local total preorders,
concurrence agreement between lines, and graph-vertex endpoint compatibility.
These checks are necessary consistency checks, NOT a realizability solver.
Every output explicitly states realizability_checked=false and conditional_tau.

The pure modules perform only memory operations; controls.py prints JSON to
stdout. They contain no network, filesystem reads/writes, child processes,
secret/environment access, dynamic import or dynamic code evaluation. The
runtime is bounded externally. Input caps: 3<=n<=8, rational numerator and
denominator at most 256 bits, and at most 100,000 cover recursion states.
Each cover recursion removes its chosen uncovered target, so remaining-target
cardinality strictly decreases. Resource refusal is an error, not a lower bound.

controls.py uses the already-delivered C21 model ONLY as a comparison oracle.
It compares the component/target hypergraph up to label renaming and computes
covers by a separate exhaustive subset search on that edge-only arrangement.
For at most ten all-pair lines it also compares the full cell census with
C21 strict elimination. For every tested placement it checks all local cut
orders by direct rational intersection coordinates, all face covectors by
direct evaluation, and the exact polynomial identity (1).

The actual finite suite checks 116 drawing/graph pairs: all 8 three-vertex
graphs and 64 four-vertex graphs on the chosen points, 34 five-vertex masks,
five C24 cactus parameters and five transformed controls. It performs 29,754
exact factorization checks. The suite rejects eight out-of-domain coordinate
inputs and five damaged sign tables, including a deleted forced concurrence.
Changing a triangle's only triple-line sign is rejected by local consistency;
this particular rejection is NOT asserted to decide general realizability.

The C24 cactus control retains vertex positions
p0=(1,1),p1=(-2,-2),p2=(3,6),p3=(-5,-10),p4=(7,-7),p5=(-11,11+delta),
and edges 01,23,04,12,14,15,25. Its twenty vertex-triple signs are unchanged
at delta=-1/100,0,1/100 and +/-10^-40. But

    det(L_01,L_23,L_45)=168*delta.

The quartic signs capture the previously missed change. Counts are 85,84,85
all-pair cells and five free components, with tau=2,2,1 at -1/100,0,+1/100.
The B and W sign arrays are also equal at the two nonzero 1/100 controls;
exactly one Delta sign changes. The two tiny perturbations again give 2 versus 1.
This is an attack on coarse
signature compression, not an all-placement obstruction for the cactus.
The number of zero triple-line signs is 60 away from delta=0 and 61 at zero;
forcing all triple-line signs to be nonzero would wrongly discard graph vertices.

Reproduction from this directory with existing C21 on the module search path:

    PYTHONPATH=../opg37357-a01-c21-second-replay-v1 python -B controls.py

Use 30 CPU seconds, 40 wall seconds, 512 MiB address space, one mathematical
worker and a 1,000,000-byte output cap. Actual output and source fingerprints
are recorded in observation.json and execution.json. c21-rerun.json is a NEW
execution of the four original pinned certificates: all four accepted, 24
mutations rejected, 12 model controls and four strict smoke cases passed.
Finite tests do not prove the universal theorem or create a trusted receipt.

## 6. The unrestricted placement quantifier is retained, not erased

D* is dense because its excluded equalities are finitely many nonzero
polynomials. A nonzero polynomial cannot vanish on an open box (induction on
the number of variables using the finite-root property in one variable).
Their product is nonzero, so its zero set has empty interior.

Density alone would not preserve a representation. Given finitely many
connected obstacles at any injective placement, replace their finite assigned
hits by compact polygonal path unions in the corresponding open free
components. Thicken each slightly within its positive separation from K so
its selected nonedge hits are interior. Keep those obstacles fixed while
moving graph endpoints inside a sufficiently small coordinate box. Graph
edges retain clearance, and every hit moves using its FIXED interpolation
parameter on the moved nonedge and retains interior membership. Some p' in
this box is in D*, with no more obstacles. This uses A's open-component
argument, not T's polygon corner-count lemma.

For a signature sigma let Phi_sigma be the existential real sentence on the
2n vertex coordinates imposing D* and every B/W/Delta sign. By sections 2--4
and the preceding robustness argument,

    obs_ext(G) = min { tau_decode(G,sigma) : Phi_sigma is true }.

There are finitely many signatures at fixed n, but their feasibility is not
supplied by local_decode.py. To prove obs_ext(G)>h one must rule out EVERY
realizable signature with decoded cover<=h, or prove a necessary relaxed
system for all such signatures inconsistent. A single sampled signature
cannot do this. To prove a universal bound one still needs

    exists h>=1, forall finite planar G, exists REALIZABLE sigma,
    tau_decode(G,sigma)<=h.

The quantifier over unbounded graph order remains. No root answer follows
from the number 575 or from successful code execution. For n=0,1 the graph
is complete; for n=2 its obstacle parameter is zero or one. These small
orders are treated directly, not by a degenerate atlas.

## 7. An all-placement lower-bound family uses the existing X4 chain

The selected root direction remains LOWER BOUND, not the impossible goal of
reconstructing every planar graph with one obstacle. The existing C22 chain
for the ten-vertex planar X4 is the relevant universal invariant: a hypothetical
one-obstacle placement, after robust GP reduction, induces orientations and
key-path side choices satisfying the necessary CNF. Its stored unit-reason
proof ends with contradiction. No numerical placement is fixed in this
implication. C22's topology, CNF faithfulness and its finite trace remain
separate verification obligations; C25 does not reissue their old receipts.

Here is a precise hereditary extension, conditional on that C22 candidate.
If H is an INDUCED subgraph of G, restricting any obstacle representation of
G to V(H), while keeping its obstacles, gives a representation of H. Every
remaining edge still avoids the obstacles; every remaining nonedge was a
nonedge of G and is still blocked. Thus obs_ext(H)<=obs_ext(G). In particular,
no placement of G can evade an induced all-placement obstruction in H.
This is stronger than inferring anything from one bad drawing, and does not
rely on component labels being unchanged after deletion of edges.

Let X4(t), t>=0, be X4 with t new leaves adjacent only to its vertex N.
It has 10+t vertices and 24+t edges. X4 is induced, and planarity is retained
by placing the new leaf edges in a small wedge of a face incident to N in
any plane embedding of X4. Therefore C22's lower-bound implication would give

    forall t>=0, forall injective placements p of X4(t),
    no one-connected-obstacle representation exists at p.

This supplies an explicitly quantified target family and invariant, not a
new proof of the X4 premise. The bound stays TWO; allowing t to grow does
not prove divergence and does not negate the uniform-h root question.
Inducedness is essential to this monotonicity proof: deleting an edge creates
a new nonedge constraint which need not be blocked by the old obstacles.

## 8. Layer obligations, source audit and trusted admission gap

Candidate-local labels only; the protected obligation graph is unchanged:
T: C19's arbitrary-tree thin polygon/Jordan proof and corner count.
    To retain B17(n,e), rebuild its witness tree using ONLY edge-support
    lines after decoding the component cover. The all-pair arrangement has
    M=C(n,2) lines; a tree charged to all its cells need not satisfy the
    e-based count. C25 exports no tube or size-controlled tree and makes no
    such substitution. Connected-set existence and polygon count stay separate.
A: C20 arbitrary fixed-drawing characterization; C21's different exact consumer.
P1: C22 arbitrary-placement X4 regularization/key-path implication and finite CNF
    trace, with the hereditary extension above; no compatible trusted receipt.
P2a: the present quartic reconstruction theorem, conditional on realizability.
P2b: eliminate or certify the real-feasibility quantifier for target signatures,
     then obtain a result uniform over all planar graph orders (still open).

First actionable placement lemma: use the local interval orders and forced
concurrences to derive necessary constraints for low-cover REALIZABLE signatures,
without assuming vertex order types alone determine free components. A proposed
low-cover abstract signature must carry Phi_sigma feasibility or be kept pending.
The all-placement X4 chain is an existing P1 candidate, not a solution to P2b.

At the fresh base research/verifiers.json still has only the fixture policies,
blob b93b32955eb94c3b4ee82f045f7bbb85fd900f05. No compatible registered consumer
for the root geometry/trace or this quartic atlas is available. Web principal
cannot sign Evidence. Request a trusted statement-faithfulness and axiom/escape
review plus a correctly scoped frozen-input run. No truth records or Result
are written, and the ordinary three-job PR workflow is transport only.

The five missing C20 byte strings are not reconstructed from their hashes.
Their status and the re-audited C21 replacement fingerprints are in execution.json.
New C25 code is ordinary small UTF-8 text. No network, process or dynamic execution
is hidden in an alternate representation. C19/C20/C21/C22/C23/C24 remain unchanged.

Reasoning audit: domains/negation are frozen; explicit identities (1),(2) trace
orders to faces to components to covers. Degenerate event groups are retained;
nonincident cut order is never assumed. Finite graph traversal and decreasing
uncovered-target masks give termination. Dense-domain replacement has strict
clearance witnesses; it is not justified by density alone. Tests preserve
reflection, relabeling and tiny gaps, but do not replace proof. No probability
argument or asymptotic uniform-h inference is used. Neither T, A, P1 nor P2 is
closed by these execution logs, a PR, or a merge.

Sources: C19/C20/C21/C22/C23/C24 and the frozen ProblemContract at the declared
base. The quartic identity and local-face proof are given here explicitly.
No external source text is copied and no novelty claim is made for recognizing
line arrangements from their local incidence/order data.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
unrestricted_one_obstacle_completeness: open
next_action: audit the real-feasibility layer and low-cover local-order constraints;
retain C22's all-placement lower-bound chain and seek its compatible trusted gate.
