"""Maori Quiz -mode- v1
This is part of the menu which gives the player an option to pick the type
of questions they want to be given
Update: Added a while loop to continue to ask for an input until the player
gives a valid input"""

# gives mode a value for while loop
mode = ""
while mode != 1 or mode != 2:
    # asks player for what mode to play on
    mode = input("What mode would You like to play?:")
    # number mode
    if mode == 1:
        print("Starting Number questions")
    # day mode
    elif mode == 2:
        print("Starting Day questions")
    # error for unexpected inputs
    else:
        print("<error> please enter a valid option (1 or 2)")
