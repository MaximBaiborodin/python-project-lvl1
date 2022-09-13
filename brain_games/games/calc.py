#!/usr/bin/env python3

import random


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    operator = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(operator)
    question = f'{num1}{op}{num2}'
    if op == '+':
        answer = str(num1 + num2)
    if op == '-':
        answer = str(num1 - num2)
    if op == '*':
        answer = str(num1 * num2)
    return question, answer