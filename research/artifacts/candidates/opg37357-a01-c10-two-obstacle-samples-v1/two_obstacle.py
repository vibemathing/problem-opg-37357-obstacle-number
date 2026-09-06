"""Candidate two-obstacle necessary-condition search, not a geometric verifier.
Finite limits: n<=14, path edges<=4, <=220000 clauses, Z3 timeout<=10000 ms.
Uses the same orientation/key-path necessity as c08, gated by blocker labels.
"""
from __future__ import annotations
import argparse, ctypes as C, ctypes.util, functools, hashlib, itertools as I
import json, pathlib, resource, sys, time

class Budget(RuntimeError): pass

def h(data): return hashlib.sha256(data).hexdigest()
def ordered(ls): return tuple(sorted(set(ls),key=lambda x:(abs(x),x)))

def xr(r):
    if not 3<=r<=6: raise ValueError('r budget')
    a=lambda i:2+i%r; b=lambda i:2+r+i%r
    es=set();fs=[]
    for i in range(r):
        es.update(tuple(sorted(x)) for x in [(0,a(i)),(1,b(i)),(a(i),a(i+1)),(b(i),b(i+1)),(a(i),b(i)),(a(i+1),b(i))])
        fs += [[0,a(i),a(i+1)],[1,b(i+1),b(i)],[a(i),b(i),a(i+1)],[a(i+1),b(i),b(i+1)]]
    return 2*r+2,sorted(es),fs

@functools.lru_cache(maxsize=2)
def orientations(n):
    tr={t:i+1 for i,t in enumerate(I.combinations(range(n),3))}
    def x(a,b,c):
        t=(a,b,c);return tr[tuple(sorted(t))]*(-1 if sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))%2 else 1)
    cs=set()
    def add(ls):
        s=set(ls)
        if not any(-z in s for z in s):cs.add(ordered(s))
    for a,b,c,d in I.permutations(range(n),4):add([-x(a,b,c),-x(a,c,d),-x(a,d,b),x(b,c,d)])
    n4=len(cs)
    for a,b,c,d,e in I.permutations(range(n),5):
        p=[-x(a,b,c),-x(a,c,d),-x(a,d,e),-x(a,b,e)]
        add(p+[x(a,b,d),-x(a,c,e)]);add(p+[-x(a,b,d),x(a,c,e)])
    return tr,frozenset(cs),n4

def compile_cnf(n,edges,L=4,same_color=False,cap=220000):
    if type(n) is not int or not 4<=n<=14 or type(L) is not int or not 2<=L<=4:raise ValueError('input range')
    if len(edges)!=len(set(map(tuple,edges))) or any(not 0<=u<v<n for u,v in edges):raise ValueError('canonical simple edges')
    start=time.monotonic();tr,base,n4=orientations(n)
    def x(a,b,c):
        t=(a,b,c);return tr[tuple(sorted(t))]*(-1 if sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))%2 else 1)
    E=set(map(tuple,edges));ne=[p for p in I.combinations(range(n),2) if p not in E];adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    for row in adj:row.sort()
    colors={p:len(tr)+1+i for i,p in enumerate(ne)};nextv=len(tr)+len(ne)+1;cs=set(base);paths_count=0
    def add(ls):
        s=set(ls)
        if any(-z in s for z in s):return
        cs.add(ordered(s))
        if len(cs)>cap:raise Budget('clause cap; no formula conclusion')
    if ne:add([-colors[ne[0]]])  # Rename obstacle colors, not graph vertices.
    if same_color:
        for p in ne:add([-colors[p]])
    color_units=len(cs)-len(base)
    def paths(a,b):
        def rec(p):
            if len(p)-1==L:return
            for v in adj[p[-1]]:
                if v in p:continue
                if v==b:yield p+[v]
                else:yield from rec(p+[v])
        return list(rec([a]))
    for a,b in ne:
        if time.monotonic()-start>25:raise Budget('formula compilation time cap')
        ps=paths(a,b);paths_count+=len(ps)
        for c,d in ne:
            if (a,b)==(c,d):continue
            s=nextv;nextv+=1;u=colors[a,b];v=colors[c,d]
            for p in ps:
                cd=[x(c,d,z) for z in p if z not in (c,d)];ab=[x(a,b,z) for z in p[1:-1]]
                for side in (cd,[-z for z in cd]):
                    for clause in (side+[-s]+ab,side+[s]+[-z for z in ab]):
                        # Equal colors make one guard false; different colors disable both.
                        add([u,v]+clause);add([-u,-v]+clause)
    cs=sorted(cs);data=(f'p cnf {nextv-1} {len(cs)}\n'+'\n'.join(' '.join(map(str,c))+' 0' for c in cs)+'\n').encode()
    return nextv-1,cs,{'orientation_variables':len(tr),'color_variables':len(ne),'side_variables':len(ne)*(len(ne)-1),'four_clauses':n4,'five_clauses':len(base)-n4,'color_units':color_units,'key_clauses':len(cs)-len(base)-color_units,'path_count':paths_count,'cnf_sha256':h(data),'cnf_bytes':len(data)},colors

class Solver:
    def __init__(self,ms):
        name=ctypes.util.find_library('z3')
        if not name:raise RuntimeError('Z3 C library unavailable')
        self.z=C.CDLL(name);P=C.c_void_p;S=C.c_char_p
        sig={'Z3_get_full_version':(S,[]),'Z3_mk_config':(P,[]),'Z3_set_param_value':(None,[P,S,S]),'Z3_del_config':(None,[P]),'Z3_mk_context':(P,[P]),'Z3_del_context':(None,[P]),'Z3_mk_simple_solver':(P,[P]),'Z3_solver_inc_ref':(None,[P,P]),'Z3_solver_from_string':(None,[P,P,S]),'Z3_solver_check':(C.c_int,[P,P]),'Z3_solver_get_model':(P,[P,P]),'Z3_model_inc_ref':(None,[P,P]),'Z3_mk_string_symbol':(P,[P,S]),'Z3_mk_bool_sort':(P,[P]),'Z3_mk_const':(P,[P,P,P]),'Z3_model_eval':(C.c_bool,[P,P,P,C.c_bool,C.POINTER(P)]),'Z3_get_bool_value':(C.c_int,[P,P]),'Z3_solver_get_proof':(P,[P,P]),'Z3_ast_to_string':(S,[P,P]),'Z3_solver_get_reason_unknown':(S,[P,P])}
        for k,(r,a) in sig.items():f=getattr(self.z,k);f.restype=r;f.argtypes=a
        cfg=self.z.Z3_mk_config();self.z.Z3_set_param_value(cfg,b'proof',b'true');self.z.Z3_set_param_value(cfg,b'timeout',str(ms).encode());self.ctx=self.z.Z3_mk_context(cfg);self.z.Z3_del_config(cfg);self.s=self.z.Z3_mk_simple_solver(self.ctx);self.z.Z3_solver_inc_ref(self.ctx,self.s)
    def run(self,nv,cs):
        script='\n'.join([f'(declare-const v{i} Bool)' for i in range(1,nv+1)]+['(assert (or '+' '.join(f'v{x}' if x>0 else f'(not v{-x})' for x in c)+'))' for c in cs])
        self.z.Z3_solver_from_string(self.ctx,self.s,script.encode());t=time.monotonic();r=self.z.Z3_solver_check(self.ctx,self.s)
        out={'z3_version':self.z.Z3_get_full_version().decode(),'solver_seconds':time.monotonic()-t}
        if r==1:
            model=self.z.Z3_solver_get_model(self.ctx,self.s);self.z.Z3_model_inc_ref(self.ctx,model);sort=self.z.Z3_mk_bool_sort(self.ctx);assignment=[]
            for i in range(1,nv+1):
                sym=self.z.Z3_mk_string_symbol(self.ctx,f'v{i}'.encode());var=self.z.Z3_mk_const(self.ctx,sym,sort);value=C.c_void_p()
                if not self.z.Z3_model_eval(self.ctx,model,var,True,C.byref(value)):raise RuntimeError('model eval failed')
                b=self.z.Z3_get_bool_value(self.ctx,value)
                if b not in (-1,1):raise RuntimeError('nonBoolean model')
                assignment.append(i if b==1 else -i)
            vals=set(assignment)
            if any(not any(x in vals for x in c) for c in cs):raise AssertionError('exact clause model replay failed')
            out.update(status='relaxed_boolean_sat',assignment=assignment,all_clauses_replayed=True)
        elif r==-1:
            pr=self.z.Z3_solver_get_proof(self.ctx,self.s)
            if not pr:raise RuntimeError('UNSAT without returned proof')
            proof=self.z.Z3_ast_to_string(self.ctx,pr).decode()
            out.update(status='unsat_proof_generated_not_checked',proof_text=proof,proof_sha256=h(proof.encode()))
        else:out.update(status='unknown',reason=self.z.Z3_solver_get_reason_unknown(self.ctx,self.s).decode())
        return out
    def close(self):self.z.Z3_del_context(self.ctx)

def graph_case(r,flip_index=None):
    n,es,fs=xr(r);changes=[]
    if flip_index is not None:
        edge_set=set(es);valid=[]
        for u,v in es:
            ff=[f for f in fs if u in f and v in f]
            a=next(x for x in ff[0] if x not in (u,v));b=next(x for x in ff[1] if x not in (u,v));diagonal=tuple(sorted((a,b)))
            if diagonal not in edge_set:valid.append((u,v,a,b,ff))
        u,v,a,b,ff=valid[flip_index%len(valid)];edge_set.remove((u,v));edge_set.add(tuple(sorted((a,b))));es=sorted(edge_set)
        # Recompute a consistent oriented embedding only for the certificate, not for visibility constraints.
        import networkx as nx
        g=nx.Graph();g.add_nodes_from(range(n));g.add_edges_from(es);ok,emb=nx.check_planarity(g)
        if not ok:raise AssertionError('flip lost planarity')
        seen=set();fs=[emb.traverse_face(x,y,seen) for x in range(n) for y in sorted(g[x]) if (x,y) not in seen]
        changes=[{'remove':[u,v],'add':sorted((a,b))}]
    return {'case_id':f'X{r}'+('' if flip_index is None else f'-flip{flip_index}'),'n':n,'edges':[list(x) for x in es],'faces':fs,'flips':changes}

def do_case(r,flip,L,ms,same,out):
    import networkx as nx
    spec=graph_case(r,flip);g=nx.Graph();g.add_nodes_from(range(spec['n']));g.add_edges_from(spec['edges'])
    if not nx.check_planarity(g)[0] or any(len(f)!=3 for f in spec['faces']):raise AssertionError('input planarity/face check')
    folder=pathlib.Path(out);folder.mkdir(parents=True,exist_ok=True)
    graph_bytes=(json.dumps(spec,sort_keys=True,separators=(',',':'))+'\n').encode();(folder/'graph.json').write_bytes(graph_bytes)
    row={'verdict':'candidate_only','case_id':spec['case_id'],'n':spec['n'],'e':g.number_of_edges(),'minimum_degree':min(dict(g.degree()).values()),'python':sys.version.split()[0],'networkx':nx.__version__,'path_edge_cap':L,'solver_timeout_ms':ms,'same_color_control':same,'graph_sha256':h(graph_bytes)}
    try:
        nv,cs,meta,colors=compile_cnf(spec['n'],spec['edges'],L,same);row.update(meta,variables=nv,clauses=len(cs));print('compiled',row['case_id'],nv,len(cs),flush=True)
        solver=Solver(ms)
        try:res=solver.run(nv,cs)
        finally:solver.close()
        if 'assignment' in res:
            model=res.pop('assignment');mb=(json.dumps(model,separators=(',',':'))+'\n').encode();(folder/'boolean-model.json').write_bytes(mb);res['model_sha256']=h(mb)
            vals=set(model);res['color_class_sizes']=[sum((-v if i==0 else v) in vals for v in colors.values()) for i in (0,1)]
        if 'proof_text' in res:(folder/'unchecked-z3-proof.txt').write_text(res.pop('proof_text'))
        row.update(res)
    except Budget as exc:row.update(status='resource_refusal',reason=str(exc))
    (folder/'observation.json').write_text(json.dumps(row,indent=2)+'\n');print(json.dumps(row,sort_keys=True),flush=True)

if __name__=='__main__':
    resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
    p=argparse.ArgumentParser();p.add_argument('r',type=int,choices=range(3,7));p.add_argument('--flip',type=int);p.add_argument('--length',type=int,choices=range(2,5),default=4);p.add_argument('--timeout-ms',type=int,default=5000);p.add_argument('--same-color',action='store_true');p.add_argument('--out',required=True);a=p.parse_args()
    if not 1<=a.timeout_ms<=10000:raise SystemExit('timeout budget')
    do_case(a.r,a.flip,a.length,a.timeout_ms,a.same_color,a.out)
