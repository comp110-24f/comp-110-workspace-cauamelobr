from unit_tests import get_name, get_first, get_last


def test_name_func() -> None:
    assert get_name(n="Izzi")


def test_get_first() -> None:
    assert get_first(input=[1, 2, 3]) == 1

def test_get_last() -> None:
    assert get_last(input=[1,2,3]) == 3