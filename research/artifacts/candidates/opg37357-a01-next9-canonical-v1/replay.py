"""NEXT9 bounded direct witness, catalog, local surgery and CNF audit.
Existing NB9 modules are SHA-bound, not copied into this candidate.
"""
import json,sys,hashlib,copy
from pathlib import Path
from fractions import Fraction as Q
from struct import pack,unpack
ROOT=Path(__file__).resolve().parent
DEP=ROOT.parent/'opg37357-a01-nb9-edge-expansion-v1'
DIGESTS={'polygon_verify.py':'6a89082083c356b53082bc59bc8c7c6084b75ea8ee68627c65b489e5b85b5e74','clause_generate.py':'73d6325d59812c772e5140f2061b2b1cc7e97d6125ed57df0cb9283d29bc2134','interface9.py':'e230316805a352cdcfb25d65f92248ed59d6d5ce4ec126eed3a8b3ed6e919e70'}
for name,h in DIGESTS.items():
 if hashlib.sha256((DEP/name).read_bytes()).hexdigest()!=h:raise ValueError('dependency digest '+name)
sys.path.insert(0,str(DEP))
from polygon_verify import verify
from clause_generate import generate
from interface9 import analyze
from compact_verify import check
from closure_check import audit,read_catalog
from ear_check import check as check_ear

def load(name):
 b=(ROOT/name).read_bytes()
 if len(b)>1048576:raise ValueError('input byte cap')
 return json.loads(b)

def need(x,m):
 if not x:raise ValueError(m)

def run(mode):
 G,W=load('input.json'),load('witness.json');E=load('ear-certificate.json')
 need(G['edges']==W['edges'] and G['n']==W['n']==9,'frozen graph')
 if mode=='polygon':return verify(W)
 if mode=='ear':return check_ear(W,E)
 if mode=='catalog':return audit(read_catalog((ROOT/'catalog.tsv').read_text()))
 if mode=='mutations':
  edits=[('duplicate_point',lambda x:x['points'].__setitem__(1,x['points'][0])),('duplicate_edge',lambda x:x['edges'].append(x['edges'][0])),('delete_edge',lambda x:x['edges'].pop()),('add_nonedge',lambda x:x['edges'].append([0,1])),('omit_hit',lambda x:x['witnesses'].pop()),('endpoint_hit',lambda x:x['witnesses'][0].__setitem__('parameter','0')),('wrong_hit',lambda x:x['witnesses'][0].__setitem__('point',['0','0'])),('wrong_obstacle',lambda x:x['witnesses'][0].__setitem__('obstacle',1)),('duplicate_corner',lambda x:x['polygons'][0].__setitem__(1,x['polygons'][0][0])),('reverse_orientation',lambda x:x['polygons'][0].reverse()),('overlap_obstacles',lambda x:x['polygons'].__setitem__(1,x['polygons'][0])),('vertex_contact',lambda x:x['polygons'][1].__setitem__(0,x['points'][0]))]
  out=[]
  def reject(name,fn):
   try:fn()
   except (ValueError,IndexError,KeyError,TypeError) as e:out.append({'name':name,'rejected':True,'reason':str(e)})
   else:raise ValueError('mutation accepted '+name)
  for name,edit in edits:
   x=copy.deepcopy(W);edit(x);reject(name,lambda:verify(x))
  bad=copy.deepcopy(E);bad['added_cap'].pop();reject('cap_omission',lambda:check_ear(W,bad))
  bad=copy.deepcopy(W);bad['polygons'][1]=E['parent_inner'];reject('no_cap_blocks_deleted_edge',lambda:verify(bad))
  D=read_catalog((ROOT/'catalog.tsv').read_text());D['classes'].pop();reject('missing_isomorphism_class',lambda:audit(D))
  D=read_catalog((ROOT/'catalog.tsv').read_text());D['classes'][0]['rotation'][0][:2]=list(reversed(D['classes'][0]['rotation'][0][:2]));reject('bad_rotation',lambda:audit(D))
  for v in range(-309,310):need(unpack('>h',pack('>h',v))[0]==v,'packing roundtrip')
  return {'verdict':'candidate_only','mutations':out,'rejected':len(out),'int16_roundtrips':619}
 F=generate(G)
 if mode in ('omit','guard','path','flip'):
  if mode=='omit':F['clauses'].pop();F['origins'].pop()
  elif mode=='flip':F['clauses'][0][0]*=-1
  else:
   i=next(i for i,s in enumerate(F['origins']) if s[0]=='key')
   if mode=='path':F['origins'][i][3][0]=F['origins'][i][3][-1]
   else:F['clauses'][i].remove(next(v for v in F['clauses'][i] if 84<abs(v)<=99))
  try:check(F)
  except ValueError as e:return {'verdict':'candidate_only','mutation':mode,'rejected':True,'reason':str(e)}
  raise ValueError('bad clause accepted')
 if mode=='audit':
  result=check(F);H=hashlib.sha256();O=hashlib.sha256();cb=ob=0
  b=('p cnf %d %d\n'%(F['variables'],len(F['clauses']))).encode();H.update(b);cb+=len(b)
  for c in F['clauses']:
   b=(' '.join(map(str,c))+' 0\n').encode();H.update(b);cb+=len(b)
  for i,s in enumerate(F['origins']):
   b=(json.dumps([i+1,s],separators=(',',':'))+'\n').encode();O.update(b);ob+=len(b)
  return {'verdict':'candidate_only','audit':result,'variables':F['variables'],'cnf_bytes':cb,'cnf_sha256':H.hexdigest(),'origins_bytes':ob,'origins_sha256':O.hexdigest(),'encoding':'lossless signed int16 expected-set consumption; same clauses, no relaxation'}
 if mode=='interface':
  D=load('incidence.json');need(D['witness_sha256']==hashlib.sha256((ROOT/'witness.json').read_bytes()).hexdigest(),'witness binding')
  need([t['pair'] for t in D['targets']]==G['nonedges'],'incidence target census')
  R=analyze(F,[tuple(map(Q,p)) for p in W['points']],[t['incidence'] for t in D['targets']],D['components'])
  R['geometric_completeness_replayed']=False
  return R
 if mode=='cnf':
  print('p cnf',F['variables'],len(F['clauses']))
  for c in F['clauses']:print(*c,0)
  return None
 if mode in ('origins-a','origins-b'):
  m=len(F['origins'])//2;start,end=(0,m) if mode=='origins-a' else (m,len(F['origins']))
  for i in range(start,end):print(json.dumps([i+1,F['origins'][i]],separators=(',',':')))
  return None
 raise ValueError('unknown mode')
if __name__=='__main__':
 R=run(sys.argv[1] if len(sys.argv)==2 else 'polygon')
 if R is not None:print(json.dumps(R,sort_keys=True,separators=(',',':')))
