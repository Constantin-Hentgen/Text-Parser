#utiliser un fichier remplis de français pour pouvoir y faire une analyse de fréquence des lettres
#aussi pouvoir dire quel sont les mots les plus fréquents
#faire l'intégralité du dev en POO

f = open('hugo_notre_dame_de_paris.txt','r')
lecture = f.read()
print(lecture)
f.close()