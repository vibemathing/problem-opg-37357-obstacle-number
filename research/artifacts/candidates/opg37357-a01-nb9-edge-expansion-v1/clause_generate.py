"""NB9 explicit domain/cap extension of supplied NB8 code. See source-reuse.json.
No all-order-type enumeration claim.
"""
"""C31 all-simple-path compiler, derived from the supplied C30 generate/dimacs.
Only vertex/target caps and schema tag are generalized; no truth-table run is
claimed over the new 35 or 56 direction bits. Candidate-only.
"""
from itertools import combinations, permutations

def need(ok, message):
    if not ok:
        raise ValueError(message)

def generate(graph):
    n = graph['n']; need(type(n) is int and 3 <= n <= 9, '3<=n<=9 cap')
    edges = {tuple(e) for e in graph['edges']}
    need(len(edges) == len(graph['edges']) and all(0 <= a < b < n for a,b in edges), 'edges')
    targets = [t for t in combinations(range(n), 2) if t not in edges]
    need(len(targets) <= 15, 'at most fifteen targets in this finite interface')
    triples = list(combinations(range(n), 3)); ovars = {t: i+1 for i,t in enumerate(triples)}
    colors = {s: len(triples)+i+1 for i,s in enumerate(targets)}
    ordered = [(s,t) for s in targets for t in targets if s != t]
    sides = {pair: len(triples)+len(targets)+i+1 for i,pair in enumerate(ordered)}
    def orient(a,b,c):
        seq = (a,b,c)
        parity = sum(seq[i] > seq[j] for i,j in combinations(range(3),2))
        return ovars[tuple(sorted(seq))]*(-1 if parity % 2 else 1)
    def canonical(values):
        vals = set(values)
        return None if any(-v in vals for v in vals) else tuple(sorted(vals, key=lambda v: (abs(v),v)))
    rows = {}
    raw_attempts = 0
    def put(values, origin):
        nonlocal raw_attempts
        raw_attempts += 1
        need(raw_attempts <= 2_000_000, "raw clause budget")
        clause = canonical(values)
        if clause is not None:
            rows.setdefault(clause, origin)
            need(len(rows) <= 250_000, 'unique clause budget')
    for a,b,c,d in permutations(range(n),4):
        put([-orient(a,b,c),-orient(a,c,d),-orient(a,d,b),orient(b,c,d)], ['four',[a,b,c,d]])
    for a,b,c,d,e in permutations(range(n),5):
        pre = [-orient(a,b,c),-orient(a,c,d),-orient(a,d,e),-orient(a,b,e)]
        for mode, tail in enumerate(([orient(a,b,d),-orient(a,c,e)],[-orient(a,b,d),orient(a,c,e)])):
            put(pre+tail,['five',[a,b,c,d,e],mode])
    paths = {}
    for a,b in targets:
        others = [v for v in range(n) if v not in (a,b)]
        found = []
        for length in range(1,len(others)+1):
            for middle in permutations(others,length):
                path = (a,)+middle+(b,)
                if all(tuple(sorted(e)) in edges for e in zip(path,path[1:])):
                    found.append(path)
        need(len(found)<=14_000, 'per-target path cap')
        paths[a,b] = sorted(found)
    for ab,cd in ordered:
        a,b = ab; c,d = cd; sid = sides[ab,cd]
        for path in paths[ab]:
            key = [orient(c,d,v) for v in path if v not in cd]
            internal = [orient(a,b,v) for v in path[1:-1]]
            for mode in range(4):
                pre = key if mode < 2 else [-v for v in key]
                tail = [-sid]+internal if mode % 2 == 0 else [sid]+[-v for v in internal]
                for r in (0,1):
                    # c_s=0 encodes z_(s,0), c_s=1 encodes z_(s,1).
                    guard = [colors[ab],colors[cd]] if r == 0 else [-colors[ab],-colors[cd]]
                    put(guard+pre+tail,['key',list(ab),list(cd),list(path),mode,r])
    need(sum(len(v) for v in paths.values())<=20_000, 'all-path budget')
    clauses = sorted(rows)
    return {'schema':'nb9-h2-cnf-v1','n':n,'edges':[list(e) for e in sorted(edges)],
            'triples':[list(t) for t in triples],'targets':[list(t) for t in targets],
            'color_variables':[colors[t] for t in targets],
            'side_variables':[{'variable':sides[ab,cd],'ab':list(ab),'cd':list(cd)} for ab,cd in ordered],
            'variables':len(triples)+len(targets)+len(sides),'clauses':[list(c) for c in clauses],
            'origins':[rows[c] for c in clauses],
            'paths':[{'target':list(s),'paths':[list(p) for p in paths[s]]} for s in targets],
            'path_scope':'ALL simple paths, up to n-1 edges','verdict':'candidate_only'}


def dimacs(data):
    return ('p cnf %d %d\n' % (data['variables'],len(data['clauses']))+
            ''.join(' '.join(map(str,c))+' 0\n' for c in data['clauses'])).encode('ascii')
