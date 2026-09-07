"""C28 complete bit-parallel enumeration of <=2^20 orientation tables.
No sampling, no solver, no old compiler imports. Side variables are eliminated
exactly. One bit position denotes one lexicographically indexed truth table.
"""
from guarded import require, extend, value


def truth_masks(d):
    require(type(d) is int and 0<=d<=20, 'direction bit cap')
    count=1<<d; universe=(1<<count)-1
    masks=[]
    for i in range(d):
        block=1<<(d-1-i)
        pattern=((1<<block)-1)<<block
        width=2*block
        while width<count:
            pattern |= pattern<<width
            width*=2
        masks.append(pattern)
    return universe,masks


def enumeration(enc):
    nd=len(enc.triples); U,positive=truth_masks(nd)
    def literal(q):
        return positive[q-1] if q>0 else U^positive[-q-1]
    allowed=U
    four=five=0
    for clause,origin in zip(enc.clauses,enc.origins):
        if origin[0]=='key': continue
        r=0
        for q in clause: r |= literal(q)
        allowed &= r
        if origin[0]=='four': four+=1
        else: five+=1
    conflict={}
    for s,t in enc.pairs:
        a,b=s;c,d=t; forced=[0,0]
        for path in enc.paths[s]:
            K=[enc.lit(c,d,v) for v in path if v not in t]
            J=[enc.lit(a,b,v) for v in path[1:-1]]
            allpos=allneg=U
            for q in K:
                allpos &= literal(q);allneg &= literal(-q)
            key=allpos|allneg
            for side in (0,1):
                inter=U
                for q in J: inter &= literal(q if side else -q)
                forced[side] |= key & inter
        conflict[s,t]=forced[0]&forced[1]
    counts=[]; accepted=0; model=None
    for z in range(1<<len(enc.targets)):
        ok=allowed
        for i,s in enumerate(enc.targets):
            for j,t in enumerate(enc.targets):
                if i>=j:continue
                if ((z>>(len(enc.targets)-1-i))&1)==((z>>(len(enc.targets)-1-j))&1):
                    ok &= U^(conflict[s,t]|conflict[t,s])
        counts.append(ok.bit_count());accepted|=ok
        if ok:
            first=(ok&-ok).bit_length()-1
            if model is None or (first,z)<tuple(model[:2]):model=[first,z]
    if model:
        assignment=extend(enc,*model)
        require(assignment is not None and all(value(c,assignment) for c in enc.clauses),'enumerated minimum model check')
        model.append(assignment)
    return {'verdict':'candidate_only','result':'SAT' if model else 'UNSAT',
            'all_orientation_tables':1<<nd,'orientation_tables_passing_four_five':allowed.bit_count(),
            'all_orientation_label_pairs':1<<(nd+len(enc.targets)),
            'accepted_projected_pairs':sum(counts),'orientations_with_some_two_labeling':accepted.bit_count(),
            'counts_by_color_word':counts,'minimum_model':model,
            'side_projection':'exact existential elimination; not a claim to enumerate real placements',
            'direction_realizability_decided':False}
