#!/usr/bin/env python3
from random import randint
from brain_games.scripts.game_logic import welcome_user, \
    answer, reaction, check_answer


def main():
    pass


if __name__ == "__main__":
    main()


def progression():
    b_prev = randint(1, 20)  # первое число
    list_progress = [b_prev]
    q = randint(2, 5)  # знаменатель прогресии
    for i in range(9):
        b_cur = b_prev + q  # следующий элемент прогрессии
        b_prev = b_cur
        list_progress.append(b_cur)
    return list_progress


def loop():
    for i in range(3):
        spisok = progression()
        rand_num = randint(0, 9)
        spisok.insert(rand_num + 1, '..')
        del_el = spisok.pop(rand_num)  # Удаленное из последовательности число
        print('Question: ', end='')  # задается вопрос пользователю
        print(*spisok)
        guess = int(answer())  # ответ от пользователя
        check = check_answer(del_el, guess)  # Проверка на правильность ответа

        if check is True:
            print(cor)
            continue
        elif check is False:
            print(reaction(name_user, guess, del_el))
            break
    else:
        print(f"Congratulations, {name_user}!")


game_rules = "What number is missing in the progression?"
cor = "Correct!"
name_user = welcome_user(game_rules)

loop()
