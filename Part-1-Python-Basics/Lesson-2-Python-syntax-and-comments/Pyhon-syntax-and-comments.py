# Python syntax and comments

def calculate(num1, num2, operation):
    """
    This
    is a
    docstring
    """
    if operation == "+":
        return num1 + num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "You cannot divide by zero"
        return num1 / num2
    elif operation == "-":
        return num1 - num2
    else:
        return "Unknown operation."


''' This is a docstring '''
print(calculate(12, 25, "+"))  # call function calculate
print(calculate(2, 0, "/"))
print(calculate(4, 5, "*"))
print(calculate(4, 5, "-"))
print(calculate(4, 5, "**"))
