import prompt



def welcome_user(name_u, game):  # Функция для приветствия
    print("Welcome to the Brain Games!")
    print(f'Hello, {name_u}!')
    print(game)


def answer():  # Функция для запроса ответа
    que = prompt.string("Your answer: ")  
    return que


def reaction(name_u, answer1, answer2):  # Функция для реакции
    t_again = f"Let's try again, {name_u}!"
    fail = f"'{answer1}' is wrong answer ;(. Correct answer was '{answer2}'."
    return f"{fail}\n {t_again}"


def w():  # Функция для Вопроса
    pass

print(reaction("nik", 25, 2))