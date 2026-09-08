"""Pure finite structural certificate consumer; no NetworkX/atlas imports."""
from itertools import combinations,permutations,product,combinations_with_replacement

def need(t,w):
    if not t:raise ValueError(w)
def edge_set(es,n):
    E=set(map(tuple,es));need(len(E)==len(es) and all(len(e)==2 and 0<=e[0]<e[1]<n for e in E),'simple edges');return E
def reachable(n,E,cut=()):
    keep=set(range(n))-set(cut)
    if not keep:return set()
    got={min(keep)}
    for _ in range(n):
        nxt=got|{v for a,b in E for u,v in ((a,b),(b,a)) if u in got and v in keep}
        if nxt==got:break
        got=nxt
    return got

def rotation(n,E,R):
    need(len(R)==n,'rotation length')
    for u,row in enumerate(R):need(len(set(row))==len(row) and set(row)=={b if a==u else a for a,b in E if u in (a,b)},'neighbors')
    left={(a,b) for u,v in E for a,b in ((u,v),(v,u))};faces=[]
    while left:
        start=min(left);d=start;f=[]
        for _ in range(2*len(E)+1):
            need(d in left,'face repeats');left.remove(d);a,b=d;f.append(a);r=R[b];d=(b,r[(r.index(a)-1)%len(r)])
            if d==start:break
        else:raise ValueError('orbit cap')
        faces.append(f)
    need(len(reachable(n,E))==n and n-len(E)+len(faces)==2,'sphere Euler')
    need(all(len(f)==3 for f in faces),'triangular faces')
    return faces

def kuratowski(n,E,certificate):
    H=edge_set(certificate,n);need(H<=E,'minor edges');adj={v:set() for e in H for v in e}
    for a,b in H:adj[a].add(b);adj[b].add(a)
    branch={v for v in adj if len(adj[v])!=2};need(len(branch) in (5,6),'Kuratowski branch count')
    used=set();core=set()
    for a in sorted(branch):
        for b in sorted(adj[a]):
            if tuple(sorted((a,b))) in used:continue
            prev,at=a,b;used.add(tuple(sorted((prev,at))))
            for _ in range(n):
                if at in branch:break
                options=adj[at]-{prev};need(len(options)==1,'path split');nextv=next(iter(options));prev,at=at,nextv
                e=tuple(sorted((prev,at)));need(e not in used,'reused subdivision edge');used.add(e)
            else:raise ValueError('subdivision cap')
            e=tuple(sorted((a,at)));need(a!=at and e not in core,'subdivision core loop/duplicate');core.add(e)
    need(used==H,'uncovered subdivision edges')
    if len(branch)==5:need(core==set(combinations(sorted(branch),2)),'not K5')
    else:
        parts=[]
        for A in combinations(sorted(branch),3):
            A=set(A);B=branch-A
            if core=={tuple(sorted((a,b))) for a in A for b in B}:parts.append(A)
        need(bool(parts),'not K33')

def labelled_complements(n):
    """All sorted-degree labelled complements; only necessary pruning is used."""
    target=(n-3)*(n-4);pairs=list(combinations(range(n),2));bit={p:1<<i for i,p in enumerate(pairs)};out=set()
    def extend(i,d,code):
        if i==n:
            if not any(d):out.add(code)
            return
        pool=[j for j in range(i+1,n) if d[j]>0];k=d[i]
        if k<0 or k>len(pool):return
        for ns in combinations(pool,k):
            r=list(d);r[i]=0;c=code
            for j in ns:r[j]-=1;c|=bit[i,j]
            active=sum(v>0 for v in r[i+1:])
            if sum(r)%2 or any(v<0 or v>active-1 for v in r[i+1:] if v):continue
            extend(i+1,tuple(r),c)
    for seq in combinations_with_replacement(range(max(0,n-5)+1),n):
        if sum(seq)==target:extend(0,seq,0)
    return out

def relabelled_complements(n,reps):
    universe=set();pairs=list(combinations(range(n),2))
    for rec in reps:
        H=edge_set(rec['complement'],n);degrees=[sum(i in e for e in H) for i in range(n)]
        groups=[[i for i in range(n) if degrees[i]==d] for d in sorted(set(degrees))]
        orbit=set()
        for choices in product(*(list(permutations(g)) for g in groups)):
            order=sum((tuple(g) for g in choices),());code=sum(1<<i for i,(a,b) in enumerate(pairs) if tuple(sorted((order[a],order[b]))) in H)
            orbit.add(code)
        need(not (orbit & universe),'duplicate complement isomorphism class')
        universe.update(orbit)
    return universe

def audit(census):
    need(type(census) is dict and set(census['complement_representatives'])=={'5','6','7','8'},'complete order domain')
    results={};counts={}
    for key,records in census['complement_representatives'].items():
        n=int(key);need(5<=n<=8,'enumeration domain');labels=labelled_complements(n)
        need(labels==relabelled_complements(n,records),'complete sorted-degree extension coverage')
        admitted=[]
        for rec in records:
            E=set(combinations(range(n),2))-edge_set(rec['complement'],n)
            need(len(E)==3*n-6 and all(sum(i in e for e in E)>=4 for i in range(n)),'complement scope')
            kind=rec['kind']
            if kind=='nonplanar':kuratowski(n,E,rec['kuratowski'])
            elif kind=='separator':
                cut=rec['separator'];need(len(cut)<=3 and len(set(cut))==len(cut),'cut size')
                got=reachable(n,E,cut);need(0<len(got)<n-len(cut),'invalid separator')
            else:
                need(kind=='admissible','kind');f=rotation(n,E,rec['rotation'])
                for k in range(4):
                    for cut in combinations(range(n),k):need(len(reachable(n,E,cut))==n-k,'not four-connected')
                hubs=[list(s) for s in combinations(range(n),2) if s not in E and all(sum(v in e for e in E)==n-2 for v in s)]
                need(hubs==rec['hub_pairs'],'hub filter');admitted.append({'edges':sorted(E),'hub_pairs':hubs,'faces':f})
        results[key]=admitted;counts[key]={'degree_sorted_labelled_complements':len(labels),'representatives':len(records),'four_connected_triangulations':len(admitted),'non_bipyramid':sum(not x['hub_pairs'] for x in admitted)}
    return {'accepted':True,'counts':counts,'domain':'n=5..8','no_graph_library_import':True}

if __name__=="__main__":
    import sys,json
    print(json.dumps(audit(json.load(sys.stdin)),sort_keys=True,separators=(",",":")))
