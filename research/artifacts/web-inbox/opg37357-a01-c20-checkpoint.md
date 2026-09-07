# C20 finite-arrangement continuation checkpoint

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
mathematical_deliverable: finite-arrangement-characterization proof draft and explicit certificates
best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root
unrestricted_one_obstacle_completeness: open

## Frozen transaction

Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
PR: #25
Branch: web/attempt-opg37357-a01-c20-finite-arrangement-v1
Base: 524c1e402d85e513de58a20f9b7a73bbde0a4e10
Head before this checkpoint: b30bacd48d70c58c3f7a4874e7a068a7ff12d746
Packet creation commit: 747e283eca7e624a9be70c1d914f706445be33af
Actual PR binding commit: b30bacd48d70c58c3f7a4874e7a068a7ff12d746
Harness 1.2.4 snapshot: 4181effe1481eb1454130d2d6c87a7c327ef84e39b28d051fc496870d08864d1

This file precedes final-head checks and merge. The actual final check IDs,
merge SHA and fresh main must be appended to Issue #3 after they are read.
A protected merge of this non-executable package does not resolve the
source-publication block or the missing compatible verifier.

## Delivered progress

The proof treats fixed injective real drawings, including collinear points,
coincident/concurrent support lines, partial segment coverage, and vertices
inside nonincident edges. It proves obstacle/common-component equivalence,
complete refined-face and sign-cell correspondence, and full nonedge
parameter-interval incidence. Empty target lists are explicit. A rational
witness-tree certificate supplies the second-stage input; B17 still uses
C19's separate tree/tube/Jordan proof. No drawing coordinate is moved.

Actual local CPython 3.13.5 Fraction execution: 23 fixtures, 16 damaged
certificate rejections, 5 invalid-input rejections, 160 three-point graphs,
35 C18 determinants and 3 crossings. Bounds and fingerprints are in
execution.json. These are finite generator observations, not a trusted
receipt. The local checker shares its arrangement core with the producer.

All eight candidate file blobs were fresh-read and matched against exact
locally hashed bytes. The packet is actually bound to PR #25. Earlier
candidates and protected files remain unchanged.

## Delivered path / SHA-256 manifest

research/artifacts/candidates/opg37357-a01-c20-finite-arrangement-v1/theorem.md
  a5ce9bb515741ea819f8c152b952d6bdd17f00df8e79f4a0f03f56647a2ea6a8
research/artifacts/candidates/opg37357-a01-c20-finite-arrangement-v1/execution.json
  cd5e134def8a57b814819aadd5e1d75ebf526c030c6fc0d78b9acae5e62753e3
research/artifacts/candidates/opg37357-a01-c20-finite-arrangement-v1/data/fixtures.json
  c2409c352128834961adff1fbf2bc4b88880bdef7d96e974b96cd473d47af1fd
research/artifacts/candidates/opg37357-a01-c20-finite-arrangement-v1/data/observations.json
  a0e22edd80cf77192c6cc655e2a63243b2e0d6af0a7e1bad517c8e4df3d58873
research/artifacts/candidates/opg37357-a01-c20-finite-arrangement-v1/data/c18_negative.certificate.json
  307717b13e0e756c2a5cd09d3575473d59c3aee6bf5e416756c1fde1ae0603e6
research/artifacts/candidates/opg37357-a01-c20-finite-arrangement-v1/data/forced_line_witness.certificate.json
  bfb059d6f8c1f31128a1255992416e99ecd98068f26ece4ae06b953f8ac27e33
research/artifacts/candidates/opg37357-a01-c20-finite-arrangement-v1/data/square_diagonals.certificate.json
  bc71008cc8b04e24f46ba90940ced13f808beabe7a9609d04c4f2f7d59b0a362
research/artifacts/candidates/opg37357-a01-c20-finite-arrangement-v1/data/tiny_open_gap.certificate.json
  c4646e4ac9b91a2e36b1179ff8cf47f1a9f1a872d76f55921518d045fa373e1f
research/artifacts/web-inbox/opg37357-a01-c20.packet.json
  94e16a2448e627c5cca4ec2b7d9cec58a1d875fcf5f13ef3f573dec9d0792375
research/artifacts/web-inbox/opg37357-a01-c20-verifier-request.md
  cce564d430ff0e3b4c605feaa772e0d8679cc9311ad4ebec55f9a15433bd8279

This checkpoint's own hash will appear in the final Issue receipt rather
than in a self-referential field here.

## Remaining files: NOT published

The first geometry.py create_file request was blocked by the platform
safety check and returned no commit; an idempotent same-branch read then
returned 404. Issue #3 comment 5565680013 preserves that exact event.
No source was retried through another upload channel or representation.
The other four files were not submitted after the block. Intended prefix:
research/artifacts/candidates/opg37357-a01-c20-finite-arrangement-v1/

geometry.py
  1675bfb842e9b9836eda5a821722b0cbe8f3edc912430400f0d33b785d812d64
arrangement.py
  70671996a490775fd3dbc3b00ca80c521ae938223558945f1997a42eff505f4b
checker.py
  5c062a48e885ee453245ede83412f5b77e38fa13fd26e9f4d74659f25c23d52c
selftest.py
  b1295744896935eb89278f2967b52f5b21f351641fd29525e8b0fbc99d771a92
run_bounded.py
  6166e2cc0754e7499e25bf068bcf99a5876a167104c2ea1f893127e2fab6877e

The four stored full certificates and compact observations are distinct
non-executable research data, not encoded source. A local duplicate data
bundle and preliminary output summary add no separate mathematical content;
their information is covered by the individual data files and execution
record. No executable repository replay is claimed.

## Verification and recovery

First missing delivery gate: authorized resolution of the platform source
restriction, without bypass. First mathematical admission gap: there is no
registered compatible arrangement-certificate consumer/action. The fixture
verifier registry and the three-job PR transport workflow are not substitutes.
The detailed frozen request is opg37357-a01-c20-verifier-request.md.
No mathematical verification run, signing receipt, EvidenceLink or Result
was produced. User authorization does not expand this principal's powers.

next_action: finish this PR's final-head three checks and candidate-only
review/merge; fresh-read its main and artifacts and append the precise
transport receipt to Issue #3. Retain NONTERMINAL_CHECKPOINT and all five
unpublished source files in the remaining-work list. Subsequent work first
requires resolving the source restriction and obtaining a compatible trusted
consumer, not a new root search or an alternate source upload workaround.
