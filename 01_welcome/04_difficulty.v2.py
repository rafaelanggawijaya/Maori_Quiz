"""Maori Quiz -difficulty- v2
This program is part of the menu and is after selecting which mode the
player wants. It gives the player an option to pick a difficulty of easy or
hard
Update: added a while loop which would stp asking question until the player
inputs a valid answer"""

# asks question for difficulty
difficulty = input("What difficulty do you want to play on?:").lower()
# while loop to ask question again if player does not input a valid answer
while difficulty != "x":
    # when easy is selected
    if difficulty == "easy":
        print("Starting easy game")
        difficulty = "x"
    # when hard is selected
    elif difficulty == "hard":
        print("Starting Hard game")
        difficulty = "x"
    # if player enters an invalid intput
    else:
        print("<error> please enter a valid option (easy or hard)")
        difficulty = input("What difficulty do you want to play on?:").lower()
