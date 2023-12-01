def get_input(file_name: str):
    """Get the text input from the input.txt file"""
    with open(f"year_2023/day_1/{file_name}") as f:
        return f.read()

def extract_first_last_digits(text: str) -> list:
    result = []

    # Iterate through each line
    for line in text.split("\n"):
        first_digit = None
        last_digit = None

        # Find the first digit from the beginning of the line
        for char in line:
            if char.isdigit():
                first_digit = char
                break

        # Find the last digit from the end of the line
        for char in reversed(line):
            if char.isdigit():
                last_digit = char
                break

        # Add the digits to the result list if both are found
        if first_digit and last_digit:
            result.append(int(first_digit + last_digit))

    return result

def main() -> None:
    text = get_input("input.txt")
    result = extract_first_last_digits(text)
    print(sum(result))

if __name__ == "__main__":
    main()
