"""C28 guarded h=2 CNF producer. No C22/C26 imports or external effects."""
from itertools import combinations, permutations


def layout(n, edges):
    if type(n) is not int or not 3 <= n <= 6:
        raise ValueError('producer domain 3<=n<=6')
    e = {tuple(sorted(x)) for x in edges}
    if len(e) != len(edges) or any(len(x) != 2 or x[0] == x[1] or not all(type(v) is int and 0 <= v < n for v in x) for x in e):
        raise ValueError('invalid edge set')
    triples = list(combinations(range(n), 3)); targets = [x for x in combinations(range(n), 2) if x not in e]
    o = {x: i+1 for i,x in enumerate(triples)}
    colors = {(x,r): len(o)+2*i+r+1 for i,x in enumerate(targets) for r in range(2)}
    sides = {(s,t): len(o)+2*len(targets)+i+1 for i,(s,t) in enumerate(permutations(targets,2))}
    return e, triples, targets, o, colors, sides


def make(n, edges):
    e, triples, targets, orient, colors, sides = layout(n, edges)
    def lit(t):
        inversions = sum(t[i] > t[j] for i in range(3) for j in range(i+1, 3))
        return orient[tuple(sorted(t))] * (-1 if inversions % 2 else 1)
    source = {}; families = {}
    def add(row, origin):
        terms = set(row)
        if any(-v in terms for v in terms):
            return
        key = tuple(sorted(terms, key=lambda v: (abs(v), v)))
        if key not in source or origin < source[key]:
            source[key] = origin
    for t in permutations(range(n), 4):
        a,b,c,d = t
        add([-lit((a,b,c)), -lit((a,c,d)), -lit((a,d,b)), lit((b,c,d))], ('four',t))
    for t in permutations(range(n), 5):
        a,b,c,d,f = t
        prefix = [-lit((a,b,c)), -lit((a,c,d)), -lit((a,d,f)), -lit((a,b,f))]
        for mode in range(2):
            sign = 1 if mode == 0 else -1
            add(prefix+[sign*lit((a,b,d)), -sign*lit((a,c,f))], ('five',t,mode))
    for s in targets:
        add([colors[s,0], colors[s,1]], ('color',s,0))
        add([-colors[s,0], -colors[s,1]], ('color',s,1))
    paths = {}
    for a,b in targets:
        rest = [v for v in range(n) if v not in (a,b)]
        rows = []
        for k in range(1,n-1):
            for middle in permutations(rest, k):
                path = (a,)+middle+(b,)
                if all(tuple(sorted(uv)) in e for uv in zip(path,path[1:])):
                    rows.append(path)
        paths[a,b] = sorted(rows)
    for (s,t), sid in sides.items():
        a,b = s; c,d = t
        for path in paths[s]:
            C = [lit((c,d,v)) for v in path if v not in t]
            J = [lit((a,b,v)) for v in path[1:-1]]
            for r in range(2):
                for mode in range(4):
                    key = C if mode < 2 else [-v for v in C]
                    tail = [-sid]+J if mode % 2 == 0 else [sid]+[-v for v in J]
                    add([-colors[s,r], -colors[t,r]]+key+tail, ('key',s,t,path,r,mode))
    clauses = sorted(source)
    for row in clauses:
        family = source[row][0]; families[family] = families.get(family,0)+1
    return {'n':n, 'edges':[list(x) for x in sorted(e)], 'triples':[list(x) for x in triples],
            'nonedges':[list(x) for x in targets], 'variables':len(triples)+2*len(targets)+len(sides),
            'clauses':[list(x) for x in clauses], 'origins':[source[x] for x in clauses],
            'counts':families, 'paths':[{'target':list(s),'paths':[list(p) for p in paths[s]]} for s in targets],
            'path_limit':n-1,'verdict':'candidate_only'}


def dimacs(data):
    return f"p cnf {data['variables']} {len(data['clauses'])}\n"+''.join(' '.join(map(str,c))+' 0\n' for c in data['clauses'])
