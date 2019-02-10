import random


def dream():
    s = str(random.randint(100, 999))
    print('Randomly generated three digit number:   ', s)
    sum = 0
    for i in s:
        sum += int(i)
    print('SUM:    ', sum)


dream()
