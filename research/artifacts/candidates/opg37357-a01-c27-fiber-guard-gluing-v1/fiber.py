"""C27 exact vertical-fiber decomposition of finite CLOSED graph segments.
Pure memory. No C20/C21/C25 source, sign-atlas input, network or process access.
Resource refusals raise ValueError; they are never mathematical negatives.
"""
from fractions import Fraction as Q
from itertools import combinations
from bisect import bisect_right


def need(ok, message):
    if not ok:
        raise ValueError(message)


def rational(v):
    need(type(v) in (int, str), 'integer/rational string only')
    if type(v) is str:
        need(len(v) <= 180 and v.count('/') <= 1, 'rational size')
        need(all(s.lstrip('-').isdigit() for s in v.split('/')), 'rational syntax')
    x = Q(v)
    need(max(x.numerator.bit_length(), x.denominator.bit_length()) <= 256, 'bit cap')
    return x


def sub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def det(u, v):
    return u[0]*v[1]-u[1]*v[0]


def turn(a, b, c):
    return det(sub(b, a), sub(c, a))


def at(a, b, t):
    return (a[0]+t*(b[0]-a[0]), a[1]+t*(b[1]-a[1]))


def on(p, a, b):
    return turn(a, b, p) == 0 and all(min(a[i], b[i]) <= p[i] <= max(a[i], b[i]) for i in (0, 1))


def hits(a, b, c, d):
    """All isolated hits, or the two ends of a collinear intersection."""
    u, v = sub(b, a), sub(d, c)
    z = det(u, v)
    if z:
        t, s = Q(det(sub(c, a), v))/z, Q(det(sub(c, a), u))/z
        return [at(a, b, t)] if 0 <= t <= 1 and 0 <= s <= 1 else []
    return sorted({p for p in (a, b, c, d) if on(p, a, b) and on(p, c, d)})


def height(a, b, x):
    need(a[0] != b[0], 'vertical height query')
    return a[1]+Q(b[1]-a[1])*(x-a[0])/(b[0]-a[0])


def mid(lo, hi):
    if lo is None:
        return Q(0) if hi is None else hi-1
    return lo+1 if hi is None else (lo+hi)/2


def inside(x, lo, hi):
    return (lo is None or lo < x) and (hi is None or x < hi)


def gaps(closed):
    merged = []
    for lo, hi in sorted(closed):
        if merged and lo <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(hi, merged[-1][1]))
        else:
            merged.append((lo, hi))
    if not merged:
        return [(None, None)]
    return [(None, merged[0][0])] + [(a[1], b[0]) for a, b in zip(merged, merged[1:])] + [(merged[-1][1], None)]


class Fiber:
    def __init__(self, raw):
        need(type(raw) is dict and set(raw) <= {'points', 'edges', 'nonedges'}, 'input keys')
        need(type(raw['points']) is list and len(raw['points']) <= 32, 'point cap')
        self.p = []
        for row in raw['points']:
            need(type(row) is list and len(row) == 2, 'point shape')
            self.p.append(tuple(rational(v) for v in row))
        need(len(set(self.p)) == len(self.p), 'noninjective points')
        need(type(raw['edges']) is list and len(raw['edges']) <= 128, 'edge cap')
        self.e = []
        for pair in raw['edges']:
            need(type(pair) is list and len(pair) == 2, 'edge shape')
            need(all(type(i) is int and 0 <= i < len(self.p) for i in pair) and pair[0] != pair[1], 'edge index')
            self.e.append(tuple(sorted(pair)))
        need(len(set(self.e)) == len(self.e), 'duplicate edge')
        self.e.sort()
        self.targets = sorted(set(combinations(range(len(self.p)), 2))-set(self.e))
        if 'nonedges' in raw:
            need(raw['nonedges'] == [list(t) for t in self.targets], 'full sorted complement required')
        self.segments = [(self.p[a], self.p[b]) for a, b in self.e]
        event = {p[0] for p in self.p}
        for ab, cd in combinations(self.segments, 2):
            event.update(q[0] for q in hits(*ab, *cd))
        self.xs = sorted(event)
        need(len(self.xs) <= 1000, 'event cap')
        self.nodes, self.slabs, self.fibers, self.links = [], [], [], []
        bounds = [None]+self.xs+[None]
        for lo, hi in zip(bounds, bounds[1:]):
            x = mid(lo, hi)
            walls = {}
            for i, (a, b) in enumerate(self.segments):
                if min(a[0], b[0]) < x < max(a[0], b[0]):
                    walls.setdefault(height(a, b, x), i)
            heights = sorted(walls)
            ids = []
            ys = [None]+heights+[None]
            for low, high in zip(ys, ys[1:]):
                ids.append(len(self.nodes)); self.nodes.append((x, mid(low, high)))
            self.slabs.append({'lo': lo, 'hi': hi, 'walls': [walls[y] for y in heights], 'nodes': ids})
        for j, x in enumerate(self.xs):
            closed = [(p[1], p[1]) for p in self.p if p[0] == x]
            for a, b in self.segments:
                if min(a[0], b[0]) <= x <= max(a[0], b[0]):
                    if a[0] == b[0]:
                        closed.append((min(a[1], b[1]), max(a[1], b[1])))
                    else:
                        y = height(a, b, x); closed.append((y, y))
            rows = []
            for lo, hi in gaps(closed):
                y = mid(lo, hi); node = len(self.nodes); self.nodes.append((x, y))
                ends = []
                for slab in (self.slabs[j], self.slabs[j+1]):
                    values = [height(*self.segments[i], x) for i in slab['walls']]
                    need(all(y != v for v in values), 'free fiber meets wall endpoint')
                    band = sum(v < y for v in values)
                    ends.append(slab['nodes'][band]); self.links.append((node, ends[-1]))
                rows.append({'lo': lo, 'hi': hi, 'node': node, 'neighbors': ends})
            self.fibers.append(rows)
        need(len(self.nodes) <= 20000, 'decomposition cap')
        neighbors = [[] for _ in self.nodes]
        for a, b in self.links:
            neighbors[a].append(b); neighbors[b].append(a)
        self.labels = [-1]*len(self.nodes); self.components = []
        for v in range(len(self.nodes)):
            if self.labels[v] >= 0:
                continue
            c = len(self.components); todo = [v]; self.labels[v] = c
            for a in todo:
                for b in neighbors[a]:
                    if self.labels[b] < 0:
                        self.labels[b] = c; todo.append(b)
            self.components.append(sorted(todo))
        self.incidence, self.intervals = {}, {}
        for target in self.targets:
            a, b = (self.p[i] for i in target); cuts = {Q(0), Q(1)}
            axis = 0 if b[0] != a[0] else 1
            if axis == 0:
                cuts.update((x-a[0])/(b[0]-a[0]) for x in self.xs if min(a[0], b[0]) < x < max(a[0], b[0]))
            for q in self.p:
                if on(q, a, b):
                    cuts.add((q[axis]-a[axis])/(b[axis]-a[axis]))
            for c, d in self.segments:
                cuts.update((q[axis]-a[axis])/(b[axis]-a[axis]) for q in hits(a, b, c, d))
            cuts = sorted(cuts); rows = []; seen = set()
            for lo, hi in zip(cuts, cuts[1:]):
                t = (lo+hi)/2; q = at(a, b, t)
                c = None if self.blocked(q) else self.component(q)
                rows.append({'lo': lo, 'hi': hi, 'parameter': t, 'point': q, 'component': c})
                if c is not None:
                    seen.add(c)
            self.incidence[target] = sorted(seen); self.intervals[target] = rows
        common = set(range(len(self.components)))
        for seen in self.incidence.values():
            common.intersection_update(seen)
        self.common = sorted(common)

    def blocked(self, p):
        return p in self.p or any(on(p, a, b) for a, b in self.segments)

    def component(self, p):
        need(not self.blocked(p), 'point belongs to closed forbidden set')
        j = bisect_right(self.xs, p[0])
        if j and p[0] == self.xs[j-1]:
            for row in self.fibers[j-1]:
                if inside(p[1], row['lo'], row['hi']):
                    return self.labels[row['node']]
            raise ValueError('unlisted free fiber')
        slab = self.slabs[j]
        values = [height(*self.segments[i], p[0]) for i in slab['walls']]
        need(p[1] not in values, 'point on active wall')
        return self.labels[slab['nodes'][sum(v < p[1] for v in values)]]

    def report(self):
        return {'schema': 'c27-vertical-fiber-v1', 'verdict': 'candidate_only',
                'critical_x': self.xs, 'slabs': self.slabs, 'fibers': self.fibers,
                'node_points': self.nodes, 'links': self.links, 'labels': self.labels,
                'components': self.components,
                'targets': [{'pair': pair, 'incidence': self.incidence[pair],
                             'intervals': self.intervals[pair]} for pair in self.targets],
                'common_components': self.common}


def jsonable(obj):
    if isinstance(obj, Q):
        return str(obj)
    if isinstance(obj, (tuple, list)):
        return [jsonable(x) for x in obj]
    if isinstance(obj, dict):
        return {k: jsonable(v) for k, v in obj.items()}
    return obj
