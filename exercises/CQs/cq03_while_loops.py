"""CQ03 - while loops"""

__author__: "730798914"


def num_instance(
    phrase: str, search_char: str
) -> int:  # the number of times search_char appears
    count = 0  # initial counting
    index = 0  # initialize in the first character
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count
