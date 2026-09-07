"""C22 bounded local-data replay of the existing C08 X4 certificate.
Usage: python replay.py C08_CERTIFICATE_JSON [--emit-hints]
No network, process launch, dynamic import/evaluation, or file writes.
"""
import base64
import bz2
import copy
import hashlib
import json
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import platform
import sys
import time
from root_cnf import graph, compile_cnf, dimacs
from rup_hints import parse_rup, produce
from trim_hints import trim
from hint_check import ensure, verify

SOURCE = 'b4668771fd98f902ebc6c8fc73e7db2a6a5c103660ccfed6e20c442f73505dc5'
PACKAGE = '440c92278e01888c19bbb341958eca1320da6f28362d66343d0eb3e8e8cce697'
PROOF = '9d16206d67cb450cbaaa4920fe83a5d463584a612f29367e0f2da4a8acd6ec5e'
CNF = 'de54d35f78d3c7d84e24651e5ce6f82c9ebe6d78bc7bd2deb66aa591e6ea276c'
HINTS = 'f9a6f8e4369c456f014974656b17944e4946401e6a20ec7350e6646efd71adb2'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def unique(items):
    result = {}
    for k,v in items:
        ensure(k not in result,'duplicate JSON key')
        result[k] = v
    return result


def load(path):
    with Path(path).open('rb') as stream:
        raw = stream.read(40001)
    ensure(len(raw)<=40000 and digest(raw)==SOURCE,'frozen source package hash')
    # The exact pre-existing C08 transport correction is pinned on both sides.
    ensure(raw.count(b'BJd6Q')==1,'unique recorded text delta')
    raw = raw.replace(b'BJd6Q',b'BJd6FQ')
    ensure(digest(raw)==PACKAGE,'corrected package hash')
    package = json.loads(raw,object_pairs_hook=unique)
    compressed = base64.b64decode(''.join(package['proof_base64']),validate=True)
    decoder = bz2.BZ2Decompressor()
    proof = decoder.decompress(compressed,max_length=100001)
    ensure(decoder.eof and not decoder.unused_data,'incomplete/trailing compressed data')
    ensure(len(proof)==60632 and digest(proof)==PROOF,'decoded RUP hash')
    return package,proof


def orient(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def on(q,a,b):
    return orient(a,b,q)==0 and sum((q[j]-a[j])*(q[j]-b[j]) for j in (0,1))<=0


def intersect(a,b,c,d):
    return (orient(a,b,c)*orient(a,b,d)<0 and orient(c,d,a)*orient(c,d,b)<0
            or on(a,c,d) or on(b,c,d) or on(c,a,b) or on(d,a,b))


def plane_check(cert):
    edges,faces = graph()
    ensure(cert['edges']==[list(e) for e in edges],'graph edge identity')
    ensure(cert['faces']==[list(f) for f in faces],'face identity')
    points = [tuple(F(v) for v in p) for p in cert['coordinates']]
    ensure(len(points)==len(set(points))==10,'planarity points')
    vertex_tests = edge_tests = 0
    for a,b in edges:
        for v in range(10):
            if v not in (a,b):
                ensure(not on(points[v],points[a],points[b]),'vertex-edge contact')
                vertex_tests += 1
    for (a,b),(c,d) in combinations(edges,2):
        if len({a,b,c,d})==4:
            ensure(not intersect(points[a],points[b],points[c],points[d]),'edge crossing/contact')
            edge_tests += 1
    neighborhoods = [{v if u==a else a for a,v in edges if u in (a,v)} for u in range(10)]
    ensure(all(neighborhoods),'isolated vertex would require a separate exclusion argument')
    ensure(all(neighborhoods[u]|{u} != neighborhoods[v]|{v} for u,v in combinations(range(10),2)),
           'true twin exception to injectivity argument')
    return {'vertex_edge_tests':vertex_tests,'disjoint_edge_tests':edge_tests,
            'minimum_degree':min(map(len,neighborhoods)),'true_twins':False}


def regressions():
    clauses = [tuple((i+1)*s for i,s in enumerate(signs) if s)
               for signs in product((-1,0,1),repeat=2) if any(signs)]
    accepted = 0
    for mask in range(1<<len(clauses)):
        initial = [c for i,c in enumerate(clauses) if mask>>i&1]
        try:
            rows = produce(2,initial,[()])
        except ValueError:
            continue
        ensure(verify(2,initial,rows)['accepted'],'small replay')
        satisfiable = any(all(any(bits[abs(lit)-1]==(lit>0) for lit in c)
                             for c in initial) for bits in product((False,True),repeat=2))
        ensure(not satisfiable,'accepted satisfiable small formula')
        accepted += 1
    # Small contradictory source; mutations are tested without a huge recompile.
    initial = [(1,),(-1,2),(-2,)]
    rows = produce(2,initial,[()])
    changes = [
        ('future_reason',lambda r:r[0][2].__setitem__(0,4)),
        ('zero_reason',lambda r:r[0][2].__setitem__(0,0)),
        ('bool_reason',lambda r:r[0][2].__setitem__(0,True)),
        ('no_reasons',lambda r:r[0].__setitem__(2,[])),
        ('nonfresh_id',lambda r:r[0].__setitem__(0,3)),
        ('bool_clause',lambda r:r[0].__setitem__(1,[True])),
        ('range_clause',lambda r:r[0].__setitem__(1,[3])),
        ('duplicate_clause_literal',lambda r:r[0].__setitem__(1,[1,1])),
        ('tautology',lambda r:r[0].__setitem__(1,[1,-1])),
        ('missing_conflict',lambda r:r[0][2].pop()),
        ('after_conflict',lambda r:r[0][2].append(1)),
        ('nonempty_final',lambda r:r.append([5,[1],[1]])),
    ]
    rejected = []
    for name,change in changes:
        altered = copy.deepcopy(rows);change(altered)
        try:
            verify(2,initial,altered)
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError('accepted damaged trace '+name)
    return {'two_variable_formulas':256,'unit_refutable_accepted':accepted,
            'rejected_trace_mutations':rejected}


def main(path, emit=False):
    started = time.monotonic()
    package,proof = load(path)
    variables,clauses,counts = compile_cnf()
    ensure(digest(dimacs(variables,clauses))==CNF,'recompiled necessary formula hash')
    rows = trim(clauses,produce(variables,clauses,parse_rup(proof,variables)))
    trace = (json.dumps(rows,separators=(',',':'))+'\n').encode('ascii')
    ensure(len(trace)<1000000 and digest(trace)==HINTS,'deterministic reason trace hash')
    result = verify(variables,clauses,rows)
    if emit:
        return trace.decode('ascii').rstrip('\n')
    result.update({'verdict':'candidate_only','trusted_verifier_receipt':False,
        'python':platform.python_version(),'implementation':platform.python_implementation(),
        'source_package_sha256':SOURCE,'decoded_proof_sha256':PROOF,'cnf_sha256':CNF,
        'trace_sha256':HINTS,'trace_bytes':len(trace),'variables':variables,
        'clauses':len(clauses),'blocks_and_paths':counts,
        'planarity':plane_check(package['graph']),'regressions':regressions()})
    result['elapsed_seconds'] = round(time.monotonic()-started,6)
    return json.dumps(result,sort_keys=True,separators=(',',':'))


if __name__=='__main__':
    ensure(len(sys.argv) in (2,3) and (len(sys.argv)==2 or sys.argv[2]=='--emit-hints'),
           'provide C08 certificate path and optional --emit-hints')
    print(main(sys.argv[1],len(sys.argv)==3))
