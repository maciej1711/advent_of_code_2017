import argparse
from collections import defaultdict
"""
--- Day 12: Digital Plumber ---

Walking along the memory banks of the stream, you find a small village that is experiencing a little confusion: some programs can't communicate with each other.

Programs in this village communicate using a fixed system of pipes. Messages are passed between programs using these pipes, but most programs aren't connected to each other directly. Instead, programs pass messages between each other until the message reaches the intended recipient.

For some reason, though, some of these messages aren't ever reaching their intended recipient, and the programs suspect that some pipes are missing. They would like you to investigate.

You walk through the village and record the ID of each program and the IDs with which it can communicate directly (your puzzle input). Each program has one or more programs with which it can communicate, and these pipes are bidirectional; if 8 says it can communicate with 11, then 11 will say it can communicate with 8.

You need to figure out how many programs are in the group that contains program ID 0.

For example, suppose you go door-to-door like a travelling salesman and record the following list:

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5

In this example, the following programs are in the group that contains program ID 0:

    Program 0 by definition.
    Program 2, directly connected to program 0.
    Program 3 via program 2.
    Program 4 via program 2.
    Program 5 via programs 6, then 4, then 2.
    Program 6 via programs 4, then 2.

Therefore, a total of 6 programs are in this group; all but program 1, which has a pipe that connects it to itself.

How many programs are in the group that contains program ID 0?


"""


def open_file(file_name):
    '''
    Opens a file and returns its content as a list
    '''
    with open(file_name[0], 'r') as input_file:
        content = input_file.readlines()
    return content


def interconnected_groups(file_name):
    """
    This program iterates over lines connected with group {0} and append all of the possible groups
    to a set collection to avoid duplicated entries.
    :param file_name: name of a file with input data
    :return:
    """
    content = open_file(file_name)
    content_dict = defaultdict(list)

    # Create defautl dict with all the data provided in input file
    for line in content:
        line_items = line.split()
        line_id = int(line_items[0])
        line_communicate_ids = map(lambda x: int(x.strip(',')), line_items[2:])
        # Create content dict
        for id in line_communicate_ids:
            # Assign all the values to the line_id
            content_dict[line_id].append(id)
            # Assign all connected values to the connected items in the line
            content_dict[id].append(line_id)

    search_group = [0]
    # Initialize collection with no duplicated entries
    set_collection = set()
    while search_group:
        # Remove item from search group so it won't duplicate
        removed_item = search_group.pop()
        # Check for the removed item in the content default dict
        for item_line in content_dict[removed_item]:
            # If the item is not in the set collection - add it. Add the value from item_line to the search group.
            if item_line not in set_collection:
                set_collection.add(item_line)
                search_group.append(item_line)
    print "Number of programs with same group as program {0} is: %i" % len(set_collection)


def main():
    parser = argparse.ArgumentParser(
            description="Script for calculating total number of groups connected to the program with id {0}"
                        "Execute the script by typing python hex_path.py --name file_name",
        )
    parser.add_argument('--name', help='Name of a file to open', nargs='*')
    args = parser.parse_args()
    interconnected_groups(args.name)


if __name__ == "__main__":
    main()
