def sum():
    a = int(input('Enter the first number:   '))
    c = int(input('Enter the second number:   '))
    b = 100
    while a <= b:
        a = a + c
        if a == b:
            continue
        print(a)
    else:
        print('Stop:')


sum()
