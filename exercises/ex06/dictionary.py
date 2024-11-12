"""exercise 06 - dictionary functions"""

__author__ = "730798914"


def invert(
    input_dict: dict[str, str]
) -> dict[str, str]:  # define a function that gets a dic as parameter
    # and returns the inverted dict
    inverted_dict = {}
    for x in input_dict:
        value = input_dict[x]
        if value in inverted_dict:
            raise KeyError("sorry, duplicate key: {x}")
        # checking if x exists in the dict because we cannot have duplicated keys
        inverted_dict[value] = x
    return inverted_dict


def favorite_color(fav_color: dict[str, str]) -> str:
    popular_color: str = ""
    max_count: int = 0

    for color in fav_color.values():  # acessing values of dict
        count: int = 0  # initialize current color
        for c in fav_color.values():
            if c == color:  # count occurences od the current color
                count += 1

        # Update the most popular color based on the highest count
        if count > max_count:
            max_count = count
            popular_color = color

    return popular_color


def count(values: list[str]) -> dict[str, int]:
    # Empty dict to store counts
    count_dict: dict[str, int] = {}

    # loop though the list "values"
    for item in values:
        # check if the item is already a key in the dictionary
        if item in count_dict:
            count_dict[item] += 1  # adds 1 for the value of the dict
        else:
            # otherwise, add the item in the dict with the frequency of 1
            count_dict[item] = 1

    return count_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    # as we did in the count dict, store an empty dictonoary to store the result
    result_dict: dict[str, list[str]] = {}

    # Loop through the list
    for word in words:
        # Create a variable for the first letter and make sure it is in lowercase using .lower
        first_letter = word[0].lower()

        # check if the first letter is already a key (remember key is unique always)
        if first_letter not in result_dict:
            result_dict[first_letter] = []  # empty list to later append

        # Append the word to the list corresponding to the first letter
        result_dict[first_letter].append(word)

    return result_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    # Check if day, the key, exists in the dict:
    if day not in attendance:
        # empty dict
        attendance[day] = []
    if student not in attendance[day]:  # ensure no duplicate entries
        # if not, modify by adding the student, the value, in the dictionary key, which is the day
        attendance[day].append(student)

    return None
