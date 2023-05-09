"""Maori Quiz -difficulty- v1
This program is part of the menu and is after selecting which mode the
player wants. It gives the player an option to pick a difficulty of easy or
hard"""

# asks question for difficulty
difficulty = input("What difficulty do you want to play on?:").lower()
# when easy is selected
if difficulty == "easy":
    print("Starting easy game")
else:
    # when hard is selected
    print("Starting Hard game")
