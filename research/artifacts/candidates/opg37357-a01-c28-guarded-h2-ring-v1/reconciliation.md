# C28 reconciliation of two implementation stacks

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Issue: #3
PR: #33
Base: f09892bdb8e26edcdfc80edacc2790de904a70ea

## Preserved records

The initial package (guarded_cnf.py, second_check.py, controls.py and existing
C27 fiber.py) retains execution.json's 2.135539-second run. Its 32-variable
formula, 15,952 projected models, 12-corner analytical witness and realized
C18 four-target ternary control are not overwritten. The original nine-file
manifest describes that package, not every later addition to the shared branch.

Five additional files at head 1ae96270bce27bae60e34ff482a7b81a54cbc791 were
separately read, byte-matched and reviewed: guarded.py, exhaust.py, audit.py,
geometry_check.py and run.py. They have no network, child-process, dynamic-code,
credential or repository-file-access operations. Their entry prints stdout.
The geometry consumer is not the blocked slab_geometry.py source; that blocked
payload was never retried through another name, encoding or channel. Neither
published runner imports it. Existing C27 Fiber remains the incidence dependency.
The safety-block record in Issue comment 5572877352 remains unchanged.

## New actual replay, not a replacement receipt

The five files plus guarded_cnf.py, second_check.py and C27 fiber.py were run
at 2026-09-07T16:06:57.073885+00:00, CPython 3.13.5/Linux, exact arithmetic.
Exit 0; elapsed 10.048397 seconds; 35 CPU seconds (36 hard), 40 wall seconds,
512 MiB address space, 4 MiB file output and one worker. Reproduce from C28:

    PYTHONPATH=.:../opg37357-a01-c27-fiber-guard-gluing-v1 python -B run.py

The 23,830-byte deterministic stdout has SHA-256
8d085ef01516e6f20a278a98892a1d859105b3f9817bfb2dc196c6ddf80926f8.
Stderr is empty. Source fingerprints, bounded output summary and limits are
in reconciliation-execution.json, SHA-256
6f6546f7e030977d87864dbb8f2297b086087e246151d21b452e2b62a6daf6a2.

Observed: diamond chain, 36 variables/1,430 clauses/21,248 projected models,
least direction-color tuple (0,7), with accepted 4- and 7-vertex polygons;
octahedron, 29 variables/1,134 clauses/15,952 models, least tuple (0,0), with
an accepted 26-boundary-vertex polygon. The latter is a DIFFERENT witness
from the original 12-corner polygon. All 23 indexed edge-deletion inputs
are SAT, with deletion models not classified geometrically; 16 corrupted
source/rotation records are rejected. Port-chain sizes 3,4,5,8,16 pass exact
polygon checks. General all-length claims require the separate inequalities
in two-coupling-extension.md, not extrapolation from these five tests.

The original two-bit exact-one labels/little-endian words and the extension's
single-bit labels/MSB-first words are different conventions. The full formula
substitution and renaming are checked explicitly, not inferred from equal counts.

## Scope and continuation

The base minima are genuine geometric representations; no faithful added
empty-intersection clause can remove them. The original C18 rank-three cut
remains a fixed-drawing control. The extension's abstract five-target triple-only
obstruction has no asserted planar realization or placement-universal forcing.
These are also distinct from separately coordinated C29 results.

The original saturated ring and the shared missing-port path family do not
yield a lower bound three. Their precise failure scopes do not exclude every
other coupling. T=C19 tube/Jordan, A=fixed incidence, P1=X4 all-placement bridge,
and P2=unrestricted growth remain separate. The next P2 obligation is an
all-real-placement higher-order incompatibility on a different simple planar
family, including real-chart feasibility and common-component semantics.

Keep ONE packet and PR #33. This supplement introduces no duplicate earlier
candidate and modifies no protected file. Historical runs retain their own
scopes. No code replay, transport check, review or merge provides a trusted
mathematical receipt; no EvidenceLink, Result or Solution is created.

best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
next_action: complete the final one-packet transport and continue the all-placement ternary growth obligation.
