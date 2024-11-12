# INDEX in python
"""
You can use negative number inside the index, in which -1 refers to the
last character, and it goes down by -1

example:
new: str = "Caua"
print(new[-1])

// Index and Substrings!
- Can slice string using [start:stop:step]
- Get characters at start up to including stop-1 taking every single character
- If you give two numbers, [start: stop], setp will be 1 by default

example:
s: string = "abcdefgh"
print(S[3:6:2])
print(S[3:6:1])
print(S[:])
print(S[::-1])

s: str = "abc de fgh"
print(s[3:6:2])
print(s[3:6:1])
print(s[:])
print(s[::-1])
"""

# Working with INPUT from users!
"""
- Ask for a string:
verb: str = input("Write a verb: ")
print("I can " + verb + " better than you!")
print((verb + " ") * 5)


def input_verb() -> None:
    verb: str = input("Write a verb: ")
    print("I can " + verb + " better than you!")

- Find roots of a polynomial
  - Fid roots of a polynomial:
  ex.: fing g such that f(g,x)= g**3 - x=0
  - Algorithm uses successive approximation
  next_guess = guess - f(guess)/d/dxf(gues)

  partial code:

# Try Newton Raphson for cube root
x = int(input("What x to find the cube root of? "))
g = int(input("What guess to start with? "))
print("Current estimate cubbed = ", g**3)

next_g = g - ((g**3 - x / (3 * g**2)))
print("Next guess to try = ", next_g)


"""
# F-Strings
"""
- Easy formatted string literal
  - anything can appear in a normal string literal
  - expressions bracketed by curly braces {}
- Expressions in curly braces evaluated at runtime, automatically
converted to strings, and concataneted to the string preceding them

num: int = 3000
fraction: float = 1/3
print(num*fraction, "is", fraction*100, "% of", num)
with f-string:
print(f'{num * fraction} is {fraction*100}% of {num}')

"""

# Conditions for Branching
"""
- Variable = value
  - assignment of value
- some_expression == other_expression
  - a test of veracity (evaluates a boolean!)

# If Statement

# While loops
ex1:
where = input("Go left or right? " )
while where == "right":
    where = input("Go left or right? ") #asks the user and storage the info(variable)
print("You got out!")

ex2:


"""

# Iteration
"""
# Recap
- input: 
Done with the input command
Anything the user inputs is reas as a string object
- output
Done with the output command




# While Loops
while <condition>: #evaluate into a boolean
    <code> 
    ...

- If the condition is true, execute the block indented (within the block).
- Will check and repeat until the <condition> is False.
- If <condition> is never Flase, we will have an infinite loop

example 1:
'Simple You are in the lost Forest. Go left or right? ' 
where: string = input("You are in the Lost Forest. Go left or right? ")
while where == "right":
    where = input("You're in the Lost Forest. Go left or right)
print("You got out of the Lost Forest!")

example 2: simple non-negativer integer
n: int = int(input("Enter a non-negative integer: "))
while n > 0:
    print("x")
    n = n-1

# You try it!
Expand this code to show a sad face when the user entered 
the while loop more than 2 times
- Hint: Use a variable as a counter
CODE:
n: int = 0  # track how many times we go through the loop
where: str = input("Go left or right? ")
while where == "right":  # it checks for what the user entered
    n = n + 1
    if n > 2:
        print(" :( ")
    where = input("Go left or right? ")
print("You got out of the Lost Forest!")

# Iterate with numbers in a sequence
- Set a loop variable outside the while loop
- Test loop variable in condition
- increment variable inside while loop, so it 
does not result in a infinite loop!!!

-> Factorial Calculator!
x: int = int(input("Enter a value: "))
i: int = 1
factorial: int = 1
while i <= x:
    factorial = factorial * i
    i = i + 1
print(f"{x} factorial id {factorial}")



"""
