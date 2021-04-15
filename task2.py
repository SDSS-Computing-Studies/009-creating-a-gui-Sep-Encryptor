import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("600x200")

label1 = tk.Label(window,text="Client Database")
label2 = tk.Label(window,text="Name")
label3 = tk.Label(window,text="Type")
label4 = tk.Label(window,text="Breed")
label5 = tk.Label(window,text="Owner")
label6 = tk.Label(window,text="Birthdate")


dogphoto = PhotoImage(file="dog.png")
label8 = tk.Label(window, image=dogphoto)

button1 = tk.Button(window,text="<Previous")
button2 = tk.Button(window,text="Save Entry")
button3 = tk.Button(window,text="Next>")

button7 = tk.Button(window,text="search by name",width=15)

entry1 = tk.Entry(window,text="", width=15)
entry2 = tk.Entry(window,text="", width=15)
entry3 = tk.Entry(window,text="", width=15)
entry4 = tk.Entry(window,text="", width=15)
entry5 = tk.Entry(window,text="", width=15)
entry6 = tk.Entry(window,text="", width=25)


button1.place(x=10,y=175)
button2.place(x=270,y=175)
button3.place(x=550,y=175)

entry1.place(x=10,y=150)
entry2.place(x=130,y=150)
