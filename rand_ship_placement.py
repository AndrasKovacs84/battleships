import random
import itertools

# Generates a 3, 4, and 5 square long ships with random position.
# The generated ships cannot overlap and cannot occupy squares next to
# each other, horizontally, vertically or diagonally.


def rand_ship_factory(length):
    global invalid_coords
    invalid_coords = []
    AI_ship = []

    all_coords = list(range(0, 10))  # contains possible values for X and Y coordinates
    coords1 = []
    coords2 = []

    # starts to generate the 3 long ship

    slice_start = random.randrange(0, len(all_coords) - (length - 1))  # set the start of slicing
    slice_end = slice_start + length                             # set the end of slicing
    coords1.append(all_coords[slice_start:slice_end])       # slices a 3 long piece of list from "all_coords"

    # generate a random sequence with 3 neighbouring numbers between 0 and 10
    rand_num = random.randrange(0, 10)
    for i in range(length):
        coords2.append(rand_num)

    print(slice_start)
    print(slice_end)
    print(coords1)
    print(coords2)

    # randomly decides whether coords1 or coords2 represents the horizontal coordinates on the gameboard
    # "AI_ship" will be filled up with coordinates
    if random.choice((True, False)):
        for i in range(length):
            AI_ship.append([coords1[0][i], coords2[i]])
    else:
        for i in range(length):
            AI_ship.append([coords2[i], coords1[0][i]])

    print(AI_ship)             # "AI_ship is ready and joins to the AI_ship list"

    # return AI_ship

    for i in AI_ship:
        invalid_coords.append(i)
    print(invalid_coords)

    for i in AI_ship:
        invalid_coords.append([(i[0] - 1), i[1]])
        invalid_coords.append([(i[0] + 1), i[1]])
        invalid_coords.append([i[0], (i[1] - 1)])
        invalid_coords.append([i[0], (i[1] + 1)])
        invalid_coords.append([(i[0] - 1), (i[1] - 1)])
        invalid_coords.append([(i[0] + 1), (i[1] + 1)])
        invalid_coords.append([(i[0] - 1), (i[1] + 1)])
        invalid_coords.append([(i[0] + 1), (i[1] - 1)])

        # invalid_coords.append([(AI_ship[0][0] - 1), AI_ship[0][1]])
    invalid_coords.sort()
    invalid_coords = list(invalid_coords for invalid_coords, _ in itertools.groupby(invalid_coords))
    print(invalid_coords)

rand_ship_factory(5)
