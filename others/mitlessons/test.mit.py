s: str = "absafasca"
char: int = 0

for x in s:
    if s[char] != x:
        char = char + 1
print(char)
