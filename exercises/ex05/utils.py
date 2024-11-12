"""ex 05 - list unit tests"""

__author__ = "730798914"


def only_evens(xs: list[int]) -> list[int]:
    # we should return a new list with only even int
    evens: list[int] = []  # list of even
    for num in xs:  # num is the element (number) in the list
        if num % 2 == 0:
            evens.append(num)
    return evens  # append until the list contains only even numbers


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Return a subset of the given list between start and end indices (non-inclusive)."""
    result: list[int] = []

    # Handle edge cases with start and end boundaries, as the example in
    # the instructions shows
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    if start >= len(a_list) or end <= 0:
        return result  # Return empty list for invalid ranges, as the instructions show!

    # result with elements in the valid range.
    for i in range(start, end):
        result.append(a_list[i])

    return result


def add_at_index(a_list: list[int], elem: int, index: int) -> None:
    """Add an elem at the index and raise IndexError if necessary"""
    if index < 0 or index > len(a_list):
        raise IndexError("Index is out of bounds for the input list")
    # Extend the list sixe and shift elements to the index:
    a_list.append(0)
    for i in range(len(a_list) - 1, index, -1):
        a_list[i] = a_list[i - 1]

    a_list[index] = elem  # Placing the new element at the target index.
