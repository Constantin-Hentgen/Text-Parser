from random import randint
import string

path = "../data/java.txt"
f = open(path, "r", encoding="utf-8")
text = f.read()
f.close()

def text_refactor(text, mode) -> tuple[str, list[str]]:
    if mode == "alpha":
        filtered_text = ''.join([c.lower() for c in text if c.isalpha() or c == ' '])
        words = filtered_text.split()
        sanitized_string = ''.join(words)
        return sanitized_string, words
        print('test')
    elif mode == "specials":
        filtered_text = ''.join([c for c in text if not c.isalnum() and c != ' ' and c != '\n' and c != '\t'])
        return filtered_text

def doubles_sanitizer(list) -> list:
    sanitized_list = []
    for word in list:
        if word not in sanitized_list:
            sanitized_list.append(word)
    return sanitized_list

def special_doubles_sanitizer(string) -> list:
    sanitized_string = []
    for character in string:
        if character not in sanitized_string:
            sanitized_string += character
    return sanitized_string

def inventory_of_characters(string) -> str:
    inventory = set()
    for character in string:
        if character not in inventory:
            inventory.add(character)
    return inventory

def get_frequency(inventory, data) -> dict[str, int]:
    couples_list = []
    for i in inventory:
        couples_list.append((i,sum(1 for e in data if e == i)))
    return couples_list

def dictionnary_sorter(list) -> dict[str, int]: #trie la liste des unités en fonction de leur fréquence
    sorted_list = sorted(list, key=lambda x: x[1], reverse=True)
    return {key: value for key, value in sorted_list}

# EXECUTION

# materials
clustered_letters = text_refactor(text, 'alpha')[0]
isolated_words_raw = text_refactor(text, 'alpha')[1]
isolated_words_doubleless = doubles_sanitizer(isolated_words_raw)
inventory = inventory_of_characters(clustered_letters)
letters_frequency = get_frequency(inventory, clustered_letters)
words_frequency = get_frequency(isolated_words_doubleless, isolated_words_raw)

# results
ranking_of_letters_frequency = dictionnary_sorter(letters_frequency)
ranking_of_words_frequency = dictionnary_sorter(words_frequency)
number_of_sentences = sum([1 for character in text if character == "."])

special_characters = text_refactor(text, 'specials')
inventory_special_characters = special_doubles_sanitizer(special_characters)
special_characters_frequency = get_frequency(inventory_special_characters, special_characters)
ranking_of_special_characters_frequency = dictionnary_sorter(special_characters_frequency)
