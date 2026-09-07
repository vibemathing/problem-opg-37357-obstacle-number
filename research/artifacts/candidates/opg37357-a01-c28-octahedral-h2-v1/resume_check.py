"""Bounded resumption of PR34. Frozen cores are imported, never regenerated.
Pure arithmetic/data checks and JSON stdout; no file or network operations.
"""
from collections import Counter
from copy import deepcopy
from itertools import combinations, product
import hashlib
import json
from coupling import build, graph, dimacs
from exhaustive import enumerate_models
from second_check import reconstruct, scalar_table
from geometry import witness_data, check_witness


def require(test, text):
    if not test:
        raise ValueError(text)


def mutations(formula, witness, model):
    rejected = []
    def test(name, function):
        try:
            function()
        except (ValueError, KeyError, IndexError, TypeError):
            rejected.append(name)
        else:
            raise ValueError('accepted damaged candidate: '+name)
    for edge in ([1, 3], [1, 5], [3, 5]):
        f = deepcopy(formula); f['edges'].remove(edge)
        test('stale_edge_'+str(edge), lambda: reconstruct(f))
    row = next(i for i, o in enumerate(formula['origins']) if o['family'] == 'key')
    for mode in range(3):
        f = deepcopy(formula); o = f['origins'][row]; a, b = o['nonedges'][0]
        if mode == 0: o['path'] = [a, b]
        if mode == 1: o['path'][1] = a
        if mode == 2: o['nonedges'][1] = o['nonedges'][0]
        test('path_'+str(mode), lambda: reconstruct(f))
    for variable in (1, 7, 20):
        m = model[:]; m[variable-1] *= -1
        test('coordinate_orientation_'+str(variable), lambda: check_witness(witness, formula, m))
    for family in ('four', 'five', 'key'):
        f = deepcopy(formula); i = next(i for i, o in enumerate(f['origins']) if o['family'] == family)
        f['origins'].pop(i); f['clauses'].pop(i)
        for j, o in enumerate(f['origins']): o['row'] = j+1
        test('omit_'+family, lambda: reconstruct(f))
    for name, index, value in [('both_labels', 20, 21), ('no_label', 21, -22)]:
        m = model[:]; m[index] = value
        test(name, lambda: check_witness(witness, formula, m))
    w = deepcopy(witness); w['polygon'][2][1] = -49; w['polygon'][3][1] = -49
    test('shallow_finger', lambda: check_witness(w, formula, model))
    w = deepcopy(witness); w['rotation'][0].reverse()
    test('rotation', lambda: check_witness(w, formula, model))
    return rejected


def main():
    f = build(graph()); require(reconstruct(f) == len(f['clauses']), 'complete attribution')
    a, b = enumerate_models(f), scalar_table(f)
    require([v['satisfying_direction_assignments'] for v in a['labels']] == b['projected_counts_by_lex_color'], 'distinct counters')
    w = witness_data(); g = check_witness(w, f, a['minimal_model'])
    rejected = mutations(f, w, a['minimal_model'])
    require(len(rejected) == 16, 'mutation census')
    variants = []
    for mask in range(8):
        formula = build(graph(mask)); reconstruct(formula)
        r = enumerate_models(formula)
        variants.append({'mask': mask, 'sat': r['sat'], 'pairs_exhausted': r['direction_label_pairs_exhausted'],
                         'model': r['minimal_model'], 'cnf_sha256': hashlib.sha256(dimacs(formula)).hexdigest()})
    return {'verdict': 'candidate_only', 'trusted_receipt': False,
            'source_scope': 'four unchanged PR34 cores, not C22/C26 or C21/C25',
            'variables': f['variables'], 'clauses': len(f['clauses']),
            'families': dict(Counter(o['family'] for o in f['origins'])),
            'cnf_sha256': hashlib.sha256(dimacs(f)).hexdigest(),
            'path_counts': [len(p) for p in f['path_census']],
            'bit_parallel': a, 'scalar_full_tail': b, 'geometry': g,
            'witness': w, 'rejected_mutations': rejected, 'connector_boolean_replays': variants,
            'not_rerun_here': 'C27 fiber and PR33 extension; original records retain their own scope'}


if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True, separators=(',', ':')))
