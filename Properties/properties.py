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
    square = int(input('Enter square:'))
    return square


def input_district():
    district = input('Enter district:')
    return district


def search(year, square, district):
    print(year, square, district)


year = input_year()
square = input_square()
district = input_district()
search(year, square, district)
