from random import randint
from tkinter import *
from tkinter import filedialog
import os

window = Tk()

window.title("Text Analyzer by Constantin")
window.geometry('1900x1080')
#window.attributes('-fullscreen', True)

display_text = StringVar()
lbl = Label(window, textvariable=display_text)
#lbl.grid(column=1,row=1)
lbl.place(relx=0.5, rely=0.4, anchor=CENTER)

#txt = Entry(window,width=10)
#txt.grid(column=1, row=0)

def pathfinder():
    file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
    s = display_text.get()
    s += "\n" + str(file)
    display_text.set(s)

    return file

#########################################################################################
special = " .,/\n\\*%&;?$€•(! ){#[]}–\"=+-*“”|…’'`:»«0123456789" #définition des caractères spéciaux pour effectuer des tests
particular = ".,/\\*%&;?$€•(=~!{#[–“|”…’'`:«"
alphabet = "abcdefghijklmnßopqrstuvwxyzçêèàéâûîùôœæïîôùüäëû" #définition de l'alphabet pour effectuer les tests
voyelles = "aeiouyàâéèêiïîôùüäëû"
consonnes = "bcdfghjklmnpqrstvwxzßç"
accents = "àâéèêiïîôùûëäü"

def identity(path):
    #lecture du fichier texte pour effectuer le traitement
    f = open(path, "r", encoding="utf-8") #ouverture du document
    original = f.read() #assignement à une variable du contenu du document
    f.close() #fermeture du document
    
    return original

def phrase_counter(original):
    compteur_points = 0

    for character in original: #compteur de points pour connaître le nombre de phrase
        if character == ".":
            compteur_points += 1

    return compteur_points

def frequency(original): #renvoi la fréquence pour chaque caractère
    ranking = [] #liste vide pour contenir les fréquences
    total = 0
    number = 0

    for letter in original: #boucle pour compter le nombre total de caractères non vides dans le document
        if letter in alphabet: #comptabilisation du nombre de caractères non spéciaux
            total += 1

    for letter in alphabet: #pour chaque lettre de l'alphabet
        for element in original: #pour chaque lettre du document
            if element == letter:
                number += 1 #incrémenter pour la stat de la lettre par occurence

        number = number * 100 / total #calcul de la fréquence
        ranking.append(number)

        number = 0 #réinitialisation de number pour pas qu'une lettre hérite les statistiques d'une autre

    return ranking #ranking des fréquences selon l'ordre alphabétique

def frequenci(original): #renvoi la fréquence pour chaque caractère
    ranking = [] #liste vide pour contenir les fréquences
    total = 0
    number = 0

    for letter in original: #boucle pour compter le nombre total de caractères non vides dans le document
        if letter in particular: #comptabilisation du nombre de caractères non spéciaux
            total += 1

    for letter in particular: #pour chaque lettre de l'alphabet
        for element in original: #pour chaque lettre du document
            if element == letter:
                number += 1 #incrémenter pour la stat de la lettre par occurence

        number = number * 100 / total #calcul de la fréquence
        ranking.append(number)

        number = 0 #réinitialisation de number pour pas qu'une lettre hérite les statistiques d'une autre

    return ranking #ranking des fréquences selon l'ordre alphabétique

def split(document): #sépare le textes en petites unités que nous allons analyser
    split = [] #liste résultat contenant les unités séparées
    iterator = 0 #correspond au suivi des unités
    iteration = 0 #correspond au suivi des caractères
    document = document.replace("-\n", '') #suppresion des \n de passage à la ligne et des - de jonction

    for caracter in document: #pour chaque caractère du document
        if caracter in special: #si le caractère du document est un caractère spécial
            split.append(document[iterator:iteration].lower()) #ajouter à split l'unité déterminée
            iterator = iteration + 1 #évolue d'unité en unité

        iteration += 1 # évolue caractère par caractère
    
    while("" in split) : #supprime les éléments vides
        split.remove("")
                
    return split

def gatherer(liste): #rassemble les unités égales
    gathered = []

    while len(liste) > 0:
        gathered.append(liste[0])
        del liste[0]
        for element in liste:
            if element == gathered[-1]:
                gathered.append(element)
                liste.remove(element)

    return gathered

def ranker(liste): #compte le nombre d'éléments par unités
    rank = []
    count = 0

    for a in range(len(liste)):
        for b in range(len(liste)):
            if liste[b] == liste[a]:
                count += 1
        rank.append(count)
        count = 0

    return rank

def doublon(liste_rank, real_liste): #supprime les doublons
    liste_propre = []
    rank_propre = []

    liste_propre.append(real_liste[0])
    rank_propre.append(liste_rank[0])

    for a in range(len(real_liste) - 1):
        if real_liste[a + 1] not in liste_propre:
            liste_propre.append(real_liste[a + 1])
            rank_propre.append(liste_rank[a + 1])

    return rank_propre, liste_propre

def vowel(document):
    compteur_voyelles = 0
    compteur_consonnes = 0
    lettres_francais_accents = 0

    for character in document:
        if character in voyelles:
            compteur_voyelles += 1

        if character in consonnes:
            compteur_consonnes += 1
        
        if character in accents:
            lettres_francais_accents += 1
  
    return compteur_voyelles, compteur_consonnes, compteur_consonnes+compteur_voyelles,lettres_francais_accents

def algotri(liste_rank, real_liste): #trie la liste des unités en fonction de leur fréquence
    for a in range(len(liste_rank)):
        maximum = 0
        rank = 0
        for b in range(len(liste_rank) - a):
            if liste_rank[b] >= maximum:
                maximum = liste_rank[b]
                rank = b
        liste_rank[rank], liste_rank[len(liste_rank) - a - 1] = (liste_rank[len(liste_rank) - a - 1], liste_rank[rank])
        real_liste[rank], real_liste[len(real_liste) - a - 1] = (real_liste[len(real_liste) - a - 1], real_liste[rank])

    return liste_rank, real_liste


#############################################################################################

def rocket():
    #original = identity(pathfinder())
    original = identity("/home/constantin/github/text-analyzer/fasten.txt")

    compteur_lettres = 0

    for element in split(original):
        compteur_lettres += len(element)

    liste = algotri(doublon(ranker(gatherer(split(original))),gatherer(split(original)))[0],doublon(ranker(gatherer(split(original))),gatherer(split(original)))[1])[1] #liste propre des mots sans doublons
    rang = algotri(doublon(ranker(gatherer(split(original))),gatherer(split(original)))[0],doublon(ranker(gatherer(split(original))),gatherer(split(original)))[1])[0] #liste propre des occurences sans doublons
    mot_par_phrase = int(10000*len(split(original))/phrase_counter(original))/10000
    lettre_par_mot = int(10000*compteur_lettres/len(split(original)))/10000
    mot_uniques_sur_total = 100*int(10000*len(liste)/len(split(original)))/10000
    nombre_total_mots = len(split(original))
    taux_voyelles = int(1000000*vowel(original)[0]/vowel(original)[2])/10000
    taux_consonnes = int(1000000*vowel(original)[1]/vowel(original)[2])/10000
    liste_lettre = algotri(frequency(original), list(alphabet))[1] # liste triée dans l'ordre décroissant d'occurences des lettres de l'alphabet
    lettre_rang = algotri(frequency(original), list(alphabet))[0] # liste triée dans l'ordre décroissant d'occurences des fréquences des lettres de l'alphabet

    s = display_text.get()
    s += "\n Les mots ont en moyenne " + str(lettre_par_mot) + " lettres."
    
    if taux_consonnes < taux_voyelles:
        s += "\n Voyelles majoritaires ("+ str(taux_voyelles)+"% )"

    elif taux_voyelles == taux_consonnes:
        s += "\n Il y a le même taux de consonnes que de voyelles."

    else:
        s += "\n Consonnes majoritaires ( "+ str(taux_consonnes) +" % )"

    s += "\n ratio de voyelles accentuées : "+str(int(1000000*vowel(original)[3]/vowel(original)[2])/10000)+"%"
    s += "\n Les phrases contiennent "+str(mot_par_phrase)+" mots en moyenne."
    s += "\n Les mots ont en moyenne "+str(lettre_par_mot)+" lettres."
    s += "\n proportion de mots uniques : "+str(mot_uniques_sur_total)+" %"
    #print(len(liste)/len(split(original)))
    #print(len(split(original))/compteur_points)
    if mot_par_phrase >= 10 and mot_par_phrase <= 30 and nombre_total_mots >= 150:
        s += "\n Complexité de lecture texte BETA : " + str(int((mot_par_phrase**2)*lettre_par_mot*(mot_uniques_sur_total**3)/10**6))
        #print("nombre de mots : ", nombre_total_mots)

    else:
        s += "\n score non pertinent"

    display_text.set(s)

    return lettre_rang,liste_lettre,rang,liste

#btn = Button(window, text="Get path", command=pathfinder)
#btn.place(relx=0.5, rely=0.2, anchor=CENTER)

#print(rocket()[0],rocket()[1])

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

solution = rocket()
counter = 0
while solution[0][counter] == 0:
    del solution[0][counter]
    del solution[1][counter]

raffin_rang = []
raffin_liste = []

for a in range(20):
    raffin_liste.append(solution[3][-a-1])
    raffin_rang.append(solution[2][-a-1])

#print(raffin_rang,raffin_liste)

data1 = {'Lettres': solution[1],
         'Fréquences': solution[0]
        }
df1 = DataFrame(data1,columns=['Lettres','Fréquences'])



data2 = {'Mots': raffin_liste,
         'Nb': raffin_rang
        }
df2 = DataFrame(
    {"Nb":raffin_rang},
    index=raffin_liste)

#data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
#         'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
#        }
#df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])
#
#
#data3 = {'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],
#         'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
#        }  
#df3 = DataFrame(data3,columns=['Interest_Rate','Stock_Index_Price'])
# 
#####################################

figure1 = plt.Figure(figsize=(6,5), dpi=100)
ax1 = figure1.add_subplot(111)
ax1.scatter(df1['Lettres'],df1['Fréquences'], color = 'b')
scatter1 = FigureCanvasTkAgg(figure1, window)
scatter1.get_tk_widget().pack(side=LEFT, fill=BOTH)
ax1.legend(['Fréquences']) 
ax1.set_xlabel('Lettres')
ax1.set_title('Fréquence en fonction des lettres (%)')


#figure2 = plt.Figure(figsize=(6,5), dpi=100)
#ax2 = figure2.add_subplot(111)
#ax2.scatter(df2['Mots'],df2['Nb'], color = 'r')
#scatter2 = FigureCanvasTkAgg(figure2, window)
#scatter2.get_tk_widget().pack(side=RIGHT, fill=BOTH)
#ax2.legend(["Nombre d'apparitions"])
#ax2.set_xlabel('Mots')
#ax2.set_title("Mots les plus courants")


figure2 = plt.Figure(figsize=(6,5), dpi=100)
ax2 = figure2.add_subplot(111)
bar2 = FigureCanvasTkAgg(figure2, window)
bar2.get_tk_widget().pack(side=RIGHT, fill=BOTH)
#df2 = df2[['Mots','Nb']].groupby('Mots').sum()
df2.plot(kind='barh', legend=True, ax=ax2)
ax2.set_title("Mots les plus courants")

#figure2 = plt.Figure(figsize=(6,5), dpi=100)
#ax2 = figure2.add_subplot(111)
#bar2 = FigureCanvasTkAgg(figure2, window)
#bar2.get_tk_widget().pack(side=RIGHT, fill=BOTH)
#df2 = df2.plot(x="Mots",y=["Nb"],kind="barh")
#plt.show()
##df2.plot(kind='bar', legend=True, ax=ax2)
#ax2.set_title("Nombre d'apparitions des mots")
############################################
#figure2 = plt.Figure(figsize=(5,4), dpi=100)
#ax2 = figure2.add_subplot(111)
#line2 = FigureCanvasTkAgg(figure2, window)
#line2.get_tk_widget().pack(side=LEFT, fill=BOTH)
#df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
#df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
#ax2.set_title('Year Vs. Unemployment Rate')
#
#figure3 = plt.Figure(figsize=(5,4), dpi=100)
#ax3 = figure3.add_subplot(111)
#ax3.scatter(df3['Interest_Rate'],df3['Stock_Index_Price'], color = 'g')
#scatter3 = FigureCanvasTkAgg(figure3, window) 
#scatter3.get_tk_widget().pack(side=LEFT, fill=BOTH)
#ax3.legend(['Stock_Index_Price']) 
#ax3.set_xlabel('Interest Rate')
#ax3.set_title('Interest Rate Vs. Stock Index Price')
#############################################################################
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
#labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
#sizes = [15, 30, 45, 10]
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
#
#fig1, ax1 = plt.subplots()
#ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
#plt.show()
################################################################################

#batn = Button(window, text="launch engine", command=rocket)
##batn.grid(column=1,row=0)
#batn.place(relx=0.5, rely=0.2, anchor=CENTER)

window.mainloop()