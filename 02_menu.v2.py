"""Maori Quiz -menu- v2
This part is after the welcome screen and instructions and gives the player
options to choose a mode to play and a difficulty level which would
determine questions given for the next component
Update: Added subcomponents mode and difficulty functions"""


# function for mode selection
def mode_selection(modes):
    # asks player for what mode to play on
    answer = input(modes).lower()
    # while loop to keep asking question
    while True:
        # mode 1 selection
        if answer == "1" or answer == "one":
            answer = 1
            return answer
        # mode 2 selection
        elif answer == "2" or answer == "two":
            answer = 2
            return answer
        # error for unexpected inputs
        else:
            print("<error> please enter a valid option (1 or 2)")
            answer = input(modes).lower()


# function for difficulty
def difficulty_level(level):
    # asks question for difficulty
    answer = input(level).lower()
    # while loop to ask question again if player does not input a valid answer
    while True:
        # when easy is selected
        if answer == "easy":
            answer = "Easy"
            return answer
        # when hard is selected
        elif answer == "hard":
            answer = "Hard"
            return answer
        # if player enters an invalid intput
        else:
            print("<error> please enter a valid option (easy or hard)")
            answer = input(level).lower()


# main routine
# tittle/ decoration
print("***menu***\n")
# calling function
modes_ = mode_selection("What mode do you want\n1. numbers(enter 1)\n2. "
                        "days(enter 2)\n:")
difficulty = difficulty_level("What difficulty do you want to play on?(easy "
                              "or hard:")
# makes sure shows mode string not number
if modes_ == 1:
    modes_ = "Numbers"
if modes_ == 2:
    modes_ = "Days"

print(f"Starting {difficulty} {modes_}")
