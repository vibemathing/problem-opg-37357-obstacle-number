"""Run C21's second replay against four immutable C20 JSON certificates.
Local JSON reads only; no network, child processes, or dynamic code loading.
Usage: python replay.py DIRECTORY_CONTAINING_C20_CERTIFICATES
"""
import copy
import hashlib
import json
from pathlib import Path
import platform
import sys
import time
from certificate_recheck import recheck
from arrangement_model import Model
from exact_primitives import require
from strict_cells import strict_witness

PINS = {
 'c18_negative.certificate.json':'307717b13e0e756c2a5cd09d3575473d59c3aee6bf5e416756c1fde1ae0603e6',
 'forced_line_witness.certificate.json':'bfb059d6f8c1f31128a1255992416e99ecd98068f26ece4ae06b953f8ac27e33',
 'square_diagonals.certificate.json':'bc71008cc8b04e24f46ba90940ced13f808beabe7a9609d04c4f2f7d59b0a362',
 'tiny_open_gap.certificate.json':'c4646e4ac9b91a2e36b1179ff8cf47f1a9f1a872d76f55921518d045fa373e1f'}


def unique_object(items):
    result = {}
    for key,value in items:
        require(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def reject_number(text):
    raise ValueError('floating or nonfinite JSON number')


def load(path):
    require(path.stat().st_size<=1000000, 'input byte cap')
    data = path.read_bytes()
    require(hashlib.sha256(data).hexdigest()==PINS[path.name], 'frozen input hash')
    return json.loads(data,object_pairs_hook=unique_object,
                      parse_float=reject_number,parse_constant=reject_number)


def set_at(obj,path,value):
    for key in path[:-1]:
        obj = obj[key]
    obj[path[-1]] = value


def main(directory):
    started = time.monotonic()
    certs,results = {},[]
    for name in sorted(PINS):
        certs[name] = load(Path(directory)/name)
        results.append({'file':name,'sha256':PINS[name],**recheck(certs[name])})
    positive = certs['forced_line_witness.certificate.json']
    negative = certs['c18_negative.certificate.json']
    mutations = [
      ('drop_cell',positive,['cells'],positive['cells'][:-1]),
      ('wrong_sign',positive,['cells',0,'signs'],[1]),
      ('bool_label',positive,['cells',0,'component'],False),
      ('drop_cut',positive,['line_cuts',0],['-1','1']),
      ('drop_face',positive,['faces'],positive['faces'][:-1]),
      ('whole_line_barrier',positive,['faces',0,'blocked'],True),
      ('open_covered_face',positive,['faces',2,'blocked'],False),
      ('portal_at_vertex',positive,['faces',1,'sample'],['0','0']),
      ('free_graph_vertex',positive,['zero_faces',0,'blocked'],False),
      ('omit_zero',positive,['zero_faces'],positive['zero_faces'][:-1]),
      ('wrong_partition',positive,['components'],[[0],[1]]),
      ('omit_target',positive,['nonedges'],positive['nonedges'][:-1]),
      ('omit_interval',positive,['nonedges',0,'intervals'],[]),
      ('wrong_interval_cut',positive,['nonedges',0,'cuts'],['0','1']),
      ('false_incidence',positive,['nonedges',0,'components'],[]),
      ('false_locator',positive,['nonedges',0,'intervals',1,'location','id'],0),
      ('invent_common',negative,['common_components'],[0]),
      ('wrong_exclusion',negative,['construction','exclusions',0,'pair'],[0,6]),
      ('endpoint_witness',positive,['construction','vertices',1,'parameter'],'0'),
      ('duplicate_vertex',positive,['construction','vertices',2,'point'],['1/5','0']),
      ('center_on_K',positive,['construction','vertices',0,'point'],['0','0']),
      ('drop_tree_edge',positive,['construction','edges'],[[0,1]]),
      ('wrong_tree_role',positive,['construction','vertices',0,'kind'],'witness'),
      ('wrong_tube_count',positive,['construction','tube_corner_bound'],3),
    ]
    rejected = []
    for name,base,path,value in mutations:
        item = copy.deepcopy(base);set_at(item,path,value)
        try:
            recheck(item)
        except (ValueError,KeyError,TypeError,IndexError,ZeroDivisionError):
            rejected.append(name)
        else:
            raise ValueError('accepted damage: '+name)
    tiny = '1/10000000000000000000000000000000000000000'
    cases = [
      ('empty',[],[],1,True),
      ('point',[[0,0]],[],1,True),
      ('finite_edge',[[0,0],[1,0]],[[0,1]],1,True),
      ('forced_line',[[-1,0],[0,0],[1,0]],[[0,1]],1,True),
      ('vertex_on_edge',[[0,0],[1,0],[2,0]],[[0,2]],1,False),
      ('overlap',[[0,0],[1,0],[2,0],[3,0]],[[0,2],[1,3]],1,False),
      ('coincident_gapped',[[-3,0],[-2,0],[2,0],[3,0]],[[0,1],[2,3]],1,True),
      ('free_concurrence',[[2,0],[3,0],[0,2],[0,3],[2,2],[3,3]],[[0,1],[2,3],[4,5]],1,True),
      ('forbidden_concurrence',[[-1,0],[1,0],[0,-1],[0,1],[0,0]],[[0,1],[2,3]],1,False),
      ('puncture',[[-1,0],[0,0],[1,0]],[],1,True),
      ('near_parallel',[[0,0],[1,0],[0,tiny],[1,'2/'+tiny.split('/')[1]]],[[0,1],[2,3]],1,True),
      ('tiny_gap',[[-2,0],[0,0],[tiny,0],[2,0]],[[0,1],[2,3]],1,True),
    ]
    controls = []
    for name,pts,edges,count,exists in cases:
        model = Model({'points':pts,'edges':edges})
        require(len(model.components)==count and bool(model.common)==exists, 'control '+name)
        controls.append({'name':name,'components':count,'fixed_drawing_exists':exists})
    strict_cases = [([(1,0,0),(-1,0,0)],False),
                    ([(1,0,0),(-1,0,1)],True),
                    ([(1,1,0),(-1,-1,0)],False),
                    ([(1,1,0),(-1,-1,1)],True)]
    for rows,answer in strict_cases:
        require((strict_witness(rows) is not None)==answer, 'strict inequality smoke')
    return {'verdict':'candidate_only','trusted_verifier_receipt':False,
            'core_relation':'new strict-Fourier-Motzkin core; no C20 code imported',
            'python':platform.python_version(),'implementation':platform.python_implementation(),
            'certificates':results,'rejected_mutations':rejected,'controls':controls,
            'strict_smoke_cases':len(strict_cases),'elapsed_seconds':round(time.monotonic()-started,6)}


if __name__=='__main__':
    require(len(sys.argv)==2, 'provide exactly one certificate directory')
    print(json.dumps(main(sys.argv[1]),sort_keys=True,separators=(',',':')))
