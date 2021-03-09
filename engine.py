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


#print(frequency("e",lecture))


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
            or a == "!"
            or a == "?"
            or a == ""
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
                split.append(document[iterator:iteration])
            iterator = iteration + 1

        iteration += 1

    return split



def ranker(liste): #renvoie une liste complémentaire qui remplace chaque mot par son nombre d'occurences
    rank = []
    count = 0

    for a in range(len(liste)):
        for b in range(len(liste)):
            if liste[b] == liste[a]:
                count += 1
        rank.append(count)
        count = 0

    return rank


def gatherer(liste_rank,real_liste):
    gathered = []
    gathered_rank = []
    
    while len(real_liste) > 0:
        gathered.append(real_liste[0])
        gathered_rank.append(liste_rank[0])
        del real_liste[0]
        del liste_rank[0]
        for element in real_liste:
            if element == gathered[-1]:
                gathered.append(element)
                gathered_rank.append(liste_rank[real_liste.index(element)])                
                liste_rank.remove(liste_rank[real_liste.index(element)])
                real_liste.remove(element)
                
    return gathered_rank, gathered



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
        for b in range(len(liste_rank) - a):  # tri des valeurs numériques tout en conservant le lien avec les mots
            if liste_rank[b] >= maximum:
                maximum = liste_rank[b]
                rank = b
        liste_rank[rank], liste_rank[len(liste_rank) - a - 1] = liste_rank[len(liste_rank) - a - 1], liste_rank[rank]
        real_liste[rank], real_liste[len(liste_rank) - a - 1] = real_liste[len(liste_rank) - a - 1], real_liste[rank]

    return liste_rank, real_liste




#print(split(lecture))

lecture = split(lecture)   #stock de lecture dans une liste

rank = ranker(lecture)     #crée une liste tierce qui remplace les mots par leur occurence

ring = gatherer(rank,lecture)   # regroupe par chaîne de caractères, ça fonctionne jusqu'ici _apparemment_

doublon = doublon(ring[0],ring[1]) #je sais pas encore mais ça à l'air ok avant toute execution de tri

rank = doublon[0]
lecture = doublon[1]
#tri = algotri(rank,lecture) 
print(lecture)

#commentaire de test pour montrer à Gauthier

#counter = 0
#for element in doublon:
#    if element == "à":
#        counter += 1
#print(counter)

#truc bizarre avec deux "de" random à la fin qui n'ont pas été regroupés
#print(ring[1])
#print(doublon[1])



#test = ["a","b","b","c","c","c","c"]
#rank = [1,2,2,3,3,3,3]
#print(doublon(rank,test))




# for a in range(50):
#   prop = 100 * world2[0][a] / universe
#   print(int(1000*prop)/1000, "% : ",world2[1][a], " : ", world2[0][a] )

# print(split[randint(0,len(split))])


# trouver un mot en fonction de caractéristiques
# exploration par mot et par phrase
# prendre en compte la morphologie des mains et les dimensions ains que le type du clavier
# faire les exports de données : le traitement statistique : sur un document txt ou csv
