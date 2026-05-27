
# Teste uma função de soma usando o módulo unittest
import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma_positiva(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativa(self):
        self.assertEqual(soma(-2, -3), -5)

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

    # Crie testes para uma classe Calculadora com métodos como somar e dividir.

class Calculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b
    
class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calculadora.somar(2, 3), 5)

    def test_dividir(self):
        self.assertEqual(self.calculadora.dividir(10, 2), 5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            self.calculadora.dividir(10, 0)

if __name__ == '__main__':    unittest.main()

# Valide entradas inváidas (ex: divisão por zero deve lançar uma exceção)
