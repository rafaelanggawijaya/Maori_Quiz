"""Maori Quiz v1
A program that tests players knowledge on maori language.
10 questions and a hard or easy difficulty. It is timed to encourage the
player to practice and get better times.
Update: Added 01 component which has two functions. This component has the
welcome screen and a yes/no checker for an option for players to have
instructions
By Rafael Anggawijaya"""


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


# Function instructions (From Lucky Unicorn pre-assessment)

def instructions():
    print("***How To Play***")
    print()
    print("The rules of the game go here")
    print()
    print("menu")
    print()


# Main routine

# Welcome screen
print(text_formatter("-", "", "-", "Welcome To Maori Quiz"))

# Asks player if they need instructions
instructions_ = yes_no("Do you need Instructions? (enter y or n): ")
# Gives instructions  then menu when the answer is yes or just menu when no

if instructions_ == "yes":
    instructions()
else:
    print("Menu")
