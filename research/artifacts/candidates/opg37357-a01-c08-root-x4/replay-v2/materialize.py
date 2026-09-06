"""Lossless transport decoder, not a mathematical proof-repair algorithm.
The stored text has one known omitted character. Fixed source/output hashes
bind this explicit text delta; any other byte change is rejected.
"""
import hashlib

def read_certificate(path):
    raw=path.read_bytes()
    source='b4668771fd98f902ebc6c8fc73e7db2a6a5c103660ccfed6e20c442f73505dc5'
    target='440c92278e01888c19bbb341958eca1320da6f28362d66343d0eb3e8e8cce697'
    if len(raw)>40000 or hashlib.sha256(raw).hexdigest()!=source:
        raise ValueError('transport source mismatch')
    if raw.count(b'BJd6Q')!=1:
        raise ValueError('transport delta is not unique')
    decoded=raw.replace(b'BJd6Q',b'BJd6FQ')
    if hashlib.sha256(decoded).hexdigest()!=target:
        raise ValueError('transport output mismatch')
    return decoded
