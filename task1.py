#!python3

import tkinter as tk
from tkinter import *
from tkinter import Tk

window = tk.Tk()
window.title("Calculator")
window.geometry("500x20")

e1 = tk.Entry(window,width = 30)
l1 = tk.Label(window,text = "X")
e2 = tk.Entry(window,width = 30)
l2 = tk.Label(window,text = "=")
e3 = tk.Enrty(window,width = 20)

e1.grid(row = 1,column = 1)
l1.grid(row = 1,column = 2)
e2.grid(row = 1,column = 3)
l2.grid(row = 1,column = 4)
e3.grid(row = 1,column = 5)

window.mainloop()


