"""C21 semantic consumer for complete C20 certificates; pure in-memory input.
Cells are rederived by exhaustive strict elimination, not by the producer.
"""
from exact_primitives import require, rational, point, value, parameter, subtract
from arrangement_model import Model, open_interval
from tree_recheck import check_tree


def same(actual, expected, message):
    require(type(actual) is type(expected) and actual == expected, message)
    if isinstance(expected, list):
        for a,b in zip(actual,expected):
            same(a,b,message)
    if isinstance(expected, dict):
        for key in expected:
            same(actual[key],expected[key],message)


def recheck(cert):
    require(type(cert) is dict, 'certificate object')
    same(sorted(cert), sorted(['schema','verdict','domain','input','support_lines',
        'line_cuts','cells','faces','zero_faces','components','nonedges',
        'common_components','exists_connected_obstacle','construction']), 'certificate keys')
    same(cert['schema'],'c20-arrangement-certificate-v1','schema')
    same(cert['verdict'],'candidate_only','verdict')
    same(cert['domain'],'fixed_injective_rational_drawing','domain')
    m = Model(cert['input'])
    same(cert['support_lines'],[list(line) for line in m.lines],'support-line census')
    require(len(cert['line_cuts'])==len(m.cuts),'line-cut rows')
    for row,expected in zip(cert['line_cuts'],m.cuts):
        require([rational(v) for v in row]==expected,'complete line cuts')
    require(len(cert['cells'])==len(m.signs),'complete cell census')
    for i,(row,signs) in enumerate(zip(cert['cells'],m.signs)):
        same(row['signs'],list(signs),'cell sign vector')
        q = point(row['sample'])
        require(not m.blocked(q),'cell sample forbidden')
        require(all(s*value(line,q)>0 for s,line in zip(signs,m.lines)), 'cell sample signs')
        same(row['component'],m.labels[i],'cell label')
    require(len(cert['faces'])==len(m.faces),'complete face census')
    for row,(i,lo,hi,cells,is_blocked) in zip(cert['faces'],m.faces):
        same(row['line'],i,'face line index')
        require((None if row['lo'] is None else rational(row['lo']))==lo,'face lower cut')
        require((None if row['hi'] is None else rational(row['hi']))==hi,'face upper cut')
        q = point(row['sample']);r,v = m.frames[i]
        require(value(m.lines[i],q)==0,'face sample off line')
        require(open_interval(parameter(q,r,v),lo,hi),'face sample at/beyond cut')
        same(row['cells'],cells,'incident cells')
        same(row['blocked'],is_blocked,'face coverage')
        require(m.blocked(q)==is_blocked,'sample coverage disagreement')
    require(len(cert['zero_faces'])==len(m.zeros),'complete zero-face census')
    for row,q in zip(cert['zero_faces'],m.zeros):
        require(point(row['point'])==q,'zero-face coordinates')
        same(row['blocked'],m.blocked(q),'zero-face coverage')
        same(row['incident_cells'],m.incident(q),'zero-face incidence')
        if not m.blocked(q):
            require(len({m.labels[i] for i in m.incident(q)})==1,'free concurrence splits labels')
    same(cert['components'],m.components,'component partition')
    require(len(cert['nonedges'])==len(m.targets),'full nonedge census')
    interval_count = 0
    for row,pair in zip(cert['nonedges'],m.targets):
        same(row['pair'],list(pair),'nonedge pair')
        cuts = m.target_cuts[pair]
        require([rational(v) for v in row['cuts']]==cuts,'nonedge cut completeness')
        require(len(row['intervals'])==len(cuts)-1,'interval completeness')
        a,b = [m.points[i] for i in pair]
        for interval,lo,hi in zip(row['intervals'],cuts,cuts[1:]):
            require(rational(interval['lo'])==lo and rational(interval['hi'])==hi,'interval endpoints')
            q = point(interval['sample'])
            require(lo<parameter(q,a,subtract(b,a))<hi,'interval sample position')
            status = m.blocked(q)
            same(interval['blocked'],status,'interval coverage')
            same(interval['location'],None if status else m.locate(q),'sample face/cell locator')
            interval_count += 1
        same(row['components'],m.incidence[pair],'complete incidence set')
    same(cert['common_components'],m.common,'total intersection')
    same(cert['exists_connected_obstacle'],bool(m.common),'existence flag')
    tree = check_tree(cert['construction'],m)
    return {'accepted':True,'cells':len(m.signs),'faces':len(m.faces),
            'components':len(m.components),'nonedge_intervals':interval_count,
            'common_components':m.common,'fixed_drawing_exists':bool(m.common),**tree}
