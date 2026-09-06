# C14 typed circuit compiler and witness contract

Candidate: candidate:opg37357-a01-c14-compiler-contract-v1
Verdict: candidate_only
Owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: 3ee1546d580fa56b9b5b25b5d3ec82caeabb8f6d

## Interface and scope

The Python candidate compiles the explicit acyclic circuit language below to
the c13 quadratic conjunction. It is NOT a c11 SMT-LIB parser or a complete
polygon-to-circuit front end. The outstanding front-end mapping must preserve
all polygon predicates, anchors, variable meanings and indexed constraints.
Generic circuit correctness alone is not end-to-end geometric faithfulness.

Input has exactly inputs, arithmetic, boolean, root. inputs is the nonnegative
count n of original real variables x0,...,x(n-1), not the number of graph vertices.
The two node arrays have zero-based indices. All references are strict Python
integers: JSON booleans are not accepted as indices or dimensions.

Arithmetic node forms:
- {"op":"input","index":i}, with 0<=i<n;
- {"op":"const","value":"p/q"}, or an integer string, denominator positive;
- {"op":"add"|"sub"|"mul","args":[j,k]}, both references smaller than this
  node's index in the arithmetic array.

Boolean node forms:
- {"op":"const","value":true|false};
- {"op":"atom","value":j,"relation":"eq"|"ne"|"lt"|"le"|"gt"|"ge"},
  referencing an arithmetic node's value compared with ZERO;
- {"op":"not","arg":j}, referring to an earlier Boolean node;
- {"op":"and"|"or","args":[j,k]}, referring to earlier Boolean nodes.

The displayed alternatives are grammar notation, not literal valid JSON.
Each real input JSON node has exactly the keys of its chosen form.
root is a valid Boolean index, so a Boolean array cannot be empty.
True and false are represented by constant nodes. Empty/unary connectives
must already have been normalized by the producer; they are not silently
invented by this format. Full validation precedes any output construction.

## Candidate compilation claim

For every accepted finite circuit F and fixed original real input x, the
emitted conjunction has an extension exactly when F(x) is true, conditional
on c13 and source-to-template replay.

The arithmetic pass emits a_i=x_j for input nodes. A reduced rational
constant p/q is emitted as q*a_i=p, with q>0 and a properly formatted negative
SMT numeral when needed. No variable or constant division is emitted. Every
other arithmetic node emits one addition/subtraction/product wire equation.
Forward references and cycles are excluded structurally by the earlier-index
checks, not by a hope that an evaluator will terminate.

Every Boolean atom gets its own P_i,N_i,Z_i,rP_i,rN_i. Seven SIGN equations,
two nonnegativity constraints, and one truth-wire equation implement c13.
For a comparison eq on a positive value, P_i=1 and Z_i=0 while the atom's
truth bit t_i=0. Sign indicators describe the underlying value, not the
selected comparison's truth. Conflating those concepts is a likely decoder bug.

Each remaining Boolean node emits its one defining constant/NOT/AND/OR
equation. All nodes, including those outside the root's dependency cone,
are compiled. Their operations are total, so they do not restrict original
inputs beyond correct values and sign witnesses. Finally t_root=1 is emitted.

With A arithmetic nodes, B Boolean nodes INCLUDING C atom nodes, counts are:
- declarations n+A+B+5C;
- equations A+B+7C+1;
- nonnegativity inequalities 2C.
These agree with c13's count after identifying its non-atom Boolean count
as B-C. The source checks all three output counts. Every emitted assertion
is an equality or a nonnegativity comparison. Degrees are at most two by
the individual templates, without macro expansion or DNF enumeration.

## Explicit boundedness and error meanings

Defaults: <=512 original variables, <=8192 nodes in either array,
<=100000 constraints, <=262144 input bytes, <=1048576 output bytes,
<=256 characters per rational string. Integer JSON tokens are capped at
128 digits. Duplicate JSON keys, floats, nonfinite values, wrong keys,
unsupported operators, wrong-type references and out-of-range references
are rejected. No user-controlled identifier text is copied into SMT names.

These independent caps do not guarantee that every dimension-bounded input
fits the byte cap. Output is buffered, then returned once complete. The CLI
reads at most one byte beyond its cap and emits no SMT text for an input or
budget failure. External I/O failure can interrupt delivery and is not a
logical outcome. Defaults are finite safety limits, not theorems about
polygon coordinates, circuit size or universal obstacle bounds.

Exit 0 means compilation completed, including a false-root conjunction.
Exit 2 is invalid input; 3 is resource refusal; 4 is I/O failure; 5 is an
internal template-count failure. The compiler never invokes a solver,
network call, subprocess or other candidate module. No actual satisfiability
verdict is returned. check-sat in the output is text, not an executed action.

## Frozen whole-assignment fixtures

The companion JSON supplies a three-node Boolean circuit
(x0>0) OR (x0=0), with one arithmetic input wire. Its expected counts are
15 declarations, 19 equations and 4 inequalities. It also supplies complete
rational assignments at x0=2, x0=0 and x0=-1.

At x0=2 the gt atom is true and eq atom false, with BOTH sign gadgets in
their positive branches. At zero only eq is true. At -1 both atoms are
false and t_root=0, so all equations except the final root requirement
are expected to hold. That is rejection of this fixed original assignment,
not UNSAT of the existential circuit, which has other satisfying inputs.

The false constant circuit has zero arithmetic nodes, one Boolean node,
one declaration and two contradictory equations t0=0,t0=1. The true
constant circuit has the same counts but consistent equations. Invalid
self/forward/cross-sort references are not encoded as the false circuit.

Fixture statuses are derived expectations only. The JSON is not a receipt.
Before using an assignment, a replay checker must require EXACT equality
between declared names and assignment keys, reject missing/extra names,
parse rational strings exactly, and evaluate every assertion including
the final root. A loose checker that checks only all supplied bindings
can accept an empty dictionary vacuously. An assertion parser must also
check operator arities/types, rather than relying on balanced parentheses.

## Observed work and next replay

Only Python 3.13.5 ast.parse on the new source plus UTF-8 JSON/hash
bookkeeping was performed. The compiler module and its functions, fixture
evaluator, SMT parser, solver and formal verifier were NOT executed.
No output script digest or test PASS is reported because no such execution
occurred. The data file and source hashes refer to prepared input bytes.

Planned authorized replay: one process/thread, 256 MiB memory, 30 seconds
per tiny fixture, at most one MiB output, no automatic retries. Record
interpreter/parser versions and frozen source hashes. Run the compiler
on the fixture circuit, verify counts and exact declared-name sets, then
evaluate all constraints on the three rational assignments. Also test
duplicate keys, Boolean-as-index, a self-reference, wrong-sort reference,
false constants, negative rational constants, and independent budget caps.
Finite checks do not replace general c13 or compiler-loop induction.

The next mathematical translation obligation is the missing c11 formula
front end: either parse the narrowly frozen SMT fragment with explicit
macro expansion/type rules or construct the circuit directly from indexed
polygon predicates. Both approaches must reject unsupported syntax rather
than silently dropping conditions. A proof-producing circuit construction
is preferable to a permissive generic SMT parser.

Sources: the repository's c13 total-sign lifting proof and c11 exact sparse
export contract at the declared base. No library or external theorem beyond
those explicit candidate premises is used to justify correctness.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
next_action: direct typed-circuit construction for all polygon primitives,
with node-level semantic invariants and exact full-assignment checking.
