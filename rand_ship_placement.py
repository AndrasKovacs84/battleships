import random
import itertools

# Generates a 3, 4, and 5 square long ships with random position.
# The generated ships cannot overlap and cannot occupy squares next to
# each other, horizontally, vertically or diagonally.


def rand_ship_factory(length):
    global invalid_coords
    invalid_coords = []
    random_ship = []

    all_coords = list(range(0, 10))  # contains possible values for X and Y coordinates
    coords1 = []
    coords2 = []

    # starts to generate the length long ship

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
    return random_ship

