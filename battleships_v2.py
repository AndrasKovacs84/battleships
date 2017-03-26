import random
import os
import sys
import string
import itertools
import copy
from game_init_conf import *

#  Dict variable containing all the relevant player data
player_stats = {"player1_turn": True,  # Used to determing whose turn it is.
                "player1_name": "",  # Input name, must be char, if too long, truncated.
                "player1_board": [],  # shows where the ships are, list (rows) of lists (0-9 coords)
                "player1_ship_list": [],  # Contains lists for each ship. Each list consists of 2 long lists for coords.
                "player2_name": "Computer",  # Init as "computer", if it's a 2 player game, overwrite with user input.
                "player2_board": []  # same as for player 1
                "player2_ship_list": [],  # Same as before
                "invalid_coords": []  # Contains restrictions on where the next ship can NOT be placed due to proximity.
                }

# Dict containing settings
game_conf = {"new_game_switch": False,  # When checking any input, break cycle and reset the whole game.
             "game_events": [],  # Used as a game log of previous events
             "single_player": False,  # decides if it will be a 2 player game or vs AI.
             }

AI = {"first_hit": [],  # Used to determine logic when AI picks next target, detailed explanation in __insert__
      "second_hit": [],  # Same as above
      "acceptable_target_coords": [],  # Coords that can be considered as next target based on goond strat and validity.
      }