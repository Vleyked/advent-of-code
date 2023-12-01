import re

from .a import get_input, extract_first_last_digits


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

def preprocess_text(text: str) -> str:
    """Preprocess the text to make it easier to extract the digits"""
    
    # Replace the number words with their digit counterparts
    for word, digit in number_words.items():
        text = text = re.sub(r"\b{}\b".format(word),
                             digit,
                             text,
                             flags=re.IGNORECASE)
    
    return text

# def main() -> None:
#     text = get_input("input.txt")
#     text = preprocess_text(text)
#     result = extract_first_last_digits(text)
#     print(sum(result))

if __name__ == "__main__":
    # main()
    text = get_input("input.txt")
    text2 = preprocess_text(text)

    print(text == text2)