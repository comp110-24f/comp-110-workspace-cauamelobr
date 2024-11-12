"""concatenation doc"""

__author__: "730798914"


def concat(str1: str, str2: str) -> str:
    """function concat"""
    return str1 + str2


# Global variables
word1 = "happy"
word2 = "tuesday"

# Print the result of calling concat with word1 and word2
print(concat(str1=word1, str2=word2))

# Only call the function if this file is executed directly
if __name__ == "__main__":
    # Print the result of calling concat with word 1 and word 2
    print(concat(str1=word1, str2=word2))
