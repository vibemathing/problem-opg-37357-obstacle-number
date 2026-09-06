"""Candidate exact RUP replay, deliberately separate from the CDCL producer.
This checker uses occurrence counts, no watched literals or conflict analysis.
Successful replay establishes a propositional certificate only; no admission role.
"""
from collections import deque
import argparse, hashlib, json, time
from pathlib import Path

class BadProof(ValueError): pass

def read_cnf(path):
    raw=Path(path).read_bytes()
    if len(raw)>6000000: raise BadProof('input size refusal')
    clauses=[];n=m=None;pending=[]
    for line in raw.decode('ascii').splitlines():
        if not line or line.startswith('c'):continue
        if line.startswith('p '):
            if n is not None:raise BadProof('duplicate header')
            p,kind,ns,ms=line.split();n,m=int(ns),int(ms)
            if kind!='cnf' or not 1<=n<=5000 or not 1<=m<=200000:raise BadProof('dimensions refused')
            continue
        if n is None:raise BadProof('missing header')
        for word in line.split():
            l=int(word)
            if l==0:
                if len(pending)!=len(set(pending)) or any(-z in pending for z in pending):raise BadProof('noncanonical clause')
                clauses.append(tuple(pending));pending=[]
            elif abs(l)>n:raise BadProof('out of range')
            else:pending.append(l)
    if pending or n is None or len(clauses)!=m:raise BadProof('malformed CNF')
    return n,clauses,hashlib.sha256(raw).hexdigest()

class Replay:
    def __init__(self,n,clauses):
        self.n=n;self.cs=[];self.occ={l:[] for v in range(1,n+1) for l in (v,-v)};self.units=[];self.empty=False
        for c in clauses:self.add(c)
    def add(self,c):
        i=len(self.cs);self.cs.append(c)
        if len(c)==0:self.empty=True
        if len(c)==1:self.units.append(c[0])
        for l in c:self.occ[l].append(i)
    def rup(self,c):
        if self.empty:return True
        values=[0]*(self.n+1);false_count=[0]*len(self.cs);queue=deque()
        def force(l):
            v=abs(l);s=1 if l>0 else -1
            if values[v]:return values[v]==s
            values[v]=s;queue.append(l);return True
        for l in (*self.units,*(-z for z in c)):
            if not force(l):return True
        while queue:
            l=queue.popleft()
            for i in self.occ[-l]:
                false_count[i]+=1;row=self.cs[i]
                if false_count[i]==len(row):return True
                if false_count[i]==len(row)-1:
                    # Exactly one literal is not yet known false. It may already be true.
                    for z in row:
                        v=values[abs(z)];sign=1 if z>0 else -1
                        if v!= -sign:
                            if not force(z):return True
                            break
        return False

def check(cnf_path,proof_path):
    begin=time.monotonic();n,cs,cnf_sha=read_cnf(cnf_path);engine=Replay(n,cs)
    data=Path(proof_path).read_bytes()
    if len(data)>6000000:raise BadProof('proof size refusal')
    lines=data.decode('ascii').splitlines();closed=False;steps=0
    for k,line in enumerate(lines,1):
        if time.monotonic()-begin>55:raise BadProof('replay timeout')
        if closed:raise BadProof('data after final empty clause')
        words=line.split()
        if not words or words[-1]!='0':raise BadProof(f'malformed step {k}')
        row=tuple(map(int,words[:-1]))
        if any(l==0 or abs(l)>n for l in row) or len(set(row))!=len(row) or any(-l in row for l in row):raise BadProof(f'invalid literals step {k}')
        if not engine.rup(row):raise BadProof(f'not RUP at step {k}')
        engine.add(row);steps+=1;closed=(len(row)==0)
    if not closed:raise BadProof('missing final empty clause')
    return {'status':'RUP_REPLAY_PASS','input_variables':n,'input_clauses':len(cs),'proof_additions':steps,'cnf_sha256':cnf_sha,'proof_sha256':hashlib.sha256(data).hexdigest(),'seconds':time.monotonic()-begin,'scope':'propositional replay by candidate-generated checker; not trusted admission'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('cnf');ap.add_argument('proof');args=ap.parse_args()
    try:print(json.dumps(check(args.cnf,args.proof),sort_keys=True))
    except (BadProof,OSError,UnicodeError,ValueError) as e:
        print(json.dumps({'status':'REPLAY_REJECT_OR_REFUSE','message':str(e)}));return 1
    return 0
if __name__=='__main__':raise SystemExit(main())
