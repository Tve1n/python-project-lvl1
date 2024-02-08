import prompt


def game_engine(game): 
    print("Welcome to the Brain Games!") 
    name_u = prompt.string("May I have your name? ")  
    print(f'Hello, {name_u}!')
    print(game.rules)  # 1) Правила игры 
    for i in range(3):
        operation, true_answer = game.objective()  # две переменные разом
        print(f'Question: {operation}')  
        guess = prompt.string("Your answer: ")  # ПОДУМАТЬ КАК ИСПРАВИТЬ СТРОЧКУ!!!
        t_again = f"Let's try again, {name_u}!"
        fail = f"'{guess}' is wrong answer ;(. Correct answer was '{true_answer}'."
        if str(true_answer) == guess:  
            print('Correct')
            continue
        else:
            print(f'{fail}\n{t_again}')
            break
    else:
        print(f"Congratulations, {name_u}!")
