# Battleship
import random
import os
import sys
import string
import itertools
import copy


def init():
    os.system('clear')                              # initialize the global variables of the game
    global player1_turn #
    player1_turn = random.choice((True, False))
    global player1_name #
    player1_name = ""
    global player2_name #
    player2_name = ""
    global current_event #
    current_event = ""
    global new_game_switch #
    new_game_switch = False
    global player1_board #
    player1_board = []
    global player2_board #
    player2_board = []
    global coord
    coord = []
    global first_hit #
    first_hit = []
    global second_hit #
    second_hit = []
    global acceptable_target_coords #
    acceptable_target_coords = []
    global invalid_coords # 
    invalid_coords = []
    global player1_ship_list #
    player1_ship_list = []
    global player2_ship_list #
    player2_ship_list = []
    chosen_option = ""
    global single_player #
    single_player = True
    for i in range(0, 10):
        player1_board.append(["~"] * 10)    # fill up playerboards with tildes "~"
    for i in range(0, 10):                  #
        player2_board.append(["~"] * 10)    #

    # Start deploying ships, deploy 1 by 1 or random?

    while True:

        print("Choose an option:", "\n",
              "1 - play against another player", "\n",
              "2 - play against AI")
        chosen_option = input("enter option: ")
        os.system("clear")
        if chosen_option == "1":
            single_player = False
            break
        elif chosen_option == "2":
            single_player = True
            break
        else:
            print("incorrect option, try again.")
            continue

    if single_player is True:
        player1_name = input("Player 1's name: ")
        # player 1 goes first for ship deployment
        os.system("clear")
        print("SHIP PLACEMENT FOR", player1_name.upper(), "\n",
              "Choose an option:", "\n",
              "1 - manual ship placement", "\n",
              "2 - random ship placement")
        chosen_option = input("enter option: ")
        os.system("clear")
        if chosen_option == "1":  # manual ship placement
            for ship_length in range(3, 6):  # 1 of each length of ships
                show_board(player1_board, player2_board, True)
                player1_ship_list.append(set_ship(ship_length))

        elif chosen_option == "2":  # random placement
            for i in range(0, 2):
                for ship_length in range(3, 6):
                    player1_ship_list.append(rand_ship_placement(ship_length, True))
            invalid_coords = []
        for i in range(0, 2):
            for ship_length in range(3, 6):
                    player2_ship_list.append(rand_ship_placement(ship_length, False))

    elif single_player is False:
        # initialize ships for player 1
        while True:
            if player1_name == "":
                player1_name = input("Player 1 name: ")
                # player 1 goes first for ship deployment
                os.system("clear")
                print("SHIP PLACEMENT FOR", player1_name.upper(), "\n",
                      "Choose an option:", "\n",
                      "1 - manual ship placement", "\n",
                      "2 - random ship placement")
                chosen_option = input("enter option: ")
                os.system("clear")
                if chosen_option == "1":  # manual ship placement
                    for ship_length in range(3, 6):  # 1 of each length of ships
                        show_board(player1_board, player2_board, True)
                        player1_ship_list.append(set_ship(ship_length))
                elif chosen_option == "2":  # random placement
                    for ship_length in range(3, 6):
                        player1_ship_list.append(rand_ship_placement(ship_length, True))
                continue
                # initialize ships for player 2
            elif player2_name == "":
                player2_name = input("Player 2 name: ")
                # player 1 goes first for ship deployment
                os.system("clear")
                print("SHIP PLACEMENT FOR", player2_name.upper(), "\n",
                      "Choose an option:", "\n",
                      "1 - manual ship placement", "\n",
                      "2 - random ship placement")
                chosen_option = input("enter option: ")
                os.system("clear")

                if chosen_option == "1":  # manual ship placement
                    for ship_length in range(3, 6):  # 1 of each length of ships
                        show_board(player1_board, player2_board, False)
                        player2_ship_list.append(set_ship(ship_length))

                elif chosen_option == "2":  # random placement
                    for ship_length in range(3, 6):
                        player2_ship_list.append(rand_ship_placement(ship_length, False))
            break


def rand_ship_placement(length, whose_turn):
    global invalid_coords
    global player1_board
    global player2_board

    all_coords = list(range(0, 10))  # contains possible values for X and Y coordinates
    coords1 = []
    coords2 = []

    # starts to generate the length long ship
    while True:
        random_ship = []
        coords1 = []
        coords2 = []

        slice_start = random.randrange(0, len(all_coords) - (length - 1))  # set the start of slicing
        slice_end = slice_start + length                             # set the end of slicing
        coords1.append(all_coords[slice_start:slice_end])       # slices a 3 long piece of list from "all_coords"

        # generate a random sequence with length nr of neighbouring numbers between 0 and 10
        rand_num = random.randrange(0, 10)
        for i in range(length):
            coords2.append(rand_num)

        # randomly decides whether coords1 or coords2 represents the horizontal coordinates on the gameboard
        # "random_ship" will be filled up with coordinates
        if random.choice((True, False)):
            for i in range(length):
                random_ship.append([coords1[0][i], coords2[i]])
        else:
            for i in range(length):
                random_ship.append([coords2[i], coords1[0][i]])
        acceptable_ship = [item for item in random_ship if item not in invalid_coords]
        if len(acceptable_ship) < length:
            continue
        elif len(acceptable_ship) == length:
            break

    # Ship created, update invalid_coords with the new additions
    for i in random_ship:
        invalid_coords.append(i)

    for i in random_ship:
        invalid_coords.append([(i[0] - 1), i[1]])
        invalid_coords.append([(i[0] + 1), i[1]])
        invalid_coords.append([i[0], (i[1] - 1)])
        invalid_coords.append([i[0], (i[1] + 1)])
        invalid_coords.append([(i[0] - 1), (i[1] - 1)])
        invalid_coords.append([(i[0] + 1), (i[1] + 1)])
        invalid_coords.append([(i[0] - 1), (i[1] + 1)])
        invalid_coords.append([(i[0] + 1), (i[1] - 1)])

    invalid_coords.sort()
    invalid_coords = list(invalid_coords for invalid_coords, _ in itertools.groupby(invalid_coords))

    for coord_pair in random_ship:
        if whose_turn:
            player1_board[coord_pair[0]][coord_pair[1]] = "S"
        else:
            player2_board[coord_pair[0]][coord_pair[1]] = "S"

    return random_ship


def AI_pick_shooting_coordinate():
    global coord
    coord = []
    global first_hit
    global second_hit
    global player1_board
    board_w_hidden_ships = copy.deepcopy(player1_board)

    if first_hit != []:
        if player1_board[first_hit[0]][first_hit[1]] == "+":
            first_hit = []
            second_hit = []

    for row in range(len(board_w_hidden_ships)):
        for item in range(len(board_w_hidden_ships[row])):
            if board_w_hidden_ships[row][item] == "S":
                board_w_hidden_ships[row][item] = "~"

    acceptable_target_coords = []  # A list of coordinates for potential next shot
    coords_to_remove_from_acceptable_targets = []
    if first_hit == []:
        # no new ship found, build a list of potential coordinates (all "unshot" coords)
        for row in range(len(board_w_hidden_ships)):
            for item in range(len(board_w_hidden_ships[row])):
                if board_w_hidden_ships[row][item] == "~":
                    acceptable_target_coords.append([row, item])
                else:
                    continue
        # pick a coord from the list of viable options, then shoot it.
        coord = random.choice(acceptable_target_coords)
        shot(coord, False)
        # if the shot is a hit, register it as the starting point for future logical decision.
        if player1_board[coord[0]][coord[1]] == "O":
            first_hit = copy.deepcopy(coord)

    elif first_hit != [] and second_hit == []:
        # first hit is not empty, but we have no second_hit yet, pick a coord near first_hit
        # can only consider future coords in the 4 cardinal directions!
        acceptable_target_coords.append([first_hit[0] + 1, first_hit[1]])
        acceptable_target_coords.append([first_hit[0] - 1, first_hit[1]])
        acceptable_target_coords.append([first_hit[0], first_hit[1] - 1])
        acceptable_target_coords.append([first_hit[0], first_hit[1] + 1])

        #  delete potential coordinates that cannot exist (out of bounds from the board)
        for coords in acceptable_target_coords:
            for index in coords:
                if index < 0 or index > 9:
                    coords_to_remove_from_acceptable_targets.append(coords)
        for coords in coords_to_remove_from_acceptable_targets:
            acceptable_target_coords.remove(coords)
        # pick a random coordinate from the remaining list of reasonable targets
        coord = random.choice(acceptable_target_coords)
        shot(coord, player1_turn)
        if player1_board[coord[0]][coord[1]] == "O":
            second_hit = copy.deepcopy(coord)

    elif first_hit != [] and second_hit != []:
        # got 2 hits, now we know along which axis we need to shoot
        # start building the list of acceptable targets
        if first_hit[0] == second_hit[0]:  # if the x coords match, that means we need to search along the y axis
            i = 1
            # append the list of acceptable targets
            while True:  # start adding eligible coords towards +y
                #  if the coord is not ~ and we are not at the edge of the board, then keep searching
                if board_w_hidden_ships[first_hit[0]][first_hit[1] + i] != "~" and (first_hit[1] + i) <= 9:
                    if board_w_hidden_ships[first_hit[0]][first_hit[1] + i] == "X":
                        break
                    i += 1
                    continue
                # when ~ is found, append the coordinate
                elif board_w_hidden_ships[first_hit[0]][first_hit[1] + i] == "~":
                    acceptable_target_coords.append([first_hit[0], first_hit[1] + i])
                    break
                # no ~ is found, but we reached the edge of the board, do nothing, search other way
                else:
                    break
            i = 1  # reset the iterator so that we can start again in the other direction
            while True:  # start adding eligible coords towards -y
                #  if the coord is not ~ and we are not at the edge of the board, then keep searching
                if board_w_hidden_ships[first_hit[0]][first_hit[1] - i] != "~" and (first_hit[1] - i) >= 0:
                    if board_w_hidden_ships[first_hit[0]][first_hit[1] - i] == "X":
                        break
                    i += 1
                    continue
                # when ~ is found, append the coordinate
                elif board_w_hidden_ships[first_hit[0]][first_hit[1] - i] == "~":
                    acceptable_target_coords.append([first_hit[0], first_hit[1]-i])
                    break
                # no ~ is found, but we reached the edge of the board, do nothing, search other way
                else:
                    break
            # pick a target coordinate from the list of acceptable targets.
            coord = random.choice(acceptable_target_coords)
            shot(coord, player1_turn)
            if player1_board[coord[0]][coord[1]] == "O":
                second_hit = copy.deepcopy(coord)

        elif first_hit[1] == second_hit[1]:  # if the y coords match, that means we need to search along the x axis
            i = 1
            # append the list of acceptable targets
            while True:  # start adding eligible coords towards +x
                #  if the coord is not ~ and we are not at the edge of the board, then keep searching
                if board_w_hidden_ships[first_hit[0] + i][first_hit[1]] != "~" and (first_hit[0] + i) <= 9:
                    if board_w_hidden_ships[first_hit[0] + i][first_hit[1]] == "X":
                        break
                    i += 1
                    continue
                # when ~ is found, append the coordinate
                elif board_w_hidden_ships[first_hit[0] + i][first_hit[1]] == "~":
                    acceptable_target_coords.append([first_hit[0] + i, first_hit[1]])
                    break
                # no ~ is found, but we reached the edge of the board, do nothing, search other way
                else:
                    break
            i = 1
            while True:  # start adding eligible coords towards -x
                #  if the coord is not ~ and we are not at the edge of the board, then keep searching
                if board_w_hidden_ships[first_hit[0] - i][first_hit[1]] != "~" and (first_hit[0] - i) >= 0:
                    if board_w_hidden_ships[first_hit[0] - i][first_hit[1]] == "X":
                        break
                    i += 1
                    continue
                # when ~ is found, append the coordinate
                elif board_w_hidden_ships[first_hit[0] - i][first_hit[1]] == "~":
                    acceptable_target_coords.append([first_hit[0]-i, first_hit[1]])
                    break
                # no ~ is found, but we reached the edge of the board, do nothing, search other way
                else:
                    break
            # pick a target coordinate from the list of acceptable targets.
            coord = random.choice(acceptable_target_coords)
            shot(coord, player1_turn)
            if player1_board[coord[0]][coord[1]] == "O":
                second_hit = copy.deepcopy(coord)


def menu_keys(key):                         # handles user input for starting a new game or quitting
    if key == "q":
        sys.exit(0)
    elif key == "n":
        new_game_switch = True


def input_and_check():      # checks validity of user input

    x = ""  # checks if user input is a valid letter
    y = ""
    valid_char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    coord = []
    while True:
        x = input("input x coordinate (A-J): ")
        x = x.lower()
        menu_keys(x)
        if x in valid_char_list:
            x = valid_char_list.index(x)
            break
        else:
            print("invalid coordinate, x needs to be a letter between (A-J): ")
            continue
    while True:  # checks if user input is a valid number
        y = input("input y coordinate (1-10): ")
        menu_keys(y)
        if y.isdigit():
            y = int(y) - 1
            if y >= 0 and y <= 9:
                break
            else:
                print("invalid coordinate, y needs to be a number between (1-10): ")
            continue
        else:
            print("invalid coordinate, y needs to be a number between (1-10): ")
            continue
    coord.append(y)
    coord.append(x)
    return coord


def show_board(player1_board, player2_board, whose_turn):   # shows the player boards
    current_player_board = []
    enemy_player_board = []
    current_player_name = ""
    current_line = ""
    if whose_turn:                                    # checks whose turn is the game at in accordance with "whose_turn"
        current_player_name = player1_name
        current_player_board = player1_board
        enemy_player_board = player2_board
    else:
        current_player_name = player2_name
        current_player_board = player2_board
        enemy_player_board = player1_board

    # "clear" the screen and print a header
    os.system('clear')
    print(current_player_name + "'s turn")
    print("=================================================", "\n")
    print("   Player's ships             Previous shots")
    print("   A B C D E F G H I J        A B C D E F G H I J")

    for i in range(0, 10):
        current_line = ""
        # print the player board on the left
        if i < 9:
            print(i + 1, sep=" ", end="  ")
        else:
            print(i + 1, sep=" ", end=" ")
        for j in range(0, 10):
            print(current_player_board[i][j], sep=" ", end=" ", flush=True)

        # add spacing between the two boards
        print("   ", sep=" ", end=" ")

        # print the enemy board on the right
        if i < 9:
            print(i + 1, sep=" ", end="  ")
        else:
            print(i + 1, sep=" ", end=" ")
        for j in range(0, 10):
            current_line = current_line + str(enemy_player_board[i][j]) + " "
        print(current_line.replace("S", "~"))
        # the following seems to be needed to print in the following line... ("\n" skips a line)


def shot(shot, whose_turn):
    global player1_board
    global player2_board

    if single_player is False or (single_player is True and whose_turn is True):
        while True:
            shot = input_and_check()
            shotX = int(shot[0])
            shotY = int(shot[1])

            if whose_turn and player2_board[shotX][shotY] == "S":
                player2_board[shotX][shotY] = "O"
                break
            elif whose_turn and player2_board[shotX][shotY] == "~":
                player2_board[shotX][shotY] = "X"
                break
            elif whose_turn and player2_board[shotX][shotY] == "X" or player2_board[shotX][shotY] == "O":
                print("coordinate already shot, choose another one!")
                continue

            if whose_turn is False and player1_board[shotX][shotY] == "S":
                player1_board[shotX][shotY] = "O"
                break
            elif whose_turn is False and player1_board[shotX][shotY] == "~":
                player1_board[shotX][shotY] = "X"
                break
            elif whose_turn is False and player1_board[shotX][shotY] == "X" or player1_board[shotX][shotY] == "O":
                print("coordinate already shot, choose another one!")
                continue

    elif single_player is True and whose_turn is False:
        shotX = int(shot[0])
        shotY = int(shot[1])
        if player1_board[shotX][shotY] == "S":
            player1_board[shotX][shotY] = "O"
        elif player1_board[shotX][shotY] == "~":
            player1_board[shotX][shotY] = "X"


def set_ship(length):
    ship_list = []
    while True:
        print("Please input starting coordinates for a", length, "long ship.")
        first_pos = input_and_check()  # e.g.: [1,1]
        print("Please input ending coordinates for a", length, "long ship.")
        last_pos = input_and_check()  # e.g.: [1,5]
        # input ship coordinate and check if valid (either x or y of the beginning
        # and end must match and their distance can't be more than the ship's
        # length)
        while True:
            if first_pos[0] == last_pos[0]:  # Check if y coords are the same
                if first_pos[1] > last_pos[1]:  # set which x coord is smaller
                    smaller_value = last_pos[1]
                    for i in range(0, abs(first_pos[1] - last_pos[1]) + 1):
                        ship_list.append([first_pos[0], smaller_value + i])
                elif first_pos[1] < last_pos[1]:
                    smaller_value = first_pos[1]
                    for i in range(0, abs(first_pos[1] - last_pos[1]) + 1):
                        ship_list.append([first_pos[0], smaller_value + i])
                break

            elif first_pos[1] == last_pos[1]:  # same as above only the other way around.
                if first_pos[0] > last_pos[0]:
                    smaller_value = last_pos[0]
                    for i in range(0, abs(first_pos[0] - last_pos[0]) + 1):
                        ship_list.append([smaller_value + i, first_pos[1]])
                elif first_pos[0] < last_pos[0]:
                    smaller_value = first_pos[0]
                    for i in range(0, abs(first_pos[0] - last_pos[0]) + 1):
                        ship_list.append([smaller_value + i, first_pos[1]])
                break
            else:
                print("Invalid coordinates!")
                ship_list = []
                continue

        if int(len(ship_list)) != length:
            print("Invalid coordinates!")
            ship_list = []
            continue

        if player1_turn:
            for i in range(0, length):
                if player1_board[ship_list[i][0]][ship_list[i][1]] == "S":
                    ship_list = []
                    print("Ship obstructed, try placing elsewhere")
                    break
            if ship_list == []:
                continue
            else:
                break

        elif not player1_turn:
            for i in range(0, length):
                if player2_board[ship_list[i][0]][ship_list[i][1]] == "S":
                    ship_list = []
                    print("Ship obstructed, try placing elsewhere")
                    break
            if ship_list == []:
                continue
            else:
                break

    if player1_turn:
        for i in range(0, length):
            player1_board[ship_list[i][0]][ship_list[i][1]] = "S"
    else:
        for i in range(0, length):
            player2_board[ship_list[i][0]][ship_list[i][1]] = "S"

    return ship_list


def win_state_check():
    p1_ships = 0
    p2_ships = 0
    for i in range(0, 10):
        for j in range(0, 10):
            if player2_board[i][j] == "S":
                p1_ships += 1
            if player1_board[i][j] == "S":
                p2_ships += 1
    if p1_ships == 0:
        print("Game over,", player2_name, "wins!")
        input("Press ENTER to start a new game...")
        return True
    if p2_ships == 0:
        print("Game over,", player1_name, "wins!")
        input("Press ENTER to start a new game...")
        return True
    else:
        return False


def ship_sunk_check(ship_list, whose_ship):  # whose_ship true for p1, false for p2
    ship_damage = 0
    for i in range(0, len(ship_list)):  # check each set of coords the ship has e.g.: each [x,y]
        if whose_ship and player1_board[ship_list[i][0]][ship_list[i][1]] == "O":
            ship_damage += 1
            if ship_damage == len(ship_list):
                for j in range(0, len(ship_list)):
                    player1_board[ship_list[j][0]][ship_list[j][1]] = "+"
        if whose_ship is False and player2_board[ship_list[i][0]][ship_list[i][1]] == "O":
            ship_damage += 1
            if ship_damage == len(ship_list):
                for j in range(0, len(ship_list)):
                    player2_board[ship_list[j][0]][ship_list[j][1]] = "+"


def turn_sequence(single_player):
    global player1_turn
    is_game_over = False
    if single_player is True:
        while True:
            show_board(player1_board, player2_board, player1_turn)
            if player1_turn is True:
                shot([], player1_turn)
            else:
                AI_pick_shooting_coordinate()
            for ship in player1_ship_list:
                ship_sunk_check(ship, player1_turn)
            for ship in player2_ship_list:
                ship_sunk_check(ship, player1_turn)
            is_game_over = win_state_check()
            if is_game_over:
                break
            else:
                player1_turn = not player1_turn
                continue

    if single_player is False:
        while True:
            show_board(player1_board, player2_board, player1_turn)
            shot(player1_turn)
            for ship in player1_ship_list:
                ship_sunk_check(ship, player1_turn)
            for ship in player2_ship_list:
                ship_sunk_check(ship, player1_turn)
            if win_state_check() is True:
                break
            else:
                player1_turn = not player1_turn
                continue


def main():
    while True:
        init()
        turn_sequence(single_player)

main()
