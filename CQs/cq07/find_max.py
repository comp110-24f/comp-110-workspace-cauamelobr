"""Unit Test - cHALLENGE qUESTION"""

__author__ = "730798914"


def find_and_remove_max(lst: list[int]) -> int:
    # Check if the list is empty
    if not lst:
        return -1

    # Find the maximum value in the list
    max_value = max(lst)

    # Remove all instances of the max value from the list using a while loop
    while max_value in lst:  # while loop to remove
        lst.remove(max_value)

    # Return the maximum value
    return max_value
