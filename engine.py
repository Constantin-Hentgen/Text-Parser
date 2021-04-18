from random import randint

#lecture du fichier texte pour effectuer le traitement
f = open("en.txt", "r", encoding="utf-8") #ouverture du document
original = f.read() #assignement à une variable du contenu du document
f.close() #fermeture du document

alphabet = "abcdefghijklmnopqrstuvwxyzçêèàéâûîùôœæï" #définition de l'alphabet pour effectuer les tests
special = " .,/\n\\*%&;?(! )–*“”…’'`:»«0123456789" #définition des caractères spéciaux pour effectuer des tests

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

def split(document): #sépare le textes en petites unités que nous allons analyser
    split = [] #liste résultat contenant les unités séparées
    iterator = 0 #correspond au suivi des unitésmi
    iteration = 0 #correspond au suivi des caractères
    document = document.replace("-\n", '') #suppresion des \n de passage à la ligne et des - de jonction

    for caracter in document: #pour chaque caractère du document
        if caracter in special: #si le caractère du document est un caractère spécial
            split.append(document[iterator:iteration].lower()) #ajouter à split l'unité déterminée
            iterator = iteration + 1 #évolue d'unité en unité
        if iteration > 1 and split[-1] == '': #supprime les éléments vides
            del split[-1]
        iteration += 1 # évolue caractère par caractère
                
    return split

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

def doublon(liste_rank, real_liste): #supprime les doublons
    liste_propre = []
    rank_propre = []

    liste_propre.append(real_liste[0])
    rank_propre.append(liste_rank[0])

    for a in range(len(real_liste) - 1):
        if real_liste[a + 1] not in liste_propre:
            liste_propre.append(real_liste[a + 1])
            rank_propre.append(liste_rank[a + 1])

    return rank_propre, liste_propre

def algotri(liste_rank, real_liste): #trie la liste des unités en fonction de leur fréquence
    for a in range(len(liste_rank)):
        maximum = 0
        rank = 0
        for b in range(len(liste_rank) - a):
            if liste_rank[b] >= maximum:
                maximum = liste_rank[b]
                rank = b
        liste_rank[rank], liste_rank[len(liste_rank) - a - 1] = (liste_rank[len(liste_rank) - a - 1], liste_rank[rank])
        real_liste[rank], real_liste[len(real_liste) - a - 1] = (real_liste[len(real_liste) - a - 1], real_liste[rank])

    return liste_rank, real_liste

#print(frequency(original)) 
#print(split(original)) #partage du document en unités
#print(gatherer(split(original))) #rassemblement des unités semblables
#print(ranker(gatherer(split(original)))) #production des classements sur victor hugo de la liste rassemblée

#print(algotri(doublon(ranker(gatherer(split(original))),gatherer(split(original)))[0],doublon(ranker(gatherer(split(original))),gatherer(split(original)))[1]))
#concaténation des applications de toutes les fonctions

#print(algotri(frequency(original), list(alphabet))) #fréquence des lettres

liste = algotri(doublon(ranker(gatherer(split(original))),gatherer(split(original)))[0],doublon(ranker(gatherer(split(original))),gatherer(split(original)))[1])[1] #liste propre des mots sans doublons
rang = algotri(doublon(ranker(gatherer(split(original))),gatherer(split(original)))[0],doublon(ranker(gatherer(split(original))),gatherer(split(original)))[1])[0] #liste propre des occurences sans doublons

print("***************************************************************")

print("mot aléatoire :", liste[randint(0, len(liste)-1)]) #affichage d'un mot aléatoire avec equiprobabilité

liste_lettre = algotri(frequency(original), list(alphabet))[1] # liste triée dans l'ordre décroissant d'occurences des lettres de l'alphabet
lettre_rang = algotri(frequency(original), list(alphabet))[0] # liste triée dans l'ordre décroissant d'occurences des fréquences des lettres de l'alphabet

print("***************************************************************")

for a in range(10): #affichage du top 10 des lettres fréquentes
    print(a + 1,liste_lettre[-a-1],lettre_rang[-a-1],"% ")

print("***************************************************************")

for a in range(10): #affichage du top 10 des mots fréquents
    print(a + 1,liste[-a-1],rang[-a-1]*100/len(rang),"% ")

print("***************************************************************")