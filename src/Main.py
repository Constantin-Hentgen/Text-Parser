import Text
import Report
import tool

if __name__ == '__main__':
	# maximum 3 langues
	# language_codes = ['custom_source_a','custom_source_b','custom_source_c']
	language_codes = ['fr','en','dk']

	letters_rankings = []
	special_characters_rankings = []
	mean_nb_words_per_sentence = []
	letters_inventories = []
	special_characters_inventories = []
	mean_nb_letters_per_word = []

	accuracy = 3

	for language in language_codes:
		temp = Text.Text(str(language))
		temp.generate_ranking()
		letters_rankings.append(temp.ranking_of_letters_frequency)
		special_characters_rankings.append(temp.ranking_of_special_characters_frequency)
		mean_nb_words_per_sentence.append(round(temp.number_of_words/temp.number_of_sentences,accuracy))
		letters_inventories.append([k for k in temp.ranking_of_letters_frequency if temp.ranking_of_letters_frequency.get(k) > 0.05])
		special_characters_inventories.append([k for k in temp.ranking_of_special_characters_frequency if temp.ranking_of_special_characters_frequency.get(k) > 0.05])
		mean_nb_letters_per_word.append(round(temp.number_of_letters/temp.number_of_words,accuracy))

	common_inventory = tool.generate_common_inventory(letters_inventories, language_codes, letters_rankings)
	common_inventory_special_characters = tool.generate_common_inventory(special_characters_inventories, language_codes, special_characters_rankings)

	list_of_letters_stats = tool.generate_sorted_frequencies(common_inventory, letters_rankings)
	list_of_special_characters_stats = tool.generate_sorted_frequencies(common_inventory_special_characters, special_characters_rankings)
	
	my_report = Report.Report(
		language_codes,
		mean_nb_words_per_sentence,
		common_inventory,
		list_of_letters_stats,
		mean_nb_letters_per_word,
		list_of_special_characters_stats,
		common_inventory_special_characters
	)

	my_report.generate()