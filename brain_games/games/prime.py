import prompt

import random


def prime_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    winscore = 0
    rounds = 3
    while winscore < rounds:
        num = random.randint(2, 50)
        print(f'Question: {num}')
        answer = 'yes'
        for i in range(2, num):
            if num % i == 0:
               answer = 'no'
               break
        usr_answ = prompt.string('Your answer: ')
        if answer == usr_answ:
            print('Correct!')
            winscore += 1
        elif answer != usr_answ:
            print(f"{usr_answ} is wrong answer ;(. Correct answer was {answer}.\
Let's try again, {name}")
            return
    print(f'Congratulations, {name}!')