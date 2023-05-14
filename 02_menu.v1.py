"""Maori Quiz -menu- v1
This part is after the welcome screen and instructions and gives the player
options to choose a mode to play and a difficulty level which would
determine questions given for the next component"""

# tittle
print("***menu***\n")
# mode selection
mode = input("1. Maori numbers(enter 1)\n2. Maori days(Enter 2)\n:")
while True:
    # when number is selected
    if mode == "1":
        mode = "Numbers"
        break
    # when days is selected
    elif mode == "2":
        mode = "Days"
        break
    # unexpected input
    else:
        print("<error> please enter a valid option (1 or 2)")
        mode = input("1. Maori numbers(enter 1)\n2. Maori days(Enter 2)\n:")
# difficulty selection
level = input("What difficulty do you want to play on?:").lower()
while True:
    # when easy is picked
    if level == "easy":
        break
    # when easy is picked
    elif level == "hard":
        break
    # unexpected inputs
    else:
        print("<error> please enter a valid option (easy or hard)")
        level = input("What difficulty do you want to play on?(easy "
                      "or hard):").lower()

# main routine

print(f"Starting {level} {mode}")
