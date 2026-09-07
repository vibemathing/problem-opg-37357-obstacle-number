"""Exact fixed-layout controls and a one-convex-obstacle fan construction.
No external input files, network, subprocesses, dynamic execution or writes.
Usage: python fan_certificate.py [r]  (3 <= r <= 32); default: finite self-test.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import sys


def orient(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def on(a, b, p):
    return orient(a, b, p) == 0 and all(min(a[d], b[d]) <= p[d] <= max(a[d], b[d]) for d in (0, 1))


def meet(a, b, c, d):
    x, y, z, w = orient(a, b, c), orient(a, b, d), orient(c, d, a), orient(c, d, b)
    return x*y < 0 and z*w < 0 or on(a, b, c) or on(a, b, d) or on(c, d, a) or on(c, d, b)


def inside(poly, p):
    return all(orient(poly[i], poly[(i+1) % len(poly)], p) > 0 for i in range(len(poly)))


def fan(r, gap=F(1, 2), shifted=True):
    if type(r) is not int or not 3 <= r <= 32:
        raise ValueError('r must be an integer in [3,32]')
    points = [(F(0), F(-r*r if shifted else 0))] + [(F(i), F(i*i)) for i in range(1, r+1)]
    edges = [(0, i) for i in range(1, r+1)] + [(i, i+1) for i in range(1, r)]
    polygon = [(F(i), F(i*i)+gap) for i in range(1, r+1)]
    return points, edges, polygon


def audit_positive(r, gap=F(1, 2), shifted=True):
    p, edges, poly = fan(r, gap, shifted)
    sides = list(zip(poly, poly[1:]+poly[:1]))
    if not all(orient(poly[i], poly[(i+1) % r], poly[j]) > 0
               for i in range(r) for j in range(r) if j not in (i, (i+1) % r)):
        return False
    if any(inside(poly, v) or any(on(a, b, v) for a, b in sides) for v in p):
        return False
    if any(meet(p[i], p[j], a, b) for i, j in edges for a, b in sides):
        return False
    nonedges = [(i, j) for i in range(1, r+1) for j in range(i+2, r+1)]
    if not all(inside(poly, ((p[i][0]+p[j][0])/2, (p[i][1]+p[j][1])/2)) for i, j in nonedges):
        return False
    return all(orient(p[i], p[j], p[k]) != 0 for i, j, k in combinations(range(r+1), 3))


def audit_convex_layout(r):
    p, edges, _ = fan(r, shifted=False)
    incidences = []
    crossing_count = 0
    for i in range(1, r+1):
        for j in range(i+2, r+1):
            order = []
            for a in range(i+1, j):
                x = F(i*j, i+j-a)
                t = (x-i)/(j-i)
                q = (x, a*x)
                if not (0 < t < 1 and 0 < x < a and on(p[i], p[j], q) and on(p[0], p[a], q)):
                    raise AssertionError('spoke crossing formula')
                order.append(t)
                crossing_count += 1
            if order != sorted(set(order)):
                raise AssertionError('crossing order')
            for u, v in edges:
                expected = i in (u, v) or j in (u, v) or u == 0 and i < v < j
                if meet(p[i], p[j], p[u], p[v]) != expected:
                    raise AssertionError('unlisted finite-edge contact')
            incidences.append(set(range(i, j)))
    cover = set(range(2, r, 2))
    packing = [set((a, a+1)) for a in range(1, r-1, 2)]
    if not all(cover & c for c in incidences) or len(cover) != (r-1)//2:
        raise AssertionError('cover')
    if len(packing) != len(cover) or any(x & y for x, y in combinations(packing, 2)):
        raise AssertionError('dual packing')
    if any(c not in incidences for c in packing):
        raise AssertionError('dual targets')
    if r <= 12:
        lower = min(len(s) for z in range(r) for s in combinations(range(1, r), z)
                    if all(set(s) & c for c in incidences))
        if lower != len(cover):
            raise AssertionError('exhaustive cover disagreement')
    return {'r': r, 'vertices': r+1, 'edges': 2*r-1, 'nonedges': len(incidences),
            'fixed_layout_cover': len(cover),
            'spoke_crossings_checked': crossing_count, 'exhaustive_cover': r <= 12}


def build(r):
    p, edges, poly = fan(r)
    return {'schema': 'c23-fan-placement-v1', 'verdict': 'candidate_only', 'r': r,
            'points': [[str(x), str(y)] for x, y in p], 'edges': edges,
            'polygon': [[str(x), str(y)] for x, y in poly],
            'nonedge_witness_rule': 'midpoint', 'parameter_domain': '3<=r<=32 for this CLI'}


def selftest():
    rs = list(range(3, 13)) + [16, 24, 32]
    rows = []
    for r in rs:
        if not audit_positive(r):
            raise AssertionError('positive construction')
        row = audit_convex_layout(r)
        row['one_obstacle_layout_checked'] = True
        rows.append(row)
    negative_controls = {'zero_shift_contacts_graph': not audit_positive(5, F(0)),
                         'overlarge_shift_misses_short_nonedge': not audit_positive(5, F(2)),
                         'unshifted_apex_hits_polygon': not audit_positive(5, F(1, 2), False)}
    if not all(negative_controls.values()):
        raise AssertionError('mutation not rejected')
    for bad in (True, 2, 33, F(4)):
        try:
            fan(bad)
        except ValueError:
            continue
        raise AssertionError('invalid parameter')
    return {'verdict': 'candidate_only', 'arithmetic': 'fractions.Fraction', 'controls': rows,
            'negative_controls': negative_controls, 'invalid_parameters_rejected': 4,
            'unrestricted_root_closed': False}


if __name__ == '__main__':
    if len(sys.argv) > 2:
        raise ValueError('zero or one integer argument required')
    print(json.dumps(build(int(sys.argv[1])) if len(sys.argv) == 2 else selftest(), sort_keys=True, separators=(',', ':')))
