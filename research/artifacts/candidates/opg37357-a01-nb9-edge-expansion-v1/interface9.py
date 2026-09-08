"""NB9 complete fixed-placement projection; never all-placement feasibility."""
from itertools import combinations

def need(ok,msg):
 if not ok:raise ValueError(msg)

def projection(F,signs):
 q=len(signs);k=len(F['targets']);forces={v['variable']:set() for v in F['side_variables']}
 for row in F['clauses']:
  if any(signs[abs(v)-1]==int(v>0) for v in row if abs(v)<=q):continue
  sides=[v for v in row if abs(v)>q+k]
  need(len(sides)==1,'residual row is not a guarded side row')
  need(len([v for v in row if q<abs(v)<=q+k])==2,'missing guards')
  forces[abs(sides[0])].add(int(sides[0]>0))
 index={tuple(t):i for i,t in enumerate(F['targets'])};bad=set()
 for info in F['side_variables']:
  if len(forces[info['variable']])==2:bad.add(tuple(sorted((index[tuple(info['ab'])],index[tuple(info['cd'])]))))
 # A second path-local derivation does not inspect generated clauses/origins.
 tri={tuple(t):signs[i] for i,t in enumerate(F['triples'])}
 def chi(a,b,c):
  t=(a,b,c);parity=sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))
  return tri[tuple(sorted(t))] ^ (parity%2)
 paths={tuple(x['target']):x['paths'] for x in F['paths']};direct={}
 for info in F['side_variables']:
  a,b=info['ab'];c,d=info['cd'];f=set()
  for P in paths[a,b]:
   C=[chi(c,d,v) for v in P if v not in (c,d)];J=[chi(a,b,v) for v in P[1:-1]]
   if len(set(C))==len(set(J))==1:f.add(J[0])
  direct[info['variable']]=f
 need(forces==direct,'clause/path side disagreement')
 models=[];validmask=0
 for code in range(1<<k):
  colors=[(code>>i)&1 for i in range(k)]
  if any(colors[a]==colors[b] for a,b in bad):continue
  side=[]
  for info in F['side_variables']:
   a,b=index[tuple(info['ab'])],index[tuple(info['cd'])];f=forces[info['variable']]
   side.append(next(iter(f)) if colors[a]==colors[b] and len(f)==1 else 0)
  m=signs+colors+side
  need(all(any(m[abs(l)-1]==int(l>0) for l in C) for C in F['clauses']),'model failure')
  validmask|=1<<code;models.append({'code':code,'bits':m})
 return models,validmask,sorted(bad)

def analyze(F,points,incidence,f):
 q=len(F['triples']);k=len(incidence);need(k<=15 and f<=200,'interface cap')
 signs=[]
 for a,b,c in F['triples']:
  A,B,C=points[a],points[b],points[c];v=(B[0]-A[0])*(C[1]-A[1])-(B[1]-A[1])*(C[0]-A[0]);need(v!=0,'vertex general position');signs.append(int(v>0))
 models,valid,bad=projection(F,signs);whole=(1<<(1<<k))-1
 bitmasks=[]
 for i in range(k):
  block=(1<<(1<<i))-1;mask=0
  for pos in range(1<<i,1<<k,2<<i):mask|=block<<pos
  bitmasks.append(mask)
 solutions=[];total=0
 for u in range(f):
  for v in range(f):
   mask=whole
   for i,J in enumerate(incidence):
    if u not in J:mask &= bitmasks[i]
    if v not in J:mask &= whole^bitmasks[i]
   # Compare the exact truth mask with direct membership for ALL surviving
   # guarded color models. Other labels are already excluded by necessary clauses.
   expected=[m['code'] for m in models if all((v if (m['code']>>i)&1 else u) in J for i,J in enumerate(incidence))]
   jointmask=mask&valid;got=[]
   while jointmask:
    bit=jointmask&-jointmask;got.append(bit.bit_length()-1);jointmask-=bit
   need(got==sorted(expected),'selector disagreement')
   total+=len(got)
   solutions.extend({'code':code,'components':[u,v]} for code in got)
 cores=[]
 for size in range(1,k+1):
  for S in combinations(range(k),size):
   if any(set(A)<=set(S) for A in cores):continue
   if not set.intersection(*(set(incidence[i]) for i in S)):cores.append(S)
 anchors=[]
 for u in range(f):
  missed=[i for i,J in enumerate(incidence) if u not in J];R=set(range(f))
  for i in missed:R.intersection_update(incidence[i])
  core=None if R else next(A for A in cores if set(A)<=set(missed))
  anchors.append({'first_component':u,'second_components':sorted(R),'empty_core':core})
 fixedrows=F['clauses']+[[i+1 if b else -i-1] for i,b in enumerate(signs)]
 base=F['variables']
 for r in (0,1):
  ys=[base+r*f+j+1 for j in range(f)];fixedrows.append(ys);fixedrows.extend([-a,-b] for a,b in combinations(ys,2))
  for i,J in enumerate(incidence):fixedrows.append([q+i+1 if r==0 else -q-i-1]+[base+r*f+j+1 for j in J])
 md={m['code']:m['bits'] for m in models};jointmodels=[]
 for sol in solutions:
  u,v=sol['components'];bits=md[sol['code']]+[int(j==u) for j in range(f)]+[int(j==v) for j in range(f)]
  need(all(any(bits[abs(l)-1]==int(l>0) for l in row) for row in fixedrows),'joint model failure');jointmodels.append(bits)
 return {'verdict':'candidate_only','fixed_direction_bits':signs,'relaxed_models':models,'conflict_pairs':bad,'component_solutions':solutions,'joint_models':jointmodels,'joint_variables':base+2*f,'joint_clauses':len(fixedrows),'represented_label_component_cases':(1<<k)*f*f,'explicit_component_pairs':f*f,'minimal_empty_families':cores,'anchors':anchors,'all_order_types_enumerated':False}
