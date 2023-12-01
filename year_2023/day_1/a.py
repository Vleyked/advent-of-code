from .utils import sum_calibration_values, get_input
from .patterns import digit_patterns, number_words


def solve_a() -> None:
    text = get_input("input.txt")
    print(sum_calibration_values(text, digit_patterns.numeric_pattern))


if __name__ == "__main__":
    solve_a()
