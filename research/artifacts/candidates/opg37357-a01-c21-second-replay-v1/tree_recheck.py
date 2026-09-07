"""C21 direct embedded-tree certificate checks, separate from cell enumeration."""
from itertools import combinations
from exact_primitives import (require, point, rational, on_segment, meet,
    orientation, subtract, dot, interpolate, value)
from arrangement_model import pairs


def check_tree(data, model):
    if not model.common:
        require(data.get('mode')=='negative', 'negative construction mode')
        exclusions = data['exclusions']
        require(len(exclusions)==len(model.components), 'negative coverage')
        labels = []
        for row in exclusions:
            c = row['component']; pair = tuple(row['pair'])
            require(type(c) is int and 0<=c<len(model.components), 'negative label')
            require(pair in model.incidence and c not in model.incidence[pair], 'false exclusion')
            labels.append(c)
        require(sorted(labels)==list(range(len(model.components))), 'missing component exclusion')
        return {'tree_vertices':0,'tree_edges':0,'tube_count':None}
    k = len(model.targets)
    require(k>=2, 'this tree consumer currently supports k>=2; use nonterminal for k<2')
    require(data.get('mode')=='tree', 'positive construction mode')
    raw = data['vertices']; require(1<len(raw)<=256, 'tree size cap')
    vertices = [point(v['point']) for v in raw]
    require(len(set(vertices))==len(vertices), 'identified tree vertices')
    require(all(not model.blocked(p) for p in vertices), 'forbidden tree vertex')
    edges = pairs(data['edges'],len(vertices))
    require(len(edges)==len(vertices)-1, 'tree edge count')
    neighbors = [set() for _ in vertices]
    for a,b in edges:
        neighbors[a].add(b); neighbors[b].add(a)
        require(all(not on_segment(p,vertices[a],vertices[b]) for p in model.points), 'edge hits graph point')
        for c,d in model.edges:
            require(not meet(vertices[a],vertices[b],model.points[c],model.points[d]), 'tree hits graph edge')
    reached,todo = {0},[0]
    for u in todo:
        for v in neighbors[u]:
            if v not in reached:
                reached.add(v);todo.append(v)
    require(len(reached)==len(vertices), 'disconnected tree')
    for (a,b),(c,d) in combinations(edges,2):
        common = {a,b}&{c,d}
        if not common:
            require(not meet(vertices[a],vertices[b],vertices[c],vertices[d]), 'tree crossing/contact')
        else:
            w = next(iter(common));u = next(iter({a,b}-{w}));v = next(iter({c,d}-{w}))
            require(orientation(vertices[w],vertices[u],vertices[v])!=0 or
                    dot(subtract(vertices[u],vertices[w]),subtract(vertices[v],vertices[w]))<0,
                    'same-ray overlap')
    selected = data['selected_component']
    require(type(selected) is int and selected in model.common, 'selected component')
    witness_pairs, centers, portals = [],[],[]
    for i,row in enumerate(raw):
        role = row['kind']; p = vertices[i]
        if role=='witness':
            pair = tuple(row['pair']);t = rational(row['parameter'])
            require(pair in model.targets and 0<t<1, 'witness target or endpoint')
            require(p==interpolate(model.points[pair[0]],model.points[pair[1]],t), 'witness equation')
            require(len(neighbors[i])==1, 'witness not leaf')
            witness_pairs.append(pair)
        elif role=='center':
            cell = row['cell']
            require(type(cell) is int and 0<=cell<len(model.signs), 'center cell id')
            require(all(s*value(line,p)>0 for s,line in zip(model.signs[cell],model.lines)), 'center not strict')
            require(len(neighbors[i])>=2, 'unpruned center leaf')
            centers.append(cell)
        elif role=='portal':
            require(len(neighbors[i])==2 and model.locate(p)['kind']=='face', 'bad tree portal')
            portals.append(i)
        else:
            raise ValueError('unknown tree role')
        require(model.locate(p)['component']==selected, 'point outside chosen component')
        if 'cell' in row:
            cell = row['cell']
            require(type(cell) is int and cell in model.incident(p), 'role cell incidence')
    require(sorted(witness_pairs)==model.targets, 'witness coverage')
    require(sorted(centers)==data['retained_cells'] and len(set(centers))==len(centers), 'center census')
    t = len(centers)
    require(t>=1 and len(portals)==t-1, 'portal census')
    require(len(vertices)==2*t-1+k and len(edges)==2*t-2+k, 'spoke tree count')
    leaves = sum(len(n)==1 for n in neighbors)
    require(leaves==k and data['leaves']==leaves, 'leaf census')
    bound = max(3,2*len(model.edges)**2-len(model.edges)+3*len(model.points)*(len(model.points)-1)//2)
    count = 2*len(edges)+leaves
    require(data['B17']==bound and data['tube_corner_bound']==count and count<=bound, 'corner count')
    return {'tree_vertices':len(vertices),'tree_edges':len(edges),'tube_count':count}
