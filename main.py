def caesar_cipher():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    chaine = input("Que voulez-vous chiffrer ? ").lower()
    décalage = int(input("Décalage ? "))
    resultat = ""
    for lettre in chaine:
        if lettre in alphabet:
            index = (alphabet.index(lettre) + décalage) % len(alphabet)
            resultat += alphabet[index]
        else:
            resultat += lettre
    print("Texte chiffré :", resultat)

caesar_cipher()