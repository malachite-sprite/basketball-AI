#!/usr/bin/env python
# encoding: utf-8
"""
Game.py
"""

from Team import Team
#from Display import Display

class Game:
    
    number_of_players_per_team = 5
    teams = []
    
    def __init__( self, team_file_1, team_file_2, board_file ):
        teams.append( Team( team_file_1, 1, 3 ) )
        teams.append( Team( team_file_2, -1, 3 ) )
    