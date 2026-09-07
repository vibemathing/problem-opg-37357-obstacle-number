"""C28 bounded reproducible run. stdout JSON only; no file/network/process access.
C27 fiber.py must be on PYTHONPATH; its exact bytes are pinned in execution.json.
The CNF generator and second truth checker do not import that geometry core.
"""
from itertools import combinations, product
from collections import Counter
from copy import deepcopy
from fractions import Fraction
import hashlib
import json
import sys
from coupling import build, graph, dimacs
from exhaustive import enumerate_models
from second_check import reconstruct, scalar_table
from geometry import witness_data, check_witness, check_rotation, det, point
from fiber import Fiber, jsonable


def require(ok,message):
    if not ok: raise ValueError(message)


def compact(obj):
    return (json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode('utf-8')


def mutate_tests(formula,witness,model):
    result=[]
    def rejected(name,fn):
        try:fn()
        except (ValueError,KeyError,IndexError,TypeError):result.append({'name':name,'rejected':True})
        else:raise ValueError('accepted damaged input: '+name)
    # Three stale-edge deletions must invalidate the frozen complement/origins.
    for e in ([1,3],[1,5],[3,5]):
        f=deepcopy(formula);f['edges'].remove(e)
        rejected('delete_edge_without_recompile_'+str(e),lambda:reconstruct(f))
    key=next(i for i,o in enumerate(formula['origins']) if o['family']=='key')
    for mode in range(3):
        f=deepcopy(formula);o=f['origins'][key];a,b=o['nonedges'][0]
        if mode==0:o['path']=[a,b]
        if mode==1:o['path'][1]=a
        if mode==2:o['nonedges'][1]=o['nonedges'][0]
        rejected('wrong_path_or_target_'+str(mode),lambda:reconstruct(f))
    for variable in (1,7,20):
        m=model[:];m[variable-1]*=-1
        rejected('flip_coordinate_bound_direction_'+str(variable),lambda:check_witness(witness,formula,m))
    for family in ('four','five','key'):
        f=deepcopy(formula);i=next(i for i,o in enumerate(f['origins']) if o['family']==family)
        f['origins'].pop(i);f['clauses'].pop(i)
        for j,o in enumerate(f['origins']):o['row']=j+1
        rejected('omit_clause_'+family,lambda:reconstruct(f))
    m=model[:];m[20]=21
    rejected('both_obstacle_labels_true',lambda:check_witness(witness,formula,m))
    m=model[:];m[21]=-22
    rejected('neither_obstacle_label_true',lambda:check_witness(witness,formula,m))
    w=deepcopy(witness);w['polygon'][2][1]=-49;w['polygon'][3][1]=-49
    rejected('miss_nonedges_by_shallow_finger',lambda:check_witness(w,formula,model))
    w=deepcopy(witness);w['rotation'][0]=list(reversed(w['rotation'][0]))
    rejected('reverse_one_vertex_rotation',lambda:check_witness(w,formula,model))
    return result


def higher_rank():
    # Frozen C18 drawing re-evaluated by the delivered C27 finite-segment core.
    raw={'points':[[-20,0],[0,20],[20,0],[0,-20],[1,8],[-2,-7],[30,1]],
         'edges':[[0,1],[1,2],[2,3],[0,3],[0,2]]}
    f=Fiber(raw);targets=[(4,5),(4,6),(5,6)]
    rows=[set(f.incidence[t]) for t in targets]
    require(all(rows) and all(a&b for a,b in combinations(rows,2)) and not set.intersection(*rows),'C18 triple')
    admitted=[]
    for labels in product(range(2),repeat=3):
        valid=True
        for color in (0,1):
            group=[rows[i] for i in range(3) if labels[i]==color]
            if group and not set.intersection(*group):valid=False
        if valid:admitted.append(list(labels))
    require(len(admitted)==6,'empty triple does not exclude all two-labelings')
    threshold=[]
    for n in (3,4,5):
        triples=list(combinations(range(n),3))
        valid=[list(z) for z in product(range(2),repeat=n) if all(len({z[i] for i in t})>1 for t in triples)]
        threshold.append({'targets':n,'all_triples_forbidden':True,'assignments_exhausted':1<<n,'models':valid})
    require(threshold[0]['models'] and threshold[1]['models'] and not threshold[2]['models'],'ternary threshold')
    pair_components=list(combinations(range(5),2))
    incidence=[[i for i,pair in enumerate(pair_components) if v in pair] for v in range(5)]
    require(all(set(incidence[a])&set(incidence[b]) for a,b in combinations(range(5),2)), 'abstract pair incidence')
    require(all(not set.intersection(*(set(incidence[a]) for a in t)) for t in combinations(range(5),3)), 'abstract triple incidence')
    return {'C18_input':raw,'selected_targets':[list(t) for t in targets],
            'incidence':[sorted(r) for r in rows], 'two_label_models':admitted,
            'C18_fixed_drawing_only':True,'ternary_only_threshold':threshold,
            'five_target_abstract_components':[list(p) for p in pair_components],
            'five_target_abstract_incidence':incidence,'planar_graph_realization':None,
            'next_condition':'For every placement force five targets for which every triple has empty common-component intersection.'}


def run():
    formula=build(graph());require(reconstruct(formula)==len(formula['clauses']),'source reconstruction')
    exhaustive=enumerate_models(formula);second=scalar_table(formula)
    require([r['satisfying_direction_assignments'] for r in exhaustive['labels']]==second['projected_counts_by_lex_color'],'two counting methods differ')
    w=witness_data();model=exhaustive['minimal_model'];geo=check_witness(w,formula,model)
    main_fiber=Fiber({'points':w['points'],'edges':formula['edges']})
    require(main_fiber.common==[0],'explicit obstacle not in common free component')
    connectors=[]
    for mask in range(8):
        f=build(graph(mask));reconstruct(f);r=enumerate_models(f)
        fp=Fiber({'points':w['points'],'edges':f['edges']})
        require(r['sat'] and all(v<0 for v in r['minimal_model'][:20]) and fp.common==[0], 'connector control')
        rot=[[v for v in row if tuple(sorted((u,v))) in graph(mask)] for u,row in enumerate(w['rotation'])]
        faces=check_rotation(f['edges'],rot)
        target_witnesses=[]
        for pair in fp.targets:
            target_witnesses.append({'pair':list(pair),**jsonable(next(v for v in fp.intervals[pair] if v['component']==0))})
        connectors.append({'mask':mask,'edges':f['edges'],'nonedges':f['nonedges'],
                           'rotation':rot,'faces':faces,'clauses':len(f['clauses']),
                           'cnf_sha256':hashlib.sha256(dimacs(f)).hexdigest(),
                           'enumeration':r,'free_components':len(fp.components),
                           'common_components':fp.common,'witnesses':target_witnesses,
                           'claim_scope':'specific rational drawing; eight specified connector graphs only'})
    for origin in formula['origins']:
        if origin['family']=='key':
            require(origin['nonedges'][0]!=origin['nonedges'][1],'distinct key demands')
    observation={'schema':'c28-execution-observation-v1','verdict':'candidate_only','trusted_receipt':False,
                 'clauses':len(formula['clauses']),'variables':formula['variables'],
                 'clause_families':dict(Counter(o['family'] for o in formula['origins'])),
                 'path_counts':[len(p) for p in formula['path_census']],
                 'cnf_sha256':hashlib.sha256(dimacs(formula)).hexdigest(),
                 'formula_sha256':hashlib.sha256(compact(formula)).hexdigest(),
                 'enumeration':exhaustive,'second_checker':second,'geometry':geo,
                 'main_fiber_components':len(main_fiber.components),'main_common_components':main_fiber.common,
                 'mutations':mutate_tests(formula,w,model),'connectors':connectors,'higher_rank':higher_rank()}
    artifact={'verdict':'candidate_only','edges':formula['edges'],'nonedges':formula['nonedges'],
              'modules':[[0,1,2,4],[2,3,0,4],[4,5,0,2]],'connector_edges':[[1,3],[1,5],[3,5]],
              'z':formula['z'],'side_pairs':formula['side_pairs'],
              'minimal_model':model,'geometry':w,
              'minimality_scope':'six vertices is minimal for three pairwise vertex-disjoint target nonedges; not a global graph minimality claim'}
    return formula,artifact,observation


def source_table(formula):
    lines=['# row\tfamily\tfields; 4:tuple; 5:flip,tuple; Z:target,positive; K:ab,cd,color,mode,side,path']
    for o in formula['origins']:
        f=o['family']
        if f=='four': tag,items='4',o['tuple']
        elif f=='five': tag,items='5',[o['flip']]+o['tuple']
        elif f=='one': tag,items='Z',[o['target'],int(o['positive'])]
        else: tag,items='K',o['nonedges'][0]+o['nonedges'][1]+[o['color'],o['mode'],o['side']]+o['path']
        lines.append(str(o['row'])+'\t'+tag+'\t'+','.join(map(str,items)))
    return ('\n'.join(lines)+'\n').encode('ascii')


if __name__=='__main__':
    require(sys.argv[1:] in ([],['--cnf'],['--sources']), 'arguments')
    if sys.argv[1:] == ['--cnf']:sys.stdout.write(dimacs(build(graph())).decode('ascii'))
    elif sys.argv[1:] == ['--sources']:sys.stdout.write(source_table(build(graph())).decode('ascii'))
    else:
        formula,artifact,observation=run()
        observation['source_table_sha256']=hashlib.sha256(source_table(formula)).hexdigest()
        observation['source_table_bytes']=len(source_table(formula))
        print(json.dumps({'formula':formula,'witness':artifact,'observation':observation},sort_keys=True,separators=(',',':')))
