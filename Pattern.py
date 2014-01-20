#!/usr/bin/env python
# encoding: utf-8
"""
Pattern.py

The basic pattern. Each pattern consists of a list of player positions (See position.py).

Patterns are, like positions, practically immutable.

Patterns are comparable, as well. The algorithm for comparason runs as follows:
 Each position in the primary Pattern (where there ordering is, 'if primary_pattern
  equals secondary_pattern:' -- N.B. a == b is NOT the same as b == a) finds the nearest
  position in the compare_to pattern. If that position not within the tolerance then
  the two patterns are not "equal". Otherwise, move on to the next position. At the end
  of the loop, the two positions must be "equal"

"""

from Position import Position

class Pattern:
    
    state = []
    
    def __init__( self, _state ):
        self.state = _state
    
    def __eq__( self, compare_to ):
        for position in self.state:
            closest_position = 0
            distance = 0
            nearest_distance = -1
            for compare_position in compare_to.state:
                distance = compare_position.distance_to( position )
                if nearest_distance == -1 or distance < nearest_distance:
                    nearest_distance = distance
                    compare_position = closest_position
            if nearest_distance > position.tolerance:
                return False
        return True
    
    def __str__( self ):
            toreturn = "[ "
            for position in self.state:
                toreturn = toreturn + str( position ) + "; "
            return toreturn + "]"
    
    @staticmethod
    def from_string( string ):
        components = string.replace("[","").replace("]","").replace(" ","").split(";")
        state = []
        for position in components:
            if position is not "":
                state.append( Position.from_string( position ) )
        return Pattern( state )
    
