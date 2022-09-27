#!/usr/bin/env python3

import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = random.randint(1, 50)
    step = random.randint(2, 10)
    numbers_count = random.randint(5, 15)
    end = start + (numbers_count * step)
    progression = list(range(start, end, step))
    missing_number = random.randint(0, numbers_count - 1)
    answer = str(progression[missing_number])
    mod_progression = ' '.join(map(str, progression))
    question = mod_progression.replace(answer, '..', 1)
    return question, answer
