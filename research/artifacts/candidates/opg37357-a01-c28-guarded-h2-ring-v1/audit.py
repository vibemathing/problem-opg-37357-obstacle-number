"""C28 scalar cross-check. No bit-parallel enumerator or prior CNF imports.
Coordinates are not assumed from a rotation system. Pure finite computation.
"""
from itertools import combinations, permutations


def need(ok,text):
    if not ok: raise ValueError(text)


def rotation_check(n,edges,rotation):
    e={tuple(sorted(x)) for x in edges};darts={(a,b) for a,b in e}|{(b,a) for a,b in e}
    need(set(rotation)==set(range(n)), 'rotation domain')
    for v in range(n):
        row=rotation[v];expected={b for a,b in darts if a==v}
        need(len(row)==len(set(row)) and set(row)==expected,'rotation neighbor census')
    seen=set();faces=[]
    for start in sorted(darts):
        if start in seen: continue
        u,v=start;face=[]
        for _ in range(len(darts)+1):
            need((u,v) not in seen,'premature dart repeat')
            seen.add((u,v));face.append(u)
            row=rotation[v];u,v=v,row[(row.index(u)+1)%len(row)]
            if (u,v)==start:break
        else:raise ValueError('nonclosing face')
        faces.append(face)
    reach={0}
    for _ in range(n): reach|={b for a,b in darts if a in reach}
    need(len(reach)==n and seen==darts and n-len(e)+len(faces)==2,'not a connected sphere rotation')
    return faces


def literal(n,a,b,c):
    ts=list(combinations(range(n),3));t=(a,b,c)
    need(len(set(t))==3 and all(type(v) is int and 0<=v<n for v in t),'triple indices')
    j=t.index(min(t));sign=1 if t[(j+1)%3]<t[(j+2)%3] else -1
    return sign*(ts.index(tuple(sorted(t)))+1)


def origin_row(n,edges,source):
    targets=sorted(set(combinations(range(n),2))-set(edges));triples=list(combinations(range(n),3))
    z={s:len(triples)+i+1 for i,s in enumerate(targets)}
    pairs=[(s,t) for s in targets for t in targets if s!=t]
    side={p:len(triples)+len(targets)+i+1 for i,p in enumerate(pairs)}
    o=lambda a,b,c:literal(n,a,b,c)
    if source[0]=='four':
        a,b,c,d=source[1];need(len(set(source[1]))==4,'four indices')
        row=[-o(a,b,c),-o(a,c,d),-o(a,d,b),o(b,c,d)]
    elif source[0]=='five':
        a,b,c,d,e=source[1];mode=source[2];need(len(set(source[1]))==5 and mode in (0,1),'five origin')
        row=[-o(a,b,c),-o(a,c,d),-o(a,d,e),-o(a,b,e)]+([o(a,b,d),-o(a,c,e)] if not mode else[-o(a,b,d),o(a,c,e)])
    else:
        need(source[0]=='key' and len(source)==7,'key record')
        _,s,t,p,neg,which,color=source;s=tuple(s);t=tuple(t)
        need((s,t) in side and all(type(i) is int and i in (0,1) for i in (neg,which,color)), 'guard identity')
        need(3<=len(p)<=n and len(p)==len(set(p)) and tuple((p[0],p[-1]))==s,'simple complete path')
        need(all(tuple(sorted(q)) in edges for q in zip(p,p[1:])),'nonedge used as path')
        row=([z[s],z[t]] if color==0 else [-z[s],-z[t]])
        row += [(-1 if neg else 1)*o(*t,v) for v in p if v not in t]
        row += [-side[s,t]]+[o(*s,v) for v in p[1:-1]] if not which else [side[s,t]]+[-o(*s,v) for v in p[1:-1]]
    need(not any(-q in row for q in row),'tautological stored row')
    return tuple(sorted(set(row), key=lambda x:(abs(x),x)))


def record_check(enc,clauses,origins):
    need(len(clauses)==len(origins)==len(enc.clauses),'complete fixed row census')
    need(clauses==sorted(set(clauses)),'canonical row order')
    for c,r in zip(clauses,origins):need(origin_row(enc.n,enc.edges,r)==c,'row does not follow source')
    return len(clauses)


def scalar_orientations(n,clauses):
    """Visits every direction bit word using scalar masks, no whole-domain bitsets."""
    nd=n*(n-1)*(n-2)//6;need(nd<=20,'scalar domain')
    masks=[(sum(1<<(nd-q) for q in c if q>0),sum(1<<(nd+q) for q in c if q<0)) for c in clauses]
    return [v for v in range(1<<nd) if all((v&p) or ((~v)&m) for p,m in masks)]


def scalar_colors(n,edges,orientations):
    triples=list(combinations(range(n),3));nd=len(triples)
    targets=sorted(set(combinations(range(n),2))-set(edges));pairs=[(s,t) for s in targets for t in targets if s!=t]
    adj={v:sorted({b if a==v else a for a,b in edges if v in (a,b)}) for v in range(n)}
    paths={}
    for s in targets:
        stack=[(s[0],)];out=[]
        while stack:
            p=stack.pop()
            for v in adj[p[-1]]:
                if v in p:continue
                q=p+(v,)
                if v==s[1]:out.append(q)
                else:stack.append(q)
        paths[s]=out
    def requirement(lits):
        values={}
        for lit in lits:
            var=abs(lit)
            if var in values and values[var]!=(lit>0):return None
            values[var]=lit>0
        return sum(1<<(nd-v) for v in values),sum(1<<(nd-v) for v,b in values.items() if b)
    patterns={}
    for s,t in pairs:
        cases=[set(),set()]
        for path in paths[s]:
            key=[literal(n,*t,v) for v in path if v not in t];inter=[literal(n,*s,v) for v in path[1:-1]]
            for r in (0,1):
                for k in (0,1):
                    req=requirement([q if k else -q for q in key]+[q if r else -q for q in inter])
                    if req is not None:cases[r].add(req)
        patterns[s,t]=cases
    k=len(targets);counts=[0]*(1<<k);first=None;with_color=0
    for word in orientations:
        incompatible=[]
        for i,j in combinations(range(k),2):
            s,t=targets[i],targets[j]
            if any(all(any((word&mask)==val for mask,val in patterns[p][r]) for r in (0,1)) for p in [(s,t),(t,s)]):
                incompatible.append((i,j))
        any_color=False
        for z in range(1<<k):
            if all(((z>>(k-1-i))&1)!=((z>>(k-1-j))&1) for i,j in incompatible):
                counts[z]+=1;any_color=True
                if first is None:first=[word,z]
        with_color+=any_color
    return {'counts_by_color_word':counts,'minimum':first,'orientations_with_some_two_labeling':with_color,
            'path_census':sum(map(len,paths.values()))}
