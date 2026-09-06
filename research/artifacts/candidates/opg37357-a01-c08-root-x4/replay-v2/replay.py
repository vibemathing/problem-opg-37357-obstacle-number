"""Exact candidate replay: graph planarity + generated CNF + stored RUP.
Uses only Python's standard library and necessary_cnf.py, NOT a SAT solver.
Invocation: python replay.py [--self-test]. Success is not repository admission.
"""
from __future__ import annotations
import base64, bz2, collections, hashlib, itertools, json, pathlib, sys, time
from fractions import Fraction
from necessary_cnf import dimacs, make_graph

class Rejected(ValueError): pass

def require(condition, message):
    if not condition: raise Rejected(message)

def digest(data): return hashlib.sha256(data).hexdigest()

def orient(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def on(a,b,c):
    return orient(a,b,c)==0 and sum((c[i]-a[i])*(c[i]-b[i]) for i in (0,1))<=0
def meet(a,b,c,d):
    return (orient(a,b,c)*orient(a,b,d)<0 and orient(c,d,a)*orient(c,d,b)<0) or on(a,b,c) or on(a,b,d) or on(c,d,a) or on(c,d,b)

def check_plane(graph):
    n,es,fs=make_graph(4)
    require(graph['vertices']==list(range(n)), 'graph vertices')
    require(graph['edges']==[list(e) for e in es], 'graph edge identity')
    require(graph['faces']==[list(f) for f in fs], 'face identity')
    q=[tuple(Fraction(x) for x in p) for p in graph['coordinates']]
    require(len(q)==n and all(len(p)==2 for p in q) and len(set(q))==n,'point identity')
    dart=collections.Counter((f[i],f[(i+1)%3]) for f in fs for i in range(3))
    require(len(fs)==16 and n-len(es)+len(fs)==2,'Euler count')
    require(all(dart[(a,b)]==dart[(b,a)]==1 for a,b in es) and len(dart)==2*len(es),'oriented edge incidence')
    vertex_edge=0;edge_pairs=0
    for a,b in es:
        for c in range(n):
            if c not in (a,b):
                require(not on(q[a],q[b],q[c]),'vertex on nonincident edge');vertex_edge+=1
    for (a,b),(c,d) in itertools.combinations(es,2):
        if len({a,b,c,d})==4:
            require(not meet(q[a],q[b],q[c],q[d]),'crossing or contacting disjoint edges');edge_pairs+=1
    return {'vertices':n,'edges':len(es),'faces':len(fs),'vertex_edge_tests':vertex_edge,'disjoint_edge_tests':edge_pairs}

class RUP:
    def __init__(self,n,clauses):
        self.n=n;self.cs=[];self.occ=collections.defaultdict(list);self.units=[];self.empty=False
        for c in clauses:self.add(c)
    def validate(self,c):
        require(all(type(l)is int and 0<abs(l)<=self.n for l in c),'literal out of range')
        require(len(set(c))==len(c) and not any(-l in c for l in c),'noncanonical clause')
    def add(self,c):
        self.validate(c);c=tuple(c);i=len(self.cs);self.cs.append(c)
        for l in c:self.occ[l].append(i)
        if len(c)==1:self.units.append(c[0])
        if not c:self.empty=True
    def conflicts(self,assumptions):
        if self.empty:return True
        values={};queue=collections.deque(self.units);queue.extend(assumptions);sat=set();falses={}
        while queue:
            l=queue.popleft();v=abs(l);sign=l>0
            if v in values:
                if values[v]!=sign:return True
                continue
            values[v]=sign
            for i in self.occ.get(l,()):sat.add(i)
            for i in self.occ.get(-l,()):
                if i in sat:continue
                k=falses.get(i,0)+1;falses[i]=k;row=self.cs[i];remaining=len(row)-k
                if remaining==0:return True
                if remaining==1:
                    for other in row:
                        if abs(other) not in values:queue.append(other);break
                    else:raise Rejected('unit-state invariant')
        return False
    def step(self,c):
        self.validate(c)
        if not self.conflicts([-l for l in c]):return False
        self.add(c);return True

def check_proof(n,clauses,proof,timeout=55):
    require(len(proof)<=100000,'proof byte cap');engine=RUP(n,clauses);start=time.monotonic();closed=False;steps=0
    for line in proof.decode('ascii').splitlines():
        require(not closed,'data after empty clause');require(time.monotonic()-start<timeout,'replay timeout')
        words=line.split();require(words and words[-1]=='0','proof syntax');c=tuple(map(int,words[:-1]))
        require(engine.step(c),f'not RUP at step {steps+1}');steps+=1;closed=not c
    require(closed,'missing final empty clause');return steps

def self_test():
    clauses=[]
    for signs in itertools.product((-1,0,1),repeat=3):
        clauses.append(tuple((i+1)*s for i,s in enumerate(signs) if s))
    trials=0
    for f in itertools.combinations_with_replacement(clauses,2):
        for c in clauses:
            engine=RUP(3,f);accepted=engine.conflicts([-l for l in c])
            if accepted:
                for assignment in itertools.product((False,True),repeat=3):
                    sat=lambda row:any(assignment[abs(l)-1]==(l>0) for l in row)
                    require(not all(sat(row) for row in f) or sat(c),'truth-table soundness failure')
            trials+=1
    for bad in (b'',b'1 0\n',b'4 0\n0\n',b'0\n0\n'):
        try:check_proof(3,[(1,2)],bad,1)
        except Rejected:pass
        else:raise Rejected('negative regression unexpectedly accepted')
    return {'truth_table_cases':trials,'negative_cases':4}

def main():
    base=pathlib.Path(__file__).resolve().parent;raw=(base/'certificate.json').read_bytes();require(len(raw)<40000,'package cap');d=json.loads(raw)
    require(d['format']=='opg37357-x4-rup-package-v2' and d['r']==4 and d['max_path_edges']==4,'package scope')
    plane=check_plane(d['graph']);data,info=dimacs(4,4);require(digest(data)==d['cnf_sha256'],'generated CNF digest');require(info['variables']==d['variables'] and len(info['clauses'])==d['clauses'],'CNF dimensions')
    encoded=''.join(d['proof_base64']);require(len(encoded)<30000,'encoded cap');packed=base64.b64decode(encoded,validate=True)
    decoder=bz2.BZ2Decompressor();proof=decoder.decompress(packed,max_length=100001)
    require(decoder.eof and not decoder.unused_data and len(proof)<=100000,'compressed stream invalid or over cap')
    require(len(proof)==d['proof_bytes'] and digest(proof)==d['proof_sha256'],'proof digest')
    steps=check_proof(info['variables'],info['clauses'],proof);require(steps==d['proof_additions'],'proof step count')
    report={'verdict':'candidate_only','scope':'exact propositional and planarity replay, not trusted admission','planarity':plane,'variables':info['variables'],'clauses':len(info['clauses']),'RUP_additions':steps,'cnf_sha256':digest(data),'proof_sha256':digest(proof),'python':sys.version.split()[0]}
    if '--self-test' in sys.argv:report['checker_regressions']=self_test()
    print(json.dumps(report,sort_keys=True))
if __name__=='__main__':
    try:main()
    except (Rejected,ValueError,KeyError,TypeError,OSError,EOFError) as e:
        print(json.dumps({'verdict':'candidate_only','status':'REJECT_OR_REFUSE','reason':str(e)}));raise SystemExit(1)
