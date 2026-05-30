# string formatting in python
name = "Ali"
age = 20
salary = 1234567.8912
score = 0.875
number = 42

# basic f-string
print("\nBASIC F-STRING")
print(f"My name is {name} and I am {age} years old.")
# Output:
# My name is Ali and I am 20 years old.

# field width
print("\nFIELD WIDTH")
print(f"|{name:10}|") # |Ali       |
print(f"|{name:20}|") # |Ali                 |


# alignment
print("\nALIGNMENT")
print(f"|{name:<10}|") # |Ali       |
print(f"|{name:>10}|") # |       Ali|
print(f"|{name:^10}|") # |   Ali    |


# fill characters
print("\nFILL CHARACTERS")
print(f"|{name:*<10}|") # |Ali*******|
print(f"|{name:*>10}|") # |*******Ali|
print(f"|{name:*^10}|") # |***Ali****|


# float formatting
print("\nFLOAT FORMATTING")
print(f"{salary:.2f}") # 1234567.89
print(f"{salary:.3f}") # 1234567.891
print(f"{salary:.1f}") # 1234567.9


# comma separators
print("\nCOMMA SEPARATORS")
print(f"{salary:,.2f}") # 1,234,567.89


# percentage formatting
print("\nPERCENTAGE FORMATTING")
print(f"{score:.1%}") # 87.5%
print(f"{score:.2%}") # 87.50%


# sign display
print("\nSIGN DISPLAY")
print(f"{25:+}")  # +25
print(f"{-25:+}") # -25


# zero padding
print("\nZERO PADDING")
print(f"{number:05}") # 00042
print(f"{number:08}") # 00000042


# binary, octal, hexadecimal
print("\nNUMBER SYSTEMS")
print(f"Binary      : {number:b}") # Binary      : 101010
print(f"Octal       : {number:o}") # Octal       : 52
print(f"Hexadecimal : {number:x}") # Hexadecimal : 2a


# combining formatters
print("\nCOMBINED FORMATTING")
print(f"|{salary:>20,.2f}|") # |       1,234,567.89|


# repr conversion (!r) => It shows the official representation of a value.
print("\nREPR CONVERSION")
print(f"{name}") # Ali
print(f"{name!r}") # 'Ali'

# multi-line f-strings
print("\nMULTI-LINE F-STRING")

print(f"""
Name   : {name}
Age    : {age}
Salary : {salary:,.2f}
""")

# Output:
# Name   : Ali
# Age    : 20
# Salary : 1,234,567.89

