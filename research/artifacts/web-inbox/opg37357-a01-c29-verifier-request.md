# C29 verification request (not a receipt)

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Target: obligation:opg37357-root
Mathematical execution base: f09892bdb8e26edcdfc80edacc2790de904a70ea
Synchronized packet base: 61943c788f95f91874b99b77f06b4b8c898a6db7
Non-force synchronization commit: 1059b792c8fa8c50ae3a8a76f6cb80a781627c25

## Exact claims, separated from admission

1. Replay all 27 explicitly labeled triangular-prism face completions. All
simple paths through five edges, every direction assignment and every one-hot
valid two-label assignment are covered. Side variables are eliminated exactly,
not sampled. Every formula is SAT; smallest full models and every CNF hash are
frozen in family-results.json. Scope is this finite family, not all planar graphs.
The seed has 62 variables, 2106 clauses, 54 paths and 42 cross-module paths.
Across the family: 536870912 projected assignments and 924356 satisfying pairs.
Audit producer.py and the separately written audit.py without trusting either.

2. Check the rotation/dart certificates and the rational plane drawing of all
27 completions. Their planarity drawings do not constrain obstacle placements.
Check the necessary implication using one component PER LABEL from the SAME
placement, with C26 robust clearance before GP normalization. Local side choices
are shared across a target pair's paths, but apply only under same-obstacle guards.
Neither direction axioms nor a SAT model certify full geometric realizability.

3. Check the actual common-component control for the seed p_i=(i,-i^2), using
C27's byte-pinned fiber comparator; it is not republished. The other 26 Boolean
models are not claimed to have exported obstacles. C19 polygon conversion is
separate; no polygonal output or kernel proof is generated here.

4. Check the new six-target profile consisting of every pair of four components.
Pair-only exclusions leave eight two-label models; four ternary exclusions remove
all eight. Integer cover is three while the fractional weight/cover optimum is
two. Six selected nonedges of the rational K4-plus-isolated-points drawing realize
this profile. It is ONE drawing, not an all-placement or abstract graph lower bound.
Check every missing-component source of a projected monochromatic exclusion.
The all-placement coupling of these targets is the first open geometric obligation.

5. Replay the 4096 four-target incidence profiles on three components (65536
label cases), all 14 source/graph/CNF/rotation mutations and three affine controls.
These are bounded tests, not universal consumer correctness or trusted receipts.

## Reproduction and fingerprints

Published directory: research/artifacts/candidates/opg37357-a01-c29-prism-rank3-v1/
Run python -B run_census.py --completion CODE for each CODE=0..26.
Run python -B run_census.py --cnf or --formula for the full seed formula/sources.
Run controls.py with the existing C27 directory on PYTHONPATH.
External per-command limits: 30 CPU seconds, 40 wall seconds, 512 MiB address
space, one mathematical worker and 4 MiB stdout. Actual CPython 3.13.5 execution
records, repaired batch timeout and emission hashes are in execution.json.
The six math source files have no network, subprocess or dynamic execution;
stdout is the only external mathematical output. Old C20 bytes are not recovered.

research/artifacts/candidates/opg37357-a01-c29-prism-rank3-v1/README.md
  SHA-256 c6c259fb0c866c71b0725c68bd22dc35d86e3e78c6619eef52a756905127ae5b
research/artifacts/candidates/opg37357-a01-c29-prism-rank3-v1/seed.py
  SHA-256 8557e38e9519cfae085601b1394b41a90d2067422321d01c14759f623d6c58b6
research/artifacts/candidates/opg37357-a01-c29-prism-rank3-v1/producer.py
  SHA-256 2228e0ecce7aedc35ab322fa8be2636b32e3709ca7bbc171da15b1fc9f874a44
research/artifacts/candidates/opg37357-a01-c29-prism-rank3-v1/audit.py
  SHA-256 0c9d0551e4b4f2b99d33e707c286694e0d70bedb0f8c84f944bd02edca3090b0
research/artifacts/candidates/opg37357-a01-c29-prism-rank3-v1/run_census.py
  SHA-256 991b5fe7f1b99d1ce4f34700d27772897923941420c7b14db9e0330ae53e813e
research/artifacts/candidates/opg37357-a01-c29-prism-rank3-v1/controls.py
  SHA-256 a1a4b0841dab508b484fc1f960b6139037907394a0d86bcc38074148ae48adc3
research/artifacts/candidates/opg37357-a01-c29-prism-rank3-v1/rank3.py
  SHA-256 73211f05be70855eb5ca991c07b03f5981dfc9107c557a220e9a0e9ba0ecec53
research/artifacts/candidates/opg37357-a01-c29-prism-rank3-v1/family-results.json
  SHA-256 fc1bf96a85d9370e811b56231f919572063110b08ae06f7354873174dbd40689
research/artifacts/candidates/opg37357-a01-c29-prism-rank3-v1/controls.json
  SHA-256 db9daf351d0357886fbf270c54ef3ea52d6b1c9489fb9093f96ef0976098ce58
research/artifacts/candidates/opg37357-a01-c29-prism-rank3-v1/execution.json
  SHA-256 dbefbc52fed25f1e1f2ed9df3cb6a30e8b87a50aa75f8b88f6704ee9f3ca0e68

These hashes are from actual local bytes matched to the complete remote blobs.
Emitted caches seed.cnf, seed-formula.json and raw per-code outputs are not
separately published; their exact data are reproducible from the pinned source.

## Failure proposal and next gate

Failure fingerprint: e4be5daf44a9e2b2d222be4185b1a87fcdbe7de3ec5c43590ab25b6bae0142ed
Only the proposed UNSAT route on these 27 prism formulas is excluded by the
frozen SAT models. No failed truth record, EvidenceLink or Result is appended.
A compatible trusted consumer must bind its executable identity, frozen inputs,
axiom/escape and statement-faithfulness review to the actual closure gate.
At synchronized main research/verifiers.json still has fixture-only policies
(blob b93b32955eb94c3b4ee82f045f7bbb85fd900f05); no compatible invocation is registered.
No trusted run, mathematical signing capability or closure receipt is claimed.

T=C19 tube/Jordan; A=C20/C27 fixed incidence; P1=C22/C26 X4; P2=placement-universal
ternary growth remain separate. The root's uniform bound over all finite planar
orders is not settled by finite SAT, the integer gap or transport checks.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: force or disprove the ternary integer profile at every placement,
with a simple planar coupling construction; do not recycle the excluded prism
formulas or the X4-copy-only relaxation. NONTERMINAL_CHECKPOINT.
