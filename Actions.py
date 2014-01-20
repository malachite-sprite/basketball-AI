#!/usr/bin/env python
# encoding: utf-8
"""
Actions.py
"""
def move_forward( player ):
    direction = player.team.basket_location
    if direction is "+":
        player.position.x = player.position.x + 1
    elif direction is "-":
        player.position.x = player.position.x - 1
    else:
        print "agh! something's wrong with the direction!"
        break

def move_backword( player ):
    direction = player.team.basket_location
    if direction is "+":
        player.position.x = player.position.x - 1
    elif direction is "-":
        player.position.x = player.position.x + 1
    else:
        print "agh! something's wrong with the direction!"
        break

def move_left( player ):
    direction = player.team.basket_location
    if direction is "+":
        player.position.y = player.position.x + 1
    elif direction is "-":
        player.position.y = player.position.x - 1
    else:
        print "agh! something's wrong with the direction!"
        break

def move_right( player ):
    direction = player.team.basket_location
    if direction is "+":
        player.position.y = player.position.x - 1
    elif direction is "-":
        player.position.y = player.position.x + 1
    else:
        print "agh! something's wrong with the direction!"
        break

def move_hold( player ):
    pass






