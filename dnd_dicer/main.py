#!/usr/bin/env python
import random

doing = (2, 4, 6, 8, 10, 12, 20, 100)
done = False
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen

while not done:
    print('DND dicer')
    print('Possible dice is 2, 4, 6, 8, 10, 12, 20, 100')
    print('Choose your dice in xdx format 4d6 for example')

    what = 0
    amount = 0
    while what not in doing:
        dices = input("Dices: ")
        if not dices.find('d'):
            print('something wrong')
            continue
        arr = dices.split('d')
        if len(arr) != 2:
            print('something wrong')
            continue
        try:
            what = abs(int(arr[1]))
            amount = abs(int(arr[0]))
        except ValueError:
            print('something wrong')

    fins = []
    for i in range(amount):
        fins.append(random.randint(1, int(what)))
        print(fins[i], end=' | ')
    print("Sum = ", sum(fins))
    if input('Press \'y\' for repeat: ') != 'y':
        done = True
    cls()
