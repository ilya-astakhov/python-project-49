#!/usr/bin/env python3


from random import randint
from brain_games.cli import welcome_user


def main():
    # welcome_user()
    even()


if __name__ == '__main__':
    main()


def even():
    name1 = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # первый проход
    x = randint(1, 999)
    print('Question:', x)
    y = (input("Your answer:"))
    if y in ['yes'] and x % 2 == 0:
        print('Correct!')
    elif y in ['yes'] and x % 2 != 0:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again,", name1)  # noqa: E501
        return
    elif y in ['no'] and x % 2 != 0:
        print('Correct!')
    else:
        y in ['no'] and x % 2 == 0
        print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again,", name1)  # noqa: E501
        return
    # второй проход
    x = randint(1, 999)
    print('Question:', x)
    y = (input("Your answer:"))
    if y in ['yes'] and x % 2 == 0:
        print('Correct!')
    elif y in ['yes'] and x % 2 != 0:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again,", name1)  # noqa: E501
        return
    elif y in ['no'] and x % 2 != 0:
        print('Correct!')
    else:
        y in ['no'] and x % 2 == 0
        print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again,", name1)  # noqa: E501
        return
    # третий проход
    x = randint(1, 999)
    print('Question:', x)
    y = (input("Your answer:"))
    if y in ['yes'] and x % 2 == 0:
        print('Correct!\nCongratulations,', name1, end='!')
	# print(f'Correct!\nCongratulations, {name1}!')
    elif y in ['yes'] and x % 2 != 0:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again,", name1)  # noqa: E501
        return
    elif y in ['no'] and x % 2 != 0:
        # print(f'Correct!'\n'Congratulations, {name1}!')
        print('Correct!\nCongratulations,', name1, end='!')
    else:
        y in ['no'] and x % 2 == 0
        print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again,", name1)  # noqa: E501
        return
