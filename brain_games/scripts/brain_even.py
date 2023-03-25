#!/usr/bin/env python3
from brain_games.cli import welcome_user
import random
import prompt
COUNT_OF_ROUNDS = 3


def check_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < COUNT_OF_ROUNDS:
        number = random.randint(0, 50)
        print(f"Question: {number}")
        answer = get_answer()

        result = check_even(number)
        if result == answer:
            print('Correct')
        else:
            print(f'"{answer}" is wrong answer ;(. \
                  Correct answer was "{result}"')
            return
        i += 1
    print(f'Congratulations, {name}!')


def main():
    name = welcome_user()
    even_game(name)


if __name__ == '__main__':
    main()
