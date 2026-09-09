"""LAST9 exact half-plane cap check with direct whole-graph certificates.
Consumes explicit polygons; imports no constructor or incidence reconstruction.
"""
import json,sys
from fractions import Fraction as Q
from pathlib import Path
DEP=Path(__file__).resolve().parent.parent/'opg37357-a01-nb9-edge-expansion-v1';sys.path.insert(0,str(DEP))
from polygon_verify import verify,membership,cross
from parity_check import check as parity

def clip(P,positive):
 out=[]
 def f(p):return 12*p[0]+p[1]-Q(127,4)
 for a,b in zip(P,P[1:]+P[:1]):
  A,B=f(a),f(b);ia=A>=0 if positive else A<=0;ib=B>=0 if positive else B<=0
  if ia:out.append(a)
  if ia!=ib:
   t=A/(A-B);out.append(tuple((1-t)*x+t*y for x,y in zip(a,b)))
 return out

def exact(B):return [[str(x) for x in p] for p in B]

def audit(W,certificate=None):
 if sorted(b if a==1 else a for a,b in W['edges'] if 1 in (a,b))!=[2,5,7,8]:raise ValueError('new vertex neighborhood')
 P=[tuple(map(Q,x)) for x in W['polygons'][1]]
 if not all(cross(P[i-1],P[i],P[(i+1)%len(P)])>0 for i in range(len(P))):raise ValueError('convex P required')
 keep,cap=clip(P,False),clip(P,True);chord=set(keep)&set(cap)
 if len(chord)!=2 or not all(12*x+y==Q(127,4) for x,y in chord):raise ValueError('proper chord')
 C={'schema':'last9-cap-v1','new_vertex':1,'neighbors':[2,5,7,8],'removed_edge':[2,7],'halfplane':[12,1,'-127/4'],'parent_inner':exact(keep),'cap':exact(cap),'attachment_chord':exact(sorted(chord))}
 if certificate is not None and C!=certificate:raise ValueError('cap identity/coordinates mismatch')
 intermediate={**W,'edges':sorted(W['edges']+[[2,7]]),'polygons':[W['polygons'][0],exact(keep)],'witnesses':[h for h in W['witnesses'] if h['target']!=[2,7]]}
 inserted=verify(intermediate)
 labels=[0,2,3,4,5,6,7,8];ren={v:i for i,v in enumerate(labels)}
 parent={'n':8,'points':[W['points'][v] for v in labels],'edges':[[ren[a],ren[b]] for a,b in intermediate['edges'] if 1 not in (a,b)],'polygons':intermediate['polygons'],'witnesses':[{**h,'target':[ren[v] for v in h['target']]} for h in intermediate['witnesses'] if 1 not in h['target']]}
 old=verify(parent);final=verify(W)
 second=[parity(x) for x in (parent,intermediate,W)]
 h=next(h for h in W['witnesses'] if h['target']==[2,7]);hit=tuple(map(Q,h['point']))
 if membership(hit,cap)!=1:raise ValueError('strict cap hit')
 return C,{'verdict':'candidate_only','parent':old,'insertion_before_deletion':inserted,'final':final,'cap_corners':len(cap),'chord':C['attachment_chord'],'strict_deleted_edge_hit':h,'old_labels':labels,'second_consumer':second},parent

if __name__=='__main__':
 W=json.load(open('witness.json'));certificate=json.load(open('cap-certificate.json')) if Path('cap-certificate.json').exists() else None
 C,R,P=audit(W,certificate)
 if certificate is None:
  Path('cap-certificate.json').write_text(json.dumps(C,sort_keys=True,separators=(',',':'))+'\n');Path('parent-witness.json').write_text(json.dumps(P,sort_keys=True,separators=(',',':'))+'\n')
 print(json.dumps(R,sort_keys=True,separators=(',',':')))
