"""C28: fresh six-vertex guarded CNF with complete path-permutation origins.
No imports from C22/C26 or any prior geometry implementation. Memory-only.
"""
from itertools import combinations, permutations


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(row):
    s = set(row)
    return None if any(-v in s for v in s) else tuple(sorted(s, key=lambda v: (abs(v), v)))


def graph(connector_mask=7):
    require(type(connector_mask) is int and 0 <= connector_mask < 8, 'connector mask')
    modules = [[0, 1, 2, 4], [2, 3, 0, 4], [4, 5, 0, 2]]
    targets = {(0, 1), (2, 3), (4, 5)}
    base = set()
    for vertices in modules:
        base.update(p for p in combinations(sorted(vertices), 2) if p not in targets)
    connectors = [(1, 3), (1, 5), (3, 5)]
    base.update(e for i, e in enumerate(connectors) if connector_mask >> i & 1)
    return sorted(base)


def build(edges):
    require(type(edges) is list and len(edges) <= 15, 'edge cap')
    es = [tuple(sorted(e)) for e in edges]
    require(all(len(e) == 2 and all(type(v) is int and 0 <= v < 6 for v in e)
                and e[0] < e[1] for e in es), 'edge syntax')
    require(len(set(es)) == len(es), 'duplicate edge')
    es = sorted(es)
    triples = list(combinations(range(6), 3))
    ids = {t: i+1 for i, t in enumerate(triples)}
    targets = [e for e in combinations(range(6), 2) if e not in es]
    require(len(targets) <= 6, 'this exhaustive release caps targets at six')
    z = [[21+2*i, 22+2*i] for i in range(len(targets))]
    pair_order = [(i, j) for i in range(len(targets)) for j in range(len(targets)) if i != j]
    sid = {q: 21+2*len(targets)+i for i, q in enumerate(pair_order)}
    def o(a, b, c):
        inversions = (a > b)+(a > c)+(b > c)
        return ids[tuple(sorted((a, b, c)))] * (-1 if inversions % 2 else 1)
    clauses = {}
    def add(lits, origin):
        c = canonical(lits)
        if c is not None:
            clauses.setdefault(c, origin)
    for t in permutations(range(6), 4):
        a, b, c, d = t
        add([-o(a,b,c), -o(a,c,d), -o(a,d,b), o(b,c,d)], {'family':'four','tuple':list(t)})
    for t in permutations(range(6), 5):
        a,b,c,d,e = t
        prefix = [-o(a,b,c), -o(a,c,d), -o(a,d,e), -o(a,b,e)]
        for flip in range(2):
            tail = [o(a,b,d), -o(a,c,e)]
            add(prefix+[v*(-1 if flip else 1) for v in tail],
                {'family':'five','tuple':list(t),'flip':flip})
    for i in range(len(targets)):
        add(z[i], {'family':'one','target':i,'positive':True})
        add([-v for v in z[i]], {'family':'one','target':i,'positive':False})
    paths = []
    for a,b in targets:
        available = [i for i in range(6) if i not in (a,b)]
        row = []
        # Enumerate ALL possible internal-vertex permutations: no DFS/frontier reuse.
        for length in range(1,5):
            for internal in permutations(available, length):
                path = (a,)+internal+(b,)
                if all(tuple(sorted(e)) in es for e in zip(path,path[1:])):
                    row.append(path)
        paths.append(sorted(row))
    for i,j in pair_order:
        a,b = targets[i]; c,d = targets[j]
        for path in paths[i]:
            side = sid[i,j]
            ctest = [o(c,d,v) for v in path if v not in (c,d)]
            jtest = [o(a,b,v) for v in path[1:-1]]
            for color in range(2):
                for mode in range(4):
                    prefix = ctest if mode < 2 else [-v for v in ctest]
                    tail = [-side]+jtest if mode % 2 == 0 else [side]+[-v for v in jtest]
                    add([-z[i][color], -z[j][color]]+prefix+tail,
                        {'family':'key','targets':[i,j],'nonedges':[list(targets[i]),list(targets[j])],
                         'path':list(path),'color':color,'mode':mode,'side':side})
    ordered = sorted(clauses)
    return {'schema':'c28-guarded-cnf-v1','verdict':'candidate_only','n':6,
            'edges':[list(e) for e in es], 'nonedges':[list(e) for e in targets],
            'orientation_triples':[list(t) for t in triples], 'z':z,
            'side_pairs':[{'variable':sid[q], 'target_indices':list(q)} for q in pair_order],
            'variables':20+2*len(targets)+len(pair_order),
            'path_census':[[list(p) for p in row] for row in paths],
            'clauses':[list(c) for c in ordered],
            'origins':[{'row':i+1, **clauses[c]} for i,c in enumerate(ordered)]}


def dimacs(data):
    return (f"p cnf {data['variables']} {len(data['clauses'])}\n"+
            ''.join(' '.join(map(str,c))+' 0\n' for c in data['clauses'])).encode('ascii')
