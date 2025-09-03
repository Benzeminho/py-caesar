def caesar_cipher():
    texte = input("Texte à chiffrer : ").lower()
    decalage = int(input("Décalage : "))
    resultat = ""

    for c in texte:
        if c.isalpha():
            resultat += chr((ord(c) - ord('a') + decalage) % 26 + ord('a'))
        else:
            resultat += c

    print("Texte chiffré :", resultat)

caesar_cipher()

# ord pour obtenir le code ASCII d'un caractère
# chr pour convertir le code en lettre

def caesar_decipher():
    texte = input("Texte à déchiffrer : ").lower()
    decalage = int(input("Décalage : "))
    resultat = ""

    for c in texte:
        if c.isalpha():
            resultat += chr((ord(c) - ord('a') - decalage) % 26 + ord('a')) # j'ai juste remplacé le + par un -
        else:
            resultat += c

    print("Texte déchiffré :", resultat)

caesar_decipher()