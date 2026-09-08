"""Exact consumer for two arbitrary simple polygon obstacles.
No constructor, arrangement core, graph library or numerical tolerances.
"""
from fractions import Fraction as Q
from itertools import combinations

def need(ok,message):
    if not ok:raise ValueError(message)

def rational(x):
    need(type(x) in (int,str,Q),'exact scalar required')
    if type(x) is str:need(len(x)<=300,'scalar length')
    q=Q(x);need(max(q.numerator.bit_length(),q.denominator.bit_length())<=1024,'scalar bit cap')
    return q

def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def contains_on_segment(p,a,b):
    return cross(a,b,p)==0 and all(min(a[i],b[i])<=p[i]<=max(a[i],b[i]) for i in (0,1))

def meet(a,b,c,d):
    if any(max(a[i],b[i])<min(c[i],d[i]) or max(c[i],d[i])<min(a[i],b[i]) for i in (0,1)):return False
    x,y,z,w=cross(a,b,c),cross(a,b,d),cross(c,d,a),cross(c,d,b)
    if x*y<0 and z*w<0:return True
    return (x==0 and contains_on_segment(c,a,b) or y==0 and contains_on_segment(d,a,b)
            or z==0 and contains_on_segment(a,c,d) or w==0 and contains_on_segment(b,c,d))

def membership(p,P):
    winding=0
    for a,b in zip(P,P[1:]+P[:1]):
        if contains_on_segment(p,a,b):return 0
        det=cross(a,b,p)
        if a[1]<=p[1]<b[1] and det>0:winding+=1
        elif b[1]<=p[1]<a[1] and det<0:winding-=1
    return 1 if winding else -1

def check_simple(P):
    n=len(P);need(3<=n<=128 and len(set(P))==n,'polygon vertex list')
    checks=0
    for i in range(n):
        a,b=P[i],P[(i+1)%n]
        for j in range(i+1,n):
            c,d=P[j],P[(j+1)%n]
            if j==i+1 or (i==0 and j==n-1):
                common=({a,b}&{c,d});need(len(common)==1,'adjacent endpoint')
                v=next(iter(common));u=next(x for x in (a,b) if x!=v);w=next(x for x in (c,d) if x!=v)
                need(not contains_on_segment(u,v,w) and not contains_on_segment(w,u,v),'adjacent overlap')
            else:need(not meet(a,b,c,d),'polygon nonadjacent contact');checks+=1
    area=sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(P,P[1:]+P[:1]))
    need(area>0,'CCW positive area')
    return checks

def verify(w):
    n=w['n'];need(type(n) is int and 5<=n<=16,'n domain')
    p=[tuple(rational(x) for x in t) for t in w['points']]
    need(len(p)==n and all(len(t)==2 for t in p) and len(set(p))==n,'injective point list')
    E=[tuple(e) for e in w['edges']];need(len(E)==len(set(E)) and all(len(e)==2 and all(type(v) is int for v in e) and 0<=e[0]<e[1]<n for e in E),'simple edges')
    targets=sorted(set(combinations(range(n),2))-set(E))
    need(len(w['polygons'])==2,'two obstacle list')
    polygons=[[tuple(rational(x) for x in v) for v in B] for B in w['polygons']]
    polygon_tests=sum(check_simple(B) for B in polygons)
    need(all(membership(v,B)==-1 for B in polygons for v in p),'graph point in closed obstacle')
    boundary_tests=0
    for a,b in E:
        for B in polygons:
            for c,d in zip(B,B[1:]+B[:1]):need(not meet(p[a],p[b],c,d),'graph edge hits obstacle');boundary_tests+=1
    A,B=polygons
    need(all(not meet(a,b,c,d) for a,b in zip(A,A[1:]+A[:1]) for c,d in zip(B,B[1:]+B[:1])),'obstacles touch')
    need(membership(A[0],B)==membership(B[0],A)==-1,'obstacles nested')
    need([tuple(h['target']) for h in w['witnesses']]==targets,'complete nonedge witness census')
    colors=[]
    for (a,b),h in zip(targets,w['witnesses']):
        t=rational(h['parameter']);need(0<t<1,'nonedge internal parameter')
        q=tuple((1-t)*p[a][i]+t*p[b][i] for i in (0,1));need(q==tuple(rational(x) for x in h['point']),'witness interpolation')
        r=h['obstacle'];need(type(r) is int and r in (0,1),'obstacle label')
        need(membership(q,polygons[r])==1,'witness not strict interior');colors.append(r)
    gp=all(cross(p[a],p[b],p[c])!=0 for a,b,c in combinations(range(n),3))
    return {'verdict':'candidate_only','accepted':True,'n':n,'edges':len(E),'nonedges':len(targets),
            'polygon_vertices':[len(B) for B in polygons],
            'polygon_nonadjacent_pairs':polygon_tests,'closed_edge_boundary_pairs':boundary_tests,
            'obstacle_boundary_pairs':len(A)*len(B),'strict_witnesses':len(targets),'colors':colors,'vertex_general_position':gp}

def verify_margin(w,certificate):
    p=[tuple(rational(x) for x in v) for v in w['points']];P=[[tuple(rational(x) for x in v) for v in B] for B in w['polygons']]
    eta=rational(certificate['eta_linf']);need(eta>0,'positive margin')
    want=[(i,r,j) for i in range(len(w['edges'])) for r in range(2) for j in range(len(P[r]))]
    need([tuple(row['index']) for row in certificate['edge_separators']]==want,'edge separator census')
    def check_sep(A,B,row):
        v=tuple(rational(x) for x in row['axis']);need(v!=(0,0),'separator axis')
        aa=[v[0]*x+v[1]*y for x,y in A];bb=[v[0]*x+v[1]*y for x,y in B]
        gap=max(min(bb)-max(aa),min(aa)-max(bb));need(gap>0,'not strict separator')
        need(gap==rational(row['gap']) and eta*(abs(v[0])+abs(v[1]))<gap,'margin does not preserve separator')
    for row in certificate['edge_separators']:
        i,r,j=row['index'];a,b=w['edges'][i];B=P[r];check_sep([p[a],p[b]],[B[j],B[(j+1)%len(B)]],row)
    want=[(i,j) for i,h in enumerate(w['witnesses']) for j in range(len(P[h['obstacle']]))]
    need([tuple(row['index']) for row in certificate['hit_separators']]==want,'hit separator census')
    for row in certificate['hit_separators']:
        i,j=row['index'];h=w['witnesses'][i];q=tuple(rational(x) for x in h['point']);B=P[h['obstacle']]
        check_sep([q],[B[j],B[(j+1)%len(B)]],row)
    need(all(2*eta<max(abs(a[k]-b[k]) for k in (0,1)) for a,b in combinations(p,2)),'point collision margin')
    return {'accepted':True,'eta_linf':str(eta),'edge_separators':len(certificate['edge_separators']),
            'hit_separators':len(certificate['hit_separators']),'scope':'all endpoint moves strictly below eta preserve fixed obstacles and fixed interpolation parameters'}

if __name__=='__main__':
    import sys,json
    text=sys.stdin.read(2_000_001);need(len(text)<=2_000_000,'input cap')
    print(json.dumps(verify(json.loads(text)),sort_keys=True,separators=(',',':')))
