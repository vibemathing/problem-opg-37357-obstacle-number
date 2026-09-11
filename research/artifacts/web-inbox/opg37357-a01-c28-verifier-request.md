# C28 verification request: complete h=2 test and realized ternary interface

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
request_kind: not_a_receipt
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
Base: f09892bdb8e26edcdfc80edacc2790de904a70ea
Target: obligation:opg37357-root

## Frozen requests and separation of scope

1. Check the exact three-K2,2-port graph, every rotation dart, all 84 simple
paths (including five edges), 72 mixed-module paths and all clause origins.
The graph is minimal only in the declared saturated three-two-terminal-group
template. Neither graph-minimality nor an obstacle-number-three example is claimed.
2. Check the two exact exhaustive methods: 2^20 direction tables, eight
exact-one colorings and exact elimination of all 64 side assignments.
Both give 15,952 direction/color pairs with an extension. Four/five-point
clauses do not certify every surviving direction table's real realizability.
3. Check the minimum tuple (0,0,0), rational points p_i=(i,-i^2), the stored
12-corner polygon and the analytical 38/100 edge-clearance bound. The final
runner verifies component incidence and orientation, NOT a generic polygon
boundary checker. This explicit model invalidates the proposed lower bound
for this graph, not C22/C26 or either unrestricted root alternative.
4. Check the family exclusion: R_t=C_t[empty two-point groups] has n=2t,e=4t.
For t>=4 it is triangle-free and violates planar e<=2n-4. R_3 has one obstacle.
Thus only this exact saturated port-ring amplification attempt fails.
5. Check the four-target realized C18 slice. Pair constraints allow eight
labelings; a ternary empty-intersection clause eliminates 7 and 8, leaving
six exactly valid component assignments. The rejected assignments USE BOTH
colors. This remains a fixed-drawing control, not a universal placement cut.

T (C19 polygon tube/Jordan), A (C20/C21/C27 free-space incidence), P1
(C22/C26 X4 chain), and P2 (placement-universal growth) remain separate.
No old X4 formula, prior source or candidate is retransported. There is no
assertion that all guarded h=2 systems are satisfiable. The next open premise
is a planar nonsaturated construction forcing cross-module ternary cuts for
EVERY real placement, or a verified complete cover of its realizable charts.

## Actual reproducibility and source boundary

From the C28 directory:

    PYTHONPATH=../opg37357-a01-c27-fiber-guard-gluing-v1 python -B controls.py --bundle

Final actual CPython 3.13.5/Fraction/integer run: exit 0, 2.135539 seconds.
Limits: 30 CPU seconds (31 hard), 40 wall seconds, 512 MiB address space,
4 MiB file output, one mathematical process/thread. Fifteen geometry controls
and fifteen input/model/rotation mutations passed their stated expectations.
The runner imports existing C27 fiber.py, SHA-256
7209f677207695d220f7766286fdd94867f75d88a42d35b36cdfdef8d709ba35,
blob 1d00079aafa49149e08c13dcb5c837e886982e5d. That file is not copied or changed.

Development slab_geometry.py was blocked by the platform, with no commit;
its SHA-256 is f87e3b7099fffe3cce0e683bf867aec2db896dc39c5a26380836bed7743180ce.
No alternative encoding/path/upload was tried. Final execution does not use
it; original block checkpoint is Issue #3 comment 5572877352. The delivered
three-source package plus existing C27 dependency is runnable without it.
This is not recovery or publication of that rejected source. No attachment
of the blocked source is supplied. Earlier development outputs are not used
as the final published-source replay record.

Complete CNF/origin cache is 95,624 bytes, SHA-256
94bf19a6788c5b923dfba2dd0d1387bc12fd91d69f0725f6d988f87508109efc.
Native C27 fiber report is 16,832 bytes, SHA-256
85386d0fa08562babff9bdbe1c1e2eb621e2d25dc3676512dd0c69e0d708acfd.
They are deterministic keys cnf.json and fiber-certificate.json in --bundle,
not separately stored files. All published candidate bytes have been matched
to their complete remote Git blob identities. Execution.json differs from
the initial local JSON only in key ordering, not data.

## Published file digests

- `research/artifacts/candidates/opg37357-a01-c28-guarded-h2-ring-v1/README.md`: `6af2f1420dffa6e07df74608e60d8510007d71688c3a89e94a28c167bc2059ed`
- `research/artifacts/candidates/opg37357-a01-c28-guarded-h2-ring-v1/controls.py`: `261b4a0a02e3f3bd5253098d023f24c98d636b23432a8a6461c05d88fe3a14d7`
- `research/artifacts/candidates/opg37357-a01-c28-guarded-h2-ring-v1/execution.json`: `38b6a736454a7f577f2c7f67c10c1ca892bafb9042eae3d39ac7f8d5bb600b8a`
- `research/artifacts/candidates/opg37357-a01-c28-guarded-h2-ring-v1/graph.json`: `329e09efbc68bcc510407574a9f04732d93d00ecd622af56414213df1a27e0a4`
- `research/artifacts/candidates/opg37357-a01-c28-guarded-h2-ring-v1/guarded_cnf.py`: `32b4b1102765d3166a6de7c7eb23c98e92abce5473dc414e69f14ccbb91fb743`
- `research/artifacts/candidates/opg37357-a01-c28-guarded-h2-ring-v1/model.json`: `f0175893f2a15e499563d4c0a647ee1d6121e5faea65d9f386b1188794a5d66a`
- `research/artifacts/candidates/opg37357-a01-c28-guarded-h2-ring-v1/observation.json`: `9b7e3f90a13e160062a7d324f1a1b57b91d9753ee0a80aa88eef0276f72ba3a7`
- `research/artifacts/candidates/opg37357-a01-c28-guarded-h2-ring-v1/rank3-control.json`: `7e6302aa5e43a1f2e703da38a142489d01d7a147dbc7b5d40fa426b1c179b978`
- `research/artifacts/candidates/opg37357-a01-c28-guarded-h2-ring-v1/second_check.py`: `edcfac08a2122d6b8fe382df9e61e80d3cfc36be71ae1e6d3a9bf7bb9c7b021d`

## First trusted admission gap

Fresh registry research/verifiers.json still has fixture policies, blob
b93b32955eb94c3b4ee82f045f7bbb85fd900f05. No compatible mathematical consumer
and statement-faithfulness/axiom/closure invocation contract was found.
The PR's packet/Harness/diff checks are transport only. No mathematical
trusted run, EvidenceLink, Result or Solution is asserted or written.
A registered verifier must bind the exact executable and inputs, confirm
scope and semantic mapping, and issue its own receipt before any closure.
Different counting code in this candidate is not a different trust domain.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: audit nonsaturated planar cross-module ternary constraints with
all-placement fidelity; do not restart saturated port rings or copy-only X4 demands.
