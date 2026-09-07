"""Finite incidence interface for at most two component labels.
No geometry is inferred from abstract masks. Memory-only; JSON stdout.
"""
from itertools import combinations, product
import json


def require(test, text):
    if not test:
        raise ValueError(text)


def meet(rows, full):
    value = full
    for row in rows: value &= row
    return value


def validate(rows, components):
    require(type(components) is int and 1 <= components <= 8, 'component bound')
    require(type(rows) is list and len(rows) <= 8, 'target bound')
    require(all(type(r) is int and 0 <= r < (1 << components) for r in rows), 'incidence masks')


def anchored(rows, components, rank=3):
    validate(rows, components)
    require(type(rank) is int and 1 <= rank <= 8, 'rank bound')
    full = (1 << components)-1
    missing, intersections, obstructions = [], [], []
    for u in range(components):
        ids = [i for i, row in enumerate(rows) if not (row >> u & 1)]
        missing.append(ids)
        intersections.append(meet([rows[i] for i in ids], full))
        cut = None
        for k in range(1, min(rank, len(ids))+1):
            cut = next((list(t) for t in combinations(ids, k)
                        if meet([rows[i] for i in t], full) == 0), None)
            if cut is not None: break
        obstructions.append(cut)
    return {'two_cover': any(intersections), 'missing': missing,
            'possible_second_components': intersections, 'rank_cuts': obstructions,
            'rank_exclusion_certificate': all(t is not None for t in obstructions)}


def check_cuts(rows, components, cuts, rank):
    validate(rows, components)
    require(type(cuts) is list and len(cuts) == components, 'one cut for EVERY first component')
    for u, cut in enumerate(cuts):
        require(type(cut) is list and 1 <= len(cut) <= rank and len(set(cut)) == len(cut), 'cut size')
        require(all(type(i) is int and 0 <= i < len(rows) and not (rows[i] >> u & 1) for i in cut), 'anchor misses all targets')
        require(meet([rows[i] for i in cut], (1 << components)-1) == 0, 'cut intersection must be empty')
    return True


def by_labels(rows, components):
    # Different interface: try every two-color target partition, without selecting u.
    full = (1 << components)-1
    valid = []
    for labels in product(range(2), repeat=len(rows)):
        if all(meet([rows[i] for i in range(len(rows)) if labels[i] == c], full)
               for c in (0, 1)):
            valid.append(list(labels))
    return valid


def main():
    systems = no_two = rank_certificates = 0
    for components in range(1, 4):
        for targets in range(6):
            for family in product(range(1 << components), repeat=targets):
                rows = list(family); a = anchored(rows, components)
                b = by_labels(rows, components)
                require(a['two_cover'] == bool(b), 'anchored versus labels')
                if a['rank_exclusion_certificate']:
                    check_cuts(rows, components, a['rank_cuts'], 3)
                    require(not b, 'false rank-three exclusion')
                    rank_certificates += 1
                no_two += not bool(b); systems += 1
    # Selected C18 incidence, no new geometric realization claim.
    c18 = [6, 5, 3, 1]
    exact = by_labels(c18, 3)
    pairwise = [list(z) for z in product(range(2), repeat=4)
                if all(z[i] != z[j] or (c18[i] & c18[j]) for i, j in combinations(range(4), 2))]
    removed = [z for z in pairwise if z not in exact]
    require(len(pairwise) == 8 and len(exact) == 6 and len(removed) == 2, 'C18 rank-three control')
    # Sharp rank cap failure: {anchor}, then four complementary triples on four other labels.
    gap = [1] + [30 ^ (1 << i) for i in range(1, 5)]
    rank3, rank4 = anchored(gap, 5, 3), anchored(gap, 5, 4)
    require(not by_labels(gap, 5) and not rank3['rank_exclusion_certificate'], 'rank-three not necessary')
    require(rank3['rank_cuts'][0] is None and rank4['rank_exclusion_certificate'], 'rank-four anchor')
    check_cuts(gap, 5, rank4['rank_cuts'], 4)
    reject = []
    valid = rank4['rank_cuts']
    damaged = [('missing_anchor', valid[:-1]), ('false_empty', [[1, 2, 3]]+valid[1:]),
               ('hit_anchor', [[0]]+valid[1:]), ('repeated_target', [[1, 1, 2, 3]]+valid[1:])]
    for name, cuts in damaged:
        try: check_cuts(gap, 5, cuts, 4)
        except ValueError: reject.append(name)
        else: raise ValueError('accepted damaged anchored certificate')
    return {'verdict': 'candidate_only', 'trusted_receipt': False,
            'finite_set_systems_checked': systems, 'no_two_cover_systems': no_two,
            'valid_rank_three_exclusions': rank_certificates,
            'C18_selected': {'masks': c18, 'pairwise_models': pairwise, 'joint_models': exact, 'removed': removed},
            'rank_gap': {'masks': gap, 'rank3': rank3, 'rank4': rank4, 'geometric_realization': None},
            'rejected_mutations': reject,
            'root_gap': 'Need a planar graph forcing anchored empty intersections for EVERY actual placement; no such family is supplied.'}


if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True, separators=(',', ':')))
