import random

def generateRandomPassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def capitalizeRandomly(char: str):
        if bool(random.getrandbits(1)):
            char = char.capitalize()

        return char

    numLetters= random.randint(6, 10)
    numSymbols = random.randint(2,6)
    numNumbers = random.randint(4,6)


    sizeOfLetters = len(letters)
    sizeOfNumber = len(numbers)
    sizeOfSymbols = len(symbols)

    passwordChars = []
    for i in range(numLetters):
        letter = capitalizeRandomly(letters[random.randint(0,sizeOfLetters - 1)])
        passwordChars.append(letter)
    for i in range(numSymbols):
        passwordChars.append(symbols[random.randint(0,sizeOfSymbols - 1)])
    for i in range(numNumbers):
        passwordChars.append(numbers[random.randint(0, sizeOfNumber - 1)])

    password = ""
    while len(passwordChars) != 0:
        rand = random.randint(0, len(passwordChars) - 1)
        password += passwordChars[rand]
        passwordChars.pop(rand)


    return password


