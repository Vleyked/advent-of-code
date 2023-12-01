import re
from dataclasses import dataclass


@dataclass
class DigitPatterns:
    numeric_pattern: re.Pattern
    spelled_out_pattern: re.Pattern

    def __post_init__(self):
        self.numeric_pattern = re.compile(self.numeric_pattern)
        self.spelled_out_pattern = re.compile(self.spelled_out_pattern)


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

digit_patterns = DigitPatterns(
    r"(\d)", r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
)
