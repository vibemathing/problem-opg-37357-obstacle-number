"""Candidate all-placement necessary-condition CNF for X_r; no solver imports.
Original method: Berman et al., JGAA 21(6), Proposition 3 and Lemmas 1--3.
The explicit construction here uses only simple paths with at most 4 edges.
"""
from __future__ import annotations
import itertools as I
def make_graph(r:int):
    if type(r) is not int or not 3<=r<=6: raise ValueError("r outside candidate budget")
    n=2*r+2; north,south=0,1
    a=lambda i:2+(i%r); b=lambda i:2+r+(i%r)
    E=set(); faces=[]
    for i in range(r):
        E.update(tuple(sorted(e)) for e in [(north,a(i)),(south,b(i)),(a(i),a(i+1)),(b(i),b(i+1)),(a(i),b(i)),(a(i+1),b(i))])
        faces.extend([(north,a(i),a(i+1)),(south,b(i+1),b(i)),(a(i),b(i),a(i+1)),(a(i+1),b(i),b(i+1))])
    return n, sorted(E), faces

def cnf(r:int,max_length:int):
    if type(max_length) is not int or not 2<=max_length<=4: raise ValueError("path budget")
    n,edges,faces=make_graph(r); V=tuple(range(n)); es=set(edges)
    triples={t:i+1 for i,t in enumerate(I.combinations(V,3))}
    def x(a,b,c):
        t=(a,b,c); inv=sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))
        return triples[tuple(sorted(t))]*(-1 if inv%2 else 1)
    clauses=set(); counts={}
    def add(ls):
        v=set(ls)
        if any(-a in v for a in v): return
        clauses.add(tuple(sorted(v,key=lambda a:(abs(a),a))))
    for a,b,c,d in I.permutations(V,4): add([-x(a,b,c),-x(a,c,d),-x(a,d,b),x(b,c,d)])
    counts['four']=len(clauses)
    for a,b,c,d,e in I.permutations(V,5):
        h=[-x(a,b,c),-x(a,c,d),-x(a,d,e),-x(a,b,e)]
        add(h+[x(a,b,d),-x(a,c,e)]); add(h+[-x(a,b,d),x(a,c,e)])
    counts['five']=len(clauses)-counts['four']
    missing=[e for e in I.combinations(V,2) if e not in es]
    adj=[[] for _ in V]
    for u,v in edges: adj[u].append(v);adj[v].append(u)
    for ns in adj: ns.sort()
    def paths(a,b):
        out=[]
        def rec(p):
            u=p[-1]
            if len(p)-1==max_length:return
            for v in adj[u]:
                if v in p:continue
                if v==b:out.append(tuple(p+[v]))
                else:rec(p+[v])
        rec([a]);return out
    side={}; nextid=len(triples)+1; npaths=0
    for a,b in missing:
        ps=paths(a,b);npaths+=len(ps)
        for c,d in missing:
            if (a,b)==(c,d):continue
            s=nextid;nextid+=1;side[(a,b,c,d)]=s
            for path in ps:
                cd=[x(c,d,v) for v in path if v not in (c,d)]
                ab=[x(a,b,v) for v in path[1:-1]]
                # Resolve away the path-indicator variable in published (4)--(7).
                for cs in (cd,[-z for z in cd]):
                    add(cs+[-s]+ab);add(cs+[s]+[-z for z in ab])
    counts['key']=len(clauses)-counts['four']-counts['five']
    return n,edges,faces,nextid-1,sorted(clauses),counts,triples,side,npaths

def dimacs(r=4, max_length=4):
    n, es, faces, nv, clauses, counts, triples, sides, paths = cnf(r, max_length)
    data = (f"p cnf {nv} {len(clauses)}\n" + "\n".join(" ".join(map(str,c))+" 0" for c in clauses)+"\n").encode("ascii")
    return data, {"n":n,"edges":es,"faces":faces,"variables":nv,"clauses":clauses,"blocks":counts,"paths":paths}
