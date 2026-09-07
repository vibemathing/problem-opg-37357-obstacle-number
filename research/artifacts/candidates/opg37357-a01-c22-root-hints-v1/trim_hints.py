"""C22 data reduction by reverse reachability in an explicit unit proof.
No SAT search and no changes to the source CNF or asserted clauses.
"""
from hint_check import ensure


def trim(initial, rows):
    database = {i+1:tuple(c) for i,c in enumerate(initial)}
    trimmed = []
    for identifier, clause, hints in rows:
        assignments = {-lit:None for lit in clause}
        parents, last = {}, None
        for reason in hints:
            c = database[reason]
            ensure(not any(lit in assignments for lit in c),'satisfied reason in trim')
            remaining = [lit for lit in c if -lit not in assignments]
            ensure(len(remaining)<=1,'nonunit reason in trim')
            dependencies = {assignments[-lit] for lit in c if -lit in assignments}
            dependencies.discard(None)
            parents[reason] = dependencies
            if remaining:
                assignments[remaining[0]] = reason
            else:
                last = reason; break
        ensure(last is not None,'no conflict in trim')
        needed, todo = set(), [last]
        for reason in todo:
            if reason not in needed:
                needed.add(reason); todo.extend(parents[reason]-needed)
        trimmed.append([identifier,clause,[r for r in hints if r in needed]])
        database[identifier] = tuple(clause)
    return trimmed
