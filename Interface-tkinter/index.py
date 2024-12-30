#importar bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

# Criar janela
janela = Tk()
janela.title('Sistema de cadastro')
janela.geometry('600x300')
janela.configure(background='white')
janela.resizable(width=False, height=False)
janela.attributes('-alpha', 0.9)
janela.iconbitmap(default='interface-tkinter/icons/LogoIcon.ico')


# ====== Carregar imagens ========
logo = PhotoImage(file='interface-tkinter/icons/logo.png')

# ================ Widgets ========================================
Leftframe = Frame(janela, width=200, height=300, bg='MIDNIGHTBLUE', relief='raised')
Leftframe.pack(side=LEFT)

RightFrame = Frame(janela, width=395, height=300, bg='MIDNIGHTBLUE', relief='raised')
RightFrame.pack(side=RIGHT)

LogoLabel = Label(Leftframe, image=logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text='Username:', font=('Century Gotic', 15) , bg='MIDNIGHTBLUE', fg='White')
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=110, y=105)

PassLabel = Label(RightFrame, text='Password:', font=('Century Gotic', 15), bg='MIDNIGHTBLUE', fg='White')
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show='*')
PassEntry.place(x=110, y=153)

# Botões
def Login():
    user = UserEntry.get()
    password = PassEntry.get()

    DataBaser.cursor.execute('''
    SELECT * FROM Users
    WHERE User = ? AND Password = ?
    ''', (user, password))
    print('Selecionou')
    
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if user in VerifyLogin and password in VerifyLogin:
            messagebox.showinfo(title='Login Info', message='Acesso Confirmado. Bem Vindo!')
    except TypeError:
        messagebox.showinfo(title='Login Infor', message='Acesso Negado. Verifique se está cadastrado no sistema!')

LoginButton = ttk.Button(RightFrame, text='Login', width=30, command=Login)
LoginButton.place(x=110, y=200)

def Register():
    #Removendo widgets
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Colocando widgets de Cadastro
    NameLabel = Label(RightFrame, text='Name:', font=('Century Gotic', 15), bg='MIDNIGHTBLUE', fg='White')
    NameLabel.place(x=5, y=5)

    NameEntry = ttk.Entry(RightFrame, width=37)
    NameEntry.place(x=70, y=10)

    EmailLabel = Label(RightFrame, text='Email:', font=('Century Gotic', 15), bg='MIDNIGHTBLUE', fg='White')
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=37)
    EmailEntry.place(x=70, y=60)

    def RegisterToDataBase():
        name = NameEntry.get()
        email = EmailEntry.get()
        user = UserEntry.get()
        password = PassEntry.get()

        if name == '' and email == '' and user == '' and password == '' or name == '' and email == '':
            messagebox.showerror(title='Register Error', message='Não Deixe Nenhum Campo Vazio. Preencha Todos os Campos.')
        else:
            DataBaser.cursor.execute('''
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            ''', (name, email, user, password))
            DataBaser.conn.commit()
            messagebox.showinfo(title='Register Info', message='Conta Criada com Sucesso!')


    Register = ttk.Button(RightFrame, text='Register', width=30, command=RegisterToDataBase)
    Register.place(x=110, y=200)

    def BacktoLogin():
        #Retirando os widgets de Cadastro
        NameLabel.place(x=5000)
        NameEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        BackButton.place(x=500)
        #Retornando os widgets
        LoginButton.place(x=110, y=200)
        RegisterButton.place(x=140, y=235)
    
    BackButton = ttk.Button(RightFrame, text='Back', width=20, command=BacktoLogin)
    BackButton.place(x=140, y=235)


RegisterButton = ttk.Button(RightFrame, text='Register', width=20, command=Register)
RegisterButton.place(x=140, y=235)

janela.mainloop()