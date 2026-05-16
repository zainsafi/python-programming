#  assert statement
# assert is shorthand for:
# if condition is False -> raise AssertionError
# assert condition, "error message(optional)"

# run each program one by one to see the difference

# assert without a message
# print("\nassert without a message")
# def calculate_square_root(number):
#     assert number >= 0 # without a message
#     return number ** 0.5

# calculate_square_root(-2)

# #assert with a message
# print("\nassert with a message")
# def calculate_square_root(number):
#     assert number >= 0, "number can't be negative"
#     return number ** 0.5

# print(calculate_square_root(-2))


# now applying exception handling
def calulate_square_root(number):
    assert number >= 0, "number can't be negative"
    return number ** 0.5
try:
    calulate_square_root(-2)
except AssertionError as e:
    print(f"Assertion Error: {e}")