#!/usr/bin/env python3

import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    if question == 1:
        return False
    for i in range(2, question):
        if question % i == 0:
            return False
    return True


def get_question_and_answer():
    question = random.randint(1, 5)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
