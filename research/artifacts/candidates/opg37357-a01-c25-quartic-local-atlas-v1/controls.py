"""Bounded C25 controls. The C21 model is only a cross-check, not a decoder dependency.
Run with the existing C21 directory on PYTHONPATH. Pure memory and JSON stdout.
"""
from fractions import Fraction as F
from itertools import combinations
import copy
import json
from quartic_signature import extract, line_data, cross, determinant, sign
from local_decode import decode, local_orders, minimum_cover
from arrangement_model import Model
from strict_cells import all_cells


def require(ok, message):
    if not ok:
        raise ValueError(message)


def strings(p):
    return [[str(x) for x in row] for row in p]


def coverage_masks(incidence, count):
    return sorted(sum(1 << i for i, row in enumerate(incidence) if c in row) for c in range(count))


def direct_check(raw, edges):
    s = extract(raw); result = decode(s, edges)
    p, pairs, lines = line_data(raw); m = len(lines)
    by_line = []
    # Intersections are compared by rational division, never by the quartic signs.
    for a in range(m):
        events = {}
        for b in range(m):
            if a == b:
                continue
            x, y, w = cross(lines[a], lines[b])
            events.setdefault(x/w, []).append(b)
        ordered = sorted(events)
        expected = [sorted(events[x]) for x in ordered]
        require(result['groups'][a] == expected, 'rational local intersection order')
        by_line.append(ordered)
    # Check exact polynomial identity, including zero/concurrent and denominator signs.
    identities = 0
    for a in range(m):
        others = [b for b in range(m) if b != a]
        for b, c in combinations(others, 2):
            x1, _, w1 = cross(lines[a], lines[b]); x2, _, w2 = cross(lines[a], lines[c])
            require(x1*w2-x2*w1 == -lines[a][1]*determinant(lines[a], lines[b], lines[c]),
                    'quartic factorization')
            identities += 1
    for face in result['faces']:
        a, r = face['line'], face['interval']; cuts = by_line[a]
        x = cuts[0]-1 if r == 0 else cuts[-1]+1 if r == len(cuts) else (cuts[r-1]+cuts[r])/2
        A, B, C = lines[a]; q = (x, -(A*x+C)/B)
        values = [u*q[0]+v*q[1]+w for u, v, w in lines]
        require(values[a] == 0 and all(v != 0 for i, v in enumerate(values) if i != a), 'face point')
        for cell in face['cells']:
            require(all(i == a or result['cells'][cell][i] == sign(v) for i, v in enumerate(values)),
                    'direct face covector')
    if m <= 10:
        actual = sorted(all_cells(lines))
        require(actual == [tuple(c) for c in result['cells']], 'strict-elimination full-cell census')
    expected = Model({'points': raw, 'edges': edges})
    rows = [expected.incidence[tuple(s)] for s in result['nonedges']]
    require(len(result['components']) == len(expected.components), 'free-component count')
    require(coverage_masks(result['incidence'], len(result['components'])) ==
            coverage_masks(rows, len(expected.components)), 'incidence hypergraph up to labels')
    # Brute force covers on this separate graph-edge arrangement, not decoder recursion.
    optimum = None
    for k in range(len(expected.components)+1):
        if any(all(set(chosen).intersection(row) for row in rows)
               for chosen in combinations(range(len(expected.components)), k)):
            optimum = k; break
    require(optimum == result['conditional_tau'], 'cover optimum')
    return result, identities


def main():
    checks, identity_count = 0, 0
    for n in (3, 4):
        raw = [[i, 2**i] for i in range(n)]
        pairs = list(combinations(range(n), 2))
        for bits in range(1 << len(pairs)):
            edges = [list(p) for i, p in enumerate(pairs) if bits >> i & 1]
            _, c = direct_check(raw, edges); checks += 1; identity_count += c
    raw5 = [[i, 2**i] for i in range(5)]; pairs5 = list(combinations(range(5), 2))
    for bits in range(0, 1024, 31):
        edges = [list(p) for i, p in enumerate(pairs5) if bits >> i & 1]
        _, c = direct_check(raw5, edges); checks += 1; identity_count += c
    cactus_edges = [[0, 1], [2, 3], [0, 4], [1, 2], [1, 4], [1, 5], [2, 5]]
    cactus = []
    triple_signs = []
    for delta in (F(-1, 100), F(0), F(1, 100), F(-1, 10**40), F(1, 10**40)):
        points = [[1, 1], [-2, -2], [3, 6], [-5, -10], [7, -7], [-11, 11+delta]]
        raw = strings(points); out, c = direct_check(raw, cactus_edges)
        checks += 1; identity_count += c
        require(out['conditional_tau'] == (1 if delta > 0 else 2), 'C24 control tau')
        s = extract(raw); p, pairs, lines = line_data(raw)
        triple_signs.append([sign(determinant((*p[i], F(1)), (*p[j], F(1)), (*p[k], F(1))))
                             for i, j, k in combinations(range(6), 3)])
        a, b, z = [pairs.index(v) for v in ((0, 1), (2, 3), (4, 5))]
        require(determinant(lines[a], lines[b], lines[z]) == 168*delta, 'cactus quartic')
        cactus.append({'delta': str(delta), 'cells': len(out['cells']), 'components': len(out['components']),
                       'tau': out['conditional_tau'], 'signature_entries': sum(len(s[k]) for k in ('b', 'w', 'd')),
                       'triple_line_determinant': str(168*delta), 'zero_triple_lines': s['d'].count(0)})
    require(all(row == triple_signs[0] and 0 not in row for row in triple_signs), 'unchanged vertex order')
    minus = extract([[1, 1], [-2, -2], [3, 6], [-5, -10], [7, -7], [-11, '1099/100']])
    plus = extract([[1, 1], [-2, -2], [3, 6], [-5, -10], [7, -7], [-11, '1101/100']])
    require(minus['b'] == plus['b'] and minus['w'] == plus['w'], 'same coarse B/W signs')
    require(sum(a != b for a, b in zip(minus['d'], plus['d'])) == 1, 'one quartic event')
    base = [[1, 1], [-2, -2], [3, 6], [-5, -10], [7, -7], [-11, F(1101, 100)]]
    transformed = [
        [[-x, y] for x, y in base],
        [[y, x] for x, y in base],
        [[2*x+y+3, x+3*y-7] for x, y in base],
        [[x/F(10**40), y/F(10**40)] for x, y in base],
        list(reversed(base))]
    for i, p in enumerate(transformed):
        edges = cactus_edges if i != 4 else [[5-a, 5-b] for a, b in cactus_edges]
        out, c = direct_check(strings(p), edges); checks += 1; identity_count += c
        require(out['conditional_tau'] == 1, 'affine/relabel control')
    invalid = [
        ('too_few', [[0, 0], [1, 2]]),
        ('duplicate', [[0, 0], [1, 1], [0, 0]]),
        ('float', [[0, 0], [1, 1.1], [2, 3]]),
        ('boolean', [[0, False], [1, 1], [2, 3]]),
        ('vertical', [[0, 0], [0, 1], [2, 3]]),
        ('collinear', [[0, 0], [1, 1], [2, 2]]),
        ('parallel', [[0, 0], [1, 1], [2, 4], [3, 5]]),
        ('oversize', [[0, 0], [1, 1], [2, str(10**100)]])]
    rejected = []
    for name, raw in invalid:
        try:
            extract(raw)
        except (ValueError, ZeroDivisionError):
            rejected.append(name)
        else:
            raise ValueError('accepted invalid D*: '+name)
    s = extract(strings(base)); mutants = []
    for field, idx, val in [('b', 0, False), ('w', 0, 0), ('d', 0, 2)]:
        item = copy.deepcopy(s); item[field][idx] = val; mutants.append((field, item))
    item = copy.deepcopy(s); item['d'].pop(); mutants.append(('missing_sign', item))
    # Delete a forced vertex concurrence sign: this must not silently produce a simple arrangement.
    item = copy.deepcopy(s)
    pairs = list(combinations(range(6), 2)); rows = list(combinations(range(len(pairs)), 3))
    ids = tuple(pairs.index(p) for p in ((0, 1), (0, 2), (0, 3)))
    require(item['d'][rows.index(ids)] == 0, 'forced vertex concurrence')
    item['d'][rows.index(ids)] = 1; mutants.append(('forced_concurrence', item))
    for name, item in mutants:
        try:
            decode(item, cactus_edges)
        except (ValueError, KeyError):
            rejected.append(name)
        else:
            raise ValueError('accepted damaged signature: '+name)
    # Probe a nonrealizable triangle signature; record the outcome rather than assume it.
    # For three sorted pair lines (01,02,12), signs Delta = sign(orient^2) = +1.
    triangle = extract([[0, 0], [1, 1], [2, 4]])
    triangle['d'][0] *= -1
    try:
        decode(triangle, [])
        realizability_control = 'not_rejected: feasibility remains a separate obligation'
    except ValueError:
        realizability_control = 'rejected_by_local_consistency; not a general feasibility decision'
    return {'verdict': 'candidate_only', 'trusted_verifier_receipt': False,
            'drawing_graph_comparisons': checks, 'rational_factorization_checks': identity_count,
            'cactus': cactus, 'rejected_mutations': rejected,
            'cactus_BW_equal': True, 'cactus_changed_quartic_signs': 1,
            'realizability_mutation': realizability_control,
            'algorithm': 'line-local degree-four signs; no global intersection x/y comparisons',
            'general_theorem_not_inferred_from_tests': True}


if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True, separators=(',', ':')))
