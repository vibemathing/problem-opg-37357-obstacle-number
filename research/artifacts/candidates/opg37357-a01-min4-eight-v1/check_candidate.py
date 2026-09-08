"""Runnable counterplacement and CNF audit without the unpublished incidence core.
The general incidence reconstruction is NOT performed by this entry point.
"""
import json,sys,hashlib
from itertools import combinations,product
from fractions import Fraction as F
from guarded_cnf import generate,dimacs
from clause_audit import check
from witness_check import verify,orient
from structure_audit import rotation,reachable
from matching import build

EDGES=[[0,1],[0,3],[0,6],[0,7],[1,2],[1,3],[1,5],[1,6],[2,4],[2,5],[2,6],[3,4],[3,5],[3,7],[4,5],[4,6],[4,7],[6,7]]
TARGETS=[[0,2],[1,4],[2,7],[3,6],[5,7]]
def main(w,mode='audit'):
    if w['n']!=8 or w['edges']!=EDGES or w['frozen_targets']!=TARGETS:raise ValueError('frozen graph drift')
    d=generate(w)
    if mode=='cnf':return dimacs(d).decode()
    origin=''.join(str(i+1)+'\t'+json.dumps(s,separators=(',',':'))+'\n' for i,s in enumerate(d['origins']))
    if mode=='origins':return origin
    source=check(d);geo=verify(w);p=[tuple(F(x) for x in a) for a in w['points']]
    E=set(map(tuple,EDGES));faces=rotation(8,E,w['rotation']);deletions=0
    for k in range(4):
        for S in combinations(range(8),k):
            if len(reachable(8,E,S))!=8-k:raise ValueError('connectivity')
            deletions+=1
    dirs=[int(orient(p[a],p[b],p[c])>0) for a,b,c in d['triples']];q=len(dirs);k=len(d['targets'])
    residual=[]
    for C in d['clauses']:
        if not any(dirs[abs(v)-1]==(v>0) for v in C if abs(v)<=q):residual.append([v for v in C if abs(v)>q])
    models=[]
    for colors in product((0,1),repeat=k):
        truth=[None]+dirs+list(colors)+[None]*(d['variables']-q-k);ok=True
        for C in residual:
            if any(abs(v)<=q+k and truth[abs(v)]==(v>0) for v in C):continue
            side=[v for v in C if abs(v)>q+k]
            if len(side)!=1:ok=False;break
            v=side[0]
            if truth[abs(v)] is not None and truth[abs(v)]!=(v>0):ok=False;break
            truth[abs(v)]=int(v>0)
        if ok:
            bits=[int(x) if x is not None else 0 for x in truth[1:]]
            if not all(any(bits[abs(v)-1]==(v>0) for v in C) for C in d['clauses']):raise ValueError('model check')
            models.append({'colors':list(colors),'model':[i+1 if b else -i-1 for i,b in enumerate(bits)]})
    if geo['colors'] not in [m['colors'] for m in models]:raise ValueError('actual polygons fail necessary CNF')
    del geo['separators']
    return json.dumps({'verdict':'candidate_only','geometry':geo,'source_check':source,'variables':d['variables'],
        'cnf_sha256':hashlib.sha256(dimacs(d)).hexdigest(),'origins_sha256':hashlib.sha256(origin.encode()).hexdigest(),
        'abstract_faces':faces,'deletion_checks':deletions,'labelings_checked':1<<k,'fixed_direction_models':models,
        'matching_control':build(8,EDGES,[(0,2),(1,4),(3,6)]),
        'full_incidence_rebuilt':False,'scope':'complete polygon witness; all labels at one actual direction table; no all-placement census'},sort_keys=True,separators=(',',':'))+'\n'
if __name__=='__main__':print(main(json.load(sys.stdin),sys.argv[1] if len(sys.argv)>1 else 'audit'),end='')
