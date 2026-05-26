import sqlite3

def inicializar_banco():
    """Cria o banco de dados e a tabela se não existirem."""
    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pendente'
        )
    ''')
    conexao.commit()
    conexao.close()

def adicionar_tarefa(titulo):
    """Adiciona uma nova tarefa ao banco."""
    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Tarefas (titulo) VALUES (?)", (titulo,))
    conexao.commit()
    conexao.close()
    print(f"\n[Sucesso] Tarefa '{titulo}' adicionada!")

def visualizar_tarefas():
    """Lista todas as tarefas cadastradas."""
    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Tarefas")
    tarefas = cursor.fetchall()
    conexao.close()

    print("\n=== SUAS TAREFAS ===")
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for tarefa in tarefas:
            # tarefa[0] é o ID, tarefa[1] é o Título, tarefa[2] é o Status
            print(f"[{tarefa[0]}] {tarefa[1]} - Status: {tarefa[2]}")
    print("====================")

def excluir_tarefa(id_tarefa):
    """Exclui uma tarefa com base no ID fornecido."""
    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    
    # Verifica se o ID realmente existe antes de deletar
    cursor.execute("SELECT * FROM Tarefas WHERE id = ?", (id_tarefa,))
    if cursor.fetchone() is None:
        print(f"\n[Erro] Não existe tarefa com o ID {id_tarefa}.")
    else:
        cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id_tarefa,))
        conexao.commit()
        print(f"\n[Sucesso] Tarefa {id_tarefa} excluída com sucesso!")
        
    conexao.close()

# --- FLUXO PRINCIPAL DO PROGRAMA ---
def menu():
    inicializar_banco()
    
    while True:
        print("\n--- GERENCIADOR DE TAREFAS ---")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Excluir Tarefa")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == '1':
            titulo = input("Digite o título da tarefa: ").strip()
            if titulo:
                adicionar_tarefa(titulo)
            else:
                print("\n[Erro] O título da tarefa não pode ser vazio.")
                
        elif opcao == '2':
            visualizar_tarefas()
            
        elif opcao == '3':
            visualizar_tarefas() # Mostra as tarefas para o usuário ver os IDs
            try:
                id_tarefa = int(input("Digite o ID da tarefa que deseja excluir: "))
                excluir_tarefa(id_tarefa)
            except ValueError:
                print("\n[Erro] Por favor, digite um número válido para o ID.")
                
        elif opcao == '4':
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\n[Erro] Opção inválida! Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    menu()