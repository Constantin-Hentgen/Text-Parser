from random import randint
import string

path = "bank/fastfr.txt"
f = open(path, "r", encoding="utf-8")
text = f.read()
f.close()

# we suppose that points are used only for punctuation
number_of_sentences = sum([1 for character in text if character == "."])

def text_refactor(text) -> tuple[str, list[str]]:
    filtered_text = ''.join([c.lower() for c in text if c.isalpha() or c == ' '])
    words = filtered_text.split()
    sanitized_string = ''.join(words)
    return sanitized_string, words

def doubles_sanitizer(list) -> list:
    sanitized_list = []
    for word in list:
        if word not in sanitized_list:
            sanitized_list.append(word)
    return sanitized_list

def inventory_of_characters(string) -> str:
    inventory = ''
    for character in string:
        if character not in inventory:
            inventory += character
    return inventory

def get_characters_frequency(inventory, text) -> dict[str, int]:
    couples_list = []
    for l in inventory:
        couples_list.append((l,sum(1 for c in text if c == l)))
    return {key: value for key, value in couples_list}

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

# EXECUTION

clustered_letters = text_refactor(text)[0]
isolated_words_raw = text_refactor(text)[1]
isolated_words_doubleless = doubles_sanitizer(isolated_words_raw)
inventory = inventory_of_characters(clustered_letters)

# print(len(isolated_words_raw))
# print(len(isolated_words_doubleless))
print(inventory)
print(get_characters_frequency(inventory, clustered_letters))

# number of sentences
# print(number_of_sentences)