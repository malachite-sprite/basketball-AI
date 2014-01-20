#!/usr/bin/env python
# encoding: utf-8
"""
Team.py
"""

from PAR import PAR
from Player import Player
from Position import Position

class Team:
    
    initial_positions = [ Position( ... ) ]
    
    roster = []
    memory = []
    basket_location = None
    
    def __init__( self, filename, _basket_location, number_of_players=5 ):
        basket_location = _basket_location
        try:    
            for i in range( number_of_players ):
                roster.append( Player( team, initial_positions[ i ] ) )
        except:
            "Not enough initial positions specified to support this number of players!"
        try:
            open( filename, "r" ) as temp:
            line = ""
            memories = []
            while line is not "endfile":
                memories.append( PAR.from_string( line ) )
                line = temp.next()
            temp.close()
        except Exception as hell:
            print "Whoops, something broke when trying to read from " + filename + "!"
            raise hell
    
    def save( self ):
        pass
        #return toreturn + "\nendfile"
    
