import random

from Lists import *
from Questions import *


class Player:
    def __init__(self, name = "", point = 0, max_point = 0):
        self.name = name
        self.point = point
        self.max_point = max_point
        self.questions_answered = []
    
    def correct_answer(self, question):
        if question.point_worth == 1:
            print("\nThat was a good answer! You receive {point_worth} point!\n".format(point_worth = question.point_worth))
        else:
            print("\nThat was a good answer! You receive {point_worth} points!\n".format(point_worth = question.point_worth))
        self.point += question.point_worth
        self.max_point += question.point_worth
        self.questions_answered.append(question.question_id)

    def wrong_answer(self, question):
        print("\nThat was a wrong answer :( The right answer is   {answer}  \n\n".format(answer = question.answer))
        self.max_point += question.point_worth
        self.questions_answered.append(question.question_id)


player1 = Player()

print("\nWelcome to my first Japanese Learning App!\n\n")
player1.name = input("Before anything, can you tell me your name?\n")

print("\nHi {name}! Welcome to my game!".format(name = player1.name))


number_of_questions = int(input("How many questions do you want to answer? Between 10 and 30.\n"))

while number_of_questions < 10 or number_of_questions > 30:
    print("\nNo, please be serious and enter a number between 10 and 30!")
    number_of_questions = int(input("How many questions do you want to answer? Between 10 and 30.\n"))

print("Thank you! You will be asked {number_of_questions} questions. Do your best and try to get a score \
as high as possible!\n".format(number_of_questions = number_of_questions))

i = 1
conversion = {"A" : 0, "B" : 1, "C" : 2, "D" : 3}

while i < number_of_questions + 1:
    if i < number_of_questions:
        print("Question # {i}".format(i = i))
    else:
        print("And here is your final question!\n")
    
    question = random.choice(Question.questions_list)
    while question.question_id in player1.questions_answered:
        question = random.choice(Question.questions_list)
    
    answers = ["", "", "", ""]

    if question.type_of_question == "pronounciation":
        while len(answers) > len(set(answers)):
            answers = ["", "", "", ""]
            random_index = random.randrange(0,3)
            answers[random_index] = question.answer
            if answers[0] == "":
                answers[0] = random.choice(syllable_list)
            if answers[1] == "":
                answers[1] = random.choice(syllable_list)
            if answers[2] == "":
                answers[2] = random.choice(syllable_list)
            if answers[3] == "":
                answers[3] = random.choice(syllable_list)
    
    if question.type_of_question == "hiragana":
        while len(answers) > len(set(answers)):
            answers = ["", "", "", ""]
            random_index = random.randrange(0,3)
            answers[random_index] = question.answer
            if answers[0] == "":
                answers[0] = random.choice(hiragana_list)
            if answers[1] == "":
                answers[1] = random.choice(hiragana_list)
            if answers[2] == "":
                answers[2] = random.choice(hiragana_list)
            if answers[3] == "":
                answers[3] = random.choice(hiragana_list)


    if question.type_of_question == "katakana":
        while len(answers) > len(set(answers)):
            answers = ["", "", "", ""]
            random_index = random.randrange(0,3)
            answers[random_index] = question.answer
            if answers[0] == "":
                answers[0] = random.choice(katakana_list)
            if answers[1] == "":
                answers[1] = random.choice(katakana_list)
            if answers[2] == "":
                answers[2] = random.choice(katakana_list)
            if answers[3] == "":
                answers[3] = random.choice(katakana_list)
            
    print(question.question_sentence)
    print("A. " + answers[0])
    print("B. " + answers[1])
    print("C. " + answers[2])
    print("D. " + answers[3])

    players_answer = input("Your answer: ")
    possible_answer = ["A", "B", "C", "D"]

    while players_answer.upper() not in possible_answer:
        players_answer = input("Come on, give me your real answer! ")

    if answers[conversion[players_answer.upper()]] == question.answer:
        player1.correct_answer(question)
    else:
        player1.wrong_answer(question)
    
    i += 1

percentage = int((player1.point * 100 / player1.max_point)) + (player1.point % player1.max_point > 0)
print("{name}, your score is {point} on {max_point} for a total of {percent}%!".format(name = player1.name, point = player1.point, max_point = player1.max_point, \
    percent = percentage))

print("Thank you very much for playing!")


