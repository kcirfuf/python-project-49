from brain_games.engine import run_game
import random
BOTTOM_LINE = 1
UPPER_LINE = 9
LENGTH_OF_PROGRESSION = 10


def ask_question():
    print('What number is missing in the progression?')


def get_random_number():
    return random.randint(BOTTOM_LINE, UPPER_LINE)


def generate_progression():
    progression = [0] * LENGTH_OF_PROGRESSION
    first_element = get_random_number()
    progression_step = get_random_number()
    for index, item in enumerate(progression):
        if index == 0:
            progression[index] = first_element
        progression[index] = progression[index - 1] + progression_step
    return progression


def make_question():
    random_number = get_random_number()
    progression = generate_progression()
    result = progression[random_number]
    progression[random_number] = ".."
    return progression, result


def start_game():
    progression, result = make_question()
    print('Question:', *progression)
    return str(result)


def main():
    run_game(start_game, ask_question)
