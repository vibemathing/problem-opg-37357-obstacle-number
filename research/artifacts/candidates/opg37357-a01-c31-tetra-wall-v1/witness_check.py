"""Exact simple filled-polygon visibility checker; no arrangement dependency."""
from fractions import Fraction as Q
from itertools import combinations

def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def on(q,a,b):
    return cross(a,b,q)==0 and (q[0]-a[0])*(q[0]-b[0])+(q[1]-a[1])*(q[1]-b[1])<=0

def meet(a,b,c,d):
    return (cross(a,b,c)*cross(a,b,d)<0 and cross(c,d,a)*cross(c,d,b)<0) or any((on(a,c,d),on(b,c,d),on(c,a,b),on(d,a,b)))

def inside(p,poly):
    if any(on(p,a,b) for a,b in zip(poly,poly[1:]+poly[:1])):return 0
    w=0
    for a,b in zip(poly,poly[1:]+poly[:1]):
        if a[1]<=p[1]<b[1] and cross(a,b,p)>0:w+=1
        if b[1]<=p[1]<a[1] and cross(a,b,p)<0:w-=1
    return 1 if w else -1

def require(x,msg):
    if not x:raise ValueError(msg)

def rational_points(rows):
    require(type(rows) is list and 3<=len(rows)<=128,'point row bound')
    out=[]
    for row in rows:
        require(type(row) is list and len(row)==2,'point shape')
        require(all(type(x) in (int,str) for x in row),'exact coordinate syntax')
        p=tuple(Q(x) for x in row)
        require(all(max(x.numerator.bit_length(),x.denominator.bit_length())<=256 for x in p),'bit bound')
        out.append(p)
    require(len(set(out))==len(out),'repeated points')
    return out

def verify(data):
    P=rational_points(data['points']); n=len(P)
    E=[tuple(e) for e in data['edges']]
    require(all(len(e)==2 and all(type(v) is int for v in e) and 0<=e[0]<e[1]<n for e in E),'edge syntax')
    require(len(E)==len(set(E)),'duplicate edges')
    targets=sorted(set(combinations(range(n),2))-set(E))
    require(data['targets']==[list(s) for s in targets],'complete complement')
    polys=[rational_points(row) for row in data['polygons']]
    require(1<=len(polys)<=2,'obstacle count')
    count={'polygon_side_pairs':0,'graph_edge_polygon_side_pairs':0,'vertex_tests':0,'target_tests':0,'crossings':0}
    for poly in polys:
        m=len(poly);sides=list(zip(poly,poly[1:]+poly[:1]))
        require(sum(a[0]*b[1]-a[1]*b[0] for a,b in sides)!=0,'polygon area')
        for i in range(m):
            require(cross(poly[i-1],poly[i],poly[(i+1)%m])!=0,'adjacent backtrack/collinearity')
        for i,j in combinations(range(m),2):
            if (j-i)%m in (1,m-1):continue
            require(not meet(*sides[i],*sides[j]),'self-intersecting polygon');count['polygon_side_pairs']+=1
        for p in P:
            require(inside(p,poly)==-1,'graph vertex in closed polygon');count['vertex_tests']+=1
        for u,v in E:
            for a,b in sides:
                require(not meet(P[u],P[v],a,b),'graph edge meets closed polygon');count['graph_edge_polygon_side_pairs']+=1
    require([w['target'] for w in data['hits']]==[list(s) for s in targets],'witness target order')
    for s,w in zip(targets,data['hits']):
        t=Q(w['parameter']);r=w['label']
        require(type(r) is int and 0<=r<len(polys) and 0<t<1,'hit type/domain')
        q=tuple((1-t)*P[s[0]][j]+t*P[s[1]][j] for j in (0,1))
        require(inside(q,polys[r])==1,'missing strict nonedge hit');count['target_tests']+=1
    for e,f in combinations(E,2):
        if len(set(e+f))==4 and cross(P[e[0]],P[e[1]],P[f[0]])*cross(P[e[0]],P[e[1]],P[f[1]])<0 and cross(P[f[0]],P[f[1]],P[e[0]])*cross(P[f[0]],P[f[1]],P[e[1]])<0:count['crossings']+=1
    require(all(cross(P[a],P[b],P[c])!=0 for a,b,c in combinations(range(n),3)),'vertex GP')
    return count

if __name__=='__main__':
    import json,sys
    d=json.load(sys.stdin);print(json.dumps(verify(d),sort_keys=True))
