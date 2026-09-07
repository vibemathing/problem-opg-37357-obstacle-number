# C24 placement-sign checkpoint

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Issue: #3
PR: #29
Branch: web/attempt-opg37357-a01-c24-placement-sign-atlas-v1
Base: 2d029e51571e1e62392055a8dbbd864e3d70cbbf
Head before this checkpoint: 6dfb58dc65b6b5f12060af7c1c068469968430ca
Packet: research/artifacts/web-inbox/opg37357-a01-c24.packet.json
Actual PR fields: 29
Packet SHA-256: 4b92c8421402d38c42f322beec0517dc992bc199913cd37bf9407a3f41eb5a75
Harness snapshot: 4181effe1481eb1454130d2d6c87a7c327ef84e39b28d051fc496870d08864d1

This pre-merge checkpoint does not assert final checks or merge. Require all
three final-head checks, synchronized base and full candidate-only diff. The
post-read receipt belongs to the same Issue #3, not a newly created Issue.

## Artifact manifest

Prefix: research/artifacts/candidates/opg37357-a01-c24-placement-sign-atlas-v1/
README.md: 061a0d4a37370b740a322f29a33816285b25bfa5e3377f65a6bb3f5149bfea51
signature.py: cee640d54fa2ddba1a02f0bf6ae8edc0755c3dd204bdf0d8c30c989fa65c73ce
sweep.py: ba812b61f17321a46d7067677e5794289fb2ce7eda84d3fde1494d0333da38f1
controls.py: cf9ef5f66eec01238c4fabbdd7ecb34c496a9981943ea67a8a981b7587116cf8
coarse_search.py: d7aed8dc56023ac212e728ef48edd7b4769d6429f059cf1ab3694435739e779a
observation.json: c18efbc097b2f94cafc23da56c8902110762015a53facbf53886a6fafc0f90be
coarse_observation.json: 4c1103023512efe9dd4b74c25cce22cd2e36edc59487a7acbed8ecfa5469aacf
execution.json: d8c1cfec02beea7b0142653c6876711ede9aa4531b0479034f900dde2731e04b

All eight file identities were matched against actual local bytes using the
full remote Git blob SHA and size before packet binding. The packet lists all
eight; no historical source, workflow, schema or ledger is changed.

## Mathematical increment and rejected shortcut

The candidate gives a realizable degree-five finite signature determining
the complete free-component/nonedge hypergraph on D*. Compact robustification
before perturbation permits minimizing the graph parameter over this dense
domain; the interpreter never claims to solve real-sign feasibility.

The planar cactus with edges 01,23,04,12,14,15,25 at points
(1,1),(-2,-2),(3,6),(-5,-10),(7,-7),(-11,11+delta)
has fixed cover two at delta=-1/100 and one at +1/100, despite identical
nonzero signs of all twenty vertex triples. Exact direct triangle/escape
checks accompany the sign interpretation. This rejects one representative
per vertex order type as a complete placement search. It does not give an
unrestricted lower bound for the cactus, which has a one-obstacle placement.

The failed-route proposal fingerprint is
3bf75e3cc7880e8c78ffdd4c27fc7612a7078908aa4f76344ee3173b34b23ae4.
It identifies only the coarse premise, not the admitted route or root.

Execution is finite CPython 3.13.5 Fraction arithmetic, with bounds and the
initial axis-only diagnostic failure/diagonal repair recorded in execution.json.
There is no network, subprocess, dynamic evaluation or file access in the four
new sources. Local execution and PR checks remain in the candidate domain.

## Next obligation and assurance gap

T: C19 tube/Jordan and polygon count.
A: C20 arrangement characterization and C21 second implementation.
P1: C22 X4 all-placement lower-bound replay; trusted review pending.
P2: exists h forall finite planar G exists REALIZABLE signature with cover<=h.
P2 is still open; a fixed-size atlas is not a uniform-h theorem.

A next reduction uses the identity X_ab W_ac-X_ac W_ab=-B_a det(L_a,L_b,L_c).
It suggests quartic local event orders, but must prove complete reconstruction
through concurrence and the unbounded faces before replacing the present
fifth-degree global sweep. An arbitrary Boolean sign array remains inadmissible
as a coordinate witness even when the interpreter accepts it.

The live registry still lacks a compatible callable geometry/realizability
verifier and closure receipt. Request faithful statement and exact source
review through a registered trusted process; the web principal signs nothing.
C21's replacement sources are reused. The five original C20 byte strings are
still unavailable; hashes alone do not provide an attachment or recovery.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: finish this PR's actual final checks and protected merge, then
continue the quartic local-order reconstruction without dropping realizability.
