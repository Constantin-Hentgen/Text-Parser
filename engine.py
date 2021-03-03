from random import randint

# utiliser un fichier remplis de français pour pouvoir y faire une analyse de fréquence des lettres
# aussi pouvoir dire quel sont les mots les plus fréquents
# faire l'intégralité du dev en POO
# permettre l'exploration par mot et par phrase
# permettre la lecture par ligne

f = open("hugo_notre_dame_de_paris.txt", "r")
lecture = f.read()
f.close()

def frequency(element):
    element = str(element)
    total = 0
    number = 0
    space = 0

    for letter in lecture:
        total += 1

        if letter == element:
            number += 1

        elif letter == " ":
            space += 1

    return number * 100 / total, space * 100 / total, total / space


# element = input("Enter a character : ")
# print(frequency(element))


def split():
    split = []
    iterator = 0
    iteration = 0

    for a in lecture:
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
            if lecture[iterator:iteration] != "":
                split.append(lecture[iterator:iteration])
            iterator = iteration + 1

        iteration += 1

    return split


# split = split()
split = ["bonsoir", "je", "suis", "bonsoir", "bonjour"]


def ranker():
    rank = []
    count = 0

    for a in range(len(split)):
        for b in range(len(split)):
            if split[b] == split[a]:
                count += 1
        rank.append(count)
        count = 0

    return rank

#faire un top 50 des mots les plus utilisés par hugo

rank = ranker()

# print(split[randint(0,len(split))])
#faire un algo de recherche sous forme de fonction
print(split)
print(rank)

#let's add some comments