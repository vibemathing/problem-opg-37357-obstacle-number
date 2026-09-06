"""Solver-free candidate replay: Boolean clauses and sphere-face certificates.
This is a local checker candidate, not a registered trusted verifier.
"""
from __future__ import annotations
import base64, collections, hashlib, json, pathlib, time, zlib
from two_obstacle import compile_cnf


def digest(b): return hashlib.sha256(b).hexdigest()

def load_data(path):
    raw=path.read_bytes()
    if len(raw)>262144:raise ValueError('manifest byte cap')
    manifest=json.loads(raw)
    if manifest['format']!='opg37357-c10-chunks-v2' or len(manifest['parts'])!=10:
        raise ValueError('manifest format/count')
    payload=[]
    for i,part in enumerate(manifest['parts']):
        name=f'samples-{i:02d}.txt'
        if part['name']!=name:raise ValueError('chunk name')
        data=path.with_name(name).read_bytes()
        if len(data)>600 or len(data)!=part['bytes'] or digest(data)!=part['sha256']:
            raise ValueError('chunk bytes/digest')
        payload.append(data)
    encoded=b''.join(payload)
    if digest(encoded)!=manifest['payload_sha256']:raise ValueError('payload digest')
    compressed=base64.b64decode(encoded,validate=True)
    dec=zlib.decompressobj();body=dec.decompress(compressed,1048577)
    if len(body)>1048576 or dec.unconsumed_tail or dec.unused_data or not dec.eof:
        raise ValueError('compressed frame/budget')
    obj=json.loads(body)
    if obj['format']!='opg37357-c10-selected-models-v1' or len(obj['cases'])>16:
        raise ValueError('data schema/range')
    return obj,digest(raw)


def sphere(graph):
    n=graph['n'];edges={tuple(x) for x in graph['edges']};faces=graph['faces']
    if not 4<=n<=14 or len(edges)!=len(graph['edges']) or any(not 0<=u<v<n for u,v in edges):raise ValueError('simple graph')
    darts=collections.Counter();links={i:{} for i in range(n)};adj={i:set() for i in range(n)}
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    for f in faces:
        if len(f)!=3 or len(set(f))!=3 or any(type(v) is not int or not 0<=v<n for v in f):raise ValueError('triangle')
        for a,b,c in (f,f[1:]+f[:1],f[2:]+f[:2]):
            darts[a,b]+=1
            if a in links[b]:raise ValueError('link duplicate')
            links[b][a]=c
    expected=edges|{(v,u) for u,v in edges}
    if set(darts)!=expected or set(darts.values())!={1}:raise ValueError('oriented edge coverage')
    if n-len(edges)+len(faces)!=2 or len(edges)!=3*n-6:raise ValueError('Euler/triangulation')
    reached={0};queue=[0]
    while queue:
        v=queue.pop()
        for u in adj[v]-reached:reached.add(u);queue.append(u)
    if len(reached)!=n:raise ValueError('disconnected graph')
    for v,link in links.items():
        if set(link)!=adj[v] or set(link.values())!=adj[v]:raise ValueError('link neighbors')
        start=next(iter(link));u=start;seen=set()
        while u not in seen:seen.add(u);u=link[u]
        if u!=start or seen!=adj[v]:raise ValueError('link cycle')
    return n,len(edges),len(faces)


def run(folder):
    start=time.monotonic();data,container_hash=load_data(folder/'samples.txt');out=[]
    for item in data['cases']:
        if time.monotonic()-start>40:raise TimeoutError('replay time budget')
        g=item['graph'];o=item['observation'];sphere(g)
        gb=(json.dumps(g,sort_keys=True,separators=(',',':'))+'\n').encode()
        if digest(gb)!=o['graph_sha256']:raise ValueError('graph digest')
        nv,clauses,meta,colors=compile_cnf(g['n'],g['edges'],o['path_edge_cap'])
        if nv!=o['variables'] or len(clauses)!=o['clauses'] or meta['cnf_sha256']!=o['cnf_sha256']:raise ValueError('formula digest/count')
        bits=base64.b64decode(item['model_little_endian_base64'],validate=True)
        if len(bits)!=(nv+7)//8 or (nv%8 and bits[-1]>>(nv%8)):raise ValueError('model bit length/padding')
        assignment=[i+1 if bits[i//8]>>(i%8)&1 else -(i+1) for i in range(nv)]
        mb=(json.dumps(assignment,separators=(',',':'))+'\n').encode()
        if digest(mb)!=o['model_sha256']:raise ValueError('original model digest')
        values=set(assignment)
        if any(not any(x in values for x in clause) for clause in clauses):raise ValueError('unsatisfied clause')
        out.append({'case':g['case_id'],'n':g['n'],'path_edge_cap':o['path_edge_cap'],'clauses':len(clauses),'boolean_model_valid':True,'sphere_faces_valid':True})
    return {'verdict':'candidate_only','operation':'solver-free Boolean and sphere-certificate replay','cases':out,'total_clauses_replayed':sum(x['clauses'] for x in out),'container_sha256':container_hash,'no_geometric_representation_claim':True}

if __name__=='__main__':
    folder=pathlib.Path(__file__).resolve().parent;result=run(folder)
    folder.joinpath('replay-observation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True))
