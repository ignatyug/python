def dream():
    print('User remember, if you want to stop the search, enter the \"stop\" ''command', '\n')
    lines = open('C:\\Users\\Yurgen\\Desktop\\database.txt').readlines()
    name = ''
    while name != 'stop':
        name = input('Enter your username from your directory reference:   ')
        result = ''
        for i in lines:
            i = i.split(';')
            if name == i[1]:
                result = i[2]
                break
        if result == '':
            print('You entered an invalid parameter, try again')
        else:
            print(result)
        name = input('If you want to continue, press enter:   ')


dream()
