#!/usr/bin/env python3
from random import randint, choice
from game_logic import *


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


def check_answer(otvet, kk):
    if otvet == kk:
        return True
    else:
        return False


def loop():
    for i in range(3):
        spisok = ['+', "-", "*"]
        sp4 = [randint(1, 100), randint(1, 100)]
        n1, n2 = max(sp4), min(sp4)
        znak = choice(spisok)  # в первых 4х происходит присвоение чисел и знака

        oper = operation(n1, n2, znak)  # происходит операция

        print(f'Question: {n1} {znak} {n2}')  # задается вопрос пользователю

        kk = int(answer())  # ответ от пользователя

        check = check_answer(oper, kk)  # Проверка на правильность ответа
        print(type(oper), type(kk), type(check))
        if check == True:
            print(cor)
            continue
        elif check == False:
            print(reaction(name_user, kk, oper))
            break
    else:
        print(f"Congratulations, {name_user}!")

    
game_rules = "What is the result of the expression?"
cor = "Correct!"
name_user = welcome_user(game_rules)
#game_logic.welcome_user(name_user, game_rules)

loop()
