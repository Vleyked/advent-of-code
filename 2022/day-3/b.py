import os
import re


def get_input(text):
    with open(text) as f:
        lines = f.readlines()
    return [set(line.strip()) for line in lines]


def split_groups(elves):
    groups = []
    for index in range(0, len(elves), 3):
        groups.append(elves[index : index + 3])
    return groups


def get_priority(groups):
    priorities = []
    for group in groups:
        common_set = group[0] & group[1] & group[2]
        common_set = [c for c in common_set if c.isalpha()]
        if len(common_set) != 1:
            raise Exception("More than one common item type")
        common_item = common_set[0]
        if common_item.islower():
            priorities.append(ord(common_item) - ord("a") + 1)
        else:
            priorities.append(ord(common_item) - ord("A") + 27)
    return priorities


def main():
    # print(get_input("input.txt"))
    # print(split_groups(get_input("input.txt")))
    return sum(get_priority(split_groups(get_input("input.txt"))))


if __name__ == "__main__":
    # Change the current working directory
    os.chdir("./2022/day-3")
    print(main())
