#!/usr/bin/env python3
from random import randint
from brain_games.scripts.game_logic import welcome_user, \
    answer, reaction, check_answer


def main():
    pass


if __name__ == "__main__":
    main()


def operation(n1, n2):  # По алгоритму Эвклида НОД
    while n1 != n2:
        if n1 > n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1
    return n2


def loop():
    for i in range(3):
        n1, n2 = randint(1, 100), randint(1, 100)
        oper = operation(n1, n2)  # происходит операци
        print(f'Question: {n1} {n2}')  # задается вопрос пользователю
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


game_rules = 'Find the greatest common divisor of given numbers.'
cor = "Correct!"
name_user = welcome_user(game_rules)

loop()
