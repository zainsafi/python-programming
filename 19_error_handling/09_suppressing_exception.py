# suppressing original exception
# raise from None

def convert_to_number(value):
    try:
        return int(value)
    except ValueError as e:
        raise ValueError("Conversion failed") from None
    
try:

    convert_to_number('abc')

except ValueError as e:
    print(e)
    print(e.__cause__) # None