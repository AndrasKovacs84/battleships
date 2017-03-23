import random
import os
import copy


def init():
    os.system('clear')                              # inicialize the global variables of the game
    global player1_turn
    global player1_name

    global player2_name

    global current_event
    current_event = ""
    global player1_board
    player1_board = []
    global player2_board
    player2_board = []
    global player1_ship5
    player1_ship5 = []
    global player1_ship4
    player1_ship4 = []
    global player1_ship3
    player1_ship3 = []
    global player2_ship5
    player2_ship5 = []
    global player2_ship4
    player2_ship4 = []
    global player2_ship3
    player2_ship3 = []
    global coord
    coord = []
    for i in range(0, 10):
        player1_board.append(["~"] * 10)    # fill up playerboards with tildes "~"
    for i in range(0, 10):                  #
        player2_board.append(["~"] * 10)    #
    player1_turn = True
    player1_name = input("Player 1's name: ")
    player2_name = input("Player 2's name: ")
    player1_turn = True  # by default player1 starts the game


coord = []
first_hit = []
second_hit = []



def AI_pick_shooting_coordinate():
    global coord
    global first_hit
    global second_hit
    global acceptable_target_coords
    acceptable_target_coords = []  # A list of coordinates for potential next shot
    coords_to_remove_from_acceptable_targets = []
    if first_hit == []:
        # if there are no hits yet, then just shoot at a random coordinate.
        x = random.randrange(0, 9)
        y = random.randrange(0, 9)
        coord.append(x) 
        coord.append(y)
        shot(coord, player1_turn)
        if player1_board[coord[0]][coord[1]] == "O":
            first_hit = copy.deepcopy(coord)

    elif first_hit != [] and second_hit == []:
        # first hit is not empty, but we have no second_hit yet, pick a coord near first_hit
        # can only consider future coords in the 4 cardinal directions!
        acceptable_target_coords.append([first_hit[0] + 1, first_hit[1]])
        acceptable_target_coords.append([first_hit[0] - 1, first_hit[1]])
        acceptable_target_coords.append([first_hit[0], first_hit[1] - 1])
        acceptable_target_coords.append([first_hit[0], first_hit[1] + 1])
        '''
        only needed for later stage
        # also include diagonally adjacent cells
        acceptable_target_coords.append([first_hit[0] + 1, first_hit[1] + 1])
        acceptable_target_coords.append([first_hit[0] - 1, first_hit[1] + 1])
        acceptable_target_coords.append([first_hit[0] + 1, first_hit[1] - 1])
        acceptable_target_coords.append([first_hit[0] - 1, first_hit[1] - 1])
        print("acceptable coords list: ", acceptable_target_coords)
        second_hit = random.choice(acceptable_target_coords)
        '''
        #  delete potential coordinates that cannot exist (out of bounds from the board)
        for coords in acceptable_target_coords:
            for index in coords:
                if index < 0 or index > 9:
                    coords_to_remove_from_acceptable_targets.append(coords)
        print("indices to delete: ", coords_to_remove_from_acceptable_targets)
        for coords in coords_to_remove_from_acceptable_targets:
            acceptable_target_coords.remove(coords)
        # pick a random coordinate from the remaining list of reasonable targets
        print("acceptable coords list: ", acceptable_target_coords)
        second_hit = random.choice(acceptable_target_coords)

if __name__ == "__main__":
    AI_pick_shooting_coordinate()
    print("first hit: ", first_hit)
    AI_pick_shooting_coordinate()
    print("second hit: ", second_hit)
