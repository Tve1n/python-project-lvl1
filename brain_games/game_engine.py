import prompt


def start_game(game):
    print("Welcome to the Brain Games!")
    name_u = prompt.string("May I have your name? ")
    print(f'Hello, {name_u}!')

    print(game.RULES)  # 1) Правила игры
    round_count = 3

    for _ in range(round_count):
        operation, true_answer = game.get_question_and_answer()
        print(f'Question: {operation}')
        guess = prompt.string("Your answer: ")

        if str(true_answer) != guess:
            print(f"'{guess}' is wrong answer ;(."
                  f"Correct answer was '{true_answer}'.\n"
                  f"Let's try again, {name_u}!")
            break

        print('Correct')

    else:
        print(f"Congratulations, {name_u}!")
