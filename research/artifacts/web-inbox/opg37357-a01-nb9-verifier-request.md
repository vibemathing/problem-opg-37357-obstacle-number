# NB9 verification request (not a receipt)

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Target: obligation:opg37357-root
Base: d21e5e28613b18e6960a0ce68b0b3051356ac8b5
Candidate prefix: research/artifacts/candidates/opg37357-a01-nb9-edge-expansion-v1/

## Requested frozen claim

For the nine-vertex graph in input.json, the exact points and two closed filled simple polygons in witness.json represent every graph edge and every nonedge. Consequently this graph and its isomorphic copies are not obstacle-number-at-least-three candidates. This is not a root result and does not decide obstacle number one versus two.

The direct consumer polygon_verify.py does not import the obstacle constructor, arrangement code or CNF producer. It checks complete edge/nonedge census, interpolation, point exclusion, Jordan boundary simplicity, strict hits and disjoint disks. Its implementation diversity is not a different verifier trust domain. A trusted proof must also justify the finite predicates-to-filled-disk implication and match the frozen ProblemContract conventions.

The all-simple-path guarded-CNF extension is a separate claim: 309 variables, 128148 clauses, 5208 paths, maximum length eight. Every clause/source is reconstructed by clause_verify.py using a different path/parity method. This supports finite compiler correctness, not exhaustive real-order-type coverage.

The fixed selector and anchor computations take a supplied incidence observation. They must not be admitted as a proof of incidence completeness. Both actual valid label classes use one common component each; the 51 minimal empty families are pairs. No nonredundant ternary cut arises here.

## Replay surface and budgets

From the candidate directory run python -B replay.py polygon, audit, interface, mutations, guard, omit, flip, path. Full deterministic outputs: cnf, origins-a, origins-b. Apply external 30 CPU seconds, 40 wall seconds, 512 MiB, one worker and 8 MiB regular-file output cap per command. execution.json binds actual runs and source/output fingerprints.

witness.json SHA-256:
1d8761dad776758574405686d781db857163437377f051019d22313bf3415473
CNF SHA-256:
6ee78d2b5fe1e5bfb2e4e79f9fa0b5ee8460fd2724db5dd2ba8a1fec7b90f199
Complete origins SHA-256:
0702dd8e7c97ee74211394eb3f8a8591babc19e59317c8bd614017d8d891afad

## Publication and admission gaps

plane_with_outer.py, SHA-256 d65b530b6f6d5ac899602e40fefa61f48ad1fd0d200e395b8bde17dd8c8b54ba, and margin_build.py, SHA-256 54260b9d69fdd2d05b4a6c0cd54498a9edbcb40ca53968afe49281581ca1f4d9, were blocked by platform safety with no commit. Neither was retried via another representation or channel. The delivered replay imports neither. Generic incidence reconstruction and the auxiliary margin-generator are not repository-only replay surfaces. These gaps do not prevent direct checking of the explicit upper witness.

The fresh registry blob b93b32955eb94c3b4ee82f045f7bbb85fd900f05 contains fixture policies. No compatible mathematical invocation and obligation-closure receipt has been obtained. The root accepts kernel_check, axiom_escape_audit and statement_faithfulness; this packet requests only those capabilities. No Actions dispatch, evidence_signing, protected-record edit or self-admission is authorized by this request.

T: polygon/Jordan semantics; A: incidence completeness; P: placement-universal lower bounds remain distinct. Root and bounded-polygon-encoding remain open. Existing MIN4 and earlier candidates are dependencies, not retransported results.
