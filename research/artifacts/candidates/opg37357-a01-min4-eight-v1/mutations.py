"""Adversarial consumers on frozen, non-secret JSON; bounded by the caller."""
import json,sys,copy
from witness_check import verify
from guarded_cnf import generate
from clause_audit import check
from structure_audit import audit

def rejects(name,fn,value):
    try:fn(value)
    except (ValueError,KeyError,IndexError,TypeError):return name
    raise ValueError('mutation was not rejected: '+name)
def geometry(w):
    out=[]
    for name,change in [
        ('omit_hit',lambda x:x['hits'].pop()),
        ('hit_parameter',lambda x:x['hits'][0].update(parameter='1/2')),
        ('outside_hit_label',lambda x:x['hits'][0].update(obstacle=1)),
        ('reverse_boundary',lambda x:x['polygons'][0].reverse()),
        ('duplicate_corner',lambda x:x['polygons'][0].append(x['polygons'][0][0])),
        ('graph_vertex_in_obstacle',lambda x:x['points'].__setitem__(0,x['polygons'][0][0])),
        ('omit_complement',lambda x:x['nonedges'].pop()),
        ('duplicate_graph_edge',lambda x:x['edges'].append(x['edges'][0])),
        ('inexact_float',lambda x:x['points'][0].__setitem__(0,0.5)),
        ('unassigned_hit',lambda x:x['hits'][0].update(obstacle=2)),
    ]:
        x=copy.deepcopy(w);change(x);out.append(rejects(name,verify,x))
    return {'rejected':out,'count':len(out)}
def clauses(w):
    d=generate({'n':w['n'],'edges':w['edges']});out=[];ki=next(i for i,s in enumerate(d['origins']) if s[0]=='key')
    def missing(x):x['clauses'].pop();x['origins'].pop()
    def guard(x):
        color=set(x['color_variables']);x['clauses'][ki]=[v for v in x['clauses'][ki] if abs(v) not in color]
    def direction(x):
        i=next(i for i,s in enumerate(x['origins']) if s[0]=='four');x['clauses'][i][0]*=-1
    def path(x):x['origins'][ki][3][0]=x['origins'][ki][3][-1]
    def incomplete(x):x['paths'][0]['paths'].pop()
    for name,change in [('omit_clause',missing),('omit_same_obstacle_guard',guard),('flip_direction',direction),('wrong_key_path',path),('incomplete_path_table',incomplete)]:
        x=copy.deepcopy(d);change(x);out.append(rejects(name,check,x))
    return {'rejected':out,'count':len(out)}
def structures(d):
    out=[]
    x=copy.deepcopy(d);x['complement_representatives']['8'].pop();out.append(rejects('omit_complement_class',audit,x))
    x=copy.deepcopy(d);x['complement_representatives']['8'].append(x['complement_representatives']['8'][0]);out.append(rejects('duplicate_isomorphism_class',audit,x))
    x=copy.deepcopy(d);r=next(r for r in x['complement_representatives']['8'] if r['kind']=='admissible');r['rotation'][0].pop();out.append(rejects('broken_rotation',audit,x))
    x=copy.deepcopy(d);r=next(r for r in x['complement_representatives']['8'] if r['kind']=='admissible' and not r['hub_pairs']);r['hub_pairs']=[[0,2]];out.append(rejects('invented_dominating_pair',audit,x))
    x=copy.deepcopy(d);r=next(r for r in x['complement_representatives']['8'] if r['kind']=='nonplanar');r['kuratowski'].pop();out.append(rejects('broken_kuratowski_certificate',audit,x))
    return {'rejected':out,'count':len(out)}
if __name__=='__main__':
    mode=sys.argv[1];d=json.load(sys.stdin);print(json.dumps({'geometry':geometry,'clauses':clauses,'structure':structures}[mode](d),sort_keys=True))
