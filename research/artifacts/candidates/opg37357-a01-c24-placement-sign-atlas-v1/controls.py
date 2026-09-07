"""Exact bounded C24 controls and direct coordinate proof checks.
No external files, network, subprocess, dynamic evaluation or filesystem writes.
"""
from fractions import Fraction as F
from itertools import combinations
import hashlib
import json
from signature import encode, orient
from sweep import arrangement, graph_cover

P = [(F(1),F(1)),(F(-2),F(-2)),(F(3),F(6)),(F(-5),F(-10)),(F(7),F(-7)),(F(-11),F(11))]
Q = P[:-1]+[(F(-11), F(1101,100))]
PM = P[:-1]+[(F(-11), F(1099,100))]
MATCHING = [(0,1),(2,3),(4,5)]
CACTUS = [(0,1),(2,3),(0,4),(1,2),(1,4),(1,5),(2,5)]


def det(u,v):
    return u[0]*v[1]-u[1]*v[0]


def sub(u,v):
    return (u[0]-v[0],u[1]-v[1])


def segment_meet(a,b,c,d):
    r,s,z = sub(b,a),sub(d,c),sub(c,a)
    den = det(r,s)
    if den:
        t,u = det(z,s)/den,det(z,r)/den
        return 0 <= t <= 1 and 0 <= u <= 1
    if det(z,r):
        return False
    return all(max(min(a[k],b[k]),min(c[k],d[k])) <= min(max(a[k],b[k]),max(c[k],d[k])) for k in (0,1))


def on(a,b,z):
    return det(sub(b,a),sub(z,a)) == 0 and all(min(a[k],b[k]) <= z[k] <= max(a[k],b[k]) for k in (0,1))


def interpolate(a,b,t):
    return ((1-t)*a[0]+t*b[0],(1-t)*a[1]+t*b[1])


def open_chord_in_triangle(a,b,triangle):
    for i in range(3):
        u,v = triangle[i],triangle[(i+1)%3]
        x,y = orient(u,v,a),orient(u,v,b)
        if min(x,y) < 0 or max(x,y) <= 0:
            return False
    return True


def escapes(points, special):
    targets = [ij for ij in combinations(range(6),2) if ij not in CACTUS]
    rows = []
    for i,j in targets:
        if (i,j) == (4,5) and not special:
            continue
        trials = [F(4199,10800)] if (i,j) == (4,5) else [F(1,100),F(1,2),F(99,100)]
        found = None
        for t in trials:
            z = interpolate(points[i],points[j],t)
            tips = [(F(50),z[1]),(F(-50),z[1]),(z[0],F(50)),(z[0],F(-50))]
            if (i,j) == (4,5) and special:
                tips.append((F(50),F(50)*z[1]/z[0]))
            for tip in tips:
                if not any(on(z,tip,p) for p in points) and not any(segment_meet(z,tip,points[a],points[b]) for a,b in CACTUS):
                    found = {'pair':[i,j],'parameter':str(t),'point':list(map(str,z)),'escape_tip':list(map(str,tip))}
                    break
            if found:
                break
        if not found:
            raise AssertionError(('escape not found',i,j))
        rows.append(found)
    return rows


def direct_control(points=P):
    delta=points[5][1]-11
    sx=7*delta/(36+delta)
    rx=(35*delta-108)/(234+5*delta)
    o=(sx,sx); r=(rx,F(8,5)*rx+F(6,5))
    if not (on(points[0],points[1],o) and on(points[4],points[5],o) and on(points[1],points[2],r)):
        raise AssertionError('partition endpoints not forbidden')
    parts=[(points[4],o,[points[0],points[1],points[4]]),(o,r,[(F(0),F(0)),points[2],points[1]]),(r,points[5],[points[1],points[2],points[5]])]
    if not all(open_chord_in_triangle(a,b,t) for a,b,t in parts):
        raise AssertionError('nonedge partition not enclosed')
    before,after=escapes(points,False),escapes(Q,True)
    w=interpolate(points[4],points[5],F(1,3))
    if any(on(points[a],points[b],w) for a,b in CACTUS):
        raise AssertionError('second obstacle witness forbidden')
    return {'before_exterior_witnesses':before,'after_exterior_witnesses':after,
            'before_additional_witness':list(map(str,w)),
            'partition_parameters':['0',str((7-sx)/18),str((7-rx)/18),'1'],
            'triangle_partition_checked':True,
            'scope':'finite algebra plus the displayed Jordan/exterior proof; not a trusted receipt'}


def digest(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def run():
    sp,sq,sm=encode(P),encode(Q),encode(PM)
    if sp['orientation'] != sq['orientation'] or sp['orientation'] != sm['orientation']:
        raise AssertionError('vertex signs')
    models=[arrangement(sp),arrangement(sq)]
    results=[]
    for name,edges,want in [('matching',MATCHING,[(1,1),(2,1)]),('cactus',CACTUS,[(5,2),(5,1)])]:
        row=[]
        for a,(components,tau) in zip(models,want):
            c=graph_cover(a,edges)
            if (c['component_count'],c['minimum_cover']) != (components,tau):
                raise AssertionError(name)
            row.append({'cells':len(a['cells']),'faces':len(a['faces']),'components':components,
                        'minimum_cover':tau,'nonedges':c['nonedges']})
        results.append({'name':name,'before':row[0],'after':row[1]})
    cm=graph_cover(arrangement(sm),CACTUS)
    if cm['minimum_cover'] != 2 or cm['component_count'] != 5:
        raise AssertionError('negative perturbation')
    near=[]
    for delta in (F(-1,10**40), F(1,10**40)):
        z=P[:-1]+[(F(-11),F(11)+delta)]
        zs=encode(z);zc=graph_cover(arrangement(zs),CACTUS)
        if zs['orientation']!=sp['orientation'] or zc['minimum_cover']!=(2 if delta<0 else 1):
            raise AssertionError('near concurrence')
        near.append({'delta':str(delta),'minimum_cover':zc['minimum_cover']})
    # Every labeled graph on a fixed three-point placement.
    tri=arrangement(encode([(0,0),(1,2),(3,1)]))
    pairs=list(combinations(range(3),2))
    for mask in range(8):
        c=graph_cover(tri,[p for k,p in enumerate(pairs) if mask>>k&1])
        if c['component_count'] != (2 if mask==7 else 1) or c['minimum_cover'] != (0 if mask==7 else 1):
            raise AssertionError('three-point reference')
    badreal=encode([(0,0),(1,2),(3,1)])
    badreal['orientation'][0] *= -1
    assumed=arrangement(badreal)
    if badreal['orientation'][0] == badreal['w'][0] or not assumed['cells']:
        raise AssertionError('realizability gap control')
    # Geometric symmetries preserve the cover, not necessarily signature labels.
    for p in (P,Q):
        wanted=graph_cover(arrangement(encode(p)),CACTUS)['minimum_cover']
        for transform in (lambda x,y:(x+13,y-8),lambda x,y:(3*x,3*y),lambda x,y:(-x,y)):
            z=[transform(x,y) for x,y in p]
            if graph_cover(arrangement(encode(z)),CACTUS)['minimum_cover'] != wanted:
                raise AssertionError('symmetry control')
    invalid=[[(0,0),(0,1),(1,2)],[(0,0),(1,1),(2,2)],[(0,0),(1,1),(2,0),(3,1)],[(False,0),(1,2),(3,1)],[(0.0,0),(1,2),(3,1)]]
    for p in invalid:
        try: encode(p)
        except ValueError: continue
        raise AssertionError('invalid domain accepted')
    broken=json.loads(json.dumps(sp));broken['w'][0]=0
    try: arrangement(broken)
    except ValueError: pass
    else: raise AssertionError('zero denominator accepted')
    return {'verdict':'candidate_only','arithmetic':'fractions.Fraction','signature_hashes':[digest(sp),digest(sq)],
            'all_twenty_vertex_signs_equal':True,'points_before':[[str(x),str(y)]for x,y in P],
            'points_after':[[str(x),str(y)]for x,y in Q],'cactus_edges':CACTUS,'results':results,
            'direct_geometry':direct_control(),'negative_perturbation_direct':direct_control(PM),
            'negative_perturbation_tau':cm['minimum_cover'],'near_controls':near,
            'orientation_values':[[list(t),[str(orient(*(pts[i] for i in t))) for pts in (PM,P,Q)]] for t in combinations(range(6),3)],
            'unrealizable_sign_input_not_detected':True,
            'realizability_warning':'interpreter does not test W_(01,02)=orient(0,1,2); a separate real-sign feasibility obligation is mandatory',
            'three_point_graphs':8,'symmetry_controls':6,
            'invalid_domain_controls':5,'zero_denominator_rejected':True,
            'realizability_solver_run':False,'trusted_verifier_receipt':False}


if __name__ == '__main__':
    print(json.dumps(run(),sort_keys=True,separators=(',',':')))
