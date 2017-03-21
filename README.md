# battleships

implement menu keys function to enable quitting or new game

fix shipSunkCheck function:
  - bug: each sunk ship is visible for both players, making the board confusing. (done)
  - feature: update the board immediately after shot
  - rewrite to work with new nested ship lists (below)

comment code to enhance readability

refactor variable names from camelCase to underscore_case

create main function.

avoid using try-except for logic!

organize ships of each player into a nested list of the individual ship coordinates.

restructure player ships in nested lists:

player1Ship3 = [[x,y], [x, y], [x, y]]

player_1_ships = [[[x,y], [x, y], [x, y]], [[x,y], [x, y], [x, y], [x, y]], [[x,y], [x, y], [x, y], [x, y], [x, y]]]

new features:
option to place ships randomly (prerequisite for a working AI)
implement restrictions on ship placement: ships cannot be placed right next to previously placed ships.
AI
