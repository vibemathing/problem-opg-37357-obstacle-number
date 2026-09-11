"""C28 direct rational polygon witness consumer. No arrangement or CNF imports.
Finite inputs only. Closed edge/polygon contacts are rejected.
"""
from fractions import Fraction as F
from itertools import combinations


def need(ok, text):
    if not ok: raise ValueError(text)


def orient(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def on(q,a,b):
    return orient(a,b,q)==0 and all(min(a[i],b[i])<=q[i]<=max(a[i],b[i]) for i in (0,1))


def intersections(a,b,c,d):
    u=(b[0]-a[0],b[1]-a[1]);v=(d[0]-c[0],d[1]-c[1])
    det=u[0]*v[1]-u[1]*v[0]
    if det:
        w=(c[0]-a[0],c[1]-a[1]);t=F(w[0]*v[1]-w[1]*v[0],det);s=F(w[0]*u[1]-w[1]*u[0],det)
        return [(a[0]+t*u[0],a[1]+t*u[1])] if 0<=t<=1 and 0<=s<=1 else []
    return sorted({q for q in (a,b,c,d) if on(q,a,b) and on(q,c,d)})


def location(q, polygon):
    """-1 outside, 0 boundary, 1 inside via an exact half-open ray."""
    odd=False
    for a,b in zip(polygon,polygon[1:]+polygon[:1]):
        if on(q,a,b): return 0
        if (a[1]>q[1])!=(b[1]>q[1]):
            x=a[0]+(q[1]-a[1])*(b[0]-a[0])/(b[1]-a[1])
            if x>q[0]:odd=not odd
    return 1 if odd else -1


def hull(raw):
    points=sorted(set(raw));lower=[];upper=[]
    for seq,out in ((points,lower),(reversed(points),upper)):
        for q in seq:
            while len(out)>1 and orient(out[-2],out[-1],q)<=0:out.pop()
            out.append(q)
    return lower[:-1]+upper[:-1]


def psegment_distance2(q,a,b):
    u=(b[0]-a[0],b[1]-a[1]);den=u[0]**2+u[1]**2
    t=max(F(0),min(F(1),((q[0]-a[0])*u[0]+(q[1]-a[1])*u[1])/den))
    return (q[0]-a[0]-t*u[0])**2+(q[1]-a[1]-t*u[1])**2


def check(points,edges,polygons):
    p=[tuple(F(v) for v in q) for q in points]
    polys=[[tuple(F(v) for v in q) for q in poly] for poly in polygons]
    need(len(p)<=32 and len(set(p))==len(p),'point domain')
    need(len(polys)<=2,'obstacle cap')
    es={tuple(sorted(e)) for e in edges};clear=[]
    for poly in polys:
        need(3<=len(poly)<=64 and len(set(poly))==len(poly),'polygon vertices')
        sides=list(zip(poly,poly[1:]+poly[:1]))
        for i,j in combinations(range(len(poly)),2):
            met=intersections(*sides[i],*sides[j])
            expected=set(sides[i]) & set(sides[j])
            need(set(met)==expected,'polygon self contact or crossing')
        need(all(location(q,poly)==-1 for q in p),'graph point not exterior')
        for i,j in es:
            a,b=p[i],p[j]
            for c,d in sides:
                need(not intersections(a,b,c,d),'blocked graph edge')
                clear += [psegment_distance2(a,c,d),psegment_distance2(b,c,d),
                          psegment_distance2(c,a,b),psegment_distance2(d,a,b)]
    witnesses=[]
    for i,j in combinations(range(len(p)),2):
        if (i,j) in es:continue
        a,b=p[i],p[j];axis=0 if a[0]!=b[0] else 1;found=None
        for r,poly in enumerate(polys):
            cuts={F(0),F(1)}
            for c,d in zip(poly,poly[1:]+poly[:1]):
                cuts.update((q[axis]-a[axis])/(b[axis]-a[axis]) for q in intersections(a,b,c,d))
            cuts=sorted(cuts)
            for lo,hi in zip(cuts,cuts[1:]):
                t=(lo+hi)/2;q=tuple(a[v]+t*(b[v]-a[v]) for v in (0,1))
                if location(q,poly)==1:
                    found={'pair':[i,j],'obstacle':r,'parameter':str(t),'point':list(map(str,q))};break
            if found:break
        need(found is not None,'unblocked nonedge');witnesses.append(found)
    for a,b in combinations(polys,2):
        need(all(location(q,b)==-1 for q in a) and all(location(q,a)==-1 for q in b),'obstacle containment')
        need(not any(intersections(x,y,u,v) for x,y in zip(a,a[1:]+a[:1]) for u,v in zip(b,b[1:]+b[:1])),'obstacle intersection')
    return {'accepted':True,'witnesses':witnesses,'corners':[len(poly) for poly in polys],
            'minimum_edge_boundary_distance_squared':str(min(clear)) if clear else None}


def examples(kind):
    points=[(F(i),F(-i*i)) for i in range(6)]
    if kind=='diamonds':
        mid=(F(1,2),F(-1,2));e=F(1,1000)
        first=[(mid[0]-e,mid[1]-e),(mid[0]+e,mid[1]-e),(mid[0]+e,mid[1]+e),(mid[0]-e,mid[1]+e)]
        qs=[(F(17,6),F(-9)),(F(11,4),F(-37,4)),(F(10,3),F(-35,3))]
        second=hull([(x+u*e,y+v*e) for x,y in qs for u in (-1,1) for v in (-1,1)])
        return points,[first,second]
    need(kind=='octahedron','example name')
    xs=list(map(F,['1/4','1/2','3/4','1','2','9/4','5/2','11/4','3','4','17/4','9/2','19/4']))
    def boundary(x):
        j=x.numerator//x.denominator
        return -(2*j+1)*x+j*(j+1)
    upper=[(x,boundary(x)+F(1,10)) for x in xs]
    lower=[(x,boundary(x)+(F(-1,20) if x in (F(1,2),F(5,2),F(9,2)) else F(1,20))) for x in xs]
    return points,[upper+list(reversed(lower))]


def port_chain(m):
    """Two convex obstacles for every suspension of a path; finite test cap 3..20."""
    need(type(m) is int and 3<=m<=20,'port-chain cap')
    R=m+1
    p=[(F(0),F(-R*R)),(F(-1),F(-R*R))]+[(F(i),F(i*i)) for i in range(1,m+1)]
    es=[(h,i) for h in (0,1) for i in range(2,m+2)]+[(i,i+1) for i in range(2,m+1)]
    eps=F(1,64*(m+1));mid=[]
    for i,j in combinations(range(2,m+2),2):
        if j-i>=2:mid.append(((p[i][0]+p[j][0])/2,(p[i][1]+p[j][1])/2))
    up=hull([(x+u*eps,y+v*eps) for x,y in mid for u in (-1,1) for v in (-1,1)])
    e=F(1,16);x=F(-1,2);y=F(-R*R)
    low=[(x-e,y-e),(x+e,y-e),(x+e,y+e),(x-e,y+e)]
    return p,es,[low,up]
