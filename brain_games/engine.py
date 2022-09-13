#!/usr/bin/env python3

import prompt


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.DESCRIPTION)
    winscore = 0
    rounds = 3
    while winscore < rounds:
        question, answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if answer == user_answer:
            print('Correct!')
            winscore += 1
        elif answer != user_answer:
            print(f"{user_answer} is wrong answer ;(.")
            print(f"Correct answer was {answer}. Let's try again, {name}")
            break
        if winscore == 3:
            print(f'Congratulations, {name}!')
