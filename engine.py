#utiliser un fichier remplis de français pour pouvoir y faire une analyse de fréquence des lettres
#aussi pouvoir dire quel sont les mots les plus fréquents
#faire l'intégralité du dev en POO
#permettre l'exploration par mot et par phrase

f = open('hugo_notre_dame_de_paris.txt','r')
lecture = f.read()
#on stocke tout le texte dans la liste lecture
#print(lecture)
f.close()

number = 0
numbera = 0
numbere = 0
numberw = 0

for a in lecture:
    number += 1

    if a == "a":
        numbera += 1
    
    elif a == "e":
        numbere += 1
        
    elif a == "w":
        numberw += 1

#print(number)
#faire un arrondi à la deuxième décimale non-nulle
print("a = ",int(numbera*1000/number)/10)
print("e = ",int(numbere*1000/number)/10)
print("w = ",int(numberw*1000/number)/10)
