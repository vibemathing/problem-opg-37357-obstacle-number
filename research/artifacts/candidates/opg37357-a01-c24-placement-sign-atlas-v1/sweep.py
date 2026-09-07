"""Decode an assumed-realizable C24 signature, without point coordinates.
Acceptance is NOT a realizability certificate. Bounds: n<=6, finite cover work.
"""
from functools import cmp_to_key, lru_cache
from itertools import combinations
from signature import event_comparators


def groups(order, cmp):
    out = []
    for x in order:
        if not out or cmp(out[-1][0], x) != 0:
            out.append([x])
        else:
            out[-1].append(x)
    if any(cmp(a, b) > 0 for i, a in enumerate(order) for b in order[i+1:]):
        raise ValueError('inconsistent total comparison')
    if any(cmp(a, b) != 0 for g in out for a in g for b in g):
        raise ValueError('inconsistent equality group')
    return out


def arrangement(s):
    pairs, epairs, cx, cy = event_comparators(s)
    m, r = len(pairs), len(epairs)
    ei = {uv: i for i, uv in enumerate(epairs)}
    pi = {uv: i for i, uv in enumerate(pairs)}
    b = s['b']
    def slope_order(a, c):
        if a == c:
            return 0
        lo, hi = sorted((a, c))
        v = s['w'][ei[lo, hi]] * b[lo] * b[hi]
        return v if a == lo else -v
    order = sorted(range(m), key=cmp_to_key(slope_order))
    if any(slope_order(a, c) >= 0 for j, a in enumerate(order) for c in order[j+1:]):
        raise ValueError('inconsistent slope order')
    batches = groups(sorted(range(r), key=cmp_to_key(cx)), cx)
    orders, event_batch = [order[:]], {}
    for g, batch in enumerate(batches):
        for e in batch:
            event_batch[e] = g
        point_groups = groups(sorted(batch, key=cmp_to_key(cy)), cy)
        blocks = []
        for point_group in point_groups:
            lines = sorted({a for e in point_group for a in epairs[e]})
            expected = {ei[tuple(sorted(ac))] for ac in combinations(lines, 2)}
            if expected != set(point_group):
                raise ValueError('incomplete concurrency group')
            positions = sorted(order.index(a) for a in lines)
            if positions != list(range(positions[0], positions[-1]+1)):
                raise ValueError('noncontiguous event block')
            blocks.append(positions)
        if any(set(a) & set(c) for a, c in combinations(blocks, 2)):
            raise ValueError('overlapping event blocks')
        for pos in blocks:
            lo, hi = pos[0], pos[-1]+1
            order[lo:hi] = reversed(order[lo:hi])
        orders.append(order[:])
    bands, all_cells = [], set()
    for order in orders:
        v = [-x for x in b]
        row = [tuple(v)]
        for a in order:
            v[a] = b[a]
            row.append(tuple(v))
        bands.append(row)
        all_cells.update(row)
    cells = sorted(all_cells)
    ci = {v: i for i, v in enumerate(cells)}
    faces, segment_faces = [], []
    for a, (i, j) in enumerate(pairs):
        cuts = sorted({event_batch[e] for e, ac in enumerate(epairs) if a in ac})
        endpoint_batches = []
        for v in (i, j):
            third = next(z for z in range(s['n']) if z not in (i, j))
            other = pi[tuple(sorted((v, third)))]
            endpoint_batches.append(event_batch[ei[tuple(sorted((a, other)))]])
        lo_end, hi_end = sorted(endpoint_batches)
        if lo_end == hi_end:
            raise ValueError('collapsed edge endpoints')
        indices = []
        ext = [-1] + cuts + [len(batches)]
        for lo, hi in zip(ext, ext[1:]):
            strip = lo+1
            rank = orders[strip].index(a)
            pair_cells = [ci[bands[strip][rank]], ci[bands[strip][rank+1]]]
            f = len(faces)
            faces.append({'line': a, 'lo_batch': lo, 'hi_batch': hi, 'cells': pair_cells})
            if lo >= lo_end and hi <= hi_end:
                indices.append(f)
        if not indices:
            raise ValueError('missing segment interior')
        segment_faces.append(indices)
    return {'pairs': pairs, 'cells': cells, 'faces': faces, 'segment_faces': segment_faces,
            'event_batches': len(batches), 'orders': orders}


def graph_cover(a, edges):
    pairs = a['pairs']
    pi = {uv: i for i, uv in enumerate(pairs)}
    n = max(max(p) for p in pairs)+1
    if type(edges) not in (list, tuple) or len(edges) > len(pairs):
        raise ValueError('edge list')
    chosen = set()
    for uv in edges:
        if type(uv) not in (list, tuple) or len(uv) != 2 or any(type(v) is not int or not 0 <= v < n for v in uv):
            raise ValueError('edge')
        t = tuple(sorted(uv))
        if t not in pi or pi[t] in chosen:
            raise ValueError('loop or duplicate edge')
        chosen.add(pi[t])
    blocked = {f for line in chosen for f in a['segment_faces'][line]}
    parent = list(range(len(a['cells'])))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for i, f in enumerate(a['faces']):
        if i not in blocked:
            u, v = sorted((find(f['cells'][0]), find(f['cells'][1])))
            parent[v] = u
    roots = sorted({find(x) for x in parent})
    labels = {u: i for i, u in enumerate(roots)}
    components = [labels[find(x)] for x in parent]
    nonedges = []
    for line, pair in enumerate(pairs):
        if line not in chosen:
            hit = sorted({components[a['faces'][f]['cells'][0]] for f in a['segment_faces'][line]})
            nonedges.append({'pair': pair, 'components': hit})
    k = len(nonedges)
    masks = [sum(1 << i for i, x in enumerate(nonedges) if c in x['components']) for c in range(len(roots))]
    work = [0]
    @lru_cache(None)
    def solve(rest):
        work[0] += 1
        if work[0] > 100000:
            raise ValueError('cover resource refusal')
        if not rest:
            return ()
        bit = rest & -rest
        choices = [(c, mask) for c, mask in enumerate(masks) if mask & bit]
        if not choices:
            raise ValueError('inconsistent empty incidence on D*')
        return min(((c,) + solve(rest & ~mask) for c, mask in choices), key=lambda v: (len(v), v))
    cover = solve((1 << k)-1)
    return {'component_count': len(roots), 'cell_components': components, 'nonedges': nonedges,
            'minimum_cover': len(cover), 'cover_labels': sorted(cover), 'cover_states': work[0]}
