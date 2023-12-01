import os
import sys


def main(text_file):
    with open(text_file) as f:
        lines = f.readlines()

    dirs = [0]
    path = [0]

    for line in lines:
        if line.startswith("$"):
            if line.startswith("$ ls"):
                continue
            elif line.startswith("$ cd"):
                name = line.split()[2]
                if name == "/":
                    path = [0]
                elif name == "..":
                    path.pop()
                else:
                    dirs.append(0)
                    path.append(len(dirs) - 1)
        elif "dir" in line:
            continue
        else:
            size = [int(s) for s in line.split() if s.isdigit()][0]
            for idx in path:
                dirs[idx] += size

    print(
        f"Sum of the total size of the directories with size less than 100_000: {sum(x for x in dirs if x <= 100_000)}"
    )


if __name__ == "__main__":
    os.chdir("./2022/day-7")
    main("input.txt")
