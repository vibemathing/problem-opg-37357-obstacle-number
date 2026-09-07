# C26 verification request: placement implication and amplification boundary

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
request_kind: verification_request_not_receipt
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
Base: c299659f0c7f505a1e9739e6d8329fbde48c30ff
Attempt: attempt:web-20260906-opg37357-a01
Route: route:one-obstacle-semialgebraic-encoding-v1
Graph: graph:opg37357-initial-v1
Target: obligation:opg37357-root

## Claims requiring separate review

P1: Any injective real X4 placement admitting one connected obstacle induces
an assignment satisfying the exact C22 CNF after the robust GP reduction.
Review each four-point, five-point and key-path clause origin, shared endpoints,
loop-erased crossing paths, the existential key-variable elimination and the
one-side-per-ordered-pair quantifier. The 14-case degeneration atlas explicitly
distinguishes proof-only cases from actual finite controls.

The exact C22 CNF digest is
de54d35f78d3c7d84e24651e5ce6f82c9ebe6d78bc7bd2deb66aa591e6ea276c.
All 69,332 clauses were regenerated with source origins and matched to C22.
The origin table is deterministically emitted by controls.py --origins; its
SHA-256 is 666420da3374818cafa9fa8805acab65740c373e1fbb9ad3af01e5d12d4813f7.
The already-merged 1,827-addition C22 contradiction is a SEPARATE dependency;
its RUP was not rerun in C26 and no new SAT solver result is claimed.

P2: Review the guarded h-color necessary formula, the fixed-orientation
conflict-graph coloring equivalence and the additive/capacity demand lemmas.
The palette-separation/capacity hypothesis must be proved for all placements
before a growing planar obstacle lower bound can be concluded.

P2 barrier: Different induced X4 copies in any planar ambient graph share
only a clique, so their sets of internal nonedges are disjoint. The relaxation
consisting only of monochromatic-X4-copy prohibitions is therefore 2-colorable.
Check the auxiliary plane-embedding/Jordan separator proof and X4's exhaustive
176 deletion spanning-tree certificates. This is NOT an obstacle upper bound
of two; it excludes only that proposed amplification inference. No protected
failed-route ledger is edited. The abstract Fano test is not a planar drawing.

T/A: C19 tube/Jordan and C20/C21 arrangement remain distinct candidate layers.
The bridge uses compact free-component regularization, not C19's corner bound.
C25 W signs are used only for a REALIZED signature; its bounded decoder is not
run at n=10 and its consistency tests do not decide real feasibility.

## Frozen candidate files

Prefix: research/artifacts/candidates/opg37357-a01-c26-placement-bridge-growth-v1/
README.md
  9cbaf03bb94fdf7bd0c5f28ec1533770540407cfcefc87c5429b83e1e2725343
growth.md
  00ee415ad060be05d242897dfdb6ee41b02be61dc4e740040b5c0d1852d5545b
clause_bridge.py
  a1395be250d45f5476e2d9734736127486a1d66b608b96179f58692f23da855b
growth.py
  3fc815d746b9e5b2a1bc697a42ab0d8f4164b7a8ea1fb98d1a9bb91a9ea1be39
controls.py
  150709c9bdb0ebfeeb57f9857aaecd75837607cb54f61ad77d4b5eb1e33ca741
degeneracy-atlas.json
  2d4ca8edb38103f254cc0fab596f5bf36d996a9dbbff175dcde303bbbed4d6c0
observation.json
  9944852f3e0564bc89f86d0b7569185df3bdb83c0d70a9257b4ebb3a11a5a6fd
execution.json
  eba1aec821ad3632d9b72274f43a6a6435f955de5117088be1b51cb89d42eda2

Source blobs were matched to the actual final local bytes. CPython 3.13.5
exact arithmetic ran under 35 CPU seconds, 40 wall seconds, 512 MiB and
bounded output. A failed GP fixture was repaired and the final source rerun.
No source imports the old C20 arrangement producer; no source uses network,
child processes or dynamic evaluation. The local bounded wrapper is not part
of the published mathematical implementation.

## First missing trusted gate

Fresh registry research/verifiers.json has blob
b93b32955eb94c3b4ee82f045f7bbb85fd900f05 and contains fixture policies, not a
compatible invocation contract for this universal geometry-to-CNF implication
or its amplification claims. The existing PR workflow validates transport.
There is no new trusted mathematical fingerprint/run/receipt. A registered
consumer must bind its executable, exact input and claim, statement-faithfulness
and axiom/escape audit to the obligation closure process. The web principal
must not manufacture that consumer, signing authority or closure record.

The canonical contract's connected polygonal-obstacle interpretation requires
explicit faithful mapping. Disconnected unions counted as one would be a
different definition. The two root questions must be admitted separately:
X4's constant lower bound does not settle a uniform bound over all planar G.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: trusted audit of the frozen bridge and old C22 contradiction;
continue cross-block guarded two-color or higher-rank demands, preserving
realizability and the all-placement quantifier.
