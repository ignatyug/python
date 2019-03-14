import sqlite3


def input_year():
    max = 2019
    min = 1900
    while True:
        try:
            year = int(input('Enter year:\t'))
            if min <= year <= max:
                return year
            else:
                print('Year is not in the range')
        except ValueError:
            print('Not valid year!')


def input_square():
    min = 20
    max = 1000
    while True:
        try:
            square = int(input('Enter square:'))
            if min <= square <= max:
                return square
            else:
                print('Square is not in the range')
        except ValueError:
            print('Not valid square!')


def input_district():
    district = input('Enter district:')
    return district


def search(year, square, district):
    cursor = sqlite3.connect('Properties').cursor()
    for row in cursor.execute('''select price
    from properties
    where year = ''' + str(year) + ''' AND square = ''' + str(square) + ''' AND district = \'''' + district + '''\'
    order by price
    limit 1'''):
        print(row[0])
        return
    print('Nay nothing')


def main():
    a = ' '
    while a.casefold() != 'no':
        year = input_year()
        square = input_square()
        district = input_district()
        search(year, square, district)
        a = input('If you want to continue, press enter:   ')
    print('By')


main()
