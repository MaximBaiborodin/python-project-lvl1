import prompt

import random


def progression_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print("What number is missing in the progression?")
    winscore = 0
    rounds = 3
    while winscore < rounds:
        num1 = random.randint(1, 10)
        num2 = random.randint(20, 40)
        step = random.randint(2,5)
        progression = list(range(num1, num2, step))
        answer = str(random.choice(progression))
        mod_progression = ' '.join(map(str, progression))
        question = mod_progression.replace(answer, '..', 1)
        print(f'Question: {question}')
        usr_answ = prompt.string('Your answer: ')
        if answer == usr_answ:
            print('Correct!')
            winscore += 1
        elif answer != usr_answ:
            print(f"{usr_answ} is wrong answer ;(. Correct answer was {answer}.\
Let's try again, {name}")
            return
    print(f'Congratulations, {name}!')