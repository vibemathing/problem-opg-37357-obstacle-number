# Cutoff source audit (c02)

Verdict: candidate_only
Target: obligation:opg37357-bounded-polygon-encoding
Retrieved: 2026-09-06

Martin Balko, Steven Chaplick, Robert Ganian, Siddharth Gupta, Michael Hoffmann, Pavel Valtr, Alexander Wolff, *Bounding and computing obstacle numbers of graphs*, arXiv:2206.15414v3, 21 January 2024; SIAM Journal on Discrete Mathematics 38(2), 1537--1565 (2024), DOI 10.1137/23M1585088.
Locators: https://arxiv.org/abs/2206.15414v3 ; https://arxiv.org/pdf/2206.15414

## Exact reuse boundary

Section 3.1 defines lexicographic minimality on PDF page 6. Lemmas 12--14, PDF pages 9--11, feed the total-corner inequality on page 13. Its connectedness and minimality assumptions are retained in c02. The page-7 component reduction is for counting graph descriptions, not for producing a global obstacle polygon. Section 5, Lemma 22, PDF pages 22--23, already contains an ETR construction sketch and a qualitative O(e^2+n) complexity bound. These are prior art, not claims of novelty for c01 or c02. That sketch does not replace c01's explicit simplicity, exterior-point, degeneracy, and parity audit.

The source introduction states graph-point general position. c02 supplies its own separate same-corner-budget conversion to combined general position; the source is not cited as if it had stated that exact lemma.

## Retrieval and verification status

Version and journal metadata were read from arXiv; relevant PDF text was retrieved. PDF screenshot attempts for this source failed with a cache/internal error, so no figure-based inference is used. No full-PDF byte digest, external code replay, or mathematical verifier receipt is claimed. The preceding c01 source note's JGAA bibliographic correction is already in its merged source revision.
