#!python3

import tkinter as tk
from tkinter import *
window=tk.Tk()
window.geometry('260x140')

dogphoto = PhotoImage(file = 'dog.png')
photo=tk.Label(window, image=dogphoto)
poc=tk.Label(window, image=dogphoto)

poc=tk.Label(window, text='Pochacco!')
label1=tk.Label(window,text='A cuddly little puppy! This is from the same /n creaters who brought you Keropi and Kero', bg = "#87ceeb")


window.mainloop()
