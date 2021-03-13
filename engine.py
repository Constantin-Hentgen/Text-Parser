from random import randint

f = open("hugo_notre_dame_de_paris.txt", "r", encoding="utf-8")
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
            or a == "/"
            or a == "\\"
            or a == "*"
            or a == "%"
            or a == "&"
            or a == " "
            or a == ";"
            or a == "!"
            or a == "?"
            or a == ""
            or a == ""
            or a == "("
            or a == ")"
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
            or a == "\x0c"
        ):
            if document[iterator:iteration] != "":
                split.append(document[iterator:iteration].lower())
            iterator = iteration + 1

        iteration += 1

    return split


# imaginer une manière de fix le problème des mots cut avec un tiret et passage à la ligne


def gatherer(liste):
    gathered = []

    while len(liste) > 0:
        gathered.append(liste[0])
        del liste[0]
        for element in liste:
            if element == gathered[-1]:
                gathered.append(element)
                liste.remove(element)

    return gathered


def ranker(
    liste,
):  # renvoie une liste complémentaire qui remplace chaque mot par son nombre d'occurences
    rank = []
    count = 0

    for a in range(len(liste)):
        for b in range(len(liste)):
            if liste[b] == liste[a]:
                count += 1
        rank.append(count)
        count = 0

    return rank


def doublon(liste_rank, real_liste):
    liste_propre = []
    rank_propre = []

    liste_propre.append(real_liste[0])
    rank_propre.append(liste_rank[0])

    for a in range(len(liste_rank) - 1):
        if real_liste[a + 1] != real_liste[a]:
            liste_propre.append(real_liste[a + 1])
            rank_propre.append(liste_rank[a + 1])

    return rank_propre, liste_propre


def algotri(liste_rank, real_liste):
    for a in range(len(liste_rank)):
        maximum = 0
        rank = 0
        # tri des valeurs numériques tout en conservant le lien avec les mots
        for b in range(len(liste_rank) - a):
            if liste_rank[b] >= maximum:
                maximum = liste_rank[b]
                rank = b
        liste_rank[rank], liste_rank[len(liste_rank) - a - 1] = (
            liste_rank[len(liste_rank) - a - 1],
            liste_rank[rank],
        )
        real_liste[rank], real_liste[len(liste_rank) - a - 1] = (
            real_liste[len(liste_rank) - a - 1],
            real_liste[rank],
        )

    return liste_rank, real_liste



alphabet = "abcdefghijklmnopqrstuvwxyzçêèéâûùôœï"







lecture = split(lecture)  # split validé
universe = len(lecture)
liste = gatherer(lecture)  # gatherer validé à 99% mais il regroupe 2 de à la fin

for a in range(3):
    liste = gatherer(liste)

rank = ranker(liste)  # ranker validé
liste = doublon(rank, liste)  # doublon validé
liste = algotri(liste[0], liste[1])
sommeA = 0
sommeB = 0

for a in range(5000):
    prop = 100 * liste[0][len(liste[1]) - 1 - a] / universe
    sommeA += prop
    sommeB += liste[0][len(liste[1]) - 1 - a]
    if len(liste[1][len(liste[1]) - 1 - a]) >= 6:
        print("\t\t\t\t\t\t",a+1,"\t",
        liste[1][len(liste[1]) - 1 - a],
       "\t", liste[0][len(liste[1]) - 1 - a],"\t",
        int(1000 * prop) / 1000 ,"% ")
    else:
        print("\t\t\t\t\t\t",a+1,"\t",
        liste[1][len(liste[1]) - 1 - a],
        "\t\t", liste[0][len(liste[1]) - 1 - a],"\t",
        int(1000 * prop) / 1000 ,"% "
        )

print("\n\t\t\t\t\t\t\t\t\t",sommeB,"\t",int(1000 * sommeA) / 1000 ,"% ")

# print(frequency("e",lecture))

# print(split[randint(0,len(split))])


# trouver un mot en fonction de caractéristiques
# exploration par mot et par phrase
# prendre en compte la morphologie des mains et les dimensions ains que le type du clavier
# faire les exports de données : le traitement statistique : sur un document txt ou csv
# faire une analyse de la taille du fichier pour s'assurer que c'est raisonnablement executable
