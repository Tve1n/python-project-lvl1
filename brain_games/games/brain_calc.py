#!/usr/bin/env python3
from random import randint, choice
from brain_games.scripts.game_logic import welcome_user, \
    answer, reaction, check_answer


def main():
    pass


if __name__ == "__main__":
    main()


def operation(n1, n2, znak):
    if znak == '+':
        return n1 + n2
    elif znak == "-":
        return n1 - n2
    elif znak == '*':
        return n1 * n2


def loop():
    for i in range(3):
        spisok = ['+', "-", "*"]
        sp4 = [randint(1, 100), randint(1, 100)]
        n1, n2 = max(sp4), min(sp4)
        znak = choice(spisok)  # в первых 4х происходит присвоение чисел и знака

        oper = operation(n1, n2, znak)  # происходит операция

        print(f'Question: {n1} {znak} {n2}')  # задается вопрос пользователю

        guess = int(answer())  # ответ от пользователя

        check = check_answer(oper, guess)  # Проверка на правильность ответа

        if check is True:
            print(cor)
            continue
        elif check is False:
            print(reaction(name_user, guess, oper))
            break
    else:
        print(f"Congratulations, {name_user}!")


game_rules = "What is the result of the expression?"
cor = "Correct!"
name_user = welcome_user(game_rules)

loop()

# Вызываем функцию движка игры 
