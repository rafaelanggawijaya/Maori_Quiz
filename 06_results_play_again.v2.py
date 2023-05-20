"""Maori Quiz -game loop- v2
This part shows the results after the game it also asks the player if they
want to play again
Update: turned the code into a function"""


# results_play_again function

def results_play_again(time, score, scored, question_text):
    # time input (for testing purposes what be received from game loop)
    player_time = time
    # score input (for testing purposes what be received from game loop)
    score = score
    # What to score out of input (for testing purposes what be received from
    # game loop)
    out_of = scored
    print(f"You got {score}/{out_of}\nIt took you {player_time} seconds")
    while True:
        # ask player input - (if they want to play again)

        answer = input(question_text).lower()

        # if player input == yes or y output - (play again goes to menu)

        if answer == "y" or answer == "yes":
            answer = "yes"
            break

        # if player input == no or n output - (goes to goodbye screen)
        elif answer == "n" or answer == "no":
            answer = "no"
            break
            # otherwise output - (error)
        else:
            print("error -invalid input- (please enter yes/no or y/n)")

    if answer == "yes":
        print("menu")
    else:
        print("Goodbye screen")


# main routine

# time input (for testing purposes what be received from game loop)
time_ = input("time:")
# score input (for testing purposes what be received from game loop)
score_ = input("score:")
# What to score out of input (for testing purposes what be received from game
# loop)
scored_ = input("out of:")
results_play_again(time_, score_, scored_, "Do you want to play again?:")
