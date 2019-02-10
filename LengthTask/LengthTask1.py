def dream():
    phrase = list(input('ready to continue the dialogue:   ').split())
    result = phrase[0]
    for element in phrase:
        if len(element) > len(result):
            result = element
    print('\n', 'The longest of its own conclusions:    ', result)


dream()
