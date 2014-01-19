#!/usr/bin/env python
# encoding: utf-8
"""
PAR.py
The main componant for learing and the basic block of a "memory". 

"""
from Pattern import Pattern
class PAR:
    
    pattern = None
    action = None
    result = None
    
    def __init__( self, _pattern, _action, _result ):
        pattern = _pattern
        action = _action
        result = _result
    
