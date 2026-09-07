"""C21: exhaustive sign cells via strict Fourier--Motzkin elimination.
This does not use C20's face-side sampling producer or any C20 source.
"""
from fractions import Fraction as F
from itertools import product
from exact_primitives import require


def choose_interval(lower, upper):
    if lower and upper and max(lower) >= min(upper):
        return None
    if lower and upper:
        return (max(lower)+min(upper))/2
    if lower:
        return max(lower)+1
    if upper:
        return min(upper)-1
    return F(0)


def strict_witness(rows):
    """Return rational (x,y) satisfying all a*x+b*y+c>0, or None."""
    require(len(rows) <= 10, 'at most 10 support lines in this checker')
    pos = [(a,b,c) for a,b,c in rows if a > 0]
    neg = [(a,b,c) for a,b,c in rows if a < 0]
    one = [(F(b),F(c)) for a,b,c in rows if a == 0]
    for a,b,c in pos:
        for d,e,f in neg:
            one.append((F(a*e-d*b), F(a*f-d*c)))
    low, high = [], []
    for b,c in one:
        if b == 0 and c <= 0:
            return None
        if b > 0:
            low.append(-c/b)
        if b < 0:
            high.append(-c/b)
    y = choose_interval(low, high)
    if y is None:
        return None
    x = choose_interval([F(-b*y-c)/a for a,b,c in pos],
                        [F(-b*y-c)/a for a,b,c in neg])
    if x is None:
        return None
    require(all(a*x+b*y+c > 0 for a,b,c in rows), 'elimination back substitution')
    return x,y


def all_cells(lines):
    require(len(lines) <= 10, 'cell enumeration refusal, not a mathematical NO')
    result = {}
    for signs in product((-1, 1), repeat=len(lines)):
        rows = [tuple(s*v for v in line) for s,line in zip(signs, lines)]
        witness = strict_witness(rows)
        if witness is not None:
            result[signs] = witness
    return result
