import random


def dream():
    randomness = [(random.randint(0, 9)) for r in range(15)]
    print('Randomly generated list number:   ', randomness, '\n')
    s = 0
    q = 0
    for j in randomness:
        b = randomness.count(j)
        if b > q:
            q = b
            s = j
    print('Most often the number is repeated in the list:   ', s)


dream()
