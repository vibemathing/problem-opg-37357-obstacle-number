# C21: second exact consumer for frozen C20 certificates

Candidate: candidate:opg37357-a01-c21-second-replay-v1
Verdict: candidate_only
Owner: math-computation
Base: d954f86e02b5b9add474ff970ec56631f8eea458
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Target: obligation:opg37357-bounded-polygon-encoding
Issue: #3

## Deliverable and exact scope

The six Python sources in this directory are a new implementation. They do
not import C20's geometry, arrangement, checker or producer. In particular,
all feasible cell sign vectors are enumerated using strict Fourier--Motzkin
elimination, not C20's samples on the two sides of every face. Input is the
four unchanged, hash-pinned C20 JSON certificates in its data directory.

Run from the repository root in a bounded local runtime:

    python research/artifacts/candidates/opg37357-a01-c21-second-replay-v1/replay.py research/artifacts/candidates/opg37357-a01-c20-finite-arrangement-v1/data

Apply 30 CPU seconds, 40 wall seconds, 512 MiB address space, one process
and one thread externally. No module starts a child process or contacts a
network. The CLI only reads the four specifically named JSON files and
writes its bounded report to stdout. It does not write repository files.

The model supports rational injective drawings with at most 16 vertices and
10 DISTINCT support lines, allowing overlaps, collinearities and vertices
inside nonincident edges. The consumer currently accepts positive tree
certificates only for at least two nonedges; k=0/1 are supported by the model
but not this tree-certificate format consumer. This explicit interface limit
is not a mathematical negative. Fractions have at most 4096 bits per input
numerator/denominator; input files are at most 1,000,000 bytes and positive
trees at most 256 vertices. Errors/refusals are not a fixed-drawing NO.

## Why the different cell core is exact

For any fixed strict sign pattern the rows are a*x+b*y+c>0. Rows with a>0
supply lower bounds x>(-b*y-c)/a; rows with a<0 supply upper bounds of the
same expression. Every lower/upper pair must be strictly ordered. Multiplying
one positive-a row and one negative-a row by positive scalars eliminates x
and gives (a*e-d*b)*y+(a*f-d*c)>0. Rows with a=0 remain constraints on y.

These pairwise strict inequalities are necessary AND sufficient because
there are finitely many lower/upper bounds. At a feasible y their maximum
lower is below their minimum upper. An intermediate rational x exists.
When a side is absent choose one unit beyond the finite bound; when both
are absent use zero. Apply the same interval rule to y. A constant row
requires its constant to be strictly positive: zero is not accepted.
Back-substitution verifies every original row.

Thus all 2^ell sign patterns, with ell<=10, produce exactly all nonempty
open cells. Refinement of one-dimensional faces is checked separately at
all line intersections AND all on-line graph points. No finite bounding
box or float tolerance can omit an unbounded or narrow cell. This argument
is a proof draft for this subroutine, not a kernel theorem.

## Complete checks, not just matching counts

The consumer checks exact input/complement identity, primitive deduplicated
lines, the complete cut lists, every cell and sample, every refined face and
its finite-edge coverage, all zero-faces, canonical component partitions,
and every nonedge's complete interval table. Labels at free concurrence
must agree. It then checks the total intersection of nonedge incidence sets.
A negative certificate must supply a missing target for every component.

Positive trees are checked directly for forbidden points, closed intersection
with each graph edge, all nonincident tree-edge intersections, incident
same-ray overlap, connectivity and acyclicity, strict witness parameters,
roles, retained centers/portals, the leaf census and numerical B17 bound.
These geometric checks use newly written rational determinants/dot products.
They do not construct a tube polygon or prove C19's general Jordan argument.

## Actual bounded replay

CPython 3.13.5 on Linux ran the entry point with the external limits above.
Exit code was 0. The stored replay-observation.json records the actual output:
all four frozen certificates accepted, all 24 damaged certificates rejected,
12 degenerate/near-degenerate model controls checked, and four strict-
inequality smoke cases checked. The four outputs are:

- C18: 12 cells, 15 faces, 3 components, 30 nonedge intervals, no common label.
- Forced-line witness: 2 cells, 4 faces, 1 component, 3 intervals, a 3-vertex tree.
- Square diagonals: 9 cells, 12 faces, 2 components, 2 intervals, a 3-vertex tree.
- Tiny gap: 2 cells, 5 faces, 1 component, 8 intervals, a 5-vertex tree.

The positive tube counts are 6, 6 and 12, checked as 2E+L; these are not
exported polygons. Controls include coincident lines, free and forbidden
concurrence, overlapping edges, a vertex on a nonincident edge, punctures,
partial support-line coverage and a 10^-40 gap. Finite tests do not prove
universal implementation correctness or produce a trusted verifier receipt.

## Delivery audit of the five earlier sources

The five C20 sources were not in the fresh repository and their exact bytes
were not present in the current local artifacts. Only these frozen fingerprints
were available from the merged verifier request:

geometry.py: 1675bfb842e9b9836eda5a821722b0cbe8f3edc912430400f0d33b785d812d64
arrangement.py: 70671996a490775fd3dbc3b00ca80c521ae938223558945f1997a42eff505f4b
checker.py: 5c062a48e885ee453245ede83412f5b77e38fa13fd26e9f4d74659f25c23d52c
selftest.py: b1295744896935eb89278f2967b52f5b21f351641fd29525e8b0fbc99d771a92
run_bounded.py: 6166e2cc0754e7499e25bf068bcf99a5876a167104c2ea1f893127e2fab6877e

A digest cannot reconstruct a source file. Their old bytes have NOT been
claimed recovered, audited safe, attached or resubmitted. The new C21 code
is explicitly separately named and hashed, not an encoded copy of the blocked
artifact. Six ordinary UTF-8 source writes succeeded on the admitted branch.
AST inspection and direct review found no network imports, process creation,
secret/environment access, eval/exec/compile or dynamic importing. The five
math modules have no file I/O. The replay entry reads only pinned local JSON.
Actual source hashes and import inventories are in execution.json.

## Three distinct verification layers and root quantifiers

These are candidate-local review slices, NOT edits to the canonical DAG:

T: C19 tree/tube/Jordan lemma for every embedded finite straight tree.
A: C20 component characterization and complete rational arrangement consumer.
P: placement quantifiers and an all-placement graph obstruction/construction.

C21 checks four instances of A and finite tree inputs to T. It does not close
T as a general theorem and cannot discharge P. With C(G,p) meaning the common-
component condition, one-obstacle existence is EXISTS p C(G,p); Q1 requires
EXISTS planar G FORALL p NOT C(G,p). Q2 additionally asks for a constant
number of obstacles uniform over all planar graphs; rejecting one obstacle
for a single graph does not answer that separate question.

The next root slice selected by the user is the lower-bound route for X4,
not an attempted one-obstacle placement for every planar graph. The repository
already contains an all-placement orientation/key-path necessary CNF and a
stored RUP certificate for X4 (C08 replay-v2). Those, not C18's bad drawing,
are the relevant invariant/certificate chain. Root continuation must separate
its geometric implication from its finite propositional replay and from Q2.

## Admission request and first missing gate

At the base, research/verifiers.json still registers fixture-only SymPy/Lean
policies, with Git blob b93b32955eb94c3b4ee82f045f7bbb85fd900f05. There is no
registered compatible arrangement consumer or invocation contract. This second
implementation is in the same candidate-generation trust domain as the agent;
implementation diversity is not verifier-domain separation. No mathematical
Action, signing receipt, EvidenceLink, Result or Solution is manufactured.

A trusted consumer must first bind its executable fingerprint, the four input
hashes and a faithful claim scope; kernel/axiom and statement-faithfulness
obligations remain separately open. The ordinary PR checks only transport.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
status: NONTERMINAL_CHECKPOINT
next_action: continue the X4 all-placement lower-bound chain after this packet;
retain the old five-source byte-availability gap without treating it as a mathematics stop.
