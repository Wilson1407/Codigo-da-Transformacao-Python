

meu_celular = Celular("Xiami", "Redmi 12")
meu_celular.fazer_chamada("Dez")# Teste de erro
meu_celular.fazer_chamada(10)

class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100

    def fazer_chamada(self, duracao):
        try:
            duracao_int = int(duracao)
            gasto = duracao_int * 2

            if self.bateria >= gasto:
                self.bateria -= gasto
                print(f"Chamada de {duracao_int} min feita! Bateria restante: {self.bateria}%")
            else:
                print("Bateria insuficiente.")

        except ValueError:
            print("Erro: A duração deve ser um número inteiro!")

meu_celular = Celular("Xiami", "Redmi 12")
meu_celular.fazer_chamada("Dez")# Teste de erro
meu_celular.fazer_chamada(10)
print(f"Bateria final: {meu_celular.bateria}%")