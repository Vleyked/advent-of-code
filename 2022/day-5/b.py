import os


def parse_input(input_file):
    """Parse the input file into a list of tuples."""
    with open(input_file) as f:
        return f.readlines()


def _get_indexes(input_list):
    """Return a list of indexes from the input_list

    Args:
        input_list (list): the list of the lines from reading the input.txt
    Returns:
        list: The list of the indexes
    """
    for line in input_list:
        try:
            if line[1].isdigit():
                return line.split()
        except IndexError:
            break


# def get_stacks(input_list):
#     """Return a list of stacks from the input_list

#     Args:
#         input_list (list): the list of the lines from reading the input.txt
#     Returns:
#         dict: The dicctionary with the stacks arranged by their index
#     """
#     # from queue import Queue
#     from collections import deque

#     stacks = {}
#     # Getting the last number of the indexes
#     last_index = int(_get_indexes(input_list)[-1]) + 1
#     # Create the stacks and the indexes
#     for i in range(1, last_index):
#         stacks[i] = deque()  # []
#     # Add the crates to the stacks
#     for line in input_list:
#         for i in range(len(line)):
#             if line[i].isalpha():
#                 print(line[i])
#                 stacks[int(i / 4) + 1].append(line[i])
#                 print(stacks)
#     return stacks


def get_stacks(input_list):
    """Return a list of stacks from the input_list

    Args:
        input_list (list): the list of the lines from reading the input.txt
    Returns:
        dict: The dicctionary with the stacks arranged by their index
    """
    from collections import deque

    stacks = {}
    for line in input_list:
        try:
            if line[1].isdigit():
                continue
            else:
                for i, letter in enumerate(line):
                    if letter.isalpha():
                        if i not in stacks:
                            stacks[i] = deque([letter])
                        else:
                            stacks[i].append(letter)
        except IndexError:
            break
    return stacks


def get_stacks(input_list):
    """Return a list of stacks from the input_list

    Args:
        input_list (list): the list of the lines from reading the input.txt
    Returns:
        dict: The dicctionary with the stacks arranged by their index
    """
    from collections import deque

    stacks = {}
    for i in range(1, 10):
        stacks[i] = deque()

    for line in input_list:
        try:
            if line[1].isdigit():
                break
            else:
                for i in range(len(line)):
                    if line[i].isalpha():
                        stacks[int(i / 4) + 1].append(line[i])
        except IndexError:
            break

    return stacks


def get_moves(input_list):
    """Return a list of moves from the input_list

    Args:
        input_list (list): the list of the lines from reading the input.txt
    Returns:
        list: The list of the moves
    """
    moves = []
    for line in input_list:
        try:
            if line[0] == "m":
                line = line.split()
                moves.append(tuple([int(n) for n in line if n.isdigit()]))
        except IndexError:
            break
    return moves


def main():
    from collections import deque

    input = parse_input("input.txt")
    stacks = get_stacks(input)
    indexes = _get_indexes(input)
    moves = get_moves(input)

    # Solving the puzzle
    for move in moves:
        if move[0] == 1:
            stacks[move[2]].appendleft(stacks[move[1]].popleft())
        if move[0] > 1:
            crates = []
            for _ in range(move[0]):
                crates.append(stacks[move[1]].popleft())
            stacks[move[2]].extendleft(crates[::-1])

    solution = []
    for n in indexes:
        try:
            solution.append(stacks[int(n)].popleft())
        except IndexError:
            continue
    print(*solution, sep="")


if __name__ == "__main__":
    os.chdir("./2022/day-5")
    main()
