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

