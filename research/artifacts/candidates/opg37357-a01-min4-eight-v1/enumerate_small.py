from itertools import combinations
import networkx as nx,json
A=nx.graph_atlas_g();allreps={str(n):[] for n in range(5,9)};extensions=0
for n in range(5,8):
 for idx,H in enumerate(A):
  if len(H)==n and H.number_of_edges()==(n-3)*(n-4)//2 and max(dict(H.degree()).values())<=n-5:allreps[str(n)].append((H,{'atlas':idx}))
for idx,H in enumerate(A):
 if len(H)!=7 or max(dict(H.degree()).values())>3:continue
 d=10-H.number_of_edges()
 if not 0<=d<=3:continue
 for ns in combinations([v for v in H if H.degree(v)<3],d):
  extensions+=1;J=H.copy();J.add_node(7);J.add_edges_from((v,7) for v in ns)
  if not any(nx.is_isomorphic(J,R) for R,_ in allreps['8']):allreps['8'].append((J,{'deleted_complement_atlas':idx,'new_neighbors':list(ns)}))
out={}
for key,reps in allreps.items():
 n=int(key);rr=[]
 for H,origin in reps:
  G=nx.complement(H);rec={'complement':sorted(tuple(sorted(e)) for e in H.edges()),'origin':origin}
  cut=next((list(s) for k in range(4) for s in combinations(range(n),k) if not nx.is_connected(nx.subgraph(G,set(G)-set(s)))),None)
  if cut is not None:rec.update(kind='separator',separator=cut)
  else:
   ok,em=nx.check_planarity(G,counterexample=True)
   if not ok:rec.update(kind='nonplanar',kuratowski=sorted(tuple(sorted(e)) for e in em.edges()))
   else:rec.update(kind='admissible',rotation=[list(em.neighbors_cw_order(v)) for v in range(n)],hub_pairs=[list(s) for s in combinations(range(n),2) if not G.has_edge(*s) and all(G.degree(v)==n-2 for v in s)])
  rr.append(rec)
 out[key]=rr
print(json.dumps({'networkx_version':nx.__version__,'atlas_count':len(A),'atlas_extensions':extensions,'complement_representatives':out},sort_keys=True,separators=(',',':')))
