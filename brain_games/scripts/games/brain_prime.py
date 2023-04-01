from brain_games.engine import run_game
import random
BOTTOM_LINE = 1
UPPER_LINE = 100


def ask_question():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def get_random_number():
    return random.randint(BOTTOM_LINE, UPPER_LINE)


def is_prime(number):
    if number % 2 == 0:
        if number == 2:
            return 'yes'
        else:
            return 'no'
    divider = 3
    while divider * divider <= number and number % divider != 0:
        divider += 2
    if divider * divider > number:
        return 'yes'
    else:
        return 'no'


def start_game():
    number = get_random_number()
    result = is_prime(number)
    print(f'Question: {number}')
    return str(result)


def main():
    run_game(start_game, ask_question)
