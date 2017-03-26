'''Contains functions that are used for setting up the game.
'''

import random


def init(player_stats):
    '''Sets initial values for the relevant variables, through user input, a set sequence or
    randomization.'''
    BOARD_NR_OF_ROWS = 10  # Determines how many rows the playing field contains.
    BOARD_NR_OF_ITEMS_PER_ROW = 10  # Determines how many items (or columns) each row contains.

    # Init the 2 player boards with "~" characters
    for i in range(0, BOARD_NR_OF_ROWS):
        player_stats[player1_board].append("~" * BOARD_NR_OF_ITEMS_PER_ROW)
        player_stats[player2_board].append("~" * BOARD_NR_OF_ITEMS_PER_ROW)

    




    return player_stats