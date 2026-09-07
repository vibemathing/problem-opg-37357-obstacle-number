"""C26 supplement: exact FINITE-SEGMENT vertical decomposition.
No C21/C25 imports, support-line arrangement, floating arithmetic, or external effects.
Public interface: reconstruct(points, edges) -> finite component/incidence transcript.
"""
from fractions import Fraction as Q
from itertools import combinations
from bisect import bisect_left


def need(ok, message):
    if not ok:
        raise ValueError(message)


def rational(x):
    need(type(x) in (int, str, Q), 'exact rational input required')
    if isinstance(x, str):
        need(len(x) <= 320 and x.count('/') <= 1, 'rational size')
        need(all(t.lstrip('-').isdigit() for t in x.split('/')), 'rational syntax')
    v = Q(x)
    need(max(v.numerator.bit_length(), v.denominator.bit_length()) <= 1024, 'input bit cap')
    return v


def sub(a, b):
    return a[0]-b[0], a[1]-b[1]


def det(a, b):
    return a[0]*b[1]-a[1]*b[0]


def at(a, b, t):
    return a[0]+t*(b[0]-a[0]), a[1]+t*(b[1]-a[1])


def on(q, a, b):
    return det(sub(q, a), sub(b, a)) == 0 and all(min(a[i], b[i]) <= q[i] <= max(a[i], b[i]) for i in (0, 1))


def hits(a, b, c, d):
    u, v, w = sub(b, a), sub(d, c), sub(c, a)
    z = det(u, v)
    if z:
        t, s = det(w, v)/z, det(w, u)/z
        return [at(a, b, t)] if 0 <= t <= 1 and 0 <= s <= 1 else []
    return sorted({q for q in (a, b, c, d) if on(q, a, b) and on(q, c, d)})


def between(x, lo, hi):
    return (lo is None or lo < x) and (hi is None or x < hi)


def overlap(a, b):
    lo = [x for x in (a[0], b[0]) if x is not None]
    hi = [x for x in (a[1], b[1]) if x is not None]
    return not lo or not hi or max(lo) < min(hi)


def gap_sample(lo, hi):
    return (Q(0) if hi is None else hi-1) if lo is None else (lo+1 if hi is None else (lo+hi)/2)


def merged(rows):
    out = []
    for lo, hi in sorted(rows):
        if out and lo <= out[-1][1]:
            out[-1][1] = max(out[-1][1], hi)
        else:
            out.append([lo, hi])
    return out


class Slabs:
    def __init__(self, points, edges):
        need(type(points) is list and len(points) <= 24, 'point cap')
        need(all(type(p) in (list, tuple) and len(p) == 2 for p in points), 'point shape')
        self.p = [tuple(rational(x) for x in p) for p in points]
        need(len(set(self.p)) == len(self.p), 'injectivity')
        need(type(edges) in (list, tuple) and len(edges) <= 64, 'edge cap')
        es = []
        for pair in edges:
            need(len(pair) == 2 and all(type(x) is int and 0 <= x < len(self.p) for x in pair), 'edge index')
            need(pair[0] != pair[1], 'loop')
            es.append(tuple(sorted(pair)))
        need(len(es) == len(set(es)), 'duplicate edge')
        self.edges = sorted(es)
        segments = [(self.p[i], self.p[j]) for i, j in self.edges]
        events = {p[0] for p in self.p}
        for (a, b), (c, d) in combinations(segments, 2):
            events.update(q[0] for q in hits(a, b, c, d))
        self.xs = sorted(events)
        need(len(self.xs) <= 2200, 'event cap')
        self.slabs, self.gates, self.nodes = [], [], []
        def node():
            i = len(self.nodes); self.nodes.append(set()); return i
        ends = [None]+self.xs+[None]
        for lo, hi in zip(ends, ends[1:]):
            x = gap_sample(lo, hi)
            levels = {}
            for a, b in segments:
                if min(a[0], b[0]) < x < max(a[0], b[0]):
                    m = (b[1]-a[1])/(b[0]-a[0]); c = a[1]-m*a[0]
                    y = m*x+c
                    need(y not in levels or levels[y] == (m, c), 'missing crossing event')
                    levels[y] = (m, c)
            lines = [levels[y] for y in sorted(levels)]
            bounds = [None]+lines+[None]
            bands = [(a, b, node()) for a, b in zip(bounds, bounds[1:])]
            self.slabs.append((lo, hi, bands))
        def ev(line, x):
            return None if line is None else line[0]*x+line[1]
        for k, x in enumerate(self.xs):
            forbidden = [(p[1], p[1]) for p in self.p if p[0] == x]
            for a, b in segments:
                if a[0] == b[0] == x:
                    forbidden.append(tuple(sorted((a[1], b[1]))))
                elif a[0] != b[0] and min(a[0], b[0]) <= x <= max(a[0], b[0]):
                    y = a[1]+(x-a[0])*(b[1]-a[1])/(b[0]-a[0])
                    forbidden.append((y, y))
            closed = merged(forbidden)
            intervals, previous = [], None
            for lo, hi in closed:
                intervals.append((previous, lo)); previous = hi
            intervals.append((previous, None))
            gates = [(lo, hi, node()) for lo, hi in intervals]
            self.gates.append((x, closed, gates))
            for lo, hi, v in gates:
                for slab in (self.slabs[k], self.slabs[k+1]):
                    for lower, upper, u in slab[2]:
                        if overlap((lo, hi), (ev(lower, x), ev(upper, x))):
                            self.nodes[u].add(v); self.nodes[v].add(u)
        need(len(self.nodes) <= 200000, 'node cap')
        self.labels = [-1]*len(self.nodes); self.components = []
        for start in range(len(self.nodes)):
            if self.labels[start] >= 0:
                continue
            label = len(self.components); todo = [start]; self.labels[start] = label
            for u in todo:
                for v in sorted(self.nodes[u]):
                    if self.labels[v] < 0:
                        self.labels[v] = label; todo.append(v)
            self.components.append(sorted(todo))
        self.targets = sorted(set(combinations(range(len(self.p)), 2))-set(self.edges))
        self.incidence, self.witnesses = [], []
        for i, j in self.targets:
            a, b = self.p[i], self.p[j]; axis = 0 if a[0] != b[0] else 1
            cuts = {Q(0), Q(1)}
            if axis == 0:
                cuts.update((x-a[0])/(b[0]-a[0]) for x in self.xs if min(a[0], b[0]) < x < max(a[0], b[0]))
            for c, d in segments:
                cuts.update((q[axis]-a[axis])/(b[axis]-a[axis]) for q in hits(a, b, c, d))
            cuts.update((q[axis]-a[axis])/(b[axis]-a[axis]) for q in self.p if on(q, a, b))
            cs = sorted(cuts); visited = {}
            for lo, hi in zip(cs, cs[1:]):
                t = (lo+hi)/2; q = at(a, b, t)
                if not self.blocked(q):
                    label = self.locate(q)
                    visited.setdefault(label, (t, q))
            self.incidence.append(sorted(visited))
            self.witnesses.append(visited)
        common = set(range(len(self.components)))
        for row in self.incidence:
            common.intersection_update(row)
        self.common = sorted(common)

    def blocked(self, q):
        return q in self.p or any(on(q, self.p[i], self.p[j]) for i, j in self.edges)

    def locate(self, q):
        need(not self.blocked(q), 'point is forbidden')
        x, y = q; k = bisect_left(self.xs, x)
        if k < len(self.xs) and self.xs[k] == x:
            candidates = [(lo, hi, v) for lo, hi, v in self.gates[k][2] if between(y, lo, hi)]
        else:
            candidates = []
            for low, high, v in self.slabs[k][2]:
                lo = None if low is None else low[0]*x+low[1]
                hi = None if high is None else high[0]*x+high[1]
                if between(y, lo, hi):
                    candidates.append((lo, hi, v))
        need(len(candidates) == 1, 'nonunique free location')
        return self.labels[candidates[0][2]]

    def report(self):
        masks = sorted(sum(1 << i for i, row in enumerate(self.incidence) if c in row) for c in range(len(self.components)))
        return {'verdict': 'candidate_only', 'method': 'finite_segment_slabs',
                'event_x': [str(x) for x in self.xs], 'nodes': len(self.nodes),
                'component_count': len(self.components), 'coverage_masks': masks,
                'nonedges': [list(p) for p in self.targets], 'incidence': self.incidence,
                'common_components': self.common,
                'witnesses': [[{'component': c, 't': str(t), 'point': [str(x) for x in q]} for c, (t, q) in sorted(row.items())] for row in self.witnesses]}


def reconstruct(points, edges):
    return Slabs(points, edges).report()
