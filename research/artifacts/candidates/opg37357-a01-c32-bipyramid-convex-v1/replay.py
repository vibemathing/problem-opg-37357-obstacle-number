"""Bipyramid candidate replay using existing C31 CNF/polygon and C27 fiber code.
Inputs are generated in memory. CLI writes bounded JSON or DIMACS to stdout.
"""
from fractions import Fraction as Q
from itertools import combinations,product
from copy import deepcopy
import hashlib,json,sys
from witness_check import require,verify,cross
from guarded_cnf import build,check_origins,fixed_color_models,check_model,dimacs
from fiber import Fiber,jsonable
from bipyramid import construct,check


def dump(v):return json.dumps(v,sort_keys=True,separators=(',',':'))+'\n'


def core_audit(inc,c):
    k=len(inc);cores=[]
    for size in range(1,k+1):
        for ids in combinations(range(k),size):
            if any(set(a)<=set(ids) for a in cores):continue
            common=set(range(c))
            for i in ids:common&=set(inc[i])
            if not common:cores.append(ids)
    return cores


def selector_audit(cnf,inc,c,models):
    n0=cnf['variables'];k=len(inc);ys=[[n0+r*c+j+1 for j in range(c)] for r in (0,1)]
    clauses=[]
    for row in ys:
        clauses.append(row)
        clauses.extend([-a,-b] for a,b in combinations(row,2))
    q=len(cnf['triples'])
    for i,J in enumerate(inc):
        clauses.append([q+i+1]+[ys[0][j] for j in J])
        clauses.append([-q-i-1]+[ys[1][j] for j in J])
    survivors=[];tested=0
    for u,v in product(range(c),repeat=2):
        for word in range(1<<k):
            tested+=1
            accepted=all((v if word>>i&1 else u) in J for i,J in enumerate(inc))
            # Evaluate selector implication/exact-one semantics without a free-label shortcut.
            flags=[False]*(n0+2*c)
            for i in range(k):flags[q+i]=bool(word>>i&1)
            flags[ys[0][u]-1]=True;flags[ys[1][v]-1]=True
            value=all(any(flags[abs(a)-1]==(a>0) for a in row) for row in clauses)
            require(accepted==value,'selector equivalence')
            if accepted:
                require(word in models,'geometry-to-key disagreement')
                flags[:n0]=models[word];check_model(cnf,flags[:n0])
                require(all(any(flags[abs(a)-1]==(a>0) for a in row) for row in clauses),'full selector model')
                survivors.append([word,u,v])
    return {'variables':n0+2*c,'added_clauses':len(clauses),
            'union_with_fixed_direction_units':len(cnf['clauses'])+len(clauses)+q,
            'label_component_assignments':tested,'survivors':survivors,'source':'all complete incidence sets of this placement'},clauses


def run():
    data=construct(5);geometry=check(data);cnf=build(data);check_origins(data,cnf)
    p=[tuple(map(Q,v)) for v in data['points']];models=fixed_color_models(cnf,p)
    for model in models.values():check_model(cnf,model)
    f=Fiber({'points':data['points'],'edges':data['edges']});inc=[f.incidence[tuple(t)] for t in data['nonedges']]
    selector,selector_clauses=selector_audit(cnf,inc,len(f.components),models)
    cores=core_audit(inc,len(f.components))
    require(cores==[(0,i) for i in range(1,6)],'complete higher-rank audit')
    actual=sorted({a[0] for a in selector['survivors']});require(actual==sorted(models),'no hidden higher-rank gap at witness')
    word=sum(w['label']<<i for i,w in enumerate(data['hits']));require(word in models,'polygon label model')
    sizes=[]
    for N in (4,5,6,8,12,20):sizes.append({'cycle_order':N,**check(construct(N))})
    rejected=[]
    def reject(name,fn):
        try:fn()
        except (ValueError,KeyError,TypeError,IndexError):rejected.append(name)
        else:raise ValueError('mutation accepted '+name)
    for name,mut in [
        ('missing_closing_edge',lambda d:d['edges'].remove([2,6])),
        ('duplicate_edge',lambda d:d['edges'].__setitem__(0,d['edges'][1])),
        ('missing_nonedge',lambda d:d['targets'].pop()),
        ('missing_face',lambda d:d['faces'].pop()),
        ('flipped_rotation',lambda d:d['rotation'][0].reverse()),
        ('noninjective_vertex',lambda d:d['points'].__setitem__(1,d['points'][0])),
        ('missing_hit',lambda d:d['hits'].pop()),
        ('endpoint_hit',lambda d:d['hits'][0].__setitem__('parameter','0')),
        ('wrong_obstacle_label',lambda d:d['hits'][1].__setitem__('label',0)),
        ('obstacle_hits_vertex',lambda d:d['polygons'][0].__setitem__(0,d['points'][0])),
        ('repeated_corner',lambda d:d['polygons'][1].__setitem__(0,d['polygons'][1][1])),
        ('crossed_boundary',lambda d:d['polygons'][1].__setitem__(1,d['polygons'][1][-2]))]:
        d=deepcopy(data);mut(d);reject(name,lambda:check(d))
    for name,kind in [('drop_same_label_guard','key'),('flip_direction_literal','four')]:
        d=deepcopy(cnf);i=next(i for i,s in enumerate(d['origins']) if s[0]==kind)
        if kind=='key':
            t=d['origins'][i][1];v=36+t;d['clauses'][i]=[a for a in d['clauses'][i] if abs(a)!=v]
        else:d['clauses'][i][0]*=-1
        reject(name,lambda:check_origins(data,d))
    d=deepcopy(cnf);i=next(i for i,s in enumerate(d['origins']) if s[0]=='key');d['origins'][i][3][1]=d['origins'][i][3][0]
    reject('repeat_path_endpoint',lambda:check_origins(data,d))
    bad=list(models[word]);bad[35]=not bad[35];reject('false_same_label_model',lambda:check_model(cnf,bad))
    raw=dimacs(cnf).encode();origin=dump({'paths':cnf['paths'],'origins':cnf['origins']}).encode()
    truevars=lambda bs:[i+1 for i,b in enumerate(bs) if b]
    return {'verdict':'candidate_only','input':data,'geometry':geometry,
            'cnf':{'variables':cnf['variables'],'clauses':len(cnf['clauses']),'counts':cnf['counts'],
                   'paths':sum(map(len,cnf['paths'])),'path_lengths':{str(k):sum(len(p)-1==k for row in cnf['paths'] for p in row) for k in range(2,7)},
                   'dimacs_sha256':hashlib.sha256(raw).hexdigest(),'dimacs_bytes':len(raw),
                   'origins_sha256':hashlib.sha256(origin).hexdigest(),'origins_bytes':len(origin)},
            'scope':'Full unfixed-direction CNF is SAT by explicit model. Only 64 colorings at the constructed direction table are exhausted; no 2^35 direction census.',
            'direction_true_variables':truevars([cross(*(p[i] for i in t))>0 for t in cnf['triples']]),
            'color_models':sorted(models),'witness_color_word':word,'witness_true_variables':truevars(models[word]),
            'incidence':inc,'component_count':len(f.components),'selector':selector,'minimal_empty_families':cores,
            'higher_order_result':'Every empty target family contains a listed disjoint pair; no irredundant rank>=3 cut exists at this realized model.',
            'finite_uniform_regressions':sizes,'rejected_mutations':rejected,'fiber_report':jsonable(f.report())}


if __name__=='__main__':
    args=sys.argv[1:]
    if args==['--cnf']:sys.stdout.write(dimacs(build(construct(5))))
    elif args==['--origins']:
        c=build(construct(5));sys.stdout.write(dump({'paths':c['paths'],'origins':c['origins']}))
    elif args==[]:sys.stdout.write(dump(run()))
    else:raise ValueError('usage: replay.py [--cnf|--origins]')
