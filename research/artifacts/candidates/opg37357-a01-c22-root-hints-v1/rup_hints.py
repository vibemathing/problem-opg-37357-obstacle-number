"""C22 two-watch RUP-to-explicit-reasons producer, pure in-memory.
The consumer hint_check.py does not use watches or this producer.
"""
from collections import defaultdict, deque
from hint_check import ensure, valid_clause


def parse_rup(data, variables):
    ensure(type(data) is bytes and len(data)<=1000000,'RUP byte cap')
    result = []
    for line in data.decode('ascii').splitlines():
        words = line.split()
        ensure(1<=len(words)<=variables+1 and words[-1]=='0','RUP terminator')
        clause = valid_clause([int(x) for x in words[:-1]],variables)
        result.append(clause)
    ensure(1<=len(result)<=5000 and not result[-1],'RUP final clause')
    ensure(all(result[:-1]),'RUP early empty clause')
    return result


def produce(variables, initial, additions):
    database,positions,units = [],[],[]
    watching = defaultdict(list)
    def insert(clause):
        cid = len(database)
        database.append(tuple(clause))
        if len(clause)==1:
            positions.append(None); units.append(cid)
        elif clause:
            positions.append([0,1])
            watching[clause[0]].append(cid); watching[clause[1]].append(cid)
        else:
            positions.append(None)
    for clause in initial:
        ensure(bool(clause),'initial empty clause')
        insert(valid_clause(clause,variables))
    rows = []
    for clause in additions:
        clause = valid_clause(clause,variables)
        values = [0]*(variables+1)
        queue = deque()
        hints = []
        def value(lit):
            return values[abs(lit)]*(1 if lit>0 else -1)
        def assign(lit):
            ensure(value(lit)==0,'duplicate assignment in producer')
            values[abs(lit)] = 1 if lit>0 else -1
            queue.append(lit)
        for lit in clause:
            assign(-lit)
        conflict = False
        for cid in units:
            lit = database[cid][0]
            if value(lit)>0:
                continue
            hints.append(cid+1)
            if value(lit)<0:
                conflict = True; break
            assign(lit)
        while queue and not conflict:
            false_lit = -queue.popleft()
            affected = watching[false_lit]
            index = 0
            while index<len(affected):
                cid = affected[index]; premise = database[cid]; pair = positions[cid]
                slot = 0 if premise[pair[0]]==false_lit else 1
                ensure(premise[pair[slot]]==false_lit,'watch index invariant')
                other_pos = pair[1-slot]; other = premise[other_pos]
                if value(other)>0:
                    index += 1; continue
                replacement = next((j for j,x in enumerate(premise)
                                    if j!=other_pos and value(x)>=0),None)
                if replacement is not None:
                    pair[slot] = replacement
                    affected[index] = affected[-1]; affected.pop()
                    watching[premise[replacement]].append(cid)
                    continue
                hints.append(cid+1)
                if value(other)<0:
                    conflict = True; break
                assign(other); index += 1
        ensure(conflict,'RUP addition not justified')
        rows.append([len(database)+1,list(clause),hints])
        insert(clause)
    return rows
