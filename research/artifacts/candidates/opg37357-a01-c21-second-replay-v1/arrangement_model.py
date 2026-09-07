"""C21 second model: strict sign feasibility, not C20 face-side sampling.
Pure in-memory rational arithmetic; bounded by 16 points and 10 lines.
"""
from fractions import Fraction as F
from itertools import combinations
from exact_primitives import (require, point, primitive_line, value, line_frame,
    parameter, interpolate, subtract, on_segment, blocked)
from strict_cells import all_cells


def pairs(rows, n):
    require(type(rows) is list and len(rows) <= n*(n-1)//2, 'pair list cap')
    out = []
    for row in rows:
        require(type(row) is list and len(row) == 2, 'pair shape')
        require(all(type(x) is int and 0 <= x < n for x in row), 'pair index')
        a,b = sorted(row)
        require(a != b, 'loop')
        out.append((a,b))
    require(len(set(out)) == len(out), 'duplicate pair')
    return sorted(out)


def open_interval(t, lo, hi):
    return (lo is None or lo < t) and (hi is None or t < hi)


def intervals(cuts):
    ends = [None]+list(cuts)+[None]
    return list(zip(ends, ends[1:]))


def middle(lo, hi):
    if lo is None:
        return F(0) if hi is None else hi-1
    return lo+1 if hi is None else (lo+hi)/2


class Model:
    def __init__(self, raw):
        require(type(raw) is dict and set(raw) <= {'points','edges','nonedges'}, 'input keys')
        require(type(raw['points']) is list and len(raw['points']) <= 16, 'point cap')
        self.points = [point(p) for p in raw['points']]
        require(len(set(self.points)) == len(self.points), 'noninjective input')
        self.edges = pairs(raw['edges'], len(self.points))
        self.targets = sorted(set(combinations(range(len(self.points)),2))-set(self.edges))
        if 'nonedges' in raw:
            require(pairs(raw['nonedges'],len(self.points)) == self.targets, 'wrong complement')
        self.lines = sorted({primitive_line(self.points[a],self.points[b]) for a,b in self.edges})
        require(len(self.lines) <= 10, 'line cap; resource refusal')
        self.signs = sorted(all_cells(self.lines))
        self.frames = [line_frame(line) for line in self.lines]
        zeros = set(self.points)
        for (a,b,c),(d,e,f) in combinations(self.lines,2):
            determinant = a*e-b*d
            if determinant:
                zeros.add((F(b*f-c*e,determinant),F(c*d-a*f,determinant)))
        self.zeros = sorted(zeros)
        self.cuts = [sorted({parameter(q,r,v) for q in self.zeros if value(line,q)==0})
                     for line,(r,v) in zip(self.lines,self.frames)]
        self.faces = []
        for i,cut in enumerate(self.cuts):
            r,v = self.frames[i]
            for lo,hi in intervals(cut):
                t = middle(lo,hi)
                q = (r[0]+t*v[0],r[1]+t*v[1])
                cells = self.incident(q)
                require(len(cells)==2, 'face must have exactly two sides')
                self.faces.append((i,lo,hi,cells,self.blocked(q)))
        adjacency = [set() for _ in self.signs]
        for i,lo,hi,cells,is_blocked in self.faces:
            if not is_blocked:
                a,b = cells
                adjacency[a].add(b); adjacency[b].add(a)
        self.components, self.labels = [], [-1]*len(self.signs)
        for start in range(len(self.signs)):
            if self.labels[start] >= 0:
                continue
            label, todo, members = len(self.components), [start], []
            self.labels[start] = label
            for u in todo:
                members.append(u)
                for v in sorted(adjacency[u]):
                    if self.labels[v] < 0:
                        self.labels[v] = label; todo.append(v)
            self.components.append(sorted(members))
        self.target_cuts, self.incidence = {}, {}
        for pair in self.targets:
            a,b = [self.points[i] for i in pair]
            cut = {F(0),F(1)}
            for line in self.lines:
                u,v = value(line,a),value(line,b)
                if u != v and 0 < -u/(v-u) < 1:
                    cut.add(-u/(v-u))
            for q in self.points:
                if on_segment(q,a,b):
                    cut.add(parameter(q,a,subtract(b,a)))
            cut = sorted(cut)
            visited = set()
            for lo,hi in zip(cut,cut[1:]):
                q = interpolate(a,b,(lo+hi)/2)
                if not self.blocked(q):
                    visited.add(self.locate(q)['component'])
            self.target_cuts[pair],self.incidence[pair] = cut,sorted(visited)
        common = set(range(len(self.components)))
        for labels in self.incidence.values():
            common.intersection_update(labels)
        self.common = sorted(common)

    def blocked(self,q):
        return blocked(q,self.points,self.edges)

    def incident(self,q):
        vals = [value(line,q) for line in self.lines]
        return [i for i,signs in enumerate(self.signs)
                if all(v==0 or s*v>0 for s,v in zip(signs,vals))]

    def locate(self,q):
        require(not self.blocked(q), 'location is forbidden')
        zero = [i for i,line in enumerate(self.lines) if value(line,q)==0]
        if not zero:
            signs = tuple(1 if value(line,q)>0 else -1 for line in self.lines)
            cell = self.signs.index(signs)
            return {'kind':'cell','id':cell,'cell':cell,'component':self.labels[cell]}
        require(len(zero)==1, 'interval sample at zero-face')
        i = zero[0]; r,v = self.frames[i]; t = parameter(q,r,v)
        for index,(j,lo,hi,cells,is_blocked) in enumerate(self.faces):
            if j==i and open_interval(t,lo,hi):
                require(not is_blocked and self.labels[cells[0]]==self.labels[cells[1]], 'bad portal')
                cell = min(cells)
                return {'kind':'face','id':index,'cell':cell,'component':self.labels[cell]}
        raise ValueError('unlisted face')
