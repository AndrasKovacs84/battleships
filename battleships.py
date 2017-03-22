# Battleship
import random
import os
import sys
import string

print(sys.version)


def AI_pick_shooting_coordinate():
    coord = []
    first_hit = []
    second_hit = []
    acceptable_target_coords = []
    if first_hit == []:
        # if there are no hits yet, then just shoot at a random coordinate.
        x, y = random.randrange(0, 9)
        coord.append(x, y)

    elif first_hit != [] and second_hit == []:
        # first hit is not empty, but we have no second_hit yet, pick a coord near first_hit
        acceptable_target_coords.append(first hit[0]-1, first_hit[1])
        acceptable_target_coords.append(first hit[0]+1, first_hit[1])
        acceptable_target_coords.append(first hit[0], first_hit[1]-1)
        acceptable_target_coords.append(first hit[0], first_hit[1]+1)
        for x, y in acceptable_target_coords:
            if x, y < 0 or x, y > 9:


def menu_keys(key):                         # handles user input for starting a new game or quitting
    if key == "q":
        sys.exit(0)
    elif key == "n":
        init()  # You can't return break!!!


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


def input_and_check():      # checks validity of user input

    x = ""  # checks if user input is a valid letter
    y = ""
    valid_char_list = "bacdefghij"
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


def shot(whose_turn):
    global player1_board
    global player2_board
    shot = []

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
        return True
    if p2_ships == 0:
        print("Game over,", player1_name, "wins!")
        return True


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
                    player1_board[ship_list[j][0]][ship_list[j][1]] = "+"


while True:
    init()

    show_board(player1_board, player2_board, player1_turn)
    print("Press any key to start deploying ships for", player1_name)
    player1_ship3 = set_ship(3)
    show_board(player1_board, player2_board, player1_turn)
    player1_ship4 = set_ship(4)
    show_board(player1_board, player2_board, player1_turn)
    player1_ship5 = set_ship(5)
    show_board(player1_board, player2_board, player1_turn)
    input("Ships deployed, press any key to deploy for next player...")
    player1_turn = False
    show_board(player1_board, player2_board, player1_turn)
    print("Press any key to start deploying ships for", player2_name)
    player2_ship3 = set_ship(3)
    show_board(player1_board, player2_board, player1_turn)
    player2_ship4 = set_ship(4)
    show_board(player1_board, player2_board, player1_turn)
    player2_ship5 = set_ship(5)
    show_board(player1_board, player2_board, player1_turn)
    player1_turn = random.choice((True, False))
    input("All ships deployed, press a key to start. Random player goes first.")
    while True:
        show_board(player1_board, player2_board, player1_turn)
        shot(player1_turn)
        ship_sunk_check(player1_ship3, player1_turn)
        ship_sunk_check(player1_ship4, player1_turn)
        ship_sunk_check(player1_ship5, player1_turn)
        ship_sunk_check(player2_ship3, player1_turn)
        ship_sunk_check(player2_ship4, player1_turn)
        ship_sunk_check(player2_ship5, player1_turn)
        show_board(player1_board, player2_board, player1_turn)
        if win_state_check():
            input("Press any key to start a new game")
            break
        # win_state_check(player1_turn)
        input("Press any key to continue...")
        player1_turn = not player1_turn
