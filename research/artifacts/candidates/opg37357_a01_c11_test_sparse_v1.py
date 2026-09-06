"""Candidate regression specification; run only in an authorized runtime.

These tests do not invoke a solver. The scalar reference checks do not parse
or certify every emitted SMT assertion.
"""
from fractions import Fraction as F
import unittest

import opg37357_a01_c11_sparse_quadratic_v1 as sparse


def orient(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def opp(u, v):
    return (u < 0 < v) or (v < 0 < u)


def same(u, v):
    return (u < 0 and v < 0) or (u > 0 and v > 0)


class SparseTests(unittest.TestCase):
    def test_counts_and_no_gp_block(self):
        for n, m, assertions, declarations in [(1,3,27,13),(2,3,49,20),
                                               (2,4,67,26),(3,3,73,29)]:
            text = sparse.export_instance({"n":n,"m":m,"edges":[]})
            self.assertEqual(text.count("(assert "), assertions)
            self.assertEqual(text.count("(declare-const "), declarations)
            self.assertEqual(text.count("(assert (adjacent-ok "), m)
            self.assertNotIn("(assert (not (= (orient ", text)
            self.assertTrue(text.endswith("(check-sat)\n"))
        # Counts only: this does not attempt a large export or certify its byte cap.
        self.assertEqual(sparse.expected_counts(24,64)[0], 13849)

    def test_edge_closed_nonedge_strict(self):
        for edges, beginning in [([], "(assert (or (proper "),
                                  ([[1,2]], "(assert (not (or (meet ")]:
            text = sparse.export_instance({"n":2,"m":3,"edges":edges})
            last = [s for s in text.splitlines() if s.startswith("(assert ")][-1]
            self.assertTrue(last.startswith(beginning))
        text = sparse.export_instance({"n":2,"m":4,"edges":[]})
        self.assertEqual(text.count("(assert (not (meet "), 2)
        self.assertEqual(text.count("(assert (not (onseg "), 8)

    def test_sign_cells_including_zero(self):
        for u in (-1,0,1):
            for v in (-1,0,1):
                self.assertEqual(opp(u,v), u*v < 0)
                self.assertEqual(same(u,v), u*v > 0)
        self.assertFalse(opp(0,1))
        self.assertFalse(same(0,1))
        self.assertNotEqual(opp(0,1), not same(0,1))

    def test_ray_family_and_side_reversal(self):
        for t in (F(-1),F(1)):
            q = [(F(-1),t),(F(2),t),(F(3,2),F(3))]
            for zx in (F(0),F(1)):
                z = (zx,F(0))
                bits = []
                for a,b in zip(q,q[1:]+q[:1]):
                    A,B,D,T = zx-a[0],zx-b[0],a[0]-b[0],orient(z,a,b)
                    hit = opp(A,B) and same(T,D)
                    self.assertEqual(hit, A*B < 0 and T*D > 0)
                    self.assertEqual(hit, opp(B,A) and same(-T,-D))
                    bits.append(int(hit))
                self.assertEqual(bits, [1,0,1] if t>0 else [0,0,1])
                parity = 0
                for c in bits:
                    parity = parity+c-2*parity*c
                self.assertEqual(parity, 0 if t>0 else 1)

    def test_input_and_refusal_separation(self):
        with self.assertRaises(sparse.InputError):
            sparse.export_instance({"n":2,"m":2,"edges":[[1,1]]})
        with self.assertRaises(sparse.InputError):
            sparse.export_instance({"n":True,"m":3,"edges":[]})
        with self.assertRaises(sparse.ResourceRefusal):
            sparse.export_instance({"n":2,"m":3,"edges":[]},
                                   sparse.Limits(max_assertions=48))
        with self.assertRaises(sparse.ResourceRefusal):
            sparse.export_instance({"n":2,"m":3,"edges":[]},
                                   sparse.Limits(max_output_bytes=64))
        self.assertIn("(assert false)", sparse.export_instance({"n":2,"m":2,"edges":[]}))
        self.assertIn("(assert true)", sparse.export_instance({"n":0,"m":100,"edges":[]}))

    def test_order_invariance(self):
        a = sparse.export_instance({"n":3,"m":3,"edges":[[2,3],[1,2]]})
        b = sparse.export_instance({"n":3,"m":3,"edges":[[2,1],[3,2]]})
        self.assertEqual(a,b)


if __name__ == "__main__":
    unittest.main()
