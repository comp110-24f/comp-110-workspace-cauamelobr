"""Mutating functions."""

__author__ = "730798914"


def manual_append(lst: list[int], item: int) -> None:
    """manual_append definition"""
    lst.append(item)


def double(lst: list[int]) -> None:
    """double definition"""
    i: int = 0
    while i < len(lst):
        lst[i] *= 2
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1  # list_2 references the same list as list_1

double(list_2)

# Print both lists
print(f"list_1: {list_1}")
print(f"list_2: {list_2}")
