"""Maori Quiz -game loop- v1
This program is what is responsible for the game mechanics and the question
generating. It also gives a score and times the player"""

import random


# menu function
def menu(mode, difficulty):
    # tittle/ decoration
    print("***menu***\n")
    # while loop to keep asking question
    answer_mode = input(mode)
    while True:
        # asks player for what mode to play on
        # mode 1 selection
        if answer_mode == "1" or answer_mode == "one":
            answer_mode = "number"
            break
            # mode 2 selection
        elif answer_mode == "2" or answer_mode == "two":
            answer_mode = "day"
            break
            # error for unexpected inputs
        else:
            print("<error> please enter a valid option (1 or 2)")
            answer_mode = input(mode)
    # while loop to ask question again if player does not input a valid answer
    answer_level = input(difficulty)
    while True:
        # When easy is selected
        if answer_level == "easy" or answer_level == "e":
            answer_level = "easy"
            break
        # when hard is selected
        elif answer_level == "hard" or answer_level == "h":
            answer_level = "hard"
            break
        # if player enters an invalid intput
        else:
            print("<error> please enter a valid option (easy or hard)")
            answer_level = input(difficulty)
    total_answer = str(answer_level + " " + answer_mode)
    return total_answer


# main routine

menu_ = menu(("What mode do you want\n1. numbers(enter 1)\n2. "
              "days(enter 2)\n:"),
             "What difficulty do you want to play on?(easy or hard):")

number = [["1", "tahi"], ["2", "rua"], ["3", "toru"], ["4", "wha"],
          ["5", "rima"],
          ["6", "ono"], ["7", "whitu"], ["8", "waru"], ["9", "iwa"], ["10",
                                                                      "tekau"]]
day = [["Monday", ]]
score = 0
print(menu_)
random.shuffle(number)
if menu_ == "easy number":
    for i in number:
        answer = input(f"What is the maori word for {i[0]}\n>")
        if answer == i[1]:
            print("Correct")
            score += 1
        else:
            print("Wrong")
elif menu_ == "easy day":

print(f"{score}/10")
