import argparse
import collections
"""
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

    Because a starts at 0, it is not greater than 1, and so b is not modified.
    a is increased by 1 (to 1) because b is less than 5 (it is 0).
    c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
    c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?

--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).

"""


def open_file(file_name):
    '''
    Opens a file and returns its content as a list
    '''
    with open(file_name[0], 'r') as input_file:
        content = [line.strip("\n") for line in input_file.readlines()]
    return content


def register_instructions(file_name):
    """
    This method replaces dec and inc commands to matematical operators, which allows to exec each line of readed file
    :param file_name: name of a file with input data
    """
    content = open_file(file_name)
    value_registry = collections.defaultdict(int)
    maximum_value = 0
    for line in content:
        # Using exec to parse string as an object
        # The variables from the sentece are kept globally. Which allows to perform operations on them
        # The Value registry stores keys and values,
        # which allows to modify the values in the dictionary within the exec command
        exec ("%s else 0" % line.replace("dec", "-=").replace("inc", "+="), globals(), value_registry)
        # Assign current maximum value to maximum_value variable.
        # If the value gets decremented the maximum_value will remain
        maximum_value = max(value_registry.values() + [maximum_value])

    print "Current maximum value of the item in registry is: %i" % (max(value_registry.values()))
    print "The highest held maximum value of the item in registry was: %i" % (maximum_value)


def main():
    parser = argparse.ArgumentParser(
            description="Script for calculating the maximum values of registry items."
                        "Execute the script by typing python register_instructions.py --name file_name",
        )
    parser.add_argument('--name', help='Name of a file to open', nargs='*')
    args = parser.parse_args()
    # Open a file
    register_instructions(args.name)


if __name__ == "__main__":
    main()
