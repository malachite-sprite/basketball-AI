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

To be used in Patterns and Pattern comparasons (see Pattern.py)

"""

class Position:
    
    x, y, tol = null
    
	def __init__(self, int _x, int _y):
		x=_x, y=_y, tol=0
	
	def __init__(self, int _x, int _y, int _tol):
	    x=_x, y=_y, tol=_tol
	
	def get_x():
        return x
    
    def get_y():
        return y
    
    def get_tol():
        return tol
    

