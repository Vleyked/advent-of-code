import re
import os


def parse_input(input_file):
    """Parse the input file into a list of tuples."""
    with open(input_file) as f:
        return [tuple(map(int, re.findall(r"\d+", line))) for line in f]


def find_overlaps(input_file):
    """Find the number of overlapping sections."""
    sections = parse_input(input_file)
    overlaps = 0
    for section in sections:
        if (section[0] >= section[2] and section[1] <= section[3]) or (
            section[0] <= section[2] and section[1] >= section[3]
        ):
            overlaps += 1

    return overlaps


if __name__ == "__main__":
    # Change the current working directory
    os.chdir("./2022/day-4")
    print(find_overlaps("input.txt"))
