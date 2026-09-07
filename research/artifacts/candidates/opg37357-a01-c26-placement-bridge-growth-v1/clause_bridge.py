"""C26: row-attributed necessary CNF; exact, finite, memory-only mathematics.
No network, process creation, file access, dynamic execution or C22 compiler import.
"""
from itertools import combinations, permutations

X4 = ((0,2),(0,3),(0,4),(0,5),(1,6),(1,7),(1,8),(1,9),
      (2,3),(2,5),(2,6),(2,9),(3,4),(3,6),(3,7),(4,5),
      (4,7),(4,8),(5,8),(5,9),(6,7),(6,9),(7,8),(8,9))


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(literals):
    values = set(literals)
    if any(-x in values for x in values):
        return None
    return tuple(sorted(values, key=lambda x: (abs(x), x)))


class Bridge:
    def __init__(self, n, edges, max_edges=4):
        require(type(n) is int and 3 <= n <= 10, 'n cap')
        require(type(max_edges) is int and 2 <= max_edges <= 4, 'path cap')
        require(len(edges) <= n*(n-1)//2, 'edge cap')
        for pair in edges:
            require(len(pair) == 2 and all(type(v) is int and 0 <= v < n for v in pair), 'edge type')
            require(pair[0] != pair[1], 'loop')
        self.n = n
        self.edges = sorted(tuple(sorted(pair)) for pair in edges)
        require(len(set(self.edges)) == len(self.edges), 'duplicate edge')
        self.triples = list(combinations(range(n), 3))
        self.variables = {t: i+1 for i,t in enumerate(self.triples)}
        self.targets = [p for p in combinations(range(n),2) if p not in self.edges]
        neighbors = [sorted(b if a == v else a for a,b in self.edges if v in (a,b)) for v in range(n)]
        self.paths = {}
        # DFS rather than the C22 layered frontier. Depth decreases at each step.
        for a,b in self.targets:
            finished = []
            def walk(path):
                if len(path)-1 == max_edges:
                    return
                for v in neighbors[path[-1]]:
                    if v in path:
                        continue
                    new = path+(v,)
                    if v == b:
                        finished.append(new)
                    else:
                        walk(new)
            walk((a,))
            self.paths[a,b] = sorted(finished)
        ordered = [(u,v) for u in self.targets for v in self.targets if u != v]
        self.sides = {len(self.triples)+i+1: uv for i,uv in enumerate(ordered)}
        self.size = len(self.triples)+len(self.sides)

    def literal(self, triple):
        inversions = sum(triple[i] > triple[j] for i,j in combinations(range(3),2))
        return (-1 if inversions % 2 else 1)*self.variables[tuple(sorted(triple))]

    def raw_clause(self, origin):
        kind, args, mode = origin
        o = lambda a,b,c: self.literal((a,b,c))
        if kind == '4':
            a,b,c,d = args
            return [-o(a,b,c),-o(a,c,d),-o(a,d,b),o(b,c,d)]
        if kind == '5':
            a,b,c,d,e = args
            prefix = [-o(a,b,c),-o(a,c,d),-o(a,d,e),-o(a,b,e)]
            tail = [o(a,b,d),-o(a,c,e)]
            return prefix + (tail if mode == 0 else [-v for v in tail])
        require(kind == 'K' and mode in range(4), 'origin type')
        sid, *path = args
        (a,b),(c,d) = self.sides[sid]
        require(tuple(path) in self.paths[a,b], 'path origin not in census')
        key = [o(c,d,v) for v in path if v not in (c,d)]
        interior = [o(a,b,v) for v in path[1:-1]]
        if mode // 2:
            key = [-v for v in key]
        return key + ([-sid]+interior if mode % 2 == 0 else [sid]+[-v for v in interior])

    def compile(self):
        attributed = {}
        def put(origin):
            clause = canonical(self.raw_clause(origin))
            if clause is not None and (clause not in attributed or origin < attributed[clause]):
                attributed[clause] = origin
        for args in permutations(range(self.n),4):
            put(('4',args,0))
        for args in permutations(range(self.n),5):
            for mode in (0,1):
                put(('5',args,mode))
        for sid,(ab,cd) in self.sides.items():
            for path in self.paths[ab]:
                for mode in range(4):
                    put(('K',(sid,)+path,mode))
        clauses = sorted(attributed)
        rows = [(i+1,attributed[c]) for i,c in enumerate(clauses)]
        return clauses, rows


def determinant(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def project(points, bridge):
    """GP real/rational data -> all orientation bits and truncated key-path sides.
    A returned conflict is one FIXED-drawing local separation witness, not an
    all-placement theorem. For a one-obstacle realization the proof excludes it.
    """
    require(len(points) == bridge.n, 'point census')
    values = {t: determinant(*(points[i] for i in t)) for t in bridge.triples}
    require(all(values.values()), 'GP projection does not encode zero orientation')
    assignment = {bridge.variables[t]: v > 0 for t,v in values.items()}
    def sign(a,b,c):
        return determinant(points[a],points[b],points[c]) > 0
    conflicts = []
    for sid,((a,b),(c,d)) in bridge.sides.items():
        forcing = {}
        for path in bridge.paths[a,b]:
            key = [sign(c,d,v) for v in path if v not in (c,d)]
            require(bool(key), 'empty key list')
            if len(set(key)) != 1:
                continue
            interior = [sign(a,b,v) for v in path[1:-1]]
            require(bool(interior), 'nonedge path cannot be direct edge')
            if len(set(interior)) == 1:
                forcing.setdefault(interior[0],path)
        if len(forcing) == 2:
            conflicts.append({'side':sid,'ab':list((a,b)),'cd':list((c,d)),
                              'positive_path':list(forcing[True]),'negative_path':list(forcing[False])})
        assignment[sid] = True in forcing
    return assignment, conflicts


def satisfied(clause, assignment):
    return any(assignment[abs(lit)] == (lit > 0) for lit in clause)


def dimacs(nvars, clauses):
    return (f'p cnf {nvars} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in clauses)).encode('ascii')


def origin_text(rows):
    return ''.join(f'{i}\t{k}\t'+','.join(map(str,args))+f'\t{mode}\n'
                   for i,(k,args,mode) in rows).encode('ascii')
