import argparse
"""
--- Day 5: A Maze of Twisty Trampolines, All Alike ---

An urgent interrupt arrives from the CPU: it's trapped in a maze of jump instructions, and it would like assistance from any programs with spare cycles to help find the exit.

The message includes a list of the offsets for each jump. Jumps are relative: -1 moves to the previous instruction, and 2 skips the next one. Start at the first instruction in the list. The goal is to follow the jumps until one leads outside the list.

In addition, these instructions are a little strange; after each jump, the offset of that instruction increases by 1. So, if you come across an offset of 3, you would move three instructions forward, but change it to a 4 for the next time it is encountered.

For example, consider the following list of jump offsets:

0
3
0
1
-3

Positive jumps ("forward") move downward; negative jumps move upward. For legibility in this example, these offset values will be written all on one line, with the current instruction marked in parentheses. The following steps would be taken before an exit is found:

    (0) 3  0  1  -3  - before we have taken any steps.
    (1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all). Fortunately, the instruction is then incremented to 1.
     2 (3) 0  1  -3  - step forward because of the instruction we just modified. The first instruction is incremented again, now to 2.
     2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
     2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
     2  5  0  1  -2  - jump 4 steps forward, escaping the maze.

In this example, the exit is reached in 5 steps.

How many steps does it take to reach the exit?

--- Part Two ---

Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?

"""


def open_file(file_name):
    '''
    Opens a file and returns its content as a list
    '''
    with open(file_name[0], 'r') as input_file:
        content = input_file.read()
    return list(map(int, content.split()))


def trampoline_maze_counter(file_name, second_part):
    """
    This function opens input data in a list and executes maze trampoline step out algorithm.
    :param file_name: name of a file with input data
    :param second_part: second condition activator
    """
    content = open_file(file_name)
    position = 0
    counter = 0
    while 0 <= position < len(content):
        next_step_value = content[position]
        if next_step_value >= 3 and content:
            content[position] -= 1
        else:
            content[position] += 1
        position += next_step_value
        counter += 1
    print "Number of steps required to step out the maze: " + str(counter) + ", while the second part was: " + str(second_part)


def main():
    parser = argparse.ArgumentParser(
            description="Simple script for navigating through trampoline maze (list of positive and negative integers. Execute the script by typing python trampolines_maze --name file_name",
        )
    parser.add_argument('--name', help='Name of a file to open', nargs='*')
    args = parser.parse_args()
    # Open a file
    trampoline_maze_counter(args.name, False)
    trampoline_maze_counter(args.name, True)




if __name__ == "__main__":
    main()
