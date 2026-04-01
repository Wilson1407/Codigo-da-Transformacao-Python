import datetime

nome = input("Qual é o seu nome?")

hora_atual = datetime.datetime.now().strftime("%H:%M:%S")

print(f"Olá, {nome}! Agora são {hora_atual}. Seja bem-vindo!")