import re

# Regular expression pattern to match digits or spelled-out digits
digit_pattern = re.compile(r'(one|two|three|four|five|six|seven|eight|nine|\d)')


def extract_first_last_digit(line):
    matches = digit_pattern.findall(line)
    if not matches:
        return 0

    # Convert spelled-out digits to numeric digits
    number_words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    first_digit = matches[0]
    last_digit = matches[-1]

    # Convert spelled-out digits to numeric if necessary
    first_digit = number_words.get(first_digit.lower(), first_digit)
    last_digit = number_words.get(last_digit.lower(), last_digit)

    return int(first_digit + last_digit)

def sum_calibration_values(text):
    lines = text.strip().split('\n')
    results = [extract_first_last_digit(line) for line in lines]
    return sum(results)

# Example usage
text = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

print(sum_calibration_values(text))
