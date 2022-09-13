#!/usr/bin/env python3

import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = random.randint(1, 50)
    step = random.randint(2, 10)
    progression = [str(start + i * step) for i in range(random.randint(5, 15))]
    answer = str(random.choice(progression))
    mod_progression = ' '.join(map(str, progression))
    question = mod_progression.replace(answer, '..', 1)
    return question, answer
