"""C27 bounded tests; C26 is a provenance producer, not an incidence dependency.
Only standard library, pure mathematical modules and JSON/TSV stdout.
Use external CPU/wall/memory/output limits. --sources emits every clause origin.
"""
from fractions import Fraction as Q
from itertools import combinations
import copy
import hashlib
import json
import sys
from fiber import Fiber, need, turn, hits, on, at, sub, jsonable
from guards import origin_clause, coordinate_audit
from stars import star, verify
from clause_bridge import Bridge, X4, dimacs


def text(raw):
    return [[str(x), str(y)] for x,y in raw]


def euler_count(f):
    """Different combinatorial check: planarize segments, then E-V+C+1."""
    pts = set(f.p)
    for ab,cd in combinations(f.segments,2):
        pts.update(hits(*ab,*cd))
    segments = set()
    for a,b in f.segments:
        axis = 0 if a[0] != b[0] else 1
        ordered = sorted((p for p in pts if on(p,a,b)),key=lambda p:p[axis])
        segments.update(tuple(sorted((u,v))) for u,v in zip(ordered,ordered[1:]))
    parent = {p:p for p in pts}
    def root(p):
        while parent[p] != p:
            p = parent[p]
        return p
    for a,b in segments:
        parent[root(a)] = root(b)
    c = len({root(p) for p in pts})
    return len(segments)-len(pts)+c+1


def packed(raw):
    return json.dumps(jsonable(raw),sort_keys=True,separators=(',',':')).encode()+b'\n'


def source_lines(bridge, rows):
    for idx,(kind,args,mode) in rows:
        if kind == 'K':
            sid,*path = args; ab,cd = bridge.sides[sid]
            fields = [idx,kind,','.join(map(str,ab)),','.join(map(str,cd)),','.join(map(str,path)),mode]
        else:
            fields = [idx,kind,'-','-',','.join(map(str,args)),mode]
        yield '\t'.join(map(str,fields))+'\n'


def capacity(model, weights):
    need(set(weights) <= set(model.targets), 'unknown weighted nonedge')
    need(all(type(w) in (Q,int) and w >= 0 for w in weights.values()), 'nonnegative exact weights')
    loads = [sum(w for s,w in weights.items() if c in model.incidence[s]) for c in range(len(model.components))]
    need(all(z <= 1 for z in loads), 'component capacity exceeded')
    total = sum(weights.values(),Q(0))
    return {'sum':total,'lower':-(-total.numerator//total.denominator),'loads':loads}


def polygons_check(p,edges,polygons):
    es = set(map(tuple,edges)); witnesses = []
    for polygon in polygons:
        sides = list(zip(polygon,polygon[1:]+polygon[:1]))
        need(all(turn(polygon[i-1],polygon[i],polygon[(i+1)%len(polygon)])>0 for i in range(len(polygon))), 'convex polygon')
        need(all(not all(turn(a,b,q)>=0 for a,b in sides) for q in p), 'forbidden point')
        need(all(not hits(p[i],p[j],a,b) for i,j in edges for a,b in sides), 'graph edge blocked')
    for i,j in combinations(range(len(p)),2):
        if (i,j) in es:
            continue
        a,b = p[i],p[j]; axis=0 if a[0]!=b[0] else 1; found=None
        for index,poly in enumerate(polygons):
            sides=list(zip(poly,poly[1:]+poly[:1])); cuts={Q(0),Q(1)}
            for u,v in sides:
                cuts.update((q[axis]-a[axis])/(b[axis]-a[axis]) for q in hits(a,b,u,v))
            cuts=sorted(cuts)
            for lo,hi in zip(cuts,cuts[1:]):
                t=(lo+hi)/2; q=at(a,b,t)
                if all(turn(u,v,q)>0 for u,v in sides):
                    found={'pair':(i,j),'polygon':index,'parameter':t,'point':q};break
            if found:
                break
        need(found is not None,'unblocked nonedge'); witnesses.append(found)
    return witnesses


def main():
    tiny='1/'+str(10**40)
    cases=[
      ('empty',[],[],1,True),('point',[[0,0]],[],1,True),
      ('finite_segment',[[0,0],[1,0]],[[0,1]],1,True),
      ('forced_line',[[-1,0],[0,0],[1,0]],[[0,1]],1,True),
      ('vertex_on_edge',[[0,0],[1,0],[2,0]],[[0,2]],1,False),
      ('overlap',[[0,0],[1,0],[2,0],[3,0]],[[0,2],[1,3]],1,False),
      ('gapped_support',[[-3,0],[-2,0],[2,0],[3,0]],[[0,1],[2,3]],1,True),
      ('vertical_gap',[[0,-2],[0,0],[0,tiny],[0,2]],[[0,1],[2,3]],1,True),
      ('tiny_gap',[[-2,0],[0,0],[tiny,0],[2,0]],[[0,1],[2,3]],1,True),
      ('near_parallel',[[0,0],[1,0],[0,tiny],[1,'2/'+str(10**40)]],[[0,1],[2,3]],1,True),
      ('free_concurrence',[[2,0],[3,0],[0,2],[0,3],[2,2],[3,3]],[[0,1],[2,3],[4,5]],1,True),
      ('forbidden_concurrence',[[-1,0],[1,0],[0,-1],[0,1],[0,0]],[[0,1],[2,3]],1,False),
      ('crossing',[[0,0],[3,2],[0,2],[3,0]],[[0,1],[2,3]],1,True),
      ('puncture',[[-1,0],[0,0],[1,0]],[],1,True),
      ('square',[[-2,-2],[2,-2],[2,2],[-2,2]],[[0,1],[1,2],[2,3],[0,3]],2,True),
      ('square_puncture',[[-2,-2],[2,-2],[2,2],[-2,2],[0,0]],[[0,1],[1,2],[2,3],[0,3]],2,True),
      ('two_regions',[[-2,-2],[2,-2],[2,2],[-2,2],[0,0],[4,0]],[[0,1],[1,2],[2,3],[0,3]],2,False),
      ('C18',[[-20,0],[0,20],[20,0],[0,-20],[1,8],[-2,-7],[30,1]],[[0,1],[0,2],[0,3],[1,2],[2,3]],3,False)]
    observations=[]; models={}
    for name,p,e,count,exists in cases:
        f=Fiber({'points':p,'edges':e}); models[name]=f
        need(len(f.components)==count==euler_count(f) and bool(f.common)==exists,'fiber fixture '+name)
        observations.append({'name':name,'components':count,'common':f.common,'nodes':len(f.nodes),
                             'report_sha256':hashlib.sha256(packed(f.report())).hexdigest()})
    c18=models['C18']; need(c18.incidence[4,5]==[1,2] and c18.incidence[4,6]==[0,2] and c18.incidence[5,6]==[0,1],'C18 exact incidence')
    packing=capacity(c18,{(0,4):1,(0,5):1,(2,6):1}); need(packing['lower']==3,'C18 fixed packing')
    # All 160 labeled graphs on triples selected from a six-point grid.
    grid=[(x,y) for x in range(3) for y in range(2)]; small=0
    for ps in combinations(grid,3):
        pairs=list(combinations(range(3),2))
        for mask in range(8):
            edges=[list(s) for j,s in enumerate(pairs) if mask>>j&1]
            f=Fiber({'points':[list(q) for q in ps],'edges':edges})
            need(len(f.components)==euler_count(f),'Euler triple')
            # With fewer than three edges the forbidden complex has no cycle.
            if len(edges)<3:
                need(len(f.components)==1,'three-point acyclic complement')
                for a,b in f.targets:
                    axis=0 if f.p[a][0]!=f.p[b][0] else 1
                    left,right=sorted((f.p[a][axis],f.p[b][axis]))
                    cuts=sorted({left,right}|{q[axis] for q in f.p if left<q[axis]<right and on(q,f.p[a],f.p[b])})
                    free=False
                    for lo,hi in zip(cuts,cuts[1:]):
                        x=(lo+hi)/2
                        t=(x-f.p[a][axis])/(f.p[b][axis]-f.p[a][axis])
                        q=at(f.p[a],f.p[b],t)
                        free |= not any(on(q,u,v) for u,v in f.segments)
                    need(bool(f.incidence[a,b]) == free,'three-point union-interval reference')
            small+=1
    bridge=Bridge(10,X4); clauses,rows=bridge.compile()
    need(hashlib.sha256(dimacs(bridge.size,clauses)).hexdigest()=='de54d35f78d3c7d84e24651e5ce6f82c9ebe6d78bc7bd2deb66aa591e6ea276c','frozen CNF mismatch')
    for clause,(idx,origin) in zip(clauses,rows):
        need(idx>=1 and origin_clause(10,bridge.edges,origin)==clause,'origin consumer mismatch')
    provenance=hashlib.sha256(); byte_count=0
    for line in source_lines(bridge,rows):
        b=line.encode('ascii');provenance.update(b);byte_count+=len(b)
    audits=[]
    moment=[(Q(i-5),Q((i-5)**2)) for i in range(10)]
    layouts=[moment,[(y,x) for x,y in moment],[(x-5,y-3*x+1) for x,y in moment],[(x,y/Q(10**40)) for x,y in moment]]
    for i,p in enumerate(layouts):
        f=Fiber({'points':text(p),'edges':[list(e) for e in X4]})
        need(len(f.components)==euler_count(f),'X4 Euler')
        audit=coordinate_audit(f,bridge,clauses,rows)
        need(audit['conflict_count']>0 and not f.common,'bad drawing control')
        lines=[(u[1]-v[1],v[0]-u[0],u[0]*v[1]-u[1]*v[0]) for u,v in combinations(p,2)]
        audit['vertical_pair_lines']=sum(b==0 for a,b,c in lines)
        audit['parallel_pair_line_pairs']=sum(a*e-b*d==0 for (a,b,c),(d,e,g) in combinations(lines,2))
        audits.append({'layout':i,**audit})
    need(audits[1]['vertical_pair_lines']>0 and audits[0]['parallel_pair_line_pairs']>0,'degenerate chart coverage')
    # Three nonparallel pair lines concur away from every graph vertex.
    triple=[(moment[i],moment[j]) for i,j in ((1,6),(3,7),(4,9))]
    need(all(hits(*a,*b)==[(Q(0),Q(4))] for a,b in combinations(triple,2)),'nonvertex concurrence')
    # Actual crossed key paths, with both targets in different components.
    crossed=[[-2,0],[2,0],[2,4],[-2,4],[0,-2],[-7,'-11/2'],[-8,'-15/2']]
    f=Fiber({'points':crossed,'edges':[[0,2],[1,3],[2,3],[0,4],[1,4]]})
    need(all(turn(*(f.p[i] for i in t)) for t in combinations(range(7),3)),'crossed fixture GP')
    cut=hits(f.p[0],f.p[2],f.p[3],f.p[1]);need(cut==[(Q(0),Q(2))],'exact loop cut')
    need(not set(f.incidence[0,1]) & set(f.incidence[5,6]),'crossed-path separation')
    bb=Bridge(7,f.e);cc,rr=bb.compile();crossaudit=coordinate_audit(f,bb,cc,rr)
    # A genuine two-obstacle drawing: dropping the same-component guard fails.
    p=[(Q(x),Q(y)) for x,y in [(-2,-2),(2,-2),(2,2),(-2,2),(6,0)]]
    two_points=text(p)
    edges=[(0,1),(0,3),(1,2),(2,3)]
    polys=[[(Q(-1,4),Q(-1,4)),(Q(1,4),Q(-1,4)),(Q(1,4),Q(1,4)),(Q(-1,4),Q(1,4))],
           [(Q(7,2),Q(-3,2)),(Q(9,2),Q(-3,2)),(Q(9,2),Q(3,2)),(Q(7,2),Q(3,2))]]
    witnesses=polygons_check(p,edges,polys)
    f=Fiber({'points':text(p),'edges':[list(e) for e in edges]});bb=Bridge(5,edges);cc,rr=bb.compile()
    twoaudit=coordinate_audit(f,bb,cc,rr);need(twoaudit['inactive_unguarded_false_rows']>0,'guard deletion not caught')
    starrows=[];firststar=None;capacity_rejected=False
    for r in (3,4,5,7,12,20):
        p,e,poly=star(r);row=verify(p,e,poly);f=Fiber({'points':text(p),'edges':[list(s) for s in e]})
        need(len(f.components)==1 and f.common==[0],'star complement');starrows.append(row)
        if r<=7:
            bb=Bridge(r+1,e);cc,rr=bb.compile();a=coordinate_audit(f,bb,cc,rr)
            need(a['inactive_unguarded_false_rows']==0,'one-obstacle clauses failed')
        if r==3:
            firststar={'points':p,'edges':e,'polygon':poly,'blocks':[[0,1,2],[0,1,3]],'shared_clique':[0,1]}
            try:
                capacity(f,{(1,2):1,(1,3):1})
            except ValueError:
                capacity_rejected=True
    need(capacity_rejected,'false additive packing accepted')
    # Boundary-only original contact can be regularized without moving graph points.
    cp=[(Q(-1),Q(0)),(Q(1),Q(0))]
    touch=[(Q(0),Q(0)),(Q(1,4),Q(1,2)),(Q(-1,4),Q(1,2))]
    touched={q for a,b in zip(touch,touch[1:]+touch[:1]) for q in hits(*cp,a,b)}
    need(touched=={(Q(0),Q(0))},'contact-only fixture')
    square=[(Q(-1,8),Q(-1,8)),(Q(1,8),Q(-1,8)),(Q(1,8),Q(1,8)),(Q(-1,8),Q(1,8))]
    contact_witness=polygons_check(cp,[],[square])
    rejected=[]
    raw={'points':[[0,0],[1,1],[2,4]],'edges':[[0,1]]}
    for name,change in [('duplicate',{'points':[[0,0],[0,0],[2,4]]}),('float',{'points':[[0,0],[1,1.0],[2,4]]}),('bool',{'points':[[0,0],[1,True],[2,4]]}),('loop',{'edges':[[0,0]]}),('duplicate_edge',{'edges':[[0,1],[1,0]]}),('wrong_complement',{'nonedges':[]})]:
        inp=copy.deepcopy(raw);inp.update(change)
        try: Fiber(inp)
        except (ValueError,TypeError,ZeroDivisionError):rejected.append(name)
        else:raise ValueError('invalid input accepted '+name)
    f=models['tiny_gap']; report=jsonable(f.report())
    damages=[('erase_event','critical_x',report['critical_x'][:-1]),('invent_common','common_components',[]),('drop_link','links',report['links'][:-1]),('drop_fiber','fibers',report['fibers'][:-1]),('merge_labels','labels',[7]*len(report['labels'])),('drop_interval','targets',report['targets'][:-1])]
    for name,key,value in damages:
        bad=copy.deepcopy(report);bad[key]=value
        need(bad!=jsonable(Fiber({'points':text(f.p),'edges':[list(e) for e in f.e]}).report()),'damaged semantic report accepted');rejected.append(name)
    # Public exact-intersection regression: integer endpoints must stay rational.
    need(all(type(v) is Q for q in hits((-2,0),(2,4),(-2,4),(2,0)) for v in q),'float intersection regression')
    # Mutation: wrong universal row origin must be rejected, not silently recast.
    for name,origin in [('four_repeated',('4',(0,0,2,3),0)),('five_mode',('5',(0,1,2,3,4),2)),('invent_side',('K',(9999,0,2,1),0)),('nonedge_path',('K',(121,0,1),0))]:
        try: origin_clause(10,bridge.edges,origin)
        except (ValueError,KeyError,IndexError):rejected.append(name)
        else:raise ValueError('damaged origin accepted')
    return {'verdict':'candidate_only','trusted_verifier_receipt':False,'fixtures':observations,
            'three_point_graphs':small,'contact_regularization':contact_witness,'nonvertex_concurrence':[0,4],'clause_origins_checked':len(rows),'provenance_bytes':byte_count,'provenance_sha256':provenance.hexdigest(),
            'x4_coordinate_guards':audits,'crossed':{'input':crossed,'cut':cut,'audit':crossaudit},
            'two_obstacle_guard_mutation':{'points':two_points,'polygons':polys,'witnesses':witnesses,'audit':twoaudit},
            'stars':starrows,'minimal_clique_sum_counterexample':firststar,'C18_fixed_drawing_packing':packing,
            'rejected_mutations':rejected,'false_additive_capacity_rejected':capacity_rejected,
            'scope':'finite execution only; original C22 implication is not inferred from sampled X4 drawings'}


if __name__=='__main__':
    if sys.argv[1:]==['--sources']:
        bridge=Bridge(10,X4);cs,rs=bridge.compile()
        for c,(idx,o) in zip(cs,rs):
            need(origin_clause(10,bridge.edges,o)==c,'source audit')
        for line in source_lines(bridge,rs):
            print(line,end='')
    else:
        need(not sys.argv[1:],'unknown argument')
        print(packed(main()).decode(),end='')
