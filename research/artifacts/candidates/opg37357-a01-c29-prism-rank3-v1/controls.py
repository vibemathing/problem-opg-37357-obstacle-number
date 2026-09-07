"""C28 mutation and coordinate controls. New logic imports no C22/C26 code.
C27 fiber is a pinned, previously delivered geometry comparator only.
"""
import copy
import json
from itertools import combinations
from fractions import Fraction as Q
from seed import seed,completion,validate_embedding
from producer import make
from audit import rederive,need
from fiber import Fiber,jsonable
from rank3 import (four_component_frame, profile_audit, abstract_four_component_control,
                   exhaustive_three_component_elimination)


def det(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def assignment_from_points(points,formula):
    n=formula['n']; trip=list(combinations(range(n),3))
    values=[det(points[a],points[b],points[c]) for a,b,c in trip]
    need(all(values),'GP required for orientation bits')
    return [int(v>0) for v in values]


def geometry_control():
    g=seed(); points=[[i,-i*i] for i in range(6)]
    m=Fiber({'points':points,'edges':g['edges']})
    need(m.common==[0],'minimum Boolean model does not share an actual free component')
    formula=make(6,g['edges'])
    need(assignment_from_points(points,formula)==[0]*20,'leximum orientation not realized')
    witnesses=[]
    for s in m.targets:
        row=next(row for row in m.intervals[s] if row['component']==0)
        witnesses.append({'nonedge':list(s),'point':row['point'],'parameter':row['parameter']})
    # Direct small Jordan check: an exterior escape ray for each witness.
    # Finite fiber certificate is retained even when a straight escape is not found.
    result={'input':{'points':points,'edges':g['edges']},'orientation_bits':[0]*20,
            'selected_component':0,'nonedge_witnesses':witnesses,'fiber_certificate':m.report(),
            'scope':'actual common-component control; simple polygon extraction depends separately on C19'}
    return jsonable(result)


def module_audit(formula):
    g=seed(); maps=[{tuple(e) for e in m['edges']} for m in g['modules']]
    paths={tuple(p) for rows in formula['paths'] for p in rows['paths']}
    cross=[]
    for p in sorted(paths):
        es={tuple(sorted(e)) for e in zip(p,p[1:])}
        if not any(es<=mod for mod in maps):
            cross.append({'path':list(p),'edge_modules':[[i for i,m in enumerate(maps) if tuple(sorted(e)) in m] for e in zip(p,p[1:])]})
    need(cross,'no cross-module paths included')
    return {'all_retained_paths':len(paths),'cross_module_paths':len(cross),'examples':cross[:6],
            'modules':g['modules'],'cross_nonedges':g['nonedges']}


def plane_completion_check():
    # Auxiliary PLANARITY drawing, never confused with obstacle placements.
    points=[(0,0),(12,0),(0,12),(2,2),(8,2),(2,8)]
    def on(q,a,b):
        return det(a,b,q)==0 and all(min(a[j],b[j])<=q[j]<=max(a[j],b[j]) for j in (0,1))
    def meet(a,b,c,d):
        return (det(a,b,c)*det(a,b,d)<0 and det(c,d,a)*det(c,d,b)<0) or any((on(a,c,d),on(b,c,d),on(c,a,b),on(d,a,b)))
    out=[]
    for code in range(27):
        g=completion(code); counts=validate_embedding(g)
        for a,b in g['edges']:
            for v in range(6):
                if v not in (a,b):need(not on(points[v],points[a],points[b]),'vertex on nonincident edge')
        for a,b in combinations(g['edges'],2):
            if set(a).isdisjoint(b):
                need(not meet(points[a[0]],points[a[1]],points[b[0]],points[b[1]]),'nonplane completion')
        out.append({'code':code,**counts})
    return {'points':[list(p) for p in points],'all_27_completions':out,'scope':'simple planar graph witness only'}


def main():
    g=seed();f=make(6,g['edges']);rederive(f)
    key=next(i for i,o in enumerate(f['origins']) if o[0]=='key')
    color=next(i for i,o in enumerate(f['origins']) if o[0]=='color')
    bad=[]
    def test(name,fn):
        d=copy.deepcopy(f);fn(d);bad.append((name,d))
    test('omit_clause',lambda d:d['clauses'].pop())
    test('invent_clause',lambda d:d['clauses'].append([1]))
    test('remove_guard',lambda d:d['clauses'][key].pop())
    test('flip_guard_or_literal',lambda d:d['clauses'][key].__setitem__(0,-d['clauses'][key][0]))
    test('omit_onehot',lambda d:d['clauses'].__delitem__(color))
    test('wrong_complement',lambda d:d['nonedges'].pop())
    test('omit_path',lambda d:d['paths'][0]['paths'].pop())
    test('source_row_mismatch',lambda d:d['origins'].__setitem__(key,d['origins'][0]))
    test('wrong_variable_count',lambda d:d.__setitem__('variables',61))
    test('wrong_path_limit',lambda d:d.__setitem__('path_limit',3))
    test('bool_literal',lambda d:d['clauses'][0].__setitem__(0,True))
    test('repeat_graph_edge',lambda d:d['edges'].append(d['edges'][0]))
    test('reverse_row_order',lambda d:d['clauses'].reverse())
    rejected=[]
    for name,d in bad:
        try:rederive(d)
        except (ValueError,KeyError,TypeError,IndexError):rejected.append(name)
        else:raise ValueError('accepted mutation '+name)
    rot=copy.deepcopy(g);rot['rotation'][0].reverse()
    try:validate_embedding(rot)
    except ValueError:rejected.append('wrong_rotation')
    else:raise ValueError('accepted genus/face mutation')
    geo=geometry_control()
    mirrored=[[-x,y] for x,y in geo['input']['points']]
    tiny=[[str(Q(x,10**40)),str(Q(y,10**40))] for x,y in geo['input']['points']]
    for pts in (mirrored,tiny,[[y,x] for x,y in geo['input']['points']]):
        m=Fiber({'points':pts,'edges':g['edges']});need(bool(m.common),'affine control lost common component')
    raw, selected=four_component_frame(); frame=Fiber(raw)
    selected_rows=[frame.incidence[tuple(t)] for t in selected]
    need(len(frame.components)==4 and sorted(map(tuple,selected_rows))==list(combinations(range(4),2)), 'six target profile not geometrically realized')
    rank=profile_audit(selected_rows,range(4))
    need(rank['cover_number']==3 and len(rank['pair_only_models'])==8 and not rank['rank3_models'], 'rank-three geometric profile')
    rank['input']=raw;rank['selected_nonedges']=selected
    rank['scope']='selected six targets in ONE fixed drawing; not all targets, not all placements'
    rank['selected_intervals']=jsonable([{'pair':t,'rows':frame.intervals[tuple(t)]} for t in selected])
    return {'verdict':'candidate_only','rejected_mutations':rejected,'module_audit':module_audit(f),
            'planarity':plane_completion_check(),
            'rank3_geometric_control':rank,'rank3_abstract_control':abstract_four_component_control(),
            'rank3_exhaustion':exhaustive_three_component_elimination(),
            'geometry_control':geo,'affine_controls':3,'trusted_receipt':False}


if __name__=='__main__':
    print(json.dumps(main(),sort_keys=True,separators=(',',':')))
