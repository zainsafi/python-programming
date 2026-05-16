# Exception Chaining in Python
# Exception chaining is the process of linking one exception to another.
# It helps us understand that one error was caused by a previous error.
# Python uses the keyword 'from' to explicitly connect exceptions.
# This preserves the original error while showing a new, more meaningful error message.

def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid value for division") from e

try:
    result = divide(5,0)

except ValueError as e:
    print(f"custom error: {e}")
    print(f"Original error: {e.__cause__}")

else: 
    print(f"result: {result}")