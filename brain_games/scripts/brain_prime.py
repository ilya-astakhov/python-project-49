#!/usr/bin/env python3


import random
from brain_games.cli import welcome_user


def main():
    # welcome_user()
    prime()


if __name__ == '__main__':
    main()


def prime():
    name1 = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    # первый проход
    x = random.randint(2, 101)
    print('Question:', x)
    y = (input("Your answer:"))
    if y in ['yes'] and (x == 2 or x == 3 or x == 5 or x == 7 or x == 11 or x == 13 or x == 17 or x == 19 or x == 23 or x == 29 or x == 31 or x == 37 or x == 41 or x == 43 or x == 47 or x == 53 or x == 59 or x == 61 or x == 67 or x == 71 or x == 73 or x == 79 or x == 83 or x == 89 or x == 97 or x == 101):  # noqa: E501
        print('Correct!')
    elif y in ['yes'] and (x != 2 or x != 3 or x != 5 or x != 7 or x != 11 or x != 13 or x != 17 or x != 19 or x != 23 or x != 29 or x != 31 or x != 37 or x != 41 or x != 43 or x != 47 or x != 53 or x != 59 or x != 61 or x != 67 or x != 71 or x != 73 or x != 79 or x != 83 or x != 89 or x != 97 or x != 101):  # noqa: E501
        print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again,", name1, end='!')  # noqa: E501
        return
    elif y in ['no'] and (x == 2 or x == 3 or x == 5 or x == 7 or x == 11 or x == 13 or x == 17 or x == 19 or x == 23 or x == 29 or x == 31 or x == 37 or x == 41 or x == 43 or x == 47 or x == 53 or x == 59 or x == 61 or x == 67 or x == 71 or x == 73 or x == 79 or x == 83 or x == 89 or x == 97 or x == 101):  # noqa: E501
        print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again,", name1, end='!')  # noqa: E501
        return
    elif y in ['no'] and (x != 2 or x != 3 or x != 5 or x != 7 or x != 11 or x != 13 or x != 17 or x != 19 or x != 23 or x != 29 or x != 31 or x != 37 or x != 41 or x != 43 or x != 47 or x != 53 or x != 59 or x != 61 or x != 67 or x != 71 or x != 73 or x != 79 or x != 83 or x != 89 or x != 97 or x != 101):  # noqa: E501
        print('Correct!')
    else:
        return
    # второй проход
    x = random.randint(2, 101)
    print('Question:', x)
    y = (input("Your answer:"))
    if y in ['yes'] and (x == 2 or x == 3 or x == 5 or x == 7 or x == 11 or x == 13 or x == 17 or x == 19 or x == 23 or x == 29 or x == 31 or x == 37 or x == 41 or x == 43 or x == 47 or x == 53 or x == 59 or x == 61 or x == 67 or x == 71 or x == 73 or x == 79 or x == 83 or x == 89 or x == 97 or x == 101):  # noqa: E501
        print('Correct!')
    elif y in ['yes'] and (x != 2 or x != 3 or x != 5 or x != 7 or x != 11 or x != 13 or x != 17 or x != 19 or x != 23 or x != 29 or x != 31 or x != 37 or x != 41 or x != 43 or x != 47 or x != 53 or x != 59 or x != 61 or x != 67 or x != 71 or x != 73 or x != 79 or x != 83 or x != 89 or x != 97 or x != 101):  # noqa: E501
        print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again,", name1, end='!')  # noqa: E501
        return
    elif y in ['no'] and (x == 2 or x == 3 or x == 5 or x == 7 or x == 11 or x == 13 or x == 17 or x == 19 or x == 23 or x == 29 or x == 31 or x == 37 or x == 41 or x == 43 or x == 47 or x == 53 or x == 59 or x == 61 or x == 67 or x == 71 or x == 73 or x == 79 or x == 83 or x == 89 or x == 97 or x == 101):  # noqa: E501
        print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again,", name1, end='!')  # noqa: E501
        return
    elif y in ['no'] and (x != 2 or x != 3 or x != 5 or x != 7 or x != 11 or x != 13 or x != 17 or x != 19 or x != 23 or x != 29 or x != 31 or x != 37 or x != 41 or x != 43 or x != 47 or x != 53 or x != 59 or x != 61 or x != 67 or x != 71 or x != 73 or x != 79 or x != 83 or x != 89 or x != 97 or x != 101):  # noqa: E501
        print('Correct!')
    else:
        return
    # третий проход
    x = random.randint(2, 101)
    print('Question:', x)
    y = (input("Your answer:"))
    if y in ['yes'] and (x == 2 or x == 3 or x == 5 or x == 7 or x == 11 or x == 13 or x == 17 or x == 19 or x == 23 or x == 29 or x == 31 or x == 37 or x == 41 or x == 43 or x == 47 or x == 53 or x == 59 or x == 61 or x == 67 or x == 71 or x == 73 or x == 79 or x == 83 or x == 89 or x == 97 or x == 101):  # noqa: E501
        print('Correct!\nCongtatulations,', name1, end='!')
    elif y in ['yes'] and (x != 2 or x != 3 or x != 5 or x != 7 or x != 11 or x != 13 or x != 17 or x != 19 or x != 23 or x != 29 or x != 31 or x != 37 or x != 41 or x != 43 or x != 47 or x != 53 or x != 59 or x != 61 or x != 67 or x != 71 or x != 73 or x != 79 or x != 83 or x != 89 or x != 97 or x != 101):  # noqa: E501
        print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again,", name1, end='!')  # noqa: E501
        return
    elif y in ['no'] and (x == 2 or x == 3 or x == 5 or x == 7 or x == 11 or x == 13 or x == 17 or x == 19 or x == 23 or x == 29 or x == 31 or x == 37 or x == 41 or x == 43 or x == 47 or x == 53 or x == 59 or x == 61 or x == 67 or x == 71 or x == 73 or x == 79 or x == 83 or x == 89 or x == 97 or x == 101):  # noqa: E501
        print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again,", name1, end='!')  # noqa: E501
        return
    elif y in ['no'] and (x != 2 or x != 3 or x != 5 or x != 7 or x != 11 or x != 13 or x != 17 or x != 19 or x != 23 or x != 29 or x != 31 or x != 37 or x != 41 or x != 43 or x != 47 or x != 53 or x != 59 or x != 61 or x != 67 or x != 71 or x != 73 or x != 79 or x != 83 or x != 89 or x != 97 or x != 101):  # noqa: E501
        print('Correct!\nCongratulations,', name1, end='!')
    else:
        return
