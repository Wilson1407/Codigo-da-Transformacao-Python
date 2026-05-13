class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100

    def fazer_chamada(self, custo_bateria):
        print(f"\n--- chamada no {self.modelo} ---")
        try:
            custo = int(custo_bateria)

            if custo > self.bateria:
                print("Erro: Bateria Insuficiente!")
            else:
                 self.bateria -= custo
                 print(f"Sucesso! Bateria atual: {self.bateria}%")

        except TypeError:
            print("Erro: O custo da bateria deve ser um número!")
        except ValueError:
            print("Erro: Digite um número inteiro válido!")
        finally:
            print("Sistema encerrada.")

meu_celular = Celular("Samsung", "S24")
meu_celular.fazer_chamada("muito")
meu_celular.fazer_chamada(30)
meu_celular.fazer_chamada(80)
print(f"\nbateria final: {meu_celular.bateria}%")