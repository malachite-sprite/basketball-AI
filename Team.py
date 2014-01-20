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
    
    def __init__( self, filename, basket_location, number_of_players=5 ):
        if basket_location is not "+" or "-":
            print "Basket location needs to be either '+' or '-'!"
            break
        else:
            try:    
                for i in range( number_of_players ):
                    roster.append( Player( team, initial_positions[ i ], basket_location ) )
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
    
