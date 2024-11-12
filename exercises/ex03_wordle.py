"""EX03 - Wordle assignment."""

__author__ = "730798914"


def input_guess(secret_word_len: int) -> str:
    """Prompt the user to input a word of the correct length."""
    guess = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:  # Loop until the input is the correct length
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Check if the specified character is present in the given word."""
    assert len(char_guess) == 1, "The character must be a single character."
    index = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Return a string of emojis"""
    assert len(guess) == len(
        secret
    )  # "The guess and secret must be of the same length."

    WHITE_BOX: str = "\U00002B1C"  # White box emoji
    GREEN_BOX: str = "\U0001F7E9"  # Green box emoji
    YELLOW_BOX: str = "\U0001F7E8"  # Yellow box emoji

    result: str = ""  # Initialize the result string
    index: int = 0  # Initialize index for the while loop

    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    max_turns: int = 6  # defining max_turns variables
    current_turn: int = 1  # defining turn variable printed on users screen
    has_won: bool = False  # defining won variable - when the user win or lose the game

    while current_turn <= max_turns and not has_won:
        print(f"=== Turn {current_turn}/{max_turns} ===")  # Current turn unmber printed
        user_guess: str = input_guess(len(secret))  # user guess prompt/variable
        guess_feedback: str = emojified(user_guess, secret)
        print(guess_feedback)

        if user_guess == secret:  # The word guessed equals secre word
            has_won = True
        else:
            current_turn += 1  # Printed turn will increase by 1

    if has_won:
        print(f"You won in {current_turn}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
