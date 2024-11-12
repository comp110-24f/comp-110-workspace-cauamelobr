"""A list is a data-structure, something that lets you organize and store data in 
a format such that they can be acessed and processed efficiently

Lists can be an arbitrary(but finite) lenght

"""

# Declaring the type of list

"""<lista name>: list[<item type>]
for instance: grocery_list: list[str]"""

# Initializing an empty list
"""With a constructor:"""
"""<list name>: list[<item type>] = list ()"""
"""with a literal:"""
"""<list name>: list[<item type>] = []"""

# Example:

my_numbers: list[float] = []  # with a literal
my_numbers: list[float] = list()  # with a constructor
my_numbers.append(1.5)
print(my_numbers)

# Adding an item to a list
"""<list name>.append(<item>)"""  # append only work for a list


# Initializing an alrady populated list
"""<list name>: list[<item type>] = [<item0>, <item 1>, ..., <item n>]"""

# make a list of numbers
game_points: list[int] = [102, 86, 94]
print(game_points)

# indexing!

"""grocery_list: list[str] = ["bananas", "milk", "bread"]"""
"""grocery_list[0]"""
"""output = "bananas" """

# indexing example
print(game_points[2])

# Modifying by index
"""grocery_list: list[str] = ["bananas', "milk", "bread"]"""
"""grocery_list[1] = "eggs" """  # modifying the index 1 from "milk" to "eggs"
# remember "=" means assignment and " == " means booleans!

# practice modyfing by index
game_points[1] = 72
print(game_points)

# Can we change individual chars in strings this way?
my_name: str = "Izzi"
# my_name[3] = "y" - TypeError: 'str' object does not support item assignment

# However we can convert t

 """ name_as_list: str = list(my_name)
print(name_as_list)
name_as_list[3] = "y"
print(name_as_list)
name_as_list.append("e")  # adding a new item to the list
print(name_as_list)
 """

# Lenght of a list
"""grocery_list: list[str] = ["eggs", "milk", "bread"]"""
""" len(grocery_list)"""

print(len(game_points))


# Remove an item from a list - POP OFF
"""grocery_list: list[str] = ["eggs", "milk", "bread"]"""
"""grocery_list.pop(1)"""

game_points.pop(1)  # you eliminate the index
print(game_points)

name_as_list.insert(
    4, "i"
)  # adding an item BEFORE index 4 and the thing to be added is "i"
print(name_as_list)

grocery_list: list[str] = ["bananas", "apple", "carrot"]
grocery_list.append("bananas")
print(grocery_list)
