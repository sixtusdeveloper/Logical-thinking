def outer_function():
    x = 10  # x is in the enclosing scope

    def inner_function():
        nonlocal x
        x = 20  # Modifies the x in the enclosing scope
        print(x)

    inner_function()  # Output: 20
    print(x)  # Output: 20

outer_function()
