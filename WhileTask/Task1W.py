def dream():
    a = 0
    c = int(input('Enter the number:   '))
    b = 100
    while a < b:
        a += c
        if c <= 0:
            return
        print(a)

    print('Stop:')


dream()
