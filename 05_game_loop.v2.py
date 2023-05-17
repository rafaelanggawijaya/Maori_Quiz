"""Maori Quiz -game loop- v1
This program is what is responsible for the game mechanics and the question
generating. It also gives a score and times the player"""

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

menu_ = menu(("What mode do you want\n1. numbers(enter 1)\n2. "
              "days(enter 2)\n:"),
             "What difficulty do you want to play on?(easy or hard):")

number_english = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
number_maori = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru",
                "iwa", "tekau"]
day_english = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
               "Saturday", "Sunday"]
day_maori = ["Rahina", "Ratu", "Raapa", "Rapare", "Ramere", "Rahoroi",
             "Ratapu"]
score = 0
number_ = ""
time_ = 0
print("\nStarting in :\n3")
time.sleep(1)
print(2)
time.sleep(1)
print(1)
start = time.time()
if menu_ == "easy number":
    for i in number_english:
        question = random.choice(number_english)
        attempt = input(f"What is the maori word for {question}\n>")
        answer_index = number_english.index(question)
        answer = number_maori[answer_index]
        if attempt == answer:
            print("Correct")
            score += 1
        else:
            print("Wrong")
elif menu_ == "easy day":
    for i in day_english:
        question = random.choice(day_english)
        attempt = input(f"What is the maori word for {question}\n>")
        answer_index = day_english.index(question)
        answer = day_maori[answer_index]
        if answer == i[1].lower():
            print("Correct")
            score += 1
        else:
            print("Wrong")
elif menu_ == "hard number":
    random.shuffle(number)
    for i in number:
        random_ = random.randint(0, 1)
        if random_ == 0:
            number_ = "maori"
            correct = 1
        else:
            number_ = "english"
            correct = 0
        answer = input(f"What is the {number_} word for"
                       f" {i[random_]}\n>").lower()
        if answer == i[correct].lower():
            print("Correct")
            score += 1
        else:
            print("Wrong")
elif menu_ == "hard day":
    random.shuffle(day)
    for i in day:
        random_ = random.randint(0, 1)
        if random_ == 0:
            number_ = "maori"
            correct = 1
        else:
            number_ = "english"
            correct = 0
        answer = input(f"What is the {number_} word for"
                       f" {i[random_]}\n>").lower()
        if answer == i[correct].lower():
            print("Correct")
            score += 1
        else:
            print("Wrong")

end = time.time()
time_ = end - start
print(f"{score}/10")
print(f"Your time = {time_:.2f} seconds")
