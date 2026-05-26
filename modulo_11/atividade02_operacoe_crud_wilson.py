# importar biblioteca
import sqlite3

# conectar banco de dados
conn = sqlite3.connect('atividade_info_cliente.db')

# executar o sql
cursor = conn.cursor()

cursor.execute('''

    INSERT INTO clientes (nome, email) VALUES
                
    ('Leticia Dorta', 'joao.silva@mail.com'),
               
    ('Ayla Sousa', 'maria.oliveira@mail.com'),
               
    ('Aurélio Dinis ', 'carlos.santos@mail.com'),
               
    ('Igor Freitas', 'joao.silva@mail.com'),
               
    ('Ana Cecília ', 'maria.oliveira@mail.com'),
               
    ('Ana Alves', 'carlos.santos@mail.com'),
    
    ('André Ramalho', 'joao.silva@mail.com'),
               
    ('Maria Helena', 'maria.oliveira@mail.com'),
               
    ('Antônio Fernandes', 'carlos.santos@mail.com'),
    
    ('Ana Clara Machado', 'joao.silva@mail.com'),
               
    ('Vitor Bispo Cruz', 'maria.oliveira@mail.com'),
               
    ('Pedro Henrique', 'carlos.santos@mail.com')
               

''')

cconn.commit()

cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?)', clientes)
conn.commit()
print("Sucesso: Novos clientes inseridos na base de dados.")

# --- CONSULTAR (Read) ---
print("\n--- LISTA DE CLIENTES ATUAIS ---")
cursor.execute("SELECT * FROM clientes")
for cliente in cursor.fetchall():
    print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")

# --- ATUALIZAR (Update) ---
# Vamos atualizar o email do Igor Freitas
cursor.execute("UPDATE clientes SET email = ? WHERE nome = ?", ('igor.freitas@mail.com', 'Igor Freitas'))
print("\nSucesso: Email do Igor Freitas atualizado.")

# --- DELETAR (Delete) ---
# Vamos deletar o registro do Leticia Dorta
cursor.execute("DELETE FROM clientes WHERE nome = ?", ('Leticia Dorta',))
print("Sucesso: Registro de Leticia Dorta removido.")

conn.commit()


print("Atividade 2 concluída: Operações CRUD realizadas.")

print('Atividade 2 concluída: Dados inseridos.')