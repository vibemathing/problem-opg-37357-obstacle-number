"""C28 public bounded entry. Prints ordinary JSON/DIMACS; no files or network."""
import json
import sys
from seed import seed, completion, validate_embedding
from producer import make, dimacs
from audit import complete_census


def main(code=0):
    g=completion(code); embedding=validate_embedding(g)
    f=make(g['n'],g['edges'])
    return {'graph':g,'embedding':embedding,'formula_counts':f['counts'],
            'clause_count':len(f['clauses']),'variables':f['variables'],
            'census':complete_census(f)}


if __name__=='__main__':
    if len(sys.argv)==3 and sys.argv[1]=='--completion':
        print(json.dumps(main(int(sys.argv[2])),sort_keys=True,separators=(',',':')))
    elif sys.argv[1:]==['--cnf']:
        g=seed(); print(dimacs(make(g['n'],g['edges'])),end='')
    elif sys.argv[1:]==['--formula']:
        g=seed(); print(json.dumps(make(g['n'],g['edges']),sort_keys=True,separators=(',',':')))
    elif not sys.argv[1:]:
        print(json.dumps(main(),sort_keys=True,separators=(',',':')))
    else:
        raise ValueError('arguments: none, --cnf, --formula')
