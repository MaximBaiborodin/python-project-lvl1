#!/usr/bin/env python3

import random
import operator

DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(list(operators.keys()))
    question = f'{num1} {op} {num2}'
    answer = str(operators.get(op)(num1, num2))
    return question, answer
