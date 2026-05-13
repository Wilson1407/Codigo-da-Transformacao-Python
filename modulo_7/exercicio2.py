from faker import Faker
from datetime import datetime

fake = Faker('pt_BR')

def gerar_dados():

    return {
        "nome": fake.name(),
        "email": fake.email(),
        "cidade": fake.city(),
        "data": datetime.now().strftime("%d/&m/%Y &H:%M")
    }

def main():

    print(f"--- Gerador de Dados ({datetime.now().strftime('%H:%M')}")

    for i in range(1, 4):
        dados = gerar_dados()
        print(f"Usuário {i}:")
        print(f" Nome: {dados['nome']}")
        print(f" Email: {dados['email']}")
        print(f" Cidade: {dados['cidade']}")
        print(f" Hora: {dados['data']}:")
        print("-" * 30)

if __name__ == "__main__":
    main()
        