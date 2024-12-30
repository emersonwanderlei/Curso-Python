#Importando SQLite
import sqlite3 as lite


# criando conexão
con = lite.connect('Interface-tkinter/CRUD/dados.db')

with con:
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE formulario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    telefone TEXT,
    dia_em DATE,
    estado TEXT,
    assunto TEXT)

''')

print('Conectado!')