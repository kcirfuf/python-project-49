#!/usr/bin/env python3
from brain_games.engine import run_game
import random


def check_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def ask_question():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def start_game():
    number = random.randint(0, 50)
    print(f'Question: {number}')
    result = check_even(number)
    return result


def main():
    run_game(start_game, ask_question)


if __name__ == '__main__':
    main()
