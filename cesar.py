
# "def" permet de définir une fonction, et donc de délimiter tout un pan de code qui fait un truc.
def cesar(phrase, key): # on définit deux arguments : une phrase (ce qu'on va "chiffrer") et une clef (le décalage qu'on applique)
    minMajuscule = ord('A') # ce code définit le point de départ de la plage ASCII A-Z
    minMinuscule = ord('a') # ce code définit le point de départ de la plage ASCII a-z
    returns = '' # ça, ça va être notre résultat final !
    for char in phrase: # pour chaque caractère dans notre phrase
        if ord(char) >= minMinuscule: # si la valeur ASCII est plus loin que du minuscule : BOUM on est en minuscule
            startingPoint = minMinuscule # on dit qu'on "démarre" de ce caractère
        else: # sinon on considère qu'on est en majuscule
            startingPoint = minMajuscule
        newChar = startingPoint + (((ord(char) - startingPoint) + key)%26) # on prend donc la différence de position entre le caractère et le démarrage qu'on a choisi.
        # ça signifie que si on a "D", on a 3 de différence avec "A" (D-A = 3).
        # le modulo (%) 26 sert à "revenir" au début si on dépasse de 26 caractères le premier caractère de la plage A-Z ou a-z
        returns += chr(newChar) # on concatène (ce terme est important) le caractère qui correspond à notre résultat
    return returns
# notez bien qu'ici, on est revenus au début de la ligne. Cela signifie à python qu'on a fini notre fonction !

# ouais j'ai fait ça vite fait pour montrer qu'on peut appeller une fonction dans une fonction.
def legionnaire(code, key):
    return cesar(code, -1 * key)

# \n sert à faire un saut de ligne. Plus propre.
a = input('Entrez une phrase\n')
b = int(input('Entrez la clef (nombre)\n')) % 26
print(cesar(a, b))
