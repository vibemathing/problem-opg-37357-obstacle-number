# NEXT9 structural completeness source note
verdict: candidate_only

Primary reference: Ryuichi Mori, Atsuhiro Nakamoto, Katsuhiro Ota,
Diagonal Flips in Hamiltonian Triangulations on the Sphere,
Graphs and Combinatorics 19(3), 413-418 (2003), DOI 10.1007/s00373-002-0508-6.
Theorem4 states finite flip connectivity for simple spherical triangulations
of the same order, up to embedded isomorphism. Only connectivity is needed here;
the numerical diameter bound is not used.

Read sources on 2026-09-09:
https://keio.elsevierpure.com/en/publications/diagonal-flips-in-hamiltonian-triangulations-on-the-sphere/
https://www.researchgate.net/publication/220397797_Diagonal_Flips_in_Hamiltonian_Triangulations_on_the_Sphere
The latter is author-uploaded paper text; the university record supplies the
publication metadata and abstract. No diagram or reproduced source text is used.

Faithfulness: n=9, finite simple spherical triangulations, legal diagonal flips
only when the other diagonal is absent, and isomorphism of embedded faces.
closure_check.py checks every such move and its rotation-compatible mapping.
Starting from one class, closure plus this theorem makes the finite catalog
complete. It does not impose a straight-line embedding on obstacle placements,
does not preserve four-connectivity along intermediate flips, and supplies no
obstacle-number inequality. The structural catalog is a candidate verification,
not an admitted result. Prior MIN4 provides the reused lower-order exclusion.
