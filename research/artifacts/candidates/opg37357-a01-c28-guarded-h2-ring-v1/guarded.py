"""C28: two-label necessary CNF. Fresh finite generator; no prior compiler import.
Pure memory. n<=6; all simple paths (not only paths up to four edges).
"""
from itertools import combinations, permutations


def require(ok, message):
    if not ok:
        raise ValueError(message)


def graph_input(n, edges):
    require(type(n) is int and 3 <= n <= 6, 'n in 3..6')
    require(type(edges) in (list, tuple) and len(edges) <= n*(n-1)//2, 'edge census')
    out = []
    for e in edges:
        require(type(e) in (list, tuple) and len(e) == 2, 'edge shape')
        require(all(type(v) is int and 0 <= v < n for v in e) and e[0] != e[1], 'edge indices')
        out.append(tuple(sorted(e)))
    require(len(set(out)) == len(out), 'duplicate edge')
    return sorted(out)


def tidy(row):
    r = set(row)
    return None if any(-x in r for x in r) else tuple(sorted(r, key=lambda x:(abs(x), x)))


class Encoding:
    def __init__(self, n, edges):
        self.n = n
        self.edges = graph_input(n, edges)
        self.triples = list(combinations(range(n), 3))
        self.orient = {t:i+1 for i,t in enumerate(self.triples)}
        self.targets = sorted(set(combinations(range(n), 2))-set(self.edges))
        require(len(self.targets) <= 8, 'target cap')
        self.z = {s:len(self.triples)+i+1 for i,s in enumerate(self.targets)}
        self.pairs = [(a,b) for a in self.targets for b in self.targets if a!=b]
        self.side = {p:len(self.triples)+len(self.targets)+i+1 for i,p in enumerate(self.pairs)}
        self.nvars = len(self.triples)+len(self.targets)+len(self.pairs)
        self.paths = {}
        for a,b in self.targets:
            pool = [v for v in range(n) if v not in (a,b)]
            self.paths[a,b] = []
            for r in range(1, n-1):
                for middle in permutations(pool, r):
                    path = (a,)+middle+(b,)
                    if all(tuple(sorted(e)) in self.edges for e in zip(path, path[1:])):
                        self.paths[a,b].append(path)
            self.paths[a,b].sort()
        self.clauses, self.origins = self.compile()

    def lit(self,a,b,c):
        require(len({a,b,c})==3 and all(type(v) is int and 0<=v<self.n for v in (a,b,c)), 'direction indices')
        t=(a,b,c)
        inversions=(a>b)+(a>c)+(b>c)
        return (-1 if inversions%2 else 1)*self.orient[tuple(sorted(t))]

    def compile(self):
        saved={}
        def add(raw, origin):
            c=tidy(raw)
            if c is not None:
                saved.setdefault(c, origin)
        o=self.lit
        for a,b,c,d in permutations(range(self.n),4):
            add([-o(a,b,c),-o(a,c,d),-o(a,d,b),o(b,c,d)], ['four',[a,b,c,d]])
        for a,b,c,d,e in permutations(range(self.n),5):
            pre=[-o(a,b,c),-o(a,c,d),-o(a,d,e),-o(a,b,e)]
            for mode in (0,1):
                tail=[o(a,b,d),-o(a,c,e)]
                if mode: tail=[-x for x in tail]
                add(pre+tail, ['five',[a,b,c,d,e],mode])
        for s,t in self.pairs:
            a,b=s;c,d=t;q=self.side[s,t]
            for path in self.paths[s]:
                key=[o(c,d,v) for v in path if v not in t]
                internal=[o(a,b,v) for v in path[1:-1]]
                for key_neg in (0,1):
                    pre=[(-1 if key_neg else 1)*x for x in key]
                    for side_neg in (0,1):
                        tail=([-q]+internal) if side_neg==0 else ([q]+[-x for x in internal])
                        for color in (0,1):
                            guard=[self.z[s],self.z[t]] if color==0 else [-self.z[s],-self.z[t]]
                            add(guard+pre+tail, ['key',list(s),list(t),list(path),key_neg,side_neg,color])
        cs=sorted(saved)
        return cs,[saved[c] for c in cs]

    def dimacs(self):
        return (f'p cnf {self.nvars} {len(self.clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in self.clauses)).encode('ascii')

    def source_tsv(self):
        rows=['row\tfamily\ttuple_or_s\tt\tpath\tkey_neg\tside_neg\tcolor\n']
        for i,r in enumerate(self.origins,1):
            if r[0]=='key':
                fields=[str(i),r[0],','.join(map(str,r[1])),','.join(map(str,r[2])),','.join(map(str,r[3]))]+list(map(str,r[4:]))
            else:
                fields=[str(i),r[0],','.join(map(str,r[1])),'-','-','-',str(r[2]) if len(r)>2 else '-','-']
            rows.append('\t'.join(fields)+'\n')
        return ''.join(rows).encode('ascii')


def bits(value, width):
    return [(value>>(width-1-i))&1 for i in range(width)]


def value(row, assignment):
    return any(assignment[abs(x)-1] == (x>0) for x in row)


def extend(enc, orientation, colors):
    """Exact existential side elimination at a fixed Boolean direction table."""
    theta=bits(orientation,len(enc.triples)); zs=bits(colors,len(enc.targets))
    assignment=theta+zs
    def pos(a,b,c):
        q=enc.lit(a,b,c)
        return bool(theta[abs(q)-1]) == (q>0)
    for s,t in enc.pairs:
        forces=set()
        if zs[enc.targets.index(s)]==zs[enc.targets.index(t)]:
            a,b=s;c,d=t
            for path in enc.paths[s]:
                key={pos(c,d,v) for v in path if v not in t}
                inter={pos(a,b,v) for v in path[1:-1]}
                if len(key)==len(inter)==1:
                    forces.update(inter)
        if len(forces)==2:
            return None
        assignment.append(int(True in forces))
    return assignment
