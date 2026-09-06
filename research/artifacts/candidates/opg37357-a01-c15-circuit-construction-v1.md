# C15: explicit sparse-polygon circuit construction

Candidate: candidate:opg37357-a01-c15-circuit-construction-v1
Verdict: candidate_only
Owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: 642573645569c9d2942abff288ff3e2a5e7bb8fb

## Exact claim and implementation status

This is a NON-EXECUTABLE mathematical construction of a c14-format circuit
for the sparse polygon sentence S_(G,m) of c07/c11. It is not a claim that a
polygon front-end program was submitted or executed. The attempted source
write was blocked by the platform and has no commit receipt. That operation
is recorded in Issue #3; this artifact does not reproduce its source code.

Claim C15.1 (candidate): for a fixed finite simple labeled graph G and m,
one can construct a finite typed acyclic circuit C_(G,m) and an explicit
bijection sigma of original variables, such that, pointwise in every real
assignment X of those variables,

    C_(G,m)(sigma(X)) = true iff S_(G,m)(X).

This is a constructive, blockwise semantics statement. It is NOT evidence
that an unexecuted program implements the construction. Planarity is only an
input promise. There is no graph-edge noncrossing condition. S describes one
closed filled simple polygon and exterior graph points; raw sparse witnesses
need not be in GP-ALL. GP extraction and at-most/exact-m equivalence depend
separately on c07/c04.

## 1. Frozen original-variable map

For n>=1,m>=3, list all c11 free real variables in the following order:
graph coordinates p3x,p3y,...,pnx,pny; polygon coordinates q0x,q0y,...,
q(m-1)x,q(m-1)y; then for each i=0,...,n-1, the m crossing variables
c(i,0),...,c(i,m-1) followed by the m+1 prefix variables b(i,0),...,b(i,m).
The literal names in c11 are c0_0, b0_0, etc.

Let x_j be the j-th listed variable's value. Distinct names in these disjoint
families prove injectivity, and inspection of c11's declarations proves
surjectivity. The input dimension is

    d = 2m + 2 max(n-2,0) + nm + n(m+1),

not the graph order n. All crossing and prefix bits are real original inputs:
their Boolean/XOR constraints will occur inside the circuit. They are not
chosen by a decoder before feasibility is tested.

p1=(0,0) and p2=(1,0) when n>=2 are constant-node references. Neither anchor
is added to the free input list. For n=1 only the first anchor exists.
Use reusable rational constants 0,1,2 for arithmetic.

When m<3, after validating the graph, use the false constant circuit with
zero real inputs. When n=0,m>=3, use the true constant circuit. Both have
one Boolean constant node and root index 0. No dummy coordinate or prefix
variables are needed for these shortcuts.

## 2. Circuit extension rules and induction invariant

The target grammar is exactly c14: arithmetic input/constant/add/subtract/
multiply nodes; Boolean constant/atom/not/and/or nodes; zero-based typed
indices; arithmetic and Boolean operation operands precede their outputs
in their respective arrays. Atoms compare an arithmetic node to zero with
one of eq,ne,lt,le,gt,ge. A comparison of two values first subtracts them.

Maintain separate real and Boolean reference tables. To build a compound
arithmetic expression, recursively construct its proper subexpressions and
then append its operation node. To build a Boolean expression, construct
all required arithmetic and Boolean subexpressions first, then its gate.
An implementation can replace recursion by a bounded explicit stack;
recursion is only a finite inductive definition here.

Induction invariant: each appended real reference evaluates to the named
polynomial in x; each appended Boolean reference evaluates to the named
predicate. Old nodes keep their meanings after appending. Every reference
has the correct sort and a smaller dependency index. An atom may refer to
any already-built arithmetic node; a later Boolean array pass sees the
complete arithmetic array. No arithmetic node depends on a Boolean node.

Binary folds implement finite conjunction/disjunction. Empty AND is true,
empty OR false, and a singleton fold is its sole reference. Returning a
Boolean reference with numeric index 0 must not be confused with an empty
fold. These conventions give exact semantics for all boundary dimensions.

## 3. Geometric primitives translated without omitted cases

Define the following arithmetic expressions using +,-,multiplication nodes:

    O(a,b,c) = (bx-ax)(cy-ay)-(by-ay)(cx-ax);
    D(a,b,z) = (z-a).(z-b);
    dist2(a,b) = D(b,b,a).

Define Opp(u,v) as (u<0 AND v>0) OR (u>0 AND v<0), and Same(u,v) as
(u<0 AND v<0) OR (u>0 AND v>0). If either argument is zero, both predicates
are false. They are not logical complements. They implement uv<0 and uv>0.

The predicate circuits are then:

On(a,b,z): O(a,b,z)=0 AND D(a,b,z)<=0.
Proper(a,b,c,d): Opp(O(a,b,c),O(a,b,d)) AND Opp(O(c,d,a),O(c,d,b)).
Meet(a,b,c,d): Proper OR On(a,b,c) OR On(a,b,d) OR On(c,d,a) OR On(c,d,b).
Adjacent(a,b,c): O(a,b,c)!=0 OR D(a,c,b)<0.
RayHit(z,a,b): Opp(zx-ax,zx-bx) AND Same(O(z,a,b),ax-bx).

D(a,c,b)=(a-b).(c-b), so Adjacent allows a straight-through subdivision
but rejects collinear reversal. RayHit retains the forward direction,
including its denominator sign. Meet retains all closed-contact cases;
it must not be replaced by Proper on edge-avoidance calls.

Apply the extension induction to these displayed formulas. It proves each
primitive's equality with c11's predicate on ALL real endpoint assignments,
including zeros and contacts. No GP premise enters this local translation.

## 4. Complete semantic clause list

Create one Boolean reference for each c11 semantic clause, recording its
block and the indices of its graph/polygon objects. Conjoin the complete
list to obtain the circuit root. The required counts are:

distinctness: C(n+m,2);
nonadjacent polygon sides: m(m-3)/2;
adjacent polygon triples: m;
signed-area nonzero: 1;
initial prefix parity: n;
point-boundary avoidance: nm;
vertical-ray generic guards: nm;
crossing-bit Boolean equations: nm;
ray-bit linkage: nm;
XOR prefix steps: nm;
final prefix parity: n;
edge avoidance: e;
nonedge proper-crossing witnesses: C(n,2)-e.

The polygon-side indices are cyclic. The nonadjacent list skips consecutive
pairs and (0,m-1), and only those pairs; it is empty when m=3.
The signed area is the sum over all cyclic consecutive corners, with either
orientation permitted. There is no all-triple general-position block.

For each graph point i and side a, use exactly these five middle clauses:

    NOT On(q_a,q_(a+1),p_i);
    (q_a)x != (p_i)x;
    c(i,a)(c(i,a)-1)=0;
    (c(i,a)=1 AND RayHit) OR (c(i,a)=0 AND NOT RayHit);
    b(i,a+1)=b(i,a)+c(i,a)-2b(i,a)c(i,a).

Also include b(i,0)=0 and b(i,m)=0. It is insufficient to include only
the recurrence. For each edge use NOT OR_a Meet. For each nonedge use
OR_a Proper. All coordinates and bits use the map from Section 1.

Primitive correctness gives equality of every listed clause. The full AND
fold gives equality of the root. Their total number is
C(n+m,2)+m(m-3)/2+m+1+5nm+2n+C(n,2). This is a count of semantic clauses,
not of circuit nodes or final lifted equations. A count check alone would
not detect replacing one clause by a duplicate of another, hence the
object-indexed block map and induction are necessary.

## 5. Composition and finite-size scope

The construction is finite and has size O((n+m)^2+n^2 m+nm+m^2) when
bounded-fanin primitive circuits are duplicated a constant number of times.
It does not require expansion into disjunctive normal form or a generic
SMT parser. The graph's edge list can be stored as a finite membership table.

By c13/c14, for a circuit produced by this construction,
C(sigma(X)) iff there exists a lifted real assignment Y satisfying its
quadratic equations and linear nonnegativity constraints. Therefore
S(X) iff exists Y Q(sigma(X),Y). This projection is pointwise; the
additional claim about a GP-ALL geometric representation is only an
existence claim inherited through c07/c04 and c01 geometry.

c14's current default engineering caps need not accommodate every circuit
from every dimension-bounded graph. A future front end must reject over-budget
construction with a resource-refusal status, not emit a false circuit.
Only the circuit field, not a containing metadata envelope, is valid c14
input. A dictionary being well-typed does not prove it corresponds to the
intended graph.

## 6. Exact raw-witness mutation fixtures

All values below are hand-derived expectations, not executed outputs.

A. K2, m=4, anchors (0,0),(1,0), cyclic polygon
(-1,1),(1/2,1),(2,1),(3/2,3). The first three corners are collinear in
straight-through order. The middle adjacent dot product is -9/4; signed
double area is 6. Both anchors and the graph edge are below the obstacle.
Vertical-ray crossing rows are (1,0,0,1) and (0,1,0,1), with prefixes
(0,1,1,1,0) and (0,0,1,1,0). Thus every sparse clause holds. Adding the
old all-triple GP block rejects this raw witness and breaks pointwise
translation, even though a separate GP perturbation preserves existence.

B. No-edge graph on two anchors, m=3, triangle
(1/2,0),(1/2,1),(-1/2,1). The first ray has crossings (0,1,1), the second
(0,0,0); both have even parity. The graph pair only touches the bottom
corner. Meet is true and every Proper is false. Exactly the nonedge
strict-crossing clause must reject this fixed assignment. It is not a
graph-level obstruction to another possible representation.

C. The c06 negative-t triangle for K2 has both anchors inside and honest
odd final parity. Side nonintersection alone passes. Dropping final parity
or dropping a semantic clause from the root can admit a false witness.
The existing c06 fixtures provide both cyclic orientations.

D. Mapping n rather than d original variables loses corner and parity
coordinates; making anchor coordinates free also changes the normalized
pointwise statement. A correct count does not establish a correct name
permutation; the explicit bijection is the decoder contract.

E. A valid numeric index in the wrong intended same-sort position can pass
c14's structural validator. The primitive/loop semantics proof cannot be
replaced by a type check or a matching total clause count.

## 7. Unexecuted replay and continuation

The accompanying fixture file stores graph parameters, rational coordinates
and original auxiliary bits, not constructed circuit nodes or solver outputs.
A future replay must construct the circuit, verify all input names, demand
exact input-key coverage, and evaluate every node and each mapped clause
with exact rationals, including the root and both parity endpoints.

The prepared source was only AST-parsed and byte-hashed locally. Its GitHub
write was blocked; no front-end source file was committed. No module,
dependency loader, graph builder, validator, backend, SMT parser, solver or
fixture evaluator was run. This proof artifact is useful without pretending
that the implementation or verification stages occurred.

Planned replay budget: one process/thread, 512 MiB memory, 60 seconds per
tiny fixture, at most one MiB output, no automatic retries. Versions and
frozen inputs must be recorded by an authorized runtime. Semantic replay,
geometric faithfulness, unrestricted completeness and both root questions
remain open.

Sources: c11 sparse exporter/contract, c13 lifting proof, c14 circuit contract,
and c06/c07 predicate/degeneracy candidates at the declared base. The displayed
construction uses no additional mathematical theorem as an unstated premise.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
next_action: formal replay of the blockwise construction or a complete-input
exact evaluator specification; executable front-end publication remains blocked.
