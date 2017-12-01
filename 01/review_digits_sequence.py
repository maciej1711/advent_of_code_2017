import argparse
"""
You're standing in a room with "digitization quarantine" written in LEDs along one wall. The only door is locked, but it includes a small interface. "Restricted Area - Strictly No Digitized Users Allowed."

It goes on to explain that you may only leave by solving a captcha to prove you're not a human. Apparently, you only get one millisecond to solve the captcha: too fast for a normal human, but it feels like hours to you.

The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

For example:

    1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
    1111 produces 4 because each digit (all 1) matches the next.
    1234 produces 0 because no digit matches the next.
    91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

What is the solution to your captcha?
"""


def open_file(file_name):
    '''
    Opens a file and returns its content line by line
    '''
    with open(file_name[0], 'r') as input_file:
        content = input_file.readlines()
    return content


def count_sum_of_chosen_digits(line):
    """
    Count sum of digits in line that fullfill the requirements
    """
    sum_of = 0
    for i, item in enumerate(line[1:-1]):
        if item == line[:-1][i]:
            sum_of += int(item)
    if line[0] == line[-2]:
        sum_of += int(line[0])
    print "Sum of digits: " + str(sum_of)


def main():
    parser = argparse.ArgumentParser(
            description="Simple script for concatenating sum of identical digits located next to each other. Script read input file line by line. Execute the script by typing python review_digits_sequence --name file_name",
        )
    parser.add_argument('--name', help='Name of a file to open', nargs='*')
    args = parser.parse_args()
    # Open a file
    content = open_file(args.name)
    # Count sum of digits for every line 
    for line in content:
        count_sum_of_chosen_digits(line)


if __name__ == "__main__":
    main()
