"""
This file contains the function calls to execute the game.
This should be the only place you have code outside of functions, and the more
code within functions the better. You should call the functions defined in the
other modules (setup_game, player_actions, enemy_actions). You are free to
define additional functions and modules if needed, but these should be in
addition to existing functions, rather than replacements.

Note: to call functions from other modules, you need to
include the module name; e.g. setup_game.create_grid()
"""

from setup_game import *
from player_actions import *
from enemy_actions import *
# add any other imports you feel are relevant here

if __name__ == "__main__":
    # this is where the code should go that runs the game.
    # you can leave the following line in or take it out, up to you:
    print("PIRATES!")
    difficulty = int(input("Difficulty >"))
    sizeofgrid = int(input("Size of grid >"))
    create_grid(sizeofgrid)
  
    # add any other code you feel is relevant here
