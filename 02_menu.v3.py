"""Maori Quiz -menu- v2
This part is after the welcome screen and instructions and gives the player
options to choose a mode to play and a difficulty level which would
determine questions given for the next component
Update: Added subcomponents mode and difficulty functions"""


# function Menu
def menu(mode, difficulty):
    # tittle/ decoration
    print("***menu***\n")
    # while loop to keep asking question
    answer_mode = input(mode)
    while answer_mode != 1 or answer_mode != 2:
        # asks player for what mode to play on
        # mode 1 selection
        if answer_mode == "1" or answer_mode == "one":
            answer_mode = "Numbers"
            break
            # mode 2 selection
        elif answer_mode == "2" or answer_mode == "two":
            answer_mode = "Days"
            break
            # error for unexpected inputs
        else:
            print("<error> please enter a valid option (1 or 2)")
    # while loop to ask question again if player does not input a valid answer
    answer_level = input(difficulty).lower
    while answer_level != "easy" or answer_level != "hard":
        if answer_level == "easy":
            answer_level = "Easy"
        # when hard is selected
        elif answer_level == "hard":
            answer_level = "Hard"
        # if player enters an invalid intput
        else:
            print("<error> please enter a valid option (easy or hard)")
    total_answer = answer_mode + "" + answer_level
    return total_answer


# main routine

# calling function

# makes sure shows mode string not number

menu_ = menu(("What mode do you want\n1. numbers(enter 1)\n2. "
              "days(enter 2)\n:").lower(),
             ("What mode do you want\n1. numbers(enter 1)\n2. "
              "days(enter 2)\n:"))
print(menu_)
