"""Stand-alone exact consumer for simple filled polygon obstacle witnesses.
No producer, arrangement, CNF or graph-library imports. All contacts are closed.
"""
from fractions import Fraction as F
from itertools import combinations

def require(test,reason):
    if not test: raise ValueError(reason)
def rat(v):
    require(type(v) in (str,int,F),'exact rational input only')
    if isinstance(v,str):require(len(v)<=256,'rational length cap')
    q=F(v);require(max(q.numerator.bit_length(),q.denominator.bit_length())<=1024,'rational bit cap')
    return q
def orient(a,b,c):
    return a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1])
def on_segment(q,a,b):
    return orient(a,b,q)==0 and sum((q[k]-a[k])*(q[k]-b[k]) for k in (0,1))<=0
def intersect(a,b,c,d):
    v=[orient(a,b,c),orient(a,b,d),orient(c,d,a),orient(c,d,b)]
    return (v[0]*v[1]<0 and v[2]*v[3]<0) or any((on_segment(c,a,b),on_segment(d,a,b),on_segment(a,c,d),on_segment(b,c,d)))
def sides(P):return list(zip(P,P[1:]+P[:1]))
def location(q,P):
    winding=0
    for a,b in sides(P):
        if on_segment(q,a,b):return 0
        if a[1]<=q[1]<b[1] and orient(a,b,q)>0:winding+=1
        if b[1]<=q[1]<a[1] and orient(a,b,q)<0:winding-=1
    return 1 if winding else -1

def separation(a,b,c,d):
    """Find a separating projection; positive gap/L1(norm) is an exact bound."""
    vecs=[(F(1),F(0)),(F(0),F(1))]
    for u,v in ((a,b),(c,d)):
        x,y=v[0]-u[0],v[1]-u[1];vecs.extend([(x,y),(-y,x)])
    bounds=[]
    for x,y in vecs:
        norm=abs(x)+abs(y)
        if not norm:continue
        ab=[x*p[0]+y*p[1] for p in (a,b)];cd=[x*p[0]+y*p[1] for p in (c,d)]
        gap=max(min(ab)-max(cd),min(cd)-max(ab))
        if gap>0:bounds.append((gap/norm,(x,y),gap))
    require(bool(bounds),'no strict segment separator')
    return max(bounds)

def verify(w):
    n=w['n'];require(type(n)is int and 1<=n<=16,'vertex cap')
    p=[tuple(rat(v) for v in a) for a in w['points']]
    require(len(p)==n and all(len(a)==2 for a in p) and len(set(p))==n,'injective points')
    E=[tuple(s) for s in w['edges']]
    require(len(E)==len(set(E)) and all(len(s)==2 and all(type(v)is int for v in s) and 0<=s[0]<s[1]<n for s in E),'simple graph')
    N=sorted(set(combinations(range(n),2))-set(E));require(N==[tuple(s) for s in w['nonedges']],'complete complement')
    P=[[tuple(rat(v) for v in a) for a in poly] for poly in w['polygons']]
    require(1<=len(P)<=2,'at most two obstacles');selftests=0
    for poly in P:
        l=len(poly);require(3<=l<=512 and len(set(poly))==l,'polygon vertices')
        require(sum(a[0]*b[1]-a[1]*b[0] for a,b in sides(poly))>0,'counterclockwise boundary')
        for i in range(l):require(orient(poly[i-1],poly[i],poly[(i+1)%l])!=0,'nonredundant corners')
        for i,j in combinations(range(l),2):
            if (i-j)%l in (1,l-1):continue
            require(not intersect(*sides(poly)[i],*sides(poly)[j]),'polygon self intersection');selftests+=1
    bounds=[];edge_tests=0;separators=[]
    for pi,poly in enumerate(P):
        require(all(location(q,poly)==-1 for q in p),'graph vertex in closed obstacle')
        for a,b in E:
            for si,(c,d) in enumerate(sides(poly)):
                require(not intersect(p[a],p[b],c,d),'closed graph edge hits obstacle boundary')
                val,axis,gap=separation(p[a],p[b],c,d);bounds.append(val/2)
                separators.append({'edge':[a,b],'polygon':pi,'side':si,'axis':list(map(str,axis)),'gap':str(gap)})
                edge_tests+=1
    if len(P)==2:
        require(all(location(q,P[1])==-1 for q in P[0]) and all(location(q,P[0])==-1 for q in P[1]),'nested polygons')
        require(not any(intersect(a,b,c,d) for a,b in sides(P[0]) for c,d in sides(P[1])),'obstacles intersect')
    H=w['hits'];require(len(H)==len(N),'hit census')
    allocation=[]
    for s,h in zip(N,H):
        require(tuple(h['target'])==s,'hit target ordering');t=rat(h['parameter']);require(0<t<1,'relative interior parameter')
        r=h['obstacle'];require(type(r)is int and 0<=r<len(P),'obstacle index')
        a,b=(p[i] for i in s);q=tuple((1-t)*a[k]+t*b[k] for k in (0,1))
        require(q==tuple(map(rat,h['point'])) and location(q,P[r])==1,'strict witness')
        for c,d in sides(P[r]):bounds.append(separation(q,q,c,d)[0]/2)
        allocation.append(r)
    gp=all(orient(p[a],p[b],p[c]) for a,b,c in combinations(range(n),3));require(gp,'vertex general position')
    bounds.append(min(max(abs(a[k]-b[k]) for k in (0,1)) for a,b in combinations(p,2))/4)
    eta=F(1)
    while eta>=min(bounds):eta/=2
    return {'accepted':True,'graph_edges':len(E),'nonedges':len(N),'corners':[len(poly) for poly in P],'self_pair_checks':selftests,'edge_side_checks':edge_tests,'colors':allocation,'eta_linf':str(eta),'separators':separators,'assurance':'candidate_only'}
if __name__=='__main__':
    import sys,json
    print(json.dumps(verify(json.load(sys.stdin)),sort_keys=True,separators=(',',':')))
