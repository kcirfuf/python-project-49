from brain_games.engine import run_game
import random
BOTTOM_LINE = 1
UPPER_LINE = 100


def ask_question():
    print('Find the greatest common divisor of given numbers.')


def get_random_number():
    return random.randint(BOTTOM_LINE, UPPER_LINE)


def evklid(number1, number2):
    if number2 == 0:
        return number1
    return evklid(number2, number1 % number2)


def start_game():
    first_number = get_random_number()
    second_number = get_random_number()
    print(f'Question: {first_number} {second_number}')
    result = evklid(first_number, second_number)
    return str(result)

def main():
    run_game(start_game, ask_question)
