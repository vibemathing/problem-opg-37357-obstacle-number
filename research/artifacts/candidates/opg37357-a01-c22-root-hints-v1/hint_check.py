"""C22 pure checker for positive-index RUP hints; no search or file access.
Each row is [new_clause_id, clause, ordered_existing_clause_reasons].
This is candidate source, not an admitted verifier identity.
"""


def ensure(test, message):
    if not test:
        raise ValueError(message)


def valid_clause(row, variables):
    ensure(type(row) in (list,tuple), 'clause shape')
    ensure(len(row)<=variables, 'clause length cap')
    ensure(all(type(x) is int and 1<=abs(x)<=variables for x in row),'literal range/type')
    ensure(len(set(row))==len(row), 'duplicate literal')
    ensure(not any(-x in row for x in row),'tautological clause')
    return tuple(row)


def verify(variables, initial, rows):
    ensure(type(variables) is int and 1<=variables<=2000,'variable cap')
    ensure(len(initial)<=100000 and 1<=len(rows)<=5000,'proof size cap')
    database = {i+1:valid_clause(c,variables) for i,c in enumerate(initial)}
    ensure(all(database.values()),'empty input clause unsupported by this format')
    reasons = 0
    for line,row in enumerate(rows):
        ensure(type(row) in (list,tuple) and len(row)==3,'proof row shape')
        identifier,clause,hints = row
        ensure(type(identifier) is int and identifier==len(database)+1,'ordered fresh clause id')
        clause = valid_clause(clause,variables)
        ensure(type(hints) in (list,tuple) and 1<=len(hints)<=variables+1,'reason count cap')
        # Literal membership is signed: true literals are stored as integers.
        assignment = {-lit for lit in clause}
        conflict = False
        for place,reason in enumerate(hints):
            ensure(type(reason) is int and 1<=reason<identifier,'future/invalid reason')
            premise = database[reason]
            ensure(not any(lit in assignment for lit in premise),'reason already satisfied')
            residual = [lit for lit in premise if -lit not in assignment]
            ensure(len(residual)<=1,'reason not unit or conflicting')
            if not residual:
                ensure(place==len(hints)-1,'steps after conflict')
                conflict = True
            else:
                assignment.add(residual[0])
            reasons += 1
        ensure(conflict,'missing final conflict')
        ensure(bool(clause) or line==len(rows)-1,'early empty clause')
        database[identifier] = clause
    ensure(not rows[-1][1],'proof does not end in empty clause')
    return {'accepted':True,'additions':len(rows),'reason_steps':reasons,
            'final_clause_id':len(database)}
