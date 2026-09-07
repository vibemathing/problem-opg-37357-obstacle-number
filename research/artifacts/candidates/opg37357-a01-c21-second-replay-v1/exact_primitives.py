"""C21: pure exact predicates. No file, network, process or dynamic-code access."""
from fractions import Fraction as F
from math import gcd, lcm


def require(test, message):
    if not test:
        raise ValueError(message)


def rational(value):
    require(type(value) in (int, str), 'rational must be an integer or string')
    if isinstance(value, str):
        require(len(value) <= 1300 and value.count('/') <= 1, 'rational size')
        for term in value.split('/'):
            require(term.lstrip('-').isdigit(), 'rational syntax')
    q = F(value)
    require(max(q.numerator.bit_length(), q.denominator.bit_length()) <= 4096,
            'rational bit limit')
    return q


def point(values):
    require(type(values) is list and len(values) == 2, 'point shape')
    return tuple(rational(v) for v in values)


def subtract(a, b):
    return a[0]-b[0], a[1]-b[1]


def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


def orientation(a, b, c):
    return cross(subtract(b, a), subtract(c, a))


def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]


def on_segment(x, a, b):
    return orientation(a, b, x) == 0 and dot(subtract(x, a), subtract(x, b)) <= 0


def meet(a, b, c, d):
    p, q = orientation(a, b, c), orientation(a, b, d)
    r, s = orientation(c, d, a), orientation(c, d, b)
    return (p*q < 0 and r*s < 0) or any((on_segment(c, a, b),
        on_segment(d, a, b), on_segment(a, c, d), on_segment(b, c, d)))


def interpolate(a, b, t):
    return tuple((1-t)*x+t*y for x, y in zip(a, b))


def primitive_line(p, q):
    require(p != q, 'line endpoints coincide')
    terms = (p[1]-q[1], q[0]-p[0], p[0]*q[1]-q[0]*p[1])
    denominator = lcm(*(v.denominator for v in terms))
    nums = [int(v*denominator) for v in terms]
    divisor = gcd(*nums)
    nums = [v//divisor for v in nums]
    if next(v for v in nums if v) < 0:
        nums = [-v for v in nums]
    return tuple(nums)


def value(line, p):
    a, b, c = line
    return a*p[0]+b*p[1]+c


def line_frame(line):
    a, b, c = line
    origin = (F(-c, a), F(0)) if a else (F(0), F(-c, b))
    return origin, (F(-b), F(a))


def parameter(p, origin, direction):
    j = 0 if direction[0] else 1
    t = (p[j]-origin[j])/direction[j]
    require(interpolate(origin, (origin[0]+direction[0], origin[1]+direction[1]), t) == p,
            'point not on parameter line')
    return t


def blocked(p, points, edges):
    return p in points or any(on_segment(p, points[i], points[j]) for i, j in edges)
