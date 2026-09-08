# MIN4 verification request

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root
Protected base: 1a5eefd266401b903f15de10c07b3aff7d3f9773
Frozen candidate/source revision before this request: 4d0f3fd426bc3a9945807b7ea0bc51eaa93af28a
Candidate directory: research/artifacts/candidates/opg37357-a01-min4-eight-v1/

## Requested objects

1. Check the complete rational two-filled-simple-polygon representation in witness.json. Its exact UTF-8 SHA-256 is c0d21807e630be1e0af0da8c8dbc5ec19124ad6d469aa56fc9807b6713931ca1; Git blob d2670108fa280ae1c8822ba690cacdae5549b109. Check all eighteen closed graph edges, all ten nonedges, graph-point exclusion, disjoint filled polygons and strict internal hits. The geometry has 28 and 8 corners. The frozen five targets are 02,14,27,36,57; the interior obstacle hits 14,27,36. Do not infer exact obstacle number one versus two.
2. Check the exhaustive structural certificate through order eight, including complete degree-sorted complement coverage, disjoint isomorphism orbits, every excluded representative's separator or Kuratowski subdivision, sphere rotations, and all 93 deletion cases for the selected graph. Do not accept a library Boolean planarity result alone. structure.json SHA-256: 94df9f2bf7b85706cae6bc9afb94a591d045c3c999255d397d4a20a46a824151.
3. Check all 31676 necessary guarded clauses and their source rows, with 156 variables and all 1502 simple paths. Retain the same-obstacle premise and all four/five-point direction rules. The coordinate-derived satisfying model proves SAT, not exhaustion of all 2^56 directions. C27's common-component/Jordan/positive-margin implications are a separate semantic dependency.
4. Review the all-graph fixed-matching concentration proof in README.md and matching.py. It says that selected matching nonedges can share a free square at some rational GP placement. It does NOT say all other nonedges are blocked or that all graphs have one-obstacle representations. A fixed target set with a three-edge matching consequently cannot obey capacity two at every unrestricted placement. Adaptive target choices are not excluded.

## Repository-only replay surface

Run from the candidate directory, with Python 3.13.5 and NetworkX 3.6.1 only for the producer:

    python -B check_candidate.py < witness.json
    python -B check_candidate.py cnf < witness.json
    python -B check_candidate.py origins < witness.json
    python -B structure_audit.py < structure.json
    python -B mutations.py structure < structure.json
    python -B mutations.py geometry < witness.json
    python -B mutations.py clauses < witness.json

Use external per-command limits: 30 CPU seconds, 40 wall seconds, 512 MiB, one mathematical worker and 4 MiB output. Existing execution.json records the actual delivered-consumer runs and source fingerprints. This request itself is NOT a new execution receipt. Large CNF/source caches are reproducible outputs, not claimed uploaded files.

## Publication and admission gaps

An earlier incidence.py publication was blocked with no commit. No alternate path, encoding, blob or attachment is authorized to bypass it. The unpublished incidence.py/build_witness.py/tube_union.py/replay.py pipeline is not a dependency of the delivered direct checker. The recorded 36-component and fixed-selector computation is a historical generation-domain observation, not a presently delivered incidence reconstruction service. A digest is not source delivery.

The registry currently lists fixture policies, not a compatible geometric implication plus structural-exhaustion consumer and root closure invocation. Requested capabilities are counterexample_check, statement_faithfulness, kernel_check and axiom_escape_audit as applicable. The web principal cannot sign Evidence/Result/Solution. An implementation-diverse local replay is not a different trusted verifier domain. Existing CI checks only transportation.

No all-placement lower bound three, root answer, Result admission or trusted closure is requested to be inferred from a successful PR. Keep C19 tube/Jordan, fixed incidence, the X4 chain and all-order growth separate. Next mathematical step: a different order-nine-or-larger structure, avoiding the fixed-target matching obstruction or using placement-dependent anchored cores.
