
def generate_common_inventory(inventories, language_codes, rankings):
	common_inventory = []
	merged_inventories = []

	for inventory in inventories:
		for letter in inventory:
			merged_inventories.append(letter)

	for letter in merged_inventories:
		count = sum([1 for c in merged_inventories if c == letter])
		if count == len(language_codes) and letter not in common_inventory:
			common_inventory.append(letter)

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
	return common_inventory_sorted

def generate_sorted_frequencies(common_inventory, rankings):
	letters_frequencies_refactored = []

	for ranking in rankings:
		temp = []
		for c in common_inventory:
			temp.append(ranking.get(c))
		letters_frequencies_refactored.append(temp)

	return letters_frequencies_refactored