import Text
import Report

if __name__ == '__main__':
	languages_to_compare = ['fr', 'en', 'de']
	# créer toutes les données à partir de ca

	text_fr = Text.Text('fr')
	text_fr.generate_ranking()

	text_de = Text.Text('de')
	text_de.generate_ranking()

	text_en = Text.Text('en')
	text_en.generate_ranking()

	fr_sentence_number = text_fr.number_of_sentences
	de_sentence_number = text_de.number_of_sentences
	en_sentence_number = text_en.number_of_sentences

	fr_letters_inventory = text_fr.letters_inventory
	de_letters_inventory = text_de.letters_inventory
	en_letters_inventory = text_en.letters_inventory

	common_inventory = [c for c in fr_letters_inventory if c in en_letters_inventory and c in de_letters_inventory]

	# faire un dictionnaire des valeurs moyennées et triée
	mean_frequency = {k: int(10000*(v1 + v2 + v3) / 3)/1000 for k, v1 in text_fr.ranking_of_letters_frequency.items() for _, v2 in text_de.ranking_of_letters_frequency.items() for _, v3 in text_en.ranking_of_letters_frequency.items() if k in common_inventory}

	# prendre les 10 premières clés
	top = len(common_inventory)
	top_10 = {k: v for i, (k, v) in enumerate(mean_frequency.items()) if i < top}

	common_inventory_sorted = list(top_10.keys())

	fr_letters_frequency_refactored = []
	de_letters_frequency_refactored = []
	en_letters_frequency_refactored = []

	for c in common_inventory_sorted:
		fr_letters_frequency_refactored.append(text_fr.ranking_of_letters_frequency.get(c))
		de_letters_frequency_refactored.append(text_de.ranking_of_letters_frequency.get(c))
		en_letters_frequency_refactored.append(text_en.ranking_of_letters_frequency.get(c))

	my_report = Report.Report(
		languages_to_compare,
		[fr_sentence_number,de_sentence_number,en_sentence_number],
		common_inventory_sorted,
		[
		fr_letters_frequency_refactored,
		de_letters_frequency_refactored,
		en_letters_frequency_refactored
		]
		)

	my_report.generate()

	# 1er graph : proportion d’usage de la lettre dans la langue (détermination de l’inter des inventaires)
	# 2e graph ce serait pour le nombre moyen de mots par phrase puis lettre par mot