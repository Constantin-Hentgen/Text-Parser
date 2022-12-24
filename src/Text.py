from random import randint
import string

class Text:
    def __init__(self, country_code):
        self.file_path = f'../data/{country_code}.txt'
        self.text = self.load_text()

        self.number_of_sentences = self.set_number_of_sentences()
        self.number_of_words = self.set_number_of_words()
        self.number_of_letters = None
        self.number_of_special_characters = self.set_number_of_special_characters()

        self.number_of_alpha_characters = None
        self.number_of_meaningful_characters = None

        self.ranking_of_letters_frequency = None
        self.ranking_of_words_frequency = None
        self.ranking_of_special_characters_frequency = None

    def load_text(self):
        f = open(self.file_path, "r", encoding="utf-8")
        content = f.read()
        f.close()
        return content

    def text_refactor(self, mode) -> tuple[str, list[str]]:
        if self.text != None:
            if mode == "alpha":
                filtered_text = ''.join([c.lower() for c in self.text if c.isalpha() or c == ' '])
                words = filtered_text.split()
                sanitized_string = ''.join(words)
                return sanitized_string, words
            elif mode == "specials":
                filtered_text = ''.join([c for c in self.text if not c.isalnum() and c != ' ' and c != '\n' and c != '\t'])
                return filtered_text

    def doubles_sanitizer(self, list) -> list:
        sanitized_list = []
        for word in list:
            if word not in sanitized_list:
                sanitized_list.append(word)
        return sanitized_list

    def special_doubles_sanitizer(self, string) -> list:
        sanitized_string = []
        for character in string:
            if character not in sanitized_string:
                sanitized_string += character
        return sanitized_string

    def inventory_of_characters(self, string) -> str:
        inventory = set()
        for character in string:
            if character not in inventory:
                inventory.add(character)
        return inventory

    def get_frequency(self, inventory, data) -> dict[str, int]:
        couples_list = []
        for i in inventory:
            couples_list.append((i,sum(1 for e in data if e == i)))
        return couples_list

    def dictionnary_sorter(self, list) -> dict[str, int]:
        #trie la liste des unités en fonction de leur fréquence
        sorted_list = sorted(list, key=lambda x: x[1], reverse=True)
        return {key: value for key, value in sorted_list}

    def set_number_of_sentences(self):
        return sum([1 for character in self.text if character == "."])

    def set_number_of_words(self):
        return len(self.text_refactor('alpha')[1])

    def set_number_of_special_characters(self):
        return len(self.text_refactor('specials')[1])

    def set_number_of_letters(self):
        return self.text_refactor('alpha')[0]

    def generate_ranking(self):
        clustered_letters = self.text_refactor('alpha')[0]
        isolated_words_raw = self.text_refactor('alpha')[1]
        isolated_words_doubleless = self.doubles_sanitizer(isolated_words_raw)
        special_characters = self.text_refactor('specials')

        letters_inventory = self.inventory_of_characters(clustered_letters)
        letters_frequency = self.get_frequency(letters_inventory, clustered_letters)
        words_frequency = self.get_frequency(isolated_words_doubleless, isolated_words_raw)

        special_characters_inventory = self.special_doubles_sanitizer(special_characters)
        special_characters_frequency = self.get_frequency(special_characters_inventory, special_characters)

        self.ranking_of_letters_frequency = self.dictionnary_sorter(letters_frequency)
        self.ranking_of_words_frequency = self.dictionnary_sorter(words_frequency)
        self.ranking_of_special_characters_frequency = self.dictionnary_sorter(special_characters_frequency)
