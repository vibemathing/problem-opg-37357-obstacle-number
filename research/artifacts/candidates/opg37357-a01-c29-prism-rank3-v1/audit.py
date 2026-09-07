"""C28 consumer and complete Boolean census, no producer or C22/C26 imports.
All inputs are in memory. Exact integer truth vectors enumerate every orientation.
"""
from itertools import combinations, permutations, product
from collections import Counter


def need(ok, message):
    if not ok:
        raise ValueError(message)


def rederive(data):
    n = data['n']; need(type(n) is int and 3 <= n <= 6, 'consumer order cap')
    need(type(data['variables']) is int and data['path_limit']==n-1, 'formula metadata')
    need(type(data['clauses']) is list and len(data['clauses']) <= 100000, 'clause cap')
    need(all(type(row) is list and all(type(v) is int and v != 0 for v in row) for row in data['clauses']), 'strict literal types')
    edge = {frozenset(e) for e in data['edges']}
    need(len(edge) == len(data['edges']) and all(len(e)==2 and all(type(v) is int and 0<=v<n for v in e) for e in edge), 'simple input')
    trip = list(combinations(range(n),3)); ts = [e for e in combinations(range(n),2) if frozenset(e) not in edge]
    need(data['triples']==[list(t) for t in trip] and data['nonedges']==[list(t) for t in ts], 'input/complement')
    def atom(a,b,c):
        t=[a,b,c]; need(len(set(t))==3,'distinct orientation arguments')
        k=t.index(min(t)); t=t[k:]+t[:k]
        return (trip.index(tuple(sorted(t)))+1)*(1 if t[1]<t[2] else -1)
    q=len(trip); z={(t,r):q+2*i+r+1 for i,t in enumerate(ts) for r in (0,1)}
    ordered=list(permutations(ts,2)); side={pair:q+2*len(ts)+i+1 for i,pair in enumerate(ordered)}
    need(data['variables']==q+2*len(ts)+len(side),'variable layout')
    adj={v:sorted(w for w in range(n) if frozenset((v,w)) in edge) for v in range(n)}
    paths={}
    for a,b in ts:
        frontier=[(a,)]; hits=[]
        for depth in range(n-1):
            future=[]
            for p in frontier:
                for v in adj[p[-1]]:
                    if v in p:
                        continue
                    pp=p+(v,)
                    if v==b:
                        hits.append(pp)
                    else:
                        future.append(pp)
            frontier=future
        paths[a,b]=sorted(hits)
    need(data['paths']==[{'target':list(t),'paths':[list(p) for p in paths[t]]} for t in ts], 'complete all-label path census')
    def clause(origin):
        family=origin[0]
        if family=='color':
            _,s,mode=origin; s=tuple(s)
            return [z[s,0],z[s,1]] if mode==0 else [-z[s,0],-z[s,1]]
        if family=='four':
            a,b,c,d=origin[1]
            # Negate the one forbidden implication assignment.
            bad=[(atom(a,b,c),True),(atom(a,c,d),True),(atom(a,d,b),True),(atom(b,c,d),False)]
        elif family=='five':
            _,t,mode=origin; a,b,c,d,e=t
            bad=[(atom(a,b,c),True),(atom(a,c,d),True),(atom(a,d,e),True),(atom(a,b,e),True),
                 (atom(a,b,d),bool(mode)),(atom(a,c,e),not bool(mode))]
        else:
            need(family=='key','source family')
            _,s,t,p,r,mode=origin; s,t,p=tuple(s),tuple(t),tuple(p)
            need((s,t) in side and p in paths[s] and r in (0,1) and mode in range(4),'key source data')
            a,b=s; c,d=t
            # Forbidden: same active color, key halfplane, wrong internal side.
            key_value=mode>=2; side_value=mode%2==0
            bad=[(z[s,r],True),(z[t,r],True),(side[s,t],side_value)]
            bad += [(atom(c,d,v),key_value) for v in p if v not in t]
            bad += [(atom(a,b,v),not side_value) for v in p[1:-1]]
        return [-v if value else v for v,value in bad]
    def normal(c):
        terms=set(c)
        return None if any(-v in terms for v in terms) else tuple(sorted(terms,key=lambda v:(abs(v),v)))
    expected=set()
    origins=[('four',t) for t in permutations(range(n),4)]
    origins += [('five',t,m) for t in permutations(range(n),5) for m in (0,1)]
    origins += [('color',s,m) for s in ts for m in (0,1)]
    origins += [('key',s,t,p,r,m) for s,t in ordered for p in paths[s] for r in (0,1) for m in range(4)]
    for origin in origins:
        row=normal(clause(origin))
        if row is not None:
            expected.add(row)
    need(data['clauses']==[list(c) for c in sorted(expected)],'missing, extra, reordered or false clause')
    need(len(data['origins'])==len(expected),'source census')
    for row,origin in zip(data['clauses'],data['origins']):
        need(normal(clause(origin))==tuple(row),'row/source mismatch')
    need(data['counts']==dict(Counter(o[0] for o in data['origins'])),'family count')
    return trip,ts,side,paths,atom,z


def truth_columns(q):
    N=1<<q; full=(1<<N)-1; cols=[]
    for i in range(q):
        block=1<<i; v=((1<<block)-1)<<block; width=2*block
        while width<N:
            v |= v<<width; width*=2
        cols.append(v)
    return N,full,cols


def complete_census(data):
    trip,ts,side,paths,atom,z=rederive(data); q=len(trip); k=len(ts)
    need(q<=20 and k<=6,'complete census resource domain')
    N,full,col=truth_columns(q)
    def literal(v):
        return col[v-1] if v>0 else full^col[-v-1]
    def disjoin(row):
        v=0
        for x in row: v |= literal(x)
        return v
    def conjoin(row):
        v=full
        for x in row: v &= literal(x)
        return v
    allowed=full
    for row,origin in zip(data['clauses'],data['origins']):
        if origin[0] in ('four','five'):
            allowed &= disjoin(row)
    pair_good={}; conflicts={}; pair_details=[]
    for (s,t),sid in side.items():
        # Consumer A: exact Shannon elimination of this side from actual CNF.
        extensions=[full,full]
        rows=0
        for row,origin in zip(data['clauses'],data['origins']):
            if origin[0]!='key' or abs(sid) not in map(abs,row) or origin[4]!=0:
                continue
            need(tuple(origin[1])==s and tuple(origin[2])==t,'side used outside its pair')
            need(-z[s,0] in row and -z[t,0] in row,'missing same-color guards')
            residual=disjoin([v for v in row if abs(v)<=q])
            need((sid in row)^(-sid in row),'exactly one side sign')
            forced_value=0 if sid in row else 1
            extensions[forced_value] &= residual; rows+=1
        projection=extensions[0]|extensions[1]
        # Consumer B: direct key-path meaning, without constructing any clause.
        plus=minus=0; a,b=s; c,d=t
        for path in paths[s]:
            C=[atom(c,d,v) for v in path if v not in t]
            J=[atom(a,b,v) for v in path[1:-1]]
            key=conjoin(C)|conjoin([-v for v in C])
            plus |= key & conjoin(J)
            minus |= key & conjoin([-v for v in J])
        semantic=full^(plus&minus)
        need(projection==semantic,'CNF side projection differs on some orientation')
        pair_good[s,t]=projection
        conflicts[s,t]=full^projection
        pair_details.append({'s':list(s),'t':list(t),'retained_paths':len(paths[s]),'canonical_color0_rows':rows,
                             'conflicting_valid_orientations':((full^projection)&allowed).bit_count()})
    color_masks=[]; total=0; union=0
    for colors in product((0,1),repeat=k):
        feasible=allowed
        for (s,t),good in pair_good.items():
            if colors[ts.index(s)]==colors[ts.index(t)]: feasible &= good
        count=feasible.bit_count(); total+=count; union|=feasible
        color_masks.append((colors,feasible))
    # Separate scalar coloring audit, grouped by exact conflict graph.
    upairs=list(combinations(range(k),2))
    conflict_bytes=[]
    for i,j in upairs:
        mask=conflicts[ts[i],ts[j]]|conflicts[ts[j],ts[i]]
        conflict_bytes.append(mask.to_bytes((N+7)//8,'little'))
    histogram=Counter(); raw=allowed.to_bytes((N+7)//8,'little')
    for byte_index,value in enumerate(raw):
        for b in range(8):
            if not (value>>b)&1: continue
            code=sum(1<<i for i,buf in enumerate(conflict_bytes) if (buf[byte_index]>>b)&1)
            histogram[code]+=1
    scalar_counts=Counter()
    for code,multiplicity in histogram.items():
        for colors in product((0,1),repeat=k):
            if all(colors[i]!=colors[j] for bit,(i,j) in enumerate(upairs) if code>>bit&1):
                scalar_counts[colors]+=multiplicity
    need(all(scalar_counts[c]==m.bit_count() for c,m in color_masks),'scalar census disagreement')
    need(union!=0,'seed is UNSAT; do not manufacture witness')
    # Lexicographic minimum in the declared full variable order, False < True.
    remaining=union; prefix=[]; xbits=[]
    for i in range(q):
        zero=remaining & (full^col[i]); pick=0 if zero else 1
        remaining=zero if zero else remaining&col[i]; xbits.append(pick)
        prefix.append({'variable':i+1,'value':pick,'feasible_directions':remaining.bit_count()})
    index=sum(v<<i for i,v in enumerate(xbits))
    choices=[c for c,m in color_masks if (m>>index)&1]
    colors=min(choices,key=lambda c:tuple(int(c[i]==r) for i in range(k) for r in (0,1)))
    bits=xbits+[int(colors[i]==r) for i in range(k) for r in (0,1)]+[0]*len(side)
    def row_value(row):
        return any(bool(bits[abs(v)-1])==(v>0) for v in row)
    for (s,t),sid in side.items():
        rows=[row for row in data['clauses'] if sid in row or -sid in row]
        bits[sid-1]=0
        if not all(row_value(row) for row in rows): bits[sid-1]=1
        need(all(row_value(row) for row in rows),'side extension failed')
    need(all(row_value(row) for row in data['clauses']),'full model does not satisfy')
    side_one_reasons=[]
    for sid in side.values():
        if bits[sid-1]:
            bits[sid-1]=0
            failed=next(i+1 for i,row in enumerate(data['clauses']) if not row_value(row))
            bits[sid-1]=1
            side_one_reasons.append({'variable':sid,'zero_fails_row':failed})
    return {'verdict':'candidate_only','logical_status':'SAT','trusted_receipt':False,
            'orientation_variables':q,'all_orientation_assignments':N,
            'onehot_valid_color_assignments':1<<k,'raw_color_bit_assignments':1<<(2*k),
            'orientation_color_pairs_exhausted':N*(1<<k),
            'valid_direction_axiom_assignments':allowed.bit_count(),
            'extendable_direction_assignments':union.bit_count(),
            'satisfiable_direction_color_pairs':total,
            'rejected_direction_assignments_after_all_colors':allowed.bit_count()-union.bit_count(),
            'color_counts':[{'colors':list(c),'orientations':m.bit_count()} for c,m in color_masks],
            'conflict_graph_histogram':[[code,count] for code,count in sorted(histogram.items())],
            'side_elimination_audits':pair_details,
            'minimal_assignment':bits,'minimal_orientation_index':index,
            'minimal_colors':list(colors),'lex_prefix_certificate':prefix,'minimal_side_one_reasons':side_one_reasons,
            'global_geometric_realizability_checked':False,
            'census_method':'integer truth vectors + exact side elimination; all projected assignments, not random drawings'}
