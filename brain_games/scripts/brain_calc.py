import prompt

import random

import operator

def main():
    calc_game()


def calc_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print("What is the result of the expression?")
    score = 0
    operator = ['+', '-', '*']
    while score < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        op = random.choice(operator)
        answer = f'{num1}{op}{num2}'
        print(f'Question: {answer}')
        user_answer = prompt.string('Your answer: ')
        if op == '+':
            answer = str(num1 + num2)
        if op == '-':
            answer = str(num1 - num2)
        if op == '*':
            answer = str(num1 * num2)
        if answer ==  user_answer:
            print('Correct!')
            score += 1
        elif answer != user_answer:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer}.\
Let's try again, {name}")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
