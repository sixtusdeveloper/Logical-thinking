# Challenge 1: Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)



# Challenge 2: Print each fruit in a fruit list, using a for loop:
for i in range(5):
    print(i)


# Challenge 3: Print each fruit in a fruit list, using a for loop:
word = "hello"
for letter in word:
    print(letter)



# Challenge 4: Print each fruit in a fruit list, using a for loop:
count = 0
while count < 5:
    print(count)
    count += 1


# Challenge 5: Print each fruit in a fruit list, using a for loop:
user_input = ""
while user_input != "exit":
    user_input = input("Type 'exit' to end the loop: ")
    print("You typed:", user_input)
    print("Type 'exit' to end the loop.")


# Challenge 6: Print each fruit in a fruit list, using a for loop:


i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1



for i in range(1, 11):
    if i == 5:
        break
    print(i)



for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(f"i = {i}, j = {j}")



i = 1, j = 1
i = 2, j = 1
i = 3, j = 1




for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed without break")



i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("Loop completed without break")



lst = [1, 2, 3]
lst.append(4)  # lst is now [1, 2, 3, 4]


lst = [1, 2, 3]
lst.insert(1, 1.5)  # lst is now [1, 1.5, 2, 3]



lst = [1, 2, 3, 2]
lst.remove(2)  # lst is now [1, 3, 2]
