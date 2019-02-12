def dream():
    database = {'Petr Petrov': 'petr@gmail,com', 'John Smith': '+380-67234-55-55', 'Sasha Ivanov': 'ivanov@gmail.com'}
    while True:
        name = input('Enter your username from your directory reference:   ')
        if name in database:
            print(database.get(name))
        else:
            print('NOT FOUND')
            break


dream()
