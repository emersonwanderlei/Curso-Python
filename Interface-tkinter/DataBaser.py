import sqlite3

conn = sqlite3.connect('UserData.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
''')

print('Conectado ao Banco de dados')

# cursor.execute('''
# INSERT INTO Users(Name) VALUES (Dev Gamer)
# ''') #INSERIR INFORMAÇÕES NA TABELA