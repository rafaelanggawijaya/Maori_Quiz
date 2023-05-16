"""Maori Quiz -difficulty- v2
This program is part of the menu and is after selecting which mode the
player wants. It gives the player an option to pick a difficulty of easy or
hard
Changed: code is made for testing"""


# function
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


# Main routine
while True:
    difficulty = difficulty_level("What difficulty do you want to play on?:")
    print(f"Starting {difficulty} game")
