from fpdf import FPDF
import chart
import table

class Report:
	def __init__(self, language_code, mean_nb_words_per_sentence, letters_inventory, list_of_letters_stats, mean_nb_letters_per_word, list_of_special_characters_stats, special_characters_inventory):
		self.language_code = language_code
		self.mean_nb_words_per_sentence = mean_nb_words_per_sentence
		self.letters_inventory = letters_inventory
		self.list_of_letters_stats = list_of_letters_stats
		self.mean_nb_letters_per_word = mean_nb_letters_per_word
		self.list_of_special_characters_stats = list_of_special_characters_stats
		self.special_characters_inventory = special_characters_inventory
		self.pdf = FPDF()

	def generate(self):
		chart.purge_chart()
		self.pdf.add_page()
		self.pdf.set_margins(left=30, top=20, right=30)
		self.pdf.add_font("OpenSans", "", "/usr/share/fonts/open-sans/OpenSans-Regular.ttf", uni=True)
		self.pdf.set_font("OpenSans", "", 25)
		self.pdf.cell(w=self.pdf.w-15, h=10, txt="Comparative report", border=0, ln=1, align="C")
		self.pdf.ln()
		self.pdf.set_font("OpenSans", "", 10)
		self.pdf.multi_cell(0, 5, "Be careful, the following statistics are based on the letters in common between the different sources. Indeed, you will notice that the total of the percentage doesn’t lead to 100% or something near as it is only a part of the total alphabet used.")
		
		self.pdf.ln()

		table.generate_table(
			pdf = self.pdf,
			column_titles = self.language_code,
			columns_as_lists_of_values = self.list_of_letters_stats,
			line_titles = self.letters_inventory,
			unit = " %",
			first_column_title = 'Letters'
		)

		self.pdf.ln()
		self.pdf.ln()

		table.generate_table(
			pdf = self.pdf,
			column_titles = self.language_code,
			columns_as_lists_of_values = self.list_of_special_characters_stats,
			line_titles = self.special_characters_inventory,
			unit = " %",
			first_column_title = 'Special characters'
		)

		self.pdf.ln()

		chart.generate_multi_column_chart(
			title = 'Proportion of usage for letters',
			x_axis = self.letters_inventory,
			y_axis = self.list_of_letters_stats,
			x_label = self.language_code,
			y_label = '%',
			accuracy = 1
		)

		self.pdf.ln()

		chart.generate_multi_column_chart(
			title = 'Proportion of usage for special characters',
			x_axis = self.special_characters_inventory,
			y_axis = self.list_of_special_characters_stats,
			x_label = self.language_code,
			y_label = '%',
			accuracy = 1
		)

		self.pdf.ln()

		chart.generate_simple_column_chart(
			title = 'Mean number of words per sentence',
			x_axis = self.language_code,
		 	y_axis = self.mean_nb_words_per_sentence,
			x_label = self.language_code,
			y_label = 'number of words'
		)

		self.pdf.ln()

		chart.generate_simple_column_chart(
			title = 'Mean number of letters per word',
			x_axis = self.language_code,
		 	y_axis = self.mean_nb_letters_per_word,
			x_label = self.language_code,
			y_label = 'number of letters'
		)

		chart.add_chart_to_report(self.pdf)

		self.pdf.output('../report.pdf', 'F')