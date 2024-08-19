#!/usr/bin/env python3


import random
from brain_games.cli import welcome_user


def main():
    # welcome_user()
    nod()


if __name__ == '__main__':
    main()


def nod():
    name1 = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    # первый проход
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    print('Question:', a, b)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    y = int(input("Your answer:"))
    if y == a:
        print('Correct!')
    else:
        y != a
        print("'", y, "' is wrong answer ;(. Correct answer was '", a, "'.\nLet's try again,", name1)  # noqa: E501
        return
    # второй проход
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    print('Question:', a, b)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    y = int(input("Your answer:"))
    if y == a:
        print('Correct!')
    else:
        y != a
        print("'", y, "' is wrong answer ;(. Correct answer was '", a, "'.\nLet's try again,", name1)  # noqa: E501
        return
    # третий проход
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    print('Question:', a, b)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    y = int(input("Your answer:"))
    if y == a:
        print('Correct!\nCongratulations,', name1)
    else:
        y != a
        print("'", y, "' is wrong answer ;(. Correct answer was '", a, "'.\nLet's try again,", name1)  # noqa: E501
        return
