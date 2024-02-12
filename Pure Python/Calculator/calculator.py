# print options
# flake8:noqa 

options = """
Choose the operation to perform:
(+) Add
(-) Subtract
(*) Multiply 
(/) Divide
"""

choice = input(options)

# list
valid_choices = ["+", "-", "*", "/"]

# check if user input is in list
if choice not in valid_choices:
    print("Not a valid choice")
else:
    if choice == "+":
        pass
    elif choice == "-":
        pass
    if choice == "*":
        pass
    elif choice == "/":
        pass
    


