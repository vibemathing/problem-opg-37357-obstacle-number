# C13: pointwise conjunctive quadratic lift

Candidate: candidate:opg37357-a01-c13-quadratic-lift-v1
Verdict: candidate_only
Owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: 6e4728e350dc8f47a2dd2e2eb2c77c344a82bd55

## 1. Frozen language and exact claim

Let F(X) be a finite Boolean circuit built from rational-coefficient polynomial
comparisons, with each comparison one of =, !=, <, <=, >, >=, and finite AND,
OR and NOT gates. X ranges over real numbers. No quantifier appears inside F,
no division or partial operation is allowed, and all arithmetic circuits are
finite acyclic graphs using rational constants, +, - and multiplication.

Claim C13.1 (candidate): there is an explicitly constructible finite
CONJUNCTION Q_F(X,Y) of polynomial equations of total degree at most two
and linear nonnegativity constraints, with rational coefficients, such that

    for EVERY real X: F(X) iff there exists real Y, Q_F(X,Y).       (LIFT)

Size is linear in an explicit bounded-fanin arithmetic/Boolean circuit for F.
It is not a polynomial bound in a hypothetical succinct expression whose
circuit has not been supplied, nor a runtime claim about solving the lift.
All Y variables are fresh; the original coordinates and auxiliary parity
bits in X are neither changed nor silently existentially reinterpreted.

The construction below applies directly to c11's expanded sparse formula.
It also applies to c12's separator-augmented formula with its separator
variables included in X, before those variables are projected away.

## 2. Arithmetic wires: no high-degree substitution

Give each arithmetic circuit gate a fresh real output v. For constant c,
input coordinate x, addition, subtraction and multiplication, respectively,
add the defining equation

    v=c; v=x; v=v1+v2; v=v1-v2; v=v1*v2.

These equations are linear or quadratic in the lifted variables. An induction
in topological order proves that for each fixed X there is exactly one
assignment to these wires, equal to the circuit's real evaluation.
A comparison p relation q is first normalized to v=p-q with its own wire.

Crucially, the value of a quadratic polynomial is treated as a WIRE in the
next block. Substituting the original polynomial expression back into a
product would destroy the degree-two assertion. Algebraic degree refers to
the emitted lifted equations, not to their elimination ideal or a projection.

## 3. Total sign gadget with the zero branch retained

For each normalized comparison value v introduce five fresh real variables
P,N,Z,rP,rN and impose the conjunction

    P(P-1)=0; N(N-1)=0; Z(Z-1)=0;
    P+N+Z=1;
    v*rP=P;
    -v*rN=N;
    Z*v=0;
    rP>=0; rN>=0.                                  (SIGN)

Claim C13.2 (candidate): for every real v, SIGN has extensions, and every
extension has (P,N,Z) equal to its actual positive/negative/zero indicator.

Soundness: the Boolean equations and sum-one equation leave exactly one
indicator equal to one. If P=1, v*rP=1 and rP>=0 force rP>0 and v>0.
If N=1, -v*rN=1 and rN>=0 force v<0. If Z=1, Z*v=0 forces v=0.
Thus no wrong branch can be selected.

Completeness: if v>0 use (P,N,Z)=(1,0,0), rP=1/v,rN=0.
If v<0 use (0,1,0), rP=0,rN=-1/v.
If v=0 use (0,0,1), rP=rN=0. All constraints follow directly.
Reciprocals are witness-construction operations, not emitted divisions.
At v=0 nonnegative reciprocal wires can be nonunique; uniqueness of all
auxiliary variables is not claimed.

The truth bit of v>0 is P, of v<0 is N, of v=0 is Z, of v!=0 is P+N,
of v>=0 is P+Z, and of v<=0 is N+Z. Give each atomic truth bit a separate
wire equated to the specified linear expression. Its value is automatically
0 or 1 because the indicators are exactly one-hot.

## 4. Boolean gate compilation and proof of LIFT

Normalize finite-fanin connectives to binary trees, with empty AND true,
empty OR false, and unary AND/OR their input. For each Boolean gate with
input bits a,b and output h impose

    NOT: h=1-a;
    AND: h=a*b;
    OR:  h=a+b-a*b.

Constants have h=0 or h=1. Induction proves h is a Boolean bit and is exactly
the indicated truth value. Extra h(h-1)=0 equations are optional redundancy,
not required for the argument. Finally impose h_root=1.

All gates are compiled unconditionally, not just the apparently selected
branches. Every polynomial has a value at every real X and SIGN always has
an extension at every v. Therefore evaluating a false branch never creates a
spurious feasibility restriction. This totality is important for negation
and disjunction. No existential statement is moved through NOT.

For fixed X, any Q assignment has correct arithmetic wires by Section 2,
correct atomic bits by Section 3, and correct Boolean outputs by the gate
induction. The root equation implies F(X). Conversely if F(X) holds, use the
actual arithmetic values, sign witnesses above, and actual Boolean values;
they satisfy every equation and nonnegativity constraint, including root=1.
This proves (LIFT) without a geometric premise.

With A arithmetic-output wires, C atom occurrences and B Boolean-output
wires, the unshared template introduces A+6C+B variables, A+8C+B+1 equations
and 2C nonnegativity inequalities. Here each atom has five SIGN variables
plus one truth bit, seven SIGN equations plus one truth-bit equation, and
B counts constant gates if represented by separate wires. Sharing identical
values/gadgets may lower the count but is not required. A bounded-fanin
linear scan constructs the template without enumerating DNF sign cases.

## 5. Rational lifting and the square-slack distinction

If X is rational and satisfies F, all arithmetic wires are rational.
The sign witnesses chosen above are rational reciprocals or zero, and all
truth wires are 0 or 1. Thus the displayed lift admits a rational Y for
every rational satisfying X. This statement concerns existence of a rational
extension, not that every extension is rational or polynomially bounded.

Over real numbers one may further replace each constraint r>=0 by a new
equation r=s*s, retaining the separate r wire. This yields a conjunction of
quadratic equations only, because both r=s*s and v*r=P are quadratic.
Real equivalence uses existence of square roots for nonnegative reals.

However, that further equality-only variant need not have rational
extensions for rational X. For the formula v>0 at v=2, P=1 forces rP=1/2,
so a replacement rP=s*s requires s=+/-1/sqrt(2), which is not rational.
The preceding inequality version still has the rational certificate rP=1/2.
Do not conflate these claims. Substituting v*s*s=P directly would also be
cubic rather than quadratic, another distinct error.

No rational or real witness-size bound, NP-membership assertion or unrestricted
obstacle-number conclusion is obtained from this syntactic lift.

## 6. Mutation counter-assignments and guard audits

These are exact hand-derived audit inputs, not executed tests.

M1. Delete nonnegativity of rP: v=-1, (P,N,Z)=(1,0,0),
rP=-1,rN=0 satisfies all remaining SIGN equations while reporting v>0.
Keeping the reciprocal-product equation alone is insufficient.

M2. Delete Z*v=0: v=1, (P,N,Z)=(0,0,1), rP=rN=0
satisfies the other constraints while reporting v=0. The zero branch
requires its own equation, not just absence of nonzero witnesses.

M3. Delete P+N+Z=1: v=1 with P=N=Z=rP=rN=0 passes the remaining
constraints and reports v!=0 as false. The formula NOT(v!=0) then has
a false positive extension under the mutated gadget.

M4. Replace OR with h=a+b: at a=b=1 a logically true OR forces h=2;
a root equality h=1 incorrectly rejects it. The product correction is
necessary unless one has separately proved mutually exclusive inputs.

M5. Atom-wise sign witnesses must be freshly named or deliberately shared
only for the exact same value. Sharing rP between v=1 and v=2, both required
positive, forces simultaneously rP=1 and rP=1/2 and creates false infeasibility.

M6. Arbitrary free truth bits are not acceptable. Atomic bits are constrained
by SIGN and Boolean output wires by defining gate equations. Leaving even
one atomic bit disconnected can satisfy a false root clause.

M7. Uniformly bounding reciprocal wires changes the projected set:
for the atom v>0, P=1 forces rP=1/v. A bound rP<=B with B>0
excludes all 0<v<1/B. The unbounded auxiliary range is exactly what
allows strict inequalities to be represented by equations and weak
nonnegativity after projection. No universal cap may be added merely
because a numerical solver prefers a bounded search box.

## 7. Application and exact non-implications

For S_(G,m) from c07/c11, (LIFT) gives S(X) iff exists Y Q_S(X,Y).
Combining with c07 gives existence of a bounded GP-ALL polygon representation,
conditional on the geometric candidate proof and source translation. A raw
X assignment can remain nongeneric; lifting does not fix this automatically.

For the c12 hard-slot replacement T(X,W), apply LIFT with (X,W) as original
variables. Then

    S(X) iff exists W T(X,W) iff exists W,Y Q_T(X,W,Y).

This composition preserves the exact projected original witness set. The
separator lemma and the total sign-gadget lemma have different hypotheses
and should receive separate replay rather than being hidden in one solver
success. The finite obstacle corner budget remains m throughout.

Any engineering cap in a future compiler yields a refusal, not the equation
1=0. The mathematically false formula may legitimately compile to an
inconsistent conjunction; these two output statuses must remain distinct.
No numeric search, SAT/UNSAT result, formal kernel run or mathematical
receipt was produced by this proof artifact.

## 8. Provenance and next verification slice

This is an explicit elementary arithmetization, with no novelty claim.
It is derived from the displayed real ordered field sign cases and finite
circuit induction. The c11 contract supplies the exact intended input formula;
the c12 separation candidate is optional, not required for the basic lift.
No unspecified external theorem or solver behavior is a proof premise.

Required replay: arithmetic wire induction, total SIGN correctness for all
three sign cases, NOT/AND/OR induction including constants, output projection,
and the rational-extension versus square-slack distinction. The implementation
slice must pin a typed circuit format, forbid forward references/cycles, bound
input and output, preserve fresh names, and compare every generated block
against the theorem. Static syntax success would not discharge those duties.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
next_action: build a bounded typed-circuit compiler for Q, with exact
counter-assignment fixtures and degree/arity checks; preserve no-execution
status until an authorized runtime actually replays the frozen inputs.
