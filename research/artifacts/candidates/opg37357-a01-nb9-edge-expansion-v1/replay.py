"""NB9 repository-only direct polygon/CNF replay and conditional set interface.
No network, process creation or dynamic evaluation. Reads three named inputs.
Generic geometric incidence reconstruction and margin generation are NOT imported.
"""
import json,sys,hashlib,copy
from fractions import Fraction as Q
from itertools import combinations
from polygon_verify import verify
from clause_generate import generate,dimacs
from clause_verify import check
from interface9 import analyze

def load(name):
 with open(name,encoding='utf-8') as f:s=f.read(1_000_001)
 if len(s)>1_000_000:raise ValueError('input byte cap')
 return json.loads(s)

def run(mode):
 G,W=load('input.json'),load('witness.json')
 if G['n']!=9 or G['edges']!=W['edges'] or W['n']!=9:raise ValueError('frozen graph mismatch')
 T=[list(t) for t in combinations(range(9),2) if list(t) not in G['edges']]
 if T!=G['nonedges']:raise ValueError('complete complement required')
 if mode=='polygon':return verify(W)
 if mode=='mutations':
  edits=[('duplicate_point',lambda x:x['points'].__setitem__(1,x['points'][0])),('duplicate_edge',lambda x:x['edges'].append(x['edges'][0])),('delete_edge',lambda x:x['edges'].pop()),('add_nonedge',lambda x:x['edges'].append([0,1])),('omit_hit',lambda x:x['witnesses'].pop()),('reorder_hits',lambda x:x['witnesses'].reverse()),('endpoint_hit',lambda x:x['witnesses'][0].__setitem__('parameter','0')),('wrong_point',lambda x:x['witnesses'][0].__setitem__('point',['0','0'])),('wrong_obstacle',lambda x:x['witnesses'][0].__setitem__('obstacle',0)),('duplicate_corner',lambda x:x['polygons'][0].__setitem__(1,x['polygons'][0][0])),('reverse_boundary',lambda x:x['polygons'][0].reverse()),('nested_obstacles',lambda x:x['polygons'].__setitem__(1,x['polygons'][0])),('vertex_contact',lambda x:x['polygons'][0].__setitem__(0,x['points'][0]))]
  rows=[]
  for name,edit in edits:
   x=copy.deepcopy(W);edit(x)
   try:verify(x)
   except (ValueError,TypeError,KeyError,IndexError) as e:rows.append({'name':name,'rejected':True,'reason':str(e)})
   else:raise ValueError('mutation accepted: '+name)
  return {'verdict':'candidate_only','rejected':len(rows),'tests':rows}
 F=generate(G)
 if mode=='cnf':sys.stdout.write(dimacs(F).decode());return None
 if mode in ('origins-a','origins-b'):
  cut=len(F['origins'])//2;start,end=(0,cut) if mode=='origins-a' else (cut,len(F['origins']))
  for i in range(start,end):print(json.dumps([i+1,F['origins'][i]],separators=(',',':')))
  return None
 if mode in ('omit','flip','guard','path'):
  if mode=='omit':F['clauses'].pop();F['origins'].pop()
  elif mode=='flip':F['clauses'][0][0]*=-1
  else:
   i=next(i for i,s in enumerate(F['origins']) if s[0]=='key')
   if mode=='path':F['origins'][i][3][0]=F['origins'][i][3][-1]
   else:
    q=len(F['triples']);k=len(F['targets']);F['clauses'][i].remove(next(v for v in F['clauses'][i] if q<abs(v)<=q+k))
  try:check(F)
  except ValueError as e:return {'mutation':mode,'rejected':True,'reason':str(e),'verdict':'candidate_only'}
  raise ValueError('damaged CNF accepted')
 if mode=='audit':
  C=dimacs(F);O=''.join(json.dumps([i+1,s],separators=(',',':'))+'\n' for i,s in enumerate(F['origins'])).encode()
  return {'verdict':'candidate_only','audit':check(F),'variables':F['variables'],'cnf_bytes':len(C),'cnf_sha256':hashlib.sha256(C).hexdigest(),'origins_bytes':len(O),'origins_sha256':hashlib.sha256(O).hexdigest(),'all_order_types_enumerated':False}
 if mode=='interface':
  D=load('fixed-incidence.json');f=D['components']
  if type(f) is not int or not 1<=f<=200 or [x['pair'] for x in D['targets']]!=T:raise ValueError('incidence domain')
  J=[x['incidence'] for x in D['targets']]
  if any(s!=sorted(set(s)) or any(type(v) is not int or not 0<=v<f for v in s) for s in J):raise ValueError('incidence labels')
  with open('witness.json','rb') as src:h=hashlib.sha256(src.read()).hexdigest()
  if h!=D['witness_sha256']:raise ValueError('incidence witness binding')
  R=analyze(F,[tuple(Q(x) for x in v) for v in W['points']],J,f)
  R['geometric_completeness_replayed']=False
  return R
 raise ValueError('unknown mode')

if __name__=='__main__':
 result=run(sys.argv[1] if len(sys.argv)==2 else 'polygon')
 if result is not None:print(json.dumps(result,sort_keys=True,separators=(',',':')))
