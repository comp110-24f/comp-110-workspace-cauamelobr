"""Practicing with conditionals"""

__author__ = "730798914"


def guess_a_number() -> None:
    secret: int = 7
    guess: int = int(input("Guess a number: "))

    # do not forget to convert the string into an int!"""
    # call: guess_a_number() cuz we got no param."""
    # youve to call call_a_number so you have the input ("Guess a Number: ") printed!"""

    print("Your guess was " + str(guess))
    if guess == secret:
        print("You got it! ")
    elif guess < secret:
        print("Your Guess was too low!" + " The Secret number was " + str(secret))
    else:
        print("Your Guess was too high!" + " The Secret number was " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
