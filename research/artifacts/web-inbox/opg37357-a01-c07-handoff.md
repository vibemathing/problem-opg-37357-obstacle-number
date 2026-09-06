# Nonterminal continuation checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
last_observed_main: 853be12e7783f3b4843e98416a9cbbd29f2d41bf
Issue: #3
Pending PR: #10
Branch: web/attempt-opg37357-a01-c07-sparse-gp-v1
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Open obligations: obligation:opg37357-bounded-polygon-encoding; obligation:opg37357-root

## Preserved candidate state

The c07 proof's intended frozen SHA-256 is 4a733bb1bfbd8bf539b59e8d25d812538d2ff86eeae7fae95db536a678c65109 at research/artifacts/candidates/opg37357-a01-c07-sparse-gp-v1.md. Its PR-bound packet's intended SHA-256 is bb4b3f4179c06b4e04f0ed4c5807574984692422223e8d560242e63e407ae91a at research/artifacts/web-inbox/opg37357-a01-c07.packet.json. Compare these with a fresh byte read and the packet gate, not with remembered draft metadata.

The proof replaces the combined-triple GP block by strict proper crossing witnesses for nonedges, retains all closed-avoidance and ray guards, fixes auxiliary bits, and constructs a same-m open coordinate neighborhood followed by rational line avoidance. It proves an existence-level candidate equivalence, not that every raw sparse assignment is GP-ALL. The claim that adjacent guards were indispensable was removed; they are retained explicitly although implied by other simplicity conditions.

A further derived note was submitted to research/artifacts/source-notes/opg37357-a01-c07-quadratic-next-slice-v1.md: strict products can be split into opposite-sign or same-sign cases, yielding Boolean combinations of quadratic atoms with no new variables. Its byte digest has not been recorded here; read it back before citing or registering it in a subsequent packet. No exporter or mathematical test was executed for this note.

## Pending transport checks

The final head, check results, and merge state of PR #10 are not confirmed by this checkpoint. The three successful checks for PR #9 do not apply to PR #10 or to any subsequent source-note/checkpoint commit. Never infer transport completion from a request being issued. Read back both this note and the Issue comment before treating checkpoint delivery as confirmed.

next_action: fresh-read main, PR #10 head and diff, this packet, and the latest workflow jobs. If the diff is still candidate-only and all three required checks succeed on the current head with a synchronized base, perform COMMENT self-review and gated squash merge, then append actual receipts to Issue #3. Only then create a new branch from fresh main for the sparse quadratic exporter. If checks fail, inspect exact logs and correct only candidate-owned files. Keep both mathematical obligations open and do not claim execution or admission from CI.
