"""C25: exact degree-four signs on D*. Pure memory; no external effects."""
from fractions import Fraction as F
from itertools import combinations


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sign(x):
    return (x > 0) - (x < 0)


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def determinant(a, b, c):
    return sum(x*y for x, y in zip(a, cross(b, c)))


def coordinates(raw):
    require(type(raw) is list and 3 <= len(raw) <= 8, 'domain: 3<=n<=8')
    out = []
    for row in raw:
        require(type(row) is list and len(row) == 2, 'point shape')
        point = []
        for x in row:
            require(type(x) in (int, str), 'exact integer or rational string required')
            if type(x) is str:
                require(len(x) <= 180 and x.count('/') <= 1, 'rational syntax/size')
                require(all(v.lstrip('-').isdigit() for v in x.split('/')), 'rational syntax')
            q = F(x)
            require(max(q.numerator.bit_length(), q.denominator.bit_length()) <= 256,
                    'rational bit cap')
            point.append(q)
        out.append(tuple(point))
    require(len(set(out)) == len(out), 'distinct points required')
    return out


def line_data(raw):
    p = coordinates(raw)
    pairs = list(combinations(range(len(p)), 2))
    lines = [cross((*p[i], F(1)), (*p[j], F(1))) for i, j in pairs]
    require(all(line[1] != 0 for line in lines), 'D*: vertical pair line')
    require(all(cross(a, b)[2] != 0 for a, b in combinations(lines, 2)),
            'D*: parallel/coincident pair lines or collinear vertex triple')
    return p, pairs, lines


def extract(raw):
    p, pairs, lines = line_data(raw)
    return {'schema': 'c25-quartic-signature-v1', 'n': len(p),
            'b': [sign(a[1]) for a in lines],
            'w': [sign(cross(a, b)[2]) for a, b in combinations(lines, 2)],
            'd': [sign(determinant(a, b, c)) for a, b, c in combinations(lines, 3)]}
