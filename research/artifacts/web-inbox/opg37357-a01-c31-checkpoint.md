# C31 NONTERMINAL_CHECKPOINT

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
Actual PR: #37
Branch: web/attempt-opg37357-a01-c31-tetra-wall-v1
Execution/packet base: 1ae28cbfb434b792fafc76514afc6cd0641d7316
Head before checkpoint: 546cdc62758096500097810172197a480c0fcf8c
Packet creation: 846265d9b5316c730fb69e9861b32f491c574af9
Actual PR37 binding: 546cdc62758096500097810172197a480c0fcf8c
Target: obligation:opg37357-root
ONE packet: research/artifacts/web-inbox/opg37357-a01-c31.packet.json

## Tested family and decisive result

One graph and its FIRST exact placement were screened. Core K4 on0..3 plus
port4+i adjacent to all core vertices other than i, i=0..3: n8/e18; degrees
6,6,6,6,3,3,3,3. Six port-port nonedges were frozen BEFORE testing. All ten
nonedges04,15,26,37,45,46,47,56,57,67 are retained. Abstract planarity is proved
by stellating four tetrahedral faces; actual visibility edges may cross.
No repeated stars, diamonds, prism connectors or leaf-port enumeration.

The first placement p_i=(i,-i^2) has explicit14-corner and4-corner filled simple
polygon obstacles representing the WHOLE graph. A standalone exact checker
accepts79 polygon-side pairs,324 edge/boundary pairs,16 exterior-point tests,
and10 strict interior nonedge hits;27 proper graph-edge crossings are allowed.
Thus this proposed nonleaf all-placement obs>=3 interface has a real counterexample.
No stage-two lower-bound survivor remains from this selected bounded family.
We do NOT claim all-order-type enumeration or graph-level exact obstacle number2.

Complete1290 simple graph paths of length<=7 give156 variables/24012 necessary
same-label-guarded clauses, including all four/five-point rules. At the displayed
real directions, all1024 labels give16 CNF extensions. Exact C27 Fiber gives39
components; component0 and24 cover everything. The joint selector system has
234 variables/25516 clauses before56 direction units. Enumerating labels and
all1521 component pairs gives8 actual label/selector assignments. This fixed
incidence is not a symbolic realizability solver.

## Genuine new higher-order bridge and its boundary

Targets15,26,47 have pairwise common components but empty triple intersection.
Graph triangles013,035,036 give inside/outside word sets
W15={010,011,100}, W26={000,001,011,100}, W47={000,001,010}.
Any common free component has a constant word; the three sets have empty total
intersection. A129-sign degree<=4 polynomial guard orders every supporting-line
root along the three targets, retaining11 zero signs. The manuscript proves
that for EVERY REAL GP placement satisfying this guard, the triple is forbidden
from being monochromatic. This is a real-region theorem candidate, not a claim
that all placements have this sign vector. The cut removes exactly8 spurious
fixed-fiber CNF labelings, leaving the8 true cover models.

A genuine graph-automorphism relabeling sigma=(0 1)(2 3)(4 5)(6 7) keeps the same
polygons but makes15,26,47 all label0. Its sign guard changes. It is an explicit
falsifier of deleting the guard, not another family search. Positive-margin
regularization and Jordan first-exit arguments are explicit; no planar rotation
is imposed on an arbitrary visibility placement.

Failed-route proposal fingerprint:
5e87df5ab5ad8f84be012ef02cd6feeb1c491b1b4b067e66300bf82d752ecf8c
Scope: ONLY this full eight-vertex face-port graph and isomorphic relabelings.
Also fails its capacity<=2-on-six-targets premise, since obstacle0 hits all six.
No other nonleaf/stacked/planar family is excluded. Protected ledger unchanged.

## Actual execution and publication gap

CPython3.13.5, exact Fraction/integer arithmetic,35CPU/40wall seconds,512MiB,
one worker,4MiB output per command. Five final local report/cache commands
exited0; eighteen mutations rejected. The standalone delivered polygon command
also exited0 in0.672805 seconds. Original run times/bytes/hashes are recorded.
The bad initial47 hit t=1/18 was rejected and replaced by23/30; no polygon changed.

Accepted new source files: witness_check.py and guarded_cnf.py.
BLOCKED source write: jordan_words.py, no commit, no alternate upload.
Not uploaded: replay.py, which depends on that missing module.
Executed-only hashes:
jordan_words.py 5f104bca12569cfe16cd02edc3ad84f2bb94602d6ee628b81d7491c06c9889a2
replay.py 146ecde114bde0d3d2debe10abccc7741f4b29679b53ce4cd51f59f2bea0a142
Neither is provided through another name/encoding/blob/tool/source attachment.
The full local suite is NOT a repository-only runnable release. The polygon
witness and CNF source are separately runnable without the missing module.
Numerical certificate and proof are delivered as non-executable research data.
Complete CNF/origin/fiber/guard outputs are retained locally with hashes;
flat origin emitter delivery is not claimed. Existing C27 source is reused,
not republished, at its exact hash7209f677207695d220f7766286fdd94867f75d88a42d35b36cdfdef8d709ba35.

## Frozen candidate hashes

research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/README.md
  cdc3613acb3a6639b8414a77d721b3fab349f699f5f0ee5b1dfd0c8f687417d5
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/witness_check.py
  86be77d1805deb3a134a46ca55641db5b18dbeedcf2a7f31a5ba959b34a828a7
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/guarded_cnf.py
  a1fb730149eb93ad7e21f63a05ebda7389817f1135de86de9bf2fbcf4ad8ede9
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/input.json
  91200aa2fadf32da2957c1eb9fb0fa635bcf76cebf89cbdd9f0595ce9eb3f7e1
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/witness.json
  1605c7406cff347e3d72eed44bef683f3a4914b7569f03be419e2037a752afcc
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/jordan-certificate.json
  8a2cb9e8e1c01ba24ed945f226b20f7cf386a7475cc8fadb7e21b613f4c3ae6f
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/observation.json
  ec77bb5c5efe50ec144fe3c9dd760ac037ba50c05a906932d5f1fe158cf200b9
research/artifacts/candidates/opg37357-a01-c31-tetra-wall-v1/execution.json
  fcfaed0cb3b1a1a6b8899afb513ecc639cbd3533472936d963962e1c42876987
research/artifacts/web-inbox/opg37357-a01-c31.packet.json
  be98fa415c4c5ba48f5cf51e1aa1edcac2b95f434ed0a594991fb989a2e26ab1
research/artifacts/web-inbox/opg37357-a01-c31-verifier-request.md
  011832716244e2903b65fec52d2ac030d90fa38e8cf6c26a7dbada92b6cda71c

## Pending transport and next atomic obligation

This checkpoint PRECEDES its final-head checks. Expect exactly11 new allowed-path
files and ONE packet against current main, with no prior artifact/protected file
changes. Check current synchronization, all three final-head required checks,
and full diff before normal protected squash merge. Actual final head/check IDs,
merge SHA, tree comparison and this checkpoint hash must be recorded in the next
Issue3 comment; do not infer successful delivery from this pre-check document.
Fresh C29 checkpoint5573358544 and PR35/36 were read and not rewritten. Separate
open PR33 was left untouched. No claim that all repository transports are clear.

best_verified_candidate: none
best_verified_result: none
best_current_candidate: explicit two-polygon graph counterplacement plus guarded Jordan-word lemma
first_open_quantifier_bridge: a complete REAL-region cover for a genuinely different nonleaf graph, not a fixed-drawing constraint
next_atomic_step: exclude known failed graph-isomorphism families; choose a different nonleaf planar coupling with six targets, apply cycle-wall word constraints to every surviving real region, or preserve its actual counterplacement
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
trusted_closure: none

The current registry remains fixture-only. No EvidenceLink, Result, Solution,
protected records/schema/workflows/Harness or verifier policy is modified.
Source-publication repair must use an authorized non-bypass process.
status: NONTERMINAL_CHECKPOINT
