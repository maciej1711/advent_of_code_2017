import argparse
"""
--- Day 2: Corruption Checksum ---

As you walk through the door, a glowing humanoid shape yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8

    The first row's largest and smallest values are 9 and 1, and their difference is 8.
    The second row's largest and smallest values are 7 and 3, and their difference is 4.
    The third row's difference is 6.

In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?

"""


def open_file(file_name):
    '''
    Opens a file and returns its content line by line
    '''
    with open(file_name[0], 'r') as input_file:
        content = input_file.read()
    return content


def main():
    parser = argparse.ArgumentParser(
            description="Simple script for counting the checksum of every line in provided file. Execute the script by typing python checksum_calculator --name file_name",
        )
    parser.add_argument('--name', help='Name of a file to open', nargs='*')
    args = parser.parse_args()
    # Open a file
    content = open_file(args.name)
    cheksum_values = [map(int, row.split()) for row in content.splitlines()]
    print "Checksum value: " +str(sum([max(line) - min(line) for line in cheksum_values]))

if __name__ == "__main__":
    main()
