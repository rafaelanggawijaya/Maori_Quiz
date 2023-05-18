import random
import time

# menu function


# main routine

# calls menu function
testing_mode = input("mode:")
testing_difficulty = input("difficulty:")
menu_ = testing_difficulty + " " + testing_mode

# english number list can be an answer or question depending on difficulty and
# random generator
number_english = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# maori number list can be an answer or question depending on difficulty and
# random generator
number_maori = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru",
                "iwa", "tekau"]
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
scored = ""
# sets time
time_ = 0
# starts countdown

start = time.time()
# starts game loop for certain modes and difficulty
if menu_ == "easy number":
    # tells program what to score the player at the end out of
    scored = 10
    for i in range(0, 100):
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
elif menu_ == "easy day":
    # tells program what to score the player at the end out of
    scored = 7
    for i in range(1, 100):
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
elif menu_ == "hard number":
    # tells program what to score the player at the end out of
    scored = 10
    for i in range(1, 100):
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
            remove_ = ""
        else:
            # question generator
            question = random.choice(number_maori)
            # question
            attempt = input(f"What is the english word for {question}\n>")
            # sets answer
            answer_index = number_maori.index(question)
            answer = number_english[answer_index]
            # tells code what to remove
            remove_ = ""
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
elif menu_ == "hard day":
    # tells program what to score the player at the end out of
    scored = 7
    for i in range(1, 100):
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
            remove_ = ""
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
            remove_ = ""
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

# simple version of results to end timer and score
end = time.time()
time_ = end - start
print(f"{score}/{scored}")
print(f"Your time = {time_:.2f} seconds")
