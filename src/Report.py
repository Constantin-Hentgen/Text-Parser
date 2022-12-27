# Import des bibliothèques nécessaires
from fpdf import FPDF
import numpy as np
import matplotlib.pyplot as plt

class Report:
	def __init__(self, language_code, number_of_sentences, letters_inventory, array_of_lang_stats):
		self.language_code = language_code
		self.number_of_sentences = number_of_sentences
		self.letters_inventory = letters_inventory
		self.array_of_lang_stats = array_of_lang_stats
		self.pdf = FPDF()

	def generate(self):
		self.pdf.add_page()
		self.pdf.set_margins(left=30, top=20, right=30)
		self.pdf.add_font("OpenSans", "", "/usr/share/fonts/open-sans/OpenSans-Regular.ttf", uni=True)
		self.pdf.set_font("OpenSans", "", 25)
		self.pdf.cell(w=self.pdf.w-15, h=10, txt="Comparative report", border=0, ln=1, align="C")

		self.pdf.ln()

		self.pdf.set_font("OpenSans", "", 10)

		self.pdf.multi_cell(0, 5, "Be careful, the following statistics are based on the letters in common between the different sources. Indeed, you will notice that the total of the percentage doesn’t lead to 100% or something near as it is only a part of the total alphabet used.")
		self.generate_table()

		self.pdf.ln()
		self.pdf.ln()

		self.generate_double_column_chart()
		self.generate_simple_column_chart()

		# Ajout du graphique au document PDF
		self.pdf.image("../img/graphique.png", x=0, w=180)
		self.pdf.image("../img/graphique2.png", x=0, w=120)

		self.pdf.output("../report.pdf")


	def generate_table(self):
		# Largeur des colonnes
		col_width = 2.2 + self.pdf.w / 6

		self.pdf.ln()

		# En-têtes du tableau
		self.pdf.cell(col_width, 5, "Letters", 1, 0, "C")

		for language in self.language_code:
			self.pdf.cell(col_width, 5, str(language), 1, 0, "C")

		# Lignes du tableau
		for i in range(1, len(self.array_of_lang_stats[0])):
			self.pdf.ln()
			
			self.pdf.cell(col_width, 5, str(self.letters_inventory[i]), 1, 0, "C")
			for array in self.array_of_lang_stats:
				self.pdf.cell(col_width, 5, str(array[i]) + " %", 1, 0, "C")
		
		self.pdf.ln()
		self.pdf.cell(col_width, 5, "Total", 1, 0, "C")
		for array in self.array_of_lang_stats:
			self.pdf.cell(col_width, 5, str(round(sum([percent for percent in array]),3)) + " %", 1, 0,"C")

	def generate_double_column_chart(self):
		letters_inventory = self.letters_inventory
		accuracy = 1

		x = np.arange(len(letters_inventory))
		width = 0.25 # taille des colonnes

		fig, ax = plt.subplots()
		
		for array in self.array_of_lang_stats:
			if self.array_of_lang_stats.index(array) != 0:
				ax.bar(x + width*(-1)**self.array_of_lang_stats.index(array), [round(percent,accuracy) for percent in array], width, label=self.language_code[self.array_of_lang_stats.index(array)])
			else:
				ax.bar(x, [round(percent,accuracy) for percent in array], width, label=self.language_code[0])

		ax.set_ylabel('%')
		ax.set_title('Proportion of usage for letters')
		ax.set_xticks(x, letters_inventory)
		ax.legend()

		fig.tight_layout()
		fig.savefig("../img/graphique.png")

	def generate_simple_column_chart(self):
		# faire en sorte que ça accepte des tailles variables de lists
		fig2, ax2 = plt.subplots()

		x_axis = self.language_code
		number_of_sentences = self.number_of_sentences
		
		bar_letters_inventory = self.language_code
		bar_colors = ['tab:red', 'tab:blue', 'tab:orange','tab:purple','tab:green']

		ax2.bar(x_axis, number_of_sentences, label=bar_letters_inventory, color=bar_colors)

		ax2.set_ylabel('number of sentences')
		ax2.set_title('Comparison of sentences number')
		ax2.legend(title='Legend')

		fig2.savefig("../img/graphique2.png")