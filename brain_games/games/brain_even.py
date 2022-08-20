#!/usr/bin/env python3

import prompt

import random


def main():
    even_game()


def even_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    score = 0
    while score < 3:
        answer = random.randint(1, 100)
        print(f'Question: {answer}')
        usr_answ = prompt.string('Your answer: ')
        if answer % 2 == 0 and usr_answ == 'yes':
            print('Correct!')
            score += 1
        elif answer % 2 != 0 and usr_answ == 'no':
            print('Correct!')
            score += 1
        elif answer % 2 == 0 and usr_answ != 'yes':
            print(f"{usr_answ} is wrong answer ;(. Correct answer was 'yes'.\
Let's try again, {name}")
            return
        elif answer % 2 != 0 and usr_answ != 'no':
            print(f"{usr_answ} is wrong answer ;(. Correct answer was 'no'.\
Let's try again, {name}")
            return
    print(f'Congratulations, {name}!')
