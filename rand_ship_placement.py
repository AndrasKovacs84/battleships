import random
import itertools

# Generates a 3, 4, and 5 square long ships with random position.
# The generated ships cannot overlap and cannot occupy squares next to
# each other, horizontally, vertically or diagonally.


def rand_ship_factory():
    global invalid_coords
    invalid_coords = []
    AI_ships = []
    AI_ship3 = []

    all_coords = list(range(0, 10))  # contains possible values for X and Y coordinates
    coords1 = []
    coords2 = []

    # starts to generate the 3 long ship

    slice_start = random.randrange(0, len(all_coords) - 2)  # set the start of slicing
    slice_end = slice_start + 3                             # set the end of slicing
    coords1.append(all_coords[slice_start:slice_end])       # slices a 3 long piece of list from "all_coords"

    # generate a random sequence with 3 neighbouring numbers between 0 and 10
    rand_num = random.randrange(0, 10)
    for i in range(3):
        coords2.append(rand_num)

    print(slice_start)
    print(slice_end)
    print(coords1)
    print(coords2)

    # randomly decides whether coords1 or coords2 represents the horizontal coordinates on the gameboard
    # "AI_ship3" will be filled up with coordinates
    if random.choice((True, False)):
        for i in range(3):
            AI_ship3.append([coords1[0][i], coords2[i]])
    else:
        for i in range(3):
            AI_ship3.append([coords2[i], coords1[0][i]])

    print(AI_ship3)             # "AI_ship3 is ready and joins to the AI_ship3 list"
    AI_ships.append(AI_ship3)   #
    print(AI_ships)
    # return AI_ships

    for i in AI_ship3:
        invalid_coords.append(i)
    print(invalid_coords)

    for i in AI_ship3:
        invalid_coords.append([(i[0] - 1), i[1]])
        invalid_coords.append([(i[0] + 1), i[1]])
        invalid_coords.append([i[0], (i[1] - 1)])
        invalid_coords.append([i[0], (i[1] + 1)])
        invalid_coords.append([(i[0] - 1), (i[1] - 1)])
        invalid_coords.append([(i[0] + 1), (i[1] + 1)])
        invalid_coords.append([(i[0] - 1), (i[1] + 1)])
        invalid_coords.append([(i[0] + 1), (i[1] - 1)])

        # invalid_coords.append([(AI_ship3[0][0] - 1), AI_ship3[0][1]])

    invalid_coords = list(set(invalid_coords))
    print(invalid_coords)

rand_ship_factory()
