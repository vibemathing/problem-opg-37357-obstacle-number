"""Candidate-only, bounded SMT-LIB export of the c04 GP-ALL normal form.

No solver, network, subprocess, or verification receipt is produced.
Input: {"n": nonnegative integer, "edges": [[u,v],...], "m": integer}.
Labels are 1..n. Planarity is an input promise, not tested by this exporter.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from dataclasses import dataclass
from typing import Any


class InputError(ValueError):
    """Malformed input; not a mathematical negative answer."""


class ResourceRefusal(RuntimeError):
    """Export budget exceeded; not an UNSAT answer."""


@dataclass(frozen=True)
class Limits:
    max_vertices: int = 24
    max_corners: int = 64
    max_edges: int = 4096
    max_assertions: int = 60000
    max_output_bytes: int = 1048576
    max_input_bytes: int = 65536

    def __post_init__(self) -> None:
        for value in vars(self).values():
            if type(value) is not int or value < 1:
                raise InputError("all limits must be positive integers")


def parse_json(text: str, limits: Limits = Limits()) -> Any:
    if len(text.encode("utf-8")) > limits.max_input_bytes:
        raise ResourceRefusal("input byte limit exceeded")

    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in items:
            if key in result:
                raise InputError("duplicate JSON key")
            result[key] = value
        return result

    def integer(token: str) -> int:
        if len(token.lstrip("-")) > 128:
            raise ResourceRefusal("integer token digit limit exceeded")
        return int(token)

    def reject_number(_: str) -> Any:
        raise InputError("only JSON integer numbers are accepted")

    try:
        return json.loads(text, object_pairs_hook=pairs, parse_int=integer,
                          parse_float=reject_number, parse_constant=reject_number)
    except json.JSONDecodeError as exc:
        raise InputError("invalid JSON") from exc
    except RecursionError as exc:
        raise ResourceRefusal("JSON nesting limit exceeded") from exc


def normalize(raw: Any, limits: Limits = Limits()) -> tuple[int, int, tuple[tuple[int, int], ...]]:
    if type(raw) is not dict or set(raw) != {"n", "edges", "m"}:
        raise InputError("expected exactly n, edges, and m")
    n, m, edges = raw["n"], raw["m"], raw["edges"]
    if type(n) is not int or n < 0 or type(m) is not int:
        raise InputError("n must be a nonnegative integer and m an integer")
    if type(edges) is not list:
        raise InputError("edges must be a JSON array")
    if len(edges) > limits.max_edges:
        raise ResourceRefusal("edge-list length limit exceeded")
    seen: set[tuple[int, int]] = set()
    for edge in edges:
        if type(edge) is not list or len(edge) != 2:
            raise InputError("each edge must be a two-element array")
        u, v = edge
        if type(u) is not int or type(v) is not int:
            raise InputError("edge labels must be integers, not booleans")
        if not (1 <= u <= n and 1 <= v <= n) or u == v:
            raise InputError("edge labels must be distinct and in 1..n")
        pair = (min(u, v), max(u, v))
        if pair in seen:
            raise InputError("duplicate undirected edge")
        seen.add(pair)
    return n, m, tuple(sorted(seen))


# Nonrecursive definitions; macro expansion uses only real polynomials.
DEFINITIONS = (
    "(define-fun orient ((ax Real) (ay Real) (bx Real) (by Real) (cx Real) (cy Real)) Real (- (* (- bx ax) (- cy ay)) (* (- by ay) (- cx ax))))",
    "(define-fun dist2 ((ax Real) (ay Real) (bx Real) (by Real)) Real (+ (* (- ax bx) (- ax bx)) (* (- ay by) (- ay by))))",
    "(define-fun onseg ((ax Real) (ay Real) (bx Real) (by Real) (cx Real) (cy Real)) Bool (and (= (orient ax ay bx by cx cy) 0) (<= (+ (* (- cx ax) (- cx bx)) (* (- cy ay) (- cy by))) 0)))",
    "(define-fun proper ((ax Real) (ay Real) (bx Real) (by Real) (cx Real) (cy Real) (dx Real) (dy Real)) Bool (and (< (* (orient ax ay bx by cx cy) (orient ax ay bx by dx dy)) 0) (< (* (orient cx cy dx dy ax ay) (orient cx cy dx dy bx by)) 0)))",
    "(define-fun meet ((ax Real) (ay Real) (bx Real) (by Real) (cx Real) (cy Real) (dx Real) (dy Real)) Bool (or (proper ax ay bx by cx cy dx dy) (onseg ax ay bx by cx cy) (onseg ax ay bx by dx dy) (onseg cx cy dx dy ax ay) (onseg cx cy dx dy bx by)))",
    "(define-fun rayhit ((zx Real) (zy Real) (ax Real) (ay Real) (bx Real) (by Real)) Bool (and (< (* (- zx ax) (- zx bx)) 0) (> (* (orient zx zy ax ay bx by) (- ax bx)) 0)))",
)
Point = tuple[str, str]


def call(name: str, *points: Point) -> str:
    return "(" + name + " " + " ".join(c for point in points for c in point) + ")"


class Builder:
    def __init__(self, limits: Limits) -> None:
        self.limits = limits
        self.lines: list[str] = []
        self.bytes = 0
        self.assertions = 0

    def add(self, line: str) -> None:
        size = len(line.encode("utf-8")) + 1
        if self.bytes + size > self.limits.max_output_bytes:
            raise ResourceRefusal("output byte limit exceeded")
        self.lines.append(line)
        self.bytes += size

    def assertion(self, expression: str) -> None:
        if self.assertions >= self.limits.max_assertions:
            raise ResourceRefusal("assertion count limit exceeded")
        self.add("(assert " + expression + ")")
        self.assertions += 1

    def real(self, name: str) -> None:
        self.add("(declare-const " + name + " Real)")

    def finish(self) -> str:
        self.add("(check-sat)")
        return "\n".join(self.lines) + "\n"


def export_instance(raw: Any, limits: Limits = Limits()) -> str:
    """Return a complete script or raise; never return a partial export.

    Successful export is not a SAT result. m<3 is a mathematical false
    formula. Invalid input and resource refusal are exceptions, not false.
    """
    n, m, edges = normalize(raw, limits)
    out = Builder(limits)
    out.add("; candidate_only: exact-m GP-ALL closed polygon; not a solver result")
    out.add("(set-logic QF_NRA)")
    if m < 3:
        out.assertion("false")
        return out.finish()
    if n == 0:
        out.assertion("true")  # A remote simple m-gon exists; no coordinates needed.
        return out.finish()
    if n > limits.max_vertices or m > limits.max_corners:
        raise ResourceRefusal("vertex or corner export limit exceeded")
    total = n + m
    expected = (math.comb(total, 2) + math.comb(total, 3)
                + m * (m - 3) // 2 + 1 + 5 * n * m + 2 * n
                + math.comb(n, 2))
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

    points = p + q
    for a, b in itertools.combinations(points, 2):
        out.assertion(f"(> {call('dist2', a, b)} 0)")
    for a, b, c in itertools.combinations(points, 3):
        out.assertion(f"(not (= {call('orient', a, b, c)} 0))")
    for a in range(m):
        for b in range(a + 1, m):
            if b == a + 1 or (a == 0 and b == m - 1):
                continue
            out.assertion(f"(not {call('meet', q[a], q[(a+1)%m], q[b], q[(b+1)%m])})")
    area = " ".join(f"(- (* {a[0]} {b[1]}) (* {a[1]} {b[0]}))"
                    for a, b in zip(q, q[1:] + q[:1]))
    out.assertion(f"(not (= (+ {area}) 0))")

    for i, point in enumerate(p):
        out.assertion(f"(= b{i}_0 0)")
        for a in range(m):
            start, end = q[a], q[(a + 1) % m]
            bit, before, after = f"c{i}_{a}", f"b{i}_{a}", f"b{i}_{a+1}"
            hit = call("rayhit", point, start, end)
            out.assertion(f"(not {call('onseg', start, end, point)})")
            out.assertion(f"(not (= {start[0]} {point[0]}))")
            out.assertion(f"(= (* {bit} (- {bit} 1)) 0)")
            out.assertion(f"(or (and (= {bit} 1) {hit}) (and (= {bit} 0) (not {hit})))")
            out.assertion(f"(= {after} (- (+ {before} {bit}) (* 2 {before} {bit})))")
        out.assertion(f"(= b{i}_{m} 0)")

    edge_set = set(edges)
    for i, j in itertools.combinations(range(n), 2):
        hits = " ".join(call("meet", p[i], p[j], q[a], q[(a + 1) % m])
                        for a in range(m))
        intersects = f"(or {hits})"
        out.assertion(f"(not {intersects})" if (i + 1, j + 1) in edge_set else intersects)
    if out.assertions != expected:
        raise RuntimeError("internal assertion-count invariant failed")
    return out.finish()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default="-", help="JSON file or - for stdin")
    args = parser.parse_args(argv)
    limits = Limits()
    try:
        if args.input == "-":
            data = sys.stdin.buffer.read(limits.max_input_bytes + 1)
        else:
            with open(args.input, "rb") as stream:
                data = stream.read(limits.max_input_bytes + 1)
        if len(data) > limits.max_input_bytes:
            raise ResourceRefusal("input byte limit exceeded")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise InputError("input must be UTF-8") from exc
        script = export_instance(parse_json(text, limits), limits)
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
