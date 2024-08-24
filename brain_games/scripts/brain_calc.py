#!/usr/bin/env python3


import random
from brain_games.cli import welcome_user


def main():
    # welcome_user()
    calc()


if __name__ == '__main__':
    main()


def calc():
    name1 = welcome_user()
    print('What is the result of the expression?')
    # первый проход
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    seq = ['+', "-", "*"]
    c = random.choice(seq)
    print("Question:", a, c, b)
    if c == '+':
        d = a + b
    elif c == '-':
        d = a - b
    elif c == '*':
        d = a * b
    y = int(input("Your answer:"))
    if y == d:
        print('Correct!')
    else:
        y != d
        print("'", y, "' is wrong answer ;(. Correct answer was '", d, "'.\nLet's try again,", name1, end='!')  # noqa: E501
        return
    # второй проход
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    seq = ['+', "-", "*"]
    c = random.choice(seq)
    print("Question:", a, c, b)
    if c == '+':
        d = a + b
    elif c == '-':
        d = a - b
    elif c == '*':
        d = a * b
    y = int(input("Your answer:"))
    if y == d:
        print('Correct!')
    else:
        y != d
        print("'", y, "' is wrong answer ;(. Correct answer was '", d, "'.\nLet's try again,", name1, end='!')  # noqa: E501
        return
    # третий проход
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    seq = ['+', "-", "*"]
    c = random.choice(seq)
    print("Question:", a, c, b)
    if c == '+':
        d = a + b
    elif c == '-':
        d = a - b
    elif c == '*':
        d = a * b
    y = int(input("Your answer:"))
    if y == d:
        print('Correct!\nCongratulations,', name1, end='!')
        return
    else:
        y != d
        print("'", y, "' is wrong answer ;(. Correct answer was '", d, "'.\nLet's try again,", name1, end='!')  # noqa: E501
        return
