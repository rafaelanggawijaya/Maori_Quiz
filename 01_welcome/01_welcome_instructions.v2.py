"""Maori Quiz -welcome_instructions- v1
This program/component is what shows at the beginning of the game and asks
players if
they need instructions
Update: Added code for testing purposes"""


# Functions for a text formatter (From Lucky Unicorn pre-assessment)
def text_formatter(symbol_1, side_symbol, symbol_2, text):
    sides = side_symbol * 3
    formatted_text = f"{sides}{text}{sides}"
    top = symbol_1 * len(formatted_text)
    bottom = symbol_2 * len(formatted_text)

    return f"{top}\n{formatted_text}\n{bottom}"


# Function for a yes no checker (From Lucky Unicorn pre-assessment)
def yes_no(question_text):
    while True:
        # ask player input - (if they need instructions)

        answer = input(question_text).lower()

        # if player input == yes or y output - (Instructions)

        if answer == "y" or answer == "yes":
            answer = "yes"
            return answer

        # if player input == no or n output - ('Display menu')
        elif answer == "n" or answer == "no":
            answer = "no"
            return answer

        # otherwise output - (error)
        else:
            print("error -invalid input- (please enter yes/no or y/n)")


# Main routine

# Welcome screen
print(text_formatter("-", "", "-", "Welcome To Maori Quiz"))
# Loop to test yes_no checker
for item in range(10):
    # Asks player if they need instructions
    instructions = yes_no("Do you need Instructions? (enter y or n): ")
    # Gives instructions  then menu when the answer is yes or just menu when no

    if instructions == "yes":
        print("Instructions")
        print("Menu")
    else:
        print("Menu")
