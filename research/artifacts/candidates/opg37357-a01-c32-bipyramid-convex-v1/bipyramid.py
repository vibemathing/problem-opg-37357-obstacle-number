"""Two disjoint convex obstacles for cyclic bipyramids. Exact bounded producer.
The all-N proof is in README; finite checks are not used as induction.
"""
from fractions import Fraction as Q
from itertools import combinations
from witness_check import require,cross,verify,inside,meet


def hull(points):
    points=sorted(set(points));require(len(points)>=3,'hull needs three points')
    def half(seq):
        out=[]
        for p in seq:
            while len(out)>1 and cross(out[-2],out[-1],p)<=0:out.pop()
            out.append(p)
        return out
    return half(points)[:-1]+half(points[::-1])[:-1]


def construct(N=5):
    require(type(N) is int and 4<=N<=24,'finite producer cap 4<=N<=24')
    n=N+2;M=N*N+1;eps=Q(1,16*(N+1));delta=Q(1,32*(M+N*N+1));q=-Q(M)-Q(1,2)
    points=[(Q(0),Q(-M)),(Q(0),Q(-M-1))]+[(Q(i),Q(i*i)) for i in range(1,N+1)]
    E={(h,j) for h in (0,1) for j in range(2,n)}
    E|={tuple(sorted((i+2,(i+1)%N+2))) for i in range(N)}
    targets=sorted(set(combinations(range(n),2))-E)
    midpoints=[tuple((points[a][j]+points[b][j])/2 for j in (0,1)) for a,b in targets if a>=2]
    leaf=hull([(x+dx,y+dy) for x,y in midpoints for dx in (-eps,eps) for dy in (-eps,eps)])
    hub=[(-delta,q-Q(1,8)),(delta,q-Q(1,8)),(delta,q+Q(1,8)),(-delta,q+Q(1,8))]
    faces=[]
    for i in range(N):
        a=i+2;b=(i+1)%N+2;faces.extend([[0,a,b],[1,b,a]])
    rot=[]
    for v in range(n):
        nxt={}
        for face in faces:
            if v in face:
                i=face.index(v);nxt[face[i-1]]=face[(i+1)%3]
        a=min(nxt);row=[a]
        while nxt[row[-1]]!=a:
            require(len(row)<n,'rotation loop');row.append(nxt[row[-1]])
        rot.append(row)
    return {'n':n,'cycle_order':N,'edges':list(map(list,sorted(E))),'nonedges':list(map(list,targets)),
            'selected_targets':list(map(list,targets)) if N==5 else [],'faces':faces,'rotation':rot,
            'points':[[str(x) for x in p] for p in points],
            'targets':list(map(list,targets)),'polygons':[[[str(x) for x in p] for p in poly] for poly in (hub,leaf)],
            'hits':[{'target':list(s),'parameter':'1/2','label':0 if s==(0,1) else 1} for s in targets],
            'parameters':{'M':M,'epsilon':str(eps),'delta':str(delta)},'verdict':'candidate_only'}


def check(data):
    N=data['cycle_order'];n=data['n'];E=set(map(tuple,data['edges']))
    require(n==N+2 and len(E)==3*N,'graph census')
    expected={(h,j) for h in (0,1) for j in range(2,n)}|{tuple(sorted((i+2,(i+1)%N+2))) for i in range(N)}
    require(E==expected,'exact bipyramid graph')
    darts={(a,b) for e in E for a,b in (e,e[::-1])};actual=[]
    for f in data['faces']:
        require(len(f)==len(set(f))==3,'face');actual.extend(zip(f,f[1:]+f[:1]))
    require(len(actual)==len(darts) and set(actual)==darts and len(data['faces'])==2*N,'complete sphere darts')
    require(n-len(E)+len(data['faces'])==2,'sphere Euler')
    for v,row in enumerate(data['rotation']):
        require(set(row)=={b if a==v else a for a,b in E if v in (a,b)} and len(set(row))==len(row),'rotation neighbors')
        for f in data['faces']:
            if v in f:
                i=f.index(v);require(row[(row.index(f[i-1])+1)%len(row)]==f[(i+1)%3],'rotation faces')
    result=verify(data)
    polys=[[tuple(map(Q,p)) for p in poly] for poly in data['polygons']]
    for poly in polys:
        require(all(cross(poly[i-1],poly[i],poly[(i+1)%len(poly)])>0 for i in range(len(poly))),'strict convexity')
    require(max(x for x,y in polys[0])<min(x for x,y in polys[1]),'obstacle separation')
    # Finite instances of the symbolic all-N inequalities; no sampled edge points.
    eps=Q(data['parameters']['epsilon'])
    for x,y in polys[1]:
        require(y-x*x>Q(3,4),'parabola clearance')
        require(all(y-(2*k+1)*x+k*(k+1)>0 for k in range(1,N)),'lower cycle boundaries')
        require((N+1)*x-N-y>0,'closing cycle boundary')
    result.update({'n':n,'edges':len(E),'nonedges':len(data['nonedges']),
                   'polygon_corners':[len(p) for p in polys],'sphere_faces':len(data['faces']),
                   'minimum_degree':min(len(r) for r in data['rotation'])})
    return result
