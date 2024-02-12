# flake8:noqa

# Data Types
# String -- anything inside of quotes 
"Kemo"
"Cabbage"
# Integers -- Positive or negative Whole numbers (No decimals)
3
-12

# Functions -- Performs an action -- Usually a verb end in ()
# print("Hola, me llamo es Josh")

# variables give data and store data for later use.
name = "Kemo"
fav_food = "Cabbage"
age = 37

print("My favorite food is " + fav_food)
print("I am " + str(age) + " years old")

# f strings allow you to put variables directly in your string
print(F"I am {age} years old and my name is {name}. I also like {fav_food}")


# Multiline stings

paragraph = F"""

I am {age} years old and my name is {name}. I also like {fav_food}. 
If I make a new line, it wil; print pout that way.


Any spaces or new lines will show up.
"""
print(paragraph)

