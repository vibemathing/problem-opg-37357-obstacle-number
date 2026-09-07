# C20 verifier request and first missing gates

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
request_kind: verification_request_not_receipt
Problem: problem:opg-37357-obstacle-number
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-bounded-polygon-encoding
Base: 524c1e402d85e513de58a20f9b7a73bbde0a4e10
Issue: #3

## Requested claims, separately scoped

1. For any fixed finite injective real straight-line drawing, the connected-obstacle, common-free-component and complete finite refined-arrangement incidence conditions in C20 theorem.md are equivalent. Closed graph-edge segments and all graph points are forbidden. Coincident/concurrent lines and vertices inside nonincident edges are allowed. Empty nonedge lists use all component labels.
2. For exact rational input, replay all cells, refined one-dimensional faces, zero-face status, adjacency, complete nonedge interval incidence and the positive tree or negative exclusions in the stored certificates. No coordinate rounding is allowed.
3. Check source-to-formula completeness and the direct geometric tree checks after the source-publication restriction has been resolved through an authorized process. The local checker shares its arrangement core with the producer, so generator self-replay cannot supply a separate verifier trust domain.
4. Separately review the C19-dependent conversion of a size-controlled tree into a filled simple polygon with B17 corners. The certificate's existence flag is not itself a checked polygon or an unrestricted obstacle-number result.

## Frozen published inputs

The following paths are relative to research/artifacts/candidates/opg37357-a01-c20-finite-arrangement-v1/:

theorem.md
  SHA-256 a5ce9bb515741ea819f8c152b952d6bdd17f00df8e79f4a0f03f56647a2ea6a8
execution.json
  SHA-256 cd5e134def8a57b814819aadd5e1d75ebf526c030c6fc0d78b9acae5e62753e3
data/fixtures.json
  SHA-256 c2409c352128834961adff1fbf2bc4b88880bdef7d96e974b96cd473d47af1fd
data/observations.json
  SHA-256 a0e22edd80cf77192c6cc655e2a63243b2e0d6af0a7e1bad517c8e4df3d58873
data/c18_negative.certificate.json
  SHA-256 307717b13e0e756c2a5cd09d3575473d59c3aee6bf5e416756c1fde1ae0603e6
data/forced_line_witness.certificate.json
  SHA-256 bfb059d6f8c1f31128a1255992416e99ecd98068f26ece4ae06b953f8ac27e33
data/square_diagonals.certificate.json
  SHA-256 bc71008cc8b04e24f46ba90940ced13f808beabe7a9609d04c4f2f7d59b0a362
data/tiny_open_gap.certificate.json
  SHA-256 c4646e4ac9b91a2e36b1179ff8cf47f1a9f1a872d76f55921518d045fa373e1f

The record execution.json describes real bounded candidate-generation execution. It is not a trusted verifier receipt. Its source fingerprints do not imply source availability in GitHub.

## Gate G0: executable source publication is blocked

GitHub.create_file for the new C20 geometry.py path returned the platform message: OpenAI could not determine the request's safety status and blocked the tool call. It returned no commit. A subsequent same-branch directory read returned 404. Issue #3 comment 5565680013 records the original observation. The rejected source was not retried via encoding, blob, archive, a different path or another upload channel. Other source files were not submitted after the block.

Still unpublished, under the intended C20 candidate directory:
geometry.py: 1675bfb842e9b9836eda5a821722b0cbe8f3edc912430400f0d33b785d812d64
arrangement.py: 70671996a490775fd3dbc3b00ca80c521ae938223558945f1997a42eff505f4b
checker.py: 5c062a48e885ee453245ede83412f5b77e38fa13fd26e9f4d74659f25c23d52c
selftest.py: b1295744896935eb89278f2967b52f5b21f351641fd29525e8b0fbc99d771a92
run_bounded.py: 6166e2cc0754e7499e25bf068bcf99a5876a167104c2ea1f893127e2fab6877e

Recovery prerequisite: an authorized resolution of that platform restriction. This request does not authorize bypassing it. Until then, reproducibility from repository source remains incomplete, even though explicit certificates and the mathematical proof can be reviewed.

## Gate G1: no compatible registered verifier consumer/action

Fresh research/verifiers.json at the base has Git blob b93b32955eb94c3b4ee82f045f7bbb85fd900f05. Its verifier policies are sympy-counterexample-fixture-v1, sympy-statement-fixture-v1, sympy-smt-counterexample-fixture-v1, smt-statement-fixture-v1, lean-kernel-fixture-v1, lean-axiom-fixture-v1 and lean-statement-fixture-v1. No arrangement-certificate consumer or invocation contract is registered there.

The current .github/workflows directory contains only web-candidate-gate.yml, Git blob c232051b6e2332ac5e4a3a7ddde7ec542ca4d9d6. Its three PR-triggered jobs check the Harness snapshot, packet and candidate-only diff. They do not execute C20 geometry or admission. No compatible mathematical run was triggered; there is no mathematical run ID, verifier fingerprint or signing receipt to report. Local lean, lake and elan were absent at the actual runtime probe.

A trusted process must supply a compatible verifier identity/policy, exact executable fingerprint and invocation contract, separately audited statement mapping, and a receipt bound to the frozen inputs. The current web principal must not modify that registry, workflow or governance to manufacture the missing capability. User approval to begin admission does not substitute for an existing compatible verifier.

## Gate G2: theorem and obligation closure

Requested capabilities remain kernel_check, axiom_escape_audit and statement_faithfulness for the admitted target. Finite rational regression and certificate replay are bounded checks, not kernel proofs of the universal characterization. A later receipt must state its exact claim strength and may not close the unrestricted root from one fixed drawing. Only the registered obligation closure and admission gate may create EvidenceLink/Result/Solution records. None is created by this request.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
unrestricted_one_obstacle_completeness: open
next_action: resolve G0 without bypass, then obtain a compatible registered consumer for the frozen certificate and its exact statement; retain both mathematical obligations until trusted closure.
