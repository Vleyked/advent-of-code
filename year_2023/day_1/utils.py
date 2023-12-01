from enum import Enum
from .patterns import DigitPatterns, NumberWords


def get_input(file_name: str) -> str:
    """Get the text input from the input.txt file"""
    with open(f"year_2023/day_1/{file_name}") as f:
        return f.read()


def extract_first_last_digit(
    line: str, pattern: DigitPatterns, mapping: Enum = None
) -> int:
    """Extract the first and last digit from a line of text

    This function uses a regex pattern to find the first and last digit
    in a line of text.

    If the mapping parameter is provided, it will map the first and last
    digit to a value in the mapping enum.
    """
    matches = pattern.findall(line)

    if not matches:
        return 0

    first_digit = matches[0]
    last_digit = matches[-1]

    if mapping is not None:
        first_digit = NumberWords.map_word_to_digit(first_digit)
        last_digit = NumberWords.map_word_to_digit(last_digit)

    return int(first_digit + last_digit)


def sum_calibration_values(
    text: str, patterns: DigitPatterns, mapping: dict = {}
) -> int:
    """Sum the calibration values from a text file

    This function takes a text file and a regex pattern and sums the
    calibration values from the text file.
    """
    lines = text.strip().split("\n")
    results = [extract_first_last_digit(line, patterns, mapping) for line in lines]
    return sum(results)
