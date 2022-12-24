import Text
import Report

if __name__ == '__main__':
	languages_to_compare = ['fr', 'en', 'de']

	texte_fr_random = Text.Text('fr')
	texte_fr_random.generate_ranking()

	texte_de_random = Text.Text('de')
	texte_de_random.generate_ranking()

	# je veux pouvoir affecter les datas à un objet report
	
	my_report = Report.Report([1,2],[1,2])
	# my_report.generate()