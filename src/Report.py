# Import des bibliothèques nécessaires
from fpdf import FPDF
import numpy as np
import matplotlib.pyplot as plt

class Report:
	def __init__(self, list_1, list_2):
		self.list_1 = list_1
		self.list_2 = list_2

	# permettre le choix de la police

	# Création de l'objet PDF
	def generate(self):
		pdf = FPDF()
		pdf.add_page()

		# Définition des marges
		pdf.set_margins(left=30, top=20, right=30)

		# Définition de la police à utiliser
		pdf.add_font("OpenSans", "", "/usr/share/fonts/open-sans/OpenSans-Regular.ttf", uni=True)
		pdf.set_font("OpenSans", "", 25)

		# Ajout du titre avec la taille de police modifiée
		pdf.cell(w=pdf.w-15, h=10, txt="Titre du rapport", border=0, ln=1, align="C")

		pdf.ln()

		pdf.set_font("OpenSans", "", 10)

		# Ajout des paragraphes "lorem ipsum"
		pdf.multi_cell(0, 5, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc interdum quam in tortor faucibus, auctor lobortis elit condimentum. Nulla sed pulvinar dolor. Fusce volutpat dui at dui laoreet, et aliquam metus venenatis. Aliquam at elit id lorem dignissim laoreet. Aenean ac nisi euismod, facilisis justo id, ornare tortor. Nam condimentum nisl nisi, eu tempus est faucibus sit amet. Donec bibendum ante id justo hendrerit, sit amet scelerisque mauris laoreet.")

		pdf.ln()

		pdf.multi_cell(0, 5, "Praesent volutpat, est ac fringilla aliquam, diam nibh tincidunt diam, ac egestas purus arcu et nisl. Sed non magna at nisl laoreet ullamcorper et at velit. Aliquam vel velit vel est dignissim luctus. Aliquam erat volutpat. Nam scelerisque urna quis quam malesuada, a tincidunt urna viverra. Maecenas condimentum felis id mauris consectetur imperdiet. Integer euismod pharetra enim, ac ultricies lacus elementum a. Nulla facilisi.")

		# Largeur des colonnes
		col_width = 2.2 + pdf.w / 6

		pdf.ln()

		# En-têtes du tableau
		pdf.cell(col_width, 5, "Colonne 1", 1, 0, "C")
		pdf.cell(col_width, 5, "Colonne 2", 1, 0, "C")
		pdf.cell(col_width, 5, "Colonne 3", 1, 0, "C")
		pdf.cell(col_width, 5, "Colonne 4", 1, 0, "C")

		# Lignes du tableau
		for i in range(1, 21):
			pdf.ln()
			pdf.cell(col_width, 5, str(i), 1, 0, "C")
			pdf.cell(col_width, 5, str(i), 1, 0, "C")
			pdf.cell(col_width, 5, str(i), 1, 0, "C")
			pdf.cell(col_width, 5, str(i), 1, 0, "C")

		pdf.ln()
		pdf.ln()

		# PLOT 1

		labels = ['G1', 'G2', 'G3', 'G4', 'G5']
		men_means = [20, 34, 30, 35, 27]
		women_means = [25, 32, 34, 20, 25]

		x = np.arange(len(labels))  # the label locations
		width = 0.35  # the width of the bars

		fig, ax = plt.subplots()
		rects1 = ax.bar(x - width/2, men_means, width, label='Men')
		rects2 = ax.bar(x + width/2, women_means, width, label='Women')

		# Add some text for labels, title and custom x-axis tick labels, etc.
		ax.set_ylabel('Scores')
		ax.set_title('Scores by group and gender')
		ax.set_xticks(x, labels)
		ax.legend()

		ax.bar_label(rects1, padding=3)
		ax.bar_label(rects2, padding=3)

		fig.tight_layout()

		# Enregistrement du graphique en tant qu'image temporaire
		fig.savefig("../img/graphique.png")

		# FIG 2

		fig2, ax2 = plt.subplots()

		fruits = ['apple', 'blueberry', 'cherry', 'orange']
		counts = [40, 100, 30, 55]
		bar_labels = ['red', 'blue', 'red', 'orange']
		bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

		ax2.bar(fruits, counts, label=bar_labels, color=bar_colors)

		ax2.set_ylabel('fruit supply')
		ax2.set_title('Fruit supply by kind and color')
		ax2.legend(title='Fruit color')

		fig2.savefig("../img/graphique2.png")

		pdf.multi_cell(0, 5, "Praesent volutpat, est ac fringilla aliquam, diam nibh tincidunt diam, ac egestas purus arcu et nisl. Sed non magna at nisl laoreet ullamcorper et at velit. Aliquam vel velit vel est dignissim luctus. Aliquam erat volutpat. Nam scelerisque urna quis quam malesuada, a tincidunt urna viverra. Maecenas condimentum felis id mauris consectetur imperdiet. Integer euismod pharetra enim, ac ultricies lacus elementum a. Nulla facilisi.")

		# Ajout du graphique au document PDF
		pdf.image("../img/graphique.png", x=0, w=120)
		pdf.image("../img/graphique2.png", x=0, w=120)

		# Enregistrement du fichier PDF
		pdf.output("../report.pdf")