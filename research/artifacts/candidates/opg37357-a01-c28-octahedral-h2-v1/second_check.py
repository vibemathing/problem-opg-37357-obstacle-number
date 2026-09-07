"""C28 scalar-direction / full-tail checker, separate from exhaustive.py.
Consumes clauses as data. No prior candidate core, solver or external effects.
"""
from itertools import combinations, permutations, product


def require(ok, message):
    if not ok:
        raise ValueError(message)


def norm(row):
    row = set(row)
    return None if any(-i in row for i in row) else tuple(sorted(row, key=lambda i:(abs(i),i)))


def reconstruct(data):
    es = {tuple(e) for e in data['edges']}
    require(len(es) == len(data['edges']), 'duplicate edges')
    require(all(len(e)==2 and 0<=e[0]<e[1]<6 for e in es), 'edges')
    targets = [e for e in combinations(range(6),2) if e not in es]
    require([list(e) for e in targets] == data['nonedges'], 'complement differs')
    tri = list(combinations(range(6),3)); tids = {v:i+1 for i,v in enumerate(tri)}
    require(data['orientation_triples'] == [list(t) for t in tri], 'triple order')
    require(data['z'] == [[21+2*i,22+2*i] for i in range(len(targets))], 'z map')
    pairs = [(a,b) for a in range(len(targets)) for b in range(len(targets)) if a!=b]
    sid = {v:21+2*len(targets)+i for i,v in enumerate(pairs)}
    require(data['side_pairs'] == [{'variable':sid[q],'target_indices':list(q)} for q in pairs], 'side map')
    require(data['variables']==20+2*len(targets)+len(pairs), 'variable census')
    def O(a,b,c):
        t=(a,b,c); ordered=sorted(t)
        # Rotation/reversal parity, rather than the producer's inversion count.
        positive = t in ((ordered[0],ordered[1],ordered[2]),
                         (ordered[1],ordered[2],ordered[0]),(ordered[2],ordered[0],ordered[1]))
        return tids[tuple(ordered)]*(1 if positive else -1)
    paths=[]
    for a,b in targets:
        row=[]
        # Enumerate all vertex words, then enforce distinctness and graph incidence.
        for length in range(1,5):
            for inner in product(range(6),repeat=length):
                p=(a,)+inner+(b,)
                if len(set(p)) == len(p) and all(tuple(sorted(e)) in es for e in zip(p,p[1:])):
                    row.append(p)
        paths.append(sorted(row))
    require(data['path_census'] == [[list(p) for p in row] for row in paths], 'path census')
    def origin_clause(o):
        family=o['family']
        if family=='four':
            a,b,c,d=o['tuple']; require(len(set((a,b,c,d)))==4, 'four tuple')
            return [-O(a,b,c),-O(a,c,d),-O(a,d,b),O(b,c,d)]
        if family=='five':
            a,b,c,d,e=o['tuple'];require(len(set((a,b,c,d,e)))==5 and o['flip'] in (0,1), 'five tuple')
            tail=[O(a,b,d),-O(a,c,e)]
            return [-O(a,b,c),-O(a,c,d),-O(a,d,e),-O(a,b,e)]+[v*(-1 if o['flip'] else 1) for v in tail]
        if family=='one':
            return [v*(1 if o['positive'] else -1) for v in data['z'][o['target']]]
        require(family=='key','origin family')
        i,j=o['targets'];p=tuple(o['path']);m=o['mode'];r=o['color']
        require((i,j) in sid and p in paths[i] and m in range(4) and r in range(2), 'key path/mode')
        require(o['nonedges']==[list(targets[i]),list(targets[j])] and o['side']==sid[i,j], 'key targets')
        a,b=targets[i];c,d=targets[j]
        C=[O(c,d,v) for v in p if v not in (c,d)];J=[O(a,b,v) for v in p[1:-1]]
        return [-data['z'][i][r],-data['z'][j][r]]+[v*(1 if m<2 else -1) for v in C]+(
            [-sid[i,j]]+J if m%2==0 else [sid[i,j]]+[-v for v in J])
    expected=set()
    def add(o):
        c=norm(origin_clause(o))
        if c is not None: expected.add(c)
    for t in permutations(range(6),4): add({'family':'four','tuple':t})
    for t in permutations(range(6),5):
        for f in (0,1): add({'family':'five','tuple':t,'flip':f})
    for i in range(len(targets)):
        for b in (False,True):add({'family':'one','target':i,'positive':b})
    for i,j in pairs:
        for p in paths[i]:
            for r in range(2):
                for m in range(4):add({'family':'key','targets':[i,j],'path':p,'mode':m,'color':r,
                                      'nonedges':[list(targets[i]),list(targets[j])],'side':sid[i,j]})
    require(data['clauses']==[list(c) for c in sorted(expected)], 'incomplete or changed clause set')
    require(len(data['origins'])==len(data['clauses']), 'origin length')
    for i,(c,o) in enumerate(zip(data['clauses'],data['origins'])):
        require(o['row']==i+1 and norm(origin_clause(o))==tuple(c), 'row source mismatch')
    return len(expected)


def scalar_table(data):
    require(len(data['nonedges'])==3 and data['variables']==32, 'full-tail checker scope: octahedron')
    # Each of the 512 bit positions is one of 8 labels x 64 side assignments.
    tails=[]
    for colors in product(range(2),repeat=3):
        for side in product((False,True),repeat=6):
            tails.append([colors[i]==r for i in range(3) for r in range(2)]+list(side))
    rows=[];pure=[]
    for clause in data['clauses']:
        pm=nm=0
        for lit in clause:
            if abs(lit)<=20:
                if lit>0:pm|=1<<(20-lit)
                else:nm|=1<<(20+lit)
        tail=[v for v in clause if abs(v)>20]
        tv=sum(1<<j for j,t in enumerate(tails) if any(t[abs(v)-21]==(v>0) for v in tail))
        rows.append((pm,nm,tv))
        if not tail:pure.append((pm,nm))
    # Visit every direction prefix. A false fully assigned clause excludes exactly
    # all its remaining completions. Track that partition's cardinality explicitly.
    activation=[[] for _ in range(21)]
    for pm,nm in pure:
        last=20-((pm|nm)&-(pm|nm)).bit_length()+1
        activation[last].append((pm,nm))
    counts=[0]*8; full_models=0; survivors=0; rejected=0; nodes=0
    def visit(depth,assignment):
        nonlocal full_models,survivors,rejected,nodes
        nodes+=1
        for pm,nm in activation[depth]:
            if not (assignment&pm) and assignment&nm==nm:
                rejected+=1<<(20-depth)
                return
        if depth<20:
            visit(depth+1,assignment)
            visit(depth+1,assignment|(1<<(19-depth)))
            return
        survivors+=1; tailmask=(1<<512)-1
        for pm,nm,tv in rows:
            if not (assignment&pm) and assignment&nm==nm:
                tailmask&=tv
        full_models+=tailmask.bit_count()
        for c in range(8):
            if tailmask>>(64*c)&((1<<64)-1):counts[c]+=1
    visit(0,0)
    require(rejected+survivors==1<<20,'direction partition not exhaustive')
    return {'orientation_survivors':survivors,'excluded_direction_completions':rejected,
            'direction_prefix_nodes':nodes,'projected_counts_by_lex_color':counts,
            'full_satisfying_direction_label_side_assignments':full_models,
            'expanded_direction_label_side_space':(1<<20)*512}
