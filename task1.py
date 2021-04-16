#!python3

import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()

l1 = tk.Label(window, text="x")
b1 = tk.Button(window, text="=")
e1 = tk.Enrty(window, borderwidth = 3)
e3 = tk.Enrty(window, borderwidth = 3)

e1.grid (row = 1, column = 1)
l1.grid (row = 1, column = 2)
e2.grid (row = 1, column = 3)
b1.grid (row = 1, column = 4)
e3.grid (row = 1, column = 5)
 
window.mainloop()
