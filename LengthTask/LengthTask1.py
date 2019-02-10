def dream():
    s = input('ready to continue the dialogue:   ')
    listWords = s.split()
    idLongestWord = 0
    for i in range(1, len(listWords)):
        if len(listWords[idLongestWord]) < len(listWords[i]):
            idLongestWord = i
    print(listWords[idLongestWord])


dream()
