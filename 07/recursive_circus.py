import argparse
"""
--- Day 7: Recursive Circus ---

Wandering further through the circuits of the computer, you come upon a tower of programs that have gotten themselves into a bit of trouble. A recursive algorithm has gotten out of hand, and now they're balanced precariously in a large tower.

One program at the bottom supports the entire tower. It's holding a large disc, and on the disc are balanced several more sub-towers. At the bottom of these sub-towers, standing on the bottom disc, are other programs, each holding their own disc, and so on. At the very tops of these sub-sub-sub-...-towers, many programs stand simply keeping the disc below them balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of these towers. You ask each program to yell out their name, their weight, and (if they're holding a disc) the names of the programs immediately above them balancing on that disc. You write this information down (your puzzle input). Unfortunately, in their panic, they don't do this in an orderly fashion; by the time you're done, you're not sure which program gave which information.

For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)

...then you would be able to recreate the structure of the towers that looks like this:

                gyxo
              /
         ugml - ebii
       /      \
      |         jptl
      |
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |
      |         ktlj
       \      /
         fwft - cntj
              \
                xhth

In this example, tknk is at the bottom of the tower (the bottom program), and is holding up ugml, padx, and fwft. Those programs are, in turn, holding up other programs; in this example, none of those programs are holding up any other programs, and are all the tops of their own towers. (The actual tower balancing in front of you is much larger.)

Before you're ready to help them, you need to make sure your information is correct. What is the name of the bottom program?
"""


def open_file(file_name):
    '''
    Opens a file and returns its content as a list
    '''
    with open(file_name[0], 'r') as input_file:
        content = input_file.readlines()
    return content


def recursive_circus(file_name):
    """
    This method splits input data into two lists - bottoms and tops.
    If the item that is present in the bottoms list does not appear in the tops it has to be item we are looking for
    :param file_name: name of a file with input data
    """
    content = open_file(file_name)
    qualified_lines = [item for item in content if ("->" in item)]
    bottoms = [line.split(" (")[0] for line in qualified_lines]
    tops = ''.join([line.split("-> ")[1] for line in qualified_lines])
    for item in bottoms:
        if item not in tops:
            return item, qualified_lines, content


def get_weights(item, content, line_weight):
    pass


def balance_weight(qualified_lines, bottom, content):
    root_list = [item.split("-> ")[1] for item in qualified_lines if bottom+" (" in item][0].split(", ")
    print "Root List"
    print root_list
    for item in root_list:
        total_weight = 0
        total_weight += get_weights(item, content, total_weight)
        print "TOTAL"
        print total_weight


def main():
    parser = argparse.ArgumentParser(
            description="Script for recognition of the bottom program in the tower of programs"
                        "Execute the script by typing python recursive_circus --name file_name",
        )
    parser.add_argument('--name', help='Name of a file to open', nargs='*')
    args = parser.parse_args()
    # Open a file
    bottom, qualified_lines, content = recursive_circus(args.name)
    balance_weight(qualified_lines, bottom, content)
    print "Bottom program name is: %s" % (bottom)


if __name__ == "__main__":
    main()
