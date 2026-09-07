# PR34 anchored continuation: verifier request and nonterminal checkpoint

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Issue: #3
PR: #34
Branch: web/attempt-opg37357-a01-c28-octahedral-h2-v1
Packet: research/artifacts/web-inbox/opg37357-a01-c28-octahedral.packet.json
Packet base: a8f3fb565464167b7375d7fe5220df66bb3413b3
Packet update commit: 50a2a8fece3174c50b304f391ce2f42770330be8
Packet SHA-256: b2e1a1ffe8dae7168a3e626bbb950144a4edec88357ce4cfc7df19b1aac053fb

## Recovered state, not duplicate research

Existing PR34 already held the complete octahedral SAT/minimum-polygon package.
Its nine original mathematical blobs and its separate earlier resume-execution
record are preserved. Generic C28 names had conflicted with PR33; the fresh
branch already had the namespaced packet and a normal synchronization when a
new-file attempt returned 422. The current file was then read and extended
with its actual blob SHA. No second packet, duplicate branch, force update,
main write, or change to PR33/C29 mathematical content was made.

This continuation really reran resume_check.py: the original four arithmetic
cores, complete clause-source reconstruction, both counting algorithms, all
eight connector Boolean formulas and sixteen mutations. It did not rerun C27
fiber, old checks.py, old RUP or PR33's extension. Records are not conflated.
The main formula has 32 variables and 1140 clauses, all 84 simple paths,
15952 projected models and 807232 full models over the entire finite space.
The minimum has an actual 16-corner single polygon; it cannot be rejected by
adding a fabricated geometric condition. The coupling is not an obs>=3 graph.

## New anchored interface and exact limit

For complete incidence J_s in a finite nonempty component set C define
M_u={s:u not in J_s}. Then tau<=2 iff some u has intersection_{s in M_u}J_s
nonempty, with empty-family intersection C. A no-two-cover certificate must
exclude EVERY first component u, not only a selected one. Rank-three cores
are sufficient and complete when |C|<=3; in general they are not necessary.

The explicit abstract system J_0={0}, J_i={1,2,3,4} minus {i} for i=1..4
has tau=3, but anchor 0 needs all four other targets to obtain empty
intersection. This is a set-system counterexample, NOT a planar drawing.

Actual anchored_triples.py execution compared the interface against all
binary target partitions for 38877 systems with <=3 components and <=5 targets,
including empty target/incidence cases; all 20867 no-two systems have accepted
rank-three certificates. Four damaged certificates reject. The C18 incidence
control removes exactly two of eight pairwise-compatible labelings, retaining
six. C18 coordinates were not re-enumerated by this entry.

Both actual runs: CPython 3.13.5, 35 CPU/40 wall seconds, 512 MiB, one worker,
4 MiB output cap, exit 0. Dates, source/import/byte identities and output hashes
are in continuation-execution.json. These are candidate-generation runs only.

## New file SHA-256 manifest

Prefix: research/artifacts/candidates/opg37357-a01-c28-octahedral-h2-v1/
resume_check.py
  ddbfdf85e7eb749291d17e460b6aac15fedbfe4ba929282c81dc37cd25b5f86b
anchored_triples.py
  253f4020674cf4bba5494cb375cf77f2deca80fd77f2ec88b0f643d33f1f8fba
resume-observation.json
  e5dcc1aa5b39951a3d05b2d9c39a896144832128bb251af162dde6009a873c95
anchored-observation.json
  ff5c31043e9573cd1e41cdca98277510df5f244021f0c1d0012112f3a2faf1ed
continuation.md
  d5de9af87be468bd8317adf9ead28009affe38702bb62383ee59d113dd29370b
continuation-execution.json
  82f140d225497ca75bd924d727a2222b213481044f161991c5c6d6e895ed73dc

The single packet also binds the ten prior preserved mathematical/report files.
This checkpoint precedes final checks. Read the actual final head, verify the
full diff has one added packet and no protected or prior-main changes, then
merge by the repository gate. Issue #3 must record actual check/run/merge/main
identities after fresh reads; pending text here is historical once merged.

## Trusted verification request and next mathematical obligation

Request a trusted audit of complete CNF source enumeration, both finite-count
methods, direct polygon/rotation checking, the anchored equivalence and its
rank-four limit. The original octahedral request remains available separately.
A registered compatible consumer must bind its executable and exact inputs,
statement-faithfulness and axiom/escape audit to the closure gate. No such
receipt is asserted by this generator. CI and merge are transport only.

T: C19 tube/Jordan remains separate; direct polygon here does not invoke T.
A: actual geometric use of incidence needs complete arrangement certification.
P1: old X4 all-placement implication and contradiction are unchanged.
P2: still requires a planar G forcing no two-component cover for EVERY
placement, not a fixed bad drawing or an abstract noncolorable hypergraph.
Next: force anchored empty-intersection cores from cross-module geometry for
all placements of a different planar graph; allow rank four rather than assume
three is complete. No new all-placement graph obstruction is supplied here.

best_verified_candidate: none
best_verified_result: none
best_fixed_drawing_candidate: original C20/C21; direct octahedral polygon control
best_growth_candidate: anchored exclusion interface and rank-three limitation
open_obligations: obligation:opg37357-root; obligation:opg37357-bounded-polygon-encoding
Original five C20 source byte strings remain unavailable; no reconstruction or
alternate-encoding retry is claimed. The new sources are ordinary safe text.
