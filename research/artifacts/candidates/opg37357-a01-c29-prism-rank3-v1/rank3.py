"""C28 fixed-incidence h=2 rank-three control. No graph-level lower-bound claim.
No network, files, processes or prior clause generators.
"""
from itertools import combinations, product
from fractions import Fraction as Q


def need(ok,msg):
    if not ok: raise ValueError(msg)


def minimal_empty(incidence,universe):
    rows=[]
    for k in range(1,len(incidence)+1):
        for sub in combinations(range(len(incidence)),k):
            if any(set(old)<=set(sub) for old in rows): continue
            common=set(universe)
            for i in sub: common.intersection_update(incidence[i])
            if not common: rows.append(sub)
    return rows


def profile_audit(incidence,universe):
    need(len(incidence)<=6 and len(universe)<=4,'profile audit cap')
    bad=minimal_empty(incidence,universe)
    pair=[s for s in bad if len(s)<=2]; rank3=[s for s in bad if len(s)<=3]
    full_pass=[]; pair_pass=[]; triple_pass=[]
    for colors in product((0,1),repeat=len(incidence)):
        common=[set(universe),set(universe)]
        for i,c in enumerate(colors): common[c].intersection_update(incidence[i])
        direct=all(common)
        weak=all(len({colors[i] for i in s})>1 for s in bad)
        need(direct==weak,'all-rank elimination mismatch')
        if direct:full_pass.append(colors)
        if all(len({colors[i] for i in s})>1 for s in pair):pair_pass.append(colors)
        if all(len({colors[i] for i in s})>1 for s in rank3):triple_pass.append(colors)
    minimum=None; cover=None
    for k in range(len(universe)+1):
        for choice in combinations(universe,k):
            if all(set(choice)&set(J) for J in incidence): minimum=k;cover=choice;break
        if minimum is not None:break
    # Every exclusion has a source for each component, not a free abstract clause.
    sources=[{'targets':list(s),'missed_by':[{'component':u,'target':next(i for i in s if u not in incidence[i])} for u in universe]} for s in bad]
    return {'incidence':[sorted(J) for J in incidence],'universe':list(universe),
            'minimal_empty_sources':sources,'all_two_label_assignments':1<<len(incidence),
            'pair_only_models':[list(c) for c in pair_pass],'rank3_models':[list(c) for c in triple_pass],
            'full_component_models':[list(c) for c in full_pass], 'cover_number':minimum,'cover':list(cover) if cover is not None else None}


def four_component_frame():
    points=[(Q(0),Q(0)),(Q(12),Q(0)),(Q(0),Q(12)),(Q(3),Q(3))]
    edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    targets=[]
    for a,b in edges:
        p,q=points[a],points[b]
        m=tuple((p[j]+q[j])/2 for j in range(2)); normal=(-(q[1]-p[1])/100,(q[0]-p[0])/100)
        i=len(points);targets.append([i,i+1])
        points.extend([tuple(m[j]+sgn*normal[j] for j in range(2)) for sgn in (-1,1)])
    return {'points':[[str(v) for v in p] for p in points],'edges':[list(e) for e in edges]},targets


def exhaustive_three_component_elimination():
    subsets=[set(s) for k in range(4) for s in combinations(range(3),k)]
    profiles=colors_checked=0
    for rows in product(subsets,repeat=4):
        bad=minimal_empty(rows,range(3))
        need(all(len(s)<=3 for s in bad),'empty-intersection rank exceeds universe size')
        for colors in product((0,1),repeat=4):
            common=[set(range(3)),set(range(3))]
            for i,c in enumerate(colors):common[c].intersection_update(rows[i])
            projected=all(len({colors[i] for i in s})>1 for s in bad)
            need(all(common)==projected,'rank-three color elimination')
            colors_checked+=1
        profiles+=1
    return {'incidence_profiles':profiles,'two_label_cases':colors_checked,'universe_size':3,'target_count':4}


def abstract_four_component_control():
    rows=list(combinations(range(4),2));out=profile_audit(rows,range(4))
    need(len(out['pair_only_models'])==8 and not out['rank3_models'] and out['cover_number']==3,'four-component target control')
    need(sorted(len(s['targets']) for s in out['minimal_empty_sources'])==[2,2,2,3,3,3,3],'minimal obstruction census')
    out['fractional_weight_optimum']='2'
    out['weight_witness']=['1/3']*6
    out['fractional_cover_witness']=['1/2']*4
    out['all_placement_claim']=False
    return out
