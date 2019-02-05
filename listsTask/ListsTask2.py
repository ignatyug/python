def dream():
    c = int(input('Если Вы хотите узнать какой элемент содержится в  ячейки '
                  'введите номер ячейки от 0 до 4:   '))
    numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    row = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z'}

    donut = [1, 5, 'a', '?', '+']
    begin = 0
    for el in donut:
        begin += 1
        if el in numbers != c:
            print(begin, 'it\'s number:   ', el)
        elif el in row != c:
            print(begin, 'it\'s row:      ', el)
        else:
            print(begin, 'it\'s unknown element!')


dream()
