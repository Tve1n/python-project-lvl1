import prompt
from random import randint, choice


def welcome_user(game):  # Функция для приветствия
    print("Welcome to the Brain Games!")
    name_u = prompt.string("May I have your name? ")
    print(f'Hello, {name_u}!')
    print(game)
    return name_u


def answer():  # Функция для запроса ответа
    que = prompt.string("Your answer: ")
    return que


def reaction(name_u, answer1, answer2):  # Функция для реакции
    t_again = f"Let's try again, {name_u}!"
    fail = f"'{answer1}' is wrong answer ;(. Correct answer was '{answer2}'."
    return f"{fail}\n {t_again}"
