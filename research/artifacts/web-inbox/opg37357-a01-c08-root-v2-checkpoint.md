# Root checkpoint: X4 certificate frozen; Q2 continuation remains active

verdict: candidate_only
best_verified_result: none
best_verified_candidate: none
locally_replayed_candidate: candidate:opg37357-a01-c08-x4-root-proof-v2
route_status: active
Issue: #3
PR: #11
Branch: web/attempt-opg37357-a01-c08-root-x4-certificate-v1
Base: 853be12e7783f3b4843e98416a9cbbd29f2d41bf
Last observed head before this checkpoint: dfb185d08a25b302f8fc5d89d870e3a689bb30d0
Open obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding

## Q1 progress

The explicit planar X4 graph has 10 vertices, 24 edges and 21 nonedges. Its all-placement necessary-condition CNF (540 variables, 69332 clauses) has a stored 1827-addition exact RUP proof. A standard-library Python replay checks planarity and the complete proof; its actual stdout is stored. The README proves the geometric implication from unrestricted one-connected-obstacle placements. No fixed drawing, obstacle coordinates, corner cutoff or affine normalization restricts the lower-bound search. Berman et al.'s journal Proposition 3 is accurately attributed as the prior Q1 theorem.

The replay-v2 package is self-contained. Its stored certificate text uses one fixed, hash-bound transport delta, checked before decompression and proof replay. Older unfinished producer/proof-part files in the parent directory are preserved and are not consumed or validated by this replay. The root packet is backfilled with PR #11. Final-head required checks have not yet been read at this checkpoint; subsequent observations belong in Issue #3.

## Frozen digests

All replay files are under research/artifacts/candidates/opg37357-a01-c08-root-x4/replay-v2/.
- README.md: a6a4ecc039d40287750eb15fd1d12d6e178197c8c3b6ec9fe5dcca34344d04f0
- necessary_cnf.py: 49a83611574808cb7296c761128821a9a2bd32fcab97de9dc0a0d610aa69f83a
- replay.py: 58d1dc95f4619a1cbe9545ded2ce275c70133fc962469f015618132433dae1e4
- materialize.py: fcfa80020fbb562524c9b3300ef0dc92d3ff0b4ac50dbec86249f1546359dd37
- certificate.json (stored transport): b4668771fd98f902ebc6c8fc73e7db2a6a5c103660ccfed6e20c442f73505dc5
- reconstructed certificate bytes: 440c92278e01888c19bbb341958eca1320da6f28362d66343d0eb3e8e8cce697
- replay-observation.json: 0ee95aab0b10d51ada5f766a6cb345cf780611ebeafd3fc1fed23849dff2636d
- generated full CNF: de54d35f78d3c7d84e24651e5ce6f82c9ebe6d78bc7bd2deb66aa591e6ea276c
- decompressed RUP: 9d16206d67cb450cbaaa4920fe83a5d463584a612f29367e0f2da4a8acd6ec5e
- research/artifacts/source-notes/opg37357-a01-c08-root-sources-v2.md: b4b8567fd31c4dfda3c682d912767e1798b884c1c8f5e709f034fdd50eb29b64
- packet Git blob SHA (not SHA-256): 3ef116c5a19dc6bcac4f70ac52a0a09b09daf7ab

## Actual search scope and limitations

X4 path caps 2 and 3: SAT, inconclusive for representation. X4 cap 4: UNSAT with proof. X3 cap 4: SAT control. No all-orders planar enumeration, graph minimality claim, or two-obstacle nonrepresentability result. Python 3.13.5 and Z3 C 4.13.3.0 were inspected; the final exact replay does not use Z3. All runs are in the candidate-generation trust domain. Trusted semantic/kernel/axiom replay and admission remain absent.

Registered failed-route ledger was empty at the base. Local dead ends: broad graph lower bounds are not planar lower bounds; plane-obstacle lower bounds are not ordinary-obstacle lower bounds; SAT on the necessary-condition relaxation does not construct a representation. No protected ledger was modified.

## Q2 next precise action

After the three required checks and diff audit permit PR #11 merge, fresh-read main and continue in a new candidate branch. Prove the induced-triangulation extension: every planar G on n>=3 vertices and e edges is an induced subgraph of a planar triangulation H with 6n-e-10 vertices. Start with a same-vertex maximal planar augmentation, subdivide only added edges, and cone every resulting face. Use induced-subgraph monotonicity of ordinary obstacle number to reduce the universal-k problem to maximal planar graphs. Never substitute unsupported monotonicity under deleting edges. Test the construction on disconnected graphs and bridge-containing graphs; separately attack any proposed strengthening to 4-connected triangulations.

The retrieved 2017 conjecture obs(G)<=2 is not a proof. The 2017 n-3 theorem concerns plane drawings, and the 2024 general lower bound is not restricted to planar graphs. No later universal ordinary-obstacle theorem was found in the bounded literature search. Q2 and trusted admission remain nonterminal.
