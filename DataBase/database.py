def dream():
    database = {'Petr Petrov': 'petr@gmail,com', 'John Smith': '+380-67234-55-55', 'Sasha Ivanov': 'ivanov@gmail.com'}
    print('User remember, if you want to stop the search, enter the \"stop\" ''command', '\n')
    name = 0
    while name != 'stop':
        name = input('Enter your username from your directory reference:   ')
        if name in database:
            print(database.get(name))
        else:
            print('You entered an invalid parameter, try again')
        name = input('If you want to continue, press enter:   ')


dream()
