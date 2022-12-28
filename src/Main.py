import Text
import Report
import tool

if __name__ == '__main__':
	# maximum 3 langues
	language_codes = ['custom_source_a','custom_source_b','custom_source_c']

	letters_rankings = []
	special_characters_rankings = []
	mean_nb_words_per_sentence = []
	inventories = []
	mean_nb_letters_per_word = []

	accuracy = 3

	for language in language_codes:
		temp = Text.Text(str(language))
		temp.generate_ranking()
		letters_rankings.append(temp.ranking_of_letters_frequency)
		mean_nb_words_per_sentence.append(round(temp.number_of_words/temp.number_of_sentences,accuracy))
		inventories.append([k for k in temp.ranking_of_letters_frequency if temp.ranking_of_letters_frequency.get(k) > 0.05])
		mean_nb_letters_per_word.append(round(temp.number_of_letters/temp.number_of_words,accuracy))

	common_inventory = tool.generate_common_inventory(inventories, language_codes, letters_rankings)
	
	letters_frequencies_refactored = tool.generate_sorted_frequencies(common_inventory, letters_rankings)
	list_of_special_characters_stats = tool.generate_sorted_frequencies(common_inventory, letters_rankings)
	
	my_report = Report.Report(
		language_codes,
		mean_nb_words_per_sentence,
		common_inventory,
		letters_frequencies_refactored,
		mean_nb_letters_per_word,
		list_of_special_characters_stats
	)

	my_report.generate()