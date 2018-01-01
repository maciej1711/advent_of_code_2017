import argparse
"""
--- Day 19: A Series of Tubes ---

Somehow, a network packet got lost and ended up here. It's trying to follow a routing diagram (your puzzle input), but it's confused about where to go.

Its starting point is just off the top of the diagram. Lines (drawn with |, -, and +) show the path it needs to take, starting by going down onto the only line connected to the top of the diagram. It needs to follow this path until it reaches the end (located somewhere within the diagram) and stop there.

Sometimes, the lines cross over each other; in these cases, it needs to continue going the same direction, and only turn left or right when there's no other option. In addition, someone has left letters on the line; these also don't change its direction, but it can use them to keep track of where it's been. For example:

     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+

Given this diagram, the packet needs to take the following path:

    Starting at the only line touching the top of the diagram, it must go down, pass through A, and continue onward to the first +.
    Travel right, up, and right, passing through B in the process.
    Continue down (collecting C), right, and up (collecting D).
    Finally, go all the way left through E and stopping at F.

Following the path to the end, the letters it sees on its path are ABCDEF.

The little packet looks up at you, hoping you can help it find the way. What letters will it see (in the order it would see them) if it follows the path? (The routing diagram is very wide; make sure you view it without line wrapping.)

To begin, get your puzzle input.

"""


def open_file(file_name):
    '''
    Opens a file and returns its content as a list
    '''
    with open(file_name[0], 'r') as input_file:
        content = input_file.read().split('\n')[:-1]
    return content


def ride_the_tube(file_name):
    """
    This program iterates over lines connected with group {0} and append all of the possible groups
    to a set collection to avoid duplicated entries.
    :param file_name: name of a file with input data
    :return:
    """
    content = open_file(file_name)
    y = 0
    # Get starting point of X coordinate
    x = content[0].index("|")
    direction = 'Down'
    letters = []
    current_case = '|'
    steps = 0
    # If the field is not empty (is not last field)
    while current_case != ' ':
        # Add one step and check direction
        steps += 1
        if direction == 'Down':
            y += 1
        elif direction == 'Up':
            y -= 1
        elif direction == 'Left':
            x -= 1
        elif direction == 'Right':
            x += 1
        # Modify current position by the direction
        current_case = content[y][x]
        # Different behaviour on the crossroads
        if current_case == '+':
            # Check in which position threre is a possibility to move
            if direction in ('Down', 'Up'):
                if content[y][x-1] != ' ':
                    direction = 'Left'
                else:
                    direction = 'Right'
            else:
                if content[y-1][x] != ' ':
                    direction = 'Up'
                else:
                    direction = 'Down'
        # Append the letters if current_case does not match any item
        elif current_case not in ('|', '-',):
            letters.append(current_case)

    print "Letters visited during the tube ride: %s" % (''.join(letters))
    print "Number of steps in the tube ride: %s" % steps








def main():
    parser = argparse.ArgumentParser(
            description="Script implements algorythm that allows you to ride the imaginary tube made by the puzzle input"
                        "Execute the script by typing python tube_line.py --name file_name",
        )
    parser.add_argument('--name', help='Name of a file to open', nargs='*')
    args = parser.parse_args()
    ride_the_tube(args.name)


if __name__ == "__main__":
    main()
