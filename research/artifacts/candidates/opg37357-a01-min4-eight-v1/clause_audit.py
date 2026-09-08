"""MIN4 clause-source audit; reused from the attached BIP2 helper. Does not import the producer or geometric core."""
from itertools import combinations, product

def need(ok,why):
    if not ok:raise ValueError(why)

def check(data):
    n=data['n'];need(type(n) is int and 3<=n<=8,'n cap')
    E={tuple(e) for e in data['edges']};need(len(E)==len(data['edges']) and all(0<=a<b<n for a,b in E),'edges')
    T=list(combinations(range(n),3));O={t:i+1 for i,t in enumerate(T)}
    S=[s for s in combinations(range(n),2) if s not in E]
    Z={s:len(T)+i+1 for i,s in enumerate(S)}
    pairs=[(s,t) for s in S for t in S if s!=t];B={pair:len(T)+len(S)+i+1 for i,pair in enumerate(pairs)}
    need(data['triples']==[list(t) for t in T] and data['targets']==[list(s) for s in S],'variable map')
    need(data['color_variables']==[Z[s] for s in S] and data['variables']==len(T)+len(S)+len(B),'variable count')
    need(data['side_variables']==[{'variable':B[s,t],'ab':list(s),'cd':list(t)} for s,t in pairs],'side map')
    def o(a,b,c):
        need(len({a,b,c})==3 and all(type(v) is int and 0<=v<n for v in (a,b,c)),'orientation indices')
        return O[tuple(sorted((a,b,c)))]*(1 if (b-a)*(c-a)*(c-b)>0 else -1)
    def row(origin):
        kind=origin[0]
        if kind=='four':
            a,b,c,d=origin[1];need(len(set((a,b,c,d)))==4,'four tuple')
            return [-o(a,b,c),-o(a,c,d),-o(a,d,b),o(b,c,d)]
        if kind=='five':
            a,b,c,d,e=origin[1];m=origin[2];need(len(set((a,b,c,d,e)))==5 and type(m) is int and m in (0,1),'five tuple')
            v=1-2*m
            return [-o(a,b,c),-o(a,c,d),-o(a,d,e),-o(a,b,e),v*o(a,b,d),-v*o(a,c,e)]
        need(kind=='key' and len(origin)==6,'key origin')
        _,ab,cd,P,m,r=origin;ab=tuple(ab);cd=tuple(cd)
        need((ab,cd) in B and type(m) is int and m in range(4) and type(r) is int and r in (0,1),'key indices')
        need(3<=len(P)<=n and len(set(P))==len(P) and (P[0],P[-1])==ab,'simple path')
        need(all(tuple(sorted(e)) in E for e in zip(P,P[1:])),'nonedge in path')
        C=[o(*cd,v)*(1 if m<2 else -1) for v in P if v not in cd];J=[o(*ab,v) for v in P[1:-1]]
        tail=[-B[ab,cd]]+J if m%2==0 else [B[ab,cd]]+[-v for v in J]
        return [(1-2*r)*Z[ab],(1-2*r)*Z[cd]]+C+tail
    def norm(c):
        c=set(c)
        return None if any(-v in c for v in c) else tuple(sorted(c,key=lambda v:(abs(v),v)))
    # Breadth-first extensions, rather than producer's internal permutations.
    neighbors={v:sorted(b if a==v else a for a,b in E if v in (a,b)) for v in range(n)}
    Pmap={}
    for a,b in S:
        queue=[(a,)];found=[]
        for P in queue:
            for v in neighbors[P[-1]]:
                if v in P:continue
                q=P+(v,)
                if v==b:found.append(q)
                else:queue.append(q)
        Pmap[a,b]=sorted(found)
    need(data['paths']==[{'target':list(s),'paths':[list(p) for p in Pmap[s]]} for s in S],'complete path census')
    expected=set()
    for size in (4,5):
        for t in product(range(n),repeat=size):
            if len(set(t))!=size:continue
            for m in range(1 if size==4 else 2):
                origin=['four',t] if size==4 else ['five',t,m];expected.add(norm(row(origin)))
    for ab,cd in pairs:
        for P in Pmap[ab]:
            for m in range(4):
                for r in range(2):expected.add(norm(row(['key',ab,cd,P,m,r])))
    expected.discard(None)
    need(len(data['origins'])==len(data['clauses']),'origin census')
    actual=[];counts={}
    for c,s in zip(data['clauses'],data['origins']):
        need(all(type(v) is int and 0<abs(v)<=data['variables'] for v in c),'literal types/range')
        need(tuple(c)==norm(row(s)),'row-source mismatch')
        actual.append(tuple(c));counts[s[0]]=counts.get(s[0],0)+1
    need(actual==sorted(expected),'complete distinct clause set')
    return {'clauses':len(actual),'counts':counts,'paths':sum(map(len,Pmap.values())),'max_path_edges':max(len(p)-1 for ps in Pmap.values() for p in ps)}
