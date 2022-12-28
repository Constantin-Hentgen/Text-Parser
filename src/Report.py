from fpdf import FPDF
import chart
import table


class Report:
	def __init__(self, language_code, number_of_sentences, letters_inventory, array_of_lang_stats):
		self.language_code = language_code
		self.number_of_sentences = number_of_sentences
		self.letters_inventory = letters_inventory
		self.array_of_lang_stats = array_of_lang_stats
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
		
		table.generate_table(
			pdf = self.pdf,
			column_titles = self.language_code,
			columns_as_lists_of_values = self.array_of_lang_stats,
			line_titles = self.letters_inventory,
			unit = " %"
		)

		self.pdf.ln()

		chart.generate_multi_column_chart(
			title = 'Proportion of usage for letters',
			x_axis = self.letters_inventory,
			y_axis = self.array_of_lang_stats,
			x_label = self.language_code,
			y_label = '%',
			accuracy = 1
		)

		chart.generate_simple_column_chart(
			title = 'Comparison of sentences number',
			x_axis = self.language_code,
		 	y_axis = self.number_of_sentences,
			x_label = self.language_code,
			y_label = 'number of sentences'
		)

		chart.add_chart_to_report(self.pdf)