"""Maori Quiz v2
A program that tests players knowledge on maori language.
10 questions and a hard or easy difficulty. It is timed to encourage the
player to practice and get better times.
Update: Added component 2 menu function
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
    print()
    print()


# menu function
def menu(mode, difficulty):
    # tittle/ decoration
    print("***menu***\n")
    # while loop to keep asking question
    answer_mode = input(mode)
    while True:
        # asks player for what mode to play on
        # mode 1 selection
        if answer_mode == "1" or answer_mode == "one":
            answer_mode = "Numbers"
            break
            # mode 2 selection
        elif answer_mode == "2" or answer_mode == "two":
            answer_mode = "Days"
            break
            # error for unexpected inputs
        else:
            print("<error> please enter a valid option (1 or 2)")
            answer_mode = input(mode)
    # while loop to ask question again if player does not input a valid answer
    answer_level = input(difficulty)
    while True:
        # When easy is selected
        if answer_level == "easy" or answer_level == "e":
            answer_level = "Easy"
            break
        # when hard is selected
        elif answer_level == "hard" or answer_level == "h":
            answer_level = "Hard"
            break
        # if player enters an invalid intput
        else:
            print("<error> please enter a valid option (easy or hard)")
            answer_level = input(difficulty)
    total_answer = answer_level + answer_mode
    return total_answer


# Main routine

# Welcome screen
print(text_formatter("-", "", "-", "Welcome To Maori Quiz"))

# Asks player if they need instructions
instructions_ = yes_no("Do you need Instructions? (enter y or n): ")
# Gives instructions  then menu when the answer is yes or just menu when no

if instructions_ == "yes":
    instructions()
    menu_ = menu(("What mode do you want\n1. numbers(enter 1)\n2. "
                  "days(enter 2)\n:"),
                 "What difficulty do you want to play on?(easy or hard):")
else:
    menu_ = menu(("What mode do you want\n1. numbers(enter 1)\n2. "
                  "days(enter 2)\n:"),
                 "What difficulty do you want to play on?(easy or hard):")
