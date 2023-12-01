import os


def get_priority(line):
    first_half_set = set(line[: len(line) // 2])
    second_half_set = set(line[len(line) // 2 :])
    common_set = first_half_set.intersection(second_half_set)
    common_set = [c for c in common_set if c.isalpha()]
    if len(common_set) != 1:
        raise Exception("More than one common item type")
    common_item = common_set[0]
    if common_item.islower():
        return ord(common_item) - ord("a") + 1
    else:
        return ord(common_item) - ord("A") + 27


def main():
    with open("input.txt") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    print(lines)
    print(sum(get_priority(line) for line in lines))


if __name__ == "__main__":
    # Change the current working directory
    os.chdir("./2022/day-3")
    main()
