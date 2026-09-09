"""Finite nine-vertex triangulation flip census. No obstacle search."""
import networkx as nx
from itertools import combinations, permutations, product
import json,hashlib,time

def faces(G):
 ok,P=nx.check_planarity(G)
 if not ok:raise ValueError('nonplanar')
 seen=set();F=[]
 for a in sorted(G):
  for b in P.neighbors_cw_order(a):
   if (a,b) not in seen:F.append(P.traverse_face(a,b,seen))
 if len(F)!=2*len(G)-4 or any(len(f)!=3 for f in F):raise ValueError('not triangulated')
 return F,{v:list(P.neighbors_cw_order(v)) for v in G}

def flips(G):
 F,_=faces(G);opp={tuple(sorted(e)):[] for e in G.edges}
 for a,b,c in F:
  for u,v,w in [(a,b,c),(b,c,a),(c,a,b)]:opp[tuple(sorted((u,v)))].append(w)
 for e,ab in sorted(opp.items()):
  if len(ab)!=2:raise ValueError('face incidence')
  a,b=ab
  if G.has_edge(a,b):continue
  H=G.copy();H.remove_edge(*e);H.add_edge(a,b)
  yield e,tuple(sorted(ab)),H

def degree(G):return tuple(sorted(dict(G.degree()).values()))
def canon(G):
 # Fix increasing degree order, then minimize upper adjacency bit string.
 d=dict(G.degree());groups=[[v for v in G if d[v]==k] for k in sorted(set(d.values()))]
 best=None;bestorder=None
 for blocks in product(*(permutations(g) for g in groups)):
  order=sum((tuple(b) for b in blocks),())
  bits=tuple(int(G.has_edge(order[i],order[j])) for i,j in combinations(range(len(G)),2))
  if best is None or bits<best:best,bestorder=bits,order
 mapping={v:i for i,v in enumerate(bestorder)}
 H=nx.relabel_nodes(G,mapping)
 return H,''.join(map(str,best))

def main():
 n=9;G=nx.Graph();G.add_nodes_from(range(n));G.add_edges_from([(i,(i+1)%7) for i in range(7)]+[(i,h) for h in (7,8) for i in range(7)])
 reps=[G];buckets={degree(G):[0]};trans=[]
 for i,g in enumerate(reps):
  if len(reps)>100:raise ValueError('graph cap')
  for old,new,h in flips(g):
   key=degree(h);found=None
   for j in buckets.get(key,[]):
    M=nx.algorithms.isomorphism.GraphMatcher(h,reps[j])
    if M.is_isomorphic():found=j;break
   if found is None:
    found=len(reps);reps.append(h);buckets.setdefault(key,[]).append(found)
   trans.append([i,list(old),list(new),found])
 classes=[]
 for i,g in enumerate(reps):
  h,code=canon(g);F,R=faces(h)
  cuts=[list(s) for k in range(4) for s in combinations(range(n),k) if not nx.is_connected(h.subgraph(set(h)-set(s)))]
  hubs=[list(s) for s in combinations(range(n),2) if not h.has_edge(*s) and all(h.degree(v)==n-2 for v in s)]
  classes.append({'source_index':i,'n':n,'edges':[list(e) for e in sorted(tuple(sorted(e)) for e in h.edges)],'degree_sequence':list(degree(h)),'canonical_bits':code,'rotation':[R[v] for v in range(n)],'faces':F,'first_small_separator':cuts[0] if cuts else None,'nonadjacent_dominating_pairs':hubs})
 classes.sort(key=lambda d:(d['degree_sequence'],d['canonical_bits']))
 out={'schema':'next9-flip-census-v1','networkx':nx.__version__,'n':n,'graph_count':len(reps),'transition_count':len(trans),'classes':classes,'raw_flip_transitions':trans,'four_connected_classes':[c for c in classes if c['first_small_separator'] is None]}
 print(json.dumps(out,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
