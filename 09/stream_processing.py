import argparse
"""
--- Day 9: Stream Processing ---

A large stream blocks your path. According to the locals, it's not safe to cross the stream at the moment because it's full of garbage. You look down at the stream; rather than water, you discover that it's a stream of characters.

You sit for a while and record part of the stream (your puzzle input). The characters represent groups - sequences that begin with { and end with }. Within a group, there are zero or more other things, separated by commas: either another group or garbage. Since groups can contain other groups, a } only closes the most-recently-opened unclosed group - that is, they are nestable. Your puzzle input represents a single, large group which itself contains many smaller ones.

Sometimes, instead of a group, you will find garbage. Garbage begins with < and ends with >. Between those angle brackets, almost any character can appear, including { and }. Within garbage, < has no special meaning.

In a futile attempt to clean up the garbage, some program has canceled some of the characters within it using !: inside garbage, any character that comes after ! should be ignored, including <, >, and even another !.

You don't see any characters that deviate from these rules. Outside garbage, you only find well-formed groups, and garbage always terminates according to the rules above.

Here are some self-contained pieces of garbage:

    <>, empty garbage.
    <random characters>, garbage containing random characters.
    <<<<>, because the extra < are ignored.
    <{!>}>, because the first > is canceled.
    <!!>, because the second ! is canceled, allowing the > to terminate the garbage.
    <!!!>>, because the second ! and the first > are canceled.
    <{o"i!a,<{i<a>, which ends at the first >.

Here are some examples of whole streams and the number of groups they contain:

    {}, 1 group.
    {{{}}}, 3 groups.
    {{},{}}, also 3 groups.
    {{{},{},{{}}}}, 6 groups.
    {<{},{},{{}}>}, 1 group (which itself contains garbage).
    {<a>,<a>,<a>,<a>}, 1 group.
    {{<a>},{<a>},{<a>},{<a>}}, 5 groups.
    {{<!>},{<!>},{<!>},{<a>}}, 2 groups (since all but the last > are canceled).

Your goal is to find the total score for all groups in your input. Each group is assigned a score which is one more than the score of the group that immediately contains it. (The outermost group gets a score of 1.)

    {}, score of 1.
    {{{}}}, score of 1 + 2 + 3 = 6.
    {{},{}}, score of 1 + 2 + 2 = 5.
    {{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
    {<a>,<a>,<a>,<a>}, score of 1.
    {{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
    {{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
    {{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.

What is the total score for all groups in your input?

--- Part Two ---

Now, you're ready to remove the garbage.

To prove you've removed it, you need to count all of the characters within the garbage. The leading and trailing < and > don't count, nor do any canceled characters or the ! doing the canceling.

    <>, 0 characters.
    <random characters>, 17 characters.
    <<<<>, 3 characters.
    <{!>}>, 2 characters.
    <!!>, 0 characters.
    <!!!>>, 0 characters.
    <{o"i!a,<{i<a>, 10 characters.

How many non-canceled characters are within the garbage in your puzzle input?

"""


def open_file(file_name):
    '''
    Opens a file and returns its content as a list
    '''
    with open(file_name[0], 'r') as input_file:
        content = input_file.read()
    return content


def char_stream_processing(file_name):
    """
    This method parses input string and count the number of "{}" groups ignoring canceled characters "!a" and garbage
    items "<->". Number of garbage characters is also calculated in this algorythm.
    :param file_name: name of a file with input data
    """
    content = open_file(file_name)
    i = 0
    garbage = False
    garbage_elements = 0
    garbage_start = 0
    group_counter = 0
    opened = [False]
    while i < len(content):
        character = content[i]

        # Check if a character is the cancel character and next character does not matter
        if character == "!":
            i += 2
            # For the part 2 of the puzzle - the canceled characters does not count
            # for total number of garbage characters.
            garbage_elements -= 2
            continue
        # If the container is garbage the only item that matters is the garbage closing character ">"
        if garbage:
            if character == ">":
                # Last item of garbage does not count for total number of garbage characters.
                # Count the remaining garbage characters.
                garbage_elements += i - garbage_start
                garbage_start = 0
                garbage = False

        elif character == "<":
            # Starting character of garbage does not count for total number of garbage characters.
            garbage_start = i+1
            garbage = True

        elif character == "{":
            # Multiply the group score by the number of items in opened groups list. Append new item to the list.
            group_counter += (len(opened)) * 1
            opened.append(True)

        elif character == "}":
            # Remove one item from the opened groups list
            if len(opened) >= 1:
                opened.pop()

        i += 1

    print "Total number of characters in garbage is: %i" % garbage_elements
    print "Total number of valid groups is: %i" % group_counter


def main():
    parser = argparse.ArgumentParser(
            description="Script for calculating total number of groups in a character stream."
                        "Execute the script by typing python stream_processing.py --name file_name",
        )
    parser.add_argument('--name', help='Name of a file to open', nargs='*')
    args = parser.parse_args()
    # Open a file
    char_stream_processing(args.name)


if __name__ == "__main__":
    main()
