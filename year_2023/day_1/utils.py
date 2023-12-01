from .patterns import DigitPatterns, number_words


def get_input(file_name: str) -> str:
    """Get the text input from the input.txt file"""
    with open(f"year_2023/day_1/{file_name}") as f:
        return f.read()


def extract_first_last_digit(line: str, patterns: DigitPatterns, mapping=None) -> int:
    matches = patterns.findall(line)

    if not matches:
        return 0

    if not mapping:
        return int(matches[0] + matches[-1])

    first_digit = mapping.get(matches[0], matches[0])
    last_digit = mapping.get(matches[-1], matches[-1])

    return int(first_digit + last_digit)


def sum_calibration_values(text: str, patterns: DigitPatterns, mapping=None) -> int:
    lines = text.strip().split("\n")
    results = [extract_first_last_digit(line, patterns, mapping) for line in lines]
    return sum(results)
