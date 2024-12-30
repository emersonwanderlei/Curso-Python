from tkinter import *
from tkinter import ttk
from tkinter import messagebox

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

# Criar janela
window = Tk()
window.title('')
window.geometry('1043x453')
window.configure(background=co9)
window.resizable(width=FALSE, height=FALSE)

# Widgets

upFrame = Frame(window, width=310, height=50, bg=co2, relief='flat')
upFrame.grid(row=0, column=0,)

lefFrame = Frame(window, width=310, height=403, bg='Blue', relief='flat')
lefFrame.grid(row=1, column=0, padx=0, pady=1, sticky='NSEW')

rightFrame = Frame(window, width=588, height=403, bg='Red', relief='flat')
rightFrame.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky='NSEW')

#=========UpFrame=============
titleUpFrame = Label(upFrame, text='Cadastro de Secretário', font=('', 15),  bg='Green', fg='White')
titleUpFrame.place(x=35, y=20)

#=========leftFrame==========
namelabel = Label(lefFrame, text='Nome:', font=('',15), bg='Blue', fg='White')
namelabel.place(x=20, y=30)

nameEntry = ttk.Entry(lefFrame, width=30)
nameEntry.place(x=80, y=35)

#=========rightFrame==========

window.mainloop()