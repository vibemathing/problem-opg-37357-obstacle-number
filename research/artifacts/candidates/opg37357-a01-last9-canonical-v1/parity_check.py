"""Second exact polygon consumer: parametric intersections and ray parity.
No constructor, NB9 checker, arrangement, or CNF imports. Candidate domain only.
"""
from fractions import Fraction as Q
from itertools import combinations

def need(ok,why):
 if not ok:raise ValueError(why)

def point(a):
 need(len(a)==2 and all(type(x) in (str,int,Q) for x in a),'exact point')
 p=tuple(Q(x) for x in a);need(all(max(x.numerator.bit_length(),x.denominator.bit_length())<=1024 for x in p),'bit cap');return p

def det(u,v):return u[0]*v[1]-u[1]*v[0]
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def on(p,a,b):return det(sub(p,a),sub(b,a))==0 and all(min(a[i],b[i])<=p[i]<=max(a[i],b[i]) for i in (0,1))

def intersection(a,b,c,d):
 u,v,w=sub(b,a),sub(d,c),sub(c,a);D=det(u,v)
 if D:
  t,s=det(w,v)/D,det(w,u)/D
  return {(a[0]+t*u[0],a[1]+t*u[1])} if 0<=t<=1 and 0<=s<=1 else set()
 if det(w,u):return set()
 return {p for p in (a,b,c,d) if on(p,a,b) and on(p,c,d)}

def inside(p,P):
 odd=False
 for a,b in zip(P,P[1:]+P[:1]):
  if on(p,a,b):return 0
  if (a[1]>p[1])!=(b[1]>p[1]):
   x=a[0]+(p[1]-a[1])*(b[0]-a[0])/(b[1]-a[1])
   if x>p[0]:odd=not odd
 return 1 if odd else -1

def check(W):
 n=W['n'];need(type(n)is int and 5<=n<=16,'n')
 p=list(map(point,W['points']));need(len(p)==n and len(set(p))==n,'distinct vertices')
 E=[tuple(e) for e in W['edges']];need(len(set(E))==len(E) and all(len(e)==2 and all(type(v)is int for v in e) and 0<=e[0]<e[1]<n for e in E),'edges')
 N=[list(e) for e in combinations(range(n),2) if e not in E];need([h['target'] for h in W['witnesses']]==N,'full complement')
 polys=[list(map(point,B)) for B in W['polygons']];need(len(polys)==2,'two disks');np=ep=cp=0
 for P in polys:
  m=len(P);need(3<=m<=128 and len(set(P))==m,'polygon vertices')
  need(sum(det(a,b) for a,b in zip(P,P[1:]+P[:1]))>0,'positive area')
  for i,j in combinations(range(m),2):
   a,b=P[i],P[(i+1)%m];c,d=P[j],P[(j+1)%m];I=intersection(a,b,c,d)
   if j==i+1 or (i,j)==(0,m-1):need(I=={b if j==i+1 else a},'adjacent only endpoint')
   else:need(not I,'boundary simple');np+=1
  need(all(inside(a,P)==-1 for a in p),'exterior vertices')
  for u,v in E:
   for a,b in zip(P,P[1:]+P[:1]):need(not intersection(p[u],p[v],a,b),'closed graph edge contact');ep+=1
 A,B=polys
 for a,b in zip(A,A[1:]+A[:1]):
  for c,d in zip(B,B[1:]+B[:1]):need(not intersection(a,b,c,d),'obstacle contact');cp+=1
 need(inside(A[0],B)==inside(B[0],A)==-1,'no nesting')
 for h in W['witnesses']:
  u,v=h['target'];t=Q(h['parameter']);need(0<t<1,'strict interpolation');q=tuple((1-t)*a+t*b for a,b in zip(p[u],p[v]))
  need(q==point(h['point']),'hit coordinates');r=h['obstacle'];need(type(r)is int and r in (0,1),'color');need(inside(q,polys[r])==1,'hit interior')
 return {'accepted':True,'verdict':'candidate_only','method':'parametric closed-segment intersections plus horizontal-ray parity','n':n,'edges':len(E),'nonedges':len(N),'polygon_vertices':list(map(len,polys)),'nonadjacent_pairs':np,'edge_side_pairs':ep,'cross_obstacle_pairs':cp,'strict_hits':len(N)}
