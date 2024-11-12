"""word: str = input("Enter a word: ")
while word != "begin":
    print("Error was reached")
    word = input("Enter again: ")
print("The while loop condition has been met.")"""

"""def sum_odd(n1: int, n2: int) -> int:
    current = n1
    sum_of_odds: int = 0
    while current <= n2:
        if current % 2 != 0 and n1 < n2:
            sum_of_odds += current
        current += 1
    return sum_odd
n1 = int(input("n1: "))
n2 = int(input("n2: "))
result = sum_odd(n1, n2)
print(sum_odd)"""

"""n1 = int(input("n1: "))
counter: int = 0
word: str = "caua me l o 10"
for x in word:
    if x == " ":
        counter += 1
print(counter)"""
"""
n1 = int(input("n1: "))
n2 = int(input("n2: "))

for x in range(n1, n2, 1):
    if x % 2 == 0:
        print(x)
    else:
        for x in range(n1, n2, -1):
            if x % 2 != 0:
                print(x)
"""

fruit_count: dict[str, int] = {"apples": 5, "bananas": 8}


for boo in fruit_count:
    ghost = fruit_count[
        boo
    ]  # creating a variable to access only the values of my dictionary
    print(f"{ghost}")
