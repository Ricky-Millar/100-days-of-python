def encrypt(word, num, alphabet):
    textList = []
    encryptMsg = ""
    j = 0
    cypherPos = 0
    for i in word:  # convert text to a list
        textList.append(i)
    for i in textList:
        cypherPos = alphabet.index(i) + num
        print(cypherPos)
        if cypherPos > 25: #this checks if a number over 25 is trying to be retreived from the alphabet and reverts to 'a'
            cypherPos -= 26
        print(cypherPos)
        textList[int(j)] = alphabet[cypherPos]         # change each letter in textList with a letter shifted down from alphabet, i = letter in tex. j = itteration of loop
        encryptMsg += str(textList[j])   # convert list to string
        j += 1
    print(textList)
    print(f"The encrypted message is: {encryptMsg}")
