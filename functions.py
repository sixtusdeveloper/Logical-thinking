def greet():
    print("Hello, welcome to Python!")


greet()




# Challenge 1: Create a function that takes a name as an argument and prints "Hello, [name]":
def greet(name):
    print(f"Hello, {name}! Welcome to Python!")
    return name



def greet(name="Guest"):
    print(f"Hello, {name}! Welcome to Python!")


greet("Alice")  # Output: Hello, Alice! Welcome to Python!
greet()         # Output: Hello, Guest! Welcome to Python!


def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4)  # Output: 1 2 3 4

def print_key_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_key_values(a=1, b=2, c=3)  # Output: a: 1 b: 2 c: 3





def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from inner function")




def add(a, b):
    """
    Adds two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.
    """
    return a + b



print(len("Hello"))  # len is a built-in function
