#!/usr/bin/env python3

import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    num = random.randint(1, 50)
    question = num
    answer = 'yes'
    for i in range(2, num):
        if num % i == 0:
            answer = 'no'
            break
    return question, answer