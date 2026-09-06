# C11: sparse quadratic exporter contract

Candidate: candidate:opg37357-a01-c11-export-contract-v1
Verdict: candidate_only
Owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: 6e42ac8958677c1824937ad841804086f6d117b8

## Exact statement and dependency boundary

For a well-formed input G on labels 1..n and integer m, a successful export
denotes the c07 sparse sentence S_(G,m), with pointwise-equivalent sign-split
primitives. Conditional on c01/c04/c07 geometry and translation replay, its
satisfiability is equivalent to a one-filled-closed-simple-polygon visibility
representation in GP-ALL with at most m corners. Planarity is an input promise;
no noncrossing-edge drawing condition is introduced. A raw sparse satisfying
coordinate tuple can be nongeneric: extracting a GP-ALL tuple requires the c07
same-m perturbation argument. This is not an unrestricted obstacle lower bound.

The new source is research/artifacts/candidates/opg37357_a01_c11_sparse_quadratic_v1.py.
It does not edit c05. Before loading any c05 definitions it reads at most
65537 bytes of its sibling source, checks regular-file/no-symlink status and the
SHA-256 46f7dd6e2ca9cdf2148efd763fae6cad6ebab33e79aecf0ee4510b93df827403,
and compiles precisely those checked bytes, not a second read. The dependency
supplies input validation, explicit limits, buffered output, and four unchanged
primitive definitions. Loading a missing/mismatched dependency raises an import
error before any SMT output. This is an environment failure, not false or UNSAT.

## Q1. Pointwise quadratic primitive translation

For real u,v, Opp(u,v) is the disjunction of u<0<v and v<0<u.
Same(u,v) is the disjunction that both are strictly negative or both strictly
positive. The nine sign cells {-1,0,1}^2 exhaust the order cases:
equal nonzero signs give Same, opposite nonzero signs give Opp, and every cell
with a zero gives neither. Hence uv<0 iff Opp, and uv>0 iff Same.
In particular Opp is not NOT Same when zero is possible.

Proper(a,b,c,d) uses Opp on each pair of quadratic orientation determinants.
Meet retains all four On disjuncts as well as Proper. The vertical-ray test is
Opp(z_x-a_x,z_x-b_x) AND Same(orient(z,a,b),a_x-b_x).
Side reversal negates both arguments of Same and swaps the arguments of Opp;
the result is unchanged. No denominator sign, endpoint contact or zero case is
discarded. These are pointwise identities on all real coordinate assignments,
not just GP assignments.

Nonrecursive expansion leaves only quadratic-or-lower atoms: orientations,
squared distances, On dot products, signed polygon area, adjacent-corner dot
products, real Boolean equations c(c-1)=0, and XOR b'=b+c-2bc.
No multiplication of two orientations remains. The formula is still a Boolean
combination, not a single conjunction of quadratic inequalities, and the claim
is syntactic degree at most two, not a runtime improvement.

## Q2. Exact emitted blocks

The p coordinates and all real auxiliary symbol names agree with c05. The
combined-pair distinctness block is retained, and the combined-triple block is
absent. Nonadjacent polygon sides use closed Meet exclusion. Every cyclic corner
has adjacent-ok, allowing a straight-through subdivision but forbidding reversal;
signed area is nonzero. The m=3 nonadjacent-side loop is correctly empty.

Every graph point has explicit On exclusion, q_x != p_x, crossing-bit Boolean
and linkage constraints, and a complete XOR prefix with initial/final zero.
Thus a whole segment inside the obstacle is not misclassified merely because
it misses the polygon boundary. Each graph edge uses NOT OR Meet; each nonedge
uses OR Proper. Polarity and use of closed versus strict predicates are separate
decisions. Replacing the edge's Meet by Proper is not allowed.

For n>=1,m>=3, assertions number
C(n+m,2)+m(m-3)/2+m+1+5nm+2n+C(n,2).
Declarations number 2m+2 max(n-2,0)+nm+n(m+1).
The source checks both counts before returning. Small expected counts are
(1,3):27/13, (2,3):49/20, (2,4):67/26, (3,3):73/29.
For n=24,m=64, 13849 is only the assertion count, not evidence that the complete
output fits the separate one-MiB cap. No combined-GP assertion is silently
reintroduced by a helper. Equisatisfiability still depends on c07.

## Q3. Termination, status and quantifiers

Reuse c05's default n<=24,m<=64, edge-list, assertion and output-byte caps.
Input validation runs before the m<3 false or n=0 true shortcuts. As before,
those constant shortcuts do not expand coordinates and need not satisfy the
nontrivial dimension caps. The stdin-only interface bounds its read; it does
not accept arbitrary solver commands or invoke a network/process/solver.

Return/exit 0 means a complete SMT script was exported, including a possible
assert-false script. Exit 2 denotes invalid input, 3 resource refusal, 4 I/O
failure, 5 an internal invariant failure. Dependency import failure is separate
and precedes the CLI. No failure path substitutes assert false for a refused
mathematical instance. No code calls an SMT solver; check-sat is emitted text.

SMT-LIB's QF_NRA specification uses closed quantifier-free formulas over Reals
extended by free real constants. Satisfiability supplies the existential
interpretation of those constants. No integer quantifier or new free function
symbol is used; define-fun is nonrecursive abbreviation.
Official source: https://smt-lib.org/logics-all.shtml#QF_NRA
Release identity consulted: 2.7; retrieved 2026-09-07.
This format source certifies no geometric or compiler correctness.

## Adversarial specifications and observed work

The regression source fixes expected counts and tests visibility polarity,
cyclic simplicity, all nine scalar sign cells, c06's two-crossing/one-crossing
ray family, side reversal, input rejections, refusals and edge-list ordering.
Those scalar reference tests do not themselves parse the emitted SMT text.
They must not be reported as end-to-end typing/degree or formula-faithfulness
verification. c07's contact-only nonedge must be rejected, even when full Meet
would be true. A sparse collinear-but-valid witness must remain allowable until
the GP extraction step. These latter whole-formula fixtures need the next slice.

Observed here: Python 3.13.5 ast.parse on both new Python sources, UTF-8 byte
hashing and Git blob-identity bookkeeping only. No module, exporter, regression,
SMT parser, solver or proof assistant was executed. Remote required checks are
transport only. No executable mathematical receipt is fabricated.

Planned authorized replay: one process/thread, 256 MiB memory, 30 seconds for
these small regressions, at most one MiB output, no automatic retries. Record
the exact interpreter and frozen dependencies; run
python research/artifacts/candidates/opg37357_a01_c11_test_sparse_v1.py
Then parse the emitted SMT, audit sorts/arity and expanded atom degree, and
evaluate all assertions on frozen rational witnesses without converting fixed
witness rejection into graph UNSAT. A model decoder must report the free
coordinates and auxiliary bits separately. Trusted geometry/faithfulness replay
and the root's two logical questions remain open.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
next_action: derive explicit positive separation certificates for closed-disjoint
segments, then compile a certificate-carrying quadratic conjunction without
losing zero/contact cases or projecting to a different bounded question.
