import argparse
"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    aa bb cc dd ee is valid.
    aa bb cc dd aa is not valid - the word aa appears more than once.
    aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

"""


def open_file(file_name):
    '''
    Opens a file and returns its content line by line
    '''
    with open(file_name[0], 'r') as input_file:
        content = input_file.readlines()
    return content


def main():
    parser = argparse.ArgumentParser(
            description="Simple script for validating high-entropy passphrases written in a provided file. Execute the script by typing python high_entropy_passphrase --name file_name",
        )
    parser.add_argument('--name', help='Name of a file to open', nargs='*')
    args = parser.parse_args()
    # Open a file
    content = open_file(args.name)
    counter = 0
    for line in content:
        line_list = line.split()
        if len(line_list) == len(set(line_list)):
            counter += 1
    print "Number of valid lines: " + str(counter)


if __name__ == "__main__":
    main()
