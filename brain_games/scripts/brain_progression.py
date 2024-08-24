#!/usr/bin/env python3


import random
from brain_games.cli import welcome_user


def main():
    # welcome_user()
    progression()


if __name__ == '__main__':
    main()


def progression():
    name1 = welcome_user()
    print('What number is missing in the progression?')
    a = random.randint(1, 50)
    b = random.randint(2, 4)
    c = random.randint(0, 6)
    list = [a, a + 1 * b, a + 2 * b, a + 3 * b, a + 4 * b, a + 5 * b, a + 6 * b]
    x = (list[c])
    list[c] = '..'
    result = ' '.join(str(item) for item in list)
    print("Question:", result)
    y = int(input("Your answer:"))
    if y == x:
        print('Correct!')
    else:
        y != x
        print("'", y, "' is wrong answer ;(. Correct answer was '", x, "'.\nLet's try again,", name1, end='!')  # noqa: E501
        return
    # вторая проходка
    a = random.randint(1, 50)
    b = random.randint(2, 4)
    c = random.randint(0, 6)
    list = [a, a + 1 * b, a + 2 * b, a + 3 * b, a + 4 * b, a + 5 * b, a + 6 * b]
    x = (list[c])
    list[c] = '..'
    result = ' '.join(str(item) for item in list)
    print("Question:", result)
    y = int(input("Your answer:"))
    if y == x:
        print('Correct!')
    else:
        y != x
        print("'", y, "' is wrong answer ;(. Correct answer was '", x, "'.\nLet's try again,", name1, end='!')  # noqa: E501
        return
    # третья проходка
    a = random.randint(1, 50)
    b = random.randint(2, 4)
    c = random.randint(0, 6)
    list = [a, a + 1 * b, a + 2 * b, a + 3 * b, a + 4 * b, a + 5 * b, a + 6 * b]
    x = (list[c])
    list[c] = '..'
    result = ' '.join(str(item) for item in list)
    print("Question:", result)
    y = int(input("Your answer:"))
    if y == x:
        print('Correct!\nCongratulations,', name1, end='!')
    else:
        y != x
        print("'", y, "' is wrong answer ;(. Correct answer was '", x, "'.\nLet's try again,", name1, end='!')  # noqa: E501
        return
