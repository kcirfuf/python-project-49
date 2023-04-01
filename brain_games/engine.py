import prompt
from brain_games.cli import welcome_and_get_user_name
COUNT_OF_ROUNDS = 3


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def run_game(game_func, question_func):
    name = welcome_and_get_user_name()
    question_func()
    i = 0
    while i < COUNT_OF_ROUNDS:
        result = game_func()
        answer = get_answer()
        if result == answer:
            print('Correct')
        else:
            print(f'"{answer}" is wrong answer ;(.',
                  f'Correct answer was "{result}"\n',
                  f'Let\'s try again, {name}')
            return
        i += 1
    print(f'Congratulations, {name}!')
