Solve this fun exercise(challenge 25)
# This program is supposed to draw the Cyrillic letter Ц ('tse'), but something went wrong. Can you figure out which line needs to be changed?

from turtle import *

width(5)     # make the stroke 5 pixels wide
left(90)     # option A
forward(200)
left(90)     # option B
forward(150)
left(90)
forward(200)
left(180)    # option C
forward(200)
left(90)
forward(30)
right(90)    # option D
forward(30)
hideturtle() # hide the turtle from the final image

bye()


# The code underneath is fixed to the correct way

width(5)     # make the stroke 5 pixels wide
right(90)     # option A
forward(200)
left(90)     # option B
forward(150)
left(90)
forward(200)
left(180)    # option C
forward(200)
left(90)
forward(30)
right(90)    # option D
forward(30)
hideturtle() # hide the turtle from the final image

bye()


# Another exercise to draw a letter C
# Sovle this quest(challenge 26)
# This program attempts to draw the letter C, but the turning angle needs to be adjusted:
from turtle import *
width(5)

left(180) # Orients the Turtle left

forward(50)
left(50)    # Turning angle
forward(50)
left(40)    # Turning angle
forward(50)
left(40)    # Turning angle
forward(50)
left(50)    # Turning angle
forward(50)

hideturtle()
bye()



# Similar challenge to the above but different approach(Using for loop)
# Challenge 27
# Here's a more compact version of the previous program that uses a for loop. Read the program's comments, and then run it:

from turtle import *
width(5)

left(180)

# Start of for loop.
for i in range(5): # Code below is repeated 5 times
    # Code to be repeated
    forward(50) # Indentation indicates code is inside the loop
    left(45) # Still inside the for loop
# No more indentation! Marks the end of the for-loop.
hideturtle()
bye()


# Try this program and see the shorthand for it
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)

# 
# Here is the shorthand for similar program using the (for loop)
for i in range(5):
    forward(100)
    left(45)
# This is more easier, readable and professional way for writting complex programs



Lets try this out (challenge 28)
from turtle import *
width(5)

left(180) # Orient the Turtle

for i in range(5):
    forward(50)
    left(45)  # Turning angle

hideturtle()
bye()




# Lets draw a letter 0 or o using for loop(challenge 29)
from turtle import *

width(5)

left(180)

for i in range(36):  # Adjusted to draw a circle
    forward(10)     # Reduced the forward distance
    left(10)        # Adjusted the angle for smoother curves

hideturtle()
bye()

# A similar approach here(They both works)
from turtle import *
width(5)

left(180)

for i in range(8):
    forward(50)
    left(45)

hideturtle()
bye()

