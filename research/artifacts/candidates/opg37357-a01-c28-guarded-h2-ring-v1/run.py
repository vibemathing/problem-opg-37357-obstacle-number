"""C28 reproducible finite h=2 research packet. JSON/DIMACS/TSV stdout only.
Existing C27 fiber.py must be on PYTHONPATH; it is not a CNF dependency.
Use external 35 CPU / 40 wall seconds, 512 MiB and 4 MiB output limits.
"""
import copy
import hashlib
import json
import sys
from collections import Counter
from itertools import combinations
from guarded import Encoding, extend, bits, value, tidy, require
from exhaust import enumeration
from audit import record_check, scalar_orientations, scalar_colors, rotation_check
from geometry_check import examples,check,orient,port_chain
from fiber import Fiber,jsonable
import guarded_cnf
import second_check


EDGES={
 'diamonds':sorted([(i,j) for i in (0,1) for j in range(2,6)]+[(2,3),(3,4),(4,5)]),
 'octahedron':[e for e in combinations(range(6),2) if e not in [(0,1),(2,3),(4,5)]]}
ROTATIONS={
 'diamonds':{0:[2,3,4,5],1:[2,5,4,3],2:[0,1,3],3:[1,4,0,2],4:[3,1,5,0],5:[4,1,0]},
 'octahedron':{0:[2,5,3,4],1:[2,4,3,5],2:[0,4,1,5],3:[1,4,0,5],4:[3,1,2,0],5:[3,0,2,1]}}
MODULES={'diamonds':[[0,1,2,3],[0,1,3,4],[0,1,4,5]],
         'octahedron':[[0,1,2,3],[2,3,4,5],[0,1,4,5]]}


def sha(raw):return hashlib.sha256(raw).hexdigest()


def dump(obj):return json.dumps(jsonable(obj),sort_keys=True,separators=(',',':')).encode()+b'\n'


def strings(p):return [[str(v) for v in row] for row in p]


def triple_interface():
    """Abstract five-target prototype, explicitly NOT a planar-geometry certificate."""
    components=list(combinations(range(5),2));triples=list(combinations(range(5),3))
    incidence=[[i for i,c in enumerate(components) if v in c] for v in range(5)]
    require(all(set(incidence[i]) & set(incidence[j]) for i,j in components),'pair control')
    require(all(not set.intersection(*(set(incidence[i]) for i in t)) for t in triples),'triple control')
    exclusions=[]
    for code in range(32):
        colors=bits(code,5)
        t=next(t for t in triples if len({colors[i] for i in t})==1)
        exclusions.append([code,list(t),colors[t[0]]])
    return {'scope':'abstract incidence system only; no planar realization or universal placement claim',
            'components':[list(c) for c in components],'incidence':incidence,
            'triples':[list(t) for t in triples],'two_label_exclusions':exclusions,
            'clause_pairs':[[[i+1 for i in t],[-i-1 for i in t]] for t in triples],
            'result':'UNSAT over all 32 five-target color words',
            'minimality':'triple-only constraints on <=4 targets always allow a 2+2 split'}


def bad_data_mutations(data):
    out=[]
    def reject(name,changed):
        try:second_check.check_sources(changed)
        except (ValueError,IndexError,KeyError,TypeError) as err:out.append({'name':name,'rejected':True,'reason':str(err)})
        else:raise ValueError('accepted mutation '+name)
    first=next(i for i,r in enumerate(data['rows']) if r['origin'][0]=='key')
    for name in ('drop_edge','reverse_edge','drop_clause','drop_guard','flip_direction','repeat_path_vertex',
                 'wrong_path_end','reverse_clause','drop_exact_one','wrong_color_map','wrong_side_map',
                 'wrong_color_origin','missing_five_edge_row','duplicate_clause'):
        d=copy.deepcopy(data);r=d['rows'][first]
        if name=='drop_edge':d['edges'].pop()
        elif name=='reverse_edge':d['edges'][0].reverse()
        elif name=='drop_clause':d['rows'].pop()
        elif name=='drop_guard':r['clause']=[v for v in r['clause'] if not 21<=abs(v)<=26]
        elif name=='flip_direction':
            j=next(j for j,v in enumerate(r['clause']) if abs(v)<=20);r['clause'][j]*=-1
        elif name=='repeat_path_vertex':r['origin'][3][1]=r['origin'][3][0]
        elif name=='wrong_path_end':r['origin'][3][-1]=r['origin'][3][0]
        elif name=='reverse_clause':r['clause'].reverse()
        elif name=='drop_exact_one':d['rows'].pop(next(i for i,r in enumerate(d['rows']) if r['origin'][0]=='exact_one'))
        elif name=='wrong_color_map':d['z_variables'][0][-1]=32
        elif name=='wrong_side_map':d['side_variables'][0][-1]=28
        elif name=='wrong_color_origin':r['origin'][4]=2
        elif name=='missing_five_edge_row':d['rows'].pop(next(i for i,r in enumerate(d['rows']) if r['origin'][0]=='key' and len(r['origin'][3])==6))
        elif name=='duplicate_clause':d['rows'].append(copy.deepcopy(r))
        reject(name,d)
    return out


def main():
    data=guarded_cnf.build();old=guarded_cnf.enumerate_interface(data)
    origin_audit=second_check.check_sources(data)
    require(second_check.census(data)==old['by_coloring'],'retained second core disagreement')
    second_check.model_check(data,old['model'])
    results=[];directions=None;deletions=[]
    for name,edges in EDGES.items():
        enc=Encoding(6,edges);res=enumeration(enc)
        record_check(enc,enc.clauses,enc.origins)
        algebra=[c for c,r in zip(enc.clauses,enc.origins) if r[0]!='key']
        if directions is None:directions=scalar_orientations(6,algebra)
        else:require(algebra==old_algebra,'same orientation layer')
        old_algebra=algebra
        slow=scalar_colors(6,edges,directions)
        require(slow['counts_by_color_word']==res['counts_by_color_word'] and slow['minimum']==res['minimum_model'][:2], 'scalar exhaustive disagreement')
        theta,z,assignment=res['minimum_model'];p,polys=examples(name)
        require(theta==0 and all(orient(*(p[i] for i in t))<0 for t in enc.triples),'minimum coordinate realization')
        geometry=check(p,edges,polys)
        f=Fiber({'points':strings(p),'edges':[list(e) for e in edges]})
        common=[];colors=bits(z,len(enc.targets))
        for color in (0,1):
            targets=[s for i,s in enumerate(enc.targets) if colors[i]==color]
            group=set(range(len(f.components)))
            for s in targets:group.intersection_update(f.incidence[s])
            require(not targets or group,'minimum label lacks joint component')
            common.append({'color':color,'targets':[list(s) for s in targets],
                           'components':sorted(group) if targets else [],'unused':not targets})
        faces=rotation_check(6,edges,ROTATIONS[name])
        if name=='octahedron':
            require(second_check.check_rotation({'n':6,'edges':[list(e) for e in edges], 'rotation':[ROTATIONS[name][i] for i in range(6)]})==faces,'rotation consumer mismatch')
            mapped=[]
            for row in data['rows']:
                c=[]
                for q in row['clause']:
                    sign=1 if q>0 else -1;a=abs(q)
                    if a<=20:new=sign*a
                    elif a<=26:
                        i,r=divmod(a-21,2);new=sign*(1 if r else -1)*(21+i)
                    else:new=sign*(a-3)
                    c.append(new)
                c=tidy(c)
                if c is not None:mapped.append(c)
            require(sorted(set(mapped))==enc.clauses,'exact-one to single-z equivalence')
            require(old['sat_direction_label_pairs']==res['accepted_projected_pairs'],'prototype count')
        results.append({'name':name,'n':6,'edges':[list(e) for e in edges],'modules':MODULES[name],
            'targets':[list(s) for s in enc.targets],'rotation':[ROTATIONS[name][i] for i in range(6)],'faces':faces,
            'variables':enc.nvars,'clauses':len(enc.clauses),'families':dict(Counter(r[0] for r in enc.origins)),
            'path_lengths':{str(s):{str(k):sum(len(p)==k+1 for p in enc.paths[s]) for k in range(2,6)} for s in enc.targets},
            'orientation_map':[list(t) for t in enc.triples],
            'label_map':[[list(s),v] for s,v in enc.z.items()],
            'side_map':[[list(s),list(t),v] for (s,t),v in enc.side.items()],
            'dimacs_sha256':sha(enc.dimacs()),'dimacs_bytes':len(enc.dimacs()),
            'origins_sha256':sha(enc.source_tsv()),'origins_bytes':len(enc.source_tsv()),
            'enumeration':res,'scalar_crosscheck':slow,'points':strings(p),
            'polygons':[strings(poly) for poly in polys],'geometry':geometry,
            'incidence':[{'pair':list(s),'components':f.incidence[s]} for s in f.targets],
            'joint_components':common,'fiber_report_sha256':sha(dump(f.report())),
            'model_classification':'explicit real straight-line polygonal obstacle representation; not merely a pseudoline model'})
        for removed in edges:
            es=[e for e in edges if e!=removed];mut=Encoding(6,es);r=enumeration(mut)
            rot={v:[u for u in ROTATIONS[name][v] if tuple(sorted((u,v)))!=removed] for v in range(6)}
            fs=rotation_check(6,es,rot)
            require(r['result']=='SAT','non-SAT deletion requires investigation')
            deletions.append({'parent':name,'removed':list(removed),'n':6,'edges':[list(e) for e in es],
                'rotation':[rot[i] for i in range(6)],'face_count':len(fs),'variables':mut.nvars,
                'clauses':len(mut.clauses),'dimacs_sha256':sha(mut.dimacs()),'result':r['result'],
                'accepted_projected_pairs':r['accepted_projected_pairs'],'minimum_model':r['minimum_model'],
                'minimum_realizability':'not classified by this deletion experiment'})
    corrupt=bad_data_mutations(data)
    for name in ('duplicate_neighbor','single_rotation_reverse'):
        rot=copy.deepcopy(ROTATIONS['octahedron'])
        if name=='duplicate_neighbor':rot[0][0]=rot[0][1]
        else:rot[0].reverse()
        try:rotation_check(6,EDGES['octahedron'],rot)
        except ValueError as e:corrupt.append({'name':name,'rejected':True,'reason':str(e)})
        else:raise ValueError('damaged rotation accepted')
    chains=[]
    for m in (3,4,5,8,16):
        p,es,polys=port_chain(m);g=check(p,es,polys)
        require(all(orient(*(p[i] for i in t))!=0 for t in combinations(range(len(p)),3)),'port chain GP')
        chains.append({'helpers':m,'n':len(p),'edges':len(es),'nonedges':len(p)*(len(p)-1)//2-len(es),
                       'corners':g['corners'],'minimum_edge_boundary_distance_squared':g['minimum_edge_boundary_distance_squared'],
                       'verified_by_direct_polygon_check':True})
    return {'verdict':'candidate_only','trusted_receipt':False,'base_revision':'f09892bdb8e26edcdfc80edacc2790de904a70ea',
            'tested_family':'two six-vertex couplings and EVERY single-edge deletion of each (25 instances)',
            'reused_C28_prototype':{'complete_sources':origin_audit,'census':old,'unchanged_original_source':True},
            'base_cases':results,'edge_deletions':deletions,'corruptions':corrupt,
            'port_chain_constructive_tests':chains,'next_triple_interface':triple_interface(),
            'first_model_cut_warning':'Both first models are genuine; a claimed empty triple intersection cutting them off is false. No such cut is added.',
            'remaining_quantifier':'No family with forall real placements excluding all two-label component assignments; no trusted gate receipt.'}


if __name__=='__main__':
    args=sys.argv[1:]
    if not args:print(dump(main()).decode(),end='')
    elif len(args)==2 and args[0] in ('--dimacs','--sources') and args[1] in EDGES:
        enc=Encoding(6,EDGES[args[1]])
        print((enc.dimacs() if args[0]=='--dimacs' else enc.source_tsv()).decode(),end='')
    else:raise ValueError('usage: run.py [--dimacs|--sources diamonds|octahedron]')
