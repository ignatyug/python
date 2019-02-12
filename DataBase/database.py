def dream():
    database = {'Petr Petrov': 'petr@gmail,com', 'John Smith': '+380-67234-55-55', 'Sasha Ivanov': 'ivanov@gmail.com'}
    print('Before you start searching for a contact, you should know', '\n',
          'that after the \"Stop\" ''command, you will complete the following contacts.', '\n')
    while True:
        name = input('Enter your username from your directory reference:   ')
        if name == 'Stop':
            print('I found what I was looking for.')
            break
        if name in database:
            print(database.get(name))
        else:
            print('NOT FOUND')
            break


dream()
