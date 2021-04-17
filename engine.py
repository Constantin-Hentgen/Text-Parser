from random import randint
#je sais pas si changer le nom d'un repo pose problème…
#lecture du fichier texte pour effectuer le traitement
f = open("fr.txt", "r", encoding="utf-8") #ouverture du document
lecture = f.read() #assignement à une variable du contenu du document
f.close() #fermeture du document

original = lecture
alphabet = "abcdefghijklmnopqrstuvwxyzçêèàéâûîùôœæï" #définition de l'alphabet pour effectuer les tests
special = " .,\n/\\*%&;?(! )–*“”…’'`:»«-0123456789" #définition des caractères spéciaux pour effectuer des tests

def frequency(original): #renvoi la fréquence pour chaque caractère
    ranking = [] #liste vide pour contenir les fréquences
    total = 0
    number = 0

    for letter in original: #boucle pour compter le nombre total de caractères non vides dans le document
        if letter in alphabet: #comptabilisation du nombre de caractères non spéciaux
            total += 1

    for letter in alphabet: #pour chaque lettre de l'alphabet
        for element in original: #pour chaque lettre du document
            if element == letter:
                number += 1 #incrémenter pour la stat de la lettre par occurence

        if number != 0: #si la lettre est apparue au moins une fois
            number = number * 100 / total #calcul de la fréquence
            ranking.append(number)
        number = 0 #réinitialisation de number pour pas qu'une lettre hérite les statistiques d'une autre

    return ranking #ranking est selon l'ordre alphabétique

#print(frequency(original)) #test sur l'extrait de victor hugo

def split(document): #sépare le textes en petites unités que nous allons analyser
    split = [] #liste résultat contenant les unités séparées
    iterator = 0 #correspond au suivi des unités
    iteration = 0 #correspond au suivi des caractères

    for caracter in document: #pour chaque caractère du document
        if caracter in special: #si le caractère du document est un caractère spécial
            split.append(document[iterator:iteration].lower()) #ajouter à split l'unité déterminée
            iterator = iteration + 1 #évolue d'unité en unité

        if iteration > 1 and split[-1] == '': #supprime les éléments vides
            del split[-1]

        iteration += 1 # évolue caractère par caractère

    return split

#print(split(original)) #test sur l'extrait de victor hugo

def gatherer(liste): #rassemble les unités égales
    gathered = []

    while len(liste) > 0:
        gathered.append(liste[0])
        del liste[0]
        for element in liste:
            if element == gathered[-1]:
                gathered.append(element)
                liste.remove(element)

    return gathered

#print(gatherer(split(original))) #test de rassemblement sur victor hugo

def ranker(liste): #compte le nombre d'éléments par unités
    rank = []
    count = 0

    for a in range(len(liste)):
        for b in range(len(liste)):
            if liste[b] == liste[a]:
                count += 1
        rank.append(count)
        count = 0

    return rank

#print(ranker(gatherer(split(original)))) #production des classements sur victor hugo

gatherer_test = gatherer(split(original))
rang_test = ranker(gatherer(split(original)))

#print(gatherer_test)
#print(rang_test)

def doublon(liste_rank, real_liste): #supprime les doublons
    liste_propre = []
    rank_propre = []

    liste_propre.append(real_liste[0])
    rank_propre.append(liste_rank[0])

    for a in range(len(liste_rank) - 1):
        if real_liste[a + 1] != real_liste[a]:
            liste_propre.append(real_liste[a + 1])
            rank_propre.append(liste_rank[a + 1])

    return rank_propre, liste_propre

doublon_rank_test = doublon(rang_test,gatherer_test)[0]
doublon_liste_test = doublon(rang_test,gatherer_test)[1]

#print(doublon_liste_test)
#print(doublon_rank_test)

def algotri(liste_rank, real_liste): #trie la liste des unités en fonction de leur fréquence
    for a in range(len(liste_rank)):
        maximum = 0
        rank = 0
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

#print(algotri(doublon_rank_test,doublon_liste_test))

#lecture = split(lecture)
#universe = len(lecture)
#liste = gatherer(lecture)
#print(liste)

#rank = ranker(liste)
#print(rank)
#liste = doublon(rank, liste)
#liste = algotri(liste[0], liste[1])
#sommeA = 0
#sommeB = 0
#ranking = frequency(original)
#ranking = algotri(ranking[0], ranking[1])

#for a in range(len(ranking[0])):
#    print(
#        "\t\t\t\t\t\t\t",
#        a + 1,
#        "\t",
#        ranking[1][len(ranking[0]) - 1 - a],
#        "\t",
#        ranking[0][len(ranking[0]) - 1 - a],
#        "% ",
#    )

#for a in range(30):
#    prop = 100 * liste[0][len(liste[1]) - 1 - a] / universe
#    sommeA += prop
#    sommeB += liste[0][len(liste[1]) - 1 - a]
#
#    if len(liste[1][len(liste[1]) - 1 - a]) >= 6:
#        print(
#            "\t\t\t\t\t\t",
#            a + 1,
#            "\t",
#            liste[1][len(liste[1]) - 1 - a],
#            "\t",
#            liste[0][len(liste[1]) - 1 - a],
#            "\t",
#            int(1000 * prop) / 1000,
#            "% ",
#        )

#    else:
#        print(
#            "\t\t\t\t\t\t",
#            a + 1,
#            "\t",
#            liste[1][len(liste[1]) - 1 - a],
#            "\t\t",
#            liste[0][len(liste[1]) - 1 - a],
#            "\t",
#            int(1000 * prop) / 1000,
#            "% ",
#        )

#print("\n\t\t\t\t\t\t\t\t\t", sommeB, "\t", int(1000 * sommeA) / 1000, "% ")
#print("\n\t\t\t\t\t\t\t mot aléatoire :", liste[1][randint(0, len(liste[1]))])