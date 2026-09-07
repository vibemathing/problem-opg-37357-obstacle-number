"""Bounded exact pressure test of vertex-order-only placement compression.
No files/network/subprocess/dynamic execution. Prints first cover discrepancy.
"""
from itertools import combinations
import json
from signature import encode
from sweep import arrangement, graph_cover


def search():
    p = [(1,1),(-2,-2),(3,6),(-5,-10),(7,-7),(-11,11)]
    q = p[:-1] + [(-11, '1101/100')]
    sp, sq = encode(p), encode(q)
    if sp['orientation'] != sq['orientation']:
        raise AssertionError('vertex order type changed')
    ap, aq = arrangement(sp), arrangement(sq)
    fixed = [(0,1),(2,3)]
    other = [ij for ij in combinations(range(6),2) if ij not in fixed+[(4,5)]]
    tested = 0
    for size in range(len(other)+1):
        for extra in combinations(other,size):
            edges = fixed+list(extra)
            cp,cq = graph_cover(ap,edges),graph_cover(aq,edges)
            tested += 1
            if cp['minimum_cover'] != cq['minimum_cover']:
                return {'verdict':'candidate_only','tested':tested,'points_before':p,'points_after':q,
                        'edges':edges,'before':cp,'after':cq,'vertex_orientation':sp['orientation'],
                        'meaning':'fixed drawing cover discrepancy; not an unrestricted graph lower bound'}
    return {'verdict':'candidate_only','tested':tested,'cover_discrepancy_found':False,
            'domain':'two mandatory matching edges, third excluded, twelve remaining edges arbitrary'}


if __name__ == '__main__':
    print(json.dumps(search(),sort_keys=True,separators=(',',':')))
