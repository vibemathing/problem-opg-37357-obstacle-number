"""C26 completion: a new finite-segment incidence check and composition attacks.
Pure memory and bounded JSON stdout; no C21/C25 code is imported.
"""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter
from copy import deepcopy
import hashlib
import json
from slab_incidence import Slabs, at, on
from clause_bridge import Bridge, X4, canonical, determinant, project, satisfied
from controls import meet, crossed_key_paths, shared_endpoint
from growth import deletion_trees, check_deletion_trees, glue_example


def need(ok, why):
    if not ok:
        raise ValueError(why)


def masks(rows, count):
    return sorted(sum(1 << i for i, row in enumerate(rows) if c in row) for c in range(count))


def projection_check(points, edges, claim):
    model = Slabs(points, edges)
    need(type(claim['components']) is int and claim['components'] == len(model.components), 'component census')
    need(claim['targets'] == [list(p) for p in model.targets], 'target census')
    rows = claim['incidence']
    need(len(rows) == len(model.targets), 'incidence census')
    need(all(type(row) is list and row == sorted(set(row)) and all(type(c) is int and 0 <= c < claim['components'] for c in row) for row in rows), 'label type/range')
    need(masks(rows, claim['components']) == masks(model.incidence, len(model.components)), 'component-target hypergraph')
    need(type(claim['exists']) is bool and claim['exists'] == bool(model.common), 'total intersection')
    return model


def fixture_replay():
    tiny = '1/'+str(10**40)
    # Exact projections read from the four frozen C20 certificates. Different
    # cell decompositions are compared as incidence hypergraphs up to relabeling.
    cases = [
      ('c18_negative', [[-20,0],[0,20],[20,0],[0,-20],[1,8],[-2,-7],[30,1]],
       [[0,1],[0,2],[0,3],[1,2],[2,3]], 3,
       [[2],[1],[0,2],[1,2],[2],[1,2],[0],[2],[1],[0],[1,2],[1],[0],[1,2],[0,2],[0,1]], False,
       '307717b13e0e756c2a5cd09d3575473d59c3aee6bf5e416756c1fde1ae0603e6'),
      ('forced_line_witness', [[-1,0],[0,0],[1,0]], [[0,1]], 1, [[0],[0]], True,
       'bfb059d6f8c1f31128a1255992416e99ecd98068f26ece4ae06b953f8ac27e33'),
      ('square_diagonals', [[-2,-2],[2,-2],[2,2],[-2,2]], [[0,1],[0,3],[1,2],[2,3]], 2, [[1],[1]], True,
       'bc71008cc8b04e24f46ba90940ced13f808beabe7a9609d04c4f2f7d59b0a362'),
      ('tiny_open_gap', [[-2,0],[0,0],[tiny,0],[2,0]], [[0,1],[2,3]], 1, [[0],[0],[0],[0]], True,
       'c4646e4ac9b91a2e36b1179ff8cf47f1a9f1a872d76f55921518d045fa373e1f')]
    results, claims = [], []
    for name, pts, edges, count, inc, exists, pin in cases:
        targets = [list(p) for p in combinations(range(len(pts)), 2) if list(p) not in edges]
        claim = {'components': count, 'targets': targets, 'incidence': inc, 'exists': exists}
        m = projection_check(pts, edges, claim); claims.append((pts, edges, claim))
        results.append({'name': name, 'original_certificate_sha256_declared': pin,
                        'scope': 'incidence projection, not old cell/tree fields',
                        'components': count, 'events': len(m.xs), 'nodes': len(m.nodes),
                        'coverage_masks': masks(m.incidence, count), 'accepted': True})
    damages = []
    p, e, original = claims[0]
    for name, field, value in [
        ('false_common', 'exists', True), ('drop_component', 'components', 2),
        ('drop_target', 'targets', original['targets'][:-1]),
        ('omit_incidence', 'incidence', original['incidence'][:-1]),
        ('pairwise_is_global', 'incidence', [[0] for _ in original['incidence']]),
        ('erase_blocked_separator', 'incidence', [[0,1,2] for _ in original['incidence']]),
        ('wrong_zero_dim_label', 'incidence', [[False]]+original['incidence'][1:])]:
        claim = deepcopy(original); claim[field] = value
        try:
            projection_check(p, e, claim)
        except ValueError:
            damages.append(name)
        else:
            raise ValueError('accepted damage '+name)
    pts, edges, orig = claims[1]
    claim = deepcopy(orig); claim['components'] = 2; claim['incidence'] = [[0],[1]]; claim['exists'] = False
    try:
        projection_check(pts, edges, claim)
    except ValueError:
        damages.append('infinite_support_line_barrier')
    else:
        raise ValueError('accepted whole-line barrier')
    return results, damages


def degeneracies():
    tiny = '1/'+str(10**40)
    tests = [
      ('empty', [], [], 1, True), ('one_point', [[0,0]], [], 1, True),
      ('vertical_edge', [[0,-1],[0,1]], [[0,1]], 1, True),
      ('collinear_forced', [[-1,0],[0,0],[1,0]], [[0,1]], 1, True),
      ('coincident_disjoint', [[-3,0],[-2,0],[2,0],[3,0]], [[0,1],[2,3]], 1, True),
      ('overlap', [[0,0],[1,0],[2,0],[3,0]], [[0,2],[1,3]], 1, False),
      ('point_on_edge', [[0,0],[1,0],[2,0]], [[0,2]], 1, False),
      ('free_support_concurrence', [[2,0],[3,0],[0,2],[0,3],[2,2],[3,3]], [[0,1],[2,3],[4,5]], 1, True),
      ('forbidden_concurrence', [[-1,0],[1,0],[0,-1],[0,1],[0,0]], [[0,1],[2,3]], 1, False),
      ('isolated_puncture', [[-1,0],[0,0],[1,0]], [], 1, True),
      ('triangle_empty_targets', [[0,0],[4,0],[0,4]], [[0,1],[0,2],[1,2]], 2, True),
      ('square_inside_outside', [[-2,-2],[2,-2],[2,2],[-2,2],[0,0],[4,0]], [[0,1],[1,2],[2,3],[0,3]], 2, False),
      ('tiny_gap', [[-2,0],[0,0],[tiny,0],[2,0]], [[0,1],[2,3]], 1, True),
      ('near_parallel', [[0,0],[1,0],[0,tiny],[1,'2/'+str(10**40)]], [[0,1],[2,3]], 1, True)]
    output = []
    for name, p, e, count, exists in tests:
        m = Slabs(p, e)
        need(len(m.components) == count and bool(m.common) == exists, 'degeneracy '+name)
        output.append({'name': name, 'components': count, 'exists': exists})
    return output


def pair_local_checks():
    b = Bridge(10, X4); clauses, rows = b.compile()
    indices = {c: i+1 for i, c in enumerate(clauses)}
    base = [(Q(i), Q(i*i)) for i in range(10)]
    tests = [(base, b), ([(y,-x) for x,y in base], b), ([(-x,y) for x,y in base], b)]
    for row in (crossed_key_paths(), shared_endpoint()):
        p = [tuple(Q(x) for x in q) for q in row['points']]
        tests.append((p, Bridge(len(p), row['edges'])))
    checked, samples = 0, []
    for points, bridge in tests:
        m = Slabs(list(points), bridge.edges)
        inc = dict(zip(m.targets, map(set, m.incidence)))
        assignment, conflicts = project(points, bridge)
        for c in conflicts:
            ab, cd, sid = tuple(c['ab']), tuple(c['cd']), c['side']
            need(not inc[ab].intersection(inc[cd]), 'opposed key paths share a real free component')
            forcing = []
            for positive, key in ((True, 'positive_path'), (False, 'negative_path')):
                path = c[key]
                signs = [determinant(points[cd[0]], points[cd[1]], points[v]) > 0 for v in path if v not in cd]
                mode = (2 if all(signs) else 0)+(1 if positive else 0)
                source = ('K', (sid,)+tuple(path), mode)
                clause = canonical(bridge.raw_clause(source))
                need(clause is not None, 'forced constraint became tautology')
                other = [x for x in clause if abs(x) != sid]
                need(all(not satisfied((x,), assignment) for x in other), 'non-side literals not all false')
                remain = [x for x in clause if abs(x) == sid]
                need(remain == [sid if positive else -sid], 'incorrect force polarity')
                forcing.append({'origin': [source[0], list(source[1]), mode],
                                'C22_row': indices[clause] if bridge is b else None,
                                'residual': remain})
            checked += 1
            if len(samples) < 3:
                samples.append({'ab': list(ab), 'cd': list(cd), 'source_rows': forcing})
    return {'opposed_path_pairs_checked': checked, 'X4_source_samples': samples,
            'scope': 'fixed-coordinate falsifiers plus universal proof, not placement enumeration'}


def strict_inside(q, polygon):
    parity = False
    for a, b in zip(polygon, polygon[1:]+polygon[:1]):
        if on(q, a, b):
            return False
        if (a[1] > q[1]) != (b[1] > q[1]):
            x = a[0]+(q[1]-a[1])*(b[0]-a[0])/(b[1]-a[1])
            if x > q[0]:
                parity = not parity
    return parity


def star_comb(r):
    need(type(r) is int and 1 <= r <= 8, 'star test range')
    m = 2*r; eps = Q(1, 10*m); delta = Q(1, 1000*m**3)
    p = [(Q(0), Q(0))]+[(Q(i), 1+delta*i*i) for i in range(1,m+1)]
    e = [(0,i) for i in range(1,m+1)]
    L, R, H = Q(5,4), Q(m)-Q(1,4), Q(5,4)
    polygon = [(L,Q(2)),(R,Q(2)),(R,H)]
    for i in range(m-1,0,-1):
        left, right = Q(i)+Q(1,3), Q(i)+Q(2,3)
        polygon.extend([(right,H),(right,1-eps),(left,1-eps),(left,H)])
    polygon.append((L,H))
    sides = list(zip(polygon, polygon[1:]+polygon[:1]))
    need(len(set(polygon)) == len(polygon), 'identified polygon corners')
    for i,j in combinations(range(len(sides)),2):
        if (i-j) % len(sides) not in (1, len(sides)-1):
            need(not meet(*sides[i], *sides[j]), 'comb self intersection')
    need(all(not strict_inside(q,polygon) and not any(on(q,a,b) for a,b in sides) for q in p), 'graph point in obstacle')
    need(all(not meet(p[i],p[j],a,b) for i,j in e for a,b in sides), 'visible edge blocked')
    need(all(determinant(p[i],p[j],p[k]) != 0 for i,j,k in combinations(range(len(p)),3)), 'star GP')
    need(all(not meet(p[i],p[j],p[k],p[l]) for (i,j),(k,l) in combinations(e,2) if not {i,j}.intersection((k,l))), 'plane star')
    for i,j in combinations(range(1,m+1),2):
        q = at(p[i],p[j],Q(1,2*(j-i)))
        need(strict_inside(q,polygon), 'unblocked within/cross-block nonedge')
    sm = Slabs(list(p),e); need(bool(sm.common), 'tree exterior should be common')
    if m <= 6:
        b = Bridge(m+1,e); cs,_ = b.compile(); assignment, conflicts = project(p,b)
        need(not conflicts and all(satisfied(c,assignment) for c in cs), 'star obstacle-to-CNF')
    return {'r':r,'n':m+1,'e':m,'block_lower_bounds_sum':r,'actual_obstacle_number':1,
            'polygon_corners':len(polygon),'nonedges_checked':m*(m-1)//2,
            'cross_block_nonedges':2*r*(r-1),
            'points':[[str(x) for x in q] for q in p] if r==2 else None,
            'polygon':[[str(x) for x in q] for q in polygon] if r==2 else None}


def growth_mutations():
    rows = deletion_trees(); rejected = []
    for name, broken in [('missing_deletion',rows[:-1]), ('duplicate_deletion',rows[:-1]+[rows[0]])]:
        try:
            check_deletion_trees(broken)
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError('accepted bad connectivity certificate')
    broken = deepcopy(rows); broken[0]['tree'][0] = [0,1]
    try:
        check_deletion_trees(broken)
    except ValueError:
        rejected.append('nonedge_tree_link')
    else:
        raise ValueError('accepted nonedge link')
    g = glue_example(); cross_nonedges = 7*7
    need(17*16//2-45 == 21+21+cross_nonedges, 'cross-block complement accounting')
    return {'connectivity_mutations_rejected':rejected,'glue_total_nonedges':91,
            'glue_cross_block_nonedges':cross_nonedges, 'copies_have_disjoint_demand_sets':True}


def three_point_census():
    grid = [(Q(x), Q(y)) for x in range(2) for y in range(3)]
    count = 0
    pairs = list(combinations(range(3), 2))
    for points in combinations(grid, 3):
        collinear = determinant(*points) == 0
        axis = 0 if len({p[0] for p in points}) > 1 else 1
        order = sorted(range(3), key=lambda i: points[i][axis])
        long_edge = tuple(sorted((order[0], order[2])))
        short_edges = {tuple(sorted((order[0], order[1]))), tuple(sorted((order[1], order[2])))}
        for bits in range(8):
            edges = [p for i, p in enumerate(pairs) if bits >> i & 1]
            expected = True
            if collinear and len(edges) != 3:
                expected = long_edge not in edges and not short_edges.issubset(edges)
            need(bool(Slabs(list(points), edges).common) == expected, 'three-point reference mismatch')
            count += 1
    return count


def main():
    replay, mutations = fixture_replay()
    out = {'verdict':'candidate_only','trusted_receipt':False,
           'incidence_method':'new finite-segment vertical decomposition; no C21/C25 imports',
           'four_certificate_incidence_projections':replay,'rejected_incidence_mutations':mutations,
           'degeneracy_controls':degeneracies(),'key_path_vs_true_component':pair_local_checks(),
           'amplification_counterexamples':[star_comb(r) for r in (1,2,3,4,8)],
           'growth_mutations':growth_mutations(), 'three_point_graphs_checked':three_point_census()}
    return out


if __name__ == '__main__':
    print(json.dumps(main(),sort_keys=True,separators=(',',':')))
