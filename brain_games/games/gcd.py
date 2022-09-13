#!/usr/bin/env python3

import random

import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    question = f'{num1} {num2}'
    answer = str(math.gcd(num1, num2))
    return question, answer
