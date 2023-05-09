"""Maori Quiz -mode- v1
This is part of the menu which gives the player an option to pick the type
of questions they want to be given
Update: changed the code into a function"""


def mode_selection(modes):
    # while loop to keep asking question
    while True:
        # asks player for what mode to play on
        answer = input(modes)
        # mode 1 selection
        if answer == "1":
            answer = 1
            return answer
        # mode 2 selection
        elif answer == "2":
            answer = 2
            return answer
        # error for unexpected inputs
        else:
            print("<error> please enter a valid option (1 or 2)")


# main routine

question = mode_selection("What mode do you want\n1. numbers\n2. days\n:")
print(f"You chose option {question}")
