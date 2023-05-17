"""Maori Quiz -game loop- v1
This program is what is responsible for the game mechanics and the question
generating. Easy is straight forward only asking the maori names while hard
chooses between the two asking for english translation of maori words and
vis versa  It also gives a score and times the player"""

import random
import time


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
            answer_mode = "number"
            break
            # mode 2 selection
        elif answer_mode == "2" or answer_mode == "two":
            answer_mode = "day"
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
            answer_level = "easy"
            break
        # when hard is selected
        elif answer_level == "hard" or answer_level == "h":
            answer_level = "hard"
            break
        # if player enters an invalid intput
        else:
            print("<error> please enter a valid option (easy or hard)")
            answer_level = input(difficulty)
    total_answer = str(answer_level + " " + answer_mode)
    return total_answer


# main routine

# calls menu function
menu_ = menu(("What mode do you want\n1. numbers(enter 1)\n2. "
              "days(enter 2)\n:"),
             "What difficulty do you want to play on?(easy or hard):")

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

# simple version of results to end timer and score
end = time.time()
time_ = end - start
print(f"{score}/10")
print(f"Your time = {time_:.2f} seconds")
