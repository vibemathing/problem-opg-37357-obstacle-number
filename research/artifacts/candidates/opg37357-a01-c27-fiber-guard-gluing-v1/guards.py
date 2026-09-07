"""C27: literal-origin consumer and coordinate/component guard audit.
The producer is supplied by the caller; no C21/C25 imports or external effects.
"""
from itertools import combinations, permutations
from fiber import need, turn


def origin_clause(n, edges, origin):
    """Validate one source record and reconstruct its clause without producer code."""
    trip = {t: i+1 for i, t in enumerate(combinations(range(n), 3))}
    targets = sorted(set(combinations(range(n), 2))-set(map(tuple, edges)))
    sides = [(a, b) for a in targets for b in targets if a != b]
    def lit(a, b, c):
        need(len({a, b, c}) == 3 and all(type(v) is int and 0 <= v < n for v in (a,b,c)), 'orientation origin')
        t = (a, b, c)
        # Cyclic order of the minimum distinguishes the two parities.
        j = t.index(min(t)); u = t[(j+1)%3]; v = t[(j+2)%3]
        return trip[tuple(sorted(t))]*(1 if u < v else -1)
    kind, args, mode = origin
    need(type(mode) is int, 'mode type')
    if kind in ('4', '5'):
        need(len(args) == int(kind) and len(set(args)) == len(args), 'distinct tuple')
        need(all(type(v) is int and 0 <= v < n for v in args), 'tuple index')
        if kind == '4':
            need(mode == 0, 'four mode'); a,b,c,d = args
            raw = [-lit(a,b,c), -lit(a,c,d), -lit(a,d,b), lit(b,c,d)]
        else:
            need(mode in (0,1), 'five mode'); a,b,c,d,e = args
            raw = [-lit(a,b,c),-lit(a,c,d),-lit(a,d,e),-lit(a,b,e)]
            raw += [lit(a,b,d),-lit(a,c,e)] if mode == 0 else [-lit(a,b,d),lit(a,c,e)]
    else:
        need(kind == 'K' and mode in range(4), 'key mode')
        sid, *path = args; pos = sid-len(trip)-1
        need(type(sid) is int and 0 <= pos < len(sides), 'side origin')
        (a,b),(c,d) = sides[pos]
        need(3 <= len(path) <= 5 and len(path) == len(set(path)), 'simple retained path')
        need(path[0] == a and path[-1] == b, 'path endpoints')
        need(all(tuple(sorted((u,v))) in edges for u,v in zip(path,path[1:])), 'path uses a nonedge')
        raw = [(1 if mode < 2 else -1)*lit(c,d,v) for v in path if v not in (c,d)]
        raw += [-sid]+[lit(a,b,v) for v in path[1:-1]] if mode%2 == 0 else [sid]+[-lit(a,b,v) for v in path[1:-1]]
    need(not set(raw).intersection(-x for x in raw), 'tautological retained origin')
    return tuple(sorted(set(raw), key=lambda z:(abs(z),z)))


def paths(n, edges, ab):
    a,b = ab; edge = set(edges); out = []
    pool = [v for v in range(n) if v not in ab]
    for length in range(1,4):
        for middle in permutations(pool,length):
            path = (a,)+middle+(b,)
            if all(tuple(sorted((u,v))) in edge for u,v in zip(path,path[1:])):
                out.append(path)
    return out


def coordinate_audit(model, bridge, clauses, rows):
    """Every key row is guarded by actual common free-component incidence.
    A failed unguarded row at a bad drawing is not a failed implication.
    """
    n = len(model.p)
    need(n == bridge.n and model.e == bridge.edges, 'producer input identity')
    triples = list(combinations(range(n),3))
    values = {t:turn(*(model.p[v] for v in t)) for t in triples}
    need(all(v != 0 for v in values.values()), 'GP required for Boolean projection')
    bits = {i+1: values[t] > 0 for i,t in enumerate(triples)}
    def positive(a,b,c):
        return turn(model.p[a],model.p[b],model.p[c]) > 0
    pathmap = {ab:paths(n,model.e,ab) for ab in model.targets}
    forcing, conflicts, active = {}, [], {}
    for sid, (ab,cd) in bridge.sides.items():
        a,b = ab; c,d = cd; force = {}
        for path in pathmap[ab]:
            key = [positive(c,d,v) for v in path if v not in cd]
            interior = [positive(a,b,v) for v in path[1:-1]]
            if len(set(key)) == 1 and len(set(interior)) == 1:
                force.setdefault(interior[0],path)
        common = sorted(set(model.incidence[ab]) & set(model.incidence[cd]))
        active[sid] = bool(common)
        need(not common or len(force) < 2, 'geometry/key-path implication failed')
        if len(force) == 2:
            conflicts.append({'side':sid, 'ab':ab, 'cd':cd,
                              'positive':force[True], 'negative':force[False],
                              'ab_components':model.incidence[ab], 'cd_components':model.incidence[cd]})
        bits[sid] = True in force; forcing[sid] = force
    counts = {'4':0,'5':0,'K':0}; activated=0; inactive_false=0; first_false=None
    for (row, origin), clause in zip(rows,clauses):
        kind, args, mode = origin; counts[kind] += 1
        enabled = kind != 'K' or active[args[0]]
        value = any(bits[abs(x)] == (x > 0) for x in clause)
        need(not enabled or value, 'active necessary clause fails')
        activated += enabled; inactive_false += not enabled and not value
        if not enabled and not value and first_false is None:
            first_false={'row':row,'clause':clause,'origin':origin,
                         'ab':bridge.sides[args[0]][0],'cd':bridge.sides[args[0]][1],
                         'literal_values':[[x,bits[abs(x)] == (x>0)] for x in clause]}
    return {'row_counts':counts, 'active_rows_checked':activated,
            'inactive_unguarded_false_rows':inactive_false, 'first_inactive_false':first_false,
            'common_components':model.common, 'components':len(model.components),
            'conflict_count':len(conflicts), 'first_conflict':conflicts[0] if conflicts else None,
            'retained_paths':sum(map(len,pathmap.values()))}
