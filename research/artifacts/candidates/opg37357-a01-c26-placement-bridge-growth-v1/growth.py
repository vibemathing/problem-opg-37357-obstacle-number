"""C26: finite combinatorial certificates for the amplification interface.
Pure memory only. X4-copy coloring is NOT asserted to be a full representation.
"""
from itertools import combinations, product
from clause_bridge import X4, require


def deletion_trees():
    result = []
    for k in range(4):
        for deleted in combinations(range(10),k):
            left = sorted(set(range(10))-set(deleted))
            seen, queue, tree = {left[0]}, [left[0]], []
            for u in queue:
                for a,b in X4:
                    if u not in (a,b):
                        continue
                    v = b if u == a else a
                    if v in left and v not in seen:
                        seen.add(v); queue.append(v); tree.append([u,v])
            require(seen == set(left), 'X4 deletion disconnected')
            result.append({'deleted':list(deleted),'tree':tree})
    return result


def check_deletion_trees(rows):
    require(len(rows) == 176, 'must cover all <=3 deletions')
    expected = {s for k in range(4) for s in combinations(range(10),k)}
    seen = set()
    for row in rows:
        deleted = tuple(row['deleted'])
        require(deleted in expected and deleted not in seen, 'deletion census')
        seen.add(deleted)
        left = set(range(10))-set(deleted)
        parent = {v:v for v in left}
        def find(v):
            while parent[v] != v:
                v = parent[v]
            return v
        require(len(row['tree']) == len(left)-1, 'spanning edge count')
        for u,v in row['tree']:
            require(u in left and v in left and tuple(sorted((u,v))) in X4, 'non-edge in certificate')
            a,b = find(u),find(v)
            require(a != b, 'cycle in spanning certificate')
            parent[a] = b
        require(len({find(v) for v in left}) == 1, 'certificate not spanning')
    return True


def hypergraph_chromatic(vertices, edges, cap=100000):
    require(type(vertices) is int and 0 <= vertices <= 10, 'abstract control vertex cap')
    require(all(len(e) >= 2 and all(0 <= v < vertices for v in e) for e in edges), 'hyperedges')
    if vertices == 0:
        return 0,[],0
    trials = 0
    for h in range(1,vertices+1):
        for colors in product(range(h),repeat=vertices):
            trials += 1
            require(trials <= cap, 'coloring resource refusal')
            if all(len({colors[v] for v in e}) > 1 for e in edges):
                return h,list(colors),trials
    raise ValueError('no finite proper coloring')


def glue_example():
    # Two copies identified exactly on their triangle (0,2,3).
    phi = {v:v for v in (0,2,3)}
    phi.update({v:10+i for i,v in enumerate(v for v in range(10) if v not in phi)})
    edges = set(X4) | {tuple(sorted((phi[a],phi[b]))) for a,b in X4}
    copies = [set(range(10)),set(phi.values())]
    target_sets = [set(combinations(sorted(vs),2))-edges for vs in copies]
    require(len(edges) == 45 and len(set.union(*copies)) == 17, 'triangle gluing count')
    require(all(len(s) == 21 for s in target_sets) and not (target_sets[0] & target_sets[1]),
            'the designated copies must share no nonedge')
    # This is only a coloring of copy-demand hyperedges, not obstacle coordinates.
    colors = {pair:1 for s in target_sets for pair in s}
    for s in target_sets:
        colors[min(s)] = 0
    require(all({colors[v] for v in s} == {0,1} for s in target_sets), 'two-color witness')
    return {'n':17,'e':45,'copies':[sorted(vs) for vs in copies],
            'nonedge_counts':[len(s) for s in target_sets], 'shared_nonedges':[],
            'red_targets':[list(min(s)) for s in target_sets],
            'scope':'copy-demand relaxation only; no obstacle upper bound'}


def amplification_controls():
    trees = deletion_trees(); check_deletion_trees(trees)
    require(min(sum(v in e for e in X4) for v in range(10)) == 4, 'minimum degree')
    fano = [(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
    h,colors,trials = hypergraph_chromatic(7,fano)
    require(h == 3, 'abstract Fano control')
    return {'x4_deletion_certificates':len(trees),'x4_min_degree':4,
            'glued_copy_relaxation':glue_example(),
            'abstract_fano':{'edges':[list(e) for e in fano], 'chromatic':h,
                             'colors':colors,'trials':trials,'planar_obstacle_realization':None}}
