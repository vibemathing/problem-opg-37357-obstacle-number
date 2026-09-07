"""Exact bit-parallel truth table over every direction and two-label assignment.
Side variables are existentially eliminated by their complete unit constraints.
No solver, prior candidate imports, I/O, process creation, or dynamic evaluation.
"""
from itertools import product


def require(ok, message):
    if not ok:
        raise ValueError(message)


def planes(n):
    require(0 <= n <= 20, 'truth-table dimension cap')
    rows = 1 << n
    allbits = (1 << rows)-1
    table = {}
    for var in range(1,n+1):
        width = 1 << (n-var)
        mask = ((1 << width)-1) << width
        covered = 2*width
        while covered < rows:
            mask |= mask << covered
            covered *= 2
        table[var] = mask
        table[-var] = allbits ^ mask
    return rows,allbits,table


def enumerate_models(data):
    n = len(data['orientation_triples']); k = len(data['nonedges'])
    require(n == 20 and k <= 6, 'release scope')
    total,universe,truth = planes(n)
    nz = 2*k; first_side = n+nz+1
    sides = list(range(first_side, data['variables']+1))
    pure, grouped = [], {}
    for row in data['clauses']:
        orient = [v for v in row if abs(v) <= n]
        guard = tuple(v for v in row if n < abs(v) < first_side)
        tail = tuple(v for v in row if abs(v) >= first_side)
        require(len(tail) <= 1, 'more than one side in clause')
        value = 0
        for lit in orient:
            value |= truth[lit]
        if not guard and not tail:
            pure.append(value)
        else:
            key = (guard, tail)
            grouped[key] = grouped.get(key, 0) | (universe ^ value)
    base = universe
    for value in pure:
        base &= value
    results, minimum = [], None
    for colors in product(range(2), repeat=k):
        zv = {data['z'][i][r]:(colors[i] == r) for i in range(k) for r in range(2)}
        force = {sid:[0,0] for sid in sides}
        allowed = base
        for (guards,tail),must in grouped.items():
            if any(zv[abs(lit)] == (lit > 0) for lit in guards):
                continue
            if not tail:
                allowed &= universe ^ must
            else:
                lit = tail[0]
                force[abs(lit)][1 if lit > 0 else 0] |= must
        for no,yes in force.values():
            allowed &= universe ^ (no & yes)
        first = (allowed & -allowed).bit_length()-1 if allowed else None
        results.append({'colors':list(colors),'satisfying_direction_assignments':allowed.bit_count(),
                        'first_direction_index':first})
        if first is not None:
            values = [bool(first >> (n-i) & 1) for i in range(1,n+1)]
            values += [zv[i] for i in range(n+1,first_side)]
            values += [bool(force[i][1] >> first & 1) for i in sides]
            require(all(any(values[abs(lit)-1] == (lit>0) for lit in c)
                        for c in data['clauses']), 'returned minimum fails raw clauses')
            if minimum is None or values < minimum:
                minimum = values
    return {'orientation_assignments':total,'direction_label_pairs_exhausted':total*(1<<k),
            'orientation_rule_survivors':base.bit_count(),'labels':results,
            'projected_model_count':sum(r['satisfying_direction_assignments'] for r in results),
            'minimal_model':None if minimum is None else [i+1 if v else -i-1 for i,v in enumerate(minimum)],
            'model_order':'lexicographic truth values by CNF variable ID, False before True',
            'side_quantifier':'complete exact existential elimination, not assumed fixed',
            'sat':minimum is not None,'verdict':'candidate_only'}
