from fpdf import FPDF

def generate_table(pdf, column_titles, columns_as_lists_of_values, line_titles, unit, first_column_title):
	column_width = pdf.w / 6

	# Headers
	pdf.cell(column_width, 5, first_column_title, 1, 0, "C")

	for column_title in column_titles:
		pdf.cell(column_width, 5, column_title, 1, 0, "C")

	# Lines
	for i in range(0, len(columns_as_lists_of_values[0])):
		pdf.ln()


		pdf.cell(column_width, 5, str(line_titles[i]), 1, 0, "C")
		for array in columns_as_lists_of_values:
			equivalents = [list[i] for list in columns_as_lists_of_values]
			
			if array[i] == max(equivalents):
				pdf.set_font('Arial', 'B', 9)

			pdf.cell(column_width, 5, str(array[i]) + unit, 1, 0, "C")
			pdf.set_font('Arial', '', 9)
	
	pdf.ln()
	pdf.cell(column_width, 5, "Total", 1, 0, "C")

	for array in columns_as_lists_of_values:
		pdf.cell(column_width, 5, str(round(sum([percent for percent in array]),3)) + unit, 1, 0,"C")