def dream():
    a = 0
    c = int(input('Enter:   '))
    b = 100
    while a < b:
        a += c
        if c <= 0:
            return
        print(a)


dream()
