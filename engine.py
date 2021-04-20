from random import randint

print("***************************************************************")
path = input("Entrer le nom du fichier sans extension : ") + ".txt"
#lecture du fichier texte pour effectuer le traitement
f = open(path, "r", encoding="utf-8") #ouverture du document
original = f.read() #assignement à une variable du contenu du document
f.close() #fermeture du document

alphabet = "abcdefghijklmnopqrstuvwxyzçêèàéâûîùôœæï" #définition de l'alphabet pour effectuer les tests
voyelles = "aeiouyàâéèêiïîôùû"
consonnes = "bcdfghjklmnpqrstvwxzç"
accents = "àâéèêiïîôùûëäü"
special = " .,/\n\\*%&;?€•(! )–*“”…’'`:»«0123456789" #définition des caractères spéciaux pour effectuer des tests

#kara = int(input("Entre 1 si tu veux étudier la fréquence des caractères spéciaux sinon 0 : "))
#
#if kara == 1:
#    alphabet,special = special,alphabet

compteur_points = 0

for character in original: #compteur de points pour connaître le nombre de phrase moyen
    if character == ".":
        compteur_points += 1

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

        number = number * 100 / total #calcul de la fréquence
        ranking.append(number)

        number = 0 #réinitialisation de number pour pas qu'une lettre hérite les statistiques d'une autre

    return ranking #ranking des fréquences selon l'ordre alphabétique

def split(document): #sépare le textes en petites unités que nous allons analyser
    split = [] #liste résultat contenant les unités séparées
    iterator = 0 #correspond au suivi des unités
    iteration = 0 #correspond au suivi des caractères
    document = document.replace("-\n", '') #suppresion des \n de passage à la ligne et des - de jonction

    for caracter in document: #pour chaque caractère du document
        if caracter in special: #si le caractère du document est un caractère spécial
            split.append(document[iterator:iteration].lower()) #ajouter à split l'unité déterminée
            iterator = iteration + 1 #évolue d'unité en unité

        iteration += 1 # évolue caractère par caractère
    
    while("" in split) : #supprime les éléments vides
        split.remove("")
                
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

def vowel(document):
    compteur_voyelles = 0
    compteur_consonnes = 0
    lettres_francais_accents = 0

    for character in document:
        if character in voyelles:
            compteur_voyelles += 1

        if character in consonnes:
            compteur_consonnes += 1
        
        if character in accents:
            lettres_francais_accents += 1
  
    return compteur_voyelles, compteur_consonnes, compteur_consonnes+compteur_voyelles,lettres_francais_accents


#print(vowel(original)[0]/vowel(original)[2])

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

compteur_lettres = 0

for element in split(original):
    compteur_lettres += len(element)

liste = algotri(doublon(ranker(gatherer(split(original))),gatherer(split(original)))[0],doublon(ranker(gatherer(split(original))),gatherer(split(original)))[1])[1] #liste propre des mots sans doublons
rang = algotri(doublon(ranker(gatherer(split(original))),gatherer(split(original)))[0],doublon(ranker(gatherer(split(original))),gatherer(split(original)))[1])[0] #liste propre des occurences sans doublons

#print("***************************************************************")
#
#print("ratio de voyelles : ", int(1000000*vowel(original)[0]/vowel(original)[2])/10000,"%")
#print("ratio de consonnes : ", int(1000000*vowel(original)[1]/vowel(original)[2])/10000,"%")
#print("ratio de lettres accentuées françaises : ",int(1000000*vowel(original)[3]/vowel(original)[2])/10000,"%")
#print("nombre de mots moyen par phrase : ",int(10000*len(split(original))/compteur_points)/10000)
#print("nombre de lettres moyen par mot : ", int(10000*compteur_lettres/len(split(original)))/10000)
#print("quotient de mots différents sur le total : ", int(10000*len(liste)/len(split(original)))/10000)
#print("SCORE FINAL (clareté et élégance) : ",int((10**8/len(split(original))/compteur_points)*(len(liste)/len(split(original)))**2))
#
#print("***************************************************************")
#
#print("mot aléatoire en situation d'équiprobabilité :", liste[randint(0, len(liste)-1)]) #affichage d'un mot aléatoire avec equiprobabilité

liste_lettre = algotri(frequency(original), list(alphabet))[1] # liste triée dans l'ordre décroissant d'occurences des lettres de l'alphabet
lettre_rang = algotri(frequency(original), list(alphabet))[0] # liste triée dans l'ordre décroissant d'occurences des fréquences des lettres de l'alphabet

print(liste_lettre)
print(lettre_rang)

print("***************************************************************")
cumul = 0
for a in range(15): #affichage du top 10 des lettres fréquentes
    cumul += lettre_rang[-a-1]
    print(a + 1,liste_lettre[-a-1],int(lettre_rang[-a-1]*10000)/10000,"% ")
    
#print("***************************************************************")
#print("le cumulé croissant est : ",int(10000*cumul)/10000,"%")
#print("***************************************************************")
#cumul = 0
#for a in range(20): #affichage du top 10 des mots fréquents
#    cumul += rang[-a-1]*100/len(split(original))
#    print(a + 1,liste[-a-1],int(rang[-a-1]*1000000/len(split(original)))/10000,"% ")
#
#print("***************************************************************")
#print("le cumulé croissant est : ",int(10000*cumul)/10000,"%")
#print("***************************************************************")