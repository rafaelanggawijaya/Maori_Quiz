"""Maori Quiz -difficulty- v1
This program is part of the menu and is after selecting which mode the
player wants. It gives the player an option to pick a difficulty of easy or
hard"""

# asks question for difficulty
difficulty = input("What difficulty do you want to play on?:").lower()

if difficulty == "easy":
    print("Starting easy game")
else:
    print("Starting Hard game")
