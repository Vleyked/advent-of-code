import re
from dataclasses import dataclass
from enum import Enum


@dataclass
class DigitPatterns:
    """Holds the regex patterns for extracting digits from text."""

    numeric_pattern: re.Pattern
    spelled_out_pattern: re.Pattern

    def __post_init__(self):
        self.numeric_pattern = re.compile(self.numeric_pattern)
        self.spelled_out_pattern = re.compile(self.spelled_out_pattern)


class NumberWords(Enum):
    """Holds the mapping of words to digits."""

    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"
    nine = "9"

    @staticmethod
    def map_word_to_digit(word):
        """Map a word to a digit

        This function takes a word and maps it to a digit. If the word
        is not found in the mapping, it returns the word.
        """
        try:
            return NumberWords[word].value
        except KeyError:
            return word


digit_patterns = DigitPatterns(
    r"(\d)", r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
)
