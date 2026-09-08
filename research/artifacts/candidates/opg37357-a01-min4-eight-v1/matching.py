"""Exact control for nonedge-matching concentration, not a full G representation."""
from fractions import Fraction as F
from itertools import combinations
from witness_check import orient,intersect,location,sides

def build(n,E,M):
    if not 2<=n<=16:raise ValueError('bounded implementation n=2..16; proof is all n')
    E=set(map(tuple,E));M=list(map(tuple,M));used=[v for e in M for v in e]
    if len(set(used))!=len(used) or any(not(0<=a<b<n) or (a,b) in E for a,b in M):raise ValueError('not a nonedge matching')
    if not M:raise ValueError('nonempty matching required')
    q=len(M);p=[None]*n
    for j,(a,b) in enumerate(M,1):p[a]=(F(1),F(j));p[b]=(F(-1),F(-j))
    for j,v in enumerate(i for i in range(n) if p[i] is None):p[v]=(F(2),F(2*q+2*j+1))
    B=2*n+1;eps=F(1,8*B);step=eps/(4*n*n);poly=[(-eps,-eps),(eps,-eps),(eps,eps),(-eps,eps)]
    for j in range(2*len(list(combinations(range(n),3)))+1):
        t=step/(j+1);pp=[(a[0]+t*i,a[1]+t*i*i) for i,a in enumerate(p)]
        if all(orient(pp[a],pp[b],pp[c]) for a,b,c in combinations(range(n),3)):break
    else:raise ValueError('finite polynomial-root bound violated')
    if any(intersect(pp[a],pp[b],u,v) for a,b in E for u,v in sides(poly)):raise ValueError('graph edge blocked')
    if any(location(a,poly)!=-1 for a in pp):raise ValueError('graph point blocked')
    if any(location(tuple((pp[a][k]+pp[b][k])/2 for k in (0,1)),poly)!=1 for a,b in M):raise ValueError('matching miss')
    return {'points':[[str(x) for x in a] for a in pp],'polygon':[[str(x) for x in a] for a in poly],
            'matching':[list(s) for s in M],'epsilon':str(eps),'perturbation_t':str(t),'trials':j+1,
            'full_graph_obstacle_representation_claimed':False,'meaning':'one genuine free component meets all selected matching nonedges'}
