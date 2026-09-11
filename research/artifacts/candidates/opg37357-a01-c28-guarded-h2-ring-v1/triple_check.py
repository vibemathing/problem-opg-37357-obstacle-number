"""C28 higher-order regression, exact coordinates and all sixteen labelings.
No CNF generator imports or external effects; C27 Fiber is a fixed dependency.
"""
from itertools import combinations, product
from fiber import Fiber
import json


def replay():
    raw={'points':[[-20,0],[0,20],[20,0],[0,-20],[1,8],[-2,-7],[30,1]],
         'edges':[[0,1],[1,2],[2,3],[0,3],[0,2]]}
    targets=[(4,5),(4,6),(5,6),(1,6)]
    f=Fiber(raw);sets=[set(f.incidence[s]) for s in targets]
    if sets!=[{1,2},{0,2},{0,1},{0}]: raise ValueError('changed fixed incidence')
    def common(indices):
        return set.intersection(*(sets[i] for i in indices)) if indices else set(range(len(f.components)))
    empty=[]
    for size in range(1,5):
        for s in combinations(range(4),size):
            if not common(s) and all(not set(old)<=set(s) for old in empty):empty.append(s)
    pair_ok=[];joint_ok=[];excluded=[]
    for z in product((0,1),repeat=4):
        pair=all(z[i]!=z[j] or sets[i]&sets[j] for i,j in combinations(range(4),2))
        joint=all(common([i for i in range(4) if z[i]==r]) for r in (0,1))
        if pair:pair_ok.append(z)
        if joint:joint_ok.append(z)
        if pair and not joint:excluded.append(z)
    if empty!=[(0,3),(0,1,2)] or len(pair_ok)!=8 or len(joint_ok)!=6:
        raise ValueError('pair versus higher-order census mismatch')
    if excluded!=[(0,0,0,1),(1,1,1,0)]:raise ValueError('unexpected false positives')
    return {'verdict':'candidate_only','trusted_receipt':False,'input':raw,
            'targets':targets,'incidence':[sorted(s) for s in sets],
            'minimal_empty_sets':empty,'all_label_tuples':16,
            'pair_compatible':pair_ok,'joint_component_compatible':joint_ok,
            'removed_by_triple':excluded,
            'single_bit_triple_clauses':[[1,2,3],[-1,-2,-3]],
            'direction_scope':'exact rational placement only; not all placements of the graph',
            'source_relation':'fresh replay of the existing C28 rank3-control, not a new graph-level lower bound'}


if __name__=='__main__':
    print(json.dumps(replay(),sort_keys=True,separators=(',',':')))
