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
        question = random.randint(1, 100)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if question % 2 == 0 and answer == 'yes':
            print('Correct!')
            score += 1
        elif question % 2 != 0 and answer == 'no':
            print('Correct!')
            score += 1
        elif question % 2 == 0 and answer != 'yes':
            print(f"{answer} is wrong answer ;(. Correct answer was 'yes'.\
Let's try again, {name}")
            return
        elif question % 2 != 0 and answer != 'no':
            print(f"{answer} is wrong answer ;(. Correct answer was 'no'.\
Let's try again, {name}")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
