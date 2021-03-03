from random import randint

f = open("hugo_notre_dame_de_paris.txt", "r")
lecture = f.read()
f.close()


def frequency(character, document):
    total = 0
    number = 0

    for letter in document:
        total += 1

        if letter == character:
            number += 1

    return number * 100 / total


# print(frequency("e",lecture))


def split(document):
    split = []
    iterator = 0
    iteration = 0

    for a in document:
        if (
            a == " "
            or a == "."
            or a == ","
            or a == "\n"
            or a == " "
            or a == ""
            or a == "–"
            or a == "…"
            or a == "’"
            or a == ":"
            or a == "»"
            or a == "«"
            or a == "-"
            or a == "0"
            or a == "1"
            or a == "2"
            or a == "3"
            or a == "4"
            or a == "5"
            or a == "6"
            or a == "7"
            or a == "8"
            or a == "9"
        ):
            if document[iterator:iteration] != "":
                split.append(document[iterator:iteration])
            iterator = iteration + 1

        iteration += 1

    return split


# print(split(lecture))


def ranker(liste):
    rank = []
    count = 0

    for a in range(len(liste)):
        for b in range(len(liste)):
            if liste[b] == liste[a]:
                count += 1
        rank.append(count)
        count = 0

    return rank


def merger(liste_A, liste_B):

    for a in range(len(liste_A)):
        liste_A[a] += "_" + str(liste_B[a])

    return liste_A


def sorter(liste):
    for a in range(len(liste)):
        temp = liste[a]
        for b in range(len(liste)):
            if str(liste[b]) == str(liste[a]):
                a = 5
    return liste


split = ["bonsoir", "je", "suis", "bonsoir", "bonjour"]
rank = ranker(split)
# print(split)
# print(rank)

# merged = merger(split, rank)
# print(sorter(merged))


# faire une fonction pour clean le nombre d'occurences
# faire une fonction qui permet de trouver un mot en fonction de caractéristiques
# telle que la longueur ou encore les lettres qui le compose

# faire un top 50 des mots les plus utilisés par hugo
# print(split[randint(0,len(split))])
# je peux merge les deux puis les classer et supprimer les doublons

# utiliser un fichier remplis de français pour pouvoir y faire une analyse de fréquence des lettres
# aussi pouvoir dire quel sont les mots les plus fréquents
# permettre l'exploration par mot et par phrase
# permettre la lecture par ligne
