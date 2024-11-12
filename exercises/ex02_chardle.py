"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730798914"


def input_word() -> str:
    word: str
    while True:  # Loop until a valid word is provided
        word = input("Enter a 5-character word: ")
        if len(word) == 5:  # Check if the word length is 5
            return word
        else:  # Handle invalid word length
            print(f"Error: word must contain 5 characters.")
            exit()  # Exit the program immediately


def input_letter() -> str:
    letter: str
    while True:
        letter = input("Enter a single character: ")
        if len(letter) == 1:
            return letter
        else:
            print("Error: Character must be a single character.")
            exit()  # Exit the program if input is invalid


def contains_char(word: str, letter: str) -> None:
    # Print the message indicating the search process
    print(f"Searching for {letter} in {word}")

    # Initialize the count of matching characters
    match_count = 0

    # Check each index of the word for the matching letter (without loops)
    if word[0] == letter:
        print(f"Letter {letter} found at index 0")
        match_count += 1
    if word[1] == letter:
        print(f"Letter {letter} found at index 1")
        match_count += 1
    if word[2] == letter:
        print(f"Letter {letter} found at index 2")
        match_count += 1
    if word[3] == letter:
        print(f"Letter {letter} found at index 3")
        match_count += 1
    if word[4] == letter:
        print(f"Letter {letter} found at index 4")
        match_count += 1

    # Print the appropriate message based on the match count
    if match_count == 0:
        print(f"No instances of {letter} found in {word}")
    elif match_count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{match_count} instances of {letter} found in {word}")


def main() -> None:
    """Main function to run the Chardle game."""
    # Get the word and letter from the user
    word = input_word()
    letter = input_letter()

    # Call the contains_char function to check for matches
    contains_char(word, letter)


# Example usage of main
if __name__ == "__main__":
    main()
