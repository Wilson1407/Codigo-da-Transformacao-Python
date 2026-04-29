class Celular:
    def __init__(self, marca, modelo):
        self.marca, self.modelo = marca, modelo
        self.bateria = 100
    def fazer_chamada(self, duracao):
        try:
            gasto = int(duracao) * 2
            if self.bateria >= gasto:
                print(f"chamada de {duracao} min feita! Bateria: {self.bateria}%")
            else:
                print("Bateria insuficiente.")
        except ValueError:
            print("Erro: A duração deve ser um número inteiro!")

meu_celular = Celular("Xiami", "Redmi 12")
meu_celular.fazer_chamada("Dez")# Teste de erro
