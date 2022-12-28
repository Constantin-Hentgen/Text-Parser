import numpy as np
import matplotlib.pyplot as plt
import os

def fetch_chart_name():
	dir_path = "../img/"
	items_list = os.listdir(dir_path)
	files_list = [item for item in items_list if os.path.isfile(os.path.join(dir_path, item))]
	if len(files_list) > 0:
		return files_list
	else:
		return []

def generate_multi_column_chart(title, x_axis, y_axis, x_label, y_label, accuracy):
	x = np.arange(len(x_axis))
	width = 0.8/len(x_label) # taille des colonnes
	fig, ax = plt.subplots()
	
	if len(x_label) == 3:
		for array in y_axis:
			if y_axis.index(array) == 0:
				ax.bar(x, [round(percent,accuracy) for percent in array], width, label=x_label[0])
			else:
				ax.bar(x + width*(-1)**y_axis.index(array), [round(percent,accuracy) for percent in array], width, label=x_label[y_axis.index(array)])
	elif len(x_label) == 2:
		for array in y_axis:
			ax.bar(x + (width*0.5)*(-1)**y_axis.index(array), [round(percent,accuracy) for percent in array], width, label=x_label[y_axis.index(array)])
	else:
		ax.bar(x, [round(percent,accuracy) for percent in y_axis[0]], width, label=x_label[0])

	ax.set_ylabel(y_label)
	ax.set_title(title)
	ax.set_xticks(x, x_axis)
	ax.legend(title='Legend')
	fig.tight_layout()
	save_chart(fig)

def save_chart(fig):
	num = len(fetch_chart_name())
	fig.savefig("../img/chart_"+str(num)+".jpeg")

def generate_simple_column_chart(title, x_axis, y_axis, x_label, y_label):
	fig, ax = plt.subplots()
	bar_colors = ['tab:red', 'tab:blue', 'tab:orange','tab:purple','tab:green']
	ax.bar(x_axis, y_axis, label=x_label, color=bar_colors)
	ax.set_ylabel(y_label)
	ax.set_title(title)
	ax.legend(title='Legend')

	for x_coord, y_coord in zip(x_axis, y_axis):
		ax.text(x_coord, y_coord, y_coord, ha='center', va='bottom')

	save_chart(fig)

def add_chart_to_report(pdf):
	for chart_name in fetch_chart_name():
		pdf.image("../img/" + chart_name, x=0, w=120)

def purge_chart():
	directory = '../img/'
	for filename in os.listdir(directory):
		file_path = os.path.join(directory, filename)
		try:
			os.unlink(file_path)
		except Exception as e:
			print(e)
