"""exercise 04 - utils"""

__author__ = "730798914"


def all(int_list: list[int], num: int) -> bool:
    # If the list is empty, return False
    if len(int_list) == 0:
        return False

    # Loop through each element in the list
    for element in int_list:
        # If the current element is not equal to num, return False
        if element != num:
            return False

    # If all elements are equal to num, return True
    return True


def max(input: list[int]) -> int:
    # If the list is empty, raise a ValueError
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    # Initialize the max value to the first element in the list
    current_max = input[0]

    # Loop through the list starting from the second element
    for i in range(1, len(input)):
        # If the current element is larger than current_max, update current_max
        if input[i] > current_max:
            current_max = input[i]

    # Return the maximum value found
    return current_max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    # Check if the lengths of the two lists are different
    if len(list1) != len(list2):
        return False

    # Loop through the lists and compare each element
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    # If all elements match, return True
    return True


"""And finaly the extend function"""


def extend(list1: list[int], list2: list[int]) -> None:
    # Loop through each element in the second list
    for element in list2:
        # Append the current element to the first list
        list1.append(element)
    return None
