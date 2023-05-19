"""Maori Quiz -game loop- v1
This part shows the results after the game it also asks the player if they
want to play again"""


# yes_no function

def yes_no(question_text):
    while True:
        # ask player input - (if they want to play again)

        answer = input(question_text).lower()

        # if player input == yes or y output - (menu)

        if answer == "y" or answer == "yes":
            answer = "yes"
            return answer

        # if player input == no or n output - (Goodbye screen)
        elif answer == "n" or answer == "no":
            answer = "no"
            return answer

        # otherwise output - (error)
        else:
            print("error -invalid input- (please enter yes/no or y/n)")


# main routine

# time input (for testing purposes what be received from game loop)
time_ = input("time:")
# score input (for testing purposes what be received from game loop)
score_ = input("score:")
# What to score out of input (for testing purposes what be received from game
# loop)
scored_ = input("out of:")
print(f"You got {score_}/{scored_}\nIt took you {time_} seconds")
play_again = yes_no("Do you want to play again?")
if play_again == "yes":
    print("menu")
else:
    print("Goodbye screen")
