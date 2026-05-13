# importar biblioteca
import sqlite3

# conectar banco de dados
conn = sqlite3.connect('atividade_info_cliente.db')

# executar o sql
cursor = conn.cursor()

cursor.execute('''
  
   CREATE TABLE IF NOT EXISTS clients (
               id INTEGER PRIMARY KEY AUTOINCREMENTE, 
               nome TEXT NOT NULL, email TEXT NOT NULL)
''')

conn.commit()

print("Atividade 1 concluida: Tabela criada")