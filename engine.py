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


def sorter(liste_rank,real_liste):
    for a in range(len(liste_rank)):
        for b in range(len(liste_rank)):
            if liste_rank[b] < liste_rank[a]:
                liste_rank[a],liste_rank[b] = liste_rank[b],liste_rank[a]
                real_liste[a],real_liste[b] = real_liste[b],real_liste[a]

    a = 0
    b = 1
        
    while real_liste[a] == real_liste[b]:
        del real_liste[b]
        del liste_rank[b]

        if real_liste[a] != real_liste[b]:
            a += 1
            b += 1
    
    return real_liste,liste_rank


split = ["bonsoir", "je", "suis", "bonsoir", "bonjour","bonsoir","bonsoir", "suis", "bonsoir", "suis", "bonsoir"]
rank = ranker(split)
world = sorter(rank,split)
resultat = 0

for a in range(len(world[1])):
    resultat += world[1][a]

for a in range(len(world[1])-1):
    prop = 100*world[1][a]/resultat
    print(prop," : ", world[0][a])

# print(split[randint(0,len(split))])

# faire un top 50 des mots les plus utilisés par hugo : donner le proportions
# faire une fonction pour clean le nombre d'occurences
# faire une fonction qui permet de trouver un mot en fonction de caractéristiques
# permettre l'exploration par mot et par phrase
# permettre la lecture par ligne