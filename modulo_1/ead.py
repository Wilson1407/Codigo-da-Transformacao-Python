tarefas = []

while True:
    print("\n--- MENU ---")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opção:")

    if opcao == "1":
        tarefa = input('Escolha uma opção')

        if opcao == "1":
            tarefa = input("Digite a tarefa: ")
            tarefas.append(tarefa)
            print("Tarefa adicionada!")

        elif opcao == "2":
            if len(tarefas) == 0:
                print("Nenhuma tarefa cadastrada.")
            else:
                for i in range(len(tarefas)):
                    print(i, "-", tarefas[i])

        elif opcao == "3":
            for i in range(len(tarefas)):
                print(i, "-", tarefas[i])

            numero = int(input("Digite o número da tarefa para remover: "))
            tarefas.pop(numero)
            print("Tarefa removida!")

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção Inválida!")