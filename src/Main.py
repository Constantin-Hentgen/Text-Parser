import Text
import Report

if __name__ == '__main__':
	language_codes = ['fr', 'en', 'de']
	# créer toutes les données à partir de ca

	rankings = []
	sentence_numbers = []
	inventories = []

	for language in language_codes:
		temp = Text.Text(str(language))
		temp.generate_ranking()
		rankings.append(temp.ranking_of_letters_frequency)
		sentence_numbers.append(temp.number_of_sentences)
		inventories.append(temp.letters_inventory)

	reference_language_inventory = inventories[0]

	common_inventory = []
	merged_inventories = []

	for inventory in inventories:
		for letter in inventory:
			merged_inventories.append(letter)

	for letter in merged_inventories:
		count = sum([1 for c in merged_inventories if c == letter])
		if count == len(language_codes) and letter not in common_inventory:
			common_inventory.append(letter)

	# print(common_inventory)

	# faire un dictionnaire des valeurs moyennées et triée

	# mean_frequency = {k: int(10000*(v1 + v2 + v3) / 3)/1000 for k, v1 in text_fr.ranking_of_letters_frequency.items() for _, v2 in text_de.ranking_of_letters_frequency.items() for _, v3 in text_en.ranking_of_letters_frequency.items() if k in common_inventory}
	mean_frequency = {}

	for k in common_inventory:
		v_sum = 0
		for ranking in rankings:
			v_sum += ranking.get(k, 0)
		mean_frequency[k] = int(10000 * v_sum / len(rankings)) / 1000

	# prendre les 10 premières clés
	top = len(common_inventory)
	top_list = {k: v for i, (k, v) in enumerate(mean_frequency.items()) if i < top}

	common_inventory_sorted = list(top_list.keys())

	letters_frequencies_refactored = []

	for ranking in rankings:
		temp = []
		for c in common_inventory_sorted:
			temp.append(ranking.get(c))
		letters_frequencies_refactored.append(temp)
	
	my_report = Report.Report(
		language_codes,
		sentence_numbers,
		common_inventory_sorted,
		letters_frequencies_refactored
		)

	my_report.generate()

	# 1er graph : proportion d’usage de la lettre dans la langue (détermination de l’inter des inventaires)
	# 2e graph ce serait pour le nombre moyen de mots par phrase puis lettre par mot