# Lista de Compras

compras = []
while True:
    print(f"\nLista atual: {compras}")
    item = input("Digite o item para adicionar, 'remover' [nome]' para tirar ou 'sair': ").strip()

    if item.lower() == 'sair':
        break
    elif item.lower().startswith("remover "):
        alvo = item.split(" ", 1)[1]
        if alvo in compras:
            compras.remove(alvo)
        else:
            print("Item não encontrado.")
    else:
        compras.append(item)

# Dados de Aluno

aluno = {
    "nome": "Lucas",
    "idade": 21,
    "Curso": "Engenharia de Software",
    "media": 8.5
}

print("Dados do Aluno:")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")

# Pares e Ímpares

numeros = [12, 7, 5, 18, 22, 9, 33, 40]
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")

# Agenda de Contatos

agenda = {}

while True:
    print("\n--- AGENDA ---")
    op = input("1. Adicionar/Editar\n2. Ver Todos\n3. Sar\nEscolha: ")

    if op == "1":
        nome = input("Nome: ")
        tel = input("Telefone: ")
        agenda[nome] = tel
        print("Contato salvo!")
    elif op == "2":
        for nome, tel in agenda.items():
            print(f"Nome: {nome} | Tel: {tel}")
    elif op == "3":
        break