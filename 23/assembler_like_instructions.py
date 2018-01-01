from collections import defaultdict
import argparse
"""
--- Day 23: Coprocessor Conflagration ---

You decide to head directly to the CPU and fix the printer from there. As you get close, you find an experimental coprocessor doing so much work that the local programs are afraid it will halt and catch fire. This would cause serious issues for the rest of the computer, so you head in and see what you can do.

The code it's running seems to be a variant of the kind you saw recently on that tablet. The general functionality seems very similar, but some of the instructions are different:

    set X Y sets register X to the value of Y.
    sub X Y decreases register X by the value of Y.
    mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
    jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

    Only the instructions listed above are used. The eight registers here, named a through h, all start at 0.

The coprocessor is currently set to some kind of debug mode, which allows for testing, but prevents it from doing any meaningful work.

If you run the program (your puzzle input), how many times is the mul instruction invoked?

"""


def open_file(file_name):
    '''
    Opens a file and returns its content as a list. By summing the absolute value of all 3 vectors of position
    '''
    with open(file_name[0], 'r') as input_file:
        content = [line.strip().split() for line in input_file.readlines()]
    return content


def process_instructions(file_name):
    """
    This program iterates over indexes of an input file and performs assembler
    like operations that are stored withtin this input.
    :param file_name: name of a file with input data
    :return:
    """
    content = open_file(file_name)
    index = 0
    counter = 0
    # Set default dict filled with ints
    registered = defaultdict(int)
    # Assign lambda function that return registered value or its actual numerical values
    values = lambda val: registered[val] if val.isalpha() else int(val)
    while index < len(content):
        operation, reg, value = content[index]
        if operation == 'set':
            registered[reg] = values(value)
        elif operation == 'jnz':
            if values(reg) != 0:
                index += values(value)
                # crucial operation to keep the index iteration
                continue
        elif operation == 'sub':
            registered[reg] -= values(value)
        elif operation == 'mul':
            registered[reg] *= values(value)
            counter += 1
        index += 1
    print "Total number of times when multiply operation was invoked is: %i" % counter


def main():
    parser = argparse.ArgumentParser(
            description="Script contain an algorythm for counting number of processes invoked from the input"
                        "Execute the script by typing python assembler_like_instructions.py --name file_name",
        )
    parser.add_argument('--name', help='Name of a file to open', nargs='*')
    args = parser.parse_args()
    process_instructions(args.name)


if __name__ == "__main__":
    main()
