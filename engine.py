from random import randint
import string

path = "bank/fastfr.txt"
f = open(path, "r", encoding="utf-8")
text = f.read()
f.close()

# Initialization for French content
vowels = "aeiouy"
accented_vowels = "àâéèêiïîôùûëäü"

# we suppose that points are used only for punctuation
number_of_sentences = sum([1 for character in text if character == "."])

def text_refactor(text) -> tuple[str, list[str]] :
    filtered_text = ''.join([c for c in text if c.isalpha() or c == ' '])
    words = filtered_text.split()
    filtered_string = ''.join(words)
    return filtered_string, words

def get_characters_frequency(text) -> list: 
    ranking = [] #liste vide pour contenir les fréquences
    alpha_characters_number = 0

    total = sum(1 for l in text if l in alphabet)
    alpha_characters_number = sum(1 for c in text if c.isalpha())

    alpha_characters_number = alpha_characters_number * 100 / total #calcul de la fréquence
    ranking.append(number)

    alpha_characters_number = 0 #réinitialisation de alpha_characters_number pour pas qu'une lettre hérite les statistiques d'une autre

    return ranking #ranking des fréquences selon l'ordre alphabétique

def split(document): #sépare le textes en petites unités que nous allons analyser
    split = [] #liste résultat contenant les unités séparées
    iterator = 0 #correspond au suivi des unités
    iteration = 0 #correspond au suivi des caractères
    document = document.replace("-\n", '') #suppresion des \n de passage à la ligne et des - de jonction

    for caracter in document: #pour chaque caractère du document
        if caracter in special_characters: #si le caractère du document est un caractère spécial
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
    compteur_vowels = 0
    compteur_consonants = 0
    lettres_francais_accented_vowels = 0

    for character in document:
        if character in vowels:
            compteur_vowels += 1

        if character in consonants:
            compteur_consonants += 1
        
        if character in accented_vowels:
            lettres_francais_accented_vowels += 1
  
    return compteur_vowels, compteur_consonants, compteur_consonants+compteur_vowels,lettres_francais_accented_vowels


#print(vowel(text)[0]/vowel(text)[2])

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

#print(frequency(text)) 
#print(split(text)) #partage du document en unités
#print(gatherer(split(text))) #rassemblement des unités semblables
#print(ranker(gatherer(split(text)))) #production des classements sur victor hugo de la liste rassemblée

#print(algotri(doublon(ranker(gatherer(split(text))),gatherer(split(text)))[0],doublon(ranker(gatherer(split(text))),gatherer(split(text)))[1]))
#concaténation des applications de toutes les fonctions

#print(algotri(frequency(text), list(alphabet))) #fréquence des lettres

text_material = text_refactor(text)
print(text_material[0])
print(text_material[1])

# number of sentences
# print(number_of_sentences)