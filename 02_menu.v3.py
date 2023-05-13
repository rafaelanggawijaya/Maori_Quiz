"""Maori Quiz -menu- v3
This part is after the welcome screen and instructions and gives the player
options to choose a mode to play and a difficulty level which would
determine questions given for the next component
Update: changed the two functions into a big function"""


# function Menu
def menu(mode, difficulty):
    # tittle/ decoration
    print("***menu***\n")
    # while loop to keep asking question
    answer_mode = input(mode)
    while True:
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
            answer_mode = input(mode)
    # while loop to ask question again if player does not input a valid answer
    answer_level = input(difficulty)
    while True:
        # When easy is selected
        if answer_level == "easy":
            answer_level = "Easy"
            break
        # when hard is selected
        elif answer_level == "hard":
            answer_level = "Hard"
            break
        # if player enters an invalid intput
        else:
            print("<error> please enter a valid option (easy or hard)")
            answer_level = input(difficulty).lower
    total_answer = answer_level + " " + answer_mode
    return total_answer


# main routine

# calling function
menu_ = menu(("What mode do you want\n1. numbers(enter 1)\n2. "
              "days(enter 2)\n:"),
             "What difficulty do you want to play on?:")
print(f"Starting {menu_}")
