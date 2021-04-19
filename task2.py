#!python3

import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Window")
window.geometry("600x200")

#first
dogphoto = PhotoImage(file = "dog.png" )
label1 = tk.Label(window, image=dogphoto)
button1 = tk.Button(window,text="Search by name")
entry1 = tk.Entry(window)
label2 = tk.Label(window, text="Client Database")




label1.grid(row = 1, column = 1, rowspan = 3)
button1.grid(row = 1,column = 4)
entry1.grid(row = 1, column = 5)
label2.grid(row = 2, column = 3)

#middle
name = tk.Label(window, text = "Name")
Nentry = tk.Entry(window, borderwidth = 3)
typeo = tk.Label(window, text = "Type")
Tentry = tk.Entry(window, borderwidth = 3)
breed = tk.Label(window, text = "Breed")
Bentry = tk.Enrty(window, borderwidth = 3)
owner = tk.Label(window, text = "Name")
Oentry = tk.Entry(window, borderwidth = 3)
bd = tk.Label(window, text = "Birthdate")
BDentry = tk.Entry(window, borderwidth = 3)

name.grid(row = 4,column = 1)
Nentry.grid(row = 5,column = 1)
typeo.grid(row = 4,column = 2)
Tentry.grid(row = 5,column = 2)
breed.grid(row = 4,column = 3)
Bentry.grid(row = 5,column = 3)
owner.grid(row = 4,column = 4)
Oentry.grid(row = 5,column = 5)
bd.grid(row = 4,column = 5)
BDentry.grid(row = 5,column = 5)

#last
button2 = tk.Button(window, text=" >Previous")
save = tk.Button(window, text = "Save Entry")
button3 = tk.Button(window, text = "Next >")

button2.grid(row = 6, column = 1, sticky = W)
save.grid(row = 6, column = 3)
button3.grid (row = 6, column = 5 , sticky = E)

window.mainloop()




