from turtle import *

# IMPORTANT NOTE
# Continuous sections of one or more characters are known as substrings.
# Substrings are defined by their starting and ending indices:
# The starting index of a substring is the index of its first character, while the ending index is the first index which is not part of the substring

# Variables

# Solve this question(challenge 01)
# num1 = 5
# num2 = 3
# sumNums = num1 + num2
# print(sumNums)
# subNums = num1 - num2
# print(subNums)
# multiplyNums = num1 * num2
# print(multiplyNums)
# sumTotalNums = sumNums + subNums + multiplyNums
# print(sumTotalNums)


# Solve this question(challenge 02)
# num = 3
# num = num + 2
# num = num * 2
# print(num)


# Solve this (challenge 03)
# For Loops

# for i in range(6):
#     print("again")
# print("again")



# Solve this question(challenge 04)
# num = 10
# for i in range(3):
#     print(num - i)


# for i in range(3):
#     print("Coffee in, ")
# print("Code out. ")


# Solve this(challenge 05)
# Fibonacci sequence
#
# def fibonacci_sequence(start1, start2, n):
#     # Initialize variables for the first two terms
#     fib_sequence = [start1, start2]
#
#     # Calculate subsequent terms using a loop
#     for i in range(2, n):
#         next_term = fib_sequence[-1] + fib_sequence[-2]
#         fib_sequence.append(next_term)
#
#     return fib_sequence
#
#
# # Input starting values
# start1 = int(input("Enter the first starting value: "))
# start2 = int(input("Enter the second starting value: "))
#
# # Calculate Fibonacci sequence up to the 20th term
# fib_sequence = fibonacci_sequence(start1, start2, 20)
#
# # Print the sequence
# print("Fibonacci sequence:")
# for term in fib_sequence:
#     print(term, end=" ")




# Solve this quest(challenge 06)

# a = 2
# b = 5
# for i in range(2, 20):  # We start the loop from the 3rd term (index 2) up to the 20th term
#     c = a + b  # Calculate the next term in the sequence
#     a = b  # Update the value of 'a' to the current 'b'
#     b = c  # Update the value of 'b' to the current 'c'
#
# # After the loop, 'c' will hold the 20th term of the sequence
# print("The 20th term of the Fibonacci sequence is:", c)



# Solve this(challenge 07)
# Conditional statement

# price = 12  # bananas usually cost 10
#
# if price < 10:
#     print("Bananas are on sale! They cost less than $10.")  # add a message here
# elif price > 10:
#     print("Oops! It seems bananas are more expensive than usual.")  # add a message here
# else:
#     print("Bananas cost $10")




# Solve this quest

# price = 0
# if price == 0:
#     print("Bananas are free!")
# elif price < 10:
#     print("Bananas are on sale!")
#
# elif price > 10:
#     print("Bananas are expensive")
# else:
#     print("Bananas cost $10")


# Solve this(challenge 08)

# wallet = 25
#
# for price in range(5):  # Using range(5) instead of range(100)
#     if price < 10:
#         wallet = wallet - price
#         print("Now I have", wallet)
#
# print("Final amount:", wallet)


# Solve this(challenge 09)
# wallet = 9

# for price in range(5):
#     if wallet >= price:  # Modify the condition to check if wallet has enough money for the current price
#         wallet = wallet - price
#         print("Now I have", wallet)
#     else:
#         print("I can't buy anything for $", price, "or I don't have enough money.")
#
# print("Final amount:", wallet)



# Solve this(challenge 10)

# wallet = 8
#
# for price in range(10):
#     if wallet >= price:
#         wallet = wallet - price
#         print("I have",wallet,"left")
#     else:
#         print("I can't afford any more")
#         break




# Solve this(challenge 11)
# Complete this program by adding a condition on line
# 11
# 11 that checks if socks is even.

# wallet = 25
# socks = 0
#
# for price in range(10):
#     if wallet >= price:
#         wallet = wallet - price
#         socks = socks + 1
#     else:
#         break
#
# if socks % 2 == 0:  # fill in this condition
#     print("I can pair my socks")
# else:
#     print("I need one more...")



# Solve this(challenge 12)
# What condition should be inserted on line 2?
# The output should classify even and odd values.

# for n in range(4):
#     if n % 2 == 0:
#         print(n, "is even.")
#
#
# else:
#     print(n, "is odd.")



# Solve this(challenge 13)
# What is the output?

# time = 3
# for n in range(3):
#     if n < time:
#         print(n)
#     elif n == time:
#         print("Go")



# Solve this(challenge 14)
# What is the output?

# time = 8
# for i in range(8):
#     if time > 5:
#         time = time -1
#     else:
#         print(time, "sconds")
#         break



# Solve this(challenge 15)


# Consider the 3 then add 1.
#
# Repeat step 2 with the new number.
#
# The Collatz conjecture asserts that following these steps will always lead to 1 for any starting integer greater than 0.


# Complete this program so that it performs the Collatz sequence and reports how many steps it took to return to 1.

# number = 3
# steps = 0
#
# for i in range(200):
#     if number == 1:
#         break
#     if number % 2 == 0:
#         number //= 2  # Divide the number by 2 if it's even
#     else:
#         number = number * 3 + 1  # Multiply the number by 3 and add 1 if it's odd
#     steps += 1  # Increment the step count
#
# if number == 1:
#     print("It took", steps, "steps")
# else:
#     print("The number didn't reach 1 yet")


# Solve this question(challenge 16)

# Starting at 27, how many steps does it take to reach 1?

# number = 27
# steps = 0
#
# while number != 1:
#     if number % 2 == 0:
#         number //= 2  # Divide the number by 2 if it's even
#     else:
#         number = number * 3 + 1  # Multiply the number by 3 and add 1 if it's odd
#     steps += 1  # Increment the step count
#
# print("It took", steps, "steps to reach 1 starting from 27.")


# Solve this fun turtle drawing exercise (challenge 17)

# forward(300)
# bye()



# Solve this quest(challenge 18)

# color('red')
# forward(200)
# left(90)
# forward(200)
# left(90)
# forward(200)
# left(90)
# forward(200)
#
# bye()


# Another challenge(challenge 19)
# The program below is supposed to draw only half a square, where the turtle draws two sides and returns
# to its starting point like this:
# However, something's wrong with this code. Can you figure out which line is the problem?


# color('blue')
# forward(200)
# left(90) # Option A
# forward(200) # Option B
# left(45) # Option C
# forward(282) # Option D
#
# bye()

# Trying to fix the issue now

# color('blue')
# forward(200)
# left(90) # Option A
# forward(200) # Option B
# left(135) # Option C
# forward(282) # Option D
#
# bye()
# Program fixed successfully


# Solve this challenge(20)
# color('blue')
# forward(200)
# left(60)
# forward(200)
# left(60)
# forward(200)
#
# bye()
# This type of shape is half a Hexagon




# Solve this quest(challenge 21)
# from turtle import *
#
# color('dark turquoise')
# forward(200)
# left(90)
# forward(200)
# left(90)
# forward(200)
# left(90)
# forward(200)
#
# bye()



# Another fun challenge that draws the lines with different colors(challenge 22

# from turtle import *
#
# color('dark turquoise') # set color to 'dark turquoise'
# forward(200) # bottom of square
# left(90)
# color('fuchsia') # set color to 'fuchsia'
# forward(200) # right side of square
# left(90)
# color('deep sky blue') # set color to 'deep sky blue'
# forward(200) # top of square
# left(90)
# color('hot pink') # set color to 'hot pink'
# forward(200) # left side of square
#
# bye()




# Now lets take another exercise that draws alphabetical letters(challenge 23)
from turtle import *

# width(5) #By changing the width here to 50 or higher values could result in drawing larger font letters
# left(90)
# forward(200)
# right(90)
# forward(100)
# right(45)
# forward(71)
# right(45)
# forward(100)
# right(45)
# forward(71)
# right(45)
# forward(100)
# hideturtle()
#
# bye()

# The above code draws the alphabetical letter D


# Solve this fun exercise(challenge 24)
# Here is a similar program to solve(
# width(5)
# left(90)
# forward(200)
# right(90)
# width(50) # line added
# forward(100)
# right(45)
# forward(71)
# right(45)
# forward(100)
# right(45)
# forward(71)
# right(45)
# forward(100)
# hideturtle()
#
# bye()



# Solve this fun exercise(challenge 25)
# This program is supposed to draw the Cyrillic letter Ц ('tse'), but something went wrong. Can you figure out which line needs to be changed?

# from turtle import *
#
# width(5)     # make the stroke 5 pixels wide
# left(90)     # option A
# forward(200)
# left(90)     # option B
# forward(150)
# left(90)
# forward(200)
# left(180)    # option C
# forward(200)
# left(90)
# forward(30)
# right(90)    # option D
# forward(30)
# hideturtle() # hide the turtle from the final image
#
# bye()


# The code underneath is fixed to the correct way

# width(5)     # make the stroke 5 pixels wide
# right(90)     # option A
# forward(200)
# left(90)     # option B
# forward(150)
# left(90)
# forward(200)
# left(180)    # option C
# forward(200)
# left(90)
# forward(30)
# right(90)    # option D
# forward(30)
# hideturtle() # hide the turtle from the final image
#
# bye()


# Another exercise to draw a letter C
# Sovle this quest(challenge 26)
# This program attempts to draw the letter C, but the turning angle needs to be adjusted:
# from turtle import *
# width(5)
#
# left(180) # Orients the Turtle left
#
# forward(50)
# left(50)    # Turning angle
# forward(50)
# left(40)    # Turning angle
# forward(50)
# left(40)    # Turning angle
# forward(50)
# left(50)    # Turning angle
# forward(50)
#
# hideturtle()
# bye()



# Similar challenge to the above but different approach(Using for loop)
# Challenge 27
# Here's a more compact version of the previous program that uses a for loop. Read the program's comments, and then run it:

# from turtle import *
# width(5)
#
# left(180)
#
# # Start of for loop.
# for i in range(5): # Code below is repeated 5 times
#     # Code to be repeated
#     forward(50) # Indentation indicates code is inside the loop
#     left(45) # Still inside the for loop
# # No more indentation! Marks the end of the for-loop.
# hideturtle()
# bye()


# Try this program and see the shorthand for it
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)


# Here is the shorthand for similar program using the (for loop)
# for i in range(5):
#     forward(100)
#     left(45)
# This is more easier, readable and professional way for writting complex programs



# Lets try this out (challenge 28)
# from turtle import *
# width(5)
#
# left(180) # Orient the Turtle
#
# for i in range(5):
#     forward(50)
#     left(45)  # Turning angle
#
# hideturtle()
# bye()




# Lets draw a letter 0 or o using for loop(challenge 29)
# from turtle import *
#
# width(5)
#
# left(180)
#
# for i in range(36):  # Adjusted to draw a circle
#     forward(10)     # Reduced the forward distance
#     left(10)        # Adjusted the angle for smoother curves
#
# hideturtle()
# bye()

# A similar approach here(They both works)
# from turtle import *
# width(5)
#
# left(180)
#
# for i in range(8):
#     forward(50)
#     left(45)
#
# hideturtle()
# bye()





# Another challenge(challenge 30)
# This exercise draws a star with a filled color
# from turtle import *
#
# speed(5)
# width(5)
#
# color('red', 'yellow')  # Two inputs: a stroke color and a fill color.
#
# begin_fill()  # Start of a filled shape.
# for i in range(5):  # Repeat 5 times
#     # The turning angle is chosen so that the star closes in on itself after five turns.
#     right(180 - 36)  # Turning angle
#     forward(200)
# end_fill()  # Fills in the shape it has been drawing
#
# hideturtle()
# bye()


# # NOTE: to draw a seven sided star, all you need is to increment the range to 7 instead 5
# from turtle import *
#
# speed(5)
# width(5)
#
# color('red', 'yellow')  # Two inputs: a stroke color and a fill color.
#
# begin_fill()  # Start of a filled shape.
# for i in range(7):  # Repeat 5 times
#     # The turning angle is chosen so that the star closes in on itself after five turns.
#     right(180 - 180/7)  # Turning angle
#     forward(200)
# end_fill()  # Fills in the shape it has been drawing
#
# hideturtle()
# bye()


# These approaches both works

# from turtle import *
#
# speed(5)
# width(5)
#
# color('red', 'yellow')  # Two inputs: a stroke color and a fill color.
#
# begin_fill()  # Start of a filled shape.
# for i in range(7):  # Repeat 5 times
#     # The turning angle is chosen so that the star closes in on itself after five turns.
#     right(154.3)  # Turning angle
#     forward(200)
# end_fill()  # Fills in the shape it has been drawing
#
# hideturtle()
# bye()


# This also works(They both works)
# from turtle import *
#
# speed(5)
# width(5)
#
# color('red', 'yellow')  # Two inputs: a stroke color and a fill color.
#
# begin_fill()  # Start of a filled shape.
# for i in range(7):  # Repeat 5 times
#     # The turning angle is chosen so that the star closes in on itself after five turns.
#     right(180 - 25.7)  # Turning angle
#     forward(200)
# end_fill()  # Fills in the shape it has been drawing
#
# hideturtle()
# bye()


# Built in Python functions(challenge 31)
# Here is the find command. Take a guess at what you think this program might output:
# str1 = "parts"
# str2 = "art"
# print(str1.find(str2))



# Built in Python functions
# Solve this challenge(challenge 32)

# str1 = "Is it going well?"
# str2 = "go"
# print(str1.find(str2))



# Predict the output  of OX in this program(challenge 34)
# str1 = "XOXOXOXOXO"
# print(str1.find("OX"))


# Prerdict the outcome of find (challenge 35)

# str1 = "Hi hey hello he."
# str2 = "he"
# print(str1.find(str2))


# Run this program to see the result(challenge 35)
# str1 = "parts"
# str2 = "ps"
# print(str1.find(str2))


# Take this challenge(challenge 36)
# What do you think could be the output of this program
# str1 = "superior"
# str2 = "Perfect"
# str3 = "personally"
# str4 = "miles per gallon"
#
# print(str1.find("per"))
# print(str2.find("per"))
# print(str3.find("per"))
# print(str4.find("per"))

# Which snippet above returns a negative value (Perfect = -2(str2)



# Solve this Challenge(37)
# What do you think could be the output of this program

# test_string = "tested, testing, tests, test"
# print(test_string.find("sted"))

# The output of this program is = 2



# Solve this challenge(38)
# test_string = "tested, testing, tests, test"
# print(test_string.find("tess"))

# The output of this program is -1

# Solve this challenge(39).
# What do you think could be the output of this program
# test_string = "tested, testing, tests, test"
# print(test_string.find("test"))

# The output of this program is = 0


# Lets run this command
# # What could be the output of this program?
# str1 = "parts"
# str2 = "ps"
# print(str1.find(str2))

# The output of the program is -1



# Solve this quest(challenge 40)
# For which snippets would the find("per")
# command return a negative number?

# str1 = "superior"
# str2 = "Perfect"
# str3 = "personally"
# str4 = "miles per gallon"
#
# print(str1.find("per"))
# print(str2.find("per"))
# print(str3.find("per"))
# print(str4.find("per"))

# The command is str2 which "Perfect"


# Another challenge to solve(challenge 41)
# What could be the output of this program?

# test_string = "tested, testing, tests, test"
# print(test_string.find("sted"))

# The outcome is 2



# Solve this Challenge(challenge 42)
# What could be the output of this program

# test_string = "tested, testing, tests, test"
# print(test_string.find("tess"))

# The outcome of this program is -1



# Solve this challenge(43)
# what do you think could be the outcome of this program?
# test_string = "tested, testing, tests, test"
# print(test_string.find("test"))

# The outcome of the program is 0



# The find function is useful if you're looking for a specific set of characters in a string, but since it only returns the first instance of the search term, it has limited functionality.
# If we wanted to find the other occurrences of test in the above program, we would have to use other functions like count and rstring.


# Extracting characters from string
# str1 = "educational"
# print(str1[4])

# The outcome comes out "a"


# what number should we replace 4 with to access the letter "n"
# str1 = "educational"
# print(str1[4])

# The number is 8 which is the index value of letter "n"



# Solve this challenge (challenge 44)
# This challenge involves substrings
# word = "learning"
# print(word[1:5])

# The substring of the above program is "earn"


# Another example(challenge 45)
# word = "embossed"
# print(word[2:6])

# The substring of this program is "boss"


# Another example(challenge 46)
# word = "climb"
# print(word[2:6])

# The substring of this program is "imb"



# Another Example of substring(challenge 47)
# word = "steamer"
# start = 1
# end = 5
# print(word[start:end])

# The substring of this program is "team"



# Another example of substring(challenge 48)
# str1 = "Spam spam spam spam. Lovely spam! Wonderful spam! Spam spa-a-a-a-a-am..."
# str2 = str1[21:25] # Needs to be fixed
# print(str2)

# The substring of this program is "Love"



# Here we're starting with a string in str1 and then(challenge 49)
# copying the substring between two indices into another variable, str2. This is known as slicing.

# str1 = "scrumptious"
# # What numbers should be filled in?
# i = 1
# j = 6
# str2 = str1[i:j]
# print(str2) # Output: "crump"

# The missing numbers are 1:6


# Another Example of how to get a slice(challenge 50)
# Another way to slice strings is to access every character before or after an index.
# You can access every character after the starting index by leaving out the ending index.
# To get “equivocal” from the string "Unequivocal" stored in str1, you can just write str1[2:]:

# str1 = "Unequivocal"
# str2 = str1[2:]
# print(str2)

# The output is "equivocal"



# Another example(challenge 51)
# Similarly, we can get every character before the selected index by leaving out the starting index:
# str1 = "Goldfish"
# str2 = str1[:4]
# print(str2)

# The output of this program is "Gold"


# sentence = "I like rocks but they seem indifferent."
# # conjunction_index = sentence.find("but")
# conjunction_index = sentence.find(" but ")
# # left_side = sentence[0:conjunction_index]
# left_side = sentence[0:conjunction_index-1]
# right_side = sentence[conjunction_index + 3:]
# # right_side = sentence[conjunction_index + 4:]
# classy_sentence = left_side + "yet" + right_side
# print(classy_sentence)


# Which lines in this code should we uncomment to correctly swap the word “but” for “yet”?

# sentence = "I like rocks but they seem indifferent."
# conjunction_index = sentence.find("but")
# left_side = sentence[0:conjunction_index]
# right_side = sentence[conjunction_index + 3:]
# classy_sentence = left_side + "yet" + right_side
# print(classy_sentence)
#



# The Replace function
# forecast = "It will be rainy today."
# new_forecast = forecast.replace("rainy", "sunny")
# print(forecast) # Original forecast
# print(new_forecast) # New forecast

# Solve this quest(Challenge 52)
# greeting = "goodbye, and say hello"
# print(greeting.replace("goodbye", "hello"))


# Solve this challenge(53)
# test_string = "The replacement will be arriving shortly"
# new_string = test_string.replace("shortly", "now")

# print(test_string)
# print(new_string)


# old_string = "the old string"
# new_string = old_string.replace("old", "new")
#
# print(old_string)
# print(new_string)
#
# print("We replaced " + old_string + " with " + new_string)




# # Solve this challenge(54)

# words = "red fish"
# words.replace("red", "blue")
# print(words)
# print(words.replace("red", "blue"))


# Solve this challenge(55)
# form_letter = "Hello [Insert Name Here]. I'd like to personally thank you for your contribution."
#
# # form_letter.replace("[Insert Name Here]", "Emily")
# form_letter = form_letter.replace("[Insert Name Here]", "Emily")
# #"Emily".replace(form_letter, "[Insert Name Here]")
# # form_letter = form_letter.replace("Emily", "[Insert Name Here]")
#
# print(form_letter)



# Solve this challenge(56)
# form_letter = "Hello [Insert Name Here]. I'd like to personally thank you for your contribution."
#
# form_letter = form_letter.replace("[Insert Name Here]", "Emily")
#
# print(form_letter)
#
# form_letter = form_letter.replace("[Insert Name Here]", "Josh")
#
# print(form_letter)


# A different approach of the above challenge
# form_letter = "Hello [Insert Name Here]. I'd like to personally thank you for your contribution."
# # Write Emily a letter
# emily_letter = form_letter.replace("[Insert Name Here]", "Emily")
# # Save as new variable
# print(emily_letter)
# # Write Josh a letter
# josh_letter = form_letter.replace("[Insert Name Here]", "Josh")
# # Saved as a new letter
# print(josh_letter)



# Solve this challenge(challenge 57)
# Suppose that we want to make a message incomprehensible by switching around all the vowels. “We want bananas”, for instance, might become “Wa went benenes”
# The first step in this process is to replace all a’s with e’s and all e’s with a’s.

# sentence = "a breakfast for billy the bee is an early egg"
#
# # sentence = sentence.replace("e", "a")
# sentence = sentence.replace("e", "@")
# # sentence = sentence.replace("a", "b")
# sentence = sentence.replace("a", "e")
# sentence = sentence.replace("@", "a")
# #sentence = sentence.replace("b", "e")

# print(sentence)



# Solve this turtle challenge(challenge 58)

# for i in range(10):
#     forward(15)
#     left(9)
#
# bye()


# Similar program like just above but different approach
# Defining a custom function named "left_turn"
# def left_turn():
#     # Start of left_turn's definition
#     for i in range(10):
#         forward(15)
#         left(9)
#         # End of the for loop
#     # End of left_turn's definition
#
# # Rest of the program below
# left_turn()



# Similar challenge, just that now the function is just above the code
# This is the function call.
# left_turn()
#
# # This is the function definition
# def left_turn():
#     for i in range(10):
#         forward(15)
#         left(9)
#
#
# bye()

# This approach doesn't work because the function is called before defined.





# Here is another similar program
# def left_turn():
#     for i in range(10):
#         left(9)
#         forward(15)
#
# left_turn()
# left_turn()
#
# bye()


# Another good example)challenge 59)
# def left_turn():
#     for i in range(10):
#         left(9)
#         forward(15)
#
# left_turn()
# left_turn()
# left_turn()
# left_turn()
#
# bye()


# Here's a program that defines a new function — petal. Notice how petal references the previously defined left_turn
#
# hideturtle()
# color('black', 'magenta')
#
# # This is the definition of left_turn, as before.
# def left_turn():
#     for i in range(10):
#         forward(15)
#         left(9)
#
# # This is definition of petal
# def petal():
#     begin_fill()
#     left_turn() # Calls the left_turn function
#     left(90)
#     left_turn() # Calls left_turn again
#     end_fill()
#
# petal()
# bye()


# Solve the challenge(59) from this challenge, write a program that draws flower that consist of five side petals
# from turtle import *
#




# hideturtle()
# color('black', 'magenta')
#
#
# def left_turn():
#     for i in range(10):
#         forward(15)
#         left(9)
#
#
# def petal():
#     begin_fill()
#     left_turn()
#     left(90)
#     left_turn()
#     left(90)  # Line added
#     end_fill()
#
#
# for i in range(5):
#     petal()
#     right(360 / 5)
#
# bye()



# Now that our program can draw a flower, the next step is to define a function flower that contains the part that actually draws the flower.
# Solve this challenge(60)

#
# from turtle import *
#
# hideturtle()
# color('black', 'magenta')
#
#
# def left_turn():
#     for i in range(10):
#         forward(15)
#         left(9)
#
#
# def petal():
#     begin_fill()
#     left_turn()
#     left(90)
#     left_turn()
#     end_fill()
#     left(90)
#
#
# for i in range(5):
#     petal()
#     right(360 / 5)
#
# bye()


# Solve this challenge(61)

# for i in range(1, 50):
#     forward(5*i) # Multiply value of i by 5
#     left(90)
#
# bye()


# Almost similar instance

# for i in range(1, 50):
#     print(i) # Prints value of i during each loop
#     forward(5*i)
#     left(90)
#
# bye()



# Try this exercise

# for i in range(50):
#     print(i)
#     forward(5*i)
#     left(90)
#
# bye()

# Solve this challenge(63)
# for i in range(5, 50, 5):
#     print(i)
#     forward(i)
#     left(90)
#
# bye()


# Solve this challenge(64)
# for i in range(10, 100, 10):
#     print(i)
#     forward(i)
#     left(90)
#
# bye()


# Solve this challenge(65)
# for i in range(100, 0, -5):
#     print(i)
#     forward(i)
#     left(90)
#
# bye()



# Solve this challenge(66)
# for i in range(0, 100, -5):
#     print(i)
#     forward(i)
#     left(90)
#
# bye()


# Solve this challenge which draws a spiral but with differet sizes
from turtle import *

color('black', 'magenta')


def left_turn(length):
    for i in range(10):
        forward(length / 10)
        left(9)


def petal(size):
    begin_fill()
    left_turn(size)
    left(90)
    left_turn(size)
    left(90)
    end_fill()


# # Loop through the "petal spiral"
# for i in range(0, 200, 10):
#     petal(i)  # Petal takes an input for size
#     right(360 / 10)
#
# bye()



# Change this program to draw the smallest petal size
# color('black', 'magenta')
#
#
# def left_turn(length):
#     for i in range(10):
#         forward(length / 10)
#         left(9)
#
#
# def petal(size):
#     begin_fill()
#     left_turn(size)
#     left(90)
#     left_turn(size)
#     left(90)
#     end_fill()
#
#
# for i in range(200, 0, -10):
#     petal(i)
#     right(360 / 10)
#
# bye()



# Functions and Arguments
# Solve this challenge(66)

# width(2)
#
# def circle():
#     penup()
#     forward(50)
#     pendown()
#     left(90)
#     for i in range(60):
#         forward(20) #changed from 5 to 20 for the size to change
#         left(6)
#     right(90)
#     penup()
#     back(50)
#     pendown()
#
# circle()
#
# bye()




# IMPORTANT NOTE
# For this lesson, we've used the term arguments. Technically, this isn't quite right.
# In a function definition, the contents of the brackets are called parameters, not arguments. It's a small but subtle distinction


# Example of parameter:
# def circle(radius): # here radius is a parameter

# Exampe of argument:
# circle(20) # here 20 is an argument


#
# def circle(size):  # Argument added in parentheses
#     penup()
#     forward(200)
#     pendown()
#     left(90)
#     for i in range(60):
#         forward(size)  # Argument being used
#         left(6)
#     right(90)
#     penup()
#     back(200)
#     pendown()
#
#
# circle(20) #Argument added from nothing to 20
#
# bye()



# from turtle import *
#
# width(2)
#
# def circle(size):
#     penup()
#     forward(200)
#     pendown()
#     left(90)
#     for i in range(60):
#         forward(size)
#         left(6)
#     right(90)
#     penup()
#     back(200)
#     pendown()
#
# circle(10)
# circle(20)
#
# bye()




# Solve this challenge 67

# width(2)

# # Function definition
# def circle(size): # Argument added in parentheses
#     penup()
#     forward(200)
#     pendown()
#     left(90)
#     for i in range(60):
#         forward(size) # Argument used in the program
#         left(6)
#     right(90)
#     penup()
#     back(200)
#     pendown()

# # Function calls
# # Draws a circle with size of 10
# circle(10) # Argument size replaced with 10 everywhere

# # Draws a circle with size of 20
# circle(20) # Argument size replaced with 20 everywhere

# bye()



# Solving this challenge


width(2)

def circle(size):
    penup()
    forward(size*30/3.14) # Updated line
    pendown()
    left(90)
    for i in range(60):
        forward(size)
        left(6)
    right(90)
    penup()
    back(size*30/3.14) # Updated line
    pendown()

# Drawing centered circles
circle(10)
circle(20)

bye()


