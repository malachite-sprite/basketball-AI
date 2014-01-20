#!/usr/bin/env python
# encoding: utf-8
"""
Position.py

A position. Stores three numbers: the x,y position as ints
and the tolerance of variance for that position.
-Tolerance must be >= 0. A tolerance of 0 means that
    the position MUST be that exact position.
-Patterns are practically immutable. They cannot be changed
    after being created.
-The distance between two positions is measured in the Manhattan
    metric.

To be used in Patterns and Pattern comparasons (see Pattern.py)

"""

class Position:
    
    x = 0
    y = 0
    tolerance = 0
    
    def __init__( self, _x, _y, _tolerance = 0 ):
        self.x = _x
        self.y = _y
        self.tolerance = _tolerance
    
    def distance_to( self, compare_to ):
        return abs( compare_to.x + compare_to.y - self.x - self.y )
    
    def __str__( self ):
        return self.to_string()
    
    def to_string( self ):
        return "( %i, %i, %i )" % (self.x, self.y, self.tolerance)
    
    @staticmethod
    def from_string( string ):
        components = string.replace(" ","").replace("(","").replace(")","").split(",")
        try:
            return Position( int( components[ 0 ] ), int( components[ 1 ] ), int( components[ 2 ] ) )
        except:
            return Position( int( components[ 0 ] ), int( components[ 1 ] ) )

