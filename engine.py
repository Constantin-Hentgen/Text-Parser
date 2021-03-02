#utiliser un fichier remplis de français pour pouvoir y faire une analyse de fréquence des lettres
#aussi pouvoir dire quel sont les mots les plus fréquents
#faire l'intégralité du dev en POO
#permettre l'exploration par mot et par phrase
#permettre la lecture par ligne

f = open('hugo_notre_dame_de_paris.txt','r')
lecture = f.read()
f.close()

#si il y a un espace c'est un nouveau mot je lis, dès que c'est un espace j'ajoute les caractères

#faire une fonction pour afficher un arrondi super propre à lire

#variable = 0.12345
#variable = str(variable) faire attention puisque le point est considéré comme un caratère
#print(variable[3])

def arrondi(number):
    number = str(number)
    product = ""
    iteration = 0
    test = 0

    while iteration < 2:
        if number[test] != "0" and number[test] != ".":
            iteration += 1

        product += number[test]
        test += 1

    return product,iteration,test

print("fonction arrondi pour number = 0.0000000323123456 : ", arrondi(0.000000032312346))

#il va de chiffre en chiffre, il lui faut 3 chiffres non nuls . compris




def frequency(element):
    element = str(element)
    total = 0
    number = 0

    for letter in lecture:
        total += 1

        if letter == element:
            number += 1
    
    return number*100/total, "%"

#element = input("Enter a character : ")
#print(frequency(element))