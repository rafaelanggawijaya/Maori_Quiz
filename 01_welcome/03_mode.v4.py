"""Maori Quiz -mode- v1
This is part of the menu which gives the player an option to pick the type
of questions they want to be given
Update: Added the ability to input one or two instead of just 1 and 2"""


def mode_selection(modes):
    # while loop to keep asking question
    while True:
        # asks player for what mode to play on
        answer = input(modes.lower())
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


# main routine

question = mode_selection("What mode do you want\n1. numbers\n2. days\n:")
print(f"You chose option {question}")
