"""C27 explicit clique-gluing counterexample: one convex obstacle for stars.
Exact rational arithmetic and finite convex hull; no external effects.
"""
from itertools import combinations, product
from fractions import Fraction as Q
from fiber import need, at, turn, hits


def hull(points):
    points = sorted(set(points)); need(len(points) >= 3, 'hull size')
    low, high = [], []
    for row, order in ((low,points),(high,list(reversed(points)))):
        for p in order:
            while len(row) >= 2 and turn(row[-2],row[-1],p) <= 0:
                row.pop()
            row.append(p)
    result = low[:-1]+high[:-1]; need(len(result) >= 3, 'nondegenerate polygon')
    return result


def star(r):
    need(type(r) is int and 3 <= r <= 30, 'star runtime cap 3..30')
    p = [(Q(0),Q(-r*r))]+[(Q(i),Q(i*i)) for i in range(1,r+1)]
    e = [(0,i) for i in range(1,r+1)]
    eps = Q(1,64*(r+1))
    mids = [at(p[i],p[j],Q(1,2)) for i,j in combinations(range(1,r+1),2)]
    polygon = hull([(x+u*eps,y+v*eps) for x,y in mids for u,v in product((-1,1),repeat=2)])
    return p,e,polygon


def verify(p,e,polygon):
    n = len(p); need(len(set(p)) == n, 'coincident vertex')
    sides = list(zip(polygon,polygon[1:]+polygon[:1]))
    need(all(turn(polygon[i-1],polygon[i],polygon[(i+1)%len(polygon)]) > 0 for i in range(len(polygon))), 'strict convexity')
    need(all(not all(turn(a,b,q)>=0 for a,b in sides) for q in p), 'graph point in polygon')
    need(all(not hits(p[i],p[j],a,b) for i,j in e for a,b in sides), 'closed graph edge hits polygon')
    missing = sorted(set(combinations(range(n),2))-set(e))
    witnesses = [at(p[i],p[j],Q(1,2)) for i,j in missing]
    need(all(all(turn(a,b,q)>0 for a,b in sides) for q in witnesses), 'nonedge midpoint not interior')
    need(all(turn(p[i],p[j],p[k])!=0 for i,j,k in combinations(range(n),3)), 'nonGP control')
    # Graph is a plane star, not just an abstract planarity assertion.
    need(all(set(hits(p[0],p[i],p[0],p[j]))=={p[0]} for i,j in combinations(range(1,n),2)), 'spoke overlap')
    return {'vertices':n,'edges':len(e),'nonedges':len(missing),'polygon_corners':len(polygon),
            'single_polygon_checked':True, 'demand_copies':n-2}
