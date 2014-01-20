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
    
    def __str__( self ):
        return = "{ %s: %s: %f }" % ( str( pattern ), str( action ), result )
    
    @staticmethod
    def from_string( string ):
        components = string.replace(" ","").replace("{","").replace("}","").split(":")
        pattern = Pattern.from_string( components[ 0 ] )
        action = Action.from_string( components[ 1 ] )
        result = float( components[ 2 ] )
        return PAR( pattern, action, result )
    
