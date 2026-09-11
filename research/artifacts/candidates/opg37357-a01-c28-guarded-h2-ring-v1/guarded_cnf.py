"""C28 finite three-module instance; no C22/C26 code or external effects.
The mathematical sources use in-memory data and stdout only.
"""
from itertools import combinations, permutations

N = 6
PAIRS = tuple(combinations(range(N), 2))
TARGETS = ((0, 1), (2, 3), (4, 5))
EDGES = tuple(p for p in PAIRS if p not in TARGETS)
MODULES = ((0, 1, 2, 3), (2, 3, 4, 5), (0, 1, 4, 5))
TRIPLES = tuple(combinations(range(N), 3))
ORDERED = tuple((s, t) for s in TARGETS for t in TARGETS if s != t)


def literal(a, b, c):
    t = (a, b, c)
    parity = sum(t[i] > t[j] for i in range(3) for j in range(i+1, 3))
    return (TRIPLES.index(tuple(sorted(t)))+1)*(-1 if parity % 2 else 1)


def z(s, r):
    return 21+2*TARGETS.index(s)+r


def side(s, t):
    return 27+ORDERED.index((s, t))


def all_paths(s):
    """Every simple path, INCLUDING five edges; internal permutations, no DFS."""
    a, b = s
    remaining = [i for i in range(N) if i not in s]
    out = []
    for k in range(1, len(remaining)+1):
        for middle in permutations(remaining, k):
            p = (a,)+middle+(b,)
            if all(tuple(sorted(e)) in EDGES for e in zip(p, p[1:])):
                out.append(p)
    return tuple(out)


def normalize(c):
    v = set(c)
    if any(-a in v for a in v):
        return None
    return tuple(sorted(v, key=lambda a: (abs(a), a)))


def raw_rows():
    for s in TARGETS:
        yield (z(s, 0), z(s, 1)), ['exact_one', list(s), 0]
        yield (-z(s, 0), -z(s, 1)), ['exact_one', list(s), 1]
    for a, b, c, d in permutations(range(N), 4):
        yield (-literal(a,b,c),-literal(a,c,d),-literal(a,d,b),literal(b,c,d)), ['four',[a,b,c,d]]
    for a, b, c, d, e in permutations(range(N), 5):
        pre = (-literal(a,b,c),-literal(a,c,d),-literal(a,d,e),-literal(a,b,e))
        u, v = literal(a,b,d), literal(a,c,e)
        for mode, tail in enumerate(((u,-v),(-u,v))):
            yield pre+tail, ['five',[a,b,c,d,e],mode]
    for s, t in ORDERED:
        a, b = s; c, d = t
        q = side(s, t)
        for path in all_paths(s):
            C = tuple(literal(c,d,v) for v in path if v not in t)
            J = tuple(literal(a,b,v) for v in path[1:-1])
            for r in (0, 1):
                guard = (-z(s,r), -z(t,r))
                for mode in range(4):
                    fail = C if mode < 2 else tuple(-v for v in C)
                    tail = (-q,)+J if mode % 2 == 0 else (q,)+tuple(-v for v in J)
                    yield guard+fail+tail, ['key',list(s),list(t),list(path),r,mode]


def build():
    import json
    origins = {}
    raw_count = 0
    for c, origin in raw_rows():
        raw_count += 1
        clause = normalize(c)
        if clause is None:
            continue
        text = json.dumps(origin,separators=(',',':'))
        if clause not in origins or text < origins[clause][0]:
            origins[clause] = text, origin
    rows = [{'id':i+1,'clause':list(c),'origin':origins[c][1]}
            for i,c in enumerate(sorted(origins))]
    return {'schema':'c28-guarded-h2-cnf-v1','verdict':'candidate_only',
            'n':N,'edges':[list(e) for e in EDGES],
            'targets':[list(e) for e in TARGETS],
            'modules':[list(v) for v in MODULES],
            'orientation_triples':[list(t) for t in TRIPLES],
            'z_variables':[[list(s),r,z(s,r)] for s in TARGETS for r in (0,1)],
            'side_variables':[[list(s),list(t),side(s,t)] for s,t in ORDERED],
            'variables':32,'raw_clause_count':raw_count,'rows':rows}


def variable_planes():
    """Bit q represents orientation assignment q, with little-endian bits."""
    total = 1 << len(TRIPLES)
    full = (1 << total)-1
    planes = []
    for j in range(len(TRIPLES)):
        half = 1 << j
        block = ((1 << half)-1) << half
        planes.append(block*(full//((1 << (2*half))-1)))
    return full, planes


def enumerate_interface(cnf):
    """Complete enumeration of 2^20 directions times eight exact-one labels.
    Each side variable is eliminated by its two incompatible forcing masks.
    No real realizability is inferred for a surviving orientation table.
    """
    full, planes = variable_planes()
    def L(v):
        return planes[v-1] if v > 0 else full ^ planes[-v-1]
    valid = full
    for row in cnf['rows']:
        if row['origin'][0] in ('four','five'):
            sat = 0
            for v in row['clause']:
                sat |= L(v)
            valid &= sat
    force = {}
    for s,t in ORDERED:
        plus = minus = 0
        for path in all_paths(s):
            C = [literal(*t,v) for v in path if v not in t]
            J = [literal(*s,v) for v in path[1:-1]]
            key_plus = key_minus = pos = neg = full
            for v in C:
                key_plus &= L(v); key_minus &= full ^ L(v)
            for v in J:
                pos &= L(v); neg &= full ^ L(v)
            plus |= (key_plus | key_minus) & pos
            minus |= (key_plus | key_minus) & neg
        force[s,t] = plus,minus
    color_results = []
    union = 0
    for coloring in range(8):
        good = valid
        for s,t in ORDERED:
            if (coloring >> TARGETS.index(s) & 1) == (coloring >> TARGETS.index(t) & 1):
                plus,minus = force[s,t]
                good &= full ^ (plus & minus)
        first = (good & -good).bit_length()-1 if good else None
        union |= good
        color_results.append({'coloring_code':coloring,'orientations':good.bit_count(),
                              'first_orientation':first})
    first = (union & -union).bit_length()-1
    first_color = next(r['coloring_code'] for r in color_results
                       if r['first_orientation'] == first)
    truth = {j+1:bool(first>>j & 1) for j in range(20)}
    for s in TARGETS:
        col = first_color >> TARGETS.index(s) & 1
        for r in (0,1):
            truth[z(s,r)] = col == r
    for s,t in ORDERED:
        same = (first_color >> TARGETS.index(s) & 1) == (first_color >> TARGETS.index(t) & 1)
        truth[side(s,t)] = same and bool(force[s,t][0] >> first & 1)
    if not all(any(truth[abs(v)] == (v>0) for v in row['clause']) for row in cnf['rows']):
        raise ValueError('constructed model fails a clause')
    return {'direction_assignments':1<<20,'label_assignments_per_direction':8,
            'direction_label_pairs':(1<<20)*8,
            'orientation_rule_survivors':valid.bit_count(),
            'by_coloring':color_results,'orientation_tables_with_h2_extension':union.bit_count(),
            'sat_direction_label_pairs':sum(x['orientations'] for x in color_results),
            'side_elimination':'all six bits eliminated exactly by incompatible forces',
            'minimum_order':'orientation integer, coloring integer, side integer; little endian',
            'minimum_orientation':first,'minimum_coloring':first_color,
            'model':[i if truth[i] else -i for i in range(1,33)],
            'realizability_of_all_survivors_checked':False}
