"""Summing the elements of a list using different loops"""

__author__: str = "730798914"

# testing
"""
vals: list[float] = [3.2, 3.3]
def w_sum(vals: list[float]) -> float:
    idx: float = 1.1
    return """


def w_sum(vals: list[float]) -> float:
    total = 0.0
    index = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


# Part 2: f_sum using a for ... in ... loop
def f_sum(vals: list[float]) -> float:
    total = 0.0
    for val in vals:
        total += val
    return total


# Part 3: f_range_sum using a for ... in range(...) loop
def f_range_sum(vals: list[float]) -> float:
    total = 0.0
    for i in range(0, 1, len(vals)):
        total += vals[i]
    return total
