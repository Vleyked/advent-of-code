import os


def parse_input(input_file):
    """Parse the input file into a list of tuples."""
    with open(input_file) as f:
        return f.readlines()


def main(text):
    text = text[0]
    for i in range(len(text)):
        if len({_ for _ in text[i : i + 4]}) == 4:
            return i + 4


if __name__ == "__main__":
    os.chdir("./2022/day-6")
    text = parse_input("input.txt")
    print(main(text))
