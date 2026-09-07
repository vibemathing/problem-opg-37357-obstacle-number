"""C28 second CNF consumer. No generator/C22/C26 imports.
Uses clause-residual unit forcing, rather than enumerating geometric key paths
when counting direction/color models. Integer bit slices cover every direction.
"""
from itertools import combinations, product


def demand(ok,msg):
    if not ok:raise ValueError(msg)


def check_sources(data):
    n=data['n'];demand(type(n) is int and n==6,'instance domain')
    T=((0,1),(2,3),(4,5));E=set(combinations(range(n),2))-set(T)
    triples=list(combinations(range(n),3));order=[(s,t) for s in T for t in T if s!=t]
    demand(data['edges']==[list(e) for e in sorted(E)],'wrong graph')
    demand(data['targets']==[list(t) for t in T] and data['variables']==32,'variable census')
    demand(data['modules']==[[0,1,2,3],[2,3,4,5],[0,1,4,5]],'module census')
    demand(data['orientation_triples']==[list(t) for t in triples],'triple map')
    demand(data['z_variables']==[[list(t),r,21+2*i+r] for i,t in enumerate(T) for r in (0,1)],'color map')
    demand(data['side_variables']==[[list(s),list(t),27+i] for i,(s,t) in enumerate(order)],'side map')
    def o(a,b,c):
        v=(b-a)*(c-a)*(c-b)
        demand(v!=0,'repeated orientation endpoint')
        return (1 if v>0 else -1)*(triples.index(tuple(sorted((a,b,c))))+1)
    def norm(c):
        terms=set(c)
        if terms.intersection(-v for v in terms):return None
        return tuple(sorted(terms,key=lambda v:(abs(v),v)))
    def equation(origin):
        k=origin[0]
        if k=='exact_one':
            _,s,mode=origin; i=T.index(tuple(s));demand(mode in (0,1),'color mode')
            return [(-1 if mode else 1)*(21+2*i+r) for r in (0,1)]
        if k in ('four','five'):
            args=origin[1];demand(len(set(args))==len(args)==(4 if k=='four' else 5),'tuple census')
            demand(all(type(v) is int and 0<=v<n for v in args),'tuple type')
            a,b,c,d,*extra=args
            if k=='four':return [-o(a,b,c),-o(a,c,d),-o(a,d,b),o(b,c,d)]
            e=extra[0];mode=origin[2];demand(mode in (0,1),'five mode')
            a1,b1=o(a,b,d),o(a,c,e)
            tail=[a1,-b1] if mode==0 else [-a1,b1]
            return [-o(a,b,c),-o(a,c,d),-o(a,d,e),-o(a,b,e)]+tail
        demand(k=='key','unknown origin')
        _,s,t,path,r,mode=origin;s,t=tuple(s),tuple(t)
        demand((s,t) in order and r in (0,1) and mode in range(4),'key origin')
        demand(tuple((path[0],path[-1]))==s and len(set(path))==len(path),'path endpoints')
        demand(3<=len(path)<=6 and all(tuple(sorted(e)) in E for e in zip(path,path[1:])),'path graph')
        a,b=s;c,d=t;sid=27+order.index((s,t))
        pre=[o(c,d,v)*(1 if mode<2 else -1) for v in path if v not in t]
        J=[o(a,b,v) for v in path[1:-1]]
        tail=[-sid]+J if mode%2==0 else [sid]+[-v for v in J]
        return [-21-2*T.index(s)-r,-21-2*T.index(t)-r]+pre+tail
    # Independently enumerate all raw origins: Cartesian words, not permutations/DFS.
    sources=[]
    for s in T:
        sources.extend([['exact_one',list(s),m] for m in (0,1)])
    for size in (4,5):
        for t in product(range(n),repeat=size):
            if len(set(t))!=size:continue
            if size==4:sources.append(['four',list(t)])
            else:sources.extend([['five',list(t),m] for m in (0,1)])
    path_census={}; paths_by_length={}
    for s in T:
        ps=[]
        for size in range(1,5):
            for word in product([v for v in range(n) if v not in s],repeat=size):
                if len(set(word))!=size:continue
                path=(s[0],)+word+(s[1],)
                if all(tuple(sorted(e)) in E for e in zip(path,path[1:])):ps.append(path)
        path_census[str(s)]=len(ps)
        paths_by_length[str(s)]={str(j):sum(len(p)-1==j for p in ps) for j in range(2,6)}
        for t in T:
            if s==t:continue
            for p in ps:
                for r in (0,1):
                    sources.extend([['key',list(s),list(t),list(p),r,m] for m in range(4)])
    expected={norm(equation(s)) for s in sources};expected.discard(None)
    rows=data['rows'];demand(len(rows)==len(expected),'clause census')
    actual=[]
    for i,row in enumerate(rows):
        demand(row['id']==i+1,'row ID')
        c=tuple(row['clause']);demand(all(type(v) is int and 0<abs(v)<=32 for v in c),'literal range')
        demand(c==norm(equation(row['origin'])),'row source mismatch')
        actual.append(c)
    demand(actual==sorted(expected),'complete clause set/order')
    demand(data['raw_clause_count']==len(sources),'raw clause count')
    return {'complete_rows':len(actual),'raw_rows':len(sources),'paths':path_census,'path_lengths':paths_by_length}


def masks():
    width=1<<20;full=(1<<width)-1;result=[]
    for j in range(20):
        half=1<<j;v=((1<<half)-1)<<half;length=2*half
        while length<width:
            v|=v<<length;length*=2
        result.append(v)
    return full,result


def census(data):
    """Exhaustive all-direction evaluation directly on the published CNF.
    A residual clause has zero or one side literal. Two force sets conflict
    exactly on their intersection; this eliminates all 64 side assignments.
    """
    full,planes=masks();results=[]
    for colors in range(8):
        force0=[0]*6;force1=[0]*6;ok=full
        for row in data['rows']:
            sat=0;side=[];constant=False
            for v in row['clause']:
                a=abs(v)
                if a<=20:sat|=planes[a-1] if v>0 else full^planes[a-1]
                elif a<=26:
                    target,r=divmod(a-21,2)
                    value=((colors>>target)&1)==r
                    if value==(v>0):constant=True;break
                else:side.append(v)
            if constant:continue
            demand(len(side)<=1,'non-unit side residual')
            if not side:ok&=sat
            elif side[0]>0:force1[side[0]-27]|=full^sat
            else:force0[-side[0]-27]|=full^sat
        for a,b in zip(force0,force1):ok&=full^(a&b)
        results.append({'coloring_code':colors,'orientations':ok.bit_count(),
                        'first_orientation':(ok&-ok).bit_length()-1 if ok else None})
    return results


def model_check(data,model):
    demand(len(model)==32 and [abs(v) for v in model]==list(range(1,33)),'model shape')
    bits={abs(v):v>0 for v in model}
    demand(all(any(bits[abs(v)]==(v>0) for v in row['clause']) for row in data['rows']),'unsatisfied clause')
    return True


def check_rotation(graph):
    E={tuple(e) for e in graph['edges']};rot=graph['rotation'];n=graph['n']
    demand(len(rot)==n and len(E)==len(graph['edges']),'rotation/edge census')
    for u in range(n):
        demand(len(rot[u])==len(set(rot[u])) and set(rot[u])=={b if a==u else a for a,b in E if u in (a,b)},'neighbors')
    darts={(a,b) for e in E for a,b in (e,tuple(reversed(e)))}
    faces=[]
    while darts:
        start=min(darts);u,v=start;f=[]
        while True:
            demand((u,v) in darts,'face repeats a dart');darts.remove((u,v));f.append(u)
            row=rot[v];u,v=v,row[(row.index(u)+1)%len(row)]
            if (u,v)==start:break
        faces.append(f)
    reached={0}
    for _ in range(n):reached|={b for a,b in E if a in reached}|{a for a,b in E if b in reached}
    demand(len(reached)==n and n-len(E)+len(faces)==2,'connected sphere Euler test')
    demand(all(len(f)==3 for f in faces),'triangular face census')
    return faces
