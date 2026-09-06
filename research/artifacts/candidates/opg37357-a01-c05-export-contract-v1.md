# Bounded SMT-LIB exporter: semantic contract and replay plan

Candidate: candidate:opg37357-a01-c05-export-contract-v1
Verdict: candidate_only
Owner: math-formalization
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: 79cdfcaad9ab63d9ea7d84a3b1d1d8341fd0e571

## Frozen function and scope

The accompanying Python source exports c04's exact-m, affine-normalized GP-ALL sentence N_(G,m). It uses one filled closed bounded simple polygon, exterior graph points, and ordinary visibility. It does not require graph edges to form a plane drawing. The graph's planarity is an input promise; the polynomial construction itself is valid for every finite simple graph. There is no GP-V mode hidden behind the interface.

Input has exactly the keys n, edges, m. Labels are integers 1..n; loops, duplicate undirected edges, malformed arrays, noninteger numbers, Boolean labels, and extra keys are invalid. Reordering edges or reversing individual endpoints does not change the export. Duplicate JSON keys and nonfinite JSON numbers are rejected. The standard input/file interface accepts at most 65536 bytes and integer tokens of at most 128 decimal digits.

The result of export_instance is a complete SMT-LIB script, not a satisfiability verdict or a witness. Nonrecursive define-fun macros expand into polynomial arithmetic and Boolean connectives; all free constants have sort Real. QF_NRA satisfiability gives the required existential interpretation of these constants. There are no additional uninterpreted functions, division operations, or universally quantified coordinates.

## Claim E1: returned-script faithfulness (candidate argument)

For a well-formed input whose export completes, the script is equisatisfiable with the bounded GP-ALL representation question, conditional on the c01 and c04 candidate lemmas.

For m<3 it asserts false because a nonempty simple polygon has at least three corners. For n=0 and m>=3 it asserts true: a generic convex m-gon exists and no visibility pair must be represented. These are explicit mathematical reductions, not observed solver outputs. Input validation precedes either reduction, except that a configured resource refusal may terminate validation early without producing any formula.

For n>=1,m>=3, the source fixes p_1=(0,0); if n>=2 it additionally fixes p_2=(1,0). All other graph coordinates and all polygon coordinates are declared once. Real crossing and prefix-parity bits are declared once per indexed occurrence. The source then emits:

1. every combined pair's distinctness and every combined triple's nonzero orientation;
2. every nonadjacent polygon side pair's nonintersection and a nonzero signed-area guard;
3. for each graph point, boundary exclusion, a generic vertical-ray guard at each corner, real crossing bits agreeing with rayhit, and the even-parity recurrence;
4. for each labeled graph pair, the negated side-intersection disjunction for an edge and the positive disjunction for a nonedge.

The nonadjacent-side loop skips exactly m adjacent pairs: consecutive indices and the cyclic pair (0,m-1). An adjacent-side backtracking test is unnecessary because the combined triple guards already exclude collinear adjacent corners. Full onseg/meet predicates are retained despite further GP-ALL simplifications being available. The boundary exclusion and exterior parity guards are not dropped.

These blocks are precisely the finite conjuncts of N_(G,m). The c01 definitions of orient, On, Proper and Meet are expanded without changing sign conventions. Substitution of d=(0,1) gives the rayhit products (z_x-a_x)(z_x-b_x)<0 and orient(z,a,b)(a_x-b_x)>0. The sign of the second factor is retained. The bit recurrence emits b_next=b+c-2bc, with first and final parity zero. Thus the only proof dependencies beyond finite-loop bookkeeping are the explicitly named c01/c04 candidate geometric lemmas. No unrestricted cutoff is inserted by this exporter.

## Claim E2: size/count invariants and refusal boundary

For nontrivial inputs n>=1,m>=3, the expected number of assert commands is

    C(n+m,2) + C(n+m,3) + m(m-3)/2 + 1 + 5nm + 2n + C(n,2).

The terms correspond, in order, to distinctness, general position, nonadjacent sides, area, point/side constraints, parity endpoints, and visibility. Every polynomial has degree at most four. With n>=2, declarations number (2n+2m-4)+nm+n(m+1); for n=1 they number 2m+m+(m+1). The n=0 and m<3 shortcuts have no declarations.

Hand-derived structural regression targets, not observed test output:

| n | m | assertions | real declarations |
|---|---|---|---|
| 1 | 3 | 28 | 13 |
| 2 | 3 | 56 | 20 |
| 2 | 4 | 83 | 26 |
| 3 | 3 | 90 | 29 |

Default expansion caps are n<=24, m<=64, 60000 assertions, and 1048576 output bytes. These caps are conjunctive, so not every pair below the individual n,m caps is necessarily exported. The edge-list scan is capped at 4096 entries before iteration, including for direct API calls. The two constant shortcuts avoid coordinate expansion and need not obey the nontrivial n,m expansion caps. All limits are explicit positive integers.

The builder buffers the whole export and checks byte counts incrementally. The CLI writes no SMT text for a validation, expansion-budget, or internal-invariant failure. An operating-system write failure can of course interrupt delivery; its error is not a mathematical conclusion. File inputs are bounded reads, not unbounded streams. No solver is called, and no external process is spawned by the exporter.

Exit semantics: 0 means export completed (including an assert-false script); 2 invalid input; 3 resource refusal; 4 input/output failure; 5 internal invariant failure. Nonzero exits carry a small JSON diagnostic on stderr. None of these statuses is translated into obstacle number greater than one. A resource refusal at m=65 does not exclude a 65-corner representation.

## Exact coordinate regression seeds (not executed)

Let p_1=(0,0), p_2=(1,0), m=3. For G=K2 use the obstacle ((2,1),(3,1),(5/2,2)); for the two-vertex graph with no edge use ((3/10,-1/10),(3/5,-1/10),(2/5,1/10)). Both combined five-point sets are in general position. Every tested vertical ray has zero crossings, so every crossing and prefix-parity bit is zero. The first pair segment misses the obstacle. The second intersects its boundary at x=7/20 and x=1/2, entering its interior. Reversing the requested adjacency without changing these coordinates gives a rejected WITNESS, not an unsatisfiable graph instance. These seeds will support a separate exact arithmetic evaluator.

The structural suite also attacks Boolean-as-integer input, duplicate reversed edges, duplicate JSON keys, visibility polarity, cyclic side counts, anchor omission, and resource refusals. Balanced parentheses and expected counts alone do not certify SMT typing or geometric faithfulness.

## Observed work versus planned replay

Observed local bookkeeping: both Python files were parsed with Python 3.13.5 ast.parse and their byte digests were computed. Their modules, exporter functions, unit tests and any solver were NOT executed. The repository web profile's command-execution limitation is retained. GitHub structural CI is a separate transport check and does not run the intended mathematical verification.

Planned authorized replay, not a receipt: first record Python and exact SMT parser/solver versions, file digests, environment and axiom scope. Use one process, one thread, 512 MiB memory, 30 seconds for structural regressions and 60 seconds per tiny SMT input, with output capped at 1 MiB and no automatic retries. Run the regression file, then export the two-vertex examples, parse the resulting QF_NRA scripts, and evaluate every assertion on exact rational witness coordinates and integer bits. Compare with a separately written geometric checker, including the c01 degeneracy failures. Freeze outputs and exit statuses. Timeout, unknown, invalid input and refusal must remain distinct from mathematical UNSAT. General equivalence still requires loop-translation, polygon separation/parity, exact-size padding and affine-normalization replay.

Reproduction commands (only for an authorized runtime, from repository root):

    python research/artifacts/candidates/opg37357_a01_c05_test_exporter_v1.py
    printf '%s\n' '{"n":2,"edges":[[1,2]],"m":3}' | python research/artifacts/candidates/opg37357_a01_c05_exporter_v1.py

## Sources and open dependencies

Local proof sources at the declared base: research/artifacts/candidates/opg37357-a01-c01-closed-contact-v1.md and research/artifacts/candidates/opg37357-a01-c04-normal-form-v1.md. The c02 regularization and c03 cutoff are NOT required for the export function's bounded GP-ALL claim.

Official format references, retrieved 2026-09-06: SMT-LIB QF_NRA declaration (language over Reals with free constant symbols), https://smt-lib.org/logics-all.shtml#QF_NRA ; Reals theory signature and arithmetic interpretation, https://smt-lib.org/theories-Reals.shtml . These specify the target language, not correctness of this generator.

best_verified_result: none
best_verified_candidate: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
next_action: exact rational assertion evaluation and geometric witness regression design; do not change the admitted route or protected ledgers.
