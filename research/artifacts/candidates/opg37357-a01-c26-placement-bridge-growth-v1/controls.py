"""C26 finite clause/projection audits. No network, child process or file I/O.
C22 root_cnf is a comparison oracle only; put its frozen directory on PYTHONPATH.
The optional --origins mode emits a reproducible derived table to stdout.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
import hashlib
import json
import sys
import root_cnf
from clause_bridge import Bridge, X4, require, canonical, determinant, project, satisfied, dimacs, origin_text
from growth import amplification_controls


def sha(data):
    return hashlib.sha256(data).hexdigest()


def on(p,a,b):
    return determinant(a,b,p) == 0 and sum((p[i]-a[i])*(p[i]-b[i]) for i in (0,1)) <= 0


def meet(a,b,c,d):
    return (determinant(a,b,c)*determinant(a,b,d) < 0 and
            determinant(c,d,a)*determinant(c,d,b) < 0) or any((on(a,c,d),on(b,c,d),on(c,a,b),on(d,a,b)))


def semantic_checks():
    total = 0
    # Existential elimination of the original paper's per-path key variable.
    for c in range(1,6):
        for j in range(1,4):
            for bits in product((False,True),repeat=c+j+1):
                C,J,s = bits[:c],bits[c:c+j],bits[-1]
                A,B = any(C),any(not v for v in C)
                U,V = (not s or any(J)),(s or any(not v for v in J))
                old = any((A or key) and (B or key) and (not key or U) and (not key or V)
                          for key in (False,True))
                new = (A or U) and (A or V) and (B or U) and (B or V)
                require(old == new, 'key-variable elimination mismatch')
                for same_color in (False,True):
                    guarded = all(not same_color or q for q in (A or U,A or V,B or U,B or V))
                    require(guarded == (not same_color or new), 'color guard mismatch')
                total += 1
    return total


def source_origin_audit(bridge, clauses, rows):
    # Every stored final row gets an explicit tuple/path and one implication type.
    for i,(number,(family,args,mode)) in enumerate(rows):
        require(number == i+1, 'row ID')
        if family in ('4','5'):
            require(len(set(args)) == len(args) == int(family), 'repeated tuple index')
        else:
            sid,*p = args
            (a,b),(c,d) = bridge.sides[sid]
            require((a,b) != (c,d) and p[0] == a and p[-1] == b, 'key endpoints')
            require(2 <= len(p)-1 <= 4 and len(set(p)) == len(p), 'path scope')
            require(all(tuple(sorted(e)) in bridge.edges for e in zip(p,p[1:])), 'not graph path')
        require(canonical(bridge.raw_clause((family,args,mode))) == clauses[i], 'row-to-origin mismatch')
    return dict(Counter(origin[0] for _,origin in rows))


def rational_identities(points):
    D = lambda a,b,c: determinant(points[a],points[b],points[c])
    require(all(D(*t) != 0 for t in combinations(range(len(points)),3)), 'GP fixture')
    four = five = projection = 0
    for a,b,c,d in permutations(range(len(points)),4):
        require(D(b,c,d) == D(a,b,c)+D(a,c,d)+D(a,d,b), 'four-point identity')
        four += 1
    for a,b,c,d,e in permutations(range(len(points)),5):
        require(D(a,b,d)*D(a,c,e) == D(a,b,c)*D(a,d,e)+D(a,b,e)*D(a,c,d),
                'five-point identity')
        five += 1
    for i,j,k in combinations(range(len(points)),3):
        A,B = points[i][1]-points[j][1],points[j][0]-points[i][0]
        C,E = points[i][1]-points[k][1],points[k][0]-points[i][0]
        require(A*E-B*C == D(i,j,k), 'C25 W-to-orientation map')
        projection += 1
    return {'four':four,'five':five,'W_projection':projection}


def fan(r):
    points = [(F(0),F(-r*r))]+[(F(i),F(i*i)) for i in range(1,r+1)]
    edges = [(0,i) for i in range(1,r+1)]+[(i,i+1) for i in range(1,r)]
    polygon = [(F(i),F(i*i)+F(1,2)) for i in range(1,r+1)]
    sides = list(zip(polygon,polygon[1:]+polygon[:1]))
    require(all(any(determinant(a,b,p) < 0 for a,b in sides) for p in points), 'graph point not outside')
    require(all(not meet(points[i],points[j],a,b) for i,j in edges for a,b in sides), 'edge/polygon contact')
    bridge = Bridge(r+1,edges)
    for i,j in bridge.targets:
        q = tuple((a+b)/2 for a,b in zip(points[i],points[j]))
        require(all(determinant(a,b,q)>0 for a,b in sides), 'nonedge witness outside')
    clauses,rows = bridge.compile()
    assignment,conflicts = project(points,bridge)
    require(not conflicts and all(satisfied(c,assignment) for c in clauses), 'actual one-obstacle to CNF')
    return {'r':r,'n':r+1,'clauses':len(clauses),'nonedges':len(bridge.targets),'all_clauses_satisfied':True}


def crossed_key_paths():
    p = [(F(-2),F(0)),(F(2),F(3)),(F(-2),F(3)),(F(1),F(1)),
         (F(2),F(0)),(F(0),F(-1,2)),(F(-5),F(-4)),(F(8),F(-4))]
    require(all(determinant(*(p[i] for i in t)) for t in combinations(range(8),3)), 'crossed fixture GP')
    edges = [(0,1),(1,2),(2,3),(3,4),(0,5),(4,5)]
    b = Bridge(8,edges)
    assignment,conflicts = project(p,b)
    hit = next(c for c in conflicts if c['ab']==[0,4] and c['cd']==[6,7])
    q = (F(2,17),F(27,17))
    require(on(q,p[0],p[1]) and on(q,p[2],p[3]), 'loop cut coordinate')
    curve = [p[0],q,p[3],p[4],p[5]]
    sides = list(zip(curve,curve[1:]+curve[:1]))
    for i,j in combinations(range(len(curve)),2):
        if (i-j)%len(curve) in (1,len(curve)-1):
            continue
        require(not meet(*sides[i],*sides[j]), 'spliced curve not simple')
    require(all(not meet(p[6],p[7],a,b) for a,b in sides), 'open cd not separated')
    return {'points':[[str(v) for v in row] for row in p], 'edges':[list(e) for e in edges],
            'conflict':hit, 'loop_cut':[str(v) for v in q],
            'loop_erased_upper':[0,'loop_cut',3,4], 'lower':[0,5,4]}



def shared_endpoint():
    p = [(0,0),(3,0),(1,1),(2,-1),(-2,3)]
    require(all(determinant(*(p[i] for i in t)) for t in combinations(range(5),3)), 'shared endpoint GP')
    edges = [(0,2),(1,2),(0,3),(1,3)]
    b = Bridge(5,edges)
    _,conflicts = project(p,b)
    row = next(c for c in conflicts if c['ab'] == [0,1] and c['cd'] == [0,4])
    return {'points':[list(q) for q in p], 'edges':[list(e) for e in edges], 'conflict':row}


def main():
    b = Bridge(10,X4); clauses,rows = b.compile()
    old_n,old_c,old_counts = root_cnf.compile_cnf()
    require(old_n == b.size and old_c == clauses, 'new attribution compiler differs from C22')
    digest = sha(dimacs(b.size,clauses))
    require(digest == 'de54d35f78d3c7d84e24651e5ce6f82c9ebe6d78bc7bd2deb66aa591e6ea276c', 'frozen DIMACS')
    counts = source_origin_audit(b,clauses,rows)
    points = [(i,i*i) for i in range(10)]
    ids = rational_identities(points)
    negative_controls = []
    for data in (points,[(y,-x) for x,y in points],[(2*x+3,y-x) for x,y in points],[(-x,y) for x,y in points]):
        assignment,conflicts = project(data,b)
        require(conflicts, 'X4 numeric control unexpectedly has no local conflict')
        false = [i+1 for i,c in enumerate(clauses) if not satisfied(c,assignment)]
        require(false and all(rows[i-1][1][0] == 'K' for i in false), 'orientation clauses cannot fail')
        negative_controls.append({'conflicts':len(conflicts),'unsatisfied_key_rows':len(false),
                                  'first_conflict':conflicts[0]})
    degree = [sum(v in e for e in X4) for v in range(10)]
    closed = [{v}|{w for e in X4 if v in e for w in e} for v in range(10)]
    require(min(degree) > 0 and all(closed[a] != closed[b] for a,b in X4), 'X4 collision guard')
    rejected_gp = []
    for name,data in [('collinear',[(i,0) for i in range(10)]),
                      ('coincident',[points[0]]+points[:-1])]:
        try:
            project(data,b)
        except ValueError:
            rejected_gp.append(name)
        else:
            raise ValueError('GP projection accepted degenerate '+name)
    text = origin_text(rows)
    return {'verdict':'candidate_only','trusted_receipt':False,'cnf_sha256':digest,
            'variables':b.size,'clauses':len(clauses),'origin_families':counts,
            'origin_rows':len(rows),'origin_table_sha256':sha(text),'origin_table_bytes':len(text),
            'gp_domain_rejections':rejected_gp,'x4_degrees':degree,'x4_true_twins':[],
            'paths':sum(map(len,b.paths.values())), 'side_variables':len(b.sides),
            'boolean_elimination_cases':semantic_checks(),'exact_identities':ids,
            'positive_polygon_controls':[fan(r) for r in range(3,7)],
            'fixed_X4_negative_controls':negative_controls,'crossed_key_paths':crossed_key_paths(),
            'shared_endpoint':shared_endpoint(),'growth':amplification_controls(),
            'old_RUP_replayed_this_run':False,
            'limitation':'Clause attribution and finite semantic tests; C22 frozen RUP is a separate dependency.'}


if __name__ == '__main__':
    require(sys.argv[1:] in ([],['--origins']), 'arguments')
    if sys.argv[1:]:
        _,rows = Bridge(10,X4).compile()
        print(origin_text(rows).decode('ascii'),end='')
    else:
        print(json.dumps(main(),sort_keys=True,separators=(',',':')))
