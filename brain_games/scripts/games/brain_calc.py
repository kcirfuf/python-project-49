from brain_games.engine import run_game
import random
OPERATIONS = ("+", "-", "*")
BOTTOM_LINE = 0
UPPER_LINE = 25


def ask_question():
    print('What is the result of the expression?.')


def get_random_operation():
    lenght_of_operations = len(OPERATIONS) - 1
    random_index = random.randint(0, lenght_of_operations)
    operation = OPERATIONS[random_index]
    return operation


def get_random_number():
    return random.randint(BOTTOM_LINE, UPPER_LINE)


def calc_expression(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    else:
        return "unsopported operation"


def start_game():
    random_operation = get_random_operation()
    first_number = get_random_number()
    second_number = get_random_number()
    print(f'Question: {first_number} {random_operation} {second_number}')
    result = calc_expression(first_number, second_number, random_operation)
    return str(result)


def main():
    run_game(start_game, ask_question)


if __name__ == '__main__':
    main()
