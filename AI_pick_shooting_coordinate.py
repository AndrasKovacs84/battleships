import random
import os
import copy

coord = []
first_hit = []
second_hit = []


def AI_pick_shooting_coordinate():
    global coord
    global first_hit
    global second_hit
    global acceptable_target_coords
    acceptable_target_coords = []
    coords_to_remove = []
    if first_hit == []:
        # if there are no hits yet, then just shoot at a random coordinate.
        x = random.randrange(0, 9)
        y = random.randrange(0, 9)
        coord.append(x) 
        coord.append(y)

        #  AFTER CHECKING VALIDITY make first_hit equal coord
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
                    coords_to_remove.append(coords)
        print("indices to delete: ", coords_to_remove)
        for coords in coords_to_remove:
            acceptable_target_coords.remove(coords)
        # pick a random coordinate from the remaining list of reasonable targets
        print("acceptable coords list: ", acceptable_target_coords)
        second_hit = random.choice(acceptable_target_coords)

if __name__ == "__main__":
    AI_pick_shooting_coordinate()
    print("first hit: ", first_hit)
    AI_pick_shooting_coordinate()
    print("second hit: ", second_hit)
