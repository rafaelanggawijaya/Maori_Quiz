"""Maori Quiz -game loop- v3
This program is what is responsible for the game mechanics and the question
generating. Easy is straight forward only asking the maori names while hard
chooses between the two asking for english translation of maori words and
vis versa  It also gives a score and times the player
Update: Made the code into a function"""

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


# Game loop function
def game_loop(mode_difficulty):
    # calls menu function

    # english number list can be an answer or question depending on difficulty
    # and random generator
    number_english = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    # maori number list can be an answer or question depending on difficulty
    # and random generator
    number_maori = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu",
                    "waru", "iwa", "tekau"]
    # english day list can be an answer or question depending on difficulty and
    # random generator
    day_english = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                   "Saturday", "Sunday"]
    # maori day list can be an answer or question depending on difficulty and
    # random generator
    day_maori = ["Rahina", "Ratu", "Raapa", "Rapare", "Ramere", "Rahoroi",
                 "Ratapu"]
    # sets score
    score = 0
    # sets what to score out of to 0
    scored = 0
    # starts countdown
    print("\nStarting in :\n3")
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    # starts timer
    start = time.time()
    # starts game loop for certain modes and difficulty
    if mode_difficulty == "easy number":
        # tells program what to score the player at the end out of
        scored = 10
        for scored in number_english:
            # question generator
            question = random.choice(number_english)
            # question
            attempt = input(f"What is the maori word for {question}\n>")
            # sets answer
            answer_index = number_english.index(question)
            answer = number_maori[answer_index]
            # checks answer if correct or incorrect
            if attempt == answer:
                print("Correct")
                # increases score
                score += 1
            else:
                print("Wrong")
    elif mode_difficulty == "easy day":
        # tells program what to score the player at the end out of
        scored = 7
        for scored in day_english:
            # question generator
            question = random.choice(day_english)
            # question
            attempt = input(f"What is the maori word for {question}\n>")
            # sets answer
            answer_index = day_english.index(question)
            answer = day_maori[answer_index]
            # checks answer if correct or incorrect
            if attempt == answer:
                print("Correct")
                # increases score
                score += 1
            else:
                print("Wrong")
    elif mode_difficulty == "hard number":
        # tells program what to score the player at the end out of
        scored = 10
        for i in range(1, 11):
            # generates a number to pick between maori and english
            random_ = random.randint(0, 1)
            if random_ == 0:
                # question generator
                question = random.choice(number_english)
                # question
                attempt = input(f"What is the maori word for {question}\n>")
                # sets answer
                answer_index = number_english.index(question)
                answer = number_maori[answer_index]
                # tells code what to remove
                remove_ = 1
            else:
                # question generator
                question = random.choice(number_maori)
                # question
                attempt = input(f"What is the english word for {question}\n>")
                # sets answer
                answer_index = number_maori.index(question)
                answer = number_english[answer_index]
                # tells code what to remove
                remove_ = 2
            # checks answer if correct or incorrect
            if attempt == answer:
                print("Correct")
                # increases score
                score += 1
            else:
                print("Wrong")
            # removes question and answer so it won't be repeated
            if remove_ == 1:
                number_maori.remove(answer)
                number_english.remove(question)
            else:
                number_maori.remove(question)
                number_english.remove(answer)
    elif mode_difficulty == "hard day":
        # tells program what to score the player at the end out of
        scored = 7
        for i in range(1, 8):
            random_ = random.randint(0, 1)
            if random_ == 0:
                # question generator
                question = random.choice(day_english)
                # question
                attempt = input(f"What is the maori word "
                                f"for {question}\n>").lower()
                # sets answer
                answer_index = day_english.index(question)
                answer = day_maori[answer_index]
                # tells code what to remove
                remove_ = 1
            else:
                # question generator
                question = random.choice(day_maori)
                # question
                attempt = input(f"What is the english word "
                                f"for {question}\n>").lower()
                # sets answer
                answer_index = day_maori.index(question)
                answer = day_english[answer_index]
                # tells code what to remove
                remove_ = 2
            # checks answer if correct or incorrect
            if attempt == answer:
                print("Correct")
                # increases score
                score += 1
            else:
                print("Wrong")
            # removes question and answer so it won't be repeated
            if remove_ == 1:
                day_maori.remove(answer)
                day_english.remove(question)
            else:
                day_maori.remove(question)
                day_english.remove(answer)
    end = time.time()
    time_ = end - start
    results = [time_, score, scored]
    return results


# main routine

# simple version of results to end timer and score
menu_ = menu(("What mode do you want\n1. numbers(enter 1)\n2. "
              "days(enter 2)\n:"),
             "What difficulty do you want to play on?(easy or hard):")
results_ = game_loop(menu_)
print(f"{results_[1]}/{results_[2]}")
print(f"Your time = {results_[0]:.2f} seconds")
