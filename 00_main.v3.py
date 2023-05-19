"""Maori Quiz v1
A program that tests players knowledge on maori language.
10 questions and a hard or easy difficulty. It is timed to encourage the
player to practice and get better times.
Update: Added component 3 game loop
By Rafael Anggawijaya"""

import random
import time


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

        answer_ = input(question_text).lower()

        # if player input == yes or y output - (Instructions)

        if answer_ == "y" or answer_ == "yes":
            answer_ = "yes"
            return answer_

        # if player input == no or n output - ('Display menu')
        elif answer_ == "n" or answer_ == "no":
            answer_ = "no"
            return answer_

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
    # calls instruction function
    instructions()
    # calls menu function
    menu_ = menu(("What mode do you want\n1. numbers(enter 1)\n2. "
                  "days(enter 2)\n:"),
                 "What difficulty do you want to play on?(easy or hard):")
else:
    # calls menu function
    menu_ = menu(("What mode do you want\n1. numbers(enter 1)\n2. "
                  "days(enter 2)\n:"),
                 "What difficulty do you want to play on?(easy or hard):")

# calls menu function


# list for number question and answer
number = [["1", "tahi"], ["2", "rua"], ["3", "toru"], ["4", "wha"],
          ["5", "rima"],
          ["6", "ono"], ["7", "whitu"], ["8", "waru"], ["9", "iwa"], ["10",
                                                                      "tekau"]]
# list for number question and answer
day = [["Monday", "Rahina"], ["Tuesday", "Ratu"], ["Wednesday", "Raapa"],
       ["Thursday", "Rapare"], ["Friday", "Ramere"], ["Saturday", "Rahoroi"],
       ["Sunday", "Ratapu"]]

# sets score
score = 0
# sets question (can change to maori or english for hard mode)
type_ = ""
# sets time
time_ = 0
time.sleep(1)
# count down
print("\nStarting in :\n3")
time.sleep(1)
print(2)
time.sleep(1)
print(1)
start = time.time()
# starts game loop for certain modes and difficulty
if menu_ == "easy number":
    # question generator
    random.shuffle(number)
    for i in number:
        # question
        answer = input(f"What is the maori word for {i[0]}\n>")
        # checks answer
        if answer == i[1]:
            print("Correct")
            score += 1
        else:
            print("Wrong")
elif menu_ == "easy day":
    # question generator
    random.shuffle(day)
    for i in day:
        # question
        answer = input(f"What is the maori word for {i[0]}\n>").lower()
        # checks answer
        if answer == i[1].lower():
            print("Correct")
            score += 1
        else:
            print("Wrong")
elif menu_ == "hard number":
    # question generator
    random.shuffle(number)
    for i in number:
        # generates a number to pick between maori and english
        random_ = random.randint(0, 1)
        if random_ == 0:
            type_ = "maori"
            correct = 1
        else:
            type_ = "english"
            correct = 0
        # question
        answer = input(f"What is the {type_} word for"
                       f" {i[random_]}\n>").lower()
        # checks answer
        if answer == i[correct].lower():
            print("Correct")
            score += 1
        else:
            print("Wrong")
elif menu_ == "hard day":
    # question generator
    random.shuffle(day)
    for i in day:
        # generates a number to pick between maori and english
        random_ = random.randint(0, 1)
        if random_ == 0:
            type_ = "maori"
            correct = 1
        else:
            type_ = "english"
            correct = 0
        # question
        answer = input(f"What is the {type_} word for"
                       f" {i[random_]}\n>").lower()
        # checks answer
        if answer == i[correct].lower():
            print("Correct")
            score += 1
        else:
            print("Wrong")
