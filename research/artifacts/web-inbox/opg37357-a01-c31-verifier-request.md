# C31 scoped verification request

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Frozen base: 1ae28cbfb434b792fafc76514afc6cd0641d7316
Candidate prefix: research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/

## Exact requested checks

Verify the tetrahedral face-port graph is simple planar with the six target
port nonedges frozen, while all ten nonedges remain in the witness. Separately
verify the two rational filled simple polygons at p_i=(i,-i^2): simplicity,
all graph points exterior, every whole closed graph edge disjoint, and ten
strict interior nonedge hits. The standalone accepted source runs as

    python -B witness_check.py < witness.json

The frozen direct run exited0 under35CPU/40wall seconds,512MiB,one worker,4MiB
output. It checked79 polygon-side pairs,324 edge/boundary pairs,16 vertex
exclusions and10 hits. Graph-edge crossings27 are allowed. Acceptance of this
witness proves only an upper bound2 for this graph, not exact obstacle number2.

Check the full necessary156-variable/24012-clause guarded formula and its1290
all-simple-path census. Audit determinant implications, positive-clearance GP
regularization and the pair-local Jordan first-exit argument. Same-label guards
must not be discarded or a side reselected per path. Verify the supplied full
model, and distinguish its fixed-coordinate1024-label evaluation from any
unperformed2^56 direction enumeration.

Audit the new symbolic lemma: three REAL graph triangles013,035,036 and the
129-sign guard imply no common free component for targets15,26,47. For each
wall edge e=ab and target uv, define A=D(a,b,u), B=D(a,b,v), H=A-B; compare roots
using A_e H_f-A_f H_e. Signs must preserve root0/1 positions, order/ties, constant
tests and triangle orientations. Eleven zero signs are required. Check all
possible segment triangle-inside words in jordan-certificate.json; their common
intersection is empty. This proof applies to every real GP point of this REGION,
not all placements. A common free component has one constant Jordan word.

Verify the relabeling sigma=(0 1)(2 3)(4 5)(6 7) is an automorphism transporting
the same polygons into a valid representation with targets15,26,47 all label0.
Its changed guard prevents any unconditional use of the new cut.

The exact C27 Fiber comparator gives39 components. Its one-common-component
selector adds78variables/1504clauses. At fixed directions, sixteen key-CNF label
models reduce to eight actual component-cover models; the new ternary condition
removes exactly those eight spurious models. This incidence computation is not
a realizability or universal placement solver.

## Publication and evidence boundary

jordan_words.py write was BLOCKED by the platform, no commit. It was not retried
by another name, encoding, blob, tool or source attachment. replay.py was not
uploaded afterward. Their real executed hashes are recorded in execution.json,
but hashes do not make the full local CLI repository-replayable. The standalone
polygon checker and CNF compiler were accepted and have no missing imports.
The published sign/interval certificate and proof are non-executable data, not
a source-policy bypass. Full emitted CNF/origin/fiber/guard caches are retained
locally with digests; the flat origin emitter is not claimed delivered.

No compatible trusted geometry/closure invocation was found in the current
fixture registry. This is a REQUEST, not a verifier receipt. No signing identity,
EvidenceLink, Result, Solution, or obligation closure is produced. Generator
execution, model self-review, transport gates and merge cannot supply those.
T=C19 polygon conversion, A=fixed incidence, P1=old X4, P2=all-placement root remain
separate. The explicit two polygons do not use T. Do not rerun old failed graph
families as new research. The failed-route proposal excludes only this exact
nonleaf coupling and isomorphic relabelings, not arbitrary planar constructions.

## Frozen candidate bytes

research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/README.md
  cdc3613acb3a6639b8414a77d721b3fab349f699f5f0ee5b1dfd0c8f687417d5
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/witness_check.py
  86be77d1805deb3a134a46ca55641db5b18dbeedcf2a7f31a5ba959b34a828a7
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/guarded_cnf.py
  a1fb730149eb93ad7e21f63a05ebda7389817f1135de86de9bf2fbcf4ad8ede9
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/input.json
  91200aa2fadf32da2957c1eb9fb0fa635bcf76cebf89cbdd9f0595ce9eb3f7e1
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/witness.json
  1605c7406cff347e3d72eed44bef683f3a4914b7569f03be419e2037a752afcc
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/jordan-certificate.json
  8a2cb9e8e1c01ba24ed945f226b20f7cf386a7475cc8fadb7e21b613f4c3ae6f
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/observation.json
  ec77bb5c5efe50ec144fe3c9dd760ac037ba50c05a906932d5f1fe158cf200b9
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/execution.json
  fcfaed0cb3b1a1a6b8899afb513ecc639cbd3533472936d963962e1c42876987

Failed-route fingerprint: 5e87df5ab5ad8f84be012ef02cd6feeb1c491b1b4b067e66300bf82d752ecf8c
