def dream():
    year = int(input('Enter the year that interests you:   '))

    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print('it\'s usual year')
    else:
        print('This year heralds a lot of interesting')


dream()
