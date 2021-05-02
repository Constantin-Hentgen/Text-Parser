from tkinter import *
from tkinter import filedialog
import os

window = Tk()

window.title("Text Analyzer by Constantin")
window.geometry('500x200')

display_text = StringVar()
lbl = Label(window, textvariable=display_text)
lbl.place(relx=0.5, rely=0.6, anchor=CENTER)

#txt = Entry(window,width=10)
#txt.grid(column=1, row=0)

def pathfinder():
    file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
    s = display_text.get()
    s += "\n"+str(file)
    display_text.set(s)

def rocket():
    os.system(str("python3 engine.py"))

btn = Button(window, text="Get path", command=pathfinder)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)

batn = Button(window, text="launch engine", command=rocket)
batn.place(relx=0.5, rely=0.4, anchor=CENTER)

window.mainloop()