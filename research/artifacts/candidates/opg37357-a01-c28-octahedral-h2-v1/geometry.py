"""C28 exact polygon and rotation-system consumer. No arrangement-core imports.
All inputs are finite rational data. Pure memory, no floats or external effects.
"""
from fractions import Fraction as F
from itertools import combinations


def require(ok, message):
    if not ok: raise ValueError(message)


def point(p):
    require(len(p)==2 and all(type(v) in (int,str) for v in p), 'rational point')
    q=tuple(F(v) for v in p)
    require(all(max(v.numerator.bit_length(),v.denominator.bit_length())<=256 for v in q),'bit cap')
    return q


def det(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def on(p,a,b):
    return det(a,b,p)==0 and (p[0]-a[0])*(p[0]-b[0])+(p[1]-a[1])*(p[1]-b[1])<=0


def meet(a,b,c,d):
    return det(a,b,c)*det(a,b,d)<0 and det(c,d,a)*det(c,d,b)<0 or any((on(a,c,d),on(b,c,d),on(c,a,b),on(d,a,b)))


def interior(p,polygon):
    winding=0
    for a,b in zip(polygon,polygon[1:]+polygon[:1]):
        if on(p,a,b): return False
        if a[1]<=p[1]<b[1] and det(a,b,p)>0:winding+=1
        if b[1]<=p[1]<a[1] and det(a,b,p)<0:winding-=1
    return winding!=0


def rotation_from_faces(faces):
    nexts=[{} for _ in range(6)]
    for face in faces:
        for i,v in enumerate(face):nexts[v][face[i-1]]=face[(i+1)%len(face)]
    result=[]
    for nxt in nexts:
        start=min(nxt); row=[start]
        while nxt[row[-1]]!=start:
            row.append(nxt[row[-1]]);require(len(row)<=5,'noncycle link')
        result.append(row)
    return result


def check_rotation(edges,rotation):
    es={tuple(sorted(e)) for e in edges}; require(len(es)==len(edges),'simple edge set')
    require(len(rotation)==6,'rotation size')
    for v,row in enumerate(rotation):
        require(len(set(row))==len(row) and set(row)=={w for e in es if v in e for w in e if w!=v},'rotation neighbors')
    darts={(a,b) for a,b in es}|{(b,a) for a,b in es};faces=[]
    while darts:
        start=min(darts);edge=start;face=[]
        while True:
            require(edge in darts,'face repeats dart');darts.remove(edge)
            a,b=edge;face.append(a);row=rotation[b];edge=(b,row[(row.index(a)+1)%len(row)])
            if edge==start:break
        faces.append(face)
    require(6-len(es)+len(faces)==2 and all(len(f)>=3 for f in faces),'sphere Euler/faces')
    return faces


def witness_data():
    faces=[[0,2,4],[0,4,3],[0,3,5],[0,5,2],[1,4,2],[1,3,4],[1,5,3],[1,2,5]]
    polygon=[[-10,100],[49,100],[49,-51],[51,-51],[51,100],
             [249,100],[249,-651],[251,-651],[251,100],
             [449,100],[449,-2051],[451,-2051],[451,100],[510,100],[510,200],[-10,200]]
    return {'points':[[100*i,-100*i*i] for i in range(6)],'polygon':polygon,
            'witnesses':[[50,-50],[250,-650],[450,-2050]],
            'rotation':rotation_from_faces(faces),'sphere_faces':faces,
            'domain':'fixed exact representation, graph-edge crossings allowed'}


def check_witness(data,formula,model):
    p=[point(q) for q in data['points']];poly=[point(q) for q in data['polygon']]
    require(len(p)==6 and len(set(p))==6 and 3<=len(poly)<=64 and len(set(poly))==len(poly),'vertex census')
    require(len(model)==formula['variables'] and all(abs(v)==i+1 for i,v in enumerate(model)),'model syntax')
    values=[v>0 for v in model]
    for i,t in enumerate(formula['orientation_triples']):
        d=det(*(p[v] for v in t));require(d and (d>0)==values[i],'orientation-coordinate binding')
    require(all(any(values[abs(v)-1]==(v>0) for v in c) for c in formula['clauses']),'CNF model')
    sides=list(zip(poly,poly[1:]+poly[:1]));pairs=0
    for i,j in combinations(range(len(poly)),2):
        if j-i not in (1,len(poly)-1):
            require(not meet(*sides[i],*sides[j]),'polygon self-contact');pairs+=1
    require(all(det(poly[i-1],poly[i],poly[(i+1)%len(poly)])!=0 for i in range(len(poly))),'flat/backtracking corner')
    require(all(not interior(q,poly) and all(not on(q,a,b) for a,b in sides) for q in p),'graph point in obstacle')
    tests=0
    for u,v in formula['edges']:
        for a,b in sides:require(not meet(p[u],p[v],a,b),'edge meets obstacle');tests+=1
    require(len(data['witnesses'])==len(formula['nonedges']),'witness count')
    for q,(a,b) in zip(data['witnesses'],formula['nonedges']):
        q=point(q); require(q==tuple((x+y)/2 for x,y in zip(p[a],p[b])) and interior(q,poly),'strict nonedge witness')
    faces=check_rotation(formula['edges'],data['rotation'])
    return {'graph_edge_polygon_side_tests':tests,'polygon_nonadjacent_side_pairs':pairs,
            'strict_nonedges':len(formula['nonedges']),'rotation_faces':faces,
            'corners':len(poly),'single_filled_simple_polygon_checked':True}
