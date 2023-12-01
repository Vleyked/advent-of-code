import os


def get_input():
    elf_carried_calories = []
    carried_calories = 0
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
        for line in f.readlines():
            if line.strip():
                carried_calories += int(line)
            elif line.strip() == None:
                break
            else:
                elf_carried_calories.append(carried_calories)
                carried_calories = 0
    return elf_carried_calories


def solve(input):
    return sum(sorted(input, reverse=True)[:3])


if __name__ == "__main__":
    print(solve(get_input()))
