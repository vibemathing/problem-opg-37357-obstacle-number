"""Standard-library consumer of a complete finite flip-closed catalog."""
from itertools import combinations,permutations,product
import json

def require(x,m):
 if not x:raise ValueError(m)

def canonical(n,E):
 N=[{b if a==i else a for a,b in E if i in (a,b)} for i in range(n)]
 deg=[len(s) for s in N];groups=[[i for i in range(n) if deg[i]==d] for d in sorted(set(deg))]
 best=None;bestp=None
 for blocks in product(*(permutations(g) for g in groups)):
  p=sum((tuple(x) for x in blocks),());v=0
  for i in range(n):
   for j in range(i+1,n):v=(v<<1)+int(p[j] in N[p[i]])
  if best is None or v<best:best=v;bestp=p
 return format(best,'0%db'%(n*(n-1)//2)),{v:i for i,v in enumerate(bestp)}

def rotation_faces(n,E,R):
 require(len(R)==n,'rotation size');N=[set() for _ in range(n)]
 for a,b in E:N[a].add(b);N[b].add(a)
 require(all(len(R[i])==len(N[i]) and set(R[i])==N[i] for i in range(n)),'rotation neighbors')
 todo={(a,b) for a,b in E}|{(b,a) for a,b in E};F=[]
 while todo:
  first=min(todo);edge=first;vs=[]
  for _ in range(2*len(E)+1):
   require(edge in todo,'dart reentry');todo.remove(edge);a,b=edge;vs.append(a)
   edge=(b,R[b][(R[b].index(a)-1)%len(R[b])])
   if edge==first:break
  else:raise ValueError('dart cap')
  F.append(vs)
 require(n-len(E)+len(F)==2 and all(len(f)==3 for f in F),'sphere triangles')
 return F

def connected(n,E,S):
 V=set(range(n))-set(S)
 if not V:return False
 root=min(V);seen={root};todo=[root]
 for x in todo:
  for a,b in E:
   y=b if a==x else a if b==x else None
   if y in V and y not in seen:seen.add(y);todo.append(y)
 return seen==V

def audit(D):
 n=D['n'];require(n==9 and len(D['classes'])<=100,'census cap')
 bycode={c['canonical_bits']:c for c in D['classes']};codes=set(bycode);require(len(codes)==len(D['classes']),'duplicate class')
 transitions=[];four=[];permutations_checked=0
 for i,C in enumerate(D['classes']):
  E=set(map(tuple,C['edges']));require(len(E)==3*n-6 and all(0<=a<b<n for a,b in E),'edge domain')
  require(canonical(n,E)[0]==C['canonical_bits'],'noncanonical')
  require(connected(n,E,()),'not connected')
  F=rotation_faces(n,E,C['rotation']);around={e:[] for e in E}
  for a,b,c in F:
   for u,v,w in [(a,b,c),(b,c,a),(c,a,b)]:around[tuple(sorted((u,v)))].append(w)
  for old,W in sorted(around.items()):
   require(len(W)==2 and W[0]!=W[1],'two incident faces');new=tuple(sorted(W))
   if new in E:continue
   code,ren=canonical(n,(E-{old})|{new});require(code in codes,'missing legal flip')
   u,v=old
   x=next(f[(f.index(u)+2)%3] for f in F if u in f and f[(f.index(u)+1)%3]==v)
   y=next(f[(f.index(v)+2)%3] for f in F if v in f and f[(f.index(v)+1)%3]==u)
   moved=[f for f in F if not ({u,v}<=set(f))]+[[u,y,x],[v,x,y]]
   cyc=lambda t:min(tuple(t[i:]+t[:i]) for i in range(3))
   images={cyc([ren[a] for a in f]) for f in moved}
   target=rotation_faces(n,set(map(tuple,bycode[code]['edges'])),bycode[code]['rotation'])
   direct={cyc(f) for f in target};mirror={cyc(list(reversed(f))) for f in target}
   require(images==direct or images==mirror,'flip embedding mismatch')
   transitions.append([i,list(old),list(new),code])
  bad=next((list(S) for k in range(4) for S in combinations(range(n),k) if not connected(n,E,S)),None)
  require(bad==C['first_small_separator'],'separator classification')
  if bad is None:four.append(C['canonical_bits'])
 require(len(transitions)==D['transition_count'],'transition census')
 require(any(c['nonadjacent_dominating_pairs'] for c in D['classes']),'missing seed class')
 return {'verdict':'candidate_only','catalog_classes':len(codes),'all_legal_flip_transitions_checked':len(transitions),'embedded_isomorphisms_checked':len(transitions),'four_connected_codes':four,'scope':'n=9 catalog closure plus external spherical flip-connectivity theorem; not placements','networkx_used_by_consumer':False}
def read_catalog(text):
 lines=text.splitlines();header=lines.pop(0).split('\t')
 require(header[0]=='next9-rotation-catalog-v1' and header[1]=='9','header')
 classes=[]
 for line in lines:
  code,rr,cut=line.split('\t');require(len(code)==36 and set(code)<={'0','1'},'code')
  E=[list(e) for e,b in zip(combinations(range(9),2),code) if b=='1']
  degree=[sum(i in e for e in E) for i in range(9)]
  classes.append({'canonical_bits':code,'edges':E,'rotation':[[int(v) for v in r.split(',')] for r in rr.split(';')], 'first_small_separator':None if cut=='-' else [int(v) for v in cut.split(',')], 'nonadjacent_dominating_pairs':[list(s) for s in combinations(range(9),2) if list(s) not in E and all(degree[v]==7 for v in s)]})
 require(len(classes)==int(header[2]),'class count')
 return {'n':9,'classes':classes,'transition_count':int(header[3])}
