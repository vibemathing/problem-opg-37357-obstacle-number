"""C28 triangular-prism three-module seed; pure data and finite graph operations."""
from itertools import combinations


def seed():
    columns = [(0, 3), (1, 4), (2, 5)]
    modules = []
    for i, j in ((0, 1), (1, 2), (2, 0)):
        a, A = columns[i]; b, B = columns[j]
        cycle = [a, b, B, A]
        modules.append({'id': len(modules), 'cycle': cycle,
                        'edges': sorted([sorted(e) for e in zip(cycle, cycle[1:]+cycle[:1])])})
    edges = sorted({tuple(e) for m in modules for e in m['edges']})
    # Consistently oriented triangular-prism sphere faces.
    faces = [[0, 2, 1], [3, 4, 5], [0, 1, 4, 3], [1, 2, 5, 4], [2, 0, 3, 5]]
    next_at = [{} for _ in range(6)]
    for f in faces:
        for k, v in enumerate(f):
            next_at[v][f[(k-1) % len(f)]] = f[(k+1) % len(f)]
    rotation = []
    for table in next_at:
        start = min(table); row = [start]
        for _ in range(len(table)-1):
            row.append(table[row[-1]])
        if table[row[-1]] != start or len(set(row)) != len(table):
            raise ValueError('vertex link is not one cycle')
        rotation.append(row)
    nonedges = [list(e) for e in combinations(range(6), 2) if e not in edges]
    return {'name': 'triangular_prism_three_C4_modules', 'n': 6, 'columns': [list(c) for c in columns],
            'modules': modules, 'edges': [list(e) for e in edges], 'nonedges': nonedges,
            'rotation': rotation, 'oriented_faces': faces,
            'minimality': 'six vertices minimal only for three disjoint two-vertex columns, not a global obstruction minimum',
            'verdict': 'candidate_only'}


def validate_embedding(data):
    n = data['n']; edges = {tuple(e) for e in data['edges']}
    if n != 6 or not 9 <= len(edges) <= 12 or any(a >= b for a, b in edges):
        raise ValueError('simple prism census')
    directed = {(a,b) for a,b in edges} | {(b,a) for a,b in edges}
    rotations = data['rotation']
    if len(rotations) != n:
        raise ValueError('rotation census')
    for v, row in enumerate(rotations):
        if len(set(row)) != len(row) or set(row) != {b for a,b in directed if a == v}:
            raise ValueError('wrong neighbors in rotation')
    todo = set(directed); cycles = []
    while todo:
        start = min(todo); d = start; cycle = []
        for _ in range(2*len(edges)+1):
            if d not in todo:
                if d != start:
                    raise ValueError('face repeats wrong dart')
                break
            todo.remove(d); a,b = d; cycle.append(a)
            row = rotations[b]; d = (b, row[(row.index(a)+1) % len(row)])
        else:
            raise ValueError('face traversal cap')
        cycles.append(cycle)
    normalize = lambda f: min(tuple(f[i:]+f[:i]) for i in range(len(f)))
    if sorted(map(normalize, cycles)) != sorted(map(normalize, data['oriented_faces'])):
        raise ValueError('face/rotation disagreement')
    if n-len(edges)+len(cycles) != 2:
        raise ValueError('not Euler sphere')
    return {'vertices': n, 'edges': len(edges), 'faces': len(cycles), 'darts': len(directed),
            'face_lengths': sorted(map(len, cycles)), 'euler': 2}


def completion(code):
    """All 27 choices: none or either diagonal in each of three quadrilateral faces."""
    if type(code) is not int or not 0 <= code < 27:
        raise ValueError('completion code 0..26')
    g=seed(); faces=g['oriented_faces'][:2]; edges={tuple(e) for e in g['edges']}
    digits=[]; state=code
    for face in g['oriented_faces'][2:]:
        digit=state%3;state//=3;digits.append(digit)
        a,b,c,d=face
        if digit==0:faces.append(face)
        elif digit==1:
            edges.add(tuple(sorted((a,c))));faces.extend([[a,b,c],[a,c,d]])
        else:
            edges.add(tuple(sorted((b,d))));faces.extend([[b,c,d],[b,d,a]])
    tables=[{} for _ in range(6)]
    for f in faces:
        for j,v in enumerate(f):tables[v][f[(j-1)%len(f)]]=f[(j+1)%len(f)]
    rotations=[]
    for table in tables:
        first=min(table);row=[first]
        for _ in range(len(table)-1):row.append(table[row[-1]])
        if table[row[-1]]!=first or len(set(row))!=len(table):raise ValueError('invalid link')
        rotations.append(row)
    g.update({'completion_code':code,'face_choices':digits,'edges':[list(e) for e in sorted(edges)],
              'nonedges':[list(e) for e in combinations(range(6),2) if e not in edges],
              'oriented_faces':faces,'rotation':rotations})
    return g
