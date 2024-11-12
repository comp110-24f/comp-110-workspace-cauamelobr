"""ex 05 - list unit tests"""

__author__ = "730798914"

# Testing everything uhul

from utils import only_evens, sub, add_at_index


def test_only_evens() -> None:
    """test edge case: return an empty list"""
    assert only_evens([]) == []


def test_sub() -> None:
    """Use case: sub should return the entire list when start=0 and end=len(list)."""
    input_list = [5, 10, 15, 20]
    assert sub(input_list, 0, len(input_list)) == [5, 10, 15, 20]


def test_add_at_index() -> None:
    """Use case: add_at_index should correctly insert an element in the middle."""
    input_list = [1, 2, 4, 5]
    add_at_index(input_list, 3, 2)
    assert input_list == [
        1,
        2,
        3,
        4,
    ]
