"""Candidate generator: X4 triangulated sphere and all-placement SAT relaxation.
No obstacle-size bound, fixed point set, or geometric realization is imposed.
"""
import argparse, itertools, json, math
from collections import Counter
from pathlib import Path


def graph(r=4):
    n=2*r+2; A=lambda i:1+i%r; B=lambda i:r+1+i%r
    N,S=0,n-1
    es=set(); fs=[]
    for i in range(r):
        for a,b in [(N,A(i)),(A(i),A(i+1)),(B(i),B(i+1)),(S,B(i)),(A(i),B(i)),(A(i+1),B(i))]:
            es.add(tuple(sorted((a,b))))
        fs += [(N,A(i),A(i+1)),(S,B(i+1),B(i)),(A(i+1),A(i),B(i)),(A(i+1),B(i),B(i+1))]
    return n,sorted(es),fs


def cnf(n, edges, outside=False, max_edges=9):
    adj=[set() for _ in range(n)]
    for a,b in edges: adj[a].add(b);adj[b].add(a)
    orient={t:i+1 for i,t in enumerate(itertools.combinations(range(n),3))}
    def x(a,b,c):
        t=(a,b,c)
        inversions=sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))
        return orient[tuple(sorted(t))]*(-1 if inversions%2 else 1)
    clauses=set(); counts={}
    def add(ls):
        ls=set(ls)
        if any(-v in ls for v in ls): return
        clauses.add(tuple(sorted(ls, key=lambda z:(abs(z),z))))
    for a,b,c,d in itertools.permutations(range(n),4):
        add([-x(a,b,c),-x(a,c,d),-x(a,d,b),x(b,c,d)])
    counts['four_point']=len(clauses)
    for a,b,c,d,e in itertools.permutations(range(n),5):
        pre=[-x(a,b,c),-x(a,c,d),-x(a,d,e),-x(a,b,e)]
        add(pre+[x(a,b,d),-x(a,c,e)])
        add(pre+[-x(a,b,d),x(a,c,e)])
    counts['five_point']=len(clauses)-counts['four_point']
    nonedges=[(a,b) for a,b in itertools.combinations(range(n),2) if b not in adj[a]]
    var=len(orient); names={str(i):['orientation',*t] for t,i in orient.items()}
    totalpaths=0; maxpath=0
    for a,b in nonedges:
        paths=[]
        def dfs(path):
            u=path[-1]
            if len(path)-1>=max_edges: return
            for v in sorted(adj[u]):
                if v in path: continue
                # Induced paths only: shortcut chords are unnecessary for this relaxation.
                if any(v in adj[w] for w in path[:-1]): continue
                if v==b: paths.append(tuple(path+[v]))
                else: dfs(path+[v])
        dfs([a]); totalpaths+=len(paths)
        maxpath=max(maxpath,max((len(p)-1 for p in paths),default=0))
        if outside:
            var+=1; s=var; names[str(s)]=['outside_side',a,b]
            for p in paths:
                ints=[x(a,b,v) for v in p[1:-1]]
                add([-s]+ints); add([s]+[-l for l in ints])
        else:
            for c,d in nonedges:
                if (a,b)==(c,d): continue
                var+=1;s=var;names[str(s)]=['keypath_side',a,b,c,d]
                for p in paths:
                    line=[x(c,d,v) for v in p if v!=c and v!=d]
                    ints=[x(a,b,v) for v in p[1:-1]]
                    for premise in [line,[-l for l in line]]:
                        add(premise+[-s]+ints)
                        add(premise+[s]+[-l for l in ints])
    counts['path_clauses']=len(clauses)-counts['four_point']-counts['five_point']
    # Whole-plane reflection reverses every orientation; select one orientation.
    add([1]);counts['reflection_unit']=1
    counts.update(variables=var,clauses=len(clauses),induced_paths=totalpaths,max_path_edges=maxpath)
    return var, sorted(clauses,key=lambda c:(len(c),c)),names,counts


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--outside',action='store_true');ap.add_argument('--max-edges',type=int,default=9);ap.add_argument('--stem',required=True);ap.add_argument('--r',type=int,default=4);args=ap.parse_args()
    if not 3<=args.r<=5 or not 2<=args.max_edges<=11: raise ValueError('bounded input only')
    n,es,fs=graph(args.r);var,cs,names,counts=cnf(n,es,args.outside,args.max_edges)
    stem=Path(args.stem)
    stem.with_suffix('.cnf').write_text(f'p cnf {var} {len(cs)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in cs))
    doc={'format':'opg37357-root-xr-v1','verdict':'candidate_only','r':args.r,'n':n,'edges':es,'oriented_faces':fs,'relaxation':'outside_one' if args.outside else 'ordinary_one','max_induced_path_edges':args.max_edges,'counts':counts,'variables':names}
    stem.with_suffix('.json').write_text(json.dumps(doc,indent=2)+'\n')
    print(json.dumps(counts,sort_keys=True))
if __name__=='__main__':main()
