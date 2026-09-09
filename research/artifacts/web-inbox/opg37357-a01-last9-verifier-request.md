# LAST9 verification request, not a receipt

verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
Repository: vibemathing/problem-opg-37357-obstacle-number
Issue: #3
Target: obligation:opg37357-root
Base: 7593b2f8aac2cde225560efc2e39a59080ef2916
Candidate directory: research/artifacts/candidates/opg37357-a01-last9-canonical-v1/

## Frozen claims and separate layers

The graph in input.json, canonical word001001111001011011001101011101110101, has the complete two-filled-simple-polygon representation in witness.json. All21 edges and15 nonedges, not just five targets, must be checked. The32-corner exterior band has a slit; it is not an annulus whose hole may be filled. The5-corner interior polygon is disjoint. The cap instance splits it at12x+y=127/4; removing vertex1/restoring edge27 yields the explicit parent, then insertion and cap addition produce the final graph. All intended old/new visibility conditions and strict nonedge hits must be checked.

Two different algorithms are available: existing NB9 polygon_verify.py (orientation/winding) and new parity_check.py (parametric intersections/ray parity). Both remain in the generation trust domain. A trusted review must justify finite predicates to filled Jordan disks, prove the proper-chord cap union is a disk, and match the frozen ProblemContract. It must not assume obstacle drawings inherit the graph's plane rotation.

Run the delivered direct entry, from the candidate directory:

    python -B cap_verify.py

Use external35 CPU seconds,40 wall seconds,512MiB,one worker,5MiB output. It checks parent, intermediate point insertion, and final representation with both consumers. Existing NB9 dependencies remain at their SHA-bound sibling paths. The fixed files already exist, so this entry does not create missing certificates during normal replay.

Witness SHA-256:33a8558580f5a8ff5f300433324f6ded5e0a45262839093215acfe23cefeef88
Parent SHA-256:632d857b758c2f9f58cd97c39ddea6b117e077060877ebc2881e11750e4dc803
Cap SHA-256:cabdf7494acba7d8b845c663aed2ed214716c9c8267753a7544d95fc1b1fa546

## Auxiliary execution and publication gap

Complete guarded-CNF/source audit was actually run:309 variables,124844 clauses,5117 all-simple paths through eight edges. The local fixed selector has431 variables,128620 clauses,two swapped models. Its table and anchors are tied to ONE placement, not an all-realizable-order-type result. The39 pair and one triple empty cores eliminate neither true representation.

The ordinary write of new replay.py was blocked by platform safety with no commit (SHA-25692be32f8158cd262ffac8e235cc0224eed7ac0eab7d6ce689f469732078c9b81; Issue comment5595439024). It was not retried through another path, encoding, blob, tool or attachment. Already published cap_verify.py imports neither this dispatcher nor the supplied local incidence helper. The auxiliary combined dispatcher is not a repository-only replay surface; supplied incidence is not a geometric-completeness receipt. execution.json preserves actual local commands, exact hashes and scopes without upgrading them to signed evidence.

The registry still lists fixture policies and no compatible authenticated mathematical closure has been obtained. Request only kernel_check,axiom_escape_audit,statement_faithfulness as admitted by the root. User authorization does not grant evidence_signing. No EvidenceLink,Result,Solution or protected record is written. The exact obstacle number one versus two and the unrestricted root remain open.
