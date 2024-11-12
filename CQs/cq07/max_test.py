"""Unit Test - cHALLENGE qUESTION"""

__author__ = "730798914"

# find_max.py


def find_and_remove_max(lst: list[int]) -> int:
    if not lst:
        return -1

    max_value = max(lst)
    while max_value in lst:
        lst.remove(max_value)

    return max_value


#  test functions and proper type annotations
def test_return_expected_value() -> None:
    """Test if the function returns the expected maximum value."""
    a: list[int] = [1, 5, 3, 9, 4]
    result = find_and_remove_max(a)
    assert result == 9, f"Expected 9 but got {result}"
    print("Test return_expected_value passed")
    return None


def test_mutates_input_correctly() -> None:
    """Test if the input list is modified correctly after removing the max value."""
    b: list[int] = [1, 5, 3, 9, 4]
    find_and_remove_max(b)
    assert b == [1, 5, 3, 4], f"Expected [1, 5, 3, 4] but got {b}"
    print("Test mutates_input_correctly passed")
    return None


def test_edge_case_empty_list() -> None:
    """Test the function handles the case where the list is empty."""
    c: list[int] = []  # Added type annotation for the empty list
    result = find_and_remove_max(c)
    assert result == -1, f"Expected -1 but got {result}"
    assert c == [], f"Expected [] but got {c}"
    print("Test edge_case_empty_list passed")
    return None
