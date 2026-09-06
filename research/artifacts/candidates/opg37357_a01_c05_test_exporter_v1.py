"""Candidate structural regressions; not a geometric or SMT verifier.

Run only in an authorized bounded runtime. No execution is claimed by this file.
"""
import importlib.util
from pathlib import Path
import sys
import unittest

NAME = "opg37357_a01_c05_exporter_v1"
SPEC = importlib.util.spec_from_file_location(NAME, Path(__file__).with_name(NAME + ".py"))
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("exporter file unavailable")
exporter = importlib.util.module_from_spec(SPEC)
sys.modules[NAME] = exporter
SPEC.loader.exec_module(exporter)


class ExportTests(unittest.TestCase):
    def instance(self, n=2, m=3, edges=None):
        return {"n": n, "edges": [] if edges is None else edges, "m": m}

    def test_small_constants(self):
        for n in (0, 1, 2):
            for m in (-1, 0, 1, 2):
                text = exporter.export_instance(self.instance(n=n, m=m))
                self.assertIn("(assert false)", text)
                self.assertNotIn("declare-const", text)
        self.assertIn("(assert true)", exporter.export_instance(self.instance(n=0)))

    def test_validate_before_false(self):
        with self.assertRaises(exporter.InputError):
            exporter.export_instance(self.instance(m=2, edges=[[1, 1]]))

    def test_invalid_integer_types(self):
        for raw in [self.instance(n=True), self.instance(m=3.0),
                    self.instance(edges=[[True, 2]]), self.instance(n=-1)]:
            with self.subTest(raw=raw), self.assertRaises(exporter.InputError):
                exporter.export_instance(raw)

    def test_invalid_edges_and_keys(self):
        for edges in [None, [[1]], [[1, 1]], [[0, 2]], [[1, 3]],
                      [[1, 2], [2, 1]], [[1, "2"]]]:
            raw = self.instance()
            raw["edges"] = edges
            with self.subTest(edges=edges), self.assertRaises(exporter.InputError):
                exporter.export_instance(raw)
        with self.assertRaises(exporter.InputError):
            exporter.export_instance({"n": 0, "m": 3, "edges": [], "extra": 0})

    def test_json_rejections(self):
        texts = ['{"n":2,"n":2,"m":3,"edges":[]}',
                 '{"n":2.0,"m":3,"edges":[]}',
                 '{"n":NaN,"m":3,"edges":[]}']
        for text in texts:
            with self.subTest(text=text), self.assertRaises(exporter.InputError):
                exporter.parse_json(text)

    def test_determinism(self):
        first = self.instance(n=3, edges=[[1, 2], [3, 2]])
        second = self.instance(n=3, edges=[[2, 3], [2, 1]])
        self.assertEqual(exporter.export_instance(first), exporter.export_instance(second))

    def test_expected_counts(self):
        for n, m, assertions, declarations in [(1, 3, 28, 13), (2, 3, 56, 20),
                                                (2, 4, 83, 26), (3, 3, 90, 29)]:
            with self.subTest(n=n, m=m):
                text = exporter.export_instance(self.instance(n=n, m=m))
                self.assertEqual(text.count("(assert "), assertions)
                self.assertEqual(text.count("(declare-const "), declarations)
                self.assertTrue(text.endswith("(check-sat)\n"))
                self.assertEqual(text.count("(check-sat)"), 1)
                self.assertEqual(text.count("("), text.count(")"))

    def test_anchors_and_no_hidden_solver(self):
        text = exporter.export_instance(self.instance(edges=[[1, 2]]))
        self.assertNotIn("(declare-const p1", text)
        self.assertNotIn("(declare-const p2", text)
        self.assertIn("(not (= q0x 0))", text)
        self.assertIn("(not (= q0x 1))", text)
        self.assertNotIn("(forall", text)
        self.assertNotIn("(exists", text)
        self.assertNotIn("(get-model)", text)
        self.assertIn("(= b0_3 0)", text)

    def test_visibility_polarity(self):
        missing = exporter.export_instance(self.instance())
        present = exporter.export_instance(self.instance(edges=[[1, 2]]))
        missing_assert = [line for line in missing.splitlines() if line.startswith("(assert")][-1]
        present_assert = [line for line in present.splitlines() if line.startswith("(assert")][-1]
        self.assertTrue(missing_assert.startswith("(assert (or (meet 0 0 1 0"))
        self.assertEqual(present_assert, "(assert (not " + missing_assert[8:-1] + "))")

    def test_resource_refusal_is_not_false(self):
        limits_list = [exporter.Limits(max_corners=3),
                       exporter.Limits(max_assertions=55),
                       exporter.Limits(max_output_bytes=64)]
        raws = [self.instance(m=4), self.instance(), self.instance()]
        for limits, raw in zip(limits_list, raws):
            with self.subTest(limits=limits), self.assertRaises(exporter.ResourceRefusal):
                exporter.export_instance(raw, limits)
        with self.assertRaises(exporter.ResourceRefusal):
            exporter.parse_json(" " * 100, exporter.Limits(max_input_bytes=32))
        with self.assertRaises(exporter.ResourceRefusal):
            exporter.export_instance(self.instance(edges=[[1, 2], [2, 1]]),
                                     exporter.Limits(max_edges=1))


if __name__ == "__main__":
    unittest.main()
