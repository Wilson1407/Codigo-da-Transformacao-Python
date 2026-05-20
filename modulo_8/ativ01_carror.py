# Criar classe de carro com atributos como marca, modelo e método exibir_info()

# Implementação de herança: criar classe CarroEletrico que herda de Carro e adiciona autonomia_bateria.

# Use métodos especiais como __init__ e __str__ para personalizar a inicialização e exibição de objetos.

class Carro:
    def __init__(self, marca: str, modelo: str, ano: int = None):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self) -> str:
        parts = [f"Marca: {self.marca}", f"Modelo: {self.modelo}"]
        if self.ano is not None:
            parts.append(f"Ano: {self.ano}")
        return " | ".join(parts)
    
    def __str__(self) -> str:
        return self.exibir_info()
    
class CarroEletrico(Carro):
    def __init__(self, marca: str, modelo: str, autonomia_bateria_km: int, ano: int = None):
        super().__init__(marca, modelo, ano)
        self.autonomia_bateria_km = autonomia_bateria_km

    def exibir_info(self) -> str:
        base = super().exibir_info()
        return f"{base} | Autonomia (km): {self.autonomia_bateria_km}"
    
    def __str__(self) -> str:
        return self.exibir_info()
    
# Exemplo de uso:

if __name__ == "__main__":
    Carro = Carro("Totoyota", "Corolla", 2020)
    print(Carro)

    print(Carro.exibir_info())

    elet = CarroEletrico("Tesla", "Model 3", autonomia_bateria_km=500, ano=2022)
    print(elet)
    print(elet.exibir_info())