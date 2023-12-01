import re

from .a import get_input

# Define the number words mapping
number_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# Regular expression pattern to match digits or spelled-out digits with lookahead
digit_pattern = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")


def extract_first_last_digit(line: str) -> int:
    matches = digit_pattern.findall(line)
    if not matches:
        return 0

    # Convert spelled-out digits to numeric digits
    first_digit = number_words.get(matches[0], matches[0])
    last_digit = number_words.get(matches[-1], matches[-1])

    return int(first_digit + last_digit)


def sum_calibration_values(text: str) -> int:
    lines = text.strip().split("\n")
    results = [extract_first_last_digit(line) for line in lines]
    return sum(results)


def main():
    # Assuming `get_input` function is defined elsewhere and reads input correctly.
    text = get_input("input.txt")
    print(sum_calibration_values(text))


if __name__ == "__main__":
    main()
