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
        # Checks if the first first section overlaps with the second section
        if (section[0] in range(section[2], section[3] + 1)) or (
            section[1] in range(section[2], section[3] + 1)
        ):
            overlaps += 1

        # Checks if the first second section overlaps with the first section
        elif (section[2] in range(section[0], section[1] + 1)) or (
            section[3] in range(section[0], section[1] + 1)
        ):
            overlaps += 1

    return overlaps


if __name__ == "__main__":
    # Change the current working directory
    os.chdir("./2022/day-4")
    print(find_overlaps("input.txt"))
