from random import randint, choice


def main():
    pass


if __name__ == "__main__":
    main()


def calculation(n1, znak, n2):
    if znak == '+':
        return n1 + n2
    elif znak == "-":
        return n1 - n2
    elif znak == '*':
        return n1 * n2



rules = "What is the result of the expression?"

def randss():
    spisok = ['+', "-", "*"]
    sp4 = [randint(1, 100), randint(1, 100)]
    n1, n2 = max(sp4), min(sp4)
    znak = choice(spisok)
    OP = f'{n1} {znak} {n2}'
    TA = calculation(n1, znak, n2)
    return OP, TA




