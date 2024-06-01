# challenge
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
        print(f"i + j: {i + j}")


# chanllenge 2

# Loops control statements
for i in range(10):
    if i == 5:
        break
    print(i)


# Loops using continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


# Loops using "else" statement
for i in range(5):
    print(i)
else:
    print("Loop completed without break")



# Looping through keys and values in a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
