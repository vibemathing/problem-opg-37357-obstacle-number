"""Candidate-only compiler of a typed finite circuit into conjunctive QF_NRA.

This module does not invoke a solver. It implements the c13 template, not
a parser for c11 polygon SMT text. All checks and execution need replay.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json
import re
import sys
from typing import Any


class InvalidInput(ValueError):
    pass


class ResourceRefusal(RuntimeError):
    pass


@dataclass(frozen=True)
class Limits:
    max_inputs: int = 512
    max_arithmetic: int = 8192
    max_boolean: int = 8192
    max_constraints: int = 100000
    max_input_bytes: int = 262144
    max_output_bytes: int = 1048576
    max_rational_chars: int = 256

    def __post_init__(self) -> None:
        for value in vars(self).values():
            if type(value) is not int or value < 1:
                raise InvalidInput("all limits must be positive integers")


def exact_keys(node: Any, keys: set[str]) -> None:
    if type(node) is not dict or set(node) != keys:
        raise InvalidInput("wrong object keys")


def index(value: Any, bound: int) -> int:
    if type(value) is not int or not 0 <= value < bound:
        raise InvalidInput("reference is not a valid earlier typed index")
    return value


def rational(value: Any, limits: Limits) -> Fraction:
    if type(value) is not str:
        raise InvalidInput("rational constants must be strings")
    if len(value) > limits.max_rational_chars:
        raise ResourceRefusal("rational token limit exceeded")
    if re.fullmatch(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?", value) is None:
        raise InvalidInput("expected integer or numerator/positive-denominator")
    return Fraction(value)


def parse_json(text: str, limits: Limits) -> Any:
    if len(text.encode("utf-8")) > limits.max_input_bytes:
        raise ResourceRefusal("input byte limit exceeded")

    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise InvalidInput("duplicate JSON key")
            result[key] = value
        return result

    def integer(token):
        if len(token.lstrip("-")) > 128:
            raise ResourceRefusal("integer token too long")
        return int(token)

    def reject_number(_):
        raise InvalidInput("noninteger JSON number")

    try:
        return json.loads(text, object_pairs_hook=pairs, parse_int=integer,
                          parse_float=reject_number, parse_constant=reject_number)
    except json.JSONDecodeError as exc:
        raise InvalidInput("invalid JSON") from exc
    except RecursionError as exc:
        raise ResourceRefusal("JSON nesting limit") from exc


def validate(raw: Any, limits: Limits) -> tuple[int, list, list, int]:
    exact_keys(raw, {"inputs", "arithmetic", "boolean", "root"})
    n, ar, bo = raw["inputs"], raw["arithmetic"], raw["boolean"]
    if type(n) is not int or n < 0 or type(ar) is not list or type(bo) is not list:
        raise InvalidInput("invalid dimensions or node arrays")
    if n > limits.max_inputs or len(ar) > limits.max_arithmetic or len(bo) > limits.max_boolean:
        raise ResourceRefusal("circuit dimension limit exceeded")
    checked_ar = []
    for i, node in enumerate(ar):
        if type(node) is not dict or type(node.get("op")) is not str:
            raise InvalidInput("arithmetic node needs an op")
        op = node["op"]
        if op == "input":
            exact_keys(node, {"op", "index"})
            checked_ar.append((op, index(node["index"], n)))
        elif op == "const":
            exact_keys(node, {"op", "value"})
            checked_ar.append((op, rational(node["value"], limits)))
        elif op in ("add", "sub", "mul"):
            exact_keys(node, {"op", "args"})
            if type(node["args"]) is not list or len(node["args"]) != 2:
                raise InvalidInput("arithmetic operation must be binary")
            checked_ar.append((op, *(index(j, i) for j in node["args"])))
        else:
            raise InvalidInput("unsupported arithmetic operation")
    checked_bo = []
    for i, node in enumerate(bo):
        if type(node) is not dict or type(node.get("op")) is not str:
            raise InvalidInput("Boolean node needs an op")
        op = node["op"]
        if op == "const":
            exact_keys(node, {"op", "value"})
            if type(node["value"]) is not bool:
                raise InvalidInput("Boolean constant must be true or false")
            checked_bo.append((op, node["value"]))
        elif op == "atom":
            exact_keys(node, {"op", "value", "relation"})
            relation = node["relation"]
            if type(relation) is not str or relation not in ("eq","ne","lt","le","gt","ge"):
                raise InvalidInput("unsupported comparison")
            checked_bo.append((op, index(node["value"], len(ar)), relation))
        elif op == "not":
            exact_keys(node, {"op", "arg"})
            checked_bo.append((op, index(node["arg"], i)))
        elif op in ("and", "or"):
            exact_keys(node, {"op", "args"})
            if type(node["args"]) is not list or len(node["args"]) != 2:
                raise InvalidInput("Boolean operation must be binary")
            checked_bo.append((op, *(index(j, i) for j in node["args"])))
        else:
            raise InvalidInput("unsupported Boolean operation")
    root = index(raw["root"], len(bo))
    return n, checked_ar, checked_bo, root


def numeral(value: int) -> str:
    return str(value) if value >= 0 else f"(- {-value})"


def compile_circuit(raw: Any, limits: Limits = Limits()) -> str:
    """Return complete SMT text, not a SAT verdict; no partial returned text."""
    if type(limits) is not Limits:
        raise InvalidInput("limits must be Limits")
    n, ar, bo, root = validate(raw, limits)
    atoms = sum(node[0] == "atom" for node in bo)
    expected_equations = len(ar) + len(bo) + 7 * atoms + 1
    expected_inequalities = 2 * atoms
    if expected_equations + expected_inequalities > limits.max_constraints:
        raise ResourceRefusal("constraint count limit exceeded")
    lines: list[str] = []
    size = equations = inequalities = declarations = 0

    def add(line: str) -> None:
        nonlocal size
        size += len(line.encode("utf-8")) + 1
        if size > limits.max_output_bytes:
            raise ResourceRefusal("output byte limit exceeded")
        lines.append(line)

    def real(name: str) -> None:
        nonlocal declarations
        add(f"(declare-const {name} Real)")
        declarations += 1

    def eq(left: str, right: str) -> None:
        nonlocal equations
        add(f"(assert (= {left} {right}))")
        equations += 1

    def nonnegative(name: str) -> None:
        nonlocal inequalities
        add(f"(assert (>= {name} 0))")
        inequalities += 1

    add("; candidate_only: typed circuit lift; not a solver result")
    add("(set-logic QF_NRA)")
    for i in range(n):
        real(f"x{i}")
    for i in range(len(ar)):
        real(f"a{i}")
    for i, node in enumerate(bo):
        real(f"t{i}")
        if node[0] == "atom":
            for prefix in ("P", "N", "Z", "rP", "rN"):
                real(f"{prefix}{i}")

    for i, node in enumerate(ar):
        v, op = f"a{i}", node[0]
        if op == "input":
            eq(v, f"x{node[1]}")
        elif op == "const":
            f = node[1]
            eq(f"(* {f.denominator} {v})", numeral(f.numerator))
        else:
            symbol = {"add": "+", "sub": "-", "mul": "*"}[op]
            eq(v, f"({symbol} a{node[1]} a{node[2]})")

    for i, node in enumerate(bo):
        t, op = f"t{i}", node[0]
        if op == "const":
            eq(t, "1" if node[1] else "0")
        elif op == "atom":
            v = f"a{node[1]}"
            P, N, Z, rp, rn = (f"{prefix}{i}" for prefix in ("P","N","Z","rP","rN"))
            for bit in (P,N,Z):
                eq(f"(* {bit} (- {bit} 1))", "0")
            eq(f"(+ {P} {N} {Z})", "1")
            eq(f"(* {v} {rp})", P)
            eq(f"(* (- {v}) {rn})", N)
            eq(f"(* {Z} {v})", "0")
            nonnegative(rp)
            nonnegative(rn)
            truth = {"gt":P, "lt":N, "eq":Z, "ne":f"(+ {P} {N})",
                     "ge":f"(+ {P} {Z})", "le":f"(+ {N} {Z})"}[node[2]]
            eq(t, truth)
        elif op == "not":
            eq(t, f"(- 1 t{node[1]})")
        else:
            a, b = f"t{node[1]}", f"t{node[2]}"
            eq(t, f"(* {a} {b})" if op == "and" else f"(- (+ {a} {b}) (* {a} {b}))")
    eq(f"t{root}", "1")
    if (equations != expected_equations or inequalities != expected_inequalities
            or declarations != n + len(ar) + len(bo) + 5 * atoms):
        raise RuntimeError("internal template count mismatch")
    add("(check-sat)")
    return "\n".join(lines) + "\n"


def main() -> int:
    limits = Limits()
    try:
        data = sys.stdin.buffer.read(limits.max_input_bytes + 1)
        if len(data) > limits.max_input_bytes:
            raise ResourceRefusal("input byte limit exceeded")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise InvalidInput("input must be UTF-8") from exc
        output = compile_circuit(parse_json(text, limits), limits)
        sys.stdout.write(output)
        sys.stdout.flush()
        return 0
    except InvalidInput as exc:
        status, code, message = "invalid_input", 2, str(exc)
    except ResourceRefusal as exc:
        status, code, message = "resource_refusal", 3, str(exc)
    except OSError:
        status, code, message = "io_error", 4, "input/output operation failed"
    except RuntimeError:
        status, code, message = "internal_error", 5, "template invariant failed"
    sys.stderr.write(json.dumps({"status": status, "message": message}) + "\n")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
