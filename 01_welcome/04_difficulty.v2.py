"""Maori Quiz -difficulty- v2
This program is part of the menu and is after selecting which mode the
player wants. It gives the player an option to pick a difficulty of easy or
hard
Update: added a while loop which would stp asking question until the player
inputs a valid answer"""

# asks question for difficulty
difficulty = input("What difficulty do you want to play on?:").lower()
while difficulty != "x":
    if difficulty == "easy":
        print("Starting easy game")
        difficulty = "x"
    elif difficulty == "hard":
        print("Starting Hard game")
        difficulty = "x"
    else:
        print("<error> please enter a valid option (easy or hard)")
        difficulty = input("What difficulty do you want to play on?:").lower()
