"""Bounded exact sign signatures; memory-only candidate code, no real solver."""
from fractions import Fraction as F
from itertools import combinations


def sign(v):
    return (v > 0) - (v < 0)


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def orient(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def rational(v):
    if type(v) not in (int, str, F):
        raise ValueError('exact rational input required')
    if type(v) is str and (len(v) > 160 or any(c not in '0123456789+-/' for c in v)):
        raise ValueError('integer or ratio string required')
    q = F(v)
    if max(abs(q.numerator).bit_length(), q.denominator.bit_length()) > 256:
        raise ValueError('rational bit budget')
    return q


def encode(raw):
    if type(raw) not in (list, tuple) or not 3 <= len(raw) <= 6:
        raise ValueError('this implementation has 3<=n<=6')
    if any(type(p) not in (list, tuple) or len(p) != 2 for p in raw):
        raise ValueError('point shape')
    p = [tuple(rational(x) for x in point) for point in raw]
    pairs = list(combinations(range(len(p)), 2))
    lines = [cross((*p[i], F(1)), (*p[j], F(1))) for i, j in pairs]
    events = [cross(lines[a], lines[b]) for a, b in combinations(range(len(lines)), 2)]
    bsign = [sign(l[1]) for l in lines]
    osign = [sign(orient(p[i], p[j], p[k])) for i, j, k in combinations(range(len(p)), 3)]
    wsign = [sign(t[2]) for t in events]
    if 0 in bsign or 0 in osign or 0 in wsign:
        raise ValueError('outside D*: vertical pair, collinear triple or parallel pair-lines')
    hx, hy = [], []
    for u, v in combinations(range(len(events)), 2):
        x, y = events[u], events[v]
        hx.append(sign(x[0]*y[2]-y[0]*x[2]))
        hy.append(sign(x[1]*y[2]-y[1]*x[2]))
    return {'n': len(p), 'b': bsign, 'orientation': osign, 'w': wsign, 'hx': hx, 'hy': hy}


def event_comparators(s):
    n = s['n']
    if type(n) is not int or not 3 <= n <= 6:
        raise ValueError('signature n')
    pairs = list(combinations(range(n), 2))
    epairs = list(combinations(range(len(pairs)), 2))
    r = len(epairs)
    sizes = {'b': len(pairs), 'orientation': n*(n-1)*(n-2)//6,
             'w': r, 'hx': r*(r-1)//2, 'hy': r*(r-1)//2}
    if set(s) != set(sizes) | {'n'}:
        raise ValueError('signature keys')
    for name, size in sizes.items():
        if type(s[name]) is not list or len(s[name]) != size:
            raise ValueError('signature dimension')
        allowed = (-1, 0, 1) if name in ('hx', 'hy') else (-1, 1)
        if any(type(t) is not int or t not in allowed for t in s[name]):
            raise ValueError('signature signs')
    idx = {uv: i for i, uv in enumerate(combinations(range(r), 2))}
    def comparison(name, u, v):
        if u == v:
            return 0
        a, b = sorted((u, v))
        value = s[name][idx[a, b]] * s['w'][a] * s['w'][b]
        return value if u == a else -value
    return pairs, epairs, lambda u, v: comparison('hx', u, v), lambda u, v: comparison('hy', u, v)
