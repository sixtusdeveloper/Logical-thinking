highest_goal_scores = 100

def player_age():
    return 18

if highest_goal_scores >= 100 and player_age() >= 18:
    print("You are qualified to play this game!")
    print("Your participation is highly appreciated!")
    print("You are a great player!")

elif highest_goal_scores <= 89 and player_age() < 18:
    print("You would have qualified to play this game if you were 18 years old!")
    print("However, your participation is appreciated!")
    print("You would have been a great player!")
    print("Feel free to try again next time!")
else:
    print("You are not qualified to play this game!")
    print("You are not a great player!")
    print("Your participation is not appreciated!")
