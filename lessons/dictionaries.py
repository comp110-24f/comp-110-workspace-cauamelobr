# Dictionaries class notes

"""
Dictionaries, like lists, are data strcutures (collection of values)

Unlike lists, dictionaries give you the ability to decide how 
what to index your data by.

Dictonaries are indexed by keys associated with values.
This is a unique one-way mapping!

The keys are unique but the values can be equals

"""

# USD wxhange rate to other currencies
exchange: dict[str, float] = {
    "CNY": 7.10,  # chinese Yuan
    "GBP": 0.77,  # british pound
    "DKK": 6.86,
}  # danish kroner

print(exchange["caua"])

"""dollars: float = 100.0

# Acess dictionary value by its key
pounds: float = dollars * exchange["GBP"]  # accessing only GBP value of the dictionary

# Append a key-value entry to dictionary
exchange["EUR"] = 0.92

# Update a key-value entry in dictionary
exchange["CNY"] -= 1.00

# len is the number of key-values entries
count: int = len(exchange)

# Dictionary syntax
"""
"""
ice_cream: dict[str, int] = {
    "Chocolate": 12,
    "Vanilla": 8,
    "Strawberry": 4, 
}

ice_cream.pop("strawberry") (removing items)
ice_cream["vanilla"] = 28 (assigning a new value)

# Test if a key is in the dictionary: 
has_PID: bool = "PID" in ice_cream
print(has_pbj)

# Loop Through items using for-in loops
for flavor in ice_cream:
print (flavor) 


"""
