def aula_tratamento_erros():
    print("--- Desafio 1: Divisão ---")
    try:
        numerador = int(input("Digita o denominador: "))
        denominador = int(input("Digita o denominador: "))
        resultado = numerador / denominador

    except ValueError:
        print("Erro: Não pode dividir por zero.")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
    else:
        print(f"Sucesso! Resultado: {resultado}")
    finally:
        print("--- Fim da Divisão ---")
aula_tratamento_erros()