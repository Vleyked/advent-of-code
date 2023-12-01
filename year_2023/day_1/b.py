from .utils import sum_calibration_values, get_input
from .patterns import digit_patterns, NumberWords


def solve_b() -> None:
    text = get_input("input.txt")
    print(sum_calibration_values(text, digit_patterns.spelled_out_pattern, NumberWords))


if __name__ == "__main__":
    solve_b()
