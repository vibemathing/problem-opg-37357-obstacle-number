# C28 verification request: exhaustive SAT, actual polygon and ternary threshold

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
request_kind: verification_request_not_receipt
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
Target: obligation:opg37357-root
Base: f09892bdb8e26edcdfc80edacc2790de904a70ea

## Frozen claims and separate gates

1. Check the 32-variable, 1140-clause octahedral h=2 necessary formula and
its per-row actual path/tuple origins. coupling.py does not import C22/C26.
second_check.py reconstructs every clause by a different path enumeration and
checks completeness, not just whether supplied rows are individually valid.
The common-component guard applies only to targets assigned the same label;
all modules share the same real placement and orientation table.

2. Replay both exhaustive methods: 2^20 orientations x eight labelings, with
exact elimination of the six side variables; and scalar direction prefixes
with a full 512-position label/side table. Their projected count is 15952,
full count is 807232. Rejected orientation prefixes count all completions.
The number 11904 is orientation-rule survivors, NOT a count of real placements.

3. Check the least Boolean model, coordinate orientation binding, graph-edge
and point avoidance, strict three nonedge witnesses, simple polygon boundary,
and plane rotation in witness.json. This model actually has ONE polygon;
it is not abstract SAT awaiting a fabricated ternary exclusion. All eight
specified tip-connector subsets are SAT and have a common component at the
stored rational points. Other diamond gluing operations are outside this claim.

4. Review the sharp abstract ternary threshold: rank-at-least-three constraints
on at most four targets always admit two labels. All triples on five targets
exclude all 32 labelings. No planar all-placement realization of the latter
incidence pattern is asserted. The next geometric obligation is still to force
five (or more) targets with per-component capacity at most two at EVERY placement.

T: C19 tube/Jordan is not needed for the explicitly given octahedral polygon;
its general extraction is a separate dependency for arbitrary component witnesses.
A: C27 finite-segment core is reused with an exact source hash, not republished.
P1: the prior X4 bridge is unchanged. P2: only this finite interface is rejected;
no obstacle-number-three planar example or uniform planar bound is produced.

## Execution and exact bytes

All final commands exited 0 in CPython 3.13.5, with externally enforced 30 CPU
seconds, 40 wall seconds, 512 MiB and 4 MiB output. The main run took 3.826872
seconds. Sixteen structural/clause/path/model/polygon/rotation mutations were
rejected. Valid connector-edge deletions were recompiled, not rejected as inputs.
Sources are readable text without network/process/dynamic-code/file operations;
the entry prints stdout. Two implementations remain in the SAME candidate
trust domain, not a trusted verifier-domain separation.

The complete DIMACS and row-origin TSV are deterministic exports of delivered
source, actually emitted in this run, not additional signing receipts:
DIMACS SHA-256 8ff2ede8552a931ff6396381a76f5961eaa0135c5227ceb72d8fbecdcb98f4aa
Sources SHA-256 74b15181d4c3c1b1b2924060ac528ba5d0c771692d76cbda0c5265bb7ffc7814
Commands (existing C27 on PYTHONPATH): python -B checks.py [--cnf | --sources].
Default stdout contains the full formula and all sources as well as the model.
The nine published candidate files carry the executable specification, witness,
compact observations and real execution identity; raw exports are rebuildable
caches, not separate GitHub files in this packet.

## Candidate digests

research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/README.md
  SHA-256 c8d0c6608db916a47cf20d9b32c176630eda055e1093f8c47b1df238f961e8b2
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/coupling.py
  SHA-256 8f45d8e8605c6347c486bd11ec91d0f30eabf58354522189243e8861bdcb681b
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/exhaustive.py
  SHA-256 31d2b29b6f75ef6b90d4e313071f8a40e8efb5952881aa3308ccc1257d492eb4
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/second_check.py
  SHA-256 171e1c685d4be4348a2b1d23032be323543c0d0dd27554d5a61b91fab5ae0bf6
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/geometry.py
  SHA-256 bbab0b90786c7e330982f12377525594877ae2cb0b7aa8f86c77c828709058b8
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/checks.py
  SHA-256 407c291d276e2f1ec7e6ef022d92c42643bea04fd117d321b3a21aa7c22fd2b8
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/witness.json
  SHA-256 c9214b2330a8c29847b1c49723c0e859d1f9e25294f5662ea80b83e76004b9e8
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/observation.json
  SHA-256 3cb6eb886c4d8a210e4413357dcc34324a190ceaa5a92e8f5873d9c477f09df7
research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/execution.json
  SHA-256 156906fb93edc5e6b91c115931306549905b477e926e960e274071e80392dc5a

## First missing trusted gate

Fresh registry research/verifiers.json has Git blob
b93b32955eb94c3b4ee82f045f7bbb85fd900f05 and fixture policies only. There is
no compatible registered mathematical invocation/closure receipt for this
finite enumeration, polygon semantics or placement-universal growth claim.
Request actual consumer fingerprint/input/receipt, statement-faithfulness and
axiom/escape audits through the registered closure process. Do not interpret
ordinary PR checks as such a process. No EvidenceLink/Result/Solution is written.

The failed-route proposal is restricted to the eight explicitly listed graphs;
route fingerprint: 74eac95efca2274008457c408260f9253d10df5642f861d888c4343afe703db7
No protected failed-route ledger is altered. Root remains open.

best_verified_candidate: none
best_verified_result: none
next_action: verify this finite rejection, then seek all-placement five-target
triple separation rather than rerunning the failed octahedral coupling.
