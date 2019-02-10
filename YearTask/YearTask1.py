def dream():
    year = int(input('Enter the year that interests you:   '))
    if year % 4 != 0:
        print('it\'s usual year')
    elif year % 100 == 0:
        if year % 400 == 0:
            print('it\'s intercalary year')
        else:
            print('it\'s usual year')
    else:
        print('it\'s intercalary year')


dream()
