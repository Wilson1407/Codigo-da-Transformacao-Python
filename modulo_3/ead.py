while True:
    print("\n--- MENU INTERATIVO ---")
    print("1 - Classificar Idade")
    print("2 - Soma")
    print("3 - Subtração")
    print("4. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        idade = int(input("Digite a idade:"))
        if idade < 13: 
            print("Categoria: Criança")
        elif idade <18:
            print("Categoria: Adolescente")
        elif idade < 60:
            print("Categoria: Adulto")
        else: 
            print("Categoria: Idoso")

    elif opcao == "2":
        n1 = float(input("Primeiro número: "))
        n2 = float(input("Segundo número: "))
        print(f"resultado da Soma: {n1 + n2}")

    elif opcao == "3":
        n1 = float(input("Primeiro número: "))
        n2 = float(input("Segundo número: "))
        print(f"Resultado da Subtração: {n1 - n2}")

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")
