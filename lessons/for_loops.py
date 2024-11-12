# For Loops - Class Notes

"""
- You can use a loop to iterate over every element in a sequence

"""
"""pets: list[str] = ["Louie", "Bo", "bear"]
for element in pets:
    print("Good boy, " + element + "!")"""

# Range
"""
- A type of sequence you can loop over
- Includes a start point, does not include the ende point,
 and steps through every point in between
- Contructor: renge(start, end, [step = 1])
- Examples:
  - range(1,5) stops at numbers 1, 2, 3, 4
  - range(1, 6, 2) stops at numbers 1, 3, 5 #if you want only odd number from a sequence, for instance!

"""

"""my_list = ["w", "x", "y", "z"]
for idx in range(0, len(my_list)):
    print(my_list[idx])
    print(idx)"""

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(str(idx) + ": " + names[idx])
