"""C25: coordinates-free local-face decoder, CONDITIONAL on realizability.
No C20/C21 imports, network, files, processes, dynamic evaluation or floats.
"""
from itertools import combinations
from functools import cmp_to_key, lru_cache


def require(ok, message):
    if not ok:
        raise ValueError(message)


def indexes(n):
    return list(combinations(range(n), 2))


def local_orders(s):
    require(type(s) is dict and set(s) == {'schema', 'n', 'b', 'w', 'd'}, 'signature keys')
    require(s['schema'] == 'c25-quartic-signature-v1', 'signature version')
    n = s['n']; require(type(n) is int and 3 <= n <= 8, 'domain: 3<=n<=8')
    pairs = indexes(n); m = len(pairs)
    wp = indexes(m); dt = list(combinations(range(m), 3))
    for field, count, allowed in [('b', m, (-1, 1)), ('w', len(wp), (-1, 1)),
                                   ('d', len(dt), (-1, 0, 1))]:
        require(type(s[field]) is list and len(s[field]) == count, 'sign array length')
        require(all(type(v) is int and v in allowed for v in s[field]), 'sign type/value')
    w = dict(zip(wp, s['w'])); d = dict(zip(dt, s['d'])); b = s['b']

    def W(i, j):
        return w[i, j] if i < j else -w[j, i]

    def D(i, j, k):
        ids = (i, j, k)
        parity = sum(ids[a] > ids[c] for a, c in indexes(3))
        return (-1 if parity % 2 else 1)*d[tuple(sorted(ids))]

    groups, ranks = [], []
    for a in range(m):
        def compare(i, j):
            return 0 if i == j else -b[a]*D(a, i, j)*W(a, i)*W(a, j)
        others = sorted((i for i in range(m) if i != a), key=cmp_to_key(compare))
        blocks = []
        for i in others:
            if blocks and compare(blocks[-1][0], i) == 0:
                blocks[-1].append(i)
            else:
                blocks.append([i])
        rank = {i: r for r, block in enumerate(blocks) for i in block}
        for i, j in combinations(others, 2):
            require(compare(i, j) == ((rank[i] > rank[j]) - (rank[i] < rank[j])),
                    'local intersection comparisons not a total preorder')
        groups.append([sorted(block) for block in blocks]); ranks.append(rank)
    # A concurrence seen on one line must be the same complete block on all its lines.
    for a, blocks in enumerate(groups):
        for block in blocks:
            event = set(block) | {a}
            for j in block:
                require(set(groups[j][ranks[j][a]]) | {j} == event, 'concurrence inconsistency')
    endpoints = []
    pair_id = {p: i for i, p in enumerate(pairs)}
    for a, (i, j) in enumerate(pairs):
        ends = []
        for v in (i, j):
            incident = [pair_id[tuple(sorted((v, u)))] for u in range(n) if u != v and u not in (i, j)]
            r = ranks[a][incident[0]]
            require(all(ranks[a][x] == r for x in incident), 'vertex concurrence missing')
            actual = set(groups[a][r]) | {a}
            expected = {pair_id[tuple(sorted((v, u)))] for u in range(n) if u != v}
            require(actual == expected, 'nonincident line through graph vertex')
            ends.append(r)
        require(ends[0] != ends[1], 'identified endpoints')
        require((ends[1] > ends[0]) - (ends[1] < ends[0]) == b[a], 'endpoint x order')
        endpoints.append(ends)
    return pairs, groups, ranks, endpoints, W


def minimum_cover(incidence, component_count):
    if not incidence:
        return 0, []
    if any(not row for row in incidence):
        return None, []  # Infinity at a realized drawing; never a resource refusal.
    masks = [sum(1 << i for i, row in enumerate(incidence) if c in row)
             for c in range(component_count)]
    calls = 0
    @lru_cache(None)
    def visit(left):
        nonlocal calls
        calls += 1
        require(calls <= 100000, 'cover state cap: resource refusal')
        if not left:
            return ()
        bit = (left & -left).bit_length()-1
        options = [(c,) + visit(left & ~masks[c]) for c in incidence[bit]]
        return min(options, key=lambda v: (len(v), v))
    cover = visit((1 << len(incidence))-1)
    return len(cover), list(cover)


def decode(s, edges):
    pairs, groups, ranks, endpoints, W = local_orders(s)
    n, m = s['n'], len(pairs)
    require(type(edges) is list and len(edges) <= m, 'edge list')
    canonical = []
    for row in edges:
        require(type(row) is list and len(row) == 2, 'edge shape')
        require(all(type(i) is int and 0 <= i < n for i in row) and row[0] != row[1], 'edge index')
        canonical.append(tuple(sorted(row)))
    require(len(set(canonical)) == len(canonical), 'duplicate edge')
    edge_set = set(canonical)
    provisional, sign_cells = [], set()
    for a, blocks in enumerate(groups):
        lo, hi = sorted(endpoints[a])
        for r in range(len(blocks)+1):
            signs = [0 if j == a else -W(a, j)*s['b'][a]*(1 if r > ranks[a][j] else -1)
                     for j in range(m)]
            sides = []
            for v in (-1, 1):
                signs[a] = v; sides.append(tuple(signs)); sign_cells.add(tuple(signs))
            blocked = pairs[a] in edge_set and lo < r <= hi
            provisional.append((a, r, sides, blocked))
    cells = sorted(sign_cells); cell_id = {v: i for i, v in enumerate(cells)}
    require(len(cells) <= 1+m*(m+1)//2, 'too many cells for line arrangement')
    neighbors = [set() for _ in cells]; faces = []
    for a, r, sides, blocked in provisional:
        u, v = [cell_id[x] for x in sides]
        faces.append({'line': a, 'interval': r, 'cells': [u, v], 'blocked': blocked})
        if not blocked:
            neighbors[u].add(v); neighbors[v].add(u)
    labels = [-1]*len(cells); components = []
    for start in range(len(cells)):
        if labels[start] >= 0:
            continue
        c = len(components); todo = [start]; labels[start] = c
        for u in todo:
            for v in sorted(neighbors[u]):
                if labels[v] < 0:
                    labels[v] = c; todo.append(v)
        components.append(sorted(todo))
    incidence, targets = [], []
    for a, pair in enumerate(pairs):
        if pair in edge_set:
            continue
        lo, hi = sorted(endpoints[a]); visited = set()
        for face in faces:
            if face['line'] == a and lo < face['interval'] <= hi:
                require(not face['blocked'], 'open nonedge face unexpectedly forbidden')
                u, v = face['cells']; require(labels[u] == labels[v], 'free face splits labels')
                visited.add(labels[u])
        targets.append(list(pair)); incidence.append(sorted(visited))
    tau, cover = minimum_cover(incidence, len(components))
    return {'domain': 'Dstar_signature_conditional_on_realizability', 'realizability_checked': False,
            'pairs': [list(p) for p in pairs], 'groups': groups, 'endpoint_ranks': endpoints,
            'cells': [list(c) for c in cells], 'faces': faces, 'components': components,
            'labels': labels, 'nonedges': targets, 'incidence': incidence,
            'conditional_tau': tau, 'cover': cover, 'verdict': 'candidate_only'}
