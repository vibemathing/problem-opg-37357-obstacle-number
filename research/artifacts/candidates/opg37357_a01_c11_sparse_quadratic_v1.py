"""Candidate-only sparse quadratic exporter; no SAT verdict or solver call.

Exports c07 S_(G,m), with pointwise quadratic sign splitting.
Runtime replay is a separate obligation. The c05 dependency is byte-pinned.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path
import sys
import types
from typing import Any

BASE_FILE = "opg37357_a01_c05_exporter_v1.py"
BASE_SHA256 = "46f7dd6e2ca9cdf2148efd763fae6cad6ebab33e79aecf0ee4510b93df827403"


def _load_base() -> types.ModuleType:
    path = Path(__file__).with_name(BASE_FILE)
    if path.is_symlink() or not path.is_file():
        raise ImportError("pinned c05 source missing or not a regular file")
    with path.open("rb") as stream:
        data = stream.read(65537)
    if len(data) > 65536 or hashlib.sha256(data).hexdigest() != BASE_SHA256:
        raise ImportError("pinned c05 source digest mismatch")
    name = "_opg37357_c11_pinned_c05"
    module = types.ModuleType(name)
    module.__file__ = str(path)
    sys.modules[name] = module  # dataclass resolves its defining module here.
    try:
        exec(compile(data, BASE_FILE, "exec"), module.__dict__)
    except Exception:
        sys.modules.pop(name, None)
        raise
    return module


base = _load_base()
Limits = base.Limits
InputError = base.InputError
ResourceRefusal = base.ResourceRefusal
Point = tuple[str, str]

OPP = "(define-fun opp ((u Real) (v Real)) Bool (or (and (< u 0) (> v 0)) (and (> u 0) (< v 0))))"
SAME = "(define-fun same ((u Real) (v Real)) Bool (or (and (< u 0) (< v 0)) (and (> u 0) (> v 0))))"
PROPER = "(define-fun proper ((ax Real) (ay Real) (bx Real) (by Real) (cx Real) (cy Real) (dx Real) (dy Real)) Bool (and (opp (orient ax ay bx by cx cy) (orient ax ay bx by dx dy)) (opp (orient cx cy dx dy ax ay) (orient cx cy dx dy bx by))))"
RAYHIT = "(define-fun rayhit ((zx Real) (zy Real) (ax Real) (ay Real) (bx Real) (by Real)) Bool (and (opp (- zx ax) (- zx bx)) (same (orient zx zy ax ay bx by) (- ax bx))))"
ADJACENT = "(define-fun adjacent-ok ((ax Real) (ay Real) (bx Real) (by Real) (cx Real) (cy Real)) Bool (or (not (= (orient ax ay bx by cx cy) 0)) (< (+ (* (- ax bx) (- cx bx)) (* (- ay by) (- cy by))) 0)))"
# The exact byte pin makes these c05 declaration positions immutable.
DEFINITIONS = (base.DEFINITIONS[0], base.DEFINITIONS[1],
               base.DEFINITIONS[2], OPP, SAME, PROPER,
               base.DEFINITIONS[4], RAYHIT, ADJACENT)


def expected_counts(n: int, m: int) -> tuple[int, int]:
    """Assertion/declaration counts after input validation, not a SAT test."""
    if m < 3 or n == 0:
        return 1, 0
    assertions = (math.comb(n + m, 2) + m * (m - 3) // 2 + m + 1
                  + 5 * n * m + 2 * n + math.comb(n, 2))
    coordinates = 2 * m + 2 * max(n - 2, 0)
    declarations = coordinates + n * m + n * (m + 1)
    return assertions, declarations


def export_instance(raw: Any, limits: Any = None) -> str:
    """Return all of S_(G,m), or raise with no partial returned formula."""
    limits = Limits() if limits is None else limits
    if type(limits) is not Limits:
        raise InputError("limits must be a pinned c05 Limits value")
    n, m, edges = base.normalize(raw, limits)
    out = base.Builder(limits)
    out.add("; candidate_only: sparse exact-m existence; raw witness need not be GP-ALL")
    out.add("(set-logic QF_NRA)")
    if m < 3 or n == 0:
        out.assertion("false" if m < 3 else "true")
        return out.finish()
    if n > limits.max_vertices or m > limits.max_corners:
        raise ResourceRefusal("vertex or corner export limit exceeded")
    expected, declarations = expected_counts(n, m)
    if expected > limits.max_assertions:
        raise ResourceRefusal("assertion count limit exceeded before expansion")
    for definition in DEFINITIONS:
        out.add(definition)

    p: list[Point] = [("0", "0")]
    if n >= 2:
        p.append(("1", "0"))
    for i in range(2, n):
        point = (f"p{i+1}x", f"p{i+1}y")
        p.append(point)
        for symbol in point:
            out.real(symbol)
    q: list[Point] = [(f"q{a}x", f"q{a}y") for a in range(m)]
    for point in q:
        for symbol in point:
            out.real(symbol)
    for i in range(n):
        for a in range(m):
            out.real(f"c{i}_{a}")
        for a in range(m + 1):
            out.real(f"b{i}_{a}")

    out.add("; block: distinctness; no combined-triple GP block")
    for a, b in itertools.combinations(p + q, 2):
        out.assertion(f"(> {base.call('dist2', a, b)} 0)")
    out.add("; block: closed polygon simplicity")
    for a in range(m):
        for b in range(a + 1, m):
            if b == a + 1 or (a == 0 and b == m - 1):
                continue
            out.assertion(f"(not {base.call('meet', q[a], q[(a+1)%m], q[b], q[(b+1)%m])})")
        out.assertion(base.call("adjacent-ok", q[(a-1)%m], q[a], q[(a+1)%m]))
    area = " ".join(f"(- (* {a[0]} {b[1]}) (* {a[1]} {b[0]}))"
                    for a, b in zip(q, q[1:] + q[:1]))
    out.assertion(f"(not (= (+ {area}) 0))")

    out.add("; block: exterior points and exact forward-ray parity")
    for i, point in enumerate(p):
        out.assertion(f"(= b{i}_0 0)")
        for a in range(m):
            start, end = q[a], q[(a + 1) % m]
            bit, before, after = f"c{i}_{a}", f"b{i}_{a}", f"b{i}_{a+1}"
            hit = base.call("rayhit", point, start, end)
            out.assertion(f"(not {base.call('onseg', start, end, point)})")
            out.assertion(f"(not (= {start[0]} {point[0]}))")
            out.assertion(f"(= (* {bit} (- {bit} 1)) 0)")
            out.assertion(f"(or (and (= {bit} 1) {hit}) (and (= {bit} 0) (not {hit})))")
            out.assertion(f"(= {after} (- (+ {before} {bit}) (* 2 {before} {bit})))")
        out.assertion(f"(= b{i}_{m} 0)")

    out.add("; block: closed edge avoidance / strict nonedge crossing")
    edge_set = set(edges)
    for i, j in itertools.combinations(range(n), 2):
        edge = (i + 1, j + 1) in edge_set
        predicate = "meet" if edge else "proper"
        hits = " ".join(base.call(predicate, p[i], p[j], q[a], q[(a+1)%m])
                        for a in range(m))
        clause = f"(or {hits})"
        out.assertion(f"(not {clause})" if edge else clause)
    if out.assertions != expected:
        raise RuntimeError("sparse assertion-count invariant failed")
    actual_declarations = sum(line.startswith("(declare-const ") for line in out.lines)
    if actual_declarations != declarations:
        raise RuntimeError("sparse declaration-count invariant failed")
    return out.finish()


def main() -> int:
    """Bounded stdin-only CLI; nonzero diagnostic is not mathematical UNSAT."""
    limits = Limits()
    try:
        data = sys.stdin.buffer.read(limits.max_input_bytes + 1)
        if len(data) > limits.max_input_bytes:
            raise ResourceRefusal("input byte limit exceeded")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise InputError("input must be UTF-8") from exc
        script = export_instance(base.parse_json(text, limits), limits)
        sys.stdout.write(script)
        sys.stdout.flush()
        return 0
    except InputError as exc:
        status, code, message = "invalid_input", 2, str(exc)
    except ResourceRefusal as exc:
        status, code, message = "resource_refusal", 3, str(exc)
    except OSError:
        status, code, message = "io_error", 4, "input/output operation failed"
    except RuntimeError:
        status, code, message = "internal_error", 5, "export invariant failed"
    sys.stderr.write(json.dumps({"status": status, "message": message}) + "\n")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
