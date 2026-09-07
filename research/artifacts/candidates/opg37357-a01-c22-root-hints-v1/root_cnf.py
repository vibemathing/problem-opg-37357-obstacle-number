"""C22: deterministic X4 necessary CNF, no solver or geometry runtime.
The graph and unrestricted semantic implication are specified in README.md.
"""
from itertools import combinations, permutations


def graph():
    edges, faces = set(), []
    for i in range(4):
        a, a1, b, b1 = 2+i, 2+(i+1)%4, 6+i, 6+(i+1)%4
        edges.update(tuple(sorted(t)) for t in
                     [(0,a),(1,b),(a,a1),(b,b1),(a,b),(a1,b)])
        faces.extend([(0,a,a1),(1,b1,b),(a,b,a1),(a1,b,b1)])
    return sorted(edges), faces


def compile_cnf():
    vertices = tuple(range(10))
    triples = {t:i+1 for i,t in enumerate(combinations(vertices,3))}
    def orient(a,b,c):
        t = (a,b,c)
        inversions = sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))
        return triples[tuple(sorted(t))] * (-1 if inversions%2 else 1)
    blocks = {'four':set(), 'five':set(), 'key':set()}
    def put(block, literals):
        c = frozenset(literals)
        if not any(-lit in c for lit in c):
            blocks[block].add(tuple(sorted(c,key=lambda lit:(abs(lit),lit))))
    for a,b,c,d in permutations(vertices,4):
        put('four',[-orient(a,b,c),-orient(a,c,d),-orient(a,d,b),orient(b,c,d)])
    for a,b,c,d,e in permutations(vertices,5):
        premise = [-orient(a,b,c),-orient(a,c,d),-orient(a,d,e),-orient(a,b,e)]
        put('five',premise+[orient(a,b,d),-orient(a,c,e)])
        put('five',premise+[-orient(a,b,d),orient(a,c,e)])
    edges,faces = graph()
    missing = [t for t in combinations(vertices,2) if t not in edges]
    adjacency = {u:sorted(v if u==w else w for w,v in edges if u in (w,v)) for u in vertices}
    # Layered path extension, not the earlier recursive DFS implementation.
    paths = {}
    for a,b in missing:
        frontier, finished = [(a,)], []
        for _ in range(4):
            following = []
            for path in frontier:
                for v in adjacency[path[-1]]:
                    if v in path:
                        continue
                    extended = path+(v,)
                    if v==b:
                        finished.append(extended)
                    else:
                        following.append(extended)
            frontier = following
        paths[a,b] = finished
    side = len(triples)
    for a,b in missing:
        for c,d in missing:
            if (a,b)==(c,d):
                continue
            side += 1
            for path in paths[a,b]:
                key = [orient(c,d,v) for v in path if v not in (c,d)]
                interior = [orient(a,b,v) for v in path[1:-1]]
                for fail_key in (key,[-x for x in key]):
                    put('key',fail_key+[-side]+interior)
                    put('key',fail_key+[side]+[-x for x in interior])
    all_clauses = sorted(set().union(*blocks.values()))
    counts = {name:len(value) for name,value in blocks.items()}
    counts['paths'] = sum(map(len,paths.values()))
    if sum(counts[name] for name in blocks)!=len(all_clauses):
        raise ValueError('unexpected overlap between clause families')
    return side,all_clauses,counts


def dimacs(variables, clauses):
    return (f'p cnf {variables} {len(clauses)}\n'+''.join(
        ' '.join(map(str,c))+' 0\n' for c in clauses)).encode('ascii')
