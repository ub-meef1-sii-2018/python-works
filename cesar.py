
def cesar(phrase, key):
    minMajuscule = ord('A')
    minMinuscule = ord('a')
    returns = ''
    for char in phrase:
        if ord(char) >= minMinuscule:
            startingPoint = minMinuscule
        else:
            startingPoint = minMajuscule
        newChar = startingPoint + (((ord(char) - startingPoint) + key)%26)
        returns += chr(newChar)
    return returns


def legionnaire(code, key):
    return cesar(code, -1 * key)

a = input('Entrez une phrase\n')
b = int(input('Entrez la clef (nombre)\n')) % 26
print(cesar(a, b))
