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