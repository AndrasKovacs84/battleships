import random
import itertools

# Generates a 3, 4, and 5 square long ships with random position.
# The generated ships cannot overlap and cannot occupy squares next to
# each other, horizontally, vertically or diagonally.


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

#######################################################
####################TESTING############################
#######################################################

player1_board = []
player2_board = []

for i in range(0, 10):
    player1_board.append(["~"] * 10)    # fill up playerboards with tildes "~"
for i in range(0, 10):                  #
    player2_board.append(["~"] * 10)    #

invalid_coords = []
player1_ship_list = []

for i in range(0, 2):
    for ship_length in range(3, 6):
        player1_ship_list.append(rand_ship_placement(ship_length, True))

print(player1_ship_list)

for i in range(0, 10):
    current_line = ""
    # print the player board on the left
    if i < 9:
        print(i + 1, sep=" ", end="  ")
    else:
        print(i + 1, sep=" ", end=" ")
    for j in range(0, 10):
        print(player1_board[i][j], sep=" ", end=" ", flush=True)

    # add spacing between the two boards
    print("   ", sep=" ", end=" ")

    # print the enemy board on the right
    if i < 9:
        print(i + 1, sep=" ", end="  ")
    else:
        print(i + 1, sep=" ", end=" ")
    for j in range(0, 10):
        current_line = current_line + str(player1_board[i][j]) + " "
        print(current_line.replace("S", "~"))