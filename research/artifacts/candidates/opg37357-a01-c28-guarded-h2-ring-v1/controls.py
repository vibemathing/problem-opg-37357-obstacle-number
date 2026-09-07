"""C28 deterministic finite checks; stdout only, no network/process/file access.
Default: compact observation. --bundle: ordinary JSON data, not encoded source.
"""
import copy
import hashlib
import json
import sys
from fractions import Fraction as F
from itertools import combinations
import guarded_cnf as gen
import second_check as chk
from fiber import Fiber, need, turn


def plain(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,(tuple,list)):return [plain(v) for v in x]
    if isinstance(x,dict):return {str(k):plain(v) for k,v in x.items()}
    return x


def packed(x):return (json.dumps(plain(x),sort_keys=True,separators=(',',':'))+'\n').encode('utf-8')


def digest(x):return hashlib.sha256(packed(x)).hexdigest()


def fiber_summary(points,edges):
    f=Fiber({'points':plain(points),'edges':plain(edges)})
    return {'components':len(f.components),'common':f.common,
            'targets':[{'pair':list(t),'components':f.incidence[t]} for t in f.targets],
            'report':f.report()}


def graph_certificate():
    triangles=[(0,2,4),(0,4,3),(0,3,5),(0,5,2),
               (1,4,2),(1,3,4),(1,5,3),(1,2,5)]
    rotation=[]
    for u in range(6):
        nxt={}
        for face in triangles:
            if u in face:
                i=face.index(u);nxt[face[(i+1)%3]]=face[(i+2)%3]
        start=min(nxt);v=start;row=[]
        while v not in row:
            row.append(v);v=nxt[v]
        need(v==start and len(row)==len(nxt),'rotation construction')
        rotation.append(row)
    g={'n':6,'edges':[list(e) for e in gen.EDGES],
       'nonedges':[list(s) for s in gen.TARGETS],
       'modules':[{'cycle':v} for v in ([0,2,1,3],[2,4,3,5],[4,0,5,1])],
       'rotation':rotation,'minimality_scope':'three disjoint two-terminal groups; not global graph minimality',
       'larger_ring':'t>=4 gives triangle-free n=2t,e=4t, violating e<=2n-4'}
    faces=chk.check_rotation(g);g['faces']=faces
    edge_module={tuple(sorted((a,b))):i for i,group in enumerate(((0,1,2,3),(2,3,4,5),(0,1,4,5))) for a in group[:2] for b in group[2:]}
    g['paths']=[{'target':list(t),'vertices':list(path),'edge_modules':[edge_module[tuple(sorted(e))] for e in zip(path,path[1:])]} for t in gen.TARGETS for path in gen.all_paths(t)]
    g['cross_module_path_count']=sum(len(set(r['edge_modules']))>1 for r in g['paths'])
    return g


def minimal_empty(sets,cap=3):
    edges=[]
    for size in range(1,min(cap,len(sets))+1):
        for row in combinations(range(len(sets)),size):
            common=set(sets[row[0]])
            for j in row[1:]:common.intersection_update(sets[j])
            if not common and not any(set(e)<=set(row) for e in edges):edges.append(list(row))
    return edges


def colorings(sets,edges=None):
    need(len(sets)<=16,'two-color enumeration cap')
    good=[]
    for colors in range(1<<len(sets)):
        if edges is not None:
            valid=all(len({colors>>j&1 for j in e})>1 for e in edges)
        else:
            valid=True
            for r in (0,1):
                group=[set(S) for j,S in enumerate(sets) if (colors>>j&1)==r]
                if group and not set.intersection(*group):valid=False
        if valid:good.append(colors)
    return good


def geometry_controls():
    gap=F(1,10**40)
    cases=[
      ('empty',[],[],1,True),('point',[(0,0)],[],1,True),
      ('vertical_edge',[(0,-1),(0,1)],[(0,1)],1,True),
      ('forced_line',[(-1,0),(0,0),(1,0)],[(0,1)],1,True),
      ('vertex_in_edge',[(0,0),(1,0),(2,0)],[(0,2)],1,False),
      ('overlap',[(0,0),(1,0),(2,0),(3,0)],[(0,2),(1,3)],1,False),
      ('free_concurrence',[(2,0),(3,0),(0,2),(0,3),(2,2),(3,3)],[(0,1),(2,3),(4,5)],1,True),
      ('forbidden_concurrence',[(-1,0),(1,0),(0,-1),(0,1),(0,0)],[(0,1),(2,3)],1,False),
      ('puncture',[(-1,0),(0,0),(1,0)],[],1,True),
      ('tiny_horizontal_gap',[(-2,0),(0,0),(gap,0),(2,0)],[(0,1),(2,3)],1,True),
      ('tiny_vertical_gap',[(0,-2),(0,0),(0,gap),(0,2)],[(0,1),(2,3)],1,True),
      ('near_parallel',[(0,0),(1,0),(0,gap),(1,2*gap)],[(0,1),(2,3)],1,True),
      ('square_diagonals',[(0,0),(2,0),(2,2),(0,2)],[(0,1),(1,2),(2,3),(0,3)],2,True),
      ('split_square',[(0,0),(2,0),(2,2),(0,2)],[(0,1),(1,2),(2,3),(0,3),(0,2)],3,True),
      ('isolated_inside_triangle',[(0,0),(3,0),(0,3),(1,1)],[(0,1),(0,2),(1,2)],2,True)]
    result=[]
    for name,p,e,count,exists in cases:
        m=fiber_summary(p,e)
        need(m['components']==count and bool(m['common'])==exists,'slab control '+name)
        result.append({'name':name,'components':count,'common_nonempty':exists})
    return result


def run():
    cnf=gen.build();sources=chk.check_sources(cnf);enumeration=gen.enumerate_interface(cnf)
    second=chk.census(cnf)
    need(second==enumeration['by_coloring'],'two exhaustive consumers disagree')
    chk.model_check(cnf,enumeration['model'])
    points=[(i,-i*i) for i in range(6)]
    polygon=[('49/100',2),('451/100',2),('451/100','-2051/100'),('449/100','-2051/100'),
             ('449/100',1),('251/100',1),('251/100','-651/100'),('249/100','-651/100'),
             ('249/100',1),('51/100',1),('51/100','-51/100'),('49/100','-51/100')]
    witnesses=[{'pair':list(t),'parameter':F(1,2),
                'point':tuple(F(points[t[0]][j]+points[t[1]][j],2) for j in (0,1))}
               for t in gen.TARGETS]
    need(all(turn(*(points[v] for v in t))<0 for t in combinations(range(6),3)),'model real orientation')
    model={'schema':'c28-sat-model-v1','verdict':'candidate_only',
           'ordering':enumeration['minimum_order'],'orientation_code':0,'coloring_code':0,'side_code':0,
           'assignment':enumeration['model'],'points':points,'polygon':polygon,'witnesses':witnesses}
    octa=fiber_summary(points,gen.EDGES)
    need(octa['common']==[0],'one-obstacle free component')
    graph=graph_certificate()
    # C18 is reused only as a coordinate control, not as an all-placement lower bound.
    p=[(-20,0),(0,20),(20,0),(0,-20),(1,8),(-2,-7),(30,1)]
    e=[(0,1),(1,2),(2,3),(0,3),(0,2)]
    c18=fiber_summary(p,e);index={tuple(row['pair']):row['components'] for row in c18['targets']}
    selected=[(4,5),(4,6),(5,6),(1,6)];sets=[index[s] for s in selected]
    pair=minimal_empty(sets,2);triple=minimal_empty(sets,3)
    pair_models=colorings(sets,pair);triple_models=colorings(sets,triple);actual=colorings(sets)
    need(len(pair_models)==8 and len(triple_models)==6 and actual==triple_models,'rank-three control')
    bad=next(c for c in pair_models if c not in actual)
    need(bad not in (0,15),'counterexample must really use two labels')
    higher={'schema':'c28-realized-rank3-control-v1','verdict':'candidate_only',
            'scope':'four selected targets in C18 fixed drawing only',
            'points':p,'edges':e,'selected_targets':selected,'incidence':sets,
            'minimal_empty_pairs':pair,'minimal_empty_sets_rank_at_most_three':triple,
            'pair_only_h2_models':pair_models,'rank3_h2_models':triple_models,
            'exact_common_component_h2_models':actual,'rejected_two_used_colors_assignment':bad,
            'full_graph_two_obstacle_assignments':len(colorings([row['components'] for row in c18['targets']])),
            'all_placement_conclusion':False,
            'exact_one_z_variables':[[j,r,1+2*j+r] for j in range(4) for r in (0,1)],
            'guarded_empty_set_clauses':[{'targets':S,'color':r,'clause':[-1-2*j-r for j in S]} for S in triple for r in (0,1)]}
    rejected=[]
    def reject(name,fn):
        try:fn()
        except (ValueError,KeyError,IndexError,TypeError,ZeroDivisionError):rejected.append(name)
        else:raise ValueError('accepted mutation '+name)
    bad_cnf=copy.deepcopy(cnf);bad_cnf['rows'].pop()
    reject('delete_clause',lambda:chk.check_sources(bad_cnf))
    key=next(i for i,r in enumerate(cnf['rows']) if r['origin'][0]=='key')
    bad_cnf2=copy.deepcopy(cnf);bad_cnf2['rows'][key]['clause']=[v for v in bad_cnf2['rows'][key]['clause'] if abs(v)<=20 or abs(v)>=27]
    reject('delete_same_obstacle_guards',lambda:chk.check_sources(bad_cnf2))
    bad_cnf3=copy.deepcopy(cnf);bad_cnf3['rows'][key]['origin'][3][1]=bad_cnf3['rows'][key]['origin'][3][0]
    reject('repeated_path_vertex',lambda:chk.check_sources(bad_cnf3))
    bad_cnf4=copy.deepcopy(cnf);bad_cnf4['rows'][0]['id']=0
    reject('wrong_clause_id',lambda:chk.check_sources(bad_cnf4))
    bad_cnf5=copy.deepcopy(cnf);bad_cnf5['edges'].pop()
    reject('wrong_input_graph',lambda:chk.check_sources(bad_cnf5))
    bad_cnf6=copy.deepcopy(cnf);bad_cnf6['z_variables'][0][2]=32
    reject('wrong_color_variable_map',lambda:chk.check_sources(bad_cnf6))
    bad_model=model['assignment'][:];bad_model[21]=22
    reject('two_labels_at_once',lambda:chk.model_check(cnf,bad_model))
    bad_model2=model['assignment'][:];bad_model2[20]=-21
    reject('no_label',lambda:chk.model_check(cnf,bad_model2))
    bad_rotation=copy.deepcopy(graph);bad_rotation['rotation'][0][0]=bad_rotation['rotation'][0][1]
    reject('duplicate_rotation_dart',lambda:chk.check_rotation(bad_rotation))
    bad_cnf7=copy.deepcopy(cnf);bad_cnf7['rows'][key]['clause'][0]*=-1
    reject('flip_guard_literal',lambda:chk.check_sources(bad_cnf7))
    bad_cnf8=copy.deepcopy(cnf);bad_cnf8['side_variables'][0][2]=21
    reject('wrong_side_map',lambda:chk.check_sources(bad_cnf8))
    bad_cnf9=copy.deepcopy(cnf);bad_cnf9['targets'].pop()
    reject('omit_target',lambda:chk.check_sources(bad_cnf9))
    reject('coincident_coordinates',lambda:fiber_summary([(0,0),(0,0)],[]))
    reject('float_coordinate',lambda:fiber_summary([(0,0),(1,0.5)],[]))
    reject('duplicate_graph_edge',lambda:fiber_summary([(0,0),(1,1)],[(0,1),(1,0)]))
    observation={'verdict':'candidate_only','status':'NONTERMINAL_CHECKPOINT','trusted_receipt':False,
                 'graph':{'vertices':6,'edges':12,'modules':3,'nonedges':3,'faces':8},
                 'source_audit':sources,'exhaustive':enumeration,'second_cnf_count_matches':True,
                 'geometry_controls':geometry_controls(),'rejected_mutations':rejected,
                 'positive_geometry':{'polygon_corners':12,'free_components':octa['components'],'common':octa['common'],
                                      'polygon_assurance':'explicit analytic proof; final run checks components, not a general polygon checker'},
                 'higher_rank':higher,
                 'data_sha256':{'graph.json':digest(graph),'cnf.json':digest(cnf),'model.json':digest(model),
                                'rank3-control.json':digest(higher),'fiber-certificate.json':digest(octa['report'])}}
    return {'observation.json':observation,'graph.json':graph,'cnf.json':cnf,'model.json':model,
            'rank3-control.json':higher,'fiber-certificate.json':octa['report']}


if __name__=='__main__':
    need(sys.argv[1:] in ([],['--bundle']),'arguments')
    data=run();print(packed(data if sys.argv[1:] else data['observation.json']).decode('utf-8'),end='')
