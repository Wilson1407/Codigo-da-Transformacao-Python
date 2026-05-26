import sqlite3

# 1. Conectar ao banco de dados (será criado na memória para ser simples e rápido)
conexao = sqlite3.connect(':memory:')
cursor = conexao.cursor()

# 2. CRIAR TABELA
cursor.execute('''
    CREATE TABLE Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

print("--- 1. CREATE (Inserir registros) ---")
# Inserindo dados de exemplo
cursor.execute("INSERT INTO Clientes (nome, email) VALUES ('Alice Silva', 'alice@email.com')")
cursor.execute("INSERT INTO Clientes (nome, email) VALUES ('Bruno Costa', 'bruno@email.com')")
cursor.execute("INSERT INTO Clientes (nome, email) VALUES ('Amanda Lima', 'amanda@email.com')")
conexao.commit() # Salva as alterações
print("Clientes inseridos com sucesso.")


print("\n--- 2. READ (Consultar todos os registros) ---")
cursor.execute("SELECT * FROM Clientes")
for cliente in cursor.fetchall():
    print(cliente)


print("\n--- 3. UPDATE (Atualizar registro) ---")
# Alterando o email do Bruno (id = 2)
cursor.execute("UPDATE Clientes SET email = 'bruno.novo@email.com' WHERE id = 2")
conexao.commit()

# Mostrando o Bruno atualizado
cursor.execute("SELECT * FROM Clientes WHERE id = 2")
print("Após atualização:", cursor.fetchone())


print("\n--- 4. DELETE (Deletar registro) ---")
# Deletando a Alice (id = 1)
cursor.execute("DELETE FROM Clientes WHERE id = 1")
conexao.commit()

# Listando para ver que a Alice sumiu
cursor.execute("SELECT * FROM Clientes")
print("Após deleção:")
for cliente in cursor.fetchall():
    print(cliente)


print("\n--- CONSULTA FILTRADA (Nomes começando com 'A') ---")
# O '%' serve para indicar que pode vir qualquer texto depois da letra A
cursor.execute("SELECT * FROM Clientes WHERE nome LIKE 'A%'")
resultados = cursor.fetchall()

if resultados:
    for cliente in resultados:
        print(cliente)
else:
    print("Nenhum cliente encontrado com a letra 'A'.")

# Fechar a conexão com o banco
conexao.close()