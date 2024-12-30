from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep as sp


# Criar janela
janela = Tk()
janela.title('SISCAU - LOGIN')
janela.geometry('300x300')
janela.resizable(width=FALSE, height=FALSE)

# Criar widgtes

UpFrame = Frame(janela, width=300, height=100, bg='Black')
UpFrame.grid(row=0, column=0)

DownFrame = Frame(janela, width=300, height=200, bg='MIDNIGHTBLUE')
DownFrame.grid(row=1, column=0, padx=0, pady=5)

TitleLabel = Label(UpFrame, text='Siscau', font=('Century Gotic', 20), bg='Black', fg='White')
TitleLabel.place(x=100, y=30)

UserLabel = ttk.Label(DownFrame, text='Login:', font=('Century Gotic', 15), background='MIDNIGHTBLUE', foreground='White')
UserLabel.place(x=15, y=30)

UserEntry = ttk.Entry(DownFrame, width=32, background='MIDNIGHTBLUE')
UserEntry.place(x=70, y=32)

PassLabel = Label(DownFrame, text='Senha:', font=('Century Gotic', 15), background='MIDNIGHTBLUE', foreground='White')
PassLabel.place(x=15, y=70)

PassEntry = ttk.Entry(DownFrame, width=30, background='MIDNIGHTBLUE', show="*")
PassEntry.place(x=80, y=72)

def EntrarNoSiscau():
    EnterButton.place(x=5000)

    usuario = UserEntry.get()
    senha = PassEntry.get()


    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    navegador = webdriver.Chrome(options=options)

    navegador.get('https://auth.2cta.eb.mil.br:6082/php/uid.php?vsys=1&rule=1&url=http://intranet.2cta.eb.mil.br')
    navegador.find_element(By.CSS_SELECTOR, '[id="user"]').send_keys(usuario)
    sp(0.5)
    navegador.find_element(By.CSS_SELECTOR, '[id="passwd"]').send_keys(senha)
    sp(0.5)
    navegador.find_element(By.CSS_SELECTOR, '[id="submit"]').click()

    messagebox.showinfo(title='Infor', message='Conectado com sucesso!')

    # ConectadoButton = Label(DownFrame, text='Conectado', font=('Century Gotic', 15), bg='MIDNIGHTBLUE', fg='Green')
    # ConectadoButton.place(x=100, y=110)

    def voltarParaLogin():
        # ConectadoButton.place(x=5000)
        RetornarLogin.place(x=5000)
        EnterButton.place(x=95, y=110)

        PassLabel = Label(DownFrame, text='Senha:', font=('Century Gotic', 15), background='MIDNIGHTBLUE', foreground='White')
        PassLabel.place(x=15, y=70)

        PassEntry = ttk.Entry(DownFrame, width=30, background='MIDNIGHTBLUE', show="*")
        PassEntry.place(x=80, y=72)

    RetornarLogin = Button(DownFrame, width=20, text='Voltar', command=voltarParaLogin)
    RetornarLogin.place(x=95, y=150)

EnterButton = Button(DownFrame, text='Login', width=20, command=EntrarNoSiscau)
EnterButton.place(x=95, y=110)


janela.mainloop()