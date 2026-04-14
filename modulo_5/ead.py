# Função que recebe um nome e imprime uma saudação personalizada
def saudacao(nome):
    print(f"Olá {nome}! Bem-vindo ao curso de Python!")

# Função para calcular a média de um aluno e determinar se foi aprovado ou reprovado
def calcular_media(notas):
    media = sum(notas) / len(notas)

    if media >= 7:
        print(f"Média: {media:.2f} - Aprovado!")
    else:
         print(f"Média: {media:.2f} - Reprovado!")

# Função que recebe uma lista de número e retorna o maior e o menor
def encontrar_extremos(numeros):
    if len(numeros) == 0:
        print("lista vazia")
    else:
        maior = max(numeros)
        menor = min(numeros)
        print(f"Maior: {maior}")
        print(f"Menor: {menor}")

# Sistema de login verificando usuário e sennha
def sistema_login(usuario, senha):
    usuarios = {
        "Lucas": "12345",
        "Maria": "abcde",
        "João": "qwert"
    }
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

# Testes fora das funções

saudacao("Lucas")

calcular_media([8, 7, 9, 6])

encontrar_extremos([5, 3, 8, 1, 4])

sistema_login("Lucas", "12345")