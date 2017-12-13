import argparse
"""
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

    ne,ne,ne is 3 steps away.
    ne,ne,sw,sw is 0 steps away (back where you started).
    ne,ne,s,s is 2 steps away (se,se).
    se,sw,se,sw,sw is 3 steps away (s,s,sw).

--- Part Two ---

How many steps away is the furthest he ever got from his starting position?

"""


def open_file(file_name):
    '''
    Opens a file and returns its content as a list
    '''
    with open(file_name[0], 'r') as input_file:
        content = input_file.read().split(",")
    return content


def follow_the_path(file_name):
    """
    Given a path, this function follows direction and calculates how far from starting hex field it went
    :param file_name: name of a file with input data
    """
    # Calculate cube distance as per: https://www.redblobgames.com/grids/hexagons/ Distances
    path = open_file(file_name)
    max_distance = 0
    # Set starting position
    position = (0, 0)
    directions = {"n": (0, 1),
            "s": (0, -1),
            "ne": (1, 0),
            "sw": (-1, 0),
            "nw": (-1, 1),
            "se": (1, -1), }
    for item in path:
        # Change position with each move
        position = (position[0] + directions[item][0], position[1] + directions[item][1])
        max_distance = max(max_distance, max(abs(position[0]), abs(position[1]), abs(position[0]+position[1])))

    print "Shortest cube distance is: %i" % max(abs(position[0]), abs(position[1]), abs(position[0]+position[1]))
    print "The furthest distance was: %i steps" % max_distance


def main():
    parser = argparse.ArgumentParser(
            description="Script for calculating the distance from starting position in hexagonal grid"
                        "Execute the script by typing python hex_path.py --name file_name",
        )
    parser.add_argument('--name', help='Name of a file to open', nargs='*')
    args = parser.parse_args()
    # Open a file
    follow_the_path(args.name)


if __name__ == "__main__":
    main()
