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


print("\nraise from None and from e example")
def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None
    except ValueError as e:
        raise ValueError('Invalid configuration format') from e

config = parse_config('config.txt')