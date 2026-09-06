"""Candidate-only induced-triangulation construction and bounded atlas audit.
No obstacle-number solver or trusted verification is invoked.
"""
from __future__ import annotations
import argparse, collections, hashlib, itertools, json, sys, time
import networkx as nx


def edge(u, v):
    return (min(u, v), max(u, v))


def cycles3(g):
    return {tuple(sorted((u, v, w))) for u in g for v in g[u]
            if u < v for w in g[v] if v < w and g.has_edge(w, u)}


def face_list(emb):
    seen = set(); result = []
    for u in sorted(emb):
        for v in sorted(emb[u]):
            if (u, v) not in seen:
                result.append(emb.traverse_face(u, v, seen))
    return result


def extend(g):
    """Return H containing G induced, and a spherical triangular-face certificate."""
    n = len(g)
    if not 3 <= n <= 32 or set(g) != set(range(n)) or g.is_directed() or g.is_multigraph():
        raise ValueError('require a simple graph labeled 0..n-1 with 3<=n<=32')
    if nx.number_of_selfloops(g) or not nx.check_planarity(g)[0]:
        raise ValueError('require a loopless planar graph')
    original = {edge(u, v) for u, v in g.edges()}
    t = g.copy()
    for u, v in itertools.combinations(range(n), 2):
        if not t.has_edge(u, v):
            t.add_edge(u, v)
            if not nx.check_planarity(t)[0]:
                t.remove_edge(u, v)
    if t.number_of_edges() != 3*n-6:
        raise AssertionError('maximal augmentation edge count')
    ok, emb = nx.check_planarity(t)
    faces = face_list(emb)
    if not ok or len(faces) != 2*n-4 or any(len(f) != 3 for f in faces):
        raise AssertionError('augmentation triangulation')
    added = sorted({edge(u, v) for u, v in t.edges()} - original)
    mid = {e:n+i for i, e in enumerate(added)}
    h = nx.Graph(); h.add_nodes_from(range(n+len(added)))
    for u, v in t.edges():
        m = mid.get(edge(u, v))
        h.add_edges_from([(u, v)] if m is None else [(u, m), (m, v)])
    output_faces = []; affected = 0
    for f in faces:
        boundary = []
        for u, v in zip(f, f[1:]+f[:1]):
            boundary.append(u)
            if edge(u, v) in mid:
                boundary.append(mid[edge(u, v)])
        if len(boundary) == 3:
            output_faces.append(boundary)
        else:
            z = len(h); h.add_node(z); affected += 1
            h.add_edges_from((z, u) for u in boundary)
            output_faces.extend([[z, u, v] for u, v in zip(boundary, boundary[1:]+boundary[:1])])
    return h, {'old_n':n, 'old_edges':sorted(original), 'added_edges':added,
               'base_faces':faces, 'faces':output_faces, 'affected_faces':affected}


def audit(g, h, cert):
    n = len(g); N = len(h); e = g.number_of_edges()
    if {edge(u,v) for u,v in h.subgraph(range(n)).edges()} != {edge(u,v) for u,v in g.edges()}:
        raise AssertionError('old induced graph changed')
    M = 3*n-6-e; t = cert['affected_faces']
    if N != n+M+t or t > min(2*M, 2*n-4) or N > 6*n-e-10:
        raise AssertionError('vertex count')
    if h.number_of_edges() != 3*N-6 or not nx.check_planarity(h)[0]:
        raise AssertionError('output maximal planarity')
    fs = cert['faces']; darts = collections.Counter(); links = {v:{} for v in h}
    for f in fs:
        if len(f) != 3 or len(set(f)) != 3: raise AssertionError('face degeneracy')
        for a,b,c in (f, f[1:]+f[:1], f[2:]+f[:2]):
            darts[a,b] += 1
            if a in links[b]: raise AssertionError('duplicate link incidence')
            links[b][a] = c
    expected = {(a,b) for a,b in h.edges()} | {(b,a) for a,b in h.edges()}
    if set(darts) != expected or set(darts.values()) != {1} or N-h.number_of_edges()+len(fs) != 2:
        raise AssertionError('sphere darts/Euler')
    for v, link in links.items():
        if set(link) != set(h[v]) or set(link.values()) != set(h[v]): raise AssertionError('link domain')
        start = next(iter(link)); cur = start; seen = set()
        while cur not in seen:
            seen.add(cur); cur = link[cur]
        if cur != start or seen != set(link): raise AssertionError('noncircular vertex link')
    triangles = cycles3(h); old = cycles3(g); facial = {tuple(sorted(f)) for f in fs}
    if not triangles-old <= facial or not old <= triangles:
        raise AssertionError('new nonfacial triangle')
    old_base_facial = {tuple(sorted(f)) for f in cert['base_faces']} & old
    if (triangles-facial) != (old-old_base_facial):
        raise AssertionError('separating-triangle correspondence')
    return {'n':n, 'e':e, 'new_n':N, 'M':M, 't':t,
            'triangle_free_input':not old, 'nonfacial_triangles':len(triangles-facial)}


def run(max_order=7, timeout=40):
    start = time.monotonic(); rows = []; representative = {}; by_order=collections.Counter()
    for index,g in enumerate(nx.graph_atlas_g()):
        if time.monotonic()-start > timeout: raise TimeoutError('atlas audit budget')
        if not 3 <= len(g) <= max_order or not nx.check_planarity(g)[0]: continue
        h,c = extend(g); r = audit(g,h,c); r['atlas_index']=index
        rows.append(r); by_order[len(g)] += 1
        if len(g)==3 or (len(g)==5 and g.number_of_edges()==9):
            representative[str(index)]={'input_edges':sorted(map(list,g.edges())),
                'H_edges':sorted(map(list,h.edges())), 'certificate':c}
    # An explicit minimum-degree connectivity audit for three triangle-free samples.
    connectivity = []
    for name,g in [('P3',nx.path_graph(3)),('C5',nx.cycle_graph(5)),('K23',nx.complete_bipartite_graph(2,3))]:
        h,c = extend(g); audit(g,h,c); k=nx.node_connectivity(h)
        if k < 4: raise AssertionError('triangle-free 4-connectivity regression')
        connectivity.append({'input':name,'H_n':len(h),'connectivity':k})
    canonical = (json.dumps(rows,sort_keys=True,separators=(',',':'))+'\n').encode()
    report = {'verdict':'candidate_only','scope':'induced triangulation regression; no obstacle SAT/UNSAT',
        'python':sys.version.split()[0],'networkx':nx.__version__,'max_input_order':max_order,
        'planar_graphs_checked':len(rows),'counts_by_order':dict(sorted(by_order.items())),
        'triangle_free_inputs':sum(r['triangle_free_input'] for r in rows),
        'largest_output_order':max(r['new_n'] for r in rows),
        'row_sha256':hashlib.sha256(canonical).hexdigest(),'connectivity_regressions':connectivity}
    return report, representative

if __name__ == '__main__':
    p=argparse.ArgumentParser();p.add_argument('--max-order',type=int,choices=range(3,8),default=7)
    p.add_argument('--save',action='store_true');a=p.parse_args()
    report, examples=run(a.max_order)
    if a.save:
        from pathlib import Path
        folder=Path(__file__).resolve().parent
        folder.joinpath('atlas-observation.json').write_text(json.dumps(report,indent=2)+'\n')
        folder.joinpath('examples.json').write_text(json.dumps(examples,separators=(',',':'))+'\n')
    print(json.dumps(report,sort_keys=True))
