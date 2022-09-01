import prompt

import random

import math


def gcd_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print("Find the greatest common divisor of given numbers.")
    score = 0
    winscore = 3
    while score < winscore:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        answer = str(math.gcd(num1, num2))
        question = f'{num1} {num2}'
        print(f'Question: {question}')
        usr_answ = prompt.string('Your answer: ')
        if answer == usr_answ:
            print('Correct!')
            score += 1
        elif answer != usr_answ:
            print(f"{usr_answ} is wrong answer ;(. Correct answer was {answer}.\
Let's try again, {name}")
            return
    print(f'Congratulations, {name}!')
