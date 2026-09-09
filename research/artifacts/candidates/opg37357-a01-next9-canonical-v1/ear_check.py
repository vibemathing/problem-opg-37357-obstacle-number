"""Exact local cap-transfer checker. No construction/arrangement dependency."""
from fractions import Fraction as Q
from polygon_verify import verify,cross

def need(x,m):
 if not x:raise ValueError(m)

def clip(P,positive):
 f=lambda p:9*p[0]+p[1]-Q(225,16)
 out=[]
 for a,b in zip(P,P[1:]+P[:1]):
  A,B=f(a),f(b);ia=A>=0 if positive else A<=0;ib=B>=0 if positive else B<=0
  if ia:out.append(a)
  if ia!=ib:
   t=A/(A-B);out.append(tuple((1-t)*x+t*y for x,y in zip(a,b)))
 return out

def check(W,E):
 need(E['new_vertex']==3 and E['removed_edge']==[2,7] and E['new_neighbors']==[2,5,6,7],'expansion identity')
 P=[tuple(map(Q,p)) for p in W['polygons'][1]]
 need(all(cross(P[i-1],P[i],P[(i+1)%len(P)])>0 for i in range(len(P))),'convex final obstacle')
 small=clip(P,True);cap=clip(P,False);S=lambda B:[[str(x) for x in p] for p in B]
 need(S(small)==E['parent_inner'] and S(cap)==E['added_cap'],'cap data')
 chord=set(small)&set(cap);need(len(chord)==2,'proper nonzero attachment chord')
 need(all(9*x+y==Q(225,16) for x,y in chord),'chord line')
 # H+edge27 is the provisional point insertion before blocking edge27.
 M=dict(W);M['edges']=sorted(W['edges']+[[2,7]]);M['polygons']=[W['polygons'][0],S(small)]
 M['witnesses']=[h for h in W['witnesses'] if h['target']!=[2,7]]
 intermediate=verify(M)
 labels=[0,1,2,4,5,6,7,8];index={v:i for i,v in enumerate(labels)}
 parent={'n':8,'points':[W['points'][v] for v in labels],'edges':[[index[a],index[b]] for a,b in M['edges'] if 3 not in (a,b)],'polygons':M['polygons'],'witnesses':[{**h,'target':[index[v] for v in h['target']]} for h in M['witnesses'] if 3 not in h['target']]}
 parent_result=verify(parent);final=verify(W)
 hit=next(h for h in W['witnesses'] if h['target']==[2,7]);x,y=map(Q,hit['point'])
 need(9*x+y<Q(225,16),'deleted edge hit is in cap interior')
 return {'verdict':'candidate_only','parent':parent_result,'point_insertion':intermediate,'expanded':final,'cap_corners':len(cap),'attachment_chord':[list(map(str,p)) for p in sorted(chord)],'lemma_scope':'one explicit instance of conditional cap-assisted edge expansion, not an unconditional monotonicity theorem'}
