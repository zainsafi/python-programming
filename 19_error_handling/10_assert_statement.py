#  assert statement
# assert is shorthand for:
# if condition is False -> raise AssertionError
# assert condition, "error message(optional)"

#assert without a message
#run each program one by one to see the difference
# print("\nassert without a message")
# def calculate_square(number):
#     assert number >= 0 # without a message
#     return number * number

# calculate_square(-2)

#assert with a message
print("\nassert with a message")
def calculate_square(number):
    assert number >= 0, "number can't be negative"
    return number * number

print(calculate_square(-2))

# now applying exception handling