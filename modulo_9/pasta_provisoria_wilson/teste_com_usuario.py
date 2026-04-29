class Celular:
    def __init__(self, marca, modelo):
        self.marca, self.modelo = marca, modelo
        self.bateria = 100

    def fazer_chamada(self, custo_bateria):
        print(f"\n--- chamada no {self.modelo} ---")
        try:
            self.bateria -= custo_bateria
        except TypeError:
            print("Erro: O custo da bateria deve ser um número!")
        else:
            print(f"Sucesso! bateria atual: {self.bateria}%")
        finally:
            print("Sistema finalizado.")

meu_celular = Celular("Samsung", "S24")
meu_celular.fazer_chamada("muito")