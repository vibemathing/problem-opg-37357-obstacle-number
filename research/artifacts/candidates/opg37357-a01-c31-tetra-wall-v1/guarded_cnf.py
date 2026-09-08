"""C31 all-simple-path necessary CNF and direct witness evaluation.
Complete four/five-point implications; one label bit per nonedge. Pure math.
"""
from itertools import combinations,permutations
from collections import Counter
from witness_check import require,cross

def normalized(row):
    r=set(row)
    return None if any(-x in r for x in r) else tuple(sorted(r,key=lambda x:(abs(x),x)))

def build(graph):
    n=graph['n'];E=set(map(tuple,graph['edges']))
    require(type(n) is int and 3<=n<=8,'n bound')
    require(len(E)==len(graph['edges']) and all(0<=a<b<n for a,b in E),'simple graph')
    triples=list(combinations(range(n),3));targets=sorted(set(combinations(range(n),2))-E)
    require([list(t) for t in targets]==graph['nonedges'],'full nonedge list')
    ids={t:i+1 for i,t in enumerate(triples)};q=len(ids);m=len(targets)
    sides={(i,j):q+m+k+1 for k,(i,j) in enumerate(permutations(range(m),2))}
    def o(a,b,c):
        require(len({a,b,c})==3,'orientation endpoints')
        sign=(-1 if ((a>b)+(a>c)+(b>c))%2 else 1)
        return sign*ids[tuple(sorted((a,b,c)))]
    paths=[]
    for a,b in targets:
        adj={v:sorted(w for w in range(n) if tuple(sorted((v,w))) in E) for v in range(n)}
        pending=[(a,)];out=[]
        while pending:
            p=pending.pop()
            for w in adj[p[-1]]:
                if w in p:continue
                if w==b:out.append(p+(b,))
                else:pending.append(p+(w,))
        paths.append(sorted(out))
    # Separate finite permutation census prevents a missing DFS branch.
    for i,(a,b) in enumerate(targets):
        expected=[];rest=[v for v in range(n) if v not in (a,b)]
        for k in range(1,n-1):
            for word in permutations(rest,k):
                p=(a,)+word+(b,)
                if all(tuple(sorted(e)) in E for e in zip(p,p[1:])):expected.append(p)
        require(paths[i]==sorted(expected),'complete simple path census')
    origins={};raw=0
    def add(c,source):
        nonlocal raw
        raw+=1;require(raw<=2_000_000,'raw row budget')
        r=normalized(c)
        if r is not None and r not in origins:origins[r]=source
    for a,b,c,d in permutations(range(n),4):
        add([-o(a,b,c),-o(a,c,d),-o(a,d,b),o(b,c,d)],['four',[a,b,c,d]])
    for a,b,c,d,e in permutations(range(n),5):
        pre=[-o(a,b,c),-o(a,c,d),-o(a,d,e),-o(a,b,e)]
        for sign in (1,-1):add(pre+[sign*o(a,b,d),-sign*o(a,c,e)],['five',[a,b,c,d,e],sign])
    for (i,j),side in sides.items():
        a,b=targets[i];c,d=targets[j]
        for p in paths[i]:
            C=[o(c,d,v) for v in p if v not in (c,d)];J=[o(a,b,v) for v in p[1:-1]]
            for mode in range(4):
                R=([side]+[-v for v in J]) if mode%2 else ([-side]+J)
                R+=C if mode<2 else [-v for v in C]
                for label in (0,1):
                    guard=[(1-2*label)*(q+i+1),(1-2*label)*(q+j+1)]
                    add(guard+R,['key',i,j,list(p),mode,label])
    rows=sorted(origins)
    return {'n':n,'variables':q+m+len(sides),'triples':[list(t) for t in triples],'targets':[list(s) for s in targets],
            'side_pairs':[[i,j,v] for (i,j),v in sides.items()],'paths':[[list(p) for p in ps] for ps in paths],
            'clauses':[list(r) for r in rows],'origins':[origins[r] for r in rows],
            'counts':dict(Counter(origins[r][0] for r in rows)),'raw_rows':raw,'path_limit':n-1}

def fixed_color_models(cnf,points):
    q=len(cnf['triples']);m=len(cnf['targets']);bits=[None]+[cross(*(points[i] for i in t))>0 for t in cnf['triples']]
    require(all(cross(*(points[i] for i in t))!=0 for t in cnf['triples']),'GP')
    # Evaluate the actual CNF with fixed directions; each side occurs in its own rows only.
    residual=[]
    for row in cnf['clauses']:
        if any(abs(v)<=q and bits[abs(v)]==(v>0) for v in row):continue
        r=[v for v in row if abs(v)>q]
        require(r,'direction implication violated');residual.append(r)
    out={}
    for word in range(1<<m):
        force={};ok=True
        for r in residual:
            if any(q<abs(v)<=q+m and bool(word>>(abs(v)-q-1)&1)==(v>0) for v in r):continue
            rest=[v for v in r if abs(v)>q+m]
            require(len(rest)<=1,'side separability')
            if not rest:ok=False;break
            v=rest[0]
            if abs(v) in force and force[abs(v)]!=(v>0):ok=False;break
            force[abs(v)]=v>0
        if ok:
            model=bits[1:]+[bool(word>>i&1) for i in range(m)]+[force.get(v,False) for v in range(q+m+1,cnf['variables']+1)]
            out[word]=model
    return out

def check_model(cnf,model):
    require(len(model)==cnf['variables'] and all(type(b) is bool for b in model),'model domain')
    require(all(any(model[abs(v)-1]==(v>0) for v in r) for r in cnf['clauses']),'CNF model failure')
    return True

def dimacs(cnf):
    return f"p cnf {cnf['variables']} {len(cnf['clauses'])}\n"+''.join(' '.join(map(str,r))+' 0\n' for r in cnf['clauses'])

def check_origins(graph,cnf):
    """Second literal reconstruction via cyclic parity, not producer's inversions."""
    n=graph['n'];E=set(map(tuple,graph['edges']));triples=list(combinations(range(n),3))
    T=[tuple(t) for t in cnf['targets']];q=len(triples);m=len(T)
    def o(a,b,c):
        t=(a,b,c);require(len(set(t))==3,'origin orientation')
        j=t.index(min(t));sgn=1 if t[(j+1)%3]<t[(j+2)%3] else -1
        return sgn*(triples.index(tuple(sorted(t)))+1)
    require(len(cnf['clauses'])==len(cnf['origins']),'origin count')
    for row,src in zip(cnf['clauses'],cnf['origins']):
        if src[0]=='four':
            a,b,c,d=src[1];r=[-o(a,b,c),-o(a,c,d),-o(a,d,b),o(b,c,d)]
        elif src[0]=='five':
            a,b,c,d,e=src[1];s=src[2];require(s in (-1,1),'five mode')
            r=[-o(a,b,c),-o(a,c,d),-o(a,d,e),-o(a,b,e),s*o(a,b,d),-s*o(a,c,e)]
        else:
            require(src[0]=='key','origin family');_,i,j,p,mode,label=src
            require(i!=j and mode in range(4) and label in (0,1),'key origin')
            a,b=T[i];c,d=T[j]
            require(p[0]==a and p[-1]==b and len(set(p))==len(p) and 3<=len(p)<=n,'path shape')
            require(all(tuple(sorted(e)) in E for e in zip(p,p[1:])),'path has nonedge')
            sid=q+m+1+i*(m-1)+j-(j>i)
            r=[(1-2*label)*(q+i+1),(1-2*label)*(q+j+1)]
            r+=[(1 if mode<2 else -1)*o(c,d,v) for v in p if v not in (c,d)]
            r+=([sid]+[-o(a,b,v) for v in p[1:-1]]) if mode%2 else ([-sid]+[o(a,b,v) for v in p[1:-1]])
        require(tuple(row)==normalized(r),'clause/source mismatch')
    return len(cnf['clauses'])
